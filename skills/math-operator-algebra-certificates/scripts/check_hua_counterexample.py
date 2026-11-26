#!/usr/bin/env python3
"""Directed Arb check of the six-matrix Hua--Bellman counterexample."""

from __future__ import annotations

import json
import sys

from flint import arb, arb_mat, ctx


RAW = (
    ((-2, -9), (-5, -10)),
    ((9, -5), (9, 6)),
    ((-10, -3), (-6, 3)),
    ((-8, -8), (1, -10)),
    ((-2, 1), (-6, -1)),
    ((-1, 3), (10, -6)),
)


def operator_norm(matrix: tuple[tuple[int, int], tuple[int, int]]) -> arb:
    a, b = matrix[0]
    c, d = matrix[1]
    g00, g01, g11 = arb(a * a + c * c), arb(a * b + c * d), arb(b * b + d * d)
    top_eigenvalue = (g00 + g11 + ((g00 - g11) ** 2 + 4 * g01**2).sqrt()) / 2
    return top_eigenvalue.sqrt()


def normalized(matrix: tuple[tuple[int, int], tuple[int, int]]) -> list[list[arb]]:
    norm = operator_norm(matrix)
    return [[arb(entry) / (2 * norm) for entry in row] for row in matrix]


def transpose_product(left: list[list[arb]], right: list[list[arb]]) -> list[list[arb]]:
    return [[sum(left[k][i] * right[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def determinant_i_minus(product: list[list[arb]]) -> arb:
    a = 1 - product[0][0]
    b = -product[0][1]
    c = -product[1][0]
    d = 1 - product[1][1]
    return a * d - b * c


def run(precision: int) -> dict[str, str | int]:
    if precision < 80:
        raise ValueError("precision must be at least 80 bits")
    ctx.prec = precision
    matrices = [normalized(matrix) for matrix in RAW]
    h_entries: list[list[arb]] = []
    for left in matrices:
        row: list[arb] = []
        for right in matrices:
            determinant = determinant_i_minus(transpose_product(left, right))
            if not determinant > 0:
                raise AssertionError("a determinant enclosure is not strictly positive")
            row.append(1 / determinant.sqrt())
        h_entries.append(row)
    eigenvalues = arb_mat(h_entries).eig()
    least_index = min(range(len(eigenvalues)), key=lambda index: eigenvalues[index].real.upper())
    least = eigenvalues[least_index]
    if not least.real.upper() < 0:
        raise AssertionError("the least eigenvalue enclosure is not strictly negative")
    for index, other in enumerate(eigenvalues):
        if index != least_index and not least.real.upper() < other.real.lower():
            raise AssertionError("the negative interval could not be separated as the least eigenvalue")
    return {
        "precision_bits": precision,
        "matrix_count": len(matrices),
        "normalization": "A_j = raw_j / (2 ||raw_j||_op)",
        "least_eigenvalue_real_enclosure": str(least.real),
        "least_eigenvalue_imaginary_enclosure": str(least.imag),
        "strictly_negative": True,
    }


if __name__ == "__main__":
    precision = int(json.loads(open(sys.argv[1]).read()).get("precision_bits", 256)) if len(sys.argv) == 2 else 256
    try:
        print(json.dumps(run(precision), sort_keys=True))
    except (ValueError, AssertionError, OSError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
