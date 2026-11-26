#!/usr/bin/env python3
"""Exact contract checks for the finite Mayer--Vietoris survival interface."""
from fractions import Fraction


def rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    m, n, r = len(a), len(a[0]), 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        q = a[r][c]
        a[r] = [x / q for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [x - q * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def b1(vertices, edges, faces=()):
    d1 = [[0] * len(edges) for _ in vertices]
    for j, (u, v) in enumerate(edges):
        d1[u][j], d1[v][j] = -1, 1
    d2 = [[0] * len(faces) for _ in edges]
    edge_index = {tuple(sorted(e)): i for i, e in enumerate(edges)}
    for j, (a, b, c) in enumerate(faces):
        for sign, e in ((1, (b, c)), (-1, (a, c)), (1, (a, b))):
            d2[edge_index[tuple(sorted(e))]][j] += sign
    return len(edges) - rank(d1) - rank(d2)


# Positive: Y is a 3-cycle and Z is a tree attached at vertex 0; A={0} has H_1=0.
y_edges = [(0, 1), (1, 2), (0, 2)]
x_edges = y_edges + [(0, 3), (3, 4)]
assert b1(range(3), y_edges) == 1
assert b1(range(5), x_edges) == 1
print("positive: H1(Y)=1, H1(X)=1, and H1(Y∩Z)=0; survival contract holds")

# Boundary rejection: Z is the filled triangle, A=Y is the same boundary circle;
# its H_1 map into Y is identity, and the cycle dies in X.
assert b1(range(3), y_edges, [(0, 1, 2)]) == 0
print("boundary: H1(Y∩Z)->H1(Y) is nonzero and H1(X)=0; reject survival claim")
