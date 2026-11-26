#!/usr/bin/env python3
"""Check the finite parity-cancellation interface of the cited construction."""
import json
import sys
from collections import defaultdict


def fail(message):
    raise ValueError(message)


def parse_component(data, name, inv):
    vertices = data.get("vertices")
    edges = data.get("edges")
    if not isinstance(vertices, list) or not vertices or len(set(vertices)) != len(vertices):
        fail(f"{name}.vertices must be a nonempty list of distinct names")
    vertex_set = set(vertices)
    outgoing = {v: {} for v in vertices}
    edge_set = set()
    for row in edges if isinstance(edges, list) else []:
        if not isinstance(row, list) or len(row) != 3:
            fail(f"{name}.edges rows must be [source,label,target]")
        source, label, target = row
        if source not in vertex_set or target not in vertex_set or label not in inv:
            fail(f"invalid {name} edge {row!r}")
        if label in outgoing[source]:
            fail(f"{name} has two outgoing edges labelled {label!r} at {source!r}")
        outgoing[source][label] = target
        edge_set.add((source, label, target))
    if not edge_set:
        fail(f"{name} has no edges")
    for source, label, target in edge_set:
        if (target, inv[label], source) not in edge_set:
            fail(f"{name} edge {(source,label,target)!r} lacks inverse-labelled reverse")
    seen = {vertices[0]}
    todo = [vertices[0]]
    while todo:
        source = todo.pop()
        for target in outgoing[source].values():
            if target not in seen:
                seen.add(target)
                todo.append(target)
    if seen != vertex_set:
        fail(f"{name} is not a connected full component")
    return vertices, outgoing


def main(path):
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    inv = data.get("label_inverse")
    if not isinstance(inv, dict) or not inv:
        fail("label_inverse must be a nonempty object")
    for label, opposite in inv.items():
        if label == opposite or inv.get(opposite) != label:
            fail("label_inverse must be a fixed-point-free involution")
    av, ao = parse_component(data.get("A", {}), "A", inv)
    bv, bo = parse_component(data.get("B", {}), "B", inv)
    left = data.get("left_labels")
    right = data.get("right_inverse_labels")
    if not isinstance(left, dict) or set(left) != set(av):
        fail("left_labels must name exactly A.vertices")
    if not isinstance(right, dict) or set(right) != set(bv):
        fail("right_inverse_labels must name exactly B.vertices")
    product = {}
    rows = data.get("products")
    if not isinstance(rows, list):
        fail("products must be a list of [left,right_inverse,value]")
    for row in rows:
        if not isinstance(row, list) or len(row) != 3:
            fail("products rows must have length three")
        key = (row[0], row[1])
        if key in product and product[key] != row[2]:
            fail(f"conflicting product oracle values for {key!r}")
        product[key] = row[2]
    value = {}
    for x in av:
        for y in bv:
            key = (left[x], right[y])
            if key not in product:
                fail(f"missing product-oracle entry for {key!r}")
            value[(x, y)] = product[key]
    adjacency = defaultdict(list)
    degree = defaultdict(int)
    handled = set()
    for x in av:
        for y in bv:
            common = set(ao[x]).intersection(bo[y])
            if len(common) % 2 != 1:
                fail(f"even common outgoing-label count at {(x,y)!r}: {len(common)}")
            for label in common:
                endpoint = (ao[x][label], bo[y][label])
                reverse_key = (endpoint, inv[label])
                key = ((x, y), label)
                if reverse_key in handled:
                    continue
                handled.add(key)
                adjacency[(x, y)].append(endpoint)
                adjacency[endpoint].append((x, y))
                degree[(x, y)] += 1
                degree[endpoint] += 1
    pairs = {(x, y) for x in av for y in bv}
    if set(degree) != pairs or any(degree[p] % 2 != 1 for p in pairs):
        fail("simultaneous-step multigraph does not have odd degree at every pair")
    unseen = set(pairs)
    components = []
    while unseen:
        start = unseen.pop()
        component = {start}
        todo = [start]
        while todo:
            point = todo.pop()
            for nxt in adjacency[point]:
                if value[nxt] != value[point]:
                    fail(f"product is not constant across simultaneous step {point!r}->{nxt!r}")
                if nxt not in component:
                    component.add(nxt)
                    unseen.discard(nxt)
                    todo.append(nxt)
        if len(component) % 2:
            fail(f"odd simultaneous component {sorted(component)!r}")
        components.append(component)
    histogram = defaultdict(int)
    for component in components:
        histogram[value[next(iter(component))]] += len(component)
    if any(count % 2 for count in histogram.values()):
        fail("a product coefficient has odd total multiplicity")
    print(f"ACCEPT components={len(components)} pairs={len(pairs)} coefficients={len(histogram)}")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("usage: check_f2_cancellation.py CERTIFICATE.json")
        main(sys.argv[1])
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"REJECT {error}")
        sys.exit(2)
