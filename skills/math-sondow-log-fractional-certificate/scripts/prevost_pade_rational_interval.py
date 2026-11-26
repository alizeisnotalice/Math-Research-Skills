#!/usr/bin/env python3
"""Exact rational Prévost--Legendre Padé approximants with a finite error bound."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb

from prevost_fractional_gate import family_weights, interval_for_log_form, remainder_upper, text


def harmonic(n: int) -> Fraction:
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction())


def pade_polynomials(n: int) -> tuple[list[Fraction], list[Fraction]]:
    """Return numerator and denominator of the source's [n/n] log(1+t) Padé form."""
    denominator = [Fraction() for _ in range(n + 1)]
    numerator = [Fraction() for _ in range(n + 1)]
    for k in range(n + 1):
        coefficient = Fraction(comb(n, k) * comb(n + k, k))
        denominator[n - k] += coefficient
        for i in range(k):
            numerator[n - k + i + 1] += coefficient * Fraction((-1) ** i, i + 1)
    return numerator, denominator


def evaluate(coefficients: list[Fraction], value: Fraction) -> Fraction:
    result = Fraction()
    for coefficient in reversed(coefficients):
        result = result * value + coefficient
    return result


def pade_at(polynomials: tuple[list[Fraction], list[Fraction]], value: Fraction) -> Fraction:
    numerator, denominator = polynomials
    denom_value = evaluate(denominator, value)
    if denom_value == 0:
        raise ArithmeticError("Padé denominator vanished at requested value")
    return evaluate(numerator, value) / denom_value


def pade_log(n: int, value: Fraction) -> Fraction:
    return pade_at(pade_polynomials(n), value)


def is_power_of_two(number: int) -> bool:
    return number > 0 and number & (number - 1) == 0


def certificate(n: int, m: int, log_terms: int) -> dict[str, object]:
    if n < 1 or not 0 <= m <= n:
        raise ValueError("require n >= 1 and 0 <= m <= n")
    if log_terms < 1:
        raise ValueError("log_terms must be positive")
    base = n - m + 1
    if not is_power_of_two(base):
        raise ValueError("require n-m+1 to be a positive power of two")
    exponent = base.bit_length() - 1
    sign = (-1) ** m
    weights = {argument: sign * coefficient for argument, coefficient in family_weights(n, m).items()}
    polynomials = pade_polynomials(n)
    pade_two = pade_at(polynomials, Fraction(1))
    rationalized_l = exponent * pade_two + sum(
        (coefficient * pade_at(polynomials, Fraction(argument - base, base))
         for argument, coefficient in weights.items()), Fraction(0)
    )
    a = 2 * harmonic(n)
    approximation = a - rationalized_l

    log_lo, log_hi = interval_for_log_form(weights, log_terms)
    j_upper = remainder_upper(n, m)
    j_lo, j_hi = (Fraction(0), j_upper) if m % 2 == 0 else (-j_upper, Fraction(0))
    lo, hi = a - log_hi + j_lo, a - log_lo + j_hi
    return {
        "n": n,
        "m": m,
        "dyadic_base": base,
        "dyadic_exponent": exponent,
        "pade_log_two": text(pade_two),
        "rationalized_L": text(rationalized_l),
        "rational_approximation": text(approximation),
        "approximation_denominator": approximation.denominator,
        "exact_log_difference_L_minus_rationalized_L": [
            text(log_lo - rationalized_l), text(log_hi - rationalized_l)
        ],
        "signed_J_enclosure": [text(j_lo), text(j_hi)],
        "closed_absolute_error_upper": text(max(abs(lo - approximation), abs(hi - approximation))),
        "closed_interval_for_gamma": [text(lo), text(hi)],
        "interval_width": text(hi - lo),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", type=int)
    parser.add_argument("m", type=int)
    parser.add_argument("--log-terms", type=int, default=64)
    arguments = parser.parse_args()
    try:
        print(json.dumps(certificate(arguments.n, arguments.m, arguments.log_terms), indent=2, sort_keys=True))
    except (ArithmeticError, ValueError) as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
