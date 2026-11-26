#!/usr/bin/env python3
"""Check the finite Lorentz rest-frame reduction of a future-timelike 4-vector."""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


def rest_frame(p: list[float], tol: float) -> dict[str, object]:
    if len(p) != 4 or any(not isinstance(x, (int, float)) or not math.isfinite(x) for x in p):
        raise ValueError("p must be four finite real numbers [energy, px, py, pz]")
    energy = float(p[0])
    spatial = [float(x) for x in p[1:]]
    norm = math.sqrt(sum(x * x for x in spatial))
    mass_squared = energy * energy - norm * norm
    if energy <= 0 or mass_squared <= tol:
        raise ValueError("p must be future timelike with energy>0 and energy^2-|spatial|^2>tol")
    mass = math.sqrt(mass_squared)
    if norm == 0:
        boosted = [energy, 0.0, 0.0, 0.0]
        beta = 0.0
        gamma = 1.0
    else:
        beta = norm / energy
        gamma = energy / mass
        boosted_energy = gamma * (energy - beta * norm)
        factor = (gamma - 1.0) - gamma * beta * energy / norm
        boosted = [boosted_energy, *(x * (1.0 + factor) for x in spatial)]
    residual = max(abs(boosted[0] - mass), *(abs(x) for x in boosted[1:]))
    return {
        "mass": mass,
        "beta": beta,
        "gamma": gamma,
        "boosted": boosted,
        "residual": residual,
        "ok": residual <= 100.0 * tol * max(1.0, energy),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="JSON file containing p and optional tol")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        got = rest_frame([5.0, 3.0, 0.0, 0.0], 1e-12)
        assert got["ok"] and abs(float(got["mass"]) - 4.0) < 1e-12
        try:
            rest_frame([4.0, 4.0, 0.0, 0.0], 1e-12)
        except ValueError:
            print(json.dumps({"self_test": "ok", "mass": got["mass"], "residual": got["residual"]}))
            return 0
        raise AssertionError("null input was not rejected")
    if not args.input:
        parser.error("input or --self-test is required")
    try:
        raw = json.loads(Path(args.input).read_text())
        result = rest_frame(raw["p"], float(raw.get("tol", 1e-12)))
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"invalid: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
