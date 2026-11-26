#!/usr/bin/env python3
"""Exact finite fractional-part gate for Prévost's Legendre–Padé family."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb, factorial, lcm

from sondow_certificate import integer_log_bounds, log_unit_bounds


def family_weights(n: int, m: int) -> dict[int, int]:
    """Coefficients of (-1)^m L_{n,m} grouped by log(integer)."""
    if n < 1 or not 0 <= m <= n:
        raise ValueError("require n >= 1 and 0 <= m <= n")
    signs = -1 if m % 2 else 1
    weights: dict[int, int] = {}
    for k in range(n + 1):
        argument = n - m + k + 1
        coefficient = signs * (-1) ** (n + k) * comb(n, k) * comb(n + k, k)
        weights[argument] = weights.get(argument, 0) + coefficient
    return {argument: coefficient for argument, coefficient in weights.items() if coefficient and argument != 1}


def interval_for_log_form(weights: dict[int, int], terms: int) -> tuple[Fraction, Fraction]:
    log_two = log_unit_bounds(Fraction(2), terms)
    lower = upper = Fraction()
    for argument, coefficient in sorted(weights.items()):
        lo, hi = integer_log_bounds(argument, terms, log_two)
        if coefficient >= 0:
            lower += coefficient * lo
            upper += coefficient * hi
        else:
            lower += coefficient * hi
            upper += coefficient * lo
    return lower, upper


def fractional_interval(lower: Fraction, upper: Fraction) -> tuple[Fraction, Fraction] | None:
    floor = lower.numerator // lower.denominator
    if upper >= floor + 1:
        return None
    return lower - floor, upper - floor


def text(value: Fraction | int | None) -> str | None:
    if value is None:
        return None
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def remainder_upper(n: int, m: int) -> Fraction:
    """Bound the positive signed remainder via the split of 1-(1-u)t."""
    a = n - m
    split_maximum = Fraction(a, n) ** a * Fraction(m, n) ** m
    beta = Fraction(factorial(a) * factorial(n), factorial(a + n + 1))
    return split_maximum * beta


def certificate(n: int, m: int, terms: int) -> dict[str, object]:
    if terms < 1:
        raise ValueError("terms must be positive")
    weights = family_weights(n, m)
    d = 1
    for j in range(1, n + 1):
        d = lcm(d, j)
    scaled_weights = {argument: d * coefficient for argument, coefficient in weights.items()}
    lower, upper = interval_for_log_form(scaled_weights, terms)
    fraction = fractional_interval(lower, upper)
    bound = d * remainder_upper(n, m)
    certified = bound <= 1 and fraction is not None and fraction[0] >= bound
    return {
        "source_relation": "d_n*(-1)^m*L_{n,m}; L_{n,m} is Prévost 2005 Eq. (3.2)",
        "n": n,
        "m": m,
        "terms": terms,
        "d_n": d,
        "log_weights_for_scaled_form": {str(argument): coefficient for argument, coefficient in sorted(scaled_weights.items())},
        "scaled_log_bounds": [text(lower), text(upper)],
        "fractional_bounds": [text(fraction[0]), text(fraction[1])] if fraction else None,
        "strict_scaled_remainder_upper": text(bound),
        "finite_denominator_exclusion_certified": certified,
        "excluded_reduced_denominators_dividing_d_n": d if certified else None,
        "scope": (
            "If certified, the strict rational bound on d_n*(-1)^m*J_{n,m} "
            "contradicts gamma=a/b with b dividing d_n. This is a finite denominator exclusion only; "
            "it does not prove gamma irrational."
        ),
        "unresolved_if_not_certified": (
            "The remainder bound does not ensure a single unit interval, or the fractional interval does not clear the bound; "
            "this is not evidence for rationality."
        ) if not certified else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    parser.add_argument("m", type=int)
    parser.add_argument("--terms", type=int, default=64)
    arguments = parser.parse_args()
    try:
        print(json.dumps(certificate(arguments.n, arguments.m, arguments.terms), ensure_ascii=False, indent=2, sort_keys=True))
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
