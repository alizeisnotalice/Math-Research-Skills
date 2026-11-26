#!/usr/bin/env python3
"""Compare a clique-and-petal domination formula with direct enumeration."""

import argparse
import json
from math import comb


def edges_of(graph):
    n = graph["n"]
    if type(n) is not int or n < 0:
        raise ValueError("petal order must be a nonnegative integer")
    edges = set()
    for u, v in graph["edges"]:
        if any(type(vertex) is not int or not 0 <= vertex < n for vertex in (u, v)) or u == v:
            raise ValueError("edge endpoint out of range or loop")
        edge = tuple(sorted((u, v)))
        if edge in edges:
            raise ValueError("duplicate edge")
        edges.add(edge)
    return n, edges


def domination_poly(n, edges):
    closed = [1 << v for v in range(n)]
    for u, v in edges:
        closed[u] |= 1 << v
        closed[v] |= 1 << u
    full = (1 << n) - 1
    result = [0] * (n + 1)
    for mask in range(1 << n):
        covered = 0
        for v in range(n):
            if mask >> v & 1:
                covered |= closed[v]
        if covered == full:
            result[bin(mask).count("1")] += 1
    return result


def multiply(left, right):
    product = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            product[i + j] += a * b
    return product


def check(graph, clique, copies):
    if type(clique) is not int or clique < 1 or type(copies) is not int or copies < 0:
        raise ValueError("clique must be a positive integer and copies a nonnegative integer")
    b, petal_edges = edges_of(graph)
    outer_vertices = copies * b
    n = clique + outer_vertices
    edges = {(u, v) for u in range(clique) for v in range(u + 1, clique)}
    edges.update((u, v) for u in range(clique) for v in range(clique, n))
    for copy in range(copies):
        offset = clique + copy * b
        edges.update((offset + u, offset + v) for u, v in petal_edges)
    direct = domination_poly(n, edges)

    # Sets containing a center vertex dominate the join.
    formula = [comb(n, size) for size in range(n + 1)]
    for size in range(outer_vertices + 1):
        formula[size] -= comb(outer_vertices, size)
    # A set avoiding the center must dominate each petal and contain a vertex
    # to dominate the center. With no petal vertices such a set is impossible.
    if outer_vertices:
        power = [1]
        petal = domination_poly(b, petal_edges)
        for _ in range(copies):
            power = multiply(power, petal)
        for size, coefficient in enumerate(power):
            formula[size] += coefficient

    return {"vertices": n, "direct": direct, "formula": formula, "exact_match": direct == formula}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--petal-json", required=True)
    parser.add_argument("--clique", type=int, required=True)
    parser.add_argument("--copies", type=int, required=True)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.petal_json), args.clique, args.copies)
    except (KeyError, TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result))
    if not result["exact_match"]:
        raise SystemExit("identity mismatch")


if __name__ == "__main__":
    main()
