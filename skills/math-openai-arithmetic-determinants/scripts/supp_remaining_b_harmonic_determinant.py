#!/usr/bin/env python3
"""Exact finite determinant for the EXT-0164 multiple-harmonic-sum matrix."""
from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path


def indices(size: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...] | None] = [None] * size
    out[0] = ()
    for i in range(size):
        k = out[i]
        assert k is not None
        even, odd = 2 * i, 2 * i + 1
        if even and even < size:
            out[even] = k[:-1] + (k[-1] + 1,) if k else ()
        if odd < size:
            out[odd] = k + (1,)
    return [x for x in out if x is not None]


def harmonic(cutoff: int, index: tuple[int, ...]) -> Fraction:
    if not index:
        return Fraction(1)
    return sum((Fraction(1, __import__("math").prod(n ** a for n, a in zip(choice, index)))
                for choice in itertools.combinations(range(1, cutoff), len(index))), Fraction(0))


def determinant(a: list[list[Fraction]]) -> Fraction:
    """Fraction-exact Bareiss elimination."""
    n = len(a)
    if not n:
        return Fraction(1)
    a = [row[:] for row in a]
    sign, prior = 1, Fraction(1)
    for k in range(n - 1):
        pivot = next((i for i in range(k, n) if a[i][k]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign *= -1
        pivot_value = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot_value - a[i][k] * a[k][j]) / prior
        prior = pivot_value
        for i in range(k + 1, n):
            a[i][k] = Fraction(0)
    return sign * a[-1][-1]


def main(path: str) -> None:
    try:
        data = json.loads(Path(path).read_text())
        w, n = data["weight"], data["N"]
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"ok": False, "error": f"need JSON integers weight and N: {exc}"}))
        raise SystemExit(2)
    if set(data) != {"weight", "N"} or not all(isinstance(x, int) and not isinstance(x, bool) for x in (w, n)) or w < 1 or n < 0:
        print(json.dumps({"ok": False, "error": "require weight>=1 and N>=0"}))
        raise SystemExit(2)
    order = 2 ** w
    if order > 16:
        print(json.dumps({"ok": False, "error": "weight is capped at 4 for this finite exact replay"}))
        raise SystemExit(2)
    ks = indices(order)
    matrix = [[harmonic(n + row + 1, k) for k in ks] for row in range(order)]
    det = determinant(matrix)
    print(json.dumps({"ok": True, "weight": w, "N": n, "order": order,
                      "determinant": str(det), "nonzero": bool(det),
                      "indices": [list(k) for k in ks]}, sort_keys=True))
    raise SystemExit(0 if det else 1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: supp_remaining_b_harmonic_determinant.py INSTANCE.json", file=sys.stderr)
        raise SystemExit(2)
    main(sys.argv[1])
