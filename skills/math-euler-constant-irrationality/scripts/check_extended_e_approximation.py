#!/usr/bin/env python3
"""Exact finite checks for Fischler--Rivoal's extended E-approximation to gamma.

The source is arXiv:1406.5995v1, physical pp. 27--28, equations (6.4)--(6.6).
This checks an exact finite identity only.  It does not certify the limiting theorem,
an irrationality result, or a general E-operator classification.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial


def coefficient_from_sum(index: int) -> Fraction:
    """Return P_index from the finite binomial formula in equation (6.6)'s setup."""
    terms = (
        (-1) ** term
        * Fraction(comb(index, term), term)
        * (1 - Fraction(1, factorial(term)))
        for term in range(1, index + 1)
    )
    return sum(terms, Fraction(0))


def coefficients_from_recurrence(last_index: int) -> list[Fraction]:
    """Generate P_0 through P_last_index from the source recurrence exactly."""
    if last_index < 0:
        return []

    values = [Fraction(0), Fraction(0)]
    if last_index < 2:
        return values[: last_index + 1]
    values.append(Fraction(1, 4))

    for index in range(last_index - 2):
        numerator = (
            (3 * index * index + 14 * index + 17) * values[index + 2]
            - (index + 2) * (3 * index + 5) * values[index + 1]
            + (index + 1) * (index + 2) * values[index]
        )
        values.append(numerator / (index + 3) ** 2)
    return values


def main() -> None:
    checked_through = 40
    from_sum = [coefficient_from_sum(index) for index in range(checked_through + 1)]
    from_recurrence = coefficients_from_recurrence(checked_through)

    if from_sum != from_recurrence:
        for index, (direct, recurrence) in enumerate(zip(from_sum, from_recurrence)):
            if direct != recurrence:
                raise AssertionError(
                    f"P_{index} differs: direct={direct}, recurrence={recurrence}"
                )
        raise AssertionError("coefficient lists have unequal lengths")

    expected = {0: Fraction(0), 1: Fraction(0), 2: Fraction(1, 4), 3: Fraction(17, 36), 5: Fraction(5197, 7200)}
    for index, value in expected.items():
        if from_sum[index] != value:
            raise AssertionError(f"P_{index}={from_sum[index]}, expected {value}")

    print(f"exact recurrence agrees with the finite sum for P_0 through P_{checked_through}")
    for index in sorted(expected):
        print(f"P_{index} = {from_sum[index]}")
    print("The source gives this construction as an extended E-approximation with log(1-z).")


if __name__ == "__main__":
    main()
