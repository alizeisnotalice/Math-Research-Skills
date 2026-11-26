#!/usr/bin/env python3
"""Exact verification of the two Bajpai--Bennett norm-form solution families."""

from __future__ import annotations

import argparse
import json


def value(t: int, x: int, y: int) -> int:
    a = t**3 - 1
    return x**3 - a * y**3 + 3 * a * x * y + a**2


def check(t: int) -> dict[str, object]:
    if t <= 1:
        raise ValueError("Theorem 1 requires an integer t greater than 1")
    pairs = ((t**2, 2*t), (t**2, -t))
    values = [value(t, x, y) for x, y in pairs]
    if any(abs(result) != 1 for result in values):
        raise AssertionError("the displayed solution families failed exact substitution")
    return {"t": t, "solutions": [{"x": x, "y": y, "value": v}
                                      for (x, y), v in zip(pairs, values)],
            "scope": "Exact verification of the two supplied solution families."}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("t", type=int)
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.t), sort_keys=True))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
