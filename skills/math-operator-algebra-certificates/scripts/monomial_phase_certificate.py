#!/usr/bin/env python3
"""Exact principal-phase check for root-of-unity monomial unitaries.

Input JSON: {"q": positive int, "U": {"perm": [...], "phase": [...]},
"V": {...}}.  The jth basis vector is sent to zeta**phase[j] e_perm[j].
"""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def unitary(data: Any, q: int) -> tuple[list[int], list[int]]:
    if not isinstance(data, dict):
        raise ValueError("unitary must be an object")
    perm, phase = data.get("perm"), data.get("phase")
    if not isinstance(perm, list) or not isinstance(phase, list) or len(perm) != len(phase):
        raise ValueError("perm and phase must be lists of equal length")
    n = len(perm)
    if n == 0 or sorted(perm) != list(range(n)):
        raise ValueError("perm must be a permutation of 0,...,n-1")
    if not all(isinstance(a, int) for a in phase):
        raise ValueError("phase entries must be integers")
    return perm, [a % q for a in phase]


def phase_mass(perm: list[int], phase: list[int], q: int) -> Fraction:
    """Ordinary-trace phase mass from exact cycle eigenvalues."""
    n, seen, total = len(perm), set(), Fraction(0)
    for start in range(n):
        if start in seen:
            continue
        cycle, j = [], start
        while j not in seen:
            seen.add(j)
            cycle.append(j)
            j = perm[j]
        r = len(cycle)
        exponent = sum(phase[j] for j in cycle) % q
        for t in range(r):
            total += Fraction((exponent + q * t) % (q * r), q * r)
    return total


def product(left: tuple[list[int], list[int]], right: tuple[list[int], list[int]], q: int) -> tuple[list[int], list[int]]:
    lp, la = left
    rp, ra = right
    return [lp[rp[j]] for j in range(len(lp))], [(la[rp[j]] + ra[j]) % q for j in range(len(lp))]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    raw = json.loads(args.input.read_text())
    q = raw.get("q")
    if not isinstance(q, int) or q <= 0:
        raise ValueError("q must be a positive integer")
    u, v = unitary(raw.get("U"), q), unitary(raw.get("V"), q)
    if len(u[0]) != len(v[0]):
        raise ValueError("U and V must have the same dimension")
    lu, lv, luv = phase_mass(*u, q), phase_mass(*v, q), phase_mass(*product(u, v, q), q)
    print(f"L(U)={lu}; L(V)={lv}; L(UV)={luv}; subadditive={luv <= lu + lv}")
    return 0 if luv <= lu + lv else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as err:
        print(f"rejected: {err}")
        raise SystemExit(2)
