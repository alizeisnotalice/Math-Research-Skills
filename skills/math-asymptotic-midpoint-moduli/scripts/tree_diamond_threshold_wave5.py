#!/usr/bin/env python3
"""Exact rational arithmetic checks for two staged midpoint/diamond interfaces."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction


def q(value: str) -> Fraction:
    return Fraction(value)


def show(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def tree(args: argparse.Namespace) -> dict[str, object]:
    alpha, beta, m, M, c, gamma = map(q, (args.alpha, args.beta, args.m, args.M, args.c, args.gamma))
    if min(alpha, beta, m, M, c) <= 0 or gamma <= 0:
        raise ValueError("alpha, beta, m, M, c, gamma must all be positive")
    left = alpha * m
    right = beta * M
    factor = 1 + gamma / 2
    h = 0
    while left <= right:
        left *= factor
        h += 1
    return {"mode": "tree", "minimal_height": h, "left_at_height": show(left), "right": show(right), "modulus_argument": show(alpha*c/(2*beta*M))}


def diamond(args: argparse.Namespace) -> dict[str, object]:
    k, distortion = q(args.k), q(args.distortion)
    if k < 0 or distortion <= 0:
        raise ValueError("k must be nonnegative and distortion positive")
    d2 = distortion * distortion
    return {"mode": "diamond", "k": show(k), "D_squared": show(d2), "strong_bound_D_squared_ge_1_plus_k_over_4": d2 >= 1 + k/4, "proposition_4_2_k_le_256D_squared": k <= 256*d2}


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="mode", required=True)
    p_tree = sub.add_parser("tree")
    for name in ("alpha", "beta", "m", "M", "c", "gamma"):
        p_tree.add_argument(f"--{name}", required=True)
    p_tree.set_defaults(run=tree)
    p_diamond = sub.add_parser("diamond")
    p_diamond.add_argument("--k", required=True)
    p_diamond.add_argument("--distortion", required=True)
    p_diamond.set_defaults(run=diamond)
    args = parser.parse_args()
    print(json.dumps(args.run(args), sort_keys=True))


if __name__ == "__main__":
    main()
