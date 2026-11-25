#!/usr/bin/env python3
"""Exact finite replays for the two transforms in math-l15.

Run: python3 scripts/replay_unit_fractions.py
"""

from collections import Counter
from fractions import Fraction


def unit_sum(denominators: list[int]) -> Fraction:
    if any(not isinstance(d, int) or d <= 0 for d in denominators):
        raise ValueError("denominators must be positive integers")
    return sum((Fraction(1, d) for d in denominators), start=Fraction())


def distinctify(denominators: list[int]) -> list[int]:
    """Preserve a strict (0, 1) sum and the number of terms."""
    total = unit_sum(denominators)
    if not Fraction() < total < Fraction(1):
        raise ValueError("Lemma 2.2 requires a unit-fraction sum strictly in (0, 1)")

    result = list(denominators)
    while True:
        duplicate = next((d for d, count in Counter(result).items() if count >= 2), None)
        if duplicate is None:
            return sorted(result)
        result.remove(duplicate)
        result.remove(duplicate)
        if duplicate % 2 == 0:
            p = duplicate // 2
            if p < 2:
                raise AssertionError("a repeated denominator 2 contradicts total < 1")
            result.extend((p + 1, p * (p + 1)))
        else:
            p = (duplicate - 1) // 2
            if p < 1:
                raise AssertionError("a denominator 1 contradicts total < 1")
            result.extend((p + 1, (p + 1) * (2 * p + 1)))


def greedy_prepare(a: int, b: int, threshold: Fraction) -> tuple[list[int], Fraction | None]:
    """Return greedy denominators and either zero or the unreduced final remainder."""
    if not (isinstance(a, int) and isinstance(b, int) and 1 <= a < b):
        raise ValueError("requires integers 1 <= a < b")
    if threshold <= b:
        raise ValueError("requires threshold T > b")

    numerator, denominator = a, b
    terms: list[int] = []
    while denominator < threshold:
        z = (denominator + numerator - 1) // numerator
        terms.append(z)
        numerator, denominator = numerator * z - denominator, denominator * z
        if numerator == 0:
            return terms, None
        if not (0 < numerator < denominator and z >= 2):
            raise AssertionError("the strict positive-remainder invariant failed")
    return terms, Fraction(numerator, denominator)


def main() -> None:
    even_input = [4, 4, 5, 20]
    even_output = distinctify(even_input)
    assert unit_sum(even_input) == Fraction(3, 4) == unit_sum(even_output)
    assert len(even_input) == len(even_output) and len(set(even_output)) == len(even_output)

    odd_input = [3, 3, 10]
    odd_output = distinctify(odd_input)
    assert unit_sum(odd_input) == Fraction(23, 30) == unit_sum(odd_output)
    assert len(odd_input) == len(odd_output) and len(set(odd_output)) == len(odd_output)

    try:
        distinctify([2, 2])
    except ValueError:
        pass
    else:
        raise AssertionError("the equality boundary x = 1 must be rejected")

    zero_terms, zero_remainder = greedy_prepare(1, 2, Fraction(3))
    assert zero_terms == [2] and zero_remainder is None

    crossing_terms, crossing_remainder = greedy_prepare(2, 7, Fraction(20))
    assert crossing_terms == [4] and crossing_remainder == Fraction(1, 28)
    assert Fraction(2, 7) == unit_sum(crossing_terms) + crossing_remainder
    assert Fraction(20) <= crossing_remainder.denominator < Fraction(20) ** 2

    terminating_terms, terminating_remainder = greedy_prepare(3, 10, Fraction(101))
    assert terminating_terms == [4, 20] and terminating_remainder is None
    assert Fraction(3, 10) == unit_sum(terminating_terms)

    print("exact replay passed")
    print(f"even distinctify: {even_input} -> {even_output}")
    print(f"odd distinctify: {odd_input} -> {odd_output}")
    print(f"greedy crossing: 2/7 = 1/{crossing_terms[0]} + {crossing_remainder}")
    print("greedy termination: 3/10 = 1/4 + 1/20")


if __name__ == "__main__":
    main()
