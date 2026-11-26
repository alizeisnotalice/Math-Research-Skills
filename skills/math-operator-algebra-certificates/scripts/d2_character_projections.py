#!/usr/bin/env python3
"""Exact regular-representation check for the D2 character projections."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction


ELTS = [(0, 0), (0, 1), (1, 0), (1, 1)]


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(4)] for i in range(4)]


def regular(g):
    return [[int(((ELTS[j][0] + g[0]) % 2, (ELTS[j][1] + g[1]) % 2) == ELTS[i]) for j in range(4)] for i in range(4)]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('fixture')
    args = parser.parse_args()
    cfg = json.load(open(args.fixture))
    if cfg.get('representation') != 'regular_d2':
        print(json.dumps({'ok': False, 'error': 'only the certified regular_d2 fixture is accepted'})); raise SystemExit(2)
    chars = [(0, 0), (0, 1), (1, 0), (1, 1)]
    projections = []
    for a, b in chars:
        P = [[Fraction(0) for _ in range(4)] for _ in range(4)]
        for g in ELTS:
            sign = (-1) ** (a * g[0] + b * g[1])
            R = regular(g)
            P = add(P, [[Fraction(sign * R[i][j], 4) for j in range(4)] for i in range(4)])
        projections.append(P)
    if cfg.get('corrupt_character'):
        projections[0][0][0] += Fraction(1, 4)
    I = [[Fraction(int(i == j)) for j in range(4)] for i in range(4)]
    total = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for P in projections:
        total = add(total, P)
    ok = all(matmul(P, P) == P for P in projections) and all(
        matmul(projections[i], projections[j]) == [[Fraction(0)] * 4 for _ in range(4)]
        for i in range(4) for j in range(4) if i != j
    ) and total == I
    if not ok:
        print(json.dumps({'ok': False, 'error': 'character projection identities fail'})); raise SystemExit(2)
    print(json.dumps({'ok': True, 'characters': 4, 'rank_each': 1, 'identity_decomposition': True}))


if __name__ == '__main__':
    main()
