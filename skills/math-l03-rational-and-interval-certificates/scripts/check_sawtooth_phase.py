#!/usr/bin/env python3
"""Exact rational witness checker for the finite sawtooth phase lemma."""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


def parse_fraction(value: object, name: str) -> Fraction:
    if isinstance(value, int) and not isinstance(value, bool):
        return Fraction(value)
    if isinstance(value, str):
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as error:
            raise ValueError(f"{name} is not a rational literal: {value!r}") from error
    raise ValueError(f"{name} must be an integer or a rational string")


def fractional_part(value: Fraction) -> Fraction:
    return value - (value.numerator // value.denominator)


def show(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def main(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    q = data.get("q")
    x_raw = data.get("x")
    c_raw = data.get("c")
    if not isinstance(q, list) or not q:
        raise ValueError("q must be a nonempty list")
    if not isinstance(x_raw, list) or not isinstance(c_raw, list) or len(q) != len(x_raw) == len(c_raw):
        raise ValueError("q, x, and c must be equally long nonempty lists")
    if any(not isinstance(item, int) or isinstance(item, bool) or item < 1 for item in q):
        raise ValueError("each q entry must be a positive integer")
    x = [parse_fraction(value, "x") for value in x_raw]
    c = [parse_fraction(value, "c") for value in c_raw]
    if any(value <= 0 for value in c):
        raise ValueError("each c entry must be positive")
    total_weight = sum((Fraction(q_i) * c_i for q_i, c_i in zip(q, c)), Fraction())
    bound = (sum(c, Fraction()) - sum((Fraction(q_i) * c_i * c_i for q_i, c_i in zip(q, c)), Fraction()) / total_weight) / 2
    candidates = []
    for index, (q_i, x_i) in enumerate(zip(q, x)):
        for k in range(q_i):
            phase = -(x_i + k) / q_i
            value = sum((c_j * fractional_part(x_j + q_j * phase)
                         for q_j, x_j, c_j in zip(q, x, c)), Fraction())
            candidates.append((value, phase, index, k))
    value, phase, index, k = min(candidates)
    print(json.dumps({
        "candidate_count": len(candidates),
        "witness_phase": show(phase),
        "witness_from": {"index": index, "k": k},
        "weighted_fractional_sum": show(value),
        "lemma_bound": show(bound),
        "certificate_holds": value <= bound,
    }, sort_keys=True))
    return 0 if value <= bound else 1


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError(f"usage: {Path(sys.argv[0]).name} INPUT.json")
        raise SystemExit(main(Path(sys.argv[1])))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
