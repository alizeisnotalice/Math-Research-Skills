#!/usr/bin/env python3
"""Recover a degree sequence from the single-edge deck of one small graph.

The implementation is deliberately finite and exact.  It builds the deck from
the supplied graph only to make a testable certificate.  Once the deck has
been built, ``recover_from_card_degrees`` uses only the degree multisets of
the cards, their common order, and their number.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from math import comb
from pathlib import Path


def read_graph(data: dict) -> tuple[int, frozenset[tuple[int, int]]]:
    if not isinstance(data, dict) or type(data.get("n")) is not int:
        raise ValueError("input must be an object with integer n")
    n = data["n"]
    if not 0 <= n <= 8 or not isinstance(data.get("edges"), list):
        raise ValueError("n must be in 0,...,8 and edges must be a list")
    edges: set[tuple[int, int]] = set()
    for item in data["edges"]:
        if (not isinstance(item, list) or len(item) != 2 or
                type(item[0]) is not int or type(item[1]) is not int):
            raise ValueError("each edge must be a two-integer list")
        left, right = sorted(item)
        if not 0 <= left < right < n:
            raise ValueError("edges must join distinct vertices in 0,...,n-1")
        edges.add((left, right))
    if len(edges) != len(data["edges"]):
        raise ValueError("duplicate edges are not allowed")
    return n, frozenset(edges)


def degree_multiset(n: int, edges: frozenset[tuple[int, int]]) -> tuple[int, ...]:
    degrees = [0] * n
    for left, right in edges:
        degrees[left] += 1
        degrees[right] += 1
    return tuple(sorted(degrees))


def card_degree_multisets(n: int, edges: frozenset[tuple[int, int]]) -> list[tuple[int, ...]]:
    return [degree_multiset(n, frozenset(edges - {edge})) for edge in edges]


def recover_from_card_degrees(n: int, cards: list[tuple[int, ...]]) -> Counter[int]:
    """Return degree multiplicities using Edge--Kelly star counts.

    For r<m, every r-edge star survives exactly m-r deletions.  Thus its
    count is recovered by averaging its count over cards.  The exceptional
    maximum-degree-m case is recognised directly from its card degree data.
    """
    m = len(cards)
    if type(n) is not int or n < 1:
        raise ValueError("n must be a positive integer")
    if not 4 <= m <= comb(n, 2):
        raise ValueError("the number of cards must be between four and n choose two")
    if any(len(card) != n or any(type(d) is not int or not 0 <= d <= min(n-1, m-1) for d in card)
           or sum(card) != 2 * (m - 1) for card in cards):
        raise ValueError("cards do not have a common valid one-edge-deletion degree total")

    star_card = tuple(sorted([0] * (n - m) + [1] * (m - 1) + [m - 1]))
    if n >= m + 1 and all(tuple(sorted(card)) == star_card for card in cards):
        return Counter({degree: count for degree, count in {0: n - m - 1, 1: m, m: 1}.items() if count})

    upper = min(n - 1, m - 1)
    star_moments: dict[int, int] = {}
    for r in range(1, upper + 1):
        total = sum(sum(comb(degree, r) for degree in card) for card in cards)
        quotient, remainder = divmod(total, m - r)
        if remainder:
            raise ArithmeticError(f"Edge--Kelly tally for r={r} is not divisible by m-r")
        star_moments[r] = quotient

    multiplicity: Counter[int] = Counter()
    for degree in range(upper, 0, -1):
        multiplicity[degree] = star_moments[degree] - sum(
            comb(larger, degree) * multiplicity[larger]
            for larger in range(degree + 1, upper + 1)
        )
        if multiplicity[degree] < 0:
            raise ArithmeticError("recovered a negative degree multiplicity")
    multiplicity[0] = n - sum(multiplicity.values())
    if multiplicity[0] < 0 or sum(degree * count for degree, count in multiplicity.items()) != 2 * m:
        raise ArithmeticError("degree moments do not describe a graph with this deck")
    return Counter({degree: count for degree, count in multiplicity.items() if count})


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON object with n and either card_degree_multisets or edges")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("input must be a JSON object")
        actual = None
        if "card_degree_multisets" in data:
            cards = data["card_degree_multisets"]
            if "edges" in data or not isinstance(cards, list) or any(not isinstance(card, list) for card in cards):
                raise ValueError("supply a list of card degree multisets or an edge list")
            n = data.get("n")
        else:
            n, edges = read_graph(data)
            cards = card_degree_multisets(n, edges)
            actual = Counter(degree_multiset(n, edges))
        recovered = recover_from_card_degrees(n, cards)
    except (OSError, ValueError, ArithmeticError) as error:
        parser.error(str(error))
    result = {
        "n": n,
        "m": len(cards),
        "card_degree_multisets": [list(card) for card in cards],
        "recovered_degree_multiplicities": dict(sorted(recovered.items())),
        "scope": "Degree sequence conditional on input being a valid edge deck of one simple graph.",
    }
    if actual is not None:
        result["actual_degree_multiplicities"] = dict(sorted(actual.items()))
        result["matches_input"] = recovered == actual
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if actual is None or recovered == actual else 1


if __name__ == "__main__":
    raise SystemExit(main())
