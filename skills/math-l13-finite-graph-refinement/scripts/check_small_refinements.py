#!/usr/bin/env python3
'''Check that joint and separate tuple-color refinements can differ.'''

from collections import Counter
from itertools import product


def equivalent(graphs, joint):
    tables = [list(product(range(len(graph)), repeat=2)) for graph in graphs]
    colors = [
        {(x, y): (x == y, y in graph[x]) for x, y in table}
        for table, graph in zip(tables, graphs)
    ]
    while True:
        if Counter(colors[0].values()) != Counter(colors[1].values()):
            return False
        palette = {}
        renamed = []
        for table, graph, old in zip(tables, graphs, colors):
            current = {}
            for x, y in table:
                vectors = [(old[z, y], old[x, z]) for z in range(len(graph))]
                if joint:
                    signature = tuple(sorted(vectors))
                else:
                    signature = tuple(tuple(sorted(column)) for column in zip(*vectors))
                key = (old[x, y], signature)
                current[x, y] = palette.setdefault(key, len(palette))
            renamed.append(current)
        previous_classes = len(set(colors[0].values()) | set(colors[1].values()))
        if len(palette) == previous_classes:
            return Counter(renamed[0].values()) == Counter(renamed[1].values())
        colors = renamed


if __name__ == '__main__':
    cycle = [{(x-1) % 6, (x+1) % 6} for x in range(6)]
    triangles = [{y for y in range(6) if y != x and y//3 == x//3} for x in range(6)]
    assert equivalent([cycle, triangles], False)
    assert not equivalent([cycle, triangles], True)
    for parity, expected in (((0, 0, 0), 2), ((1, 0, 0), 0)):
        count = sum(
            ((a+b) % 2, (a+c) % 2, (b+c) % 2) == parity
            for a, b, c in product((0, 1), repeat=3)
        )
        assert count == expected
    print('PASS: separate versus joint refinements; parity lift counts 2 and 0')
