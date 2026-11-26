#!/usr/bin/env python3
"""Exactly audit Lemma 2.1's finite weighted-tree response bound.

Input JSON has `vertices` and `edges`; each edge is [u, v, numerator,
denominator], with a strictly positive rational conductance.  The program
enumerates spanning trees and returns exact rational inclusion/covariance rows.
It intentionally does not infer an infinite-volume or FIID conclusion.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path
import sys


def is_tree(vertices, edges):
    parent = {v: v for v in vertices}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v, _ in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return len(edges) == len(vertices) - 1 and len({find(v) for v in vertices}) == 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    raw = json.loads(args.input.read_text())
    vertices = raw.get("vertices")
    raw_edges = raw.get("edges")
    if not isinstance(vertices, list) or len(vertices) < 2 or len(set(vertices)) != len(vertices):
        raise ValueError("vertices must be a duplicate-free list with at least two entries")
    if not isinstance(raw_edges, list):
        raise ValueError("edges must be a list")
    vset = set(vertices)
    edges = []
    seen = set()
    for k, e in enumerate(raw_edges):
        if not isinstance(e, list) or len(e) != 4:
            raise ValueError(f"edge {k} must be [u,v,numerator,denominator]")
        u, v, num, den = e
        if u not in vset or v not in vset or u == v:
            raise ValueError(f"edge {k} has invalid endpoints")
        key = frozenset((u, v))
        if key in seen:
            raise ValueError("parallel/repeated undirected edges are not supported by this checker")
        seen.add(key)
        if not isinstance(num, int) or not isinstance(den, int) or num <= 0 or den <= 0:
            raise ValueError(f"edge {k} needs positive integer numerator and denominator")
        edges.append((u, v, Fraction(num, den)))
    trees = []
    for subset in itertools.combinations(edges, len(vertices) - 1):
        if is_tree(vertices, subset):
            weight = Fraction(1)
            for _, _, c in subset:
                weight *= c
            trees.append((frozenset(edges.index(e) for e in subset), weight))
    if not trees:
        raise ValueError("graph is disconnected: it has no spanning tree")
    z = sum((weight for _, weight in trees), Fraction())
    p = [sum((weight for tree, weight in trees if e in tree), Fraction()) / z for e in range(len(edges))]
    cov = [[sum((weight for tree, weight in trees if i in tree and j in tree), Fraction()) / z - p[i] * p[j]
            for j in range(len(edges))] for i in range(len(edges))]
    rows = []
    for i in range(len(edges)):
        l1 = sum((abs(x) for x in cov[i]), Fraction())
        expected = 2 * p[i] * (1 - p[i])
        if l1 != expected or l1 > Fraction(1, 2):
            raise AssertionError("finite-tree response identity failed")
        rows.append({"edge": i, "p": str(p[i]), "abs_covariance_row_sum": str(l1), "identity_rhs": str(expected)})
    print(json.dumps({"spanning_tree_count": len(trees), "partition_function": str(z), "rows": rows,
                      "max_abs_covariance_row_sum": str(max(Fraction(x["abs_covariance_row_sum"]) for x in rows))},
                     sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"rejected input: {exc}", file=sys.stderr)
        raise SystemExit(2)
