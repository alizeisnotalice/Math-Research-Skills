#!/usr/bin/env python3
"""Exact replay of the shift-commutator identity on a requested dimension."""

import argparse
import json


def matmul(left, right):
    n = len(left)
    return [
        [sum(left[i][k] * right[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dimension", type=int, required=True)
    args = parser.parse_args()
    n = args.dimension
    if n < 1:
        parser.error("dimension must be positive")
    x = [[0] * n for _ in range(n)]
    y = [[0] * n for _ in range(n)]
    for j in range(1, n):
        x[j - 1][j] = j
        y[j][j - 1] = 1
    xy, yx = matmul(x, y), matmul(y, x)
    defect = [[(1 if i == j else 0) - xy[i][j] + yx[i][j]
               for j in range(n)] for i in range(n)]
    expected = [[0] * n for _ in range(n)]
    expected[-1][-1] = n
    if defect != expected:
        raise AssertionError("the exact shift-commutator identity failed")
    print(json.dumps({
        "dimension": n,
        "defect_rank": 1,
        "normalized_defect_rank": f"1/{n}",
        "defect": defect,
    }))


if __name__ == "__main__":
    main()
