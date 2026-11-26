#!/usr/bin/env python3
"""Exact rational replay of the finite-rank Schur-complement inertia identity.

The input is a JSON object with rational entries (integers, decimal-free strings,
or strings such as "-3/5") under H, J, W.  It verifies

    n_{>=0}(H + J W J^T) = n_+(H) + n_{<=0}(W^{-1} + J^T H^{-1} J).

All matrix operations use fractions.Fraction.  Inertia is obtained by symmetric
congruence elimination: a nonzero diagonal pivot is a 1x1 block; if all diagonal
entries vanish, a nonzero off-diagonal entry is a [[0,b],[b,0]] 2x2 block.  Thus
zero eigenvalues of the final M are counted exactly, without numerical tolerances.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


Q = Fraction
Matrix = list[list[Q]]


def q(value: Any) -> Q:
    return value if isinstance(value, Q) else Q(str(value))


def matrix(values: list[list[Any]]) -> Matrix:
    if not values or not values[0] or any(len(row) != len(values[0]) for row in values):
        raise ValueError("matrix must be nonempty and rectangular")
    return [[q(x) for x in row] for row in values]


def transpose(a: Matrix) -> Matrix:
    return [list(col) for col in zip(*a)]


def add(a: Matrix, b: Matrix) -> Matrix:
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError("matrix dimensions do not agree")
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def multiply(a: Matrix, b: Matrix) -> Matrix:
    if len(a[0]) != len(b):
        raise ValueError("matrix dimensions do not agree")
    return [[sum(a[i][ell] * b[ell][j] for ell in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def is_symmetric(a: Matrix) -> bool:
    return len(a) == len(a[0]) and all(a[i][j] == a[j][i] for i in range(len(a)) for j in range(len(a)))


def inverse(a: Matrix) -> Matrix:
    if len(a) != len(a[0]):
        raise ValueError("inverse requires a square matrix")
    n = len(a)
    aug = [a[i][:] + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col] != 0), None)
        if pivot is None:
            raise ValueError("matrix is singular")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pivot_value = aug[col][col]
        aug[col] = [entry / pivot_value for entry in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor:
                aug[row] = [aug[row][j] - factor * aug[col][j] for j in range(2 * n)]
    return [row[n:] for row in aug]


def reorder(a: Matrix, order: list[int]) -> Matrix:
    return [[a[i][j] for j in order] for i in order]


def inertia_congruence(a: Matrix) -> tuple[dict[str, int], list[dict[str, str]]]:
    """Return exact inertia via 1x1 and [[0,b],[b,0]] congruence pivots."""
    if not is_symmetric(a):
        raise ValueError("inertia requires a symmetric matrix")
    b = [row[:] for row in a]
    counts = {"positive": 0, "negative": 0, "zero": 0}
    pivots: list[dict[str, str]] = []
    while b:
        n = len(b)
        diagonal = next((i for i in range(n) if b[i][i] != 0), None)
        if diagonal is not None:
            c = reorder(b, [diagonal] + [i for i in range(n) if i != diagonal])
            pivot = c[0][0]
            counts["positive" if pivot > 0 else "negative"] += 1
            pivots.append({"kind": "1x1", "value": str(pivot)})
            b = [[c[i][j] - c[i][0] * c[0][j] / pivot for j in range(1, n)] for i in range(1, n)]
            continue
        pair = next(((i, j) for i in range(n) for j in range(i + 1, n) if b[i][j] != 0), None)
        if pair is None:
            counts["zero"] += n
            pivots.append({"kind": "zero-block", "value": str(n)})
            break
        i, j = pair
        c = reorder(b, [i, j] + [ell for ell in range(n) if ell not in pair])
        off_diagonal = c[0][1]
        counts["positive"] += 1
        counts["negative"] += 1
        pivots.append({"kind": "2x2", "value": str(off_diagonal)})
        b = [[c[r][s] - (c[r][0] * c[1][s] + c[r][1] * c[0][s]) / off_diagonal
              for s in range(2, n)] for r in range(2, n)]
    return counts, pivots


def verify(data: dict[str, Any]) -> dict[str, Any]:
    h, j, w = matrix(data["H"]), matrix(data["J"]), matrix(data["W"])
    n, k = len(h), len(w)
    if not is_symmetric(h) or not is_symmetric(w):
        raise ValueError("H and W must be symmetric")
    if len(h[0]) != n or len(w[0]) != k or len(j) != n or len(j[0]) != k:
        raise ValueError("need H n-by-n, J n-by-k, W k-by-k")
    jt = transpose(j)
    if multiply(jt, j) != [[Q(int(r == s)) for s in range(k)] for r in range(k)]:
        raise ValueError("J must have exactly orthonormal columns: J^T J = I")
    h_inverse = inverse(h)
    w_inertia, w_pivots = inertia_congruence(w)
    if w_inertia != {"positive": k, "negative": 0, "zero": 0}:
        raise ValueError("W must be strictly positive definite")
    m = add(h, multiply(multiply(j, w), jt))
    g = add(inverse(w), multiply(multiply(jt, h_inverse), j))
    h_inertia, h_pivots = inertia_congruence(h)
    m_inertia, m_pivots = inertia_congruence(m)
    g_inertia, g_pivots = inertia_congruence(g)
    left = m_inertia["positive"] + m_inertia["zero"]
    right = h_inertia["positive"] + g_inertia["negative"] + g_inertia["zero"]
    return {
        "identity_holds": left == right,
        "left_n_geq_0_M": left,
        "right_n_pos_H_plus_n_leq_0_G": right,
        "inertia": {"H": h_inertia, "M": m_inertia, "G": g_inertia, "W": w_inertia},
        "congruence_pivots": {"H": h_pivots, "M": m_pivots, "G": g_pivots, "W": w_pivots},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixture", type=Path, help="JSON fixture with H, J, W")
    parser.add_argument("--expect-invalid", action="store_true", help="require input validation to reject the fixture")
    args = parser.parse_args()
    try:
        result = verify(json.loads(args.fixture.read_text()))
    except (KeyError, ValueError, json.JSONDecodeError) as error:
        if args.expect_invalid:
            print(f"expected invalid fixture rejected: {error}")
            return
        raise SystemExit(f"fixture rejected: {error}") from error
    if args.expect_invalid:
        raise SystemExit("fixture was accepted but --expect-invalid was requested")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["identity_holds"]:
        raise SystemExit("exact inertia identity failed")


if __name__ == "__main__":
    main()
