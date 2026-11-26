#!/usr/bin/env python3
"""Round a rational simplex vector to denominator D using exact fractions.

This is the finite construction in Lemma 2.1(b) of the audited paper.
It does not depend on the paper's claimed global approximate-Nash result.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path
from typing import Any


def parse_fraction(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("Boolean values are not rational input")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("each coordinate must be an integer or p/q string")


def round_simplex(w: list[Fraction], denominator: int) -> list[Fraction]:
    """Largest-remainder rounding with ties toward the lower index."""
    if denominator < 1:
        raise ValueError("D must be a positive integer")
    if not w or any(x < 0 for x in w) or sum(w, Fraction()) != 1:
        raise ValueError("w must be a nonempty probability vector")
    floors = [(denominator * x.numerator) // x.denominator for x in w]
    remainders = [denominator * x - q for x, q in zip(w, floors, strict=True)]
    deficit = denominator - sum(floors)
    if not 0 <= deficit < len(w):
        raise AssertionError("the fractional-part invariant failed")
    chosen = set(sorted(range(len(w)), key=lambda i: (-remainders[i], i))[:deficit])
    counts = [q + int(i in chosen) for i, q in enumerate(floors)]
    if sum(counts) != denominator or any(q < 0 for q in counts):
        raise AssertionError("rounded counts are not a denominator-D simplex point")
    return [Fraction(q, denominator) for q in counts]


def serialise(vector: list[Fraction]) -> list[str]:
    return [str(x) for x in vector]


def run_input(data: Any) -> dict[str, Any]:
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    raw_w, denominator = data["w"], data["D"]
    if isinstance(denominator, bool) or not isinstance(denominator, int):
        raise ValueError("D must be an integer")
    if not isinstance(raw_w, list):
        raise ValueError("w must be a JSON array")
    w = [parse_fraction(x) for x in raw_w]
    x = round_simplex(w, denominator)
    l1_error = sum((abs(a - b) for a, b in zip(x, w, strict=True)), Fraction())
    return {
        "status": "certified",
        "D": denominator,
        "input": serialise(w),
        "output": serialise(x),
        "integer_counts": [item.numerator * denominator // item.denominator for item in x],
        "l1_error": str(l1_error),
        "l1_bound": str(Fraction(len(w), denominator)),
        "tie_rule": "larger remainder first, then smaller zero-based index",
    }


def simplex_points(dimension: int, denominator: int):
    for cuts in itertools.combinations(range(denominator + dimension - 1), dimension - 1):
        marks = (-1, *cuts, denominator + dimension - 1)
        counts = [marks[i + 1] - marks[i] - 1 for i in range(dimension)]
        yield [Fraction(q, denominator) for q in counts]


def self_test() -> None:
    checked = 0
    for dimension in range(1, 6):
        for source_denominator in range(1, 8):
            for target_denominator in range(1, 8):
                for w in simplex_points(dimension, source_denominator):
                    x = round_simplex(w, target_denominator)
                    error = sum((abs(a - b) for a, b in zip(x, w, strict=True)), Fraction())
                    assert sum(x, Fraction()) == 1
                    assert all(item >= 0 and (item * target_denominator).denominator == 1 for item in x)
                    assert error <= Fraction(dimension, target_denominator)
                    checked += 1
    # Equal remainders must use the lower indices.
    assert round_simplex([Fraction(1, 3)] * 3, 2) == [Fraction(1, 2), Fraction(1, 2), Fraction()]
    print(json.dumps({"exact_simplex_cases_checked": checked, "tie_example": ["1/2", "1/2", "0"]}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.input is None:
        parser.error("provide INPUT.json or --self-test")
    try:
        print(json.dumps(run_input(json.loads(args.input.read_text(encoding="utf-8"))), indent=2))
    except (OSError, ValueError, KeyError, ZeroDivisionError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
