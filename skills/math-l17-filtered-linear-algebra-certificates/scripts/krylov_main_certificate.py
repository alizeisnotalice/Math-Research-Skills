#!/usr/bin/env python3
"""Exact main-eigenvalue certificate for an integer symmetric matrix.

Input JSON: a square integer matrix, optionally with a ``signs`` vector.
The certificate uses no floating-point eigenvalues: d is the square-free
degree of the characteristic polynomial, and K=[s,As,...,A^(d-1)s].
For symmetric A, rank_Q(K)=d iff every distinct eigenvalue has nonzero
projection of s, equivalently every eigenvalue of diag(s) A diag(s) is main.
"""
import argparse
import json
import sys

import sympy as sp


def fail(message: str) -> None:
    raise ValueError(message)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="JSON file with matrix and optional signs")
    parser.add_argument("--signs", help="comma-separated +/-1 override")
    args = parser.parse_args()
    data = json.load(open(args.input, encoding="utf-8"))
    matrix = data.get("matrix")
    if not isinstance(matrix, list) or not matrix:
        fail("matrix must be a nonempty list of rows")
    n = len(matrix)
    if any(not isinstance(row, list) or len(row) != n for row in matrix):
        fail("matrix must be square")
    if any(not isinstance(x, int) for row in matrix for x in row):
        fail("matrix entries must be integers")
    A = sp.Matrix(matrix)
    if A != A.T:
        fail("matrix must be symmetric")
    raw_signs = args.signs.split(",") if args.signs else data.get("signs", [1] * n)
    if len(raw_signs) != n:
        fail("sign vector has wrong length")
    try:
        signs = [int(x) for x in raw_signs]
    except (TypeError, ValueError) as exc:
        raise ValueError("signs must be integers") from exc
    if any(x not in (-1, 1) for x in signs):
        fail("signs must all be +1 or -1")

    variable = sp.Symbol("t")
    characteristic = sp.Poly(A.charpoly(variable).as_expr(), variable)
    distinct_eigenvalues = characteristic.sqf_part().degree()
    vector = sp.Matrix(signs)
    columns = []
    for _ in range(distinct_eigenvalues):
        columns.append(vector)
        vector = A * vector
    krylov = sp.Matrix.hstack(*columns)
    active = krylov.rank()
    result = {
        "n": n,
        "distinct_eigenvalue_count": distinct_eigenvalues,
        "krylov_rank_over_Q": active,
        "all_distinct_eigenvalues_main_after_switching": active == distinct_eigenvalues,
        "characteristic_polynomial": str(characteristic.as_expr()),
    }
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
