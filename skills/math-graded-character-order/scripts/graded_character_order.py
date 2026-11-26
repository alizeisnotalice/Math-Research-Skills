#!/usr/bin/env python3
"""Exact cumulative comparison of two finite graded multiplicity arrays."""

import json
from pathlib import Path
import sys


def evaluate(data):
    left = data["left_coefficients"]
    right = data["right_coefficients"]
    if (not left or not right or any(type(x) is not int or x < 0 for x in left + right)
            or sum(left) != sum(right)):
        raise ValueError("arrays must be nonempty nonnegative integers with equal total")
    degree = max(len(left), len(right))
    left = left + [0] * (degree - len(left))
    right = right + [0] * (degree - len(right))
    cumulative = []
    running = 0
    for a, b in zip(left, right):
        running += a - b
        cumulative.append(running)
    return {
        "common_total": sum(left),
        "divided_difference_coefficients": cumulative,
        "left_stochastically_no_larger": min(cumulative) >= 0,
        "optimal_unmatched_multiplicity": max(0, -min(cumulative)),
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: graded_character_order.py INPUT.json")
    print(json.dumps(evaluate(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
