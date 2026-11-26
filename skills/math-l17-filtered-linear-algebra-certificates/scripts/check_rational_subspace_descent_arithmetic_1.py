#!/usr/bin/env python3
"""Exact finite analogue of rational-span descent in arithmetic-1 p.3/p.25."""
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


def rank(rows):
    a = [row[:] for row in rows]
    if not a:
        return 0
    pivots = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivots, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivots], a[pivot] = a[pivot], a[pivots]
        d = a[pivots][col]
        a[pivots] = [x / d for x in a[pivots]]
        for i in range(len(a)):
            if i != pivots and a[i][col]:
                f = a[i][col]
                a[i] = [x - f * y for x, y in zip(a[i], a[pivots])]
        pivots += 1
    return pivots


def main(path):
    data = json.loads(Path(path).read_text())
    basis = [[Q(x) for x in row] for row in data['rational_span_basis']]
    candidate = [Q(x) for x in data['candidate']]
    if not basis or any(len(row) != len(candidate) for row in basis):
        raise ValueError('basis must be nonempty with the candidate ambient dimension')
    r = rank(basis)
    augmented = rank(basis + [candidate])
    if augmented != r:
        raise ValueError('candidate is outside the rational span')
    print('verified: candidate lies in the exact rational span (rank %d)' % r)


try:
    raise SystemExit(main(sys.argv[1]))
except (IndexError, KeyError, ValueError, ZeroDivisionError) as error:
    print('rejected: ' + str(error), file=sys.stderr)
    raise SystemExit(2)
