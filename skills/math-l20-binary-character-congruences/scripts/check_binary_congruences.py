#!/usr/bin/env python3
"""Exact finite checks for the binary-character congruence interface."""

from itertools import product
from random import Random


def character_value(coefficients, point):
    """Evaluate sum_g coefficients[g] (-1)^(g dot point) exactly."""
    total = 0
    for group_element, coefficient in enumerate(coefficients):
        parity = (group_element & point).bit_count() & 1
        total += -coefficient if parity else coefficient
    return total


def find_match(coefficients_by_test, dimension, precision):
    modulus = 1 << precision
    baseline = [character_value(coefficients, 0) % modulus for coefficients in coefficients_by_test]
    for point in range(1, 1 << dimension):
        values = [character_value(coefficients, point) % modulus for coefficients in coefficients_by_test]
        if values == baseline:
            return point
    return None


def main():
    # Lemma 3.4: r=2, M=2 needs b > 2(4-1), hence b=7 is the first covered dimension.
    dimension, tests, precision = 7, 2, 2
    rng = Random(20261125)
    coefficients = [[rng.randrange(-20, 21) for _ in range(1 << dimension)] for _ in range(tests)]
    point = find_match(coefficients, dimension, precision)
    assert point is not None
    modulus = 1 << precision
    assert all(
        (character_value(test, point) - character_value(test, 0)) % modulus == 0
        for test in coefficients
    )

    # Lemma 11.4: q=1, M=3 needs b > 1(8-2), hence b=7 is covered.
    coefficient_dimension, coefficient_precision = 7, 3
    coefficient = [rng.randrange(-50, 51) for _ in range(1 << coefficient_dimension)]
    coefficient_point = find_match([coefficient], coefficient_dimension, coefficient_precision)
    assert coefficient_point is not None
    assert (character_value(coefficient, coefficient_point) - character_value(coefficient, 0)) % (1 << coefficient_precision) == 0

    assert dimension > tests * ((1 << precision) - 1)
    assert coefficient_dimension > (1 << coefficient_precision) - 2
    print(
        "PASS: exact character enumeration found "
        f"x={point} for two mod-4 tests and x={coefficient_point} for one mod-8 coefficient test."
    )


if __name__ == "__main__":
    main()
