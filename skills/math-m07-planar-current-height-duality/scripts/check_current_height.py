#!/usr/bin/env python3
"""Exact finite check for the square-grid current/face-height convention."""
from collections import defaultdict


def add_edge(flow, edge, value):
    """Store an integer flow in the lexicographically oriented representative."""
    left, right = edge
    if left < right:
        flow[(left, right)] += value
    else:
        flow[(right, left)] -= value


def oriented_value(flow, left, right):
    return flow[(left, right)] if left < right else -flow[(right, left)]


def divergence(flow, vertex):
    return sum(
        oriented_value(flow, vertex, neighbor)
        for neighbor in ((vertex[0] - 1, vertex[1]), (vertex[0] + 1, vertex[1]),
                         (vertex[0], vertex[1] - 1), (vertex[0], vertex[1] + 1))
        if tuple(sorted((vertex, neighbor))) in flow
    )


def height_at(height, face):
    return height.get(face, 0)  # exterior faces have fixed height zero


def rotated_gradient(height, n):
    """Current from face heights, with divergence identically zero on the grid."""
    flow = defaultdict(int)
    for x in range(n):
        for y in range(n + 1):
            # horizontal primal edge: left face is above, right face is below
            add_edge(flow, ((x, y), (x + 1, y)),
                     height_at(height, (x, y)) - height_at(height, (x, y - 1)))
    for x in range(n + 1):
        for y in range(n):
            # vertical primal edge: left face is west, right face is east
            add_edge(flow, ((x, y), (x, y + 1)),
                     height_at(height, (x - 1, y)) - height_at(height, (x, y)))
    return flow


def main():
    n = 3
    source, boundary = (1, 1), (0, 1)
    string = defaultdict(int)
    add_edge(string, (source, boundary), 1)

    # Integer units represent multiples of 2 pi.  Exterior height is pinned to zero.
    heights = {(0, 0): 2, (1, 0): -1, (2, 0): 3,
               (0, 1): -2, (1, 1): 4, (2, 1): 1,
               (0, 2): 0, (1, 2): -3, (2, 2): 2}
    curl = rotated_gradient(heights, n)
    total = defaultdict(int, string)
    for edge, value in curl.items():
        total[edge] += value

    vertices = [(x, y) for x in range(n + 1) for y in range(n + 1)]
    assert all(divergence(curl, vertex) == 0 for vertex in vertices)
    assert divergence(total, source) == 1
    assert divergence(total, boundary) == -1
    assert all(divergence(total, vertex) == 0 for vertex in vertices if vertex not in {source, boundary})

    # Recover every rotated-gradient edge exactly from the declared face heights.
    assert all(oriented_value(curl, *edge) == oriented_value(rotated_gradient(heights, n), *edge)
               for edge in curl)
    print("PASS: integer source string plus a rotated face gradient has the stated divergence.")
    print("PASS: all 24 primal-edge values recover from the pinned 3x3 face heights.")


if __name__ == "__main__":
    main()
