#!/usr/bin/env python3
"""Exact construction of the anticommuting involution test family."""

from __future__ import annotations

import json
from pathlib import Path
import sys


def kron(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[left[i][j] * right[a][b] for j in range(len(left)) for b in range(len(right))]
            for i in range(len(left)) for a in range(len(right))]


def multiply(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    size = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size)] for i in range(size)]


def add(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    return [[left[i][j] + right[i][j] for j in range(len(left))] for i in range(len(left))]


def scalar(matrix: list[list[int]], value: int) -> list[list[int]]:
    return [[value * entry for entry in row] for row in matrix]


def identity(size: int) -> list[list[int]]:
    return [[int(i == j) for j in range(size)] for i in range(size)]


def generator(index: int, count: int) -> list[list[int]]:
    z = [[1, 0], [0, -1]]
    h = [[0, 1], [1, 0]]
    result = [[1]]
    for position in range(count):
        result = kron(result, h if position == index else z if position < index else identity(2))
    return result


def check(payload: dict) -> dict:
    count = payload.get("count")
    if type(count) is not int or count < 1 or count > 7:
        raise ValueError("count must be an integer from 1 through 7")
    matrices = [generator(i, count) for i in range(count)]
    size = 2**count
    unitary = all(multiply(matrix, matrix) == identity(size) for matrix in matrices)
    anticommute = all(add(multiply(matrices[i], matrices[j]), multiply(matrices[j], matrices[i])) == scalar(identity(size), 0)
                      for i in range(count) for j in range(i + 1, count))
    if not (unitary and anticommute):
        raise AssertionError("Clifford relations failed")
    # A deterministic coefficient specialization checks the derived square identity.
    coefficients = list(range(1, count + 1))
    series = [[sum(coefficients[k] * matrices[k][i][j] for k in range(count)) for j in range(size)] for i in range(size)]
    expected = scalar(identity(size), sum(value * value for value in coefficients))
    if multiply(series, series) != expected:
        raise AssertionError("finite series-square identity failed")
    return {"count": count, "dimension": size, "involutions": unitary, "pairwise_anticommuting": anticommute,
            "specialized_series_square": sum(value * value for value in coefficients)}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_clifford_series.py INPUT.json")
    try:
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
