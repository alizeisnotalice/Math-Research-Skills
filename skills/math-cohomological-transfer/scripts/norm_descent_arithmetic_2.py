#!/usr/bin/env python3
"""Exact finite-fibre norm for the scoped semiampleness descent reference."""
from fractions import Fraction
import argparse


def parse_fraction(token: str) -> Fraction:
    value = Fraction(token)
    if value == 0:
        raise ValueError("a fibre value is zero; nonzero norm is uncertified")
    return value


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("values", nargs="+", help="nonzero rational values")
    args = parser.parse_args()
    try:
        values = [parse_fraction(token) for token in args.values]
    except ValueError as exc:
        parser.error(str(exc))
    norm = Fraction(1)
    for value in values:
        norm *= value
    print(f"degree={len(values)} norm={norm} nonzero={norm != 0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
