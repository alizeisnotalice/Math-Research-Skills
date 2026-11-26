#!/usr/bin/env python3
"""Exact finite Koteljanskii checker for a supplied rational matrix."""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


def fail(message: str) -> None:
    print(json.dumps({"status": "rejected", "reason": message}, sort_keys=True))
    raise SystemExit(2)


def parse_fraction(value: object) -> Fraction:
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"not a rational value: {value!r}") from exc


def inverse(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(matrix)
    work = [row[:] + [Fraction(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next((row for row in range(column, n) if work[row][column]), None)
        if pivot is None:
            raise ValueError("matrix is singular")
        work[column], work[pivot] = work[pivot], work[column]
        scale = work[column][column]
        work[column] = [entry / scale for entry in work[column]]
        for row in range(n):
            if row != column and work[row][column]:
                factor = work[row][column]
                work[row] = [x - factor * y for x, y in zip(work[row], work[column])]
    return [row[n:] for row in work]


def permanent(matrix: list[list[Fraction]]) -> Fraction:
    n = len(matrix)
    return sum(
        (Fraction(1) if n == 0 else _product(matrix[row][perm[row]] for row in range(n)))
        for perm in itertools.permutations(range(n))
    )


def _product(values: object) -> Fraction:
    answer = Fraction(1)
    for value in values:
        answer *= value
    return answer


def principal(matrix: list[list[Fraction]], subset: frozenset[int]) -> list[list[Fraction]]:
    indices = sorted(subset)
    return [[matrix[i][j] for j in indices] for i in indices]


def subsets(n: int) -> list[frozenset[int]]:
    return [frozenset(indices) for r in range(n + 1) for indices in itertools.combinations(range(n), r)]


def main(path: Path) -> None:
    try:
        payload = json.loads(path.read_text())
        matrix = [[parse_fraction(x) for x in row] for row in payload["matrix"]]
        diagonal = [parse_fraction(x) for x in payload["diagonal_similarity"]]
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        fail(str(exc))
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix) or len(diagonal) != n:
        fail("matrix and diagonal_similarity must have the same positive square size")
    if any(x < 0 for row in matrix for x in row):
        fail("matrix must be entrywise nonnegative")
    if any(x <= 0 for x in diagonal):
        fail("diagonal_similarity entries must be positive")
    try:
        inv = inverse(matrix)
    except ValueError as exc:
        fail(str(exc))
    if any(inv[i][j] > 0 for i in range(n) for j in range(n) if i != j):
        fail("inverse has a positive off-diagonal entry")
    scaled = [[diagonal[i] * matrix[i][j] / diagonal[j] for j in range(n)] for i in range(n)]
    if any(scaled[i][j] != scaled[j][i] for i in range(n) for j in range(n)):
        fail("given positive diagonal similarity does not produce a symmetric matrix")
    all_subsets = subsets(n)
    values = {subset: permanent(principal(matrix, subset)) for subset in all_subsets}
    minimum_slack = None
    for left in all_subsets:
        for right in all_subsets:
            slack = values[left | right] * values[left & right] - values[left] * values[right]
            if slack < 0:
                fail("Koteljanskii inequality failed for a subset pair")
            if minimum_slack is None or slack < minimum_slack:
                minimum_slack = slack
    print(json.dumps({"dimension": n, "minimum_slack": str(minimum_slack), "status": "certified", "subset_pairs": len(all_subsets) ** 2}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit(f"usage: {Path(sys.argv[0]).name} INPUT.json")
    main(Path(sys.argv[1]))
