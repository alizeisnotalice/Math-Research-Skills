#!/usr/bin/env python3
"""Exact finite evaluation of the source's C-dependent step functional."""

import argparse
import json
from fractions import Fraction


def parse_fraction(text):
    return Fraction(text)


def potential(x, C):
    value = abs(x)
    if value <= 1:
        return value ** 3 / 6
    if value <= 2:
        return Fraction(1, 6) + (value - 1) / 2 + C * (value - 1) ** 2 / 2
    raise ValueError("the finite-cell formula only evaluates |x| <= 2")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--C", required=True, type=parse_fraction)
    parser.add_argument("--heights", required=True,
                        help="comma-separated rational cell heights on [-1,1]")
    args = parser.parse_args()
    heights = [parse_fraction(x) for x in args.heights.split(",")]
    n = len(heights)
    if args.C < 1:
        parser.error("C must be at least one")
    if n < 2 or n % 2:
        parser.error("use an even positive number of cells")
    if any(x < 0 for x in heights):
        parser.error("heights must be nonnegative")
    if heights != list(reversed(heights)):
        parser.error("heights must define an even step function")
    h = Fraction(2, n)
    if h * sum(heights) != 1:
        parser.error("heights must be normalized so h*sum(heights)=1")
    Q = h * sum(x * x for x in heights)
    for i, fi in enumerate(heights):
        for j, fj in enumerate(heights):
            m = i - j
            kappa = (potential((m + 1) * h, args.C)
                     - 2 * potential(m * h, args.C)
                     + potential((m - 1) * h, args.C))
            Q += fi * fj * kappa
    lower = 2 - Q
    print(json.dumps({"cells": n, "Q": str(Q), "p_lower_bound": str(lower),
                      "p_lower_bound_decimal": float(lower)}))


if __name__ == "__main__":
    main()
