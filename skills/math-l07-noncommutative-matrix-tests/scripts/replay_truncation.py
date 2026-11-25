#!/usr/bin/env python3
"""Replay the Family 116 finite Taylor-truncation identity exactly."""

from __future__ import annotations

import argparse
from fractions import Fraction


def matrix(letter: int, dimension: int) -> list[list[Fraction]]:
    """Return the paper's T_letter on 1,z,...,z^(dimension-1)."""
    return [
        [
            Fraction((-1) ** (row - column - 1), row * letter ** (row - column))
            if column < row
            else Fraction()
            for column in range(dimension)
        ]
        for row in range(dimension)
    ]


def apply(operator: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum(entry * value for entry, value in zip(row, vector)) for row in operator]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dimension", type=int, default=7)
    args = parser.parse_args()
    if args.dimension < 4:
        parser.error("dimension must be at least 4 to detect the commutator")

    e0 = [Fraction(1)] + [Fraction()] * (args.dimension - 1)
    t1, t2 = matrix(1, args.dimension), matrix(2, args.dimension)
    h12 = apply(t1, apply(t2, e0))
    h21 = apply(t2, apply(t1, e0))
    commutator = [left - right for left, right in zip(h12, h21)]
    leading = next((degree for degree, value in enumerate(commutator) if value), None)
    assert leading == 3
    assert commutator[3] == Fraction(-1, 24)
    print(
        "PASS: T1*T2*e0 - T2*T1*e0 has leading coefficient "
        f"{commutator[3]} at z^{leading} (dimension={args.dimension})."
    )


if __name__ == "__main__":
    main()
