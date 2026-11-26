#!/usr/bin/env python3
"""Exact algebra check for the smooth-factor normalized-volume identity."""

from __future__ import annotations

import argparse
from fractions import Fraction


def positive_fraction(value: str) -> Fraction:
    parsed = Fraction(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("must be strictly positive")
    return parsed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("N", type=int)
    parser.add_argument("A", type=positive_fraction)
    parser.add_argument("sigma", type=positive_fraction)
    args = parser.parse_args()
    if args.N < 1:
        parser.error("N must be at least 1")
    a = args.A / args.N
    extended = ((args.A + a) ** (args.N + 1) * (args.sigma / a)
                / ((args.N + 1) ** (args.N + 1)))
    base = args.A ** args.N * args.sigma / (args.N ** args.N)
    if extended != base:
        raise AssertionError("exact identity failed")
    print(f"a={a}")
    print(f"normalized_base={base}")
    print(f"normalized_extended={extended}")
    print("identity=verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
