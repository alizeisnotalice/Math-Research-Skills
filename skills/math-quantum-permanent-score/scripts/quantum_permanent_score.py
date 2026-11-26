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
    return tuple(sorted(parts, reverse=True))


def read_document(document):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"duplicate JSON key {key}")
            result[key] = value
        return result

    return json.loads(document, object_pairs_hook=unique_object)


def evaluate(data):
    n = data["n"]
    if type(n) is not int or n < 2:
        raise ValueError("n must be an integer at least 2")
    weights = {}
    for key, value in data["weights"].items():
        partition = parse_partition(key, n)
        if partition in weights:
            raise ValueError(f"multiple keys for partition {partition}")
        if type(value) not in (int, str):
            raise ValueError("use integers or exact rational strings for weights")
        weights[partition] = Fraction(value)
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
    try:
        result = evaluate(read_document(Path(sys.argv[1]).read_text()))
    except (OSError, KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        raise SystemExit(str(error)) from error
    print(json.dumps(result, sort_keys=True))
