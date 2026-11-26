#!/usr/bin/env python3
"""Exact finite check of the mixed-determinant rank-one border identity."""
import json
import sys
from fractions import Fraction
from itertools import product
from pathlib import Path


def q(value):
    return Fraction(str(value))


def determinant(matrix):
    matrix = [[q(value) for value in row] for row in matrix]
    size = len(matrix)
    if size == 0:
        return Fraction(1)
    answer = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if matrix[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            answer = -answer
        value = matrix[column][column]
        answer *= value
        for row in range(column + 1, size):
            factor = matrix[row][column] / value
            for later in range(column + 1, size):
                matrix[row][later] -= factor * matrix[column][later]
    return answer


def principal(matrix, subset):
    return [[matrix[i][j] for j in subset] for i in subset]


def eta(matrices):
    dimension = len(matrices[0])
    count = len(matrices)
    total = Fraction(0)
    for coloring in product(range(count), repeat=dimension):
        term = Fraction(1)
        for color in range(count):
            subset = [i for i, label in enumerate(coloring) if label == color]
            term *= determinant(principal(matrices[color], subset))
        total += term
    return total


def outer(vector):
    return [[x * y for y in vector] for x in vector]


def plus(left, right):
    return [[left[i][j] + right[i][j] for j in range(len(left))] for i in range(len(left))]


def bordered(matrix, vector, alpha):
    return [row + [vector[i]] for i, row in enumerate(matrix)] + [list(vector) + [alpha]]


def render(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main(path):
    payload = json.loads(Path(path).read_text())
    matrices = [[[q(x) for x in row] for row in matrix] for matrix in payload["matrices"]]
    vectors = [[q(x) for x in vector] for vector in payload["vectors"]]
    alphas = [q(x) for x in payload["alphas"]]
    if not matrices or len(matrices) != len(vectors) or len(matrices) != len(alphas):
        raise ValueError("matrices, vectors, and alphas need the same positive length")
    dimension = len(matrices[0])
    if any(len(matrix) != dimension or any(len(row) != dimension for row in matrix) for matrix in matrices):
        raise ValueError("matrices must be equally sized square matrices")
    if any(len(vector) != dimension for vector in vectors):
        raise ValueError("vectors must match the matrix dimension")
    if any(matrix[i][j] != matrix[j][i] for matrix in matrices for i in range(dimension) for j in range(dimension)):
        raise ValueError("this finite checker accepts symmetric matrices only")
    base = eta(matrices)
    derivatives = [eta(matrices[:j] + [plus(matrices[j], outer(vectors[j]))] + matrices[j + 1:]) - base for j in range(len(matrices))]
    lhs = eta([bordered(matrix, vector, alpha) for matrix, vector, alpha in zip(matrices, vectors, alphas)])
    rhs = sum(alphas) * base - sum(derivatives)
    result = {"base": render(base), "derivatives": [render(x) for x in derivatives], "lhs": render(lhs), "rhs": render(rhs)}
    expected = payload.get("expected")
    if expected is not None and result != expected:
        raise AssertionError(f"expected {expected}, got {result}")
    if lhs != rhs:
        raise AssertionError(f"border identity failed: lhs={lhs}, rhs={rhs}")
    result["status"] = "verified"
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_border_identity.py INPUT.json")
    main(sys.argv[1])
