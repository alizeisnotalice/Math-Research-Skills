#!/usr/bin/env python3
"""Exact conditional-negative-semidefinite test for a rational symmetric matrix."""
from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


def rat(x):
    if isinstance(x, bool) or not isinstance(x, (str, int)):
        raise ValueError("entries must be integer or rational strings")
    return Fraction(x)


def determinant(a):
    a = [row[:] for row in a]
    n, sign, prev = len(a), 1, Fraction(1)
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if a[r][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) / prev
        prev = a[k][k]
        if not prev:
            return Fraction(0)
    return sign * a[-1][-1]


def main(argv):
    if len(argv) != 2:
        print("usage: check_cnd_matrix.py MATRIX.json", file=sys.stderr); return 2
    try:
        raw = json.loads(Path(argv[1]).read_text())
        if not isinstance(raw, list) or len(raw) < 2 or any(not isinstance(r, list) or len(r) != len(raw) for r in raw):
            raise ValueError("matrix must be a square JSON array of order at least two")
        d = [[rat(x) for x in row] for row in raw]
        n = len(d)
        if any(d[i][i] or d[i][j] != d[j][i] for i in range(n) for j in range(n)):
            raise ValueError("matrix must be symmetric with zero diagonal")
    except (OSError, json.JSONDecodeError, ValueError, ZeroDivisionError) as exc:
        print(f"input rejected: {exc}", file=sys.stderr); return 2
    b = [[-(d[i][j] - d[i][-1] - d[-1][j]) for j in range(n - 1)] for i in range(n - 1)]
    for size in range(1, n):
        for subset in itertools.combinations(range(n - 1), size):
            minor = determinant([[b[i][j] for j in subset] for i in subset])
            if minor < 0:
                print(json.dumps({"status":"not_cnd","principal_subset":list(subset),"negative_psd_minor":str(minor)}, indent=2))
                return 1
    print(json.dumps({"status":"cnd","order":n,"checked_principal_minors":2 ** (n - 1) - 1}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
