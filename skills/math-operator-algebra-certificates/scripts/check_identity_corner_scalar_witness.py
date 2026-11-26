#!/usr/bin/env python3
"""Exact scalar witness for the identity-corner commutator assembly.

No floating point arithmetic is used.  The instance and formula are from the
finite algebraic portion of Proposition 3.2 cited in ../references/identity-corner-commutator.md.
"""

from fractions import Fraction as F
import json


def matmul(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def sub(left, right):
    return [[left[i][j] - right[i][j] for j in range(2)] for i in range(2)]


def as_text(matrix):
    return [[str(entry) for entry in row] for row in matrix]


def main():
    # Coefficient algebra N=C.  Thus every coefficient commutator vanishes.
    A, D, F_lower = F(1), F(-1), F(-1)
    U = V = Z = T = F(0)
    Q, sigma = F(-1), F(122)
    x, lam = F(2), F(1)

    rho0 = 2 * lam + x + 1
    source_sigma = 2 * (rho0**2 + (2 * x + 1) * rho0 + 6 * lam + 2 * x + 1)
    assert sigma == source_sigma == 122

    d0 = U * V - V * U - A
    d1 = (Z * V - V * Z) + d0 * U - Z + (U * (T * Z) - (T * Z) * U) - F_lower
    assert A + D == (U * V - V * U) + (Z * T - T * Z)
    assert sigma * (Q - d0) == Q * Q - D * Q + Q * (A - U) + d1

    u_tilde = sigma + U
    bc = [[u_tilde, F(1)], [Z, F(0)]]
    cc = [[V, T], [Q - d0 + T * Z, V + 1 - u_tilde * T]]
    s = [[F(1), F(0)], [Q, F(1)]]
    s_inv = [[F(1), F(0)], [-Q, F(1)]]
    b = matmul(matmul(s, bc), s_inv)
    c = matmul(matmul(s, cc), s_inv)
    commutator = sub(matmul(b, c), matmul(c, b))
    target = [[A, F(1)], [F_lower, D]]
    assert commutator == target

    # Exact spectral-norm check: target^* target has eigenvalues 0 and 4.
    gram = matmul([[target[j][i] for j in range(2)] for i in range(2)], target)
    trace, determinant = gram[0][0] + gram[1][1], gram[0][0] * gram[1][1] - gram[0][1] * gram[1][0]
    assert (trace, determinant) == (F(4), F(0))

    # The source fixed-point map has this exact fixed point; this is local
    # witness data, not a replacement for the source's ball contraction proof.
    psi_q = d0 + (Q * Q - D * Q + Q * (A - U) + d1) / sigma
    derivative_at_q = (2 * Q - D + A - U) / sigma
    assert psi_q == Q and derivative_at_q == 0

    print(json.dumps({
        "status": "pass",
        "coefficient_algebra": "C",
        "sigma": str(sigma),
        "riccati_certificate": "exact",
        "target": as_text(target),
        "B": as_text(b),
        "C": as_text(c),
        "commutator": as_text(commutator),
        "target_gram_trace": str(trace),
        "target_gram_determinant": str(determinant),
        "spectral_norm": "2",
        "fixed_point_derivative": str(derivative_at_q),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
