#!/usr/bin/env python3
"""Emit the exact finite coefficient formula from the reviewed source."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb


def rational_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def coefficient(m: int) -> dict[str, object]:
    if m < 0:
        raise ValueError("m must be nonnegative")
    if m == 0:
        return {"m": 0, "gamma": 1, "zeta": {}, "rational_remainder": "-1"}
    remainder = Fraction((-1) ** (m + 1), 1)
    for k in range(1, m + 1):
        remainder += Fraction(1 + (-1) ** (k - 1), k)
    return {
        "m": m,
        "gamma": 1,
        "zeta": {f"zeta({k + 1})": comb(m, k) * (-2) ** k for k in range(1, m + 1)},
        "rational_remainder": rational_string(remainder),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("m", type=int, help="nonnegative coefficient index")
    args = parser.parse_args()
    print(json.dumps(coefficient(args.m), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
