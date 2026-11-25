#!/usr/bin/env python3
"""Exact finite sanity check for the E05 high-certificate path bound.

This enumerates one small graph only; it is not a proof for arbitrary inputs.
"""
from fractions import Fraction

# n=3. Vertex 0 belongs to Max; vertices 1 and 2 belong to Min.
# Original weights; w_hat=4*w+1.  The chosen Max edge is tight; the Min
# inequalities are deliberately slack on one edge, so no zero-sum cycle is
# required.
EDGES = {
    0: ((1, -1),),
    1: ((2, 0),),
    2: ((0, 1),),
}
CHOICE = {0: 1}
H = {0: Fraction(0), 1: Fraction(3), 2: Fraction(2)}
N, W, MAX_LENGTH = 3, 1, 9


def weight(u, v):
    for x, w in EDGES[u]:
        if x == v:
            return w
    raise AssertionError((u, v))


for u, v in CHOICE.items():
    wh = (N + 1) * weight(u, v) + 1
    assert H[u] == wh + H[v], (u, v, H[u], wh + H[v])
for u in (1, 2):
    for v, w in EDGES[u]:
        assert H[u] <= (N + 1) * w + 1 + H[v], (u, v)

# Exact enumeration of all paths consistent with the high certificate.
min_weight = 0
for start in EDGES:
    states = [(start, 0)]
    for _ in range(MAX_LENGTH):
        next_states = []
        for u, total in states:
            options = ((CHOICE[u], weight(u, CHOICE[u])),) if u in CHOICE else EDGES[u]
            for v, w in options:
                next_states.append((v, total + w))
                min_weight = min(min_weight, total + w)
        states = next_states

bound = -(N - 1) * W
assert min_weight >= bound
print(f"checked chosen paths through length {MAX_LENGTH}: min={min_weight}, bound={bound}, PASS")
