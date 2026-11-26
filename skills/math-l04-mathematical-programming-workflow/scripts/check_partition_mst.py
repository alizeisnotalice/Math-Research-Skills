#!/usr/bin/env python3
"""Exact finite partition-capacity checker with a Kruskal violation witness."""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def fail(message: str) -> None:
    raise ValueError(message)


def rational(value: Any, label: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        fail(f"{label} must be an integer or rational string, not a float/bool/object")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"{label} is not a rational number: {value!r}") from exc


def text(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def canonical_partition(blocks: list[set[int]]) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted((tuple(sorted(b)) for b in blocks), key=lambda b: b[0]))


def partitions(items: list[int]):
    if not items:
        yield []
        return
    head, *tail = items
    for rest in partitions(tail):
        yield [{head}] + [b.copy() for b in rest]
        for j in range(len(rest)):
            expanded = [b.copy() for b in rest]
            expanded[j].add(head)
            yield expanded


def block_map(blocks: list[set[int]], n: int) -> list[int]:
    out = [-1] * n
    for j, block in enumerate(blocks):
        for v in block:
            out[v] = j
    return out


def mst_weight(n: int, edges: list[tuple[int, int, Fraction]]) -> Fraction | None:
    if n == 1:
        return Fraction(0)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total, used = Fraction(0), 0
    for u, v, weight in sorted(edges, key=lambda e: (e[2], e[0], e[1])):
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            total += weight
            used += 1
            if used == n - 1:
                return total
    return None


def parse(data: Any):
    if not isinstance(data, dict):
        fail("top-level JSON value must be an object")
    vertices, raw_edges = data.get("vertices"), data.get("edges")
    if not isinstance(vertices, list) or not vertices or not all(isinstance(x, str) and x for x in vertices):
        fail("vertices must be a nonempty list of distinct nonempty strings")
    if len(set(vertices)) != len(vertices):
        fail("vertices must be distinct")
    if not isinstance(raw_edges, list):
        fail("edges must be a list")
    index = {v: i for i, v in enumerate(vertices)}
    edges: list[tuple[int, int, Fraction]] = []
    seen: set[tuple[int, int]] = set()
    for j, raw in enumerate(raw_edges):
        if not isinstance(raw, dict) or set(raw) != {"u", "v", "capacity"}:
            fail(f"edges[{j}] must have exactly u, v, capacity")
        u, v = raw["u"], raw["v"]
        if not isinstance(u, str) or not isinstance(v, str) or u not in index or v not in index or u == v:
            fail(f"edges[{j}] has an unknown endpoint or loop")
        a, b = sorted((index[u], index[v]))
        if (a, b) in seen:
            fail(f"edges[{j}] duplicates an undirected edge")
        seen.add((a, b))
        capacity = rational(raw["capacity"], f"edges[{j}].capacity")
        if capacity < 0:
            fail(f"edges[{j}].capacity must be nonnegative")
        edges.append((a, b, capacity))
    q = rational(data.get("q"), "q")
    if q < 0:
        fail("q must be nonnegative")
    if mst_weight(len(vertices), [(u, v, Fraction(1)) for u, v, _ in edges]) is None:
        fail("graph must be connected")
    return vertices, edges, q


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: check_partition_mst.py INPUT.json", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        vertices, edges, q = parse(data)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"input rejected: {exc}", file=sys.stderr)
        return 2

    best: tuple[Fraction, tuple[tuple[int, ...], ...], Fraction] | None = None
    count = 0
    for blocks in partitions(list(range(len(vertices)))):
        if len(blocks) == 1:
            continue
        count += 1
        locate = block_map(blocks, len(vertices))
        crossing = sum((cap for u, v, cap in edges if locate[u] != locate[v]), Fraction(0))
        ratio = crossing / (len(blocks) - 1)
        candidate = (ratio, canonical_partition(blocks), crossing)
        if best is None or candidate[:2] < best[:2]:
            best = candidate
    if best is None:
        print(json.dumps({
            "status": "feasible",
            "vertices": vertices,
            "q": text(q),
            "partition_count": 0,
            "minimum_partition_ratio": None,
            "minimizing_partition": None,
        }, indent=2, sort_keys=True))
        return 0
    ratio, part, crossing = best
    blocks = [set(b) for b in part]
    locate = block_map(blocks, len(vertices))
    ell = [1 if locate[u] != locate[v] else 0 for u, v, _ in edges]
    dot = sum((cap * w for (_, _, cap), w in zip(edges, ell)), Fraction(0))
    tree = mst_weight(len(vertices), [(u, v, Fraction(w)) for (u, v, _), w in zip(edges, ell)])
    assert tree is not None and tree >= len(part) - 1 and dot == crossing
    result = {
        "status": "feasible" if ratio >= q else "violation",
        "vertices": vertices,
        "q": text(q),
        "partition_count": count,
        "minimum_partition_ratio": text(ratio),
        "minimizing_partition": [[vertices[v] for v in block] for block in part],
    }
    if ratio < q:
        result["certificate"] = {
            "crossing_capacity": text(crossing),
            "blocks_minus_one": len(part) - 1,
            "edge_indicator_length": ell,
            "capacity_dot_length": text(dot),
            "kruskal_mst_length": text(tree),
            "strict_violation": f"{text(dot)} < {text(q)} * {text(tree)}",
        }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
