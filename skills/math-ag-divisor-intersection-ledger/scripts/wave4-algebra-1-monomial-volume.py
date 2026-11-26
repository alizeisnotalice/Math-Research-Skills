#!/usr/bin/env python3
"""Exact replay of the displayed cyclic-slice monomial valuation formula."""
import json
import math
import sys
from fractions import Fraction


def frac(x):
    return Fraction(str(x))


def cube_root_rational(x):
    if x < 0:
        raise ValueError("m*h must be nonnegative")
    def root(n):
        r = round(n ** (1 / 3))
        while (r + 1) ** 3 <= n:
            r += 1
        while r ** 3 > n:
            r -= 1
        return r
    p, q = root(x.numerator), root(x.denominator)
    if p ** 3 != x.numerator or q ** 3 != x.denominator:
        raise ValueError("m*h must have an exact rational cube root for this replay")
    return Fraction(p, q)


def main(path):
    d = json.load(open(path, encoding="utf-8"))
    r, alpha, m, h = (frac(d[k]) for k in ("r", "alpha", "m", "h"))
    if alpha <= 0 or m <= 0 or h <= 0:
        raise ValueError("alpha, m, and h must be positive")
    root = cube_root_rational(m * h)
    result = {
        "valid": True,
        "discrepancy": str(r + 3 * alpha),
        "volume_upper_bound": str(h * (1 + alpha * root) ** 3),
        "crossing_z0": str(Fraction(1, 1) / (1 + alpha * root)),
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except (IndexError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}, sort_keys=True))
        raise SystemExit(2)
