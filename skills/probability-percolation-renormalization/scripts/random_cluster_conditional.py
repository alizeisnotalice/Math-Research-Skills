#!/usr/bin/env python3
"""Compute the exact one-edge random-cluster conditional for supplied connectivity."""
import argparse
from fractions import Fraction


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--q", required=True)
    parser.add_argument("--odds", required=True)
    parser.add_argument("--connected", required=True, choices=("yes", "no"))
    args = parser.parse_args()
    try:
        q, odds = Fraction(args.q), Fraction(args.odds)
    except (ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    if q <= 0 or odds <= 0:
        parser.error("q and odds must be positive")
    component_factor = 1 if args.connected == "yes" else q
    print(odds / (component_factor + odds))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
