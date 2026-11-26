#!/usr/bin/env python3
"""Exact finite check of Kawashima's binomial-harmonic duality."""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache
from math import comb


def dual(index: tuple[int, ...]) -> tuple[int, ...]:
    if not index or any(part <= 0 for part in index):
        raise ValueError("index must be a nonempty tuple of positive integers")
    weight = sum(index)
    cuts: set[int] = set()
    total = 0
    for part in index[:-1]:
        total += part
        cuts.add(total)
    complement = [cut for cut in range(1, weight) if cut not in cuts]
    return tuple(b - a for a, b in zip([0, *complement], [*complement, weight]))


@lru_cache(maxsize=None)
def s(index: tuple[int, ...], n_value: int) -> Fraction:
    """Finite weak multiple harmonic sum with final summation index n_value."""
    if n_value < 0:
        return Fraction()
    if len(index) == 1:
        return Fraction(1, (n_value + 1) ** index[0])
    prefix = index[:-1]
    return sum((s(prefix, j) for j in range(n_value + 1)), Fraction()) / (n_value + 1) ** index[-1]


def nabla_s(index: tuple[int, ...], n_value: int) -> Fraction:
    return sum(((-1) ** k * comb(n_value, k) * s(index, k) for k in range(n_value + 1)), Fraction())


def main() -> None:
    examples = ((1,), (2,), (1, 1), (1, 2, 3), (2, 1, 2))
    for index in examples:
        paired = dual(index)
        for n_value in range(8):
            assert nabla_s(index, n_value) == s(paired, n_value)
        print(f"index={index} dual={paired} checked_n=0..7")


if __name__ == "__main__":
    main()
