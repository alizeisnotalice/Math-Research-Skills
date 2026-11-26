#!/usr/bin/env python3
"""Exact gate for the 2-by-4 coefficient-matrix conditions used in wave6 p.7--9."""
import json
import sys
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path


def determinant(a, b):
    return a[0] * b[1] - a[1] * b[0]


def main(path):
    matrices = json.loads(Path(path).read_text())['matrices']
    if not matrices:
        raise ValueError('need at least one matrix')
    for index, raw in enumerate(matrices, 1):
        if len(raw) != 2 or any(len(row) != 4 for row in raw):
            raise ValueError('matrix %d is not 2-by-4' % index)
        cols = [(Q(raw[0][j]), Q(raw[1][j])) for j in range(4)]
        bad = [pair for pair in combinations(range(4), 2) if determinant(cols[pair[0]], cols[pair[1]]) == 0]
        if bad:
            raise ValueError('matrix %d has vanishing 2-by-2 minor at columns %s' % (index, bad[0]))
    print('verified: every matrix has all 2-by-2 minors nonzero; all deletion rank gates follow')


try:
    raise SystemExit(main(sys.argv[1]))
except (IndexError, KeyError, ValueError, ZeroDivisionError) as error:
    print('rejected: ' + str(error), file=sys.stderr)
    raise SystemExit(2)
