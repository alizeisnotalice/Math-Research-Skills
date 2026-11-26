"""Convert proven geometric bounds for integer linear forms to rational lower bounds."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


def rational(raw: str) -> Fraction:
    try:
        return Fraction(raw)
    except (ValueError, ZeroDivisionError) as error:
        raise argparse.ArgumentTypeError(str(error)) from error


def lower_bound(
    denominator: int, first_index: int, height_base: Fraction, height_scale: Fraction,
    lower_base: Fraction, lower_scale: Fraction, upper_base: Fraction, upper_scale: Fraction,
) -> tuple[int, Fraction]:
    """Use both possibilities for the integer determinant, for every numerator."""
    if denominator < 1 or first_index < 0:
        raise ValueError("require positive denominator and nonnegative first index")
    if min(height_scale, lower_scale, upper_scale) <= 0 or height_base < 1:
        raise ValueError("height base must be at least one and all scales positive")
    if not 0 < lower_base <= upper_base < 1:
        raise ValueError("require 0 < lower base <= upper base < 1")
    if lower_scale * lower_base**first_index > upper_scale * upper_base**first_index:
        raise ValueError("remainder bounds are reversed at the first index")

    threshold = Fraction(1, 2 * denominator) / upper_scale
    if upper_base**first_index <= threshold:
        index = first_index
    else:
        lo, hi = first_index, first_index + 1
        while upper_base**hi > threshold:
            lo, hi = hi, first_index + 2 * (hi - first_index)
        while hi - lo > 1:
            middle = (hi + lo) // 2
            if upper_base**middle <= threshold:
                hi = middle
            else:
                lo = middle
        index = hi

    height = height_scale * height_base**index
    nonzero_determinant = Fraction(1, 2 * denominator) / height
    zero_determinant = lower_scale * lower_base**index / height
    return index, min(nonzero_determinant, zero_determinant)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("denominator", type=int)
    parser.add_argument("--first-index", required=True, type=int)
    parser.add_argument("--height-base", required=True, type=rational)
    parser.add_argument("--height-scale", required=True, type=rational)
    parser.add_argument("--lower-base", required=True, type=rational)
    parser.add_argument("--lower-scale", required=True, type=rational)
    parser.add_argument("--upper-base", required=True, type=rational)
    parser.add_argument("--upper-scale", required=True, type=rational)
    args = parser.parse_args()
    try:
        index, bound = lower_bound(
            args.denominator, args.first_index, args.height_base, args.height_scale,
            args.lower_base, args.lower_scale, args.upper_base, args.upper_scale,
        )
    except ValueError as error:
        parser.error(str(error))
    print(json.dumps({
        "denominator": args.denominator,
        "selected_index": index,
        "absolute_error_at_least": str(bound),
        "requires": "the input bounds for integer forms have been proved for all indices in scope",
    }, indent=2))


if __name__ == "__main__":
    main()
