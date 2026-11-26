#!/usr/bin/env python3
"""Exact, Horn-only two-cone disjunctive P+N certificate.

This is deliberately *not* a copositivity recognizer.  It verifies only the
two rational cones and P+N identities printed in Ahmadi et al., arXiv:
2605.28674v1, physical pp. 28--29 (SHA-256 6e6581b0...ae81c4c).
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction as Q


class CertificateError(ValueError):
    pass


Z = Q(0)
O = Q(1)
HALF = Q(1, 2)


def matrix(rows):
    return [[Q(x) for x in row] for row in rows]


H = matrix([
    [1, -1, 1, 1, -1],
    [-1, 1, -1, 1, 1],
    [1, -1, 1, -1, 1],
    [1, 1, -1, 1, -1],
    [-1, 1, 1, -1, 1],
])
V1 = matrix([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, HALF],
    [0, 0, 0, 0, HALF],
])
V2 = matrix([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, HALF, 0],
    [0, 0, 0, HALF, 1],
])
U1 = [O, -O, O, -O, Z]
U2 = [O, -O, O, Z, -O]
N1 = matrix([
    [0, 0, 0, 2, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
])
N2 = matrix([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 2],
    [0, 1, 0, 0, 0],
    [0, 0, 2, 0, 0],
])


def eye(n):
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))]
            for i in range(len(a))]


def outer(u):
    return [[x * y for y in u] for x in u]


def require(condition, message):
    if not condition:
        raise CertificateError(message)


def solve(a, b):
    """Exact Gauss--Jordan solution for the small invertible branch matrices."""
    n = len(a)
    work = [list(a[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = next((r for r in range(col, n) if work[r][col] != 0), None)
        require(pivot is not None, "branch matrix is singular")
        work[col], work[pivot] = work[pivot], work[col]
        scale = work[col][col]
        work[col] = [x / scale for x in work[col]]
        for row in range(n):
            if row != col:
                factor = work[row][col]
                work[row] = [work[row][j] - factor * work[col][j]
                             for j in range(n + 1)]
    return [work[i][-1] for i in range(n)]


# On x_4 >= x_5 use y=L1x=(x1,x2,x3,x4-x5,2x5).
# On x_5 >= x_4 use y=L2x=(x1,x2,x3,2x4,x5-x4).
L1 = matrix([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, -1],
    [0, 0, 0, 0, 2],
])
L2 = matrix([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 2, 0],
    [0, 0, 0, -1, 1],
])


def assert_branch_identities(v1=V1, v2=V2):
    require(mm(v1, L1) == eye(5), "V1 L1 is not the identity")
    require(mm(v2, L2) == eye(5), "V2 L2 is not the identity")
    # The only signs not automatic from x>=0 are x4-x5 and x5-x4.
    for x in ([Q(3), Q(1), Q(4), Q(7), Q(2)],
              [Q(3), Q(1), Q(4), Q(2), Q(7)],
              [Q(0), Q(0), Q(0), Q(5), Q(5)]):
        require(all(t >= 0 for t in x), "test point escaped R_+^5")
        y1, y2 = mv(L1, x), mv(L2, x)
        if x[3] >= x[4]:
            require(all(t >= 0 for t in y1) and mv(v1, y1) == x,
                    "ordered V1 branch failed")
        if x[4] >= x[3]:
            require(all(t >= 0 for t in y2) and mv(v2, y2) == x,
                    "ordered V2 branch failed")


def assert_pn_identity(v, u, n, h=H):
    p = outer(u)
    require(mm(transpose(v), mm(h, v)) == add(p, n),
            "exact congruence identity V^T H V=P+N failed")
    require(all(entry >= 0 for row in n for entry in row),
            "N is not entrywise nonnegative")
    # P=uu^T is rank-one PSD: y^T P y=(u^T y)^2.
    require(any(t != 0 for t in u), "rank-one PSD factor is zero")
    for y in ([Q(0)] * 5, [Q(1), Q(2), Q(3), Q(4), Q(5)]):
        quad_p = sum(y[i] * p[i][j] * y[j] for i in range(5) for j in range(5))
        quad_n = sum(y[i] * n[i][j] * y[j] for i in range(5) for j in range(5))
        require(quad_p == sum(u[i] * y[i] for i in range(5)) ** 2 and quad_p >= 0,
                "PSD rank-one check failed")
        require(quad_n >= 0, "nonnegative-matrix quadratic check failed")


def positive():
    assert_branch_identities()
    assert_pn_identity(V1, U1, N1)
    assert_pn_identity(V2, U2, N2)
    return {
        "status": "verified",
        "scope": "only the printed 5x5 Horn two-cone certificate",
        "source": "arXiv:2605.28674v1, SHA-256 6e6581b0fab0b52347c7ec6e7bc00a2ee8cad7f51cc79a383625bde81ae81c4c, physical pp.28-29",
        "branches": ["x4 >= x5: x=V1(x1,x2,x3,x4-x5,2x5)",
                     "x5 >= x4: x=V2(x1,x2,x3,2x4,x5-x4)"],
        "checked": ["V1 L1=I", "V2 L2=I", "V_i^T H V_i=P_i+N_i",
                    "P_i=u_i u_i^T is rank-one PSD", "N_i is entrywise nonnegative"],
    }


def expected_bad_congruence():
    h_bad = [row[:] for row in H]
    h_bad[0][0] += 1
    assert_pn_identity(V1, U1, N1, h_bad)


def expected_bad_coverage():
    v1_bad = [row[:] for row in V1]
    # Keep V1 invertible but narrow its fifth ray to e4+(1/4)e5.  Its cone
    # then requires x4>=4x5, leaving a genuine gap with V2 (which requires
    # x5>=x4), witnessed by x=(0,0,0,2,1).
    v1_bad[3][4] = O
    v1_bad[4][4] = Q(1, 4)
    x = [Z, Z, Z, Q(2), Q(1)]
    y1, y2 = solve(v1_bad, x), solve(V2, x)
    require(all(t >= 0 for t in y1) or all(t >= 0 for t in y2),
            "perturbed V1/V2 do not cover x=(0,0,0,2,1)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", choices=("positive", "perturb-horn", "perturb-coverage"),
                        default="positive")
    args = parser.parse_args()
    try:
        if args.case == "positive":
            print(json.dumps(positive(), indent=2))
        elif args.case == "perturb-horn":
            expected_bad_congruence()
            raise CertificateError("perturb-horn unexpectedly passed")
        else:
            expected_bad_coverage()
            raise CertificateError("perturb-coverage unexpectedly passed")
    except CertificateError as error:
        print("rejected: " + str(error), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
