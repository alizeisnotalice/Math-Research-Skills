#!/usr/bin/env python3
"""Exact finite checks for Beukers' Lemma 2.2 denominator bound.

This program does not evaluate a p-adic L-value or prove irrationality.  It
only computes reduced rational rising-factorial coefficients and verifies
their divisibility by mu_n(F), using Python integers and fractions.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction


def prime_factors(value: int) -> list[int]:
    """Return the distinct prime factors of a positive integer."""
    factors: list[int] = []
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            factors.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        factors.append(remaining)
    return factors


def valuation(value: int, prime: int) -> int:
    result = 0
    while value and value % prime == 0:
        value //= prime
        result += 1
    return result


def mu(n: int, denominator: int, factors: list[int]) -> int:
    value = denominator**n
    for prime in factors:
        value *= prime ** (n // (prime - 1))
    return value


def coefficient(b: int, denominator: int, n: int) -> Fraction:
    value = Fraction(1, 1)
    for k in range(n):
        value *= Fraction(b + denominator * k, denominator * (k + 1))
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, required=True, help="numerator b")
    parser.add_argument("--F", type=int, required=True, help="denominator F > 1")
    parser.add_argument("--through", type=int, required=True, help="check 0 through N")
    parser.add_argument("--prime", type=int, help="optional prime for denominator valuations")
    args = parser.parse_args()

    if args.F <= 1:
        parser.error("F must be greater than 1")
    if args.through < 0:
        parser.error("through must be nonnegative")
    if math.gcd(args.b, args.F) != 1:
        parser.error("b and F must be coprime")
    if args.prime is not None and (args.prime < 2 or any(args.prime % d == 0 for d in range(2, int(args.prime**0.5) + 1))):
        parser.error("prime must be prime")

    factors = prime_factors(args.F)
    rows = []
    for n in range(args.through + 1):
        value = coefficient(args.b, args.F, n)
        bound = mu(n, args.F, factors)
        row = {
            "n": n,
            "coefficient_numerator": str(value.numerator),
            "reduced_denominator": str(value.denominator),
            "mu_n_F": str(bound),
            "denominator_divides_mu": bound % value.denominator == 0,
        }
        if args.prime is not None:
            row["v_prime_reduced_denominator"] = valuation(value.denominator, args.prime)
            row["v_prime_mu_n_F"] = valuation(bound, args.prime)
        rows.append(row)

    print(json.dumps({
        "source": "Beukers (2008), Lemma 2.2; finite exact instances only",
        "input": {"b": args.b, "F": args.F, "through": args.through, "prime": args.prime},
        "prime_factors_of_F": factors,
        "rows": rows,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
