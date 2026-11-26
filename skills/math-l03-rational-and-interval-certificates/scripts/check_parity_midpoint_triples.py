#!/usr/bin/env python3
"""Check the midpoint-triple injection in one mod-two residue class."""

from __future__ import annotations

from itertools import combinations
import json
from pathlib import Path
import sys


def check(data: dict) -> dict:
    points = [tuple(point) for point in data["points"]]
    if len(points) < 3 or len(set(points)) != len(points):
        raise ValueError("points must be at least three distinct integer vectors")
    dimension = len(points[0])
    if any(len(point) != dimension or not all(isinstance(value, int) for value in point) for point in points):
        raise ValueError("points must be integer vectors of the same dimension")
    residue = tuple(value % 2 for value in points[0])
    if any(tuple(value % 2 for value in point) != residue for point in points):
        raise ValueError("all points must be in one mod-two class")
    images = {}
    for triple in combinations(points, 3):
        midpoints = tuple(sorted(tuple((left + right) // 2 for left, right in zip(first, second))
                                 for first, second in combinations(triple, 2)))
        if len(set(midpoints)) != 3:
            raise AssertionError("a distinct triple produced repeated midpoints")
        possibilities = set()
        for omitted in range(3):
            first, second = (midpoints[index] for index in range(3) if index != omitted)
            third = midpoints[omitted]
            possibilities.add(tuple(first[c] + second[c] - third[c] for c in range(dimension)))
        if set(triple) != possibilities:
            raise AssertionError("midpoint triple did not recover the original triple")
        if midpoints in images:
            raise AssertionError("two triples have the same midpoint triple")
        images[midpoints] = triple
    return {"dimension": dimension, "residue_mod_2": list(residue), "points": len(points),
            "triples_checked": len(images), "midpoint_triple_injective": True}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_parity_midpoint_triples.py INPUT.json")
    print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
