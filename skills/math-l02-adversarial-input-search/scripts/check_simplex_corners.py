#!/usr/bin/env python3
"""Exactly check whether every corner of integer segments lies in a simplex."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import json
from pathlib import Path
import sys


def solve(matrix: list[list[Fraction]], right: list[Fraction]) -> list[Fraction]:
    size = len(right)
    augmented = [row[:] + [value] for row, value in zip(matrix, right)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column]), None)
        if pivot is None:
            raise ValueError("simplex vertices are affinely dependent")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        divisor = augmented[column][column]
        augmented[column] = [value / divisor for value in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            augmented[row] = [left - factor * top for left, top in zip(augmented[row], augmented[column])]
    return [augmented[row][-1] for row in range(size)]


def render(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def check(data: dict) -> dict:
    vertices = data["vertices"]
    segments = data["segments"]
    if not vertices or len(vertices) != len(vertices[0]) + 1:
        raise ValueError("vertices must describe a full-dimensional simplex")
    dimension = len(vertices[0])
    if any(len(vertex) != dimension or not all(isinstance(x, int) for x in vertex) for vertex in vertices):
        raise ValueError("vertices must be integer vectors of one dimension")
    if not segments or any(len(segment) != 2 for segment in segments):
        raise ValueError("segments must be nonempty endpoint pairs")
    if any(any(len(endpoint) != dimension or not all(isinstance(x, int) for x in endpoint) for endpoint in segment) for segment in segments):
        raise ValueError("segment endpoints must be integer vectors")
    if any(left == right for left, right in segments):
        raise ValueError("every segment must be nondegenerate")
    translate = data.get("translate", [0] * dimension)
    if len(translate) != dimension or not all(isinstance(x, int) for x in translate):
        raise ValueError("translate must be an integer vector")
    base = [Fraction(value) for value in vertices[0]]
    matrix = [[Fraction(vertices[column + 1][row] - vertices[0][row]) for column in range(dimension)]
              for row in range(dimension)]
    corners = []
    inside = True
    for choice in product((0, 1), repeat=len(segments)):
        point = [translate[coordinate] + sum(segments[index][side][coordinate] for index, side in enumerate(choice))
                 for coordinate in range(dimension)]
        coordinates = solve(matrix, [Fraction(value) - start for value, start in zip(point, base)])
        barycentric = [Fraction(1) - sum(coordinates)] + coordinates
        is_inside = all(value >= 0 for value in barycentric)
        inside &= is_inside
        corners.append({"choice": list(choice), "point": point,
                        "barycentric": [render(value) for value in barycentric], "inside": is_inside})
    return {"dimension": dimension, "segments": len(segments), "corners_checked": len(corners),
            "all_corners_in_simplex": inside, "corners": corners}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_simplex_corners.py INPUT.json")
    print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
