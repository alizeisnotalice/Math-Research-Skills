#!/usr/bin/env python3
"""Exact connectivity probability for a finite independent edge list."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path


def merge(partition: tuple[int, ...], u: int, v: int) -> tuple[int, ...]:
    if partition[u] == partition[v]:
        return partition
    keep, drop = sorted((partition[u], partition[v]))
    return tuple(keep if value == drop else value for value in partition)


def probability(data: dict) -> Fraction:
    if not isinstance(data, dict) or type(data.get("vertices")) is not int or data["vertices"] < 1:
        raise ValueError("vertices must be a positive integer")
    size = data["vertices"]

    def vertex(value):
        if type(value) is not int or not 0 <= value < size:
            raise ValueError("invalid vertex index")
        return value

    terminals = data.get("terminals")
    if not isinstance(terminals, list) or len(terminals) != 2:
        raise ValueError("terminals must contain two vertex indices")
    source, target = map(vertex, terminals)
    partition = tuple(range(size))

    wiring = data.get("wiring", [])
    if not isinstance(wiring, list) or not all(isinstance(group, list) for group in wiring):
        raise ValueError("wiring must be an array of index arrays")
    for group in wiring:
        indices = [vertex(value) for value in group]
        for value in indices[1:]:
            partition = merge(partition, indices[0], value)

    edges = data.get("edges")
    if not isinstance(edges, list):
        raise ValueError("edges must be an array")
    parsed_edges = []
    for edge in edges:
        if not isinstance(edge, list) or len(edge) != 3:
            raise ValueError("edge must contain two vertex indices and a rational probability")
        u, v = map(vertex, edge[:2])
        if type(edge[2]) not in (int, str):
            raise ValueError("edge probability must be an integer or exact rational string")
        p = Fraction(edge[2])
        if not 0 <= p <= 1:
            raise ValueError("edge probability outside [0,1]")
        parsed_edges.append((u, v, p))

    weights = {partition: Fraction(1)}
    success = Fraction(0)
    for u, v, p in parsed_edges:
        following = defaultdict(Fraction)
        for state, mass in weights.items():
            if state[source] == state[target]:
                success += mass
                continue
            if p != 1:
                following[state] += (1 - p) * mass
            if p != 0:
                following[merge(state, u, v)] += p * mass
        weights = following
    return success + sum((mass for state, mass in weights.items() if state[source] == state[target]), Fraction(0))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        print(probability(json.loads(args.input.read_text(encoding="utf-8"))))
    except (OSError, ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
