#!/usr/bin/env python3
"""Exact-rational Brent–McMillan B3 enclosure for integer n >= 138."""

import argparse
import runpy
from fractions import Fraction
from math import ceil, floor
from pathlib import Path


def integer_log(n: int, tolerance: Fraction) -> tuple[Fraction, Fraction]:
    # For each log argument, z <= 1/3 gives tail <= (3/4) * 9**(-terms).
    tail = Fraction(3, 4) * n.bit_length()
    terms = 1
    tail /= 9
    while tail > tolerance:
        tail /= 9
        terms += 1
    certificate_script = (
        Path(__file__).resolve().parents[2] / "math-sondow-log-fractional-certificate"
        / "scripts" / "sondow_certificate.py"
    )
    helpers = runpy.run_path(str(certificate_script))
    log_two = helpers["log_unit_bounds"](Fraction(2), terms)
    return helpers["integer_log_bounds"](n, terms, log_two)


def b3_rational_part(n: int) -> Fraction:
    weight = Fraction(1)
    harmonic = Fraction(0)
    i_sum = Fraction(1)
    s_sum = Fraction(0)
    for k in range(1, 5 * n):
        weight *= Fraction(n * n, k * k)
        harmonic += Fraction(1, k)
        i_sum += weight
        s_sum += harmonic * weight

    product_term = product_sum = Fraction(1)
    for k in range(1, 2 * n):
        product_term *= Fraction((2 * k - 1) ** 3, 32 * k * n * n)
        product_sum += product_term
    product_sum /= 4 * n
    return s_sum / i_sum - product_sum / i_sum**2


def gamma_interval(n: int) -> tuple[Fraction, Fraction]:
    if n < 138:
        raise ValueError("the stated Brent–Johansson corollary requires n >= 138")

    # e > 8/3 implies 24 exp(-8n) < radius.
    radius = 24 * Fraction(3, 8) ** (8 * n)
    log_lower, log_upper = integer_log(n, radius)
    rational_part = b3_rational_part(n)
    return rational_part - log_upper - radius, rational_part - log_lower + radius


def least_denominator_in_interval(lower: Fraction, upper: Fraction) -> Fraction:
    """Return a fraction of least positive denominator in a closed interval."""
    if lower > upper:
        raise ValueError("interval endpoints are reversed")
    integer = ceil(lower)
    if integer <= upper:
        return Fraction(integer)

    a, b = floor(lower), 1
    c, d = a + 1, 1
    low_p, low_q = lower.numerator, lower.denominator
    high_p, high_q = upper.numerator, upper.denominator
    while True:
        mediant = Fraction(a + c, b + d)
        if mediant < lower:
            steps = (low_p * b - low_q * a - 1) // (low_q * c - low_p * d)
            a, b = a + steps * c, b + steps * d
        elif mediant > upper:
            steps = (high_q * c - high_p * d - 1) // (high_p * b - high_q * a)
            c, d = c + steps * a, d + steps * b
        else:
            return mediant


def decimal_string(scaled: int, places: int) -> str:
    whole, fractional = divmod(abs(scaled), 10**places)
    sign = "-" if scaled < 0 else ""
    return f"{sign}{whole}.{fractional:0{places}d}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=138)
    parser.add_argument("--places", type=int, default=50)
    parser.add_argument("--exclude-denominators", action="store_true")
    args = parser.parse_args()
    if args.n < 138 or args.places < 1:
        parser.error("require n >= 138 and at least one decimal place")

    lower, upper = gamma_interval(args.n)
    scale = 10**args.places
    lower_scaled = floor(lower * scale)
    upper_scaled = ceil(upper * scale)
    print(f"n={args.n}, N={5 * args.n}, product terms={2 * args.n}")
    print("lower:", decimal_string(lower_scaled, args.places))
    print("upper:", decimal_string(upper_scaled, args.places))
    if lower_scaled == floor(upper * scale):
        print(f"Common truncation certified to {args.places} decimal places.")
    if args.exclude_denominators:
        simplest = least_denominator_in_interval(lower, upper)
        print(f"Any rational in the enclosure has denominator >= {simplest.denominator}.")


if __name__ == "__main__":
    main()
