#!/usr/bin/env python3
"""Exact finite residues from Hancl--Kristensen, Corollary 4.2.

This is an exploration aid only. The corollary is conditional on a global
accumulation property; printing finitely many residues cannot prove gamma
irrational.
"""

from __future__ import annotations

import argparse
import hashlib
from fractions import Fraction
from math import factorial


def criterion_sum(n_value: int) -> Fraction:
    """Return the un-reduced finite sum in Corollary 4.2, exactly."""
    if n_value < 1:
        raise ValueError("N must be positive")
    upper = factorial(n_value) ** 3
    scale = factorial(n_value) ** 4
    return sum(
        (
            Fraction(((-1) ** index) * (index.bit_length() - 1) * scale, index)
            for index in range(n_value + 1, upper + 1)
        ),
        Fraction(),
    )


def fractional_part(value: Fraction) -> Fraction:
    return Fraction(value.numerator % value.denominator, value.denominator)


def integer_digest(value: int) -> str:
    """Return a stable short digest without decimal-converting a huge integer."""
    byte_count = max(1, (value.bit_length() + 7) // 8)
    return hashlib.sha256(value.to_bytes(byte_count, "big")).hexdigest()[:16]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-n", type=int, default=4, help="largest N (default: 4)")
    arguments = parser.parse_args()
    if not 1 <= arguments.max_n <= 5:
        raise SystemExit("--max-n must be in 1..5; the factorial truncation grows rapidly")
    for n_value in range(1, arguments.max_n + 1):
        residue = fractional_part(criterion_sum(n_value))
        print(
            f"N={n_value} upper={(factorial(n_value) ** 3)} "
            f"numerator_bits={residue.numerator.bit_length()} "
            f"denominator_bits={residue.denominator.bit_length()} "
            f"numerator_sha256_16={integer_digest(residue.numerator)} "
            f"denominator_sha256_16={integer_digest(residue.denominator)}"
        )


if __name__ == "__main__":
    main()
