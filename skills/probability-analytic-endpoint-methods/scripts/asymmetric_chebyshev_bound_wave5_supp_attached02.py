#!/usr/bin/env python3
"""Exact evaluator for Theorem 2.2's standardized asymmetric tail bound."""

import argparse
import json
from fractions import Fraction
from pathlib import Path


def fraction(value):
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    if isinstance(value, list) and len(value) == 2:
        return Fraction(value[0], value[1])
    raise ValueError("u and v must be integers, strings, or [numerator, denominator]")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON object containing positive u and v")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text())
        u, v = fraction(data["u"]), fraction(data["v"])
        if not (0 < v <= u):
            raise ValueError("require 0 < v <= u for the source's stated orientation")
    except (KeyError, TypeError, ValueError, ZeroDivisionError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    if u <= 1 / v:
        branch, bound = "trivial", Fraction(1)
    elif u <= v + 2 / v:
        branch, bound = "shifted-chebyshev", (4 + (u - v) ** 2) / (u + v) ** 2
    else:
        branch, bound = "one-sided-cantelli", 1 / (1 + v**2)
    print(json.dumps({
        "u": str(u),
        "v": str(v),
        "branch": branch,
        "sharp_upper_bound": str(bound),
        "claim": "For mean-zero, variance-one Z: P(Z <= -u or Z >= v) <= sharp_upper_bound.",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
