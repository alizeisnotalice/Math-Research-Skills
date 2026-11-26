#!/usr/bin/env python3
"""Check the finite rank-halving interface in Cogentic log-rank Appendix A.3.

The script accepts a finite Boolean matrix and a proposed nonempty rectangle.
It makes exact rational row reductions.  It verifies only the finite rank split,
not the paper's high-rank rectangle theorem or a communication protocol bound.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path


def exact_rank(rows: list[list[int]]) -> int:
    if not rows or not rows[0]:
        return 0
    matrix = [[Fraction(value) for value in row] for row in rows]
    pivot_row = 0
    columns = len(matrix[0])
    for column in range(columns):
        candidate = next((row for row in range(pivot_row, len(matrix)) if matrix[row][column]), None)
        if candidate is None:
            continue
        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / pivot for entry in matrix[pivot_row]]
        for row in range(len(matrix)):
            if row == pivot_row or not matrix[row][column]:
                continue
            coefficient = matrix[row][column]
            matrix[row] = [entry - coefficient * basis for entry, basis in zip(matrix[row], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def validate(payload: dict) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    rows = payload.get("rows")
    if not isinstance(rows, list) or not rows or not all(isinstance(row, list) and row for row in rows):
        raise ValueError("rows must be a nonempty rectangular list")
    width = len(rows[0])
    if any(len(row) != width or any(type(value) is not int or value not in (0, 1) for value in row) for row in rows):
        raise ValueError("rows must be a rectangular Boolean matrix")
    a_rows = payload.get("a_rows")
    b_cols = payload.get("b_cols")
    if not all(isinstance(indices, list) and indices for indices in (a_rows, b_cols)):
        raise ValueError("a_rows and b_cols must be nonempty lists")
    if any(type(index) is not int or not 0 <= index < len(rows) for index in a_rows):
        raise ValueError("a_rows contains an out-of-range index")
    if any(type(index) is not int or not 0 <= index < width for index in b_cols):
        raise ValueError("b_cols contains an out-of-range index")
    if len(set(a_rows)) != len(a_rows) or len(set(b_cols)) != len(b_cols):
        raise ValueError("rectangle indices must be distinct")
    values = {rows[row][column] for row in a_rows for column in b_cols}
    if len(values) != 1:
        raise ValueError("the proposed rectangle is not monochromatic")
    a_set, b_set = set(a_rows), set(b_cols)
    ac_rows = [index for index in range(len(rows)) if index not in a_set]
    bc_cols = [index for index in range(width) if index not in b_set]
    first_block = [[rows[row][column] for column in bc_cols] for row in a_rows]
    second_block = [[rows[row][column] for column in b_cols] for row in ac_rows]
    rank = exact_rank(rows)
    rank_first, rank_second = exact_rank(first_block), exact_rank(second_block)
    value = values.pop()
    split_bound = rank + value
    smaller = min(rank_first, rank_second)
    return {
        "shape": [len(rows), width],
        "matrix_rank": rank,
        "rectangle_value": value,
        "rectangle_uniform_density": f"{len(a_rows) * len(b_cols)}/{len(rows) * width}",
        "complementary_block_ranks": {"A_x_Bc": rank_first, "Ac_x_B": rank_second},
        "rank_split_bound": split_bound,
        "rank_split_verified": rank_first + rank_second <= split_bound,
        "rank_halving_bound": (rank + 1) // 2,
        "smaller_complementary_rank": smaller,
        "rank_halving_verified": smaller <= (rank + 1) // 2,
        "scope": "Exact finite check of the Appendix A.3 rank-split interface only.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = validate(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["rank_split_verified"] and result["rank_halving_verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
