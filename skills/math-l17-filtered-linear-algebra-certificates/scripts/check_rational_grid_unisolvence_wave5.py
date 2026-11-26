#!/usr/bin/env python3
"""Exact rank test for a finite rational evaluation grid of total degree at most d."""
import json
import sys
from fractions import Fraction as Q
from itertools import product
from pathlib import Path


def exponents(variables, degree):
    out = []
    for e in product(range(degree + 1), repeat=variables):
        if sum(e) <= degree:
            out.append(e)
    return out


def rank(rows):
    a = [r[:] for r in rows]
    piv = 0
    for col in range(len(a[0]) if a else 0):
        hit = next((i for i in range(piv, len(a)) if a[i][col]), None)
        if hit is None:
            continue
        a[piv], a[hit] = a[hit], a[piv]
        lead = a[piv][col]
        a[piv] = [x / lead for x in a[piv]]
        for i in range(len(a)):
            if i != piv and a[i][col]:
                f = a[i][col]
                a[i] = [x - f * y for x, y in zip(a[i], a[piv])]
        piv += 1
    return piv


def main(path):
    data = json.loads(Path(path).read_text())
    n, d = int(data['variables']), int(data['degree'])
    if n < 1 or d < 0:
        raise ValueError('variables must be positive and degree nonnegative')
    mons = exponents(n, d)
    pts = [[Q(x) for x in point] for point in data['points']]
    if any(len(point) != n for point in pts):
        raise ValueError('point dimension mismatch')
    matrix = [[Q(1) if not e else __import__('functools').reduce(lambda a, pair: a * pair[0] ** pair[1], zip(point, e), Q(1)) for e in mons] for point in pts]
    got = rank(matrix)
    if got != len(mons):
        raise ValueError('evaluation grid is not injective: rank %d < %d' % (got, len(mons)))
    print('verified: rational evaluation grid is injective for total degree <= %d (%d monomials)' % (d, len(mons)))


try:
    raise SystemExit(main(sys.argv[1]))
except (IndexError, KeyError, ValueError, ZeroDivisionError) as error:
    print('rejected: ' + str(error), file=sys.stderr)
    raise SystemExit(2)
