#!/usr/bin/env python3
"""Exact equality data for the zero-sum l1 extremizer used in simplex projections."""

import argparse
from fractions import Fraction
import json


def equality_data(dimension: int, positive_count: int) -> dict[str, object]:
    if dimension < 2:
        raise ValueError("dimension must be at least 2")
    if not 1 <= positive_count < dimension:
        raise ValueError("positive_count must lie between 1 and dimension - 1")

    negative_count = dimension - positive_count
    positive_square = Fraction(negative_count, dimension * positive_count)
    negative_square = Fraction(positive_count, dimension * negative_count)
    l1_squared = Fraction(4 * positive_count * negative_count, dimension)
    maximum_l1_squared = Fraction(4 * (dimension // 2) * ((dimension + 1) // 2), dimension)
    return {
        "dimension": dimension,
        "positive_count": positive_count,
        "negative_count": negative_count,
        "positive_coordinate_square": str(positive_square),
        "negative_coordinate_square": str(negative_square),
        "zero_sum": True,
        "squared_l2_norm": "1",
        "squared_l1_norm": str(l1_squared),
        "squared_global_maximum_l1_norm": str(maximum_l1_squared),
        "is_global_extremizer": l1_squared == maximum_l1_squared,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("dimension", type=int)
    parser.add_argument("positive_count", type=int)
    args = parser.parse_args()
    try:
        print(json.dumps(equality_data(args.dimension, args.positive_count), ensure_ascii=False))
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
