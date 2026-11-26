#!/usr/bin/env python3
"""Exact Collatz--Wielandt ratio bounds for finite nonnegative matrices.

The helper proves only min_i (A v)_i/v_i <= rho(A) <= max_i (A v)_i/v_i
for a strictly positive rational vector v.  It does not construct a Markov
partition, bound derivatives, evaluate powered weights, or assert a dimension.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path
from typing import Sequence

RationalMatrix = Sequence[Sequence[Fraction]]


def ratio_bounds(matrix: RationalMatrix, vector: Sequence[Fraction]) -> tuple[Fraction, Fraction]:
    """Return exact Collatz--Wielandt lower/upper bounds for rho(matrix)."""
    dimension = len(vector)
    if dimension == 0 or len(matrix) != dimension or any(len(row) != dimension for row in matrix):
        raise ValueError("matrix must be nonempty and square with vector-matching dimension")
    if any(entry < 0 for row in matrix for entry in row):
        raise ValueError("matrix entries must be nonnegative")
    if any(entry <= 0 for entry in vector):
        raise ValueError("test vector entries must be strictly positive")
    ratios = [sum((row[j] * vector[j] for j in range(dimension)), Fraction()) / vector[i] for i, row in enumerate(matrix)]
    return min(ratios), max(ratios)


def strict_unit_conclusion(lower: Fraction, upper: Fraction) -> str:
    """Report only a strict spectral-radius comparison certified by the ratios."""
    if lower > 1:
        return "rho(A) > 1 certified"
    if upper < 1:
        return "rho(A) < 1 certified"
    return "no strict comparison with 1 certified"


def read_rational(value: object) -> Fraction:
    if type(value) is not int and not isinstance(value, str):
        raise ValueError("entries must be integers or exact rational strings")
    return Fraction(value)


def run_examples() -> None:
    above = ((Fraction(2), Fraction(1)), (Fraction(1), Fraction(2)))
    below = ((Fraction(1, 4), Fraction()), (Fraction(), Fraction(1, 2)))
    boundary = ((Fraction(1), Fraction()), (Fraction(), Fraction(1)))
    vector = (Fraction(1), Fraction(1))
    for name, matrix in (("above", above), ("below", below), ("boundary", boundary)):
        lower, upper = ratio_bounds(matrix, vector)
        print(f"{name}: lower={lower} upper={upper}; {strict_unit_conclusion(lower, upper)}")
    try:
        ratio_bounds(boundary, (Fraction(1), Fraction()))
    except ValueError as error:
        print(f"invalid-vector: {error}")
    else:
        raise AssertionError("a zero test-vector entry must be rejected")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, help="JSON object with matrix and vector")
    args = parser.parse_args()
    if args.input is None:
        run_examples()
        return
    try:
        data = json.loads(args.input.read_text())
        matrix = [[read_rational(value) for value in row] for row in data["matrix"]]
        vector = [read_rational(value) for value in data["vector"]]
        lower, upper = ratio_bounds(matrix, vector)
    except (OSError, KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    result = {"lower": str(lower), "upper": str(upper),
              "comparison": strict_unit_conclusion(lower, upper)}
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
