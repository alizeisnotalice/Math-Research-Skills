#!/usr/bin/env python3
"""Compose a certified Dirichlet-character sum interval with a rational log tail."""
import argparse
from fractions import Fraction
import json


def tail_bound(start: int, through: int, exponent: int) -> Fraction:
    if min(start, through, exponent) < 2:
        raise ValueError("start, through, and integer exponent must all be at least 2")
    ratio = Fraction(1, start**exponent)
    first = ratio**(through + 1)
    majorant = 1 + Fraction(start, (through + 1) * exponent - 1)
    return majorant * first / ((1 - first) * (1 - ratio))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--start", type=int, required=True)
    parser.add_argument("--through", type=int, required=True)
    parser.add_argument("--exponent", type=int, required=True)
    parser.add_argument("--main-lower", type=Fraction, required=True)
    parser.add_argument("--main-upper", type=Fraction, required=True)
    args = parser.parse_args()
    try:
        error = tail_bound(args.start, args.through, args.exponent)
        if args.main_lower > args.main_upper:
            raise ValueError("main-sum interval is reversed")
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps({"log_lower": str(-args.main_upper - error),
                      "log_upper": str(-args.main_lower + error),
                      "cutoff_error_bound": str(error)}))


if __name__ == "__main__":
    main()
