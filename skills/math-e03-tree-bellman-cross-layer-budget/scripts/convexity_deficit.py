#!/usr/bin/env python3
"""Exact integer-exponent instance of the binary convexity-deficit bound."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction


def rational(value: str) -> Fraction:
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"invalid rational: {value!r}") from exc


def certificate(alpha: int, a: Fraction, b: Fraction) -> dict[str, str | bool]:
    if alpha < 2:
        raise ValueError("exact helper is restricted to integer alpha >= 2")
    if not (a >= b >= 0):
        raise ValueError("require a >= b >= 0")
    deficit = (a + b) ** alpha - a**alpha - b**alpha
    lower = (2**alpha - 2) * b**alpha
    return {"alpha": str(alpha), "a": str(a), "b": str(b), "deficit": str(deficit), "lower_bound": str(lower), "passed": deficit >= lower}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha", type=int, required=True)
    parser.add_argument("--a", required=True)
    parser.add_argument("--b", required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(certificate(args.alpha, rational(args.a), rational(args.b)), sort_keys=True))
    except ValueError as exc:
        print(f"rejected: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
