#!/usr/bin/env python3
"""Choose NumPy CPU, tuned PyTorch CPU or Metal by measured transfer-inclusive cost."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import statistics
import sys
import time

CPU_BUDGET = os.cpu_count() or 1
if os.environ.get('LOCAL_MATH_CPU_BUDGET'):
    CPU_BUDGET = int(os.environ['LOCAL_MATH_CPU_BUDGET'])
    if not 1 <= CPU_BUDGET <= (os.cpu_count() or 1):
        raise ValueError('LOCAL_MATH_CPU_BUDGET must be between 1 and the local CPU count.')
    for variable in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
        os.environ[variable] = str(CPU_BUDGET)
import gpu_math as core  # disables MPS fallback before torch import
import numpy as np
import torch

SCHEMA = 1
DEFAULT_CACHE = Path("/Volumes/data/CodexTemp/cache/local-hybrid-math/calibration_v1.json")


def numpy_op(op, x):
    if op == "matmul":
        return x["a"] @ x["b"]
    if op == "sin_exp":
        return np.sin(x["x"]) * np.exp(-x["x"] ** 2)
    return np.sum(x["x"], dtype=x["x"].dtype)


def torch_op(op, x):
    if op == "matmul":
        return x["a"] @ x["b"]
    if op == "sin_exp":
        return torch.sin(x["x"]) * torch.exp(-x["x"].square())
    return torch.sum(x["x"])


def execute(choice, op, arrays):
    if choice["engine"] == "numpy":
        return np.asarray(numpy_op(op, arrays)), "cpu"
    if choice["device"] == "cpu":
        torch.set_num_threads(choice["threads"])
        with torch.inference_mode():
            y = torch_op(op, {k: torch.from_numpy(a) for k, a in arrays.items()})
        return y.numpy(), str(y.device)
    with torch.inference_mode():
        x = {k: torch.from_numpy(a).to("mps") for k, a in arrays.items()}
        y = torch_op(op, x)
        torch.mps.synchronize()
        if y.device.type != "mps":
            raise RuntimeError("Expected an MPS output; no implicit CPU fallback.")
        return y.cpu().numpy().copy(), str(y.device)


def signature(op, arrays, available):
    description = {"schema": SCHEMA, "python": sys.executable, "torch": torch.__version__,
        "numpy": np.__version__, "platform": platform.platform(), "machine": platform.machine(),
        "cores": os.cpu_count(), "cpu_budget": CPU_BUDGET,
        "thread_environment":{k:os.environ.get(k) for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS')},
        "operation": op, "mps_available": available,
        "inputs": {k: {"shape": list(v.shape), "dtype": str(v.dtype)} for k, v in arrays.items()}}
    return hashlib.sha256(json.dumps(description, sort_keys=True).encode()).hexdigest(), description


def select_backend(op, arrays, backend, cache_path, refresh):
    available = bool(torch.backends.mps.is_built() and torch.backends.mps.is_available())
    dtype = next(iter(arrays.values())).dtype
    mps_eligible = available and dtype == np.float32
    if backend == "mps" and not mps_eligible:
        raise ValueError("Explicit MPS requires available Apple GPU and float32; no silent fallback/downcast.")
    _key, description = signature(op, arrays, available)
    description["calibration_scope"] = backend
    key = hashlib.sha256(json.dumps(description, sort_keys=True).encode()).hexdigest()
    records = {}
    if cache_path.exists():
        try:
            records = json.loads(cache_path.read_text()) if cache_path.stat().st_size < 2*1024**2 else {}
        except (ValueError, OSError):
            records = {}
    if not isinstance(records, dict): records = {}
    records = {k:v for k,v in records.items() if isinstance(v,dict)
        and type(v.get('timestamp')) in (int,float) and math.isfinite(v['timestamp'])}
    prior = records.get(key)
    # Performance cache is not trusted for correctness; validate its choices and use a 24h TTL.
    def valid_choice(c):
        if not isinstance(c, dict): return False
        if c.get("engine") == "numpy": return c.get("device") == "cpu" and backend != "mps"
        return c.get("engine") == "torch" and ((c.get("device") == "mps" and mps_eligible and backend != "cpu") or
            (c.get("device") == "cpu" and backend != "mps" and type(c.get("threads")) is int and
             1 <= c["threads"] <= CPU_BUDGET))
    if (not refresh and isinstance(prior, dict) and 0 <= time.time()-prior.get("timestamp", 0) < 86400
            and prior.get("description") == description and isinstance(prior.get("measurements"), list)
            and prior["measurements"] and all(isinstance(x,dict) and valid_choice(x.get("choice")) and
              type(x.get("median_s")) in (int,float) and 0 < x["median_s"] < 3600
              for x in prior["measurements"]) and
            (backend == "mps" or any(x['choice']['device']=='cpu' for x in prior['measurements']))):
        measurements = prior["measurements"]
        candidate_errors = prior.get('candidate_errors',[])
        hit = True
    else:
        choices = [{"engine": "numpy", "device": "cpu"}] if backend != "mps" else []
        threads = sorted({min(n, CPU_BUDGET) for n in (1, 2, 4, 8, CPU_BUDGET)})
        if backend != "mps":
            choices += [{"engine": "torch", "device": "cpu", "threads": n} for n in threads]
        if mps_eligible and backend != "cpu":
            choices.append({"engine": "torch", "device": "mps"})
        measurements = []; candidate_errors = []
        for choice in choices:
            try:
                execute(choice, op, arrays)  # warmup excluded from median
                times = []
                for _ in range(3):
                    t = time.perf_counter()
                    result, _device = execute(choice, op, arrays)
                    times.append(time.perf_counter()-t)
                if not np.isfinite(result).all():
                    continue
                measurements.append({"choice": choice, "median_s": statistics.median(times), "runs_s": times})
            except (RuntimeError, NotImplementedError) as exc:
                if choice["device"] != "mps":
                    raise
                candidate_errors.append({'choice':choice,'error':str(exc)})
        if not measurements:
            raise RuntimeError("No finite successful backend calibration.")
        hit = False
        records[key] = {"timestamp": time.time(), "description": description,
                        "measurements": measurements, "candidate_errors":candidate_errors}
        # Retain a bounded cache. Other processes may replace a timing entry; numerical validation is separate.
        records = dict(sorted(records.items(), key=lambda v: v[1].get("timestamp",0), reverse=True)[:100])
        core.write_json(cache_path, records)
    cpu_choices = [m for m in measurements if m["choice"]["device"] == "cpu"]
    cpu = min(cpu_choices, key=lambda m: m["median_s"]) if cpu_choices else None
    metal = [m for m in measurements if m["choice"]["device"] == "mps"]
    if backend == "mps":
        if not metal:
            raise RuntimeError("Explicit GPU operation did not pass calibration.")
        best = metal[0]
        reason = "explicit GPU request"
    elif backend == "cpu" or not metal:
        best = cpu
        reason = "explicit CPU request" if backend == "cpu" else "CPU: precision/support eligibility"
    elif metal[0]["median_s"] < 0.9 * cpu["median_s"]:
        best = metal[0]
        reason = "GPU measured at least 10% faster including tensor upload and output download"
    else:
        best = cpu
        reason = "CPU wins or GPU gain below 10% noise margin"
    return best["choice"], {"cache_hit": hit, "cache_key": key, "cache_file": str(cache_path),
        "reason": reason, "measurements": measurements, "candidate_errors":candidate_errors,
        "timing_scope": "warm operation, input wrapping/upload and output materialization/download; excludes import/calibration/verification"}


def validate(op, arrays, host, mode, rtol, atol):
    if mode == "none":
        return {"mode": "none", "passed": None, "evidence_class": "unverified-computation"}
    if mode == "sample" and op == "matmul":
        m,n = host.shape
        count = min(64, m*n)
        indices = np.unique(np.linspace(0, m*n-1, count, dtype=int))
        rows, cols = indices//n, indices%n
        ref = np.array([np.dot(arrays["a"][i,:].astype(float), arrays["b"][:,j].astype(float)) for i,j in zip(rows,cols)])
        actual = host[rows,cols].astype(float)
    elif mode == "sample" and op == "sin_exp":
        indices = np.unique(np.linspace(0, host.size-1, min(128, host.size), dtype=int))
        x = arrays["x"].ravel()[indices].astype(float)
        ref = np.sin(x)*np.exp(-x*x)
        actual = host.ravel()[indices].astype(float)
    else:
        ref = np.asarray(numpy_op(op, {k:v.astype(float) for k,v in arrays.items()}))
        actual = host.astype(float)
    finite = bool(np.isfinite(actual).all() and np.isfinite(ref).all())
    error = np.abs(actual-ref)
    passed = finite and bool(np.all(error <= atol+rtol*np.abs(ref)))
    return {"mode": mode, "checked_elements": int(np.size(ref)), "total_output_elements": int(host.size),
        "passed": passed, "max_abs_error": float(np.max(error)) if finite else None,
        "reference": "NumPy float64 on identical compute-dtype inputs", "rtol":rtol,"atol":atol,
        "evidence_class": "sampled-numerical-check" if mode == "sample" else "full-numerical-check",
        "is_rigorous_proof": False}


def run_job(request, cache_path=DEFAULT_CACHE, refresh=False):
    start = time.perf_counter()
    if not isinstance(request, dict): raise ValueError("Request must be an object.")
    allowed = {"operation","dtype","allow_precision_loss","inputs","output_npy","output_mat",
               "rtol","atol","backend","verify"}
    if set(request)-allowed: raise ValueError("Unknown fields: "+str(sorted(set(request)-allowed)))
    op = request.get("operation")
    backend = request.get("backend","auto")
    dtype = request.get("dtype")
    mode = request.get("verify","full")
    if op not in ("matmul","sin_exp","sum") or backend not in ("auto","cpu","mps"):
        raise ValueError("Unsupported operation/backend.")
    if dtype not in ("float32","float64") or mode not in ("full","sample","none"):
        raise ValueError("Specify float32/float64 and full/sample/none verification.")
    if type(request.get("allow_precision_loss",False)) is not bool:
        raise ValueError("allow_precision_loss must be boolean.")
    expected = {"a","b"} if op == "matmul" else {"x"}
    specs = request.get("inputs")
    if not isinstance(specs,dict) or set(specs) != expected: raise ValueError("Incorrect input keys.")
    arrays, info = {},{}
    for k,s in specs.items(): arrays[k],info[k] = core.read_array(s,np,request.get("allow_precision_loss",False),dtype)
    if op == "matmul":
        a,b = arrays["a"],arrays["b"]
        if a.ndim != 2 or b.ndim != 2 or a.shape[1] != b.shape[0]: raise ValueError("Incompatible 2D matmul shapes.")
        shape = (a.shape[0],b.shape[1])
    else: shape = arrays["x"].shape if op == "sin_exp" else ()
    estimated = (sum(v.size for v in arrays.values())+math.prod(shape))*32
    if estimated > core.MAX_JOB_BYTES: raise ValueError("Estimated job exceeds 512 MiB; split the job.")
    rtol,atol = request.get("rtol",5e-4 if dtype=="float32" else 1e-10),request.get("atol",5e-5 if dtype=="float32" else 1e-12)
    if any(type(x) not in (int,float) or not math.isfinite(x) or x < 0 for x in (rtol,atol)):
        raise ValueError("Nonnegative finite tolerances required.")
    output_keys = [k for k in ("output_npy","output_mat") if k in request]
    if len(output_keys)>1: raise ValueError("Select only one file output.")
    output = Path(request[output_keys[0]]) if output_keys else None
    if output is not None:
        ext = ".npy" if output_keys[0] == "output_npy" else ".mat"
        if not output.is_absolute() or output.suffix != ext or output.exists():
            raise ValueError("File output must be a new absolute path of the selected type.")
        if any(k in s and Path(s[k]).resolve()==output.resolve() for s in specs.values() for k in ("npy","mat")):
            raise ValueError("Output must not overwrite an input.")
    elif math.prod(shape)>core.MAX_INLINE_ELEMENTS: raise ValueError("Large results require MAT/NPY output.")
    t = time.perf_counter()
    choice,selection = select_backend(op,arrays,backend,Path(cache_path),refresh)
    calibration = time.perf_counter()-t
    t = time.perf_counter()
    host,device = execute(choice,op,arrays)
    execution = time.perf_counter()-t
    t = time.perf_counter()
    verification = validate(op,arrays,host,mode,rtol,atol)
    verification_s = time.perf_counter()-t
    finite = bool(np.isfinite(host).all())
    ok = finite and verification["passed"] is not False
    r = {"ok":ok,"device":device,"engine":choice,"dtype":str(host.dtype),
        "backend_requested":backend,"selection":selection,"inputs":info,"operation":op,
        "verification":verification,"cpu_fallback_enabled":False,"estimated_working_bytes":estimated,
        "timings_s":{"calibration_or_cache":calibration,"selected_operation_with_transfers":execution,
            "verification":verification_s},"result":{"shape":list(host.shape),"order":"C"}}
    if ok:
        if output is None: r["result"]["data"] = host.ravel().tolist()
        else:
            output.parent.mkdir(parents=True,exist_ok=True)
            with output.open("xb") as f:
                if output.suffix == ".npy": np.save(f,host,allow_pickle=False)
                else:
                    from scipy.io import savemat
                    savemat(f,{"result":host},do_compression=False)
            r["result"]["mat" if output.suffix==".mat" else "npy"] = str(output)
    r["timings_s"]["job_excluding_import_and_report_write"] = time.perf_counter()-start
    return r


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--request",type=Path,required=True)
    p.add_argument("--report",type=Path,required=True)
    p.add_argument("--cache",type=Path,default=DEFAULT_CACHE)
    p.add_argument("--refresh-calibration",action="store_true")
    a=p.parse_args()
    try:
        if not Path('/Volumes/data').is_mount(): raise RuntimeError("data volume is not mounted.")
        if a.request.resolve()==a.report.resolve(): raise ValueError("Report must not overwrite request.")
        if a.request.stat().st_size>core.MAX_REQUEST_BYTES: raise ValueError("Request exceeds 16 MiB.")
        result=run_job(json.loads(a.request.read_text()),a.cache,a.refresh_calibration)
    except Exception as exc:
        result={"ok":False,"error_type":type(exc).__name__,"error":str(exc)}
    core.write_json(a.report,result)
    print(json.dumps({k:result[k] for k in ("ok","device","dtype","error") if k in result}))
    return 0 if result["ok"] else 2


if __name__ == "__main__": raise SystemExit(main())
