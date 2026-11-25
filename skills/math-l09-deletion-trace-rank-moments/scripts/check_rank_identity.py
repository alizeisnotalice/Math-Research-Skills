#!/usr/bin/env python3
"""Exact finite checks of the deletion-trace rank-moment identity.

This tests two finite rational instances of
    prod_r(q + p*u_r) G(u) = p^k F(q + p*u).
It does not constitute a general proof or a trace-reconstruction algorithm.
"""

from fractions import Fraction
from itertools import combinations
from math import comb


def rank_moment_coefficient(indices, ranks, p):
    """Coefficient of X_indices in E[product(trace[r] for r in ranks)]."""
    q = 1 - p
    coefficient = Fraction(comb(indices[0] - 1, ranks[0] - 1), 1)
    for r in range(len(indices) - 1):
        available = indices[r + 1] - indices[r] - 1
        requested = ranks[r + 1] - ranks[r] - 1
        if available < requested:
            return Fraction(0)
        coefficient *= comb(available, requested)
    return coefficient * p ** ranks[-1] * q ** (indices[-1] - ranks[-1])


def check(n, k, p, u, delta):
    """Evaluate both sides with arbitrary rational coefficients Delta."""
    q = 1 - p
    z = [q + p * value for value in u]
    input_tuples = list(combinations(range(1, n + 1), k))

    f_value = Fraction(0)
    for indices in input_tuples:
        term = z[0] ** indices[0]
        for r in range(1, k):
            term *= z[r] ** (indices[r] - indices[r - 1])
        f_value += delta[indices] * term

    g_value = Fraction(0)
    for ranks in combinations(range(1, n + 1), k):
        trace_coefficient = sum(
            (delta[indices] * rank_moment_coefficient(indices, ranks, p)
             for indices in input_tuples),
            Fraction(0),
        )
        term = u[0] ** (ranks[0] - 1)
        for r in range(1, k):
            term *= u[r] ** (ranks[r] - ranks[r - 1] - 1)
        g_value += trace_coefficient * term

    lhs = g_value
    for value in z:
        lhs *= value
    return lhs, p ** k * f_value


def main():
    cases = [
        (5, 2, Fraction(2, 3), [Fraction(1, 5), Fraction(-1, 4)]),
        (6, 3, Fraction(3, 5), [Fraction(1, 7), Fraction(2, 9), Fraction(-2, 7)]),
    ]
    for n, k, p, u in cases:
        delta = {
            indices: Fraction(((sum(indices) * 7 + len(indices) * 3) % 11) - 5, 13)
            for indices in combinations(range(1, n + 1), k)
        }
        lhs, rhs = check(n, k, p, u, delta)
        print(f"n={n}, k={k}, p={p}: LHS==RHS {lhs == rhs}; exact difference={lhs - rhs}")


if __name__ == "__main__":
    main()
