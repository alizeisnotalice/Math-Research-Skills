#!/usr/bin/env python3
"""Certify a scalar Chernoff bound for a finite stationary reversible chain."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


from rational_reversible_chain import rational, reversible_chain


def integer(value: object, name: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{name} must be an integer")
    return value


def is_psd(matrix: list[list[Fraction]]) -> bool:
    """Test PSD by exact Schur complements, including zero pivots."""
    work = [row[:] for row in matrix]
    for i in range(len(work)):
        pivot = work[i][i]
        remaining = range(i + 1, len(work))
        if pivot < 0:
            return False
        if pivot == 0:
            if any(work[i][j] for j in remaining):
                return False
            continue
        for j in remaining:
            for k in remaining:
                work[j][k] -= work[j][i] * work[i][k] / pivot
    return True


def check(payload: object) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    _, pi, flow = reversible_chain(payload.get("transition"), payload.get("stationary"), require_positive=True)
    size = len(pi)

    raw_values = payload.get("observable")
    if not isinstance(raw_values, list) or len(raw_values) != size:
        raise ValueError("observable must have one integer value per state")
    values = [integer(x, "observable value") for x in raw_values]
    steps = integer(payload.get("steps"), "steps")
    threshold = integer(payload.get("threshold"), "threshold")
    u = rational(payload.get("tilt"))
    norm_bound = rational(payload.get("operator_bound"))
    if steps < 1 or u <= 1 or norm_bound <= 0:
        raise ValueError("require steps >= 1, tilt > 1 and operator_bound > 0")
    weights = [u**x for x in values]
    slack = [[(norm_bound * pi[i] / weights[i] if i == j else 0) - flow[i][j]
              for j in range(size)] for i in range(size)]
    if not is_psd(slack):
        raise ValueError("the proposed operator bound fails exact positive semidefiniteness")
    first_mgf = sum((pi[i] * weights[i] for i in range(size)), Fraction(0))
    mgf_bound = first_mgf * norm_bound**(steps - 1)
    tail_bound = mgf_bound / u**threshold
    return {"status": "verified_markov_chernoff_bound", "detailed_balance": True,
            "operator_bound": str(norm_bound), "steps": steps, "threshold": threshold,
            "tilted_mgf_bound": str(mgf_bound),
            "upper_tail_probability_bound": str(min(Fraction(1), tail_bound))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
