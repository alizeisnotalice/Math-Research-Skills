#!/usr/bin/env python3
"""Exact small-graph audit of unlabelled single-edge-deletion decks.

The exhaustive canonicalisation is intentionally limited to at most eight vertices.
It validates a supplied finite graph instance and never decides edge
reconstructibility in general.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


def pairs(order: int):
    return [(left, right) for right in range(order) for left in range(right)]


def read_graph(path: str) -> tuple[int, frozenset[tuple[int, int]]]:
    source = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(source, dict):
        raise ValueError("input must be a JSON object")
    order = source.get("n")
    raw_edges = source.get("edges")
    if type(order) is not int or not 0 <= order <= 8:
        raise ValueError("n must be an integer between 0 and 8")
    if not isinstance(raw_edges, list):
        raise ValueError("edges must be a list")
    edges = set()
    for raw_edge in raw_edges:
        if not isinstance(raw_edge, list) or len(raw_edge) != 2:
            raise ValueError("every edge must be a two-element list")
        first, second = raw_edge
        if type(first) is not int or type(second) is not int:
            raise ValueError("edge endpoints must be integers")
        if not 0 <= first < order or not 0 <= second < order or first == second:
            raise ValueError("edge endpoints must be distinct vertices in 0,...,n-1")
        edges.add(tuple(sorted((first, second))))
    if len(edges) != len(raw_edges):
        raise ValueError("loops or duplicate undirected edges are not allowed")
    return order, frozenset(edges)


def canonical_code(order: int, edges: frozenset[tuple[int, int]]) -> str:
    """The lexicographically least labelled adjacency word over all relabellings."""
    all_pairs = pairs(order)
    best = None
    for permutation in itertools.permutations(range(order)):
        relabelled = {tuple(sorted((permutation[first], permutation[second]))) for first, second in edges}
        code = "".join("1" if edge in relabelled else "0" for edge in all_pairs)
        if best is None or code < best:
            best = code
    return best


def deck(order: int, edges: frozenset[tuple[int, int]]) -> Counter[str]:
    return Counter(canonical_code(order, frozenset(edges - {edge})) for edge in edges)


def edge_kelly_count(order, card_counts, pattern_order, pattern_edges):
    """Recover the injective subgraph count from a canonical edge-deck."""
    edge_count = sum(card_counts.values())
    surviving_cards = edge_count - len(pattern_edges)
    if surviving_cards <= 0:
        raise ValueError("Edge–Kelly requires fewer pattern edges than host edges")
    total = 0
    all_pairs = pairs(order)
    for code, multiplicity in card_counts.items():
        edges = {edge for edge, bit in zip(all_pairs, code) if bit == "1"}
        embeddings = sum(
            all(tuple(sorted((vertices[u], vertices[v]))) in edges for u, v in pattern_edges)
            for vertices in itertools.permutations(range(order), pattern_order)
        )
        total += multiplicity * embeddings
    count, remainder = divmod(total, surviving_cards)
    if remainder:
        raise ArithmeticError("edge-deck tally is not divisible by the survival count")
    return count


def report(order: int, edges: frozenset[tuple[int, int]]) -> dict:
    degrees = [sum(vertex in edge for edge in edges) for vertex in range(order)]
    unlabelled_deck = deck(order, edges)
    return {
        "n": order,
        "m": len(edges),
        "degree_multiset": sorted(degrees),
        "canonical_code": canonical_code(order, edges),
        "edge_deck": sorted(unlabelled_deck.items()),
        "card_count": sum(unlabelled_deck.values()),
        "scope": "Exact canonical check for this graph only. It does not prove a reconstruction theorem.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", help="JSON object with n and an undirected edges list")
    parser.add_argument("--compare", help="optional second graph JSON")
    parser.add_argument("--pattern", help="optional JSON pattern for Edge–Kelly counting")
    arguments = parser.parse_args()
    try:
        first = read_graph(arguments.graph)
        second = read_graph(arguments.compare) if arguments.compare else None
        if second is not None and first[0] != second[0]:
            raise ValueError("deck comparison requires equal vertex counts")
        pattern = read_graph(arguments.pattern) if arguments.pattern else None
        result = {"first": report(*first)}
        if second is not None:
            result["second"] = report(*second)
            result["isomorphic"] = result["first"]["canonical_code"] == result["second"]["canonical_code"]
            result["same_unlabelled_edge_deck"] = result["first"]["edge_deck"] == result["second"]["edge_deck"]
        if pattern is not None:
            cards = dict(result["first"]["edge_deck"])
            result["edge_kelly_injective_count"] = edge_kelly_count(first[0], cards, *pattern)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
