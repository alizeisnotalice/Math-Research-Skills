#!/usr/bin/env python3
"""Construct a successor-colour recolouring or certify mutual reachability."""

from collections import deque
import argparse
import json
from pathlib import Path


def vertex(value, order):
    if type(value) is not int or not 0 <= value < order:
        raise ValueError(f"expected a vertex in [0, {order}), got {value!r}")
    return value


def edge(item, order):
    if not isinstance(item, list) or len(item) != 2:
        raise ValueError("an edge must be a pair of vertices")
    a, b = (vertex(v, order) for v in item)
    if a == b:
        raise ValueError("self-loops are outside the simple-graph model")
    return min(a, b), max(a, b)


def directed_search(outgoing, source):
    parent = {source: None}
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in outgoing[u]:
            if v not in parent:
                parent[v] = u
                queue.append(v)
    return parent


def restore_path(parent, destination):
    reversed_path = []
    while destination is not None:
        reversed_path.append(destination)
        destination = parent[destination]
    return reversed_path[::-1]


def check(data):
    colors = data["colors"]
    if not isinstance(colors, list):
        raise ValueError("colors must be a list indexed by vertex")
    order = len(colors)
    k = data["color_count"]
    if type(k) is not int or k < 3:
        raise ValueError("color_count must be an integer at least three")
    if any(type(c) is not int or not 0 <= c < k for c in colors):
        raise ValueError("each color must be an integer in [0, color_count)")
    cycle = data["color_cycle"]
    if not isinstance(cycle, list) or len(cycle) != k or sorted(vertex(c, k) for c in cycle) != list(range(k)):
        raise ValueError("color_cycle must list every color exactly once")
    successor = dict(zip(cycle, cycle[1:] + cycle[:1]))
    edges_list = [edge(item, order) for item in data["edges"]]
    edges = set(edges_list)
    if len(edges) != len(edges_list):
        raise ValueError("edges must not contain repetitions")
    x, y = deleted = edge(data["deleted_edge"], order)
    if deleted not in edges or colors[x] != colors[y]:
        raise ValueError("deleted_edge must be present and have endpoints of the same color")
    outgoing = [[] for _ in colors]
    for u, v in sorted(edges - {deleted}):
        if colors[u] == colors[v]:
            raise ValueError("colors must properly color the graph after deleting the edge")
        if successor[colors[u]] == colors[v]:
            outgoing[u].append(v)
        if successor[colors[v]] == colors[u]:
            outgoing[v].append(u)
    witness_paths = []
    for source, target in ((x, y), (y, x)):
        reached = directed_search(outgoing, source)
        if target in reached:
            witness_paths.append(restore_path(reached, target))
            continue
        changed = [successor[c] if u in reached else c for u, c in enumerate(colors)]
        if any(changed[u] == changed[v] for u, v in edges):
            raise AssertionError("reachable-set recolouring must color the full graph")
        return {"result": "recolored", "updated_vertices": sorted(reached), "new_colors": changed}
    return {"result": "mutual-reachability", "paths": witness_paths}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, KeyError, TypeError, ValueError) as err:
        parser.error(str(err))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
