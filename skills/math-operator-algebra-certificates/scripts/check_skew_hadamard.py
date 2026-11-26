#!/usr/bin/env python3
"""Generate the recursive skew-Hadamard family and verify integer identities."""

from __future__ import annotations

import json
from pathlib import Path
import sys


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    size = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size)] for i in range(size)]


def skew_matrix(size: int) -> list[list[int]]:
    if size == 1:
        return [[0]]
    previous = skew_matrix(size // 2)
    half = size // 2
    return [
        previous[i] + [previous[i][j] + int(i == j) for j in range(half)]
        for i in range(half)
    ] + [
        [previous[i][j] - int(i == j) for j in range(half)] + [-previous[i][j] for j in range(half)]
        for i in range(half)
    ]


def check(payload: dict) -> dict:
    size = payload.get("size")
    if type(size) is not int or size < 2 or size & (size - 1):
        raise ValueError("size must be a power of two at least 2")
    matrix = skew_matrix(size)
    square = multiply(matrix, matrix)
    skew = all(matrix[i][j] == -matrix[j][i] for i in range(size) for j in range(size))
    zero_diagonal = all(matrix[i][i] == 0 for i in range(size))
    signs = all(matrix[i][j] in (-1, 1) for i in range(size) for j in range(size) if i != j)
    square_identity = all(square[i][j] == (-(size - 1) if i == j else 0) for i in range(size) for j in range(size))
    if not (skew and zero_diagonal and signs and square_identity):
        raise AssertionError("recursive skew-Hadamard identities failed")
    return {
        "size": size,
        "skew_symmetric": skew,
        "zero_diagonal": zero_diagonal,
        "off_diagonal_signs": signs,
        "square_equals_negative_size_minus_one_identity": square_identity,
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_skew_hadamard.py INPUT.json")
    try:
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
