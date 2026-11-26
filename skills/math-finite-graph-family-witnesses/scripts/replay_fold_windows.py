#!/usr/bin/env python3
"""Verify the explicit folded windows and their ordered state overlaps."""

import argparse
from itertools import combinations
import json

from verify_window_coloring import F9, F11, INPUT_EDGES, OUTPUT_EDGES, VERTICES


def neighbours(i, j, size):
    return (i - j) % size in (1, size - 1)


def mycielski_adjacent(a, b, size, extended):
    role_a, i = a
    role_b, j = b
    if role_a == role_b:
        return role_a == "v" and neighbours(i, j, size)
    if "w" in (role_a, role_b):
        return "u" in (role_a, role_b)
    return i != j if extended else neighbours(i, j, size)


def window(start, smaller, larger):
    vertices = {"w": (("w", None), ("w", None))}
    for offset in range(3):
        i = (start + offset) % larger
        if i < smaller:
            folded = i
        else:
            folded = smaller - 2 + ((i - smaller) % 2)
        for role in ("u", "v"):
            vertices[f"{role}{offset + 1}"] = ((role, folded), (role, i))
    return vertices


def check(family, smaller, larger):
    if not (3 <= smaller < larger and smaller % 2 == larger % 2 == 1):
        raise ValueError("require odd integers 3 <= k < K")
    extended = family == "muext"
    window_types = {frozenset(map(frozenset, edges)): name
                    for name, edges in (("F9", F9), ("F11", F11))}
    types = []
    for i in range(larger):
        current = window(i, smaller, larger)
        following = window(i + 1, smaller, larger)
        if len(set(current.values())) != len(VERTICES):
            raise ValueError(f"window {i} repeats a vertex")
        actual = set()
        for a, b in combinations(VERTICES, 2):
            (a1, a2), (b1, b2) = current[a], current[b]
            if mycielski_adjacent(a1, b1, smaller, extended) and mycielski_adjacent(a2, b2, larger, True):
                actual.add(frozenset((a, b)))
        kind = window_types.get(frozenset(actual))
        if kind is None:
            raise ValueError(f"window {i} does not induce F9 or F11")
        types.append(kind)
        outlet = [(current[a], current[b]) for a, b in OUTPUT_EDGES]
        inlet = [(following[a], following[b]) for a, b in INPUT_EDGES]
        if outlet != inlet:
            raise ValueError(f"ordered states disagree at window {i}")
    return {
        "family": family,
        "k": smaller,
        "K": larger,
        "window_types": types,
        "all_induced_windows_F9_or_F11": True,
        "five_edge_state_overlap": True,
        "odd_window_count": larger,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--family", choices=("mu", "muext"), required=True)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--K", type=int, required=True)
    args = parser.parse_args()
    try:
        result = check(args.family, args.k, args.K)
    except ValueError as err:
        parser.error(str(err))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
