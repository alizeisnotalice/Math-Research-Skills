#!/usr/bin/env python3
"""Exact finite checks for Pilehrood--Pilehrood gamma approximants.

The local source is arXiv:1010.1420v3, PDF pp. 8--15.  This script checks
finite sum formulas, the two recurrences, and the non-simple continued fraction
obtained directly from Theorem A.  It does not prove an asymptotic statement or
an irrationality result.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from math import comb, factorial


def harmonic(index: int) -> Fraction:
    return sum((Fraction(1, divisor) for divisor in range(1, index + 1)), Fraction())


def sums(last_index: int) -> tuple[list[Fraction], list[int]]:
    """Return p_0,...,p_n and q_0,...,q_n from equation (21)."""
    p_values: list[Fraction] = []
    q_values: list[int] = []
    for index in range(last_index + 1):
        q_values.append(sum(comb(index, term) ** 2 * factorial(term) for term in range(index + 1)))
        p_values.append(
            sum(
                (Fraction(comb(index, term) ** 2 * factorial(term))
                 * (2 * harmonic(index - term) - harmonic(term))
                 for term in range(index + 1)),
                Fraction(),
            )
        )
    return p_values, q_values


def recurrence_values(last_index: int) -> tuple[list[Fraction], list[int]]:
    """Return the same values from Lemma 1's recurrences."""
    if last_index < 0:
        raise ValueError("last_index must be nonnegative")
    p_values = [Fraction(0)]
    q_values = [1]
    if last_index == 0:
        return p_values, q_values
    p_values.append(Fraction(1))
    q_values.append(2)
    for index in range(last_index - 1):
        q_values.append(2 * (index + 2) * q_values[index + 1] - (index + 1) ** 2 * q_values[index])
        p_values.append(
            2 * (index + 2) * p_values[index + 1]
            - (index + 1) ** 2 * p_values[index]
            - Fraction(index, index + 2)
        )
    return p_values, q_values


def theorem_a_partial_elements(p_values: list[Fraction], q_values: list[int]) -> tuple[list[Fraction], list[Fraction]]:
    """Compute Theorem A's unique non-simple continued-fraction elements."""
    last_index = len(p_values) - 1
    if last_index < 1:
        return [], []
    partial_numerators = [Fraction(1)]
    partial_denominators = [Fraction(q_values[1])]
    for index in range(2, last_index + 1):
        determinant = p_values[index - 1] * q_values[index - 2] - p_values[index - 2] * q_values[index - 1]
        if determinant == 0:
            raise ArithmeticError(f"Theorem A determinant vanishes at index {index}")
        partial_numerators.append(
            (p_values[index - 1] * q_values[index] - p_values[index] * q_values[index - 1]) / determinant
        )
        partial_denominators.append(
            (p_values[index] * q_values[index - 2] - p_values[index - 2] * q_values[index]) / determinant
        )
    return partial_numerators, partial_denominators


def convergents(partial_numerators: list[Fraction], partial_denominators: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    """Compute convergents of 0 + K(a_n/b_n)."""
    numerator_before, numerator_current = Fraction(1), Fraction(0)
    denominator_before, denominator_current = Fraction(0), Fraction(1)
    result_numerators: list[Fraction] = [numerator_current]
    result_denominators: list[Fraction] = [denominator_current]
    for numerator, denominator in zip(partial_numerators, partial_denominators):
        numerator_before, numerator_current = numerator_current, denominator * numerator_current + numerator * numerator_before
        denominator_before, denominator_current = denominator_current, denominator * denominator_current + numerator * denominator_before
        result_numerators.append(numerator_current)
        result_denominators.append(denominator_current)
    return result_numerators, result_denominators


def fraction_text(value: Fraction | int) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def check(last_index: int) -> tuple[list[Fraction], list[int], list[Fraction], list[Fraction]]:
    direct_p, direct_q = sums(last_index)
    recurrence_p, recurrence_q = recurrence_values(last_index)
    if (direct_p, direct_q) != (recurrence_p, recurrence_q):
        raise AssertionError("finite sums disagree with Lemma 1 recurrences")
    partial_a, partial_b = theorem_a_partial_elements(direct_p, direct_q)
    numerators, denominators = convergents(partial_a, partial_b)
    if numerators != direct_p or denominators != list(map(Fraction, direct_q)):
        raise AssertionError("Theorem A continued fraction does not reproduce p_n/q_n")
    return direct_p, direct_q, partial_a, partial_b


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--through", type=int, default=8, help="highest n to check, at least 0")
    arguments = parser.parse_args()
    if arguments.through < 0:
        parser.error("--through must be nonnegative")
    p_values, q_values, partial_a, partial_b = check(arguments.through)
    print(f"exact sums, recurrences, and Theorem A agree through n={arguments.through}")
    for index in range(arguments.through + 1):
        print(f"n={index}: p/q = {fraction_text(p_values[index] / q_values[index])}")
    for index, (numerator, denominator) in enumerate(zip(partial_a, partial_b), start=1):
        print(
            f"continued-fraction term {index}: "
            f"a_{index}={fraction_text(numerator)}, b_{index}={fraction_text(denominator)}"
        )
    print("scope: finite rational identities only; no irrationality conclusion")


if __name__ == "__main__":
    main()
