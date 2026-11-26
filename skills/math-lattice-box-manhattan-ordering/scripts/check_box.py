#!/usr/bin/env python3
"""Exhaustively optimize the Manhattan length of an ordering in a small box."""

import argparse
from itertools import permutations, product
import json
from math import prod


def distance(left, right):
    return sum(abs(x - y) for x, y in zip(left, right))


def length(ordering):
    return sum(distance(left, right) for left, right in zip(ordering, ordering[1:]))


def check_box(sides):
    if not sides or any(side < 1 for side in sides):
        raise ValueError("positive side lengths required")
    size = prod(sides)
    if size > 9:
        raise ValueError("enumeration limited to nine points")
    points = list(product(*(range(side) for side in sides)))
    best = max(permutations(points), key=length)
    maximum = length(best)

    # All centered coordinates are doubled so the loss identity uses integers.
    centered = [tuple(2 * point[i] - side + 1 for i, side in enumerate(sides)) for point in best]
    endpoint_cost = sum(abs(x) for x in centered[0]) + sum(abs(x) for x in centered[-1])
    same_side_cost = sum(
        2 * min(abs(x), abs(y))
        for left, right in zip(centered, centered[1:])
        for x, y in zip(left, right) if x * y > 0
    )
    twice_radial_sum = sum(size // side * (side * side // 2) for side in sides)
    identity = 2 * maximum == 2 * twice_radial_sum - endpoint_cost - same_side_cost
    return {
        "sides": sides,
        "points": size,
        "maximum": maximum,
        "ordering": best,
        "centering_identity": identity,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sides", required=True, help="comma-separated positive side lengths")
    args = parser.parse_args()
    try:
        report = check_box(tuple(map(int, args.sides.split(","))))
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps(report, sort_keys=True))
    if not report["centering_identity"]:
        raise SystemExit("centering identity mismatch")


if __name__ == "__main__":
    main()
