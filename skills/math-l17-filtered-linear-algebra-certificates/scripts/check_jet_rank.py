#!/usr/bin/env python3
"""Exact finite rank/kernel replay for a supplied jet-condition matrix."""
import json
import sys
from fractions import Fraction


def rat(x):
    return Fraction(str(x))


def rref(rows):
    a = [row[:] for row in rows]
    m = len(a)
    n = len(a[0]) if m else 0
    pivots = []
    row = 0
    for col in range(n):
        pivot = next((i for i in range(row, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [x / scale for x in a[row]]
        for i in range(m):
            if i != row and a[i][col]:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        row += 1
        if row == m:
            break
    return a, pivots


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    rows = [[rat(x) for x in row] for row in data["matrix"]]
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("matrix must be nonempty and rectangular")
    reduced, pivots = rref(rows)
    n = len(rows[0])
    free = [j for j in range(n) if j not in pivots]
    kernel = []
    for free_col in free:
        v = [Fraction(0) for _ in range(n)]
        v[free_col] = Fraction(1)
        for i, pivot_col in enumerate(pivots):
            v[pivot_col] = -reduced[i][free_col]
        kernel.append([str(x) for x in v])
    result = {"rank": len(pivots), "nullity": len(free), "kernel_basis": kernel}
    expected = data.get("expected_nullity")
    if expected is not None and result["nullity"] != expected:
        print(json.dumps({"valid": False, **result, "expected_nullity": expected}))
        return 2
    print(json.dumps({"valid": True, **result}))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1]))
    except (IndexError, KeyError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"valid": False, "error": str(exc)}))
        raise SystemExit(2)
