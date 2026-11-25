#!/usr/bin/env python3
from collections import defaultdict


def first_displacement_conflict(edges):
    adjacency = defaultdict(list)
    for start, end, (dx, dy) in edges:
        adjacency[start].append((end, (dx, dy)))
        adjacency[end].append((start, (-dx, -dy)))

    potentials = {}
    for root in adjacency:
        if root in potentials:
            continue
        potentials[root] = (0, 0)
        stack = [root]
        while stack:
            vertex = stack.pop()
            x, y = potentials[vertex]
            for neighbor, (dx, dy) in adjacency[vertex]:
                expected = (x + dx, y + dy)
                if neighbor not in potentials:
                    potentials[neighbor] = expected
                    stack.append(neighbor)
                    continue
                px, py = potentials[neighbor]
                if expected != (px, py):
                    return expected[0] - px, expected[1] - py
    return None


def main():
    motif = [("u", "w", (-3, 0))]
    assert first_displacement_conflict(motif) is None
    conflict = first_displacement_conflict(motif + [("u", "w", (0, 0))])
    assert conflict == (3, 0)
    print(f"Exact period-three motif: bounded components of size 2; added edge gives displacement {conflict}")


if __name__ == "__main__":
    main()
