#!/usr/bin/env python3
"""Exact algebra check for the restricted ell-infinity projection deficit."""

from __future__ import annotations

import argparse
from fractions import Fraction


def certify(values: list[Fraction]) -> dict[str, Fraction | int]:
    if not values:
        raise ValueError("supply at least one coordinate")
    if any(x < 0 for x in values):
        raise ValueError("coordinates must be nonnegative")
    if any(values[i] < values[i + 1] for i in range(len(values) - 1)):
        raise ValueError("coordinates must be in nonincreasing order")
    n = len(values)
    norm_sq = sum((x * x for x in values), Fraction())
    if norm_sq != 1:
        raise ValueError(f"squared norm must equal 1, got {norm_sq}")
    total = sum(values, Fraction())
    pair_sum = sum((x - y) ** 2 for x in values for y in values)
    half_variance = (Fraction(1) - total * total / n) / 2
    lower_bound = pair_sum / (4 * n)
    if half_variance != lower_bound:
        raise AssertionError("variance identity failed")
    return {"n": n, "sum": total, "pair_sum": pair_sum,
            "lower_bound": lower_bound}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("coordinates", nargs="*")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    cases = (["4/5", "3/5"], ["1/2", "1/2", "1/2", "1/2"]) if args.self_test else [args.coordinates]
    for tokens in cases:
        result = certify([Fraction(x) for x in tokens])
        print("n={n} sum={sum} pair_sum={pair_sum} lower_bound={lower_bound}".format(**result))


if __name__ == "__main__":
    main()
