#!/usr/bin/env python3
"""Exact finite evaluator for the Macdonald cycle-weighted permanent."""

from fractions import Fraction
from itertools import permutations
import json
from pathlib import Path
import sys


def fraction(value):
    return Fraction(str(value))


def cycles(permutation):
    unseen = set(range(len(permutation)))
    result = []
    while unseen:
        first = min(unseen)
        cycle = []
        index = first
        while index in unseen:
            unseen.remove(index)
            cycle.append(index)
            index = permutation[index]
        result.append(cycle)
    return result


def weight(q, t, size):
    return (1 - t ** size) / (1 - q ** size)


def evaluate(data):
    q, t = fraction(data["q"]), fraction(data["t"])
    matrix = [[fraction(value) for value in row] for row in data["matrix"]]
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("matrix must be nonempty and square")
    if any(q ** length == 1 for length in range(1, n + 1)):
        raise ValueError("require q**j != 1 for every 1 <= j <= matrix size")
    total = Fraction()
    for permutation in permutations(range(n)):
        term = Fraction(1)
        for cycle in cycles(permutation):
            term *= weight(q, t, len(cycle))
        for i, j in enumerate(permutation):
            term *= matrix[i][j]
        total += term
    h_n = Fraction(1)
    for j in range(n):
        h_n *= (1 - t * q ** j) / (1 - q ** (j + 1))
    return {
        "n": n,
        "cycle_weighted_permanent": str(total),
        "scalar_H_n": str(h_n),
        "weight_1": str(weight(q, t, 1)),
        "weight_n": str(weight(q, t, n)),
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: cycle_weighted_permanent.py INPUT.json")
    try:
        result = evaluate(json.loads(Path(sys.argv[1]).read_text()))
    except ValueError as error:
        raise SystemExit(str(error)) from error
    print(json.dumps(result, sort_keys=True))
