#!/usr/bin/env python3
"""Exact finite enclosures from the Fontana–Mascheroni Gregory series."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


def gregory_coefficients(n: int) -> list[Fraction]:
    """Return G_0,...,G_n from (sum G_k z^k) log(1+z)=z exactly."""
    if n < 0:
        raise ValueError("n must be non-negative")
    values = [Fraction(1)]
    for degree in range(1, n + 1):
        # The coefficient of z^(degree+1) in the product is zero.
        values.append(
            -sum(
                values[k] * Fraction((-1) ** (degree - k), degree - k + 1)
                for k in range(degree)
            )
        )
    return values


def enclosure(n: int) -> tuple[Fraction, Fraction, list[Fraction]]:
    """Return the partial sum, strict upper endpoint and exact coefficients."""
    if n < 1:
        raise ValueError("n must be at least 1")
    coefficients = gregory_coefficients(n)
    partial = sum((abs(coefficients[k]) / k for k in range(1, n + 1)), Fraction())
    remaining_mass = 1 - sum((abs(value) for value in coefficients[1:]), Fraction(0))
    return partial, partial + remaining_mass / (n + 1), coefficients


def as_pair(x: Fraction) -> dict[str, int]:
    return {"numerator": x.numerator, "denominator": x.denominator}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--terms", type=int, required=True, help="positive number of terms")
    args = parser.parse_args()
    try:
        lower, upper, coefficients = enclosure(args.terms)
    except ValueError as exc:
        parser.error(str(exc))
    print(
        json.dumps(
            {
                "status": "CERTIFIED_INTERVAL",
                "method": "Fontana–Mascheroni Gregory series with an exact remaining-mass bound",
                "terms": args.terms,
                "lower": as_pair(lower),
                "upper": as_pair(upper),
                "strict_upper": True,
                "tail_bound": as_pair(upper - lower),
                "remaining_coefficient_mass": as_pair((upper - lower) * (args.terms + 1)),
                "gregory_coefficients": [as_pair(x) for x in coefficients[1:]],
                "scope": "finite rational enclosure for gamma only; no denominator-scaled irrationality conclusion",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
