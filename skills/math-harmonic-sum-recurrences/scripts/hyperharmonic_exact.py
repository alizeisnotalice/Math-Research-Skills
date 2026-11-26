#!/usr/bin/env python3
"""Exact finite generalized hyperharmonic coefficients from source (2.8)."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import comb


def elementary_reciprocal_sum(start: int, stop: int, order: int) -> Fraction:
    """e_order(1/start,...,1/stop), with e_0=1."""
    if order < 0:
        raise ValueError("order must be non-negative")
    values = [Fraction(0) for _ in range(order + 1)]
    values[0] = Fraction(1)
    for d in range(start, stop + 1):
        for r in range(order, 0, -1):
            values[r] += values[r - 1] / d
    return values[order]


def hyperharmonic(m: int, n: int, order: int) -> Fraction:
    """h_n^(m)(order) via (m)_n/n! times an elementary reciprocal sum."""
    if m < 1 or n < 1 or order < 0:
        raise ValueError("require m,n >= 1 and order >= 0")
    return comb(m + n - 1, m - 1) * elementary_reciprocal_sum(m, m + n - 1, order)


def harmonic(n: int, r: int) -> Fraction:
    return sum((Fraction(1, j**r) for j in range(1, n + 1)), Fraction())


def source_formula_through_four(m: int, n: int, order: int) -> Fraction:
    """Equations (2.12)--(2.15), for independent exact contact tests."""
    if not 1 <= order <= 4:
        raise ValueError("closed source contacts implemented only for orders 1,...,4")
    delta = {r: harmonic(m + n - 1, r) - harmonic(m - 1, r) for r in range(1, 5)}
    factor = Fraction(comb(m + n - 1, m - 1), 1)
    a1, a2, a3, a4 = (delta[i] for i in range(1, 5))
    if order == 1:
        return factor * a1
    if order == 2:
        return factor * (a1 * a1 - a2) / 2
    if order == 3:
        return factor * (a1**3 - 3 * a1 * a2 + 2 * a3) / 6
    return factor * (a1**4 - 6 * a1 * a1 * a2 + 3 * a2 * a2 + 8 * a1 * a3 - 6 * a4) / 24


def pair(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("m", type=int)
    parser.add_argument("n", type=int)
    parser.add_argument("order", type=int)
    args = parser.parse_args()
    try:
        result = hyperharmonic(args.m, args.n, args.order)
        output = {"status": "EXACT_HYPERHARMONIC", "m": args.m, "n": args.n,
                  "order": args.order, "value": pair(result),
                  "scope": "finite exact coefficient; no infinite Euler-sum evaluation"}
        if 1 <= args.order <= 4:
            output["source_formula_contact"] = pair(source_formula_through_four(args.m, args.n, args.order))
        print(json.dumps(output, sort_keys=True))
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
