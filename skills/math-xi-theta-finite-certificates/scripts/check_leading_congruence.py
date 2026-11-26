#!/usr/bin/env python3
"""Exact check of the leading-principal-minor congruence gate.

For a symmetric rational matrix A and a lower triangular rational L,
the leading k-by-k block of B=L A L^T is L_k A_k L_k^T.  This script
replays that identity on two fixed dyadic inputs and verifies its exact
determinant consequence.  It performs no Xi, zero, interval, or PF check.
"""
from fractions import Fraction as Q


def matmul(left, right):
    return [[sum((left[i][h] * right[h][j] for h in range(len(right))), Q())
             for j in range(len(right[0]))]
            for i in range(len(left))]


def transpose(matrix):
    return [list(row) for row in zip(*matrix)]


def determinant(matrix):
    """Exact Gaussian elimination for the finite rational inputs below."""
    work = [row[:] for row in matrix]
    n, answer = len(work), Q(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col]), None)
        if pivot is None:
            return Q()
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            answer = -answer
        value = work[col][col]
        answer *= value
        for row in range(col + 1, n):
            factor = work[row][col] / value
            for j in range(col + 1, n):
                work[row][j] -= factor * work[col][j]
    return answer


def leading(matrix, k):
    return [row[:k] for row in matrix[:k]]


def check(name, a, lower):
    n = len(a)
    assert n == len(lower) and all(len(row) == n for row in a + lower)
    assert all(lower[i][j] == 0 for i in range(n) for j in range(i + 1, n))
    assert all(lower[i][i] != 0 for i in range(n))
    b = matmul(matmul(lower, a), transpose(lower))
    for k in range(1, n + 1):
        ak, lk, bk = leading(a, k), leading(lower, k), leading(b, k)
        assert bk == matmul(matmul(lk, ak), transpose(lk))
        lhs = determinant(bk)
        rhs = determinant(lk) ** 2 * determinant(ak)
        assert lhs == rhs
        if determinant(ak):
            assert (lhs > 0) == (determinant(ak) > 0)
        else:
            assert lhs == 0
        print(f"PASS: {name}, k={k}, det(A_k)={determinant(ak)}, det(B_k)={lhs}")


def main():
    # Nonsingular mixed-sign example with dyadic entries.
    check("mixed-sign", [
        [Q(2), Q(1), -Q(1, 2), Q(3, 4)],
        [Q(1), -Q(3), Q(5, 4), -Q(1)],
        [-Q(1, 2), Q(5, 4), Q(1, 2), Q(2)],
        [Q(3, 4), -Q(1), Q(2), Q(4)],
    ], [
        [Q(3, 2), Q(), Q(), Q()],
        [-Q(1, 4), -Q(5, 4), Q(), Q()],
        [Q(3, 8), Q(1, 2), Q(7, 4), Q()],
        [-Q(1, 2), Q(3, 4), -Q(1, 8), Q(11, 8)],
    ])
    # Singular leading block: zero is preserved as well as a strict sign.
    check("singular-leading", [
        [Q(1), Q(2), Q()],
        [Q(2), Q(4), Q(1)],
        [Q(), Q(1), Q(3)],
    ], [
        [Q(1, 2), Q(), Q()],
        [Q(1, 4), -Q(3, 2), Q()],
        [-Q(1), Q(1, 8), Q(5, 4)],
    ])
    print("ALL EXACT LEADING-CONGRUENCE CHECKS PASSED")


if __name__ == "__main__":
    main()
