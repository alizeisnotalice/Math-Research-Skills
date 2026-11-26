#!/usr/bin/env python3
"""Exact finite audit of the cut reconstruction in Lemma 2.1."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_number(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("coordinates must be integers or string rationals, never booleans/floats")
    if isinstance(value, (int, str)):
        return Fraction(value)
    raise ValueError("coordinates must be integers or string rationals")


def show(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def l1(vector: list[Fraction]) -> Fraction:
    return sum((abs(value) for value in vector), Fraction())


def parse(document: Any) -> list[list[Fraction]]:
    if not isinstance(document, dict) or set(document) != {"points"}:
        raise ValueError("input must be exactly an object with key 'points'")
    raw = document["points"]
    if not isinstance(raw, list) or not raw:
        raise ValueError("points must be a nonempty list")
    if not all(isinstance(row, list) and row for row in raw):
        raise ValueError("every point must be a nonempty coordinate list")
    dimension = len(raw[0])
    if any(len(row) != dimension for row in raw):
        raise ValueError("all points must have the same positive dimension")
    return [[parse_number(value) for value in row] for row in raw]


def audit(points: list[list[Fraction]]) -> dict[str, Any]:
    count, dimension = len(points), len(points[0])
    base = [min(point[k] for point in points) for k in range(dimension)]
    cuts: list[dict[str, Any]] = []
    indices = tuple(range(count))
    for size in range(1, count):
        for subset_tuple in itertools.combinations(indices, size):
            subset = set(subset_tuple)
            b = [max(Fraction(), min(points[i][k] for i in subset) - max(points[i][k] for i in indices if i not in subset)) for k in range(dimension)]
            weight = l1(b)
            if weight:
                cuts.append({"members": subset, "b": b, "weight": weight})
    reconstructions = []
    for i in indices:
        recovered = [base[k] + sum((cut["b"][k] for cut in cuts if i in cut["members"]), Fraction()) for k in range(dimension)]
        if recovered != points[i]:
            raise AssertionError("cut construction failed exact reconstruction")
        reconstructions.append([show(value) for value in recovered])
    pairs = []
    for i, j in itertools.combinations(indices, 2):
        original = l1([points[i][k] - points[j][k] for k in range(dimension)])
        weighted_l1 = sum((cut["weight"] * abs((1 if i in cut["members"] else 0) - (1 if j in cut["members"] else 0)) for cut in cuts), Fraction())
        hilbert_square = sum((cut["weight"] * ((1 if i in cut["members"] else 0) - (1 if j in cut["members"] else 0)) ** 2 for cut in cuts), Fraction())
        if not (original == weighted_l1 == hilbert_square):
            raise AssertionError("pair distance identity failed")
        pairs.append({"pair_1_based": [i + 1, j + 1], "l1_distance": show(original), "weighted_cut_l1": show(weighted_l1), "weighted_hilbert_square": show(hilbert_square)})
    return {
        "scope": "exact finite rational-coordinate ℓ1 inputs",
        "point_count": count,
        "dimension": dimension,
        "base_v": [show(value) for value in base],
        "positive_cut_count": len(cuts),
        "cuts": [{"members_1_based": [i + 1 for i in sorted(cut["members"])], "b": [show(value) for value in cut["b"]], "weight": show(cut["weight"])} for cut in cuts],
        "reconstructions": reconstructions,
        "all_pair_distance_identities_exact": True,
        "all_cut_weight_identities_exact": True,
        "contractivity_certificate": "triangle inequality plus weight=||b_B||_1 for every retained cut",
        "pairs": pairs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(audit(parse(document)), ensure_ascii=False, indent=2, sort_keys=True))
    except (OSError, ValueError, json.JSONDecodeError, AssertionError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
