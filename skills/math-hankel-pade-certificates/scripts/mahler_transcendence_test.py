#!/usr/bin/env python3
"""Exact finite matrix from Bell--Coons' universal Mahler-function test.

Input JSON has k, coefficients (a_i low degree first), and taylor coefficients.
It verifies only the finite matrix calculation required after the source hypotheses.
"""
import json
import sys
from fractions import Fraction


def rank(matrix):
    matrix = [row[:] for row in matrix]
    rows, cols, pivot_row = len(matrix), len(matrix[0]), 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if matrix[r][col]), None)
        if pivot is None:
            continue
        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        divisor = matrix[pivot_row][col]
        matrix[pivot_row] = [x / divisor for x in matrix[pivot_row]]
        for r in range(rows):
            if r != pivot_row and matrix[r][col]:
                factor = matrix[r][col]
                matrix[r] = [x - factor * y for x, y in zip(matrix[r], matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def main(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    k = int(data["k"])
    coeffs = data["coefficients"]
    if k < 2 or len(coeffs) < 2:
        raise ValueError("require k >= 2 and at least degree-one Mahler equation")
    d = len(coeffs) - 1
    H = max(len(poly) - 1 for poly in coeffs)
    denominator = k ** (d + 1) - 2 * k**d + 1
    if denominator <= 0:
        raise ValueError("source kappa denominator is nonpositive")
    kappa = (H * (k - 1)) // denominator + H // (k ** (d - 1) * (k - 1)) + 1
    width = 1 + H + kappa * (k ** (d + 1) - 1) // (k - 1)
    # Figure 2 asks for f(0) through f(kappa + width - 1), inclusive.
    required = kappa + width
    seq = [Fraction(x) for x in data["taylor"]]
    if len(seq) < required:
        raise ValueError(f"need at least {required} Taylor coefficients, got {len(seq)}")
    matrix = [[seq[i + j] for j in range(width)] for i in range(1 + kappa)]
    matrix_rank = rank(matrix)
    answer = {
        "k": k,
        "degree": d,
        "H": H,
        "kappa": kappa,
        "matrix_shape": [1 + kappa, width],
        "required_taylor_coefficients": required,
        "rank": matrix_rank,
        "full_row_rank": matrix_rank == 1 + kappa,
        "scope": "Exact finite rank computation only. Functional identity and all global source hypotheses are external obligations."
    }
    print(json.dumps(answer, indent=2, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: mahler_transcendence_test.py INPUT.json")
    main(sys.argv[1])
