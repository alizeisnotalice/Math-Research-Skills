#!/usr/bin/env python3
"""Exact replay of the bounded parity/perfect-power precheck on Cogentic PDF p.57."""
from __future__ import annotations

import argparse
import json


def exact_power_root(n: int, exponent: int) -> int | None:
    """Return x>=2 with x**exponent=n, using integer binary search, else None."""
    lo, hi = 2, n
    while lo <= hi:
        mid = (lo + hi) // 2
        value = pow(mid, exponent)
        if value == n:
            return mid
        if value < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def precheck(n: int) -> dict[str, object]:
    if n < 4:
        raise ValueError("n must be at least 4")
    if n % 2 == 0:
        return {"n": n, "status": "factor", "factor": 2, "cofactor": n // 2, "reason": "even"}
    bit_length = n.bit_length()
    for exponent in range(2, bit_length + 1):
        root = exact_power_root(n, exponent)
        if root is not None:
            return {"n": n, "status": "factor", "factor": root, "cofactor": n // root, "reason": "perfect_power", "exponent": exponent}
    return {"n": n, "status": "inconclusive", "reason": "not_even_or_detected_perfect_power"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int, nargs="+", help="explicit integers at least 4")
    args = parser.parse_args()
    if any(n < 4 for n in args.n):
        parser.error("n must be at least 4")
    for n in args.n:
        print(json.dumps(precheck(n), sort_keys=True))


if __name__ == "__main__":
    main()
