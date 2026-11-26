#!/usr/bin/env python3
"""Exact replay of the rational degree-10 cross-endpoint polynomial sublemma."""

from fractions import Fraction
from math import comb, factorial


def polynomial(coefficients: list[Fraction], x: Fraction) -> Fraction:
    return sum((coefficient * x ** (2 * degree) for degree, coefficient in enumerate(coefficients)), Fraction())


def main() -> None:
    coefficients = [
        Fraction(1),
        -Fraction(837, 10_000) / 2,
        Fraction(199, 10_000) / factorial(4),
        -Fraction(403, 50_000) / factorial(6),
        Fraction(429, 100_000) / factorial(8),
        -Fraction(1497, 500_000) / factorial(10),
    ]
    derivative = [(degree + 1) * coefficients[degree + 1] for degree in range(5)]
    power_on_unit_interval = [coefficient * 51**degree for degree, coefficient in enumerate(derivative)]
    bernstein = [
        sum(
            (power_on_unit_interval[k] * Fraction(comb(j, k), comb(4, k)) for k in range(j + 1)),
            Fraction(),
        )
        for j in range(5)
    ]
    assert all(value < 0 for value in bernstein)
    shifted = [
        sum(
            (derivative[original] * comb(original, degree) * 51 ** (original - degree)
             for original in range(degree, 5)),
            Fraction(),
        )
        for degree in range(5)
    ]
    assert all(value < 0 for value in shifted)
    lower = Fraction(70_165_148, 10_000_000)
    upper = Fraction(70_165_149, 10_000_000)
    at_seven = polynomial(coefficients, Fraction(7))
    assert at_seven == Fraction(299_909_357, 86_400_000_000) > 0
    assert polynomial(coefficients, lower) > 0
    assert polynomial(coefficients, upper) < 0
    print("certified: q'(t)<0 for t>=0; unique positive root in", lower, upper)
    print("P_*(7) =", at_seven)


if __name__ == "__main__":
    main()
