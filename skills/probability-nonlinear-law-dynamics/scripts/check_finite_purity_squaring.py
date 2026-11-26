#!/usr/bin/env python3
"""Check normalized squaring and the exact largest-atom defect relations."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json


def rational(value: str) -> Fraction:
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise argparse.ArgumentTypeError("use an exact rational weight") from error


def audit(weights: list[Fraction]) -> dict:
    if not weights or any(weight < 0 for weight in weights) or sum(weights) != 1:
        raise ValueError("weights must be nonnegative and sum to one")
    purity = sum(weight**2 for weight in weights)
    defect = 1 - purity
    updated = [weight**2 / purity for weight in weights]
    next_defect = 1 - sum(weight**2 for weight in updated)
    next_bound = defect**2 / (2 * purity**2)
    tail = 1 - max(weights)
    lower_defect = 2 * tail * (1 - tail)
    upper_defect = 1 - (1 - tail)**2
    assert 0 <= next_defect <= next_bound and lower_defect <= defect <= upper_defect
    result = {
        "purity_defect": str(defect),
        "updated_weights": list(map(str, updated)),
        "updated_defect": str(next_defect),
        "updated_defect_upper_bound": str(next_bound),
        "tail_mass": str(tail),
        "lower_defect_from_tail": str(lower_defect),
        "upper_defect_from_tail": str(upper_defect),
    }
    if defect < Fraction(1, 2):
        assert tail < Fraction(1, 2)
        result["small_branch_radicand"] = str(1 - 2 * defect)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("weights", nargs="+", type=rational)
    args = parser.parse_args()
    try:
        result = audit(args.weights)
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
