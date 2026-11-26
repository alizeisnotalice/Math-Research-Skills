#!/usr/bin/env python3
"""Exact coefficient-prefix check for the Fermat/Golomb Mahler identity."""
from __future__ import annotations

import argparse
import json
import sys


def coefficients(epsilon: int, degree: int, dilation: int = 1) -> list[int]:
    out = [0] * (degree + 1)
    power = dilation
    while power <= degree:
        for multiple in range(power, degree + 1, power):
            r = multiple // power
            out[multiple] += (-epsilon) ** (r - 1)
        power *= 2
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", help="JSON object with epsilon, m, and degree")
    ap.add_argument("--epsilon", type=int, choices=(-1, 1))
    ap.add_argument("--m", type=int)
    ap.add_argument("--degree", type=int)
    ns = ap.parse_args()
    if ns.input:
        try:
            data = json.load(open(ns.input))
            ns.epsilon, ns.m, ns.degree = int(data["epsilon"]), int(data["m"]), int(data["degree"])
        except (OSError, KeyError, ValueError, json.JSONDecodeError) as exc:
            print(f"rejected: invalid input JSON: {exc}", file=sys.stderr)
            return 2
    if ns.epsilon not in (-1, 1) or ns.m is None or ns.degree is None:
        print("rejected: supply epsilon in {-1,1}, m, and degree", file=sys.stderr)
        return 2
    if ns.m < 1 or ns.degree < 1:
        print("rejected: m and degree must be positive", file=sys.stderr)
        return 2
    h = coefficients(ns.epsilon, ns.degree)
    lhs = coefficients(ns.epsilon, ns.degree, dilation=2 ** ns.m)
    finite_sum = [0] * (ns.degree + 1)
    for j in range(ns.m):
        q = 2 ** j
        for multiple in range(q, ns.degree + 1, q):
            finite_sum[multiple] += (-ns.epsilon) ** (multiple // q - 1)
    rhs = [h[i] - finite_sum[i] for i in range(ns.degree + 1)]
    if lhs != rhs:
        print("rejected: coefficient identity failed", file=sys.stderr)
        return 2
    print(json.dumps({"accepted": True, "epsilon": ns.epsilon, "m": ns.m,
                      "degree": ns.degree, "identity": "H(z^(2^m))=H(z)-sum_{j<m} term_j"},
                     sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
