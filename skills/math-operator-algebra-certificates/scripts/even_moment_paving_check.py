#!/usr/bin/env python3
"""Exact finite-dimensional even-moment certificate for coordinate pavings."""

import argparse
import json
from fractions import Fraction
from pathlib import Path


def rational(value):
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, list) and len(value) == 2:
        return Fraction(value[0], value[1])
    raise ValueError("a rational must be an integer, string, or [numerator, denominator]")


def matmul(left, right):
    n = len(left)
    return [[sum((left[i][k] * right[k][j] for k in range(n)), Fraction(0))
             for j in range(n)] for i in range(n)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON with matrix, blocks, diagonal, epsilon, and k")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text())
        matrix = [[rational(x) for x in row] for row in data["matrix"]]
        n = len(matrix)
        if n == 0 or any(len(row) != n for row in matrix):
            raise ValueError("matrix must be nonempty and square")
        if any(matrix[i][j] != matrix[j][i] for i in range(n) for j in range(n)):
            raise ValueError("matrix must be symmetric (self-adjoint over the rationals)")
        blocks = data["blocks"]
        flattened = [index for block in blocks for index in block]
        if sorted(flattened) != list(range(n)):
            raise ValueError("blocks must partition indices 0 through n-1 exactly once")
        diagonal = [rational(x) for x in data["diagonal"]]
        if len(diagonal) != n:
            raise ValueError("diagonal must have the matrix dimension")
        epsilon = rational(data["epsilon"])
        k = data["k"]
        if epsilon <= 0 or not isinstance(k, int) or k < 1:
            raise ValueError("epsilon must be positive and k must be a positive integer")
    except (KeyError, TypeError, ValueError, ZeroDivisionError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    block_of = {index: block_no for block_no, block in enumerate(blocks) for index in block}
    z = [[(matrix[i][j] if block_of[i] == block_of[j] else Fraction(0))
          - (diagonal[i] if i == j else Fraction(0)) for j in range(n)] for i in range(n)]
    power = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for _ in range(2 * k):
        power = matmul(power, z)
    normalized_moment = sum((power[i][i] for i in range(n)), Fraction(0)) / n
    bound = normalized_moment / (epsilon ** (2 * k))
    result = {
        "dimension": n,
        "blocks": blocks,
        "k": k,
        "epsilon": str(epsilon),
        "normalized_even_moment": str(normalized_moment),
        "markov_bad_spectral_mass_bound": str(bound),
        "certificate": "For the normalized trace, tau(1_{|z|>epsilon}) <= tau(z^(2k))/epsilon^(2k).",
    }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
