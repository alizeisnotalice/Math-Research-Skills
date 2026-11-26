#!/usr/bin/env python3
"""Certify the exact one-dimensional Wasserstein-1 cost of finite rational laws."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path


def rational(value) -> Fraction:
    if type(value) not in (int, str):
        raise ValueError("atoms and masses must be integers or exact rational strings")
    return Fraction(value)


def law(rows) -> dict[Fraction, Fraction]:
    if not isinstance(rows, list):
        raise ValueError("each law must be a list of [location,mass] pairs")
    masses = defaultdict(Fraction)
    for row in rows:
        if not isinstance(row, list) or len(row) != 2:
            raise ValueError("each atom must contain its location and mass")
        x, mass = map(rational, row)
        if mass < 0:
            raise ValueError("atom masses must be nonnegative")
        if mass:
            masses[x] += mass
    if sum(masses.values()) != 1:
        raise ValueError("each law must have total mass exactly one")
    return dict(sorted(masses.items()))


def monotone_plan(left: dict[Fraction, Fraction], right: dict[Fraction, Fraction]):
    x = list(left)
    y = list(right)
    i = j = 0
    left_mass, right_mass = left[x[0]], right[y[0]]
    plan = []
    while i < len(x) and j < len(y):
        mass = min(left_mass, right_mass)
        plan.append((x[i], y[j], mass))
        left_mass -= mass
        right_mass -= mass
        if left_mass == 0:
            i += 1
            if i < len(x):
                left_mass = left[x[i]]
        if right_mass == 0:
            j += 1
            if j < len(y):
                right_mass = right[y[j]]
    return plan


def certificate(data: dict) -> dict:
    if not isinstance(data, dict):
        raise ValueError("input must contain left and right laws")
    left, right = law(data.get("left")), law(data.get("right"))
    plan = monotone_plan(left, right)
    cost = sum((p * abs(x - y) for x, y, p in plan), Fraction(0))
    knots = sorted(left.keys() | right.keys())
    potential = {knots[0]: Fraction(0)}
    cdf_gap = Fraction(0)
    for a, b in zip(knots, knots[1:]):
        cdf_gap += left.get(a, 0) - right.get(a, 0)
        slope = -1 if cdf_gap > 0 else 1 if cdf_gap < 0 else 0
        potential[b] = potential[a] + slope * (b - a)
    value = sum((potential[x] * (left.get(x, 0) - right.get(x, 0)) for x in knots), Fraction(0))
    if cost != value:
        raise ArithmeticError("monotone cost and Lipschitz dual value differ")
    return {
        "wasserstein_1": str(cost),
        "monotone_plan": [[str(x), str(y), str(p)] for x, y, p in plan],
        "lipschitz_potential": [[str(x), str(v)] for x, v in potential.items()],
        "dual_value": str(value),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(certificate(json.loads(args.input.read_text(encoding="utf-8"))), indent=2))
    except (OSError, ArithmeticError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
