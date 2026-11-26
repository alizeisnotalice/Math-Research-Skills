#!/usr/bin/env python3
"""Check the torus nondegeneracy premise for exact polynomial coordinates."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path
import sys


def rational(value: object) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("boolean coefficients are not rational coefficients")
    if not isinstance(value, (str, int)):
        raise ValueError("coefficients must be integer or rational strings")
    return Fraction(value)


def rank(matrix: list[list[Fraction]]) -> int:
    if not matrix:
        return 0
    rows = [row[:] for row in matrix]
    height, width = len(rows), len(rows[0])
    pivot_row = 0
    for column in range(width):
        pivot = next((row for row in range(pivot_row, height) if rows[row][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [entry / scale for entry in rows[pivot_row]]
        for row in range(height):
            if row == pivot_row or not rows[row][column]:
                continue
            factor = rows[row][column]
            rows[row] = [entry - factor * basis for entry, basis in zip(rows[row], rows[pivot_row])]
        pivot_row += 1
        if pivot_row == height:
            break
    return pivot_row


def check(data: dict[str, object]) -> dict[str, object]:
    coordinates = data.get("coordinates")
    if not isinstance(coordinates, list) or not coordinates:
        raise ValueError("coordinates must be a nonempty list of coefficient lists")
    if not all(isinstance(polynomial, list) and polynomial for polynomial in coordinates):
        raise ValueError("each coordinate must have at least its constant coefficient")
    parsed = [[rational(coefficient) for coefficient in polynomial] for polynomial in coordinates]
    coefficient_rows = [polynomial[1:] for polynomial in parsed]
    width = max(map(len, coefficient_rows), default=0)
    matrix = [row + [Fraction(0)] * (width - len(row)) for row in coefficient_rows]
    matrix_rank = rank(matrix)
    return {
        "coordinate_count": len(coordinates),
        "nonconstant_coefficient_columns": width,
        "q_rank": matrix_rank,
        "q_linearly_independent": matrix_rank == len(coordinates),
        "scope": "This exact check applies when every coordinate of f is supplied as a polynomial in z with rational coefficients.",
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_torus_q_independence.py INPUT.json")
    print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), ensure_ascii=False))


if __name__ == "__main__":
    main()
