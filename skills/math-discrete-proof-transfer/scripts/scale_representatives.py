#!/usr/bin/env python3
"""Exact boundary/midpoint representatives for rational nested periodic grids."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path


class InputError(ValueError):
    pass


def frac(value: object) -> Fraction:
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise InputError(f"invalid rational {value!r}") from exc


def check(data: dict[str, object]) -> dict[str, object]:
    q, x = frac(data.get("q")), frac(data.get("x"))
    if not 0 < q < 1:
        raise InputError("require 0 < q < 1")
    cells = data.get("cells")
    if not isinstance(cells, list) or not cells:
        raise InputError("cells must be a nonempty list")
    boundary = {Fraction(1), Fraction(2)}
    for cell in cells:
        if not isinstance(cell, dict) or not isinstance(cell.get("n"), int) or not isinstance(cell.get("N"), int):
            raise InputError("each cell needs integer n and positive integer N")
        n, N = cell["n"], cell["N"]
        if n < 1 or N < 1 or N & (N - 1):
            raise InputError("require n >= 1 and dyadic N")
        step = q**n
        low = x + step
        high = x + 2 * step
        first = (low * N).__floor__() - 1
        last = (high * N).__ceil__() + 1
        for integer in range(first, last + 1):
            t = (Fraction(integer, N) - x) / step
            if Fraction(1) <= t <= Fraction(2):
                boundary.add(t)
    ordered = sorted(boundary)
    representatives = ordered + [(left + right) / 2 for left, right in zip(ordered, ordered[1:])]
    return {"boundaries": [str(v) for v in ordered], "representatives": [str(v) for v in sorted(representatives)], "count": len(representatives), "certified": "all supplied grid keys are constant on each open interval between consecutive boundaries"}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise InputError("top-level JSON must be an object")
        print(json.dumps(check(data), sort_keys=True))
    except (InputError, json.JSONDecodeError) as exc:
        print(f"rejected: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
