#!/usr/bin/env python3
"""Check the finite assertions in Cogentic Lemma 3.1(1).

The input is one finite connected simple graph.  Vertex labels break degree
ties, thereby fixing a degree-compatible vertex order.  The program builds the
degree-ordered Kruskal tree from physical pp. 12--14 of the cited manuscript,
then checks each requested integral threshold exactly with integer graph data.

It is a finite certificate checker.  Its successful output does not establish
the manuscript's reconstruction theorem or its entropy estimates.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import defaultdict, deque
from pathlib import Path


def pairs(order: int) -> list[tuple[int, int]]:
    return [(left, right) for left in range(order) for right in range(left + 1, order)]


def read_graph(path: str) -> tuple[int, frozenset[tuple[int, int]]]:
    raw = json.loads(Path(path).read_text())
    if not isinstance(raw, dict) or type(raw.get("n")) is not int or raw["n"] < 4:
        raise ValueError("input requires integer n >= 4")
    if not isinstance(raw.get("edges"), list):
        raise ValueError("input requires an edges list")
    order = raw["n"]
    edges: set[tuple[int, int]] = set()
    for item in raw["edges"]:
        if not isinstance(item, list) or len(item) != 2 or not all(type(vertex) is int for vertex in item):
            raise ValueError("each edge must be a two-integer list")
        left, right = item
        if not 0 <= left < order or not 0 <= right < order or left == right:
            raise ValueError("edge endpoints must be distinct vertices in range")
        edges.add(tuple(sorted((left, right))))
    if len(edges) != len(raw["edges"]):
        raise ValueError("loops and duplicate edges are not allowed")
    if not connected_components(order, edges, set(range(order))) or len(connected_components(order, edges, set(range(order)))) != 1:
        raise ValueError("the Lemma 3.1(1) checker requires a connected graph")
    return order, frozenset(edges)


def neighbours(order: int, edges: frozenset[tuple[int, int]]) -> list[set[int]]:
    result = [set() for _ in range(order)]
    for left, right in edges:
        result[left].add(right)
        result[right].add(left)
    return result


def connected_components(order: int, edges: frozenset[tuple[int, int]], vertices: set[int]) -> list[frozenset[int]]:
    adjacency = neighbours(order, edges)
    remaining = set(vertices)
    answer: list[frozenset[int]] = []
    while remaining:
        first = min(remaining)
        queue = deque([first])
        component = {first}
        remaining.remove(first)
        while queue:
            vertex = queue.popleft()
            for successor in adjacency[vertex] & remaining & vertices:
                remaining.remove(successor)
                component.add(successor)
                queue.append(successor)
        answer.append(frozenset(component))
    return answer


class UnionFind:
    def __init__(self, order: int) -> None:
        self.parent = list(range(order))

    def find(self, vertex: int) -> int:
        while self.parent[vertex] != vertex:
            self.parent[vertex] = self.parent[self.parent[vertex]]
            vertex = self.parent[vertex]
        return vertex

    def union(self, left: int, right: int) -> bool:
        left, right = self.find(left), self.find(right)
        if left == right:
            return False
        self.parent[right] = left
        return True


def kruskal_tree(order: int, edges: frozenset[tuple[int, int]]) -> tuple[list[int], frozenset[tuple[int, int]], dict[tuple[int, int], int]]:
    adjacency = neighbours(order, edges)
    degree = [len(items) for items in adjacency]
    vertex_order = sorted(range(order), key=lambda vertex: (degree[vertex], vertex))
    rank = {vertex: index for index, vertex in enumerate(vertex_order)}

    def oriented(edge: tuple[int, int]) -> tuple[int, int]:
        left, right = edge
        return (right, left) if rank[left] < rank[right] else (left, right)

    def edge_key(edge: tuple[int, int]) -> tuple[int, int]:
        high, low = oriented(edge)
        return rank[high], rank[low]

    forest = UnionFind(order)
    selected: set[tuple[int, int]] = set()
    weights: dict[tuple[int, int], int] = {}
    for edge in sorted(edges, key=edge_key):
        high, _ = oriented(edge)
        weights[edge] = degree[high]
        if forest.union(*edge):
            selected.add(edge)
    if len(selected) != order - 1:
        raise AssertionError("Kruskal selection did not produce a spanning tree")
    return vertex_order, frozenset(selected), weights


def threshold_certificate(order: int, edges: frozenset[tuple[int, int]], vertex_order: list[int], tree: frozenset[tuple[int, int]], weights: dict[tuple[int, int], int], threshold: int) -> dict:
    adjacency = neighbours(order, edges)
    degree = [len(items) for items in adjacency]
    rank = {vertex: index for index, vertex in enumerate(vertex_order)}
    high = {vertex for vertex in range(order) if degree[vertex] >= threshold}
    low = set(range(order)) - high
    components = connected_components(order, edges, low)
    forest_edges = frozenset(edge for edge in tree if weights[edge] < threshold)
    forest_components = connected_components(order, forest_edges, low)
    forest_exact = set(forest_components) == set(components)
    if not forest_exact:
        raise AssertionError("low-weight tree edges do not span the induced low-degree graph")
    exits: dict[frozenset[int], list[tuple[int, int]]] = {}
    bridge_components: list[frozenset[int]] = []
    nonbridge_parents: dict[tuple[tuple[int, ...], tuple[tuple[int, tuple[int, ...]], ...]], int] = {}
    for component in components:
        exiting = [edge for edge in tree if (edge[0] in component) ^ (edge[1] in component)]
        exits[component] = exiting
        if len(exiting) >= 2:
            bridge_components.append(component)
        if len(exiting) == 1:
            endpoint = next(vertex for vertex in exiting[0] if vertex not in component)
            external_neighbours = sorted({neighbour for vertex in component for neighbour in adjacency[vertex] if neighbour in high})
            if not external_neighbours:
                raise AssertionError("a non-bridge component has no high-degree neighbour")
            expected_parent = min(external_neighbours, key=lambda vertex: rank[vertex])
            if endpoint != expected_parent:
                raise AssertionError("non-bridge component does not attach at its least ordered high neighbour")
            local = tuple(sorted(component))
            label = tuple((vertex, tuple(sorted(adjacency[vertex] & high))) for vertex in local)
            # The manuscript's labelled-component class ignores labels inside H only up to a
            # common relabelling.  This rigid input encoding is a sufficient finite subcase.
            key = (local, label)
            if key in nonbridge_parents and nonbridge_parents[key] != endpoint:
                raise AssertionError("equal rigid component labels had different parents")
            nonbridge_parents[key] = endpoint
    bridge_count = len(bridge_components)
    bridge_vertices = set().union(*bridge_components) if bridge_components else set()
    # Keep precisely the edges in Lemma 3.1(1b): high--high edges and tree
    # exits from the high set into a bridge component.  Exits into a one-exit
    # component have already been removed when forming the contracted core.
    relevant_edges = [
        edge for edge in tree
        if (edge[0] in high and edge[1] in high)
        or (edge[0] in high and edge[1] in bridge_vertices)
        or (edge[1] in high and edge[0] in bridge_vertices)
    ]
    if bridge_count > len(high) - 1:
        raise AssertionError("bridge-component count exceeds the Lemma 3.1 bound")
    if len(relevant_edges) > 2 * len(high) - 2:
        raise AssertionError("incident-edge count exceeds the Lemma 3.1 bound")
    return {
        "threshold": threshold,
        "high_vertices": sorted(high),
        "low_component_count": len(components),
        "bridge_component_count": bridge_count,
        "bridge_bound": len(high) - 1,
        "relevant_tree_edge_count": len(relevant_edges),
        "relevant_edge_bound": 2 * len(high) - 2,
        "low_forest_spans_components": forest_exact,
        "nonbridge_components_checked": sum(len(exits[component]) == 1 for component in components),
    }


def certify(order: int, edges: frozenset[tuple[int, int]], thresholds: list[int]) -> dict:
    vertex_order, tree, weights = kruskal_tree(order, edges)
    maximum_degree = max(len(items) for items in neighbours(order, edges))
    if not thresholds:
        thresholds = list(range(1, maximum_degree + 1))
    if any(type(value) is not int or value < 1 or value > maximum_degree for value in thresholds):
        raise ValueError("thresholds must be integers in 1,...,maximum_degree")
    return {
        "status": "KRUSKAL_NONBRIDGE_CERTIFIED",
        "n": order,
        "m": len(edges),
        "vertex_order_low_to_high": vertex_order,
        "tree_edges": [list(edge) for edge in sorted(tree)],
        "thresholds": [threshold_certificate(order, edges, vertex_order, tree, weights, value) for value in sorted(set(thresholds))],
        "scope": "Exact finite check of Lemma 3.1(1a--c) for the supplied graph and deterministic degree-compatible tie order. It does not establish the multiscale automorphism factorization, the entropy obstruction, or the general edge-reconstruction theorem.",
    }


def self_test() -> dict:
    checked = 0
    # All labelled connected simple graphs on four vertices, plus a non-regular five-vertex witness.
    for mask in range(1 << len(pairs(4))):
        edges = frozenset(edge for bit, edge in enumerate(pairs(4)) if mask & (1 << bit))
        if len(connected_components(4, edges, set(range(4)))) == 1:
            certify(4, edges, [])
            checked += 1
    certify(5, frozenset({(0, 1), (1, 2), (2, 3), (3, 4), (0, 2), (1, 3)}), [])
    return {"status": "SELF_TEST_PASSED", "connected_labelled_n4_graphs": checked, "additional_n5_graph": True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="JSON graph with n and edges")
    parser.add_argument("--threshold", type=int, action="append", default=[])
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    try:
        if args.self_test:
            if args.input:
                raise ValueError("--self-test accepts no graph input")
            result = self_test()
        elif args.input:
            result = certify(*read_graph(args.input), args.threshold)
        else:
            raise ValueError("supply a graph JSON file or --self-test")
        print(json.dumps(result, indent=2, sort_keys=True))
    except (OSError, ValueError, AssertionError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
