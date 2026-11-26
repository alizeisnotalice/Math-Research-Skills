#!/usr/bin/env python3
"""Check exact mass bookkeeping for a supplied stochastic box enclosure."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys


def mass_list(value: object, name: str) -> list[Fraction]:
    if not isinstance(value, list):
        raise ValueError(f"{name} must be a list")
    result = [Fraction(str(item)) for item in value]
    if any(item < 0 for item in result):
        raise ValueError(f"{name} contains a negative mass")
    return result


def check(document: dict[str, object]) -> dict[str, object]:
    if set(document) != {"inner_masses", "boundary_masses", "outside_mass"}:
        raise ValueError("expected inner_masses, boundary_masses, and outside_mass")
    inner = mass_list(document["inner_masses"], "inner_masses")
    boundary = mass_list(document["boundary_masses"], "boundary_masses")
    outside = Fraction(str(document["outside_mass"]))
    if outside < 0:
        raise ValueError("outside_mass is negative")
    lower = sum(inner, Fraction())
    upper = lower + sum(boundary, Fraction()) + outside
    if upper > 1:
        raise ValueError("the supplied enclosure exceeds total probability one")
    return {
        "status": "verified-supplied-stochastic-box-mass-enclosure",
        "local_lower_bound": str(lower),
        "local_upper_bound": str(upper),
        "global_maximum_lower_bound": str(lower),
        "requires": "caller-certified disjoint inner boxes, boundary coverage, box masses, tail bound, and feasible parameter",
        "not_certified": "interval containment, box masses, a tail estimate, an optimizer, or oracle-SGD convergence",
    }


def main() -> int:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_stochastic_box_mass_enclosure.py INPUT.json")
    try:
        result = check(json.loads(Path(sys.argv[1]).read_text()))
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        print(json.dumps({"status": "rejected", "reason": str(error)}, ensure_ascii=False))
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
