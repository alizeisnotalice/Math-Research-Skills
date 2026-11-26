#!/usr/bin/env python3
"""Recover a finite vertex-deck from an unlabelled edge-deck certificate.

The finite transform implements the triangular counting step in Lemma 2.3 of
the cited Cogentic edge-reconstruction manuscript.  It is deliberately capped
at six vertices because it enumerates all unlabelled graph classes directly.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path


def pairs(order: int) -> tuple[tuple[int, int], ...]:
    return tuple((left, right) for right in range(order) for left in range(right))


def canonical_code(order: int, edges: frozenset[tuple[int, int]]) -> str:
    all_pairs = pairs(order)
    best: str | None = None
    for permutation in itertools.permutations(range(order)):
        relabelled = {tuple(sorted((permutation[left], permutation[right]))) for left, right in edges}
        candidate = "".join("1" if edge in relabelled else "0" for edge in all_pairs)
        if best is None or candidate < best:
            best = candidate
    assert best is not None
    return best


def edges_from_code(order: int, code: str) -> frozenset[tuple[int, int]]:
    all_pairs = pairs(order)
    if len(code) != len(all_pairs) or any(bit not in "01" for bit in code):
        raise ValueError("every card code must be a binary adjacency word of the prescribed length")
    return frozenset(edge for edge, bit in zip(all_pairs, code) if bit == "1")


def normalize_edges(order: int, raw_edges: object) -> frozenset[tuple[int, int]]:
    if not isinstance(raw_edges, list):
        raise ValueError("edges must be a list")
    result: set[tuple[int, int]] = set()
    for raw_edge in raw_edges:
        if not isinstance(raw_edge, list) or len(raw_edge) != 2:
            raise ValueError("every edge must be a two-element list")
        left, right = raw_edge
        if type(left) is not int or type(right) is not int or not 0 <= left < order or not 0 <= right < order or left == right:
            raise ValueError("edge endpoints must be distinct in 0,...,n-1")
        result.add(tuple(sorted((left, right))))
    if len(result) != len(raw_edges):
        raise ValueError("duplicate edges and loops are not allowed")
    return frozenset(result)


def read_graph(path: str) -> tuple[int, frozenset[tuple[int, int]]]:
    source = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(source, dict) or type(source.get("n")) is not int:
        raise ValueError("graph input must have integer n")
    order = source["n"]
    if not 4 <= order <= 6:
        raise ValueError("this finite certificate supports 4 <= n <= 6")
    return order, normalize_edges(order, source.get("edges"))


def card_deck(order: int, edges: frozenset[tuple[int, int]]) -> Counter[str]:
    return Counter(canonical_code(order, frozenset(edges - {edge})) for edge in edges)


def read_deck(path: str) -> tuple[int, Counter[str]]:
    source = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(source, dict) or type(source.get("n")) is not int:
        raise ValueError("deck input must have integer n")
    order = source["n"]
    if not 4 <= order <= 6 or not isinstance(source.get("edge_deck"), list):
        raise ValueError("deck input needs 4 <= n <= 6 and an edge_deck list")
    result: Counter[str] = Counter()
    for entry in source["edge_deck"]:
        if not isinstance(entry, list) or len(entry) != 2 or not isinstance(entry[0], str) or type(entry[1]) is not int or entry[1] <= 0:
            raise ValueError("edge_deck entries must be [canonical_code, positive_multiplicity]")
        code, multiplicity = entry
        edges = edges_from_code(order, code)
        if canonical_code(order, edges) != code:
            raise ValueError("every card code must already be canonical")
        result[code] += multiplicity
    return order, result


@lru_cache(maxsize=None)
def graph_classes(order: int) -> tuple[str, ...]:
    representatives: set[str] = set()
    for mask in range(1 << len(pairs(order))):
        edges = frozenset(edge for index, edge in enumerate(pairs(order)) if mask & (1 << index))
        representatives.add(canonical_code(order, edges))
    return tuple(sorted(representatives, key=lambda code: (-code.count("1"), code)))


@lru_cache(maxsize=None)
def spanning_profile(order: int, code: str) -> Counter[str]:
    edges = tuple(edges_from_code(order, code))
    result: Counter[str] = Counter()
    for mask in range(1 << len(edges)):
        subset = frozenset(edge for index, edge in enumerate(edges) if mask & (1 << index))
        result[canonical_code(order, subset)] += 1
    return result


def add_isolated_vertex(order: int, code: str) -> str:
    edges = edges_from_code(order - 1, code)
    return canonical_code(order, edges)


def deck_subgraph_count(order: int, deck: Counter[str], pattern_code: str) -> int:
    edge_count = sum(deck.values())
    pattern_edges = pattern_code.count("1")
    denominator = edge_count - pattern_edges
    if denominator <= 0:
        raise ValueError("Edge--Kelly recovery requires fewer pattern edges than deck size")
    numerator = sum(multiplicity * spanning_profile(order, code)[pattern_code] for code, multiplicity in deck.items())
    value, remainder = divmod(numerator, denominator)
    if remainder:
        raise ArithmeticError("Edge--Kelly numerator is not divisible by the survival count")
    return value


def recover_vertex_deck(order: int, deck: Counter[str]) -> Counter[str]:
    edge_count = sum(deck.values())
    if edge_count < 4:
        raise ValueError("the cited triangular transform requires at least four edges")
    if any(code.count("1") != edge_count - 1 for code in deck):
        raise ValueError("every edge card must have exactly m-1 edges")
    result: Counter[str] = Counter()
    # With no isolated vertices, a vertex deletion has fewer than m edges.
    # Classes at or above m therefore have certified multiplicity zero.
    for code in (item for item in graph_classes(order - 1) if item.count("1") < edge_count):
        pattern_code = add_isolated_vertex(order, code)
        source_count = deck_subgraph_count(order, deck, pattern_code)
        isolated_vertices = sum(all(vertex not in edge for edge in edges_from_code(order - 1, code)) for vertex in range(order - 1))
        rhs = (isolated_vertices + 1) * source_count
        for larger_code, multiplicity in result.items():
            rhs -= multiplicity * spanning_profile(order - 1, larger_code)[code]
        if rhs < 0:
            raise ArithmeticError("triangular inversion produced a negative vertex-card multiplicity")
        result[code] = rhs
    if sum(result.values()) != order:
        raise ArithmeticError("recovered vertex-card multiplicities do not sum to n")
    return Counter({code: count for code, count in result.items() if count})


def direct_vertex_deck(order: int, edges: frozenset[tuple[int, int]]) -> Counter[str]:
    result: Counter[str] = Counter()
    for removed in range(order):
        retained = [vertex for vertex in range(order) if vertex != removed]
        relabel = {vertex: index for index, vertex in enumerate(retained)}
        card = frozenset(tuple(sorted((relabel[left], relabel[right]))) for left, right in edges if removed not in (left, right))
        result[canonical_code(order - 1, card)] += 1
    return result


def require_no_isolates(order: int, edges: frozenset[tuple[int, int]]) -> None:
    if any(all(vertex not in edge for edge in edges) for vertex in range(order)):
        raise ValueError("remove isolated vertices before applying this vertex-deck transform")


def serialise(deck: Counter[str]) -> list[list[object]]:
    return [[code, deck[code]] for code in sorted(deck, key=lambda item: (-item.count("1"), item))]


def self_test() -> dict[str, object]:
    checked: Counter[int] = Counter()
    for order in (4, 5):
        for code in graph_classes(order):
            edges = edges_from_code(order, code)
            if len(edges) < 4 or any(all(vertex not in edge for edge in edges) for vertex in range(order)):
                continue
            recovered = recover_vertex_deck(order, card_deck(order, edges))
            if recovered != direct_vertex_deck(order, edges):
                raise AssertionError(f"recovery mismatch for n={order}, code={code}")
            checked[order] += 1
    return {"checked_unlabelled_isolate_free_graphs": sum(checked.values()), "by_n": dict(checked)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("--graph", help="JSON graph with n and edges; directly cross-checks the result")
    group.add_argument("--deck", help="JSON object with n and canonical edge_deck pairs")
    parser.add_argument("--self-test", action="store_true", help="check all unlabelled isolate-free graphs for n=4 and n=5")
    arguments = parser.parse_args()
    try:
        if arguments.self_test:
            if arguments.graph or arguments.deck:
                raise ValueError("--self-test cannot be combined with graph or deck input")
            result = self_test()
        elif arguments.graph:
            order, edges = read_graph(arguments.graph)
            require_no_isolates(order, edges)
            deck = card_deck(order, edges)
            recovered = recover_vertex_deck(order, deck)
            direct = direct_vertex_deck(order, edges)
            result = {
                "n": order,
                "m": len(edges),
                "edge_deck": serialise(deck),
                "recovered_vertex_deck": serialise(recovered),
                "direct_vertex_deck": serialise(direct),
                "matches_direct_vertex_deck": recovered == direct,
                "scope": "Exact finite Edge--Kelly/triangular recovery for this isolate-free graph. It is not a general edge-reconstruction proof.",
            }
        elif arguments.deck:
            order, deck = read_deck(arguments.deck)
            recovered = recover_vertex_deck(order, deck)
            result = {
                "n": order,
                "m": sum(deck.values()),
                "recovered_vertex_deck": serialise(recovered),
                "scope": "Exact finite Edge--Kelly/triangular recovery from this supplied edge deck, conditional on a no-isolate origin. Realisability is not asserted.",
            }
        else:
            raise ValueError("choose --graph, --deck, or --self-test")
    except (OSError, ValueError, ArithmeticError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
