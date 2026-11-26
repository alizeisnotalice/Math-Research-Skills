#!/usr/bin/env python3
"""Certify the forced Boolean-coefficient contradiction for 1+a*x^2+x^k."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json


def obstruction(k: int, a: Fraction) -> dict:
    if k < 4 or k % 2:
        raise ValueError("the exponent k must be even and at least 4")
    if not 0 < a < 1:
        raise ValueError("the coefficient a must be strictly between 0 and 1")
    m = k // 2
    last_forced = (1 - (-a)**m) / (1 + a)
    gap = a * last_forced
    assert 0 < last_forced <= 1 and gap > 0
    return {
        "exponent": k,
        "coefficient": str(a),
        "normalized_parity_degree": m,
        "last_forced_cofactor_coefficient": str(last_forced),
        "product_coefficient_lower_bound": str(1 + gap),
        "strict_excess_over_one": str(gap),
    }


def rational(value: str) -> Fraction:
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise argparse.ArgumentTypeError("use an exact rational coefficient") from error


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exponent", type=int)
    parser.add_argument("coefficient", type=rational)
    args = parser.parse_args()
    try:
        result = obstruction(args.exponent, args.coefficient)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
