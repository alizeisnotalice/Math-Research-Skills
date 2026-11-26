#!/usr/bin/env python3
"""Exact inversion-fixedness check in Z[X]/(Phi_n), for a small input."""

from __future__ import annotations

import json
import sys
from functools import lru_cache
from pathlib import Path


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def divisors(number: int) -> list[int]:
    return [candidate for candidate in range(1, number + 1) if number % candidate == 0]


def exact_monic_quotient(dividend: list[int], divisor: list[int]) -> list[int]:
    work = dividend[:]
    degree = len(divisor) - 1
    quotient = [0] * max(1, len(work) - degree)
    while len(work) - 1 >= degree:
        shift = len(work) - 1 - degree
        coefficient = work[-1]  # divisor is monic
        quotient[shift] = coefficient
        for index, value in enumerate(divisor):
            work[shift + index] -= coefficient * value
        trim(work)
    if any(work):
        raise ValueError("nonexact cyclotomic division")
    return trim(quotient)


@lru_cache(maxsize=None)
def cyclotomic(number: int) -> tuple[int, ...]:
    if number < 1:
        raise ValueError("n must be positive")
    polynomial = [-1] + [0] * (number - 1) + [1]  # X^n - 1
    for divisor in divisors(number):
        if divisor != number:
            polynomial = exact_monic_quotient(polynomial, list(cyclotomic(divisor)))
    return tuple(polynomial)


def reduce_monic(poly: list[int], divisor: list[int]) -> list[int]:
    work = poly[:]
    degree = len(divisor) - 1
    while len(work) - 1 >= degree:
        shift = len(work) - 1 - degree
        coefficient = work[-1]
        for index, value in enumerate(divisor):
            work[shift + index] -= coefficient * value
        trim(work)
    return trim(work)


def main(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    number = data.get("n")
    coefficients = data.get("coefficients")
    if not isinstance(number, int) or isinstance(number, bool) or number < 1:
        raise ValueError("n must be a positive integer")
    if (not isinstance(coefficients, list) or not coefficients or
            any(not isinstance(c, int) or isinstance(c, bool) for c in coefficients)):
        raise ValueError("coefficients must be a nonempty integer list")
    coefficients = trim(coefficients[:])
    polynomial = list(cyclotomic(number))
    degree = len(coefficients) - 1
    # This is X^M(P(X)-P(X^{-1})).  Its first summand is X^M P(X)
    # and its second is the coefficient-reversal of P.
    inverted_difference = [0] * (2 * degree + 1)
    for index, coefficient in enumerate(coefficients):
        inverted_difference[degree + index] += coefficient
        inverted_difference[degree - index] -= coefficient
    remainder = reduce_monic(inverted_difference, polynomial)
    print(json.dumps({
        "n": number,
        "cyclotomic_polynomial": polynomial,
        "inversion_difference_remainder": remainder,
        "fixed_by_inversion": remainder == [0],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError(f"usage: {Path(sys.argv[0]).name} INPUT.json")
        raise SystemExit(main(Path(sys.argv[1])))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
