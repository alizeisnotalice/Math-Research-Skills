#!/usr/bin/env python3
"""Verify a tiny LP primal/dual certificate using exact rational arithmetic."""

from fractions import Fraction as Q


def feasible_primal(x1: Q, x2: Q) -> bool:
    return x1 + x2 == 1 and x1 >= 0 and x2 >= 0


def feasible_dual(pi: Q) -> bool:
    # Dual of min 3*x1+2*x2 subject to x1+x2=1, x>=0:
    # max pi subject to pi <= 3 and pi <= 2.
    return pi <= 3 and pi <= 2


def primal_dual_gap(x1: Q, x2: Q, pi: Q) -> Q:
    # Exact weak-duality identity for A=[1,1], b=1, c=[3,2].
    return (3 * x1 + 2 * x2) - pi


def main() -> None:
    x1, x2, pi = Q(0), Q(1), Q(2)
    assert feasible_primal(x1, x2)
    assert feasible_dual(pi)
    gap = primal_dual_gap(x1, x2, pi)
    assert gap == 0
    print("primal feasible: exact (x1=0, x2=1, objective=2)")
    print("dual feasible: exact (pi=2, objective=2)")
    print(f"primal-minus-dual gap: {gap}")
    print("certificate: optimality proved by exact weak duality")

    bad_pi = Q(3)
    assert not feasible_dual(bad_pi)
    print("invalid dual pi=3 rejected: violates pi<=2")


if __name__ == "__main__":
    main()
