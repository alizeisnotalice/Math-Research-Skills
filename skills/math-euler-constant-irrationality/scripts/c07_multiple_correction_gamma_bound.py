#!/usr/bin/env python3
"""Exact rational ledger for Cao--Xu--You (arXiv:1409.0968v1), Theorem 1.

It provides the source-certified relation
  lower_error < gamma - (H_n - log(n) - correction) < upper_error.
No floating point numbers or unproved numerical logarithm estimates are used.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, k) for k in range(1, n + 1)), Fraction())


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, required=True, help="positive integer n")
    args = parser.parse_args()
    if args.n < 1:
        parser.error("n must be positive")

    n = Fraction(args.n)
    eta0 = (6 * n - 1) / (12 * n * n)
    eta = 1 / (120 * n**4 + Fraction(10, 21) * n * n - Fraction(241, 882))
    correction = eta0 + eta
    constant = Fraction(13775, 3056130)
    lower = constant / (n + Fraction(3, 4)) ** 10
    upper = constant / (n - Fraction(1, 4)) ** 10

    def pair(value: Fraction) -> dict[str, str]:
        return {"numerator": str(value.numerator), "denominator": str(value.denominator)}

    print(json.dumps({
        "source": "Cao--Xu--You, arXiv:1409.0968v1, Theorem 1; exact rational components",
        "n": args.n,
        "H_n": pair(harmonic(args.n)),
        "eta0": pair(eta0),
        "eta": pair(eta),
        "correction_eta0_plus_eta": pair(correction),
        "mu_n": "H_n - log(n) - correction_eta0_plus_eta",
        "strict_error_bound": {
            "lower_error": pair(lower),
            "upper_error": pair(upper),
            "meaning": "lower_error < gamma - mu_n < upper_error",
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
