#!/usr/bin/env python3
"""Construct a dominated measure saturating a finite submodular capacity."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path


def members(mask: int):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit


def exact(value: object) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError("capacity values must be exact integer or rational strings")
    return Fraction(value)


def certificate(raw: object, target: int) -> dict:
    if not isinstance(raw, list) or not raw or len(raw) & (len(raw) - 1):
        raise ValueError("capacity must list all subsets in bitmask order")
    if not 0 <= target < len(raw):
        raise ValueError("target bitmask outside the ground set")
    capacity = list(map(exact, raw))
    if capacity[0] != 0:
        raise ValueError("normalized capacity requires value zero at the empty set")
    full = len(capacity) - 1
    for mask,r in enumerate(capacity):
        missing = list(members(full ^ mask))
        for i in missing:
            if capacity[mask | i] < r:
                raise ValueError(f"capacity is not nondecreasing at masks {mask}, {mask | i}")
        for i,j in combinations(missing, 2):
            if capacity[mask | i] + capacity[mask | j] < r + capacity[mask | i | j]:
                raise ValueError(f"capacity fails adjacent submodularity at masks {mask}, {mask|i}, {mask|j}, {mask|i|j}")

    weights = [Fraction(0) for _ in members(full)]
    prefix = 0
    order = [*members(target),*members(full ^ target)]
    for atom in order:
        successor = prefix | atom
        weights[atom.bit_length() - 1] = capacity[successor] - capacity[prefix]
        prefix = successor
    masses = [Fraction(0)] * len(capacity)
    for mask in range(1,len(capacity)):
        atom = mask & -mask
        masses[mask] = masses[mask ^ atom] + weights[atom.bit_length() - 1]
        if masses[mask] > capacity[mask]:
            raise ArithmeticError(f"greedy witness failed domination at mask {mask}")
    if masses[target] != capacity[target] or masses[full] != capacity[full]:
        raise ArithmeticError("greedy witness did not saturate the target and ground set")
    return {"status":"certified-finite-dominated-measure","target_mask":target,
            "atom_order_zero_based":[x.bit_length() - 1 for x in order],
            "atom_weights":[str(w) for w in weights],"target_value":str(masses[target]),
            "total_mass":str(masses[full]),"subsets_checked":len(capacity)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input",type=Path,help="JSON array of capacity values indexed by bitmask")
    parser.add_argument("--target",type=int,required=True)
    args = parser.parse_args()
    try:
        values = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(certificate(values,args.target),indent=2))
    except (OSError,ValueError,ZeroDivisionError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
