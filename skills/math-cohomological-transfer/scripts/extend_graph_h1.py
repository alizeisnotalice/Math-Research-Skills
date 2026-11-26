#!/usr/bin/env python3
"""Exact Z/mZ zero-extension check for a subgraph of a 1-dimensional nerve."""
import json
import sys


def edge(value, vertices):
    if not isinstance(value, list) or len(value) != 2 or any(not isinstance(x, str) for x in value):
        raise ValueError("each edge must be a two-element list of vertex strings")
    a, b = value
    if a == b or a not in vertices or b not in vertices:
        raise ValueError("edge must join two distinct listed vertices")
    return tuple(sorted((a, b)))


def main(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    modulus = data.get("modulus")
    if not isinstance(modulus, int) or modulus < 2:
        raise ValueError("modulus must be an integer at least 2")
    vertices = data.get("vertices")
    if not isinstance(vertices, list) or not vertices or any(not isinstance(v, str) for v in vertices) or len(set(vertices)) != len(vertices):
        raise ValueError("vertices must be a nonempty duplicate-free list of strings")
    vertex_set = set(vertices)
    ambient = [edge(e, vertex_set) for e in data.get("edges", [])]
    if len(set(ambient)) != len(ambient):
        raise ValueError("ambient edges must be duplicate-free")
    ambient_set = set(ambient)
    triangles = data.get("triangles", [])
    if triangles:
        raise ValueError("ambient nerve has a listed 2-simplex; graph extension contract fails")
    values = {}
    for item in data.get("subgraph_cochain", []):
        if not isinstance(item, dict) or not isinstance(item.get("value"), int):
            raise ValueError("each cochain item needs integer value and edge")
        e = edge(item.get("edge"), vertex_set)
        if e not in ambient_set:
            raise ValueError("subgraph edge is not an ambient edge")
        if e in values:
            raise ValueError("subgraph cochain has a duplicate edge")
        values[e] = item["value"] % modulus
    extension = [{"edge": list(e), "value": values.get(e, 0)} for e in sorted(ambient_set)]
    print(json.dumps({"modulus": modulus, "extension": extension, "cocycle_reason": "no ambient 2-simplices"}, sort_keys=True))


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("usage: extend_graph_h1.py INPUT.json")
        main(sys.argv[1])
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"rejected: {exc}", file=sys.stderr)
        raise SystemExit(2)
