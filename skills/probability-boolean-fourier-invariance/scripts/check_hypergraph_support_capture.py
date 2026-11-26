#!/usr/bin/env python3
"""Exact finite verifier for the support-capture condition in Lemma 3.2.

The input is JSON with positive integer ``n, r, m, k`` and a nonempty list
``edges`` of distinct r-subsets of {1,...,n}.  It checks the *sufficient*
preconditions printed in the cited lemma and enumerates all m-subsets B.
It is deliberately not an influence-bound verifier.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


def fail(message: str) -> None:
    print(json.dumps({"ok": False, "error": message}, sort_keys=True))
    raise SystemExit(2)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--max-blocks", type=int, default=200000,
                        help="refuse enumeration above this many m-subsets")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        n, r, m, k = (int(data[x]) for x in ("n", "r", "m", "k"))
        raw_edges = data["edges"]
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        fail(f"invalid input schema: {exc}")
    if not (n >= r >= 3 and 1 <= m <= n and k > 0):
        fail("requires n >= r >= 3, 1 <= m <= n, and integer k > 0")
    try:
        edges = [frozenset(map(int, edge)) for edge in raw_edges]
    except TypeError as exc:
        fail(f"edges must be lists of integers: {exc}")
    if not edges or len(set(edges)) != len(edges):
        fail("edges must be a nonempty list of distinct edges")
    if any(len(edge) != r or not all(1 <= v <= n for v in edge) for edge in edges):
        fail("every edge must be an r-subset of {1,...,n}")
    # L=(k/r)^(r/(r-1)).  These raised-power comparisons avoid floating point.
    s = len(edges)
    if r**r * s**(r - 1) > k**r:
        fail("support size exceeds L=(k/r)^(r/(r-1))")
    if n == 1:  # unreachable because r >= 3, retained for totality.
        fail("n-1 must be positive")
    lhs_power = Fraction(2 * r * (m - 1), n - 1) ** (r - 1) * Fraction(k, r) ** r
    if lhs_power > 1:
        fail("source size condition r*L*(m-1)/(n-1) <= 1/2 fails")
    total = math.comb(n, m)
    if total > args.max_blocks:
        fail(f"enumeration has {total} blocks, above --max-blocks")
    vertices = range(1, n + 1)
    captured = 0
    histogram: dict[int, int] = {}
    for block_tuple in itertools.combinations(vertices, m):
        block = frozenset(block_tuple)
        count = sum(bool(edge & block) for edge in edges)
        histogram[count] = histogram.get(count, 0) + 1
        if 1 <= count <= k:
            captured += 1
    probability = Fraction(captured, total)
    lower_bound = Fraction(m, 2 * n)
    print(json.dumps({
        "ok": probability >= lower_bound,
        "capture_probability": f"{probability.numerator}/{probability.denominator}",
        "capture_count": captured,
        "total_blocks": total,
        "lemma_lower_bound": f"{lower_bound.numerator}/{lower_bound.denominator}",
        "histogram": {str(key): histogram[key] for key in sorted(histogram)},
        "source_size_condition_power": f"{lhs_power.numerator}/{lhs_power.denominator}",
    }, sort_keys=True))
    if probability < lower_bound:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
