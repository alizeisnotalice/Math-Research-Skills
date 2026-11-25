#!/usr/bin/env python3
"""Bounded Apple Metal numerical jobs; never silently fall back to CPU."""
from __future__ import annotations

import argparse
import json
import math
import os
from pathlib import Path
import sys
import tempfile
import time

if "torch" in sys.modules and os.environ.get("PYTORCH_ENABLE_MPS_FALLBACK") != "0":
    raise RuntimeError("Set PYTORCH_ENABLE_MPS_FALLBACK=0 before importing torch.")
os.environ["PYTORCH_ENABLE_MPS_FALLBACK"] = "0"
os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")

MAX_REQUEST_BYTES = 16 * 1024 * 1024
MAX_INLINE_ELEMENTS = 100_000
MAX_JOB_BYTES = 512 * 1024 * 1024


def write_json(path, value):
    """Atomic complete report, allowing callers to reject stale/partial results."""
    path = Path(path).absolute()
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(value, ensure_ascii=False, allow_nan=False, indent=2) + "\n"
    fd, name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w") as out:
            out.write(text)
            out.flush()
            os.fsync(out.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def load_backend():
    import numpy as np
    import torch
    if not torch.backends.mps.is_built() or not torch.backends.mps.is_available():
        raise RuntimeError("Apple Metal/MPS unavailable in this Python; no CPU fallback.")
    return np, torch


def probe():
    np, torch = load_backend()
    x = torch.arange(16, dtype=torch.float32, device="mps")
    y = x.square()
    torch.mps.synchronize()
    ok = bool(np.array_equal(y.cpu().numpy(), np.arange(16, dtype=np.float32) ** 2))
    return {"ok": ok, "route": "native-pytorch-metal", "device": str(y.device),
            "python": sys.executable, "python_version": sys.version.split()[0],
            "torch": torch.__version__, "numpy": np.__version__,
            "mps_built": torch.backends.mps.is_built(), "mps_available": True,
            "cpu_fallback_enabled": False, "dtype": "float32"}


def read_array(spec, np, allow_loss, dtype="float32"):
    if not isinstance(spec, dict):
        raise ValueError("Each input must be a data/shape or npy specification.")
    if set(spec) in ({"npy"}, {"mat", "variable"}):
        kind = "npy" if "npy" in spec else "mat"
        path = Path(spec[kind])
        if not path.is_absolute() or path.suffix != "." + kind:
            raise ValueError("Array input must be an absolute .npy or .mat file.")
        if path.stat().st_size > MAX_JOB_BYTES:
            raise ValueError("Input exceeds the bounded job budget.")
        if kind == "npy":
            original = np.load(path, allow_pickle=False, mmap_mode="r")
        else:
            from scipy.io import loadmat
            name = spec["variable"]
            if not isinstance(name, str) or not name.isidentifier() or name.startswith("_"):
                raise ValueError("MAT variable must be a public identifier.")
            original = loadmat(path, variable_names=[name], verify_compressed_data_integrity=True)[name]
    elif set(spec) == {"data", "shape"}:
        shape = spec["shape"]
        if (not isinstance(shape, list) or not 1 <= len(shape) <= 2
                or any(type(n) is not int or n < 1 for n in shape)):
            raise ValueError("shape must contain one or two positive integers.")
        if not isinstance(spec["data"], list) or len(spec["data"]) != math.prod(shape):
            raise ValueError("data must be flat in C/row-major order and match shape.")
        original = np.asarray(spec["data"]).reshape(shape)
    else:
        raise ValueError("Use exactly {data,shape}, {npy}, or {mat,variable}; no executable inputs.")
    if (original.ndim not in (1, 2) or original.size == 0
            or original.dtype.kind not in "fiu" or original.dtype.itemsize > 8):
        raise ValueError("Only nonempty dense real numeric vectors/matrices are supported.")
    if original.nbytes > MAX_JOB_BYTES // 4:
        raise ValueError("Input exceeds the bounded job budget.")
    target = np.dtype(dtype)
    if target not in (np.dtype("float32"), np.dtype("float64")):
        raise ValueError("Only float32/float64 computation is supported.")
    if not np.can_cast(original.dtype, target, casting="safe") and not allow_loss:
        raise ValueError(str(target) + " conversion requires allow_precision_loss=true.")
    if original.dtype.kind in "iu" and (np.abs(original.astype(float)) > 2**53).any():
        raise ValueError("Large exact integers need an exact CPU tool, not this floating-point bridge.")
    if not np.isfinite(original).all():
        raise ValueError("Inputs must be finite.")
    with np.errstate(over="raise", invalid="raise"):
        a = np.array(original, dtype=target, order="C", copy=True)
    rounding = float(np.max(np.abs(original.astype(np.float64) - a.astype(np.float64))))
    return a, {"shape": list(a.shape), "original_dtype": str(original.dtype),
               "compute_dtype": str(target), "input_max_abs_rounding": rounding}


def run_job(request):
    started = time.perf_counter()
    if not isinstance(request, dict):
        raise ValueError("Request must be an object.")
    allowed = {"operation", "dtype", "allow_precision_loss", "inputs", "output_npy", "output_mat",
               "rtol", "atol"}
    if set(request) - allowed:
        raise ValueError("Unknown request fields: " + str(sorted(set(request) - allowed)))
    if request.get("dtype") != "float32":
        raise ValueError("This Metal bridge requires explicit dtype=float32; no float64 GPU claim.")
    if type(request.get("allow_precision_loss", False)) is not bool:
        raise ValueError("allow_precision_loss must be boolean.")
    op = request.get("operation")
    if op not in ("matmul", "sin_exp", "sum"):
        raise ValueError("Supported operations: matmul, sin_exp, sum.")
    specs = request.get("inputs")
    expected = {"a", "b"} if op == "matmul" else {"x"}
    if not isinstance(specs, dict) or set(specs) != expected:
        raise ValueError("Input keys must be " + str(sorted(expected)))
    np, torch = load_backend()
    arrays, input_info = {}, {}
    for name, spec in specs.items():
        arrays[name], input_info[name] = read_array(spec, np, request.get("allow_precision_loss", False))
    if op == "matmul":
        a, b = arrays["a"], arrays["b"]
        if a.ndim != 2 or b.ndim != 2 or a.shape[1] != b.shape[0]:
            raise ValueError("matmul requires compatible 2D matrices.")
        out_shape = (a.shape[0], b.shape[1])
    elif op == "sin_exp":
        out_shape = arrays["x"].shape
    else:
        out_shape = ()
    elements = sum(a.size for a in arrays.values()) + math.prod(out_shape)
    estimated = elements * 24  # host input, fp64 reference, GPU, output, scratch allowance
    if estimated > MAX_JOB_BYTES:
        raise ValueError("Estimated job memory exceeds 512 MiB; split the task.")
    if "output_npy" in request and "output_mat" in request:
        raise ValueError("Choose either output_npy or output_mat.")
    output_kind = "mat" if "output_mat" in request else "npy"
    output_path = request.get("output_" + output_kind)
    if output_path is not None:
        output_path = Path(output_path)
        if not output_path.is_absolute() or output_path.suffix != "." + output_kind:
            raise ValueError("Output must be an absolute path with the correct extension.")
        if any(k in s and Path(s[k]).resolve() == output_path.resolve()
               for s in specs.values() for k in ("npy", "mat")):
            raise ValueError("Output must not overwrite an input.")
        if output_path.exists():
            raise ValueError("Choose a new output path; outputs are never overwritten.")
    elif math.prod(out_shape) > MAX_INLINE_ELEMENTS:
        raise ValueError("Large outputs require output_npy/output_mat instead of JSON data.")
    rtol = request.get("rtol", 5e-4)
    atol = request.get("atol", 5e-5)
    if any(type(v) not in (int, float) or not math.isfinite(v) or v < 0 for v in (rtol, atol)):
        raise ValueError("rtol/atol must be finite nonnegative numbers.")
    with torch.inference_mode():
        t = time.perf_counter()
        gpu = {k: torch.from_numpy(v).to("mps") for k, v in arrays.items()}
        torch.mps.synchronize()
        upload_s = time.perf_counter() - t
        t = time.perf_counter()
        if op == "matmul":
            result = gpu["a"] @ gpu["b"]
        elif op == "sin_exp":
            result = torch.sin(gpu["x"]) * torch.exp(-gpu["x"].square())
        else:
            result = torch.sum(gpu["x"])
        torch.mps.synchronize()
        compute_s = time.perf_counter() - t
        if result.device.type != "mps":
            raise RuntimeError("Operation did not return an MPS tensor.")
        device = str(result.device)
        t = time.perf_counter()
        host = result.cpu().numpy().copy()
        download_s = time.perf_counter() - t
    t = time.perf_counter()
    doubles = {k: v.astype(np.float64) for k, v in arrays.items()}
    if op == "matmul":
        reference = doubles["a"] @ doubles["b"]
    elif op == "sin_exp":
        reference = np.sin(doubles["x"]) * np.exp(-doubles["x"] ** 2)
    else:
        reference = np.sum(doubles["x"], dtype=np.float64)
    error = np.abs(host.astype(np.float64) - reference)
    finite = bool(np.isfinite(host).all() and np.isfinite(reference).all())
    passed = finite and bool(np.all(error <= atol + rtol * np.abs(reference)))
    rel_l2 = float(np.linalg.norm(error.ravel()) /
                   max(float(np.linalg.norm(np.asarray(reference).ravel())), np.finfo(float).tiny))
    report = {"ok": passed, "operation": op, "route": "python-metal-bridge",
              "device": device, "dtype": str(host.dtype), "torch": torch.__version__,
              "cpu_fallback_enabled": False, "inputs": input_info,
              "estimated_working_bytes": estimated,
              "timings_s": {"upload": upload_s, "gpu_compute_synchronized": compute_s,
                            "download": download_s, "cpu_reference": time.perf_counter() - t},
              "verification": {"passed": passed, "finite": finite,
                  "reference": "NumPy float64 on the same float32-rounded inputs",
                  "rtol": rtol, "atol": atol, "max_abs_error": float(np.max(error)) if finite else None,
                  "relative_l2_error": rel_l2 if math.isfinite(rel_l2) else None,
                  "evidence_class": "numerical-check-not-rigorous-proof"},
              "result": {"shape": list(host.shape), "order": "C"}}
    if passed:
        if output_path is not None:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with output_path.open("xb") as f:
                if output_kind == "npy":
                    np.save(f, host, allow_pickle=False)
                else:
                    from scipy.io import savemat
                    savemat(f, {"result": host}, do_compression=False)
            report["result"][output_kind] = str(output_path)
            if output_kind == "mat":
                report["result"]["variable"] = "result"
        else:
            report["result"]["data"] = host.ravel(order="C").tolist()
    report["timings_s"]["job_excluding_report_write"] = time.perf_counter() - started
    return report


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("command", choices=("probe", "run"))
    p.add_argument("--request", type=Path)
    p.add_argument("--report", type=Path, required=True)
    args = p.parse_args()
    try:
        if args.command == "probe":
            report = probe()
        else:
            if args.request is None:
                raise ValueError("run requires --request.")
            if args.request.resolve() == args.report.resolve():
                raise ValueError("Report must not overwrite request.")
            if args.request.stat().st_size > MAX_REQUEST_BYTES:
                raise ValueError("Request exceeds 16 MiB; use npy inputs.")
            request = json.loads(args.request.read_text())
            report = run_job(request)
    except Exception as exc:
        report = {"ok": False, "error_type": type(exc).__name__, "error": str(exc),
                  "cpu_fallback_enabled": False}
    write_json(args.report, report)
    print(json.dumps({k: report[k] for k in ("ok", "device", "operation", "error") if k in report}))
    return 0 if report["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
