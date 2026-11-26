#!/usr/bin/env python3
"""Check the finite coupled L2 distance after centering and standardizing."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def rational(value: object) -> Fraction:
    if type(value) not in (int, str):
        raise ValueError("supply integers or exact rational strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"invalid rational {value!r}") from error


def at_least_scaled_root(a: Fraction, b: Fraction, radicand: Fraction) -> bool:
    """Sign-aware test of a >= b*sqrt(radicand), with positive radicand."""
    if b >= 0:
        return a >= 0 and a * a >= b * b * radicand
    return a >= 0 or a * a <= b * b * radicand


def audit(data: object) -> dict:
    if not isinstance(data, dict) or not isinstance(raw := data.get("atoms"), list) or not raw:
        raise ValueError("input must contain a nonempty atoms array")
    atoms = []
    for row in raw:
        if not isinstance(row, dict) or not {"mass", "x", "y"} <= row.keys():
            raise ValueError("every atom needs mass, x, and y")
        atoms.append(tuple(rational(row[k]) for k in ("mass", "x", "y")))
    if any(m < 0 for m, _, _ in atoms) or sum(m for m, _, _ in atoms) != 1:
        raise ValueError("masses must be nonnegative and sum to one")
    mean_x = sum(m * x for m, x, _ in atoms)
    mean_y = sum(m * y for m, _, y in atoms)
    centered = [(m, x - mean_x, y - mean_y) for m, x, y in atoms]
    variance_x = sum(m * x**2 for m, x, _ in centered)
    variance_y = sum(m * y**2 for m, _, y in centered)
    if min(variance_x, variance_y) <= 0:
        raise ValueError("both variables must have strictly positive variance")
    covariance = sum(m * x * y for m, x, y in centered)
    perturbation = sum(m * (y - x)**2 for m, x, y in centered)
    root_arg = variance_x * variance_y
    bound = min(Fraction(4), 4 * perturbation / max(variance_x, variance_y),
                perturbation / min(variance_x, variance_y))
    verify = at_least_scaled_root(covariance, 1 - bound / 2, root_arg)
    assert verify
    found = {
        "means": list(map(str, (mean_x, mean_y))),
        "variances": list(map(str, (variance_x, variance_y))),
        "centered_perturbation_variance": str(perturbation),
        "squared_coupled_l2_exact_form": {
            "constant": "2", "coefficient_over_square_root": str(-2 * covariance),
            "radicand": str(root_arg),
        },
        "certified_squared_l2_upper_bound": str(bound),
    }
    if "claimed_upper_bound" in data:
        claimed = rational(data["claimed_upper_bound"])
        if claimed < 0 or not at_least_scaled_root(covariance, 1 - claimed / 2, root_arg):
            raise ValueError("claimed squared L2 upper bound is false for the supplied coupling")
        found["checked_claimed_upper_bound"] = str(claimed)
    return found


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        result = audit(data)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
