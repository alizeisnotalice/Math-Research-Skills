#!/usr/bin/env python3
"""Check selected exact trace-moment identities for a finite simple graph."""

from __future__ import annotations

import json
from itertools import combinations, permutations
from pathlib import Path
import sys


def matrix_product(left: list[list[int]], right: list[list[int]]) -> list[list[int]]:
    size = len(left)
    return [[sum(left[i][k] * right[k][j] for k in range(size)) for j in range(size)] for i in range(size)]


def trace_power(matrix: list[list[int]], power: int) -> int:
    size = len(matrix)
    result = [[int(i == j) for j in range(size)] for i in range(size)]
    for _ in range(power):
        result = matrix_product(result, matrix)
    return sum(result[i][i] for i in range(size))


def simple_cycles(matrix: list[list[int]], length: int) -> int:
    size = len(matrix)
    found: set[tuple[int, ...]] = set()
    for chosen in combinations(range(size), length):
        start = min(chosen)
        for tail in permutations((vertex for vertex in chosen if vertex != start)):
            cycle = (start, *tail)
            if not all(matrix[cycle[i]][cycle[(i + 1) % length]] for i in range(length)):
                continue
            reverse = (start, *reversed(tail))
            found.add(min(cycle, reverse))
    return len(found)


def check(payload: dict) -> dict:
    matrix = payload.get("adjacency")
    if not isinstance(matrix, list) or not matrix:
        raise ValueError("adjacency must be a nonempty square 0-1 matrix")
    size = len(matrix)
    if any(not isinstance(row, list) or len(row) != size for row in matrix):
        raise ValueError("adjacency must be square")
    if any(entry not in (0, 1) for row in matrix for entry in row):
        raise ValueError("adjacency entries must be 0 or 1")
    if any(matrix[i][i] or matrix[i][j] != matrix[j][i] for i in range(size) for j in range(size)):
        raise ValueError("adjacency must describe a loop-free undirected graph")
    degrees = [sum(row) for row in matrix]
    edges = sum(degrees) // 2
    cycles4 = simple_cycles(matrix, 4) if size >= 4 else 0
    trace2 = trace_power(matrix, 2)
    trace4 = trace_power(matrix, 4)
    predicted4 = 2 * edges + 4 * sum(degree * (degree - 1) // 2 for degree in degrees) + 8 * cycles4
    result = {"vertices": size, "edges": edges, "degrees": degrees, "trace_A2": trace2,
              "trace_A4": trace4, "four_cycles": cycles4,
              "fourth_moment_identity": trace4 == predicted4}
    odd_girth = payload.get("odd_girth")
    if odd_girth is not None:
        if type(odd_girth) is not int or odd_girth < 3 or odd_girth % 2 != 1:
            raise ValueError("odd_girth must be an odd integer at least 3")
        lower = {str(power): trace_power(matrix, power) for power in range(1, odd_girth, 2)}
        cycles = simple_cycles(matrix, odd_girth) if odd_girth <= size else 0
        if cycles == 0:
            raise ValueError("odd_girth must be realized by at least one simple cycle")
        trace = trace_power(matrix, odd_girth)
        result.update(odd_girth=odd_girth, lower_odd_traces=lower, odd_girth_cycles=cycles,
                      odd_girth_identity=(all(value == 0 for value in lower.values()) and trace == 2 * odd_girth * cycles),
                      trace_A_odd_girth=trace)
    return result


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_spectral_moments.py INPUT.json")
    try:
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), ensure_ascii=False, sort_keys=True))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
