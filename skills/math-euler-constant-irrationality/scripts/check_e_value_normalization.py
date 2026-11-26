#!/usr/bin/env python3
"""Exact structural checks for the E-value normalization admission record.

The relation labels are evidence references supplied by the caller. No finite
computation decides Q-linear dependence of general E-values.
"""

from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path


ALLOWED = {"proved-dependent", "proved-independent", "undecided"}


def parse_rational(value: str) -> Fraction:
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"not an exact rational node: {value!r}") from exc


def main(path: str) -> int:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    points = data.get("points")
    if not isinstance(points, list) or not points:
        raise ValueError("points must be a nonempty list")
    seen: set[Fraction] = set()
    for index, point in enumerate(points, start=1):
        alpha = parse_rational(point["alpha"])
        if alpha == 0:
            raise ValueError(f"point {index}: alpha must be nonzero")
        if alpha in seen:
            raise ValueError(f"point {index}: alpha must be pairwise distinct")
        seen.add(alpha)
        values = point.get("value_labels")
        if not isinstance(values, list) or not values:
            raise ValueError(f"point {index}: value_labels must be nonempty")
        for key in ("homogeneous_status", "inhomogeneous_status"):
            if point.get(key) not in ALLOWED:
                raise ValueError(f"point {index}: invalid {key}")
        print(f"alpha={alpha}: {len(values)} requested value(s)")
        print("  homogeneous singular iff values are Q-dependent: "
              f"declared {point['homogeneous_status']}")
        print("  inhomogeneous singular iff 1 and values are Q-dependent: "
              f"declared {point['inhomogeneous_status']}")
    print("PASS: exact node constraints checked. Relation labels were not decided by this script.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1]))
    except IndexError:
        raise SystemExit("usage: check_e_value_normalization.py MANIFEST.json")
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        raise SystemExit(f"FAIL: {exc}")
