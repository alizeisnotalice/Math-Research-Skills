#!/usr/bin/env python3
"""Exact finite shifted-Legendre coefficient and moment checks.

This script checks only the polynomial identities scoped in the accompanying
reference.  It uses rational arithmetic and never infers an infinite-n claim.
"""

import json
import math
import sys
from fractions import Fraction


def polynomial(n: int) -> list[int]:
    return [(-1) ** m * math.comb(n, m) * math.comb(n + m, m)
            for m in range(n + 1)]


def moment(coefficients: list[int], degree: int) -> Fraction:
    return sum((Fraction(c, m + degree + 1)
                for m, c in enumerate(coefficients)), Fraction(0))


def check(n: int) -> dict:
    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("n must be a nonnegative integer")
    coeffs = polynomial(n)
    lower = [moment(coeffs, d) for d in range(n)]
    diagonal = moment(coeffs, n)
    expected = Fraction((-1) ** n * math.factorial(n) ** 2,
                        math.factorial(2 * n + 1))
    if any(lower) or diagonal != expected:
        raise AssertionError("exact moment identity failed")
    return {
        "n": n,
        "coefficients_low_to_high": coeffs,
        "lower_moments": [str(x) for x in lower],
        "diagonal_moment": str(diagonal),
        "expected_diagonal_moment": str(expected),
        "status": "finite exact check passed",
    }


def main() -> int:
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        for n in (0, 1, 3, 6):
            check(n)
        try:
            check(-1)
        except ValueError:
            print(json.dumps({"positive_cases": [0, 1, 3, 6],
                              "negative_case": "rejected",
                              "status": "self-test passed"}, sort_keys=True))
            return 0
        raise AssertionError("negative input was accepted")
    if len(sys.argv) != 2:
        raise ValueError("usage: script '{\"n\": nonnegative integer}' or --self-test")
    payload = json.loads(sys.argv[1])
    if not isinstance(payload, dict) or set(payload) != {"n"}:
        raise ValueError("input must be exactly an object with key n")
    print(json.dumps(check(payload["n"]), sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
