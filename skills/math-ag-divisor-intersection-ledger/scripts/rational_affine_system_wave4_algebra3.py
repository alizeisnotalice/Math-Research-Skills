#!/usr/bin/env python3
"""Find a rational particular solution of a finite rational affine system."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction


def q(x):
    return Fraction(str(x))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    ns = ap.parse_args()
    try:
        d = json.load(open(ns.input))
        a = [[q(x) for x in row] for row in d["matrix"]]
        b = [q(x) for x in d["rhs"]]
        if not a or len(a) != len(b) or any(len(row) != len(a[0]) for row in a):
            raise ValueError("matrix and rhs must form a nonempty rectangular system")
        m, n = len(a), len(a[0])
        aug = [a[i] + [b[i]] for i in range(m)]
        pivots, r = [], 0
        for c in range(n):
            pivot = next((i for i in range(r, m) if aug[i][c]), None)
            if pivot is None:
                continue
            aug[r], aug[pivot] = aug[pivot], aug[r]
            z = aug[r][c]
            aug[r] = [v / z for v in aug[r]]
            for i in range(m):
                if i != r and aug[i][c]:
                    z = aug[i][c]
                    aug[i] = [aug[i][j] - z * aug[r][j] for j in range(n + 1)]
            pivots.append(c)
            r += 1
        if any(all(v == 0 for v in row[:n]) and row[n] != 0 for row in aug):
            raise ValueError("inconsistent rational affine system")
        x = [Fraction(0) for _ in range(n)]
        for i, c in enumerate(pivots):
            x[c] = aug[i][n]
        if any(sum(a[i][j] * x[j] for j in range(n)) != b[i] for i in range(m)):
            raise ValueError("internal exact residual check failed")
        print(json.dumps({"accepted": True, "particular_solution": [str(v) for v in x],
                          "pivot_columns": pivots, "free_variables_set_to_zero": True}, sort_keys=True))
        return 0
    except (OSError, KeyError, ValueError, ZeroDivisionError, json.JSONDecodeError) as exc:
        print(f"rejected: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
