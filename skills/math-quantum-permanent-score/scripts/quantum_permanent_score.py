#!/usr/bin/env python3
"""Exact score arithmetic for supplied quantum-permanent orbital profiles."""

from fractions import Fraction
from math import comb, factorial
import json
from pathlib import Path
import sys


def parse_partition(value, n):
    parts = tuple(int(piece) for piece in value.split("+"))
    if not parts or any(part < 1 for part in parts) or sum(parts) != n:
        raise ValueError(f"invalid partition {value}")
    return parts


def evaluate(data):
    n = data["n"]
    if type(n) is not int or n < 2:
        raise ValueError("n must be an integer at least 2")
    weights = {parse_partition(key, n): Fraction(value) for key, value in data["weights"].items()}
    if any(weight < 0 for weight in weights.values()) or sum(weights.values(), Fraction()) != 1:
        raise ValueError("weights must be a nonnegative probability distribution")
    score = sum(((-1) ** (n - len(partition)) * weight / comb(n, len(partition))
                 for partition, weight in weights.items()), Fraction())
    square_free = weights.get((1,) * n, Fraction())
    floor = Fraction(factorial(n), n ** n)
    result = {
        "score": str(score),
        "square_free_weight": str(square_free),
        "square_free_floor": str(floor),
        "floor_holds": square_free >= floor,
        "universal_floor_bound": str(Fraction(factorial(n + 1), n ** (n + 1)) - Fraction(1, n)),
    }
    if square_free >= floor:
        result["profile_lower_bound"] = str((1 + Fraction(1, n)) * square_free - Fraction(1, n))
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: quantum_permanent_score.py INPUT.json")
    print(json.dumps(evaluate(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
