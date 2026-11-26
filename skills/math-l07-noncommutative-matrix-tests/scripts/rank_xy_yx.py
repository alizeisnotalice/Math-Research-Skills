#!/usr/bin/env python3
"""Verify rank(I-XY)=rank(I-YX) over the rationals for one square pair."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
             for j in range(len(right[0]))] for i in range(len(left))]


def rank(matrix):
    rows = [[Fraction(value) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0])):
        pivot = next((i for i in range(pivot_row, len(rows)) if rows[i][column]), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        scale = rows[pivot_row][column]
        rows[pivot_row] = [value / scale for value in rows[pivot_row]]
        for i in range(len(rows)):
            if i != pivot_row and rows[i][column]:
                factor = rows[i][column]
                rows[i] = [a - factor * b for a, b in zip(rows[i], rows[pivot_row])]
        pivot_row += 1
    return pivot_row


def check(data):
    x, y = data["X"], data["Y"]
    size = len(x)
    if size == 0 or any(len(row) != size for row in x + y) or len(y) != size:
        raise ValueError("X and Y must be nonempty square matrices of the same size")
    if any(type(value) not in (int, str) for matrix in (x, y) for row in matrix for value in row):
        raise ValueError("use integer entries or exact rational strings")
    x, y = ([[Fraction(value) for value in row] for row in matrix] for matrix in (x, y))
    identity = [[int(i == j) for j in range(size)] for i in range(size)]
    xy, yx = multiply(x, y), multiply(y, x)
    left = [[identity[i][j] - xy[i][j] for j in range(size)] for i in range(size)]
    right = [[identity[i][j] - yx[i][j] for j in range(size)] for i in range(size)]
    left_rank, right_rank = rank(left), rank(right)
    if left_rank != right_rank:
        raise AssertionError("rank identity failed")
    return {"dimension": size, "rank_I_minus_XY": left_rank,
            "rank_I_minus_YX": right_rank, "equal": True}


if __name__ == "__main__":
    try:
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), ensure_ascii=False))
    except (IndexError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
