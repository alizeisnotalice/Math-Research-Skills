#!/usr/bin/env python3
"""Exact constants in the source's fixed-apex transport proposition."""
import argparse
from fractions import Fraction


def nonnegative(value: str) -> Fraction:
    answer = Fraction(value)
    if answer < 0:
        raise ValueError("C must be nonnegative")
    return answer


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("A")
    parser.add_argument("C")
    args = parser.parse_args()
    A = Fraction(args.A)
    if A <= 0:
        parser.error("A must be positive")
    try:
        C = nonnegative(args.C)
    except ValueError as exc:
        parser.error(str(exc))
    R0 = A + 3 * C * A
    k0 = max(C + A * A / 6, C * R0 * A)
    print(f"R0={R0} k0={k0}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
