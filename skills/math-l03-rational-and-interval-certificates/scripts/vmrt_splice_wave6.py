#!/usr/bin/env python3
"""Exact numeric branch filter used in the pseudoindex-five VMRT splice."""
from fractions import Fraction


def main() -> int:
    roots = [Fraction(4), Fraction(8, 3)]
    accepted = []
    for u in roots:
        slope = u / 2 - 1
        assert slope > 0
        max_degree = 1 // slope
        for degree in range(3, max_degree + 1):
            genus = 1 - slope * degree
            if genus.denominator == 1:
                accepted.append((u, degree, genus))
    assert accepted == [(Fraction(8, 3), 3, Fraction(0))]
    print("u=8/3 L3=3 genus=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
