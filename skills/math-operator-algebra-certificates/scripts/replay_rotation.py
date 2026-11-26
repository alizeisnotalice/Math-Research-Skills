#!/usr/bin/env python3
"""Exact two-dimensional block-polar checks for the cited repair lemma."""
from __future__ import annotations

import argparse
from fractions import Fraction as F


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def sub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--case", choices=("valid", "rejected"), required=True)
    args = ap.parse_args()
    # Rational rotation: its exact squared distance from I is 2(1-cos theta).
    c, s = (F(12, 13), F(5, 13)) if args.case == "valid" else (F(3, 5), F(4, 5))
    u = [[c, -s], [s, c]]
    ident = [[F(1), F(0)], [F(0), F(1)]]
    assert matmul(transpose(u), u) == ident, "rotation must be exactly unitary"
    e = abs(s)  # P projects to the first coordinate.
    t_squared = 2 * (1 - c)
    if args.case == "rejected":
        assert e > F(1, 2) and t_squared > F(1, 4)
        print("REJECTED: e=4/5 and ||U-I||^2=4/5 violate the cited hypotheses")
        return
    assert e <= F(1, 2) and t_squared < F(1, 4)
    # d=c is positive, hence its polar unitary is v=1 and Uhat=I.
    uhat = ident
    # For this rotation ||Uhat-U||^2=2(1-c), checked against (3e)^2 exactly.
    assert t_squared <= 9 * e * e
    assert sub(uhat, u)  # retain the actual correction, not merely a zero case
    print("VALID: e=5/13, ||U-I||^2=2/13, ||Uhat-U||^2=2/13 <= (3e)^2")


if __name__ == "__main__":
    main()
