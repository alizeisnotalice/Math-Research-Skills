#!/usr/bin/env python3
"""Validate a finite simple graph/tree input and return an exact embedding."""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction


def _matrix(value: object, label: str) -> list[list[int]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must be a nonempty square matrix")
    n = len(value)
    result: list[list[int]] = []
    for row in value:
        if not isinstance(row, list) or len(row) != n:
            raise ValueError(f"{label} must be square")
        if any(entry not in (0, 1) or isinstance(entry, bool) for entry in row):
            raise ValueError(f"{label} entries must be integer 0 or 1")
        result.append(row)
    if any(result[i][i] for i in range(n)):
        raise ValueError(f"{label} must have zero diagonal")
    if any(result[i][j] != result[j][i] for i in range(n) for j in range(n)):
        raise ValueError(f"{label} must be symmetric")
    return result


def _is_tree(adjacency: list[list[int]]) -> bool:
    n = len(adjacency)
    edges = sum(sum(row) for row in adjacency) // 2
    if edges != n - 1:
        return False
    reached, stack = {0}, [0]
    while stack:
        current = stack.pop()
        for neighbor, linked in enumerate(adjacency[current]):
            if linked and neighbor not in reached:
                reached.add(neighbor)
                stack.append(neighbor)
    return len(reached) == n


def find_embedding(host: list[list[int]], tree: list[list[int]]) -> list[int] | None:
    """Return tree-index to host-index injection, or None, by backtracking."""
    host_n, tree_n = len(host), len(tree)
    order = sorted(range(tree_n), key=lambda v: (-sum(tree[v]), v))
    assigned: dict[int, int] = {}
    used: set[int] = set()

    def search(position: int) -> bool:
        if position == tree_n:
            return True
        vertex = order[position]
        required = [(other, host_vertex) for other, host_vertex in assigned.items() if tree[vertex][other]]
        for candidate in range(host_n):
            if candidate in used or any(not host[candidate][mapped] for _, mapped in required):
                continue
            assigned[vertex] = candidate
            used.add(candidate)
            if search(position + 1):
                return True
            used.remove(candidate)
            del assigned[vertex]
        return False

    return [assigned[index] for index in range(tree_n)] if search(0) else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON containing host_adjacency and tree_adjacency; use - for stdin")
    args = parser.parse_args()
    data = json.load(sys.stdin if args.input == "-" else open(args.input, encoding="utf-8"))
    if set(data) != {"host_adjacency", "tree_adjacency"}:
        raise ValueError("input keys must be exactly host_adjacency and tree_adjacency")
    host = _matrix(data["host_adjacency"], "host_adjacency")
    tree = _matrix(data["tree_adjacency"], "tree_adjacency")
    t = len(tree)
    if t < 2 or not _is_tree(tree):
        raise ValueError("tree_adjacency must describe a tree with at least 2 vertices")
    edges = sum(sum(row) for row in host) // 2
    average_degree = Fraction(2 * edges, len(host))
    threshold = t - 2
    if average_degree <= threshold:
        raise ValueError("strict average-degree hypothesis 2|E|/|V| > t-2 fails")
    embedding = find_embedding(host, tree)
    if embedding is None:
        raise AssertionError("no embedding found despite validated theorem hypotheses")
    print(json.dumps({
        "host_vertices": len(host),
        "host_edges": edges,
        "tree_vertices": t,
        "average_degree": str(average_degree),
        "strict_threshold": threshold,
        "tree_to_host": embedding,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
