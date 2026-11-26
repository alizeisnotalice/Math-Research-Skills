#!/usr/bin/env python3
"""Exhaustively verify the two-colouring of the F9/F11 window states."""

from collections import deque
import hashlib
import json


VERTICES = ("w", "v1", "v2", "v3", "u1", "u2", "u3")
F9 = (
    ("w", "u1"), ("w", "u2"), ("w", "u3"),
    ("v1", "v2"), ("v2", "v3"), ("u1", "v2"),
    ("u2", "v1"), ("u2", "v3"), ("u3", "v2"),
)
F11 = F9 + (("u1", "v3"), ("u3", "v1"))
INPUT_EDGES = (("w", "u1"), ("w", "u2"), ("v1", "v2"), ("v1", "u2"), ("u1", "v2"))
OUTPUT_EDGES = (("w", "u2"), ("w", "u3"), ("v2", "v3"), ("v2", "u3"), ("u2", "v3"))


def state(directions, edges):
    return sum((directions[frozenset(edge)] == edge) << bit
               for bit, edge in enumerate(edges))


def has_property_p(directions, adjacency):
    outgoing = {v: set() for v in VERTICES}
    for a, b in directions.values():
        outgoing[a].add(b)
    for a in VERTICES:
        for c in outgoing[a]:
            for d in outgoing[c]:
                for b in outgoing[d] & adjacency[a]:
                    if d not in adjacency[a] or b not in adjacency[c]:
                        return False
    return True


def constraints(edges):
    adjacency = {v: set() for v in VERTICES}
    for a, b in edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    pairs = set()
    accepted = 0
    for mask in range(1 << len(edges)):
        directions = {
            frozenset((a, b)): (a, b) if mask & (1 << bit) else (b, a)
            for bit, (a, b) in enumerate(edges)
        }
        if has_property_p(directions, adjacency):
            accepted += 1
            inlet = state(directions, INPUT_EDGES)
            outlet = state(directions, OUTPUT_EDGES)
            pairs.add((min(inlet, outlet), max(inlet, outlet)))
    return accepted, pairs


def colour_states(pairs):
    neighbours = [set() for _ in range(1 << len(INPUT_EDGES))]
    for a, b in pairs:
        if a == b:
            raise ValueError("a permitted window has identical input and output states")
        neighbours[a].add(b)
        neighbours[b].add(a)
    colours = [None] * len(neighbours)
    for root in range(len(colours)):
        if colours[root] is not None:
            continue
        colours[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            other = 1 - colours[u]
            for v in neighbours[u]:
                if colours[v] is None:
                    colours[v] = other
                    queue.append(v)
                elif colours[v] != other:
                    raise ValueError("window constraints do not admit a two-colouring")
    return "".join(map(str, colours))


def main():
    accepted = {}
    counts = {}
    union = set()
    for name, edges in (("F9", F9), ("F11", F11)):
        accepted[name], pairs = constraints(edges)
        counts[name] = len(pairs)
        union.update(pairs)
    colours = colour_states(union)
    print(json.dumps({
        "valid_orientations": accepted,
        "distinct_constraints": counts,
        "union_constraints": len(union),
        "bipartite": True,
        "colour_bits_0_to_31": colours,
        "colour_sha256": hashlib.sha256(colours.encode()).hexdigest(),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
