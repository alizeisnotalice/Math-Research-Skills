#!/usr/bin/env python3
"""Exact finite zero-rectangle search for the Lemma 3.2 input interface.

This enumerates witnesses for one supplied finite rational product distribution.
It does not prove the source's universal Gaussian-rounding lemma or evaluate
its exponential threshold.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


def fraction(value: object, field: str) -> Fraction:
    if not isinstance(value, str):
        raise ValueError(f"{field} entries must be fraction strings")
    try:
        answer = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"invalid fraction in {field}: {value}") from error
    if answer <= 0:
        raise ValueError(f"{field} entries must be positive")
    return answer


def exact_rank(rows: list[list[int]]) -> int:
    matrix = [[Fraction(entry) for entry in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        source = next((i for i in range(pivot_row, len(matrix)) if matrix[i][column]), None)
        if source is None:
            continue
        matrix[pivot_row], matrix[source] = matrix[source], matrix[pivot_row]
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / pivot for entry in matrix[pivot_row]]
        for i in range(len(matrix)):
            if i != pivot_row and matrix[i][column]:
                scale = matrix[i][column]
                matrix[i] = [entry - scale * basis for entry, basis in zip(matrix[i], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def nonempty_subsets(size: int):
    for width in range(1, size + 1):
        yield from itertools.combinations(range(size), width)


def validate(payload: object) -> tuple[list[list[int]], list[Fraction], list[Fraction]]:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    rows = payload.get("rows")
    if not isinstance(rows, list) or not rows or not all(isinstance(row, list) and row for row in rows):
        raise ValueError("rows must be a nonempty rectangular Boolean matrix")
    width = len(rows[0])
    if any(len(row) != width or any(type(entry) is not int or entry not in (0, 1) for entry in row) for row in rows):
        raise ValueError("rows must be a rectangular Boolean matrix")
    row_weights = [fraction(x, "row_weights") for x in payload.get("row_weights", [])]
    col_weights = [fraction(x, "col_weights") for x in payload.get("col_weights", [])]
    if len(row_weights) != len(rows) or len(col_weights) != width:
        raise ValueError("weight lengths must match matrix dimensions")
    if sum(row_weights) != 1 or sum(col_weights) != 1:
        raise ValueError("row_weights and col_weights must each sum to 1")
    return rows, row_weights, col_weights


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        rows, row_weights, col_weights = validate(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2

    rank = exact_rank(rows)
    density = sum(
        row_weights[i] * col_weights[j] * rows[i][j]
        for i in range(len(rows)) for j in range(len(rows[0]))
    )
    best: tuple[Fraction, tuple[int, ...], tuple[int, ...]] | None = None
    for a_rows in nonempty_subsets(len(rows)):
        row_mass = sum((row_weights[i] for i in a_rows), Fraction())
        for b_cols in nonempty_subsets(len(rows[0])):
            if any(rows[i][j] for i in a_rows for j in b_cols):
                continue
            mass = row_mass * sum((col_weights[j] for j in b_cols), Fraction())
            candidate = (mass, a_rows, b_cols)
            if best is None or candidate[0] > best[0] or (candidate[0] == best[0] and candidate[1:] < best[1:]):
                best = candidate
    if best is None:
        print("error: no nonempty zero rectangle exists", file=sys.stderr)
        return 1
    mass, a_rows, b_cols = best
    result = {
        "shape": [len(rows), len(rows[0])],
        "real_rank_exact": rank,
        "product_one_density_exact": str(density),
        "source_lemma_preconditions": {
            "full_support_product_weights": True,
            "boolean_matrix": True,
            "density_at_most_one_half": density <= Fraction(1, 2),
        },
        "maximum_zero_rectangle": {
            "rows": list(a_rows), "columns": list(b_cols), "product_measure_exact": str(mass),
        },
        "source_threshold_symbolic": f"(9/16) * exp(-240 * sqrt({rank} * {density}))",
        "scope": "Exact exhaustive witness search for this finite input; not a proof or numerical evaluation of Lemma 3.2.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
