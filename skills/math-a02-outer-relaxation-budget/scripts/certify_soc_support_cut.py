#!/usr/bin/env python3
"""Certify one rational supporting cut for a second-order cone."""

from fractions import Fraction
import json
from pathlib import Path
import sys


def rational(value: object) -> Fraction:
    return Fraction(str(value))


def certify(record: dict[str, object]) -> dict[str, object]:
    direction = [rational(value) for value in record["direction"]]
    point = [rational(value) for value in record["point"]]
    height = rational(record["height"])
    if not direction or len(direction) != len(point):
        raise ValueError("direction and point must be nonempty and have equal length")
    if height < 0:
        raise ValueError("height must be nonnegative")
    squared_norm = sum(value * value for value in direction)
    if squared_norm != 1:
        raise ValueError("direction must have exact squared norm 1")
    support_value = sum(a * b for a, b in zip(direction, point))
    cut_violation = support_value - height
    point_squared_norm = sum(value * value for value in point)
    return {
        "direction_squared_norm": str(squared_norm),
        "support_value": str(support_value),
        "height": str(height),
        "cut": "direction dot u <= t",
        "cut_violation": str(cut_violation),
        "point_squared_norm": str(point_squared_norm),
        "outside_soc_proved": cut_violation > 0,
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: certify_soc_support_cut.py input.json")
    try:
        print(json.dumps(certify(json.loads(Path(sys.argv[1]).read_text())), ensure_ascii=False))
    except (KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        raise SystemExit(f"invalid SOC support input: {error}")


if __name__ == "__main__":
    main()
