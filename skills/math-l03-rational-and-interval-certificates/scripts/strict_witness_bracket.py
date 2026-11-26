#!/usr/bin/env python3
"""Exact finite harness for declared lower certificates and strict upper witnesses."""
from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def as_fraction(value: str | int) -> Fraction:
    if type(value) not in (int, str):
        raise ValueError("certificates must be integers or rational strings")
    return Fraction(value)


def bracket(lower: list[str], upper_witnesses: list[str]) -> tuple[Fraction, Fraction]:
    if not isinstance(lower, list) or not isinstance(upper_witnesses, list):
        raise ValueError("certificates and witnesses must be arrays")
    lows = [as_fraction(x) for x in lower]
    ups = [as_fraction(x) for x in upper_witnesses]
    if not lows or not ups or any(a > b for a, b in zip(lows, lows[1:])):
        raise ValueError("need nonempty nondecreasing lower certificates and nonempty upper witnesses")
    lo, hi = lows[-1], min(ups)
    if lo >= hi:
        raise ValueError("the strongest lower certificate and strict upper witness are inconsistent")
    return lo, hi


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("input must be an object")
        lo, hi = bracket(data["lower"], data["strict_upper_witnesses"])
    except (OSError, KeyError, ValueError, ZeroDivisionError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps({"lower": str(lo), "upper": str(hi), "width": str(hi - lo)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
