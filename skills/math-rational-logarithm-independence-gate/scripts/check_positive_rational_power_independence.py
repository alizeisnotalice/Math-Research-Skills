#!/usr/bin/env python3
"""Exact multiplicative-independence test for positive rational inputs."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction

def positive_rational(text: str) -> Fraction:
    try:
        value = Fraction(text)
    except (ValueError, ZeroDivisionError) as exc:
        raise argparse.ArgumentTypeError(f"not a rational number: {text!r}") from exc
    if value <= 0:
        raise argparse.ArgumentTypeError(f"expected a positive rational, got {text!r}")
    return value


def factor_integer(value: int) -> dict[int, int]:
    """Return the positive prime factorization using exact trial division."""
    result: dict[int, int] = {}
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            result[divisor] = result.get(divisor, 0) + 1
            remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        result[remaining] = result.get(remaining, 0) + 1
    return result


def valuations(value: Fraction) -> dict[int, int]:
    result: dict[int, int] = {}
    for prime, exponent in factor_integer(value.numerator).items():
        result[int(prime)] = int(exponent)
    for prime, exponent in factor_integer(value.denominator).items():
        result[int(prime)] = result.get(int(prime), 0) - int(exponent)
    return {prime: exponent for prime, exponent in result.items() if exponent}


def rational_rank(rows: list[list[int]], columns: int) -> int:
    """Compute matrix rank by exact Gaussian elimination over Q."""
    matrix = [[Fraction(entry) for entry in row] for row in rows]
    pivot_row = 0
    for column in range(columns):
        pivot = next(
            (row for row in range(pivot_row, len(matrix)) if matrix[row][column]),
            None,
        )
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        scale = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / scale for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            multiple = matrix[row][column]
            matrix[row] = [
                entry - multiple * pivot_entry
                for entry, pivot_entry in zip(matrix[row], matrix[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Test exact multiplicative independence of positive rationals."
    )
    parser.add_argument("values", nargs="+", type=positive_rational)
    args = parser.parse_args()

    columns = [valuations(value) for value in args.values]
    primes = sorted({prime for column in columns for prime in column})
    rows = [[column.get(prime, 0) for column in columns] for prime in primes]
    rank = rational_rank(rows, len(columns))
    result = {
        "values": [str(value) for value in args.values],
        "primes": primes,
        "valuation_matrix": rows,
        "rank_over_Q": rank,
        "number_of_inputs": len(columns),
        "multiplicatively_independent": rank == len(columns),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
