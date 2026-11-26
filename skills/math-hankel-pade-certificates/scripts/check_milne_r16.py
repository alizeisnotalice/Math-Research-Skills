#!/usr/bin/env python3
"""Verify Milne's r_16 divisor-convolution formula through a finite cutoff."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction


def divisors(number: int) -> list[int]:
    return [divisor for divisor in range(1, number + 1) if number % divisor == 0]


def tilde_sigma(power: int, number: int) -> int:
    return sum((-1) ** (divisor + number // divisor) * divisor**power
               for divisor in divisors(number))


def milne_r16(number: int) -> int:
    linear = sum(tilde_sigma(power, number) for power in (1, 3, 5))
    convolution = sum(
        tilde_sigma(1, index) * tilde_sigma(5, number - index)
        - tilde_sigma(3, index) * tilde_sigma(3, number - index)
        for index in range(1, number)
    )
    value = (-1) ** number * (Fraction(-32, 3) * linear + Fraction(256, 3) * convolution)
    if value.denominator != 1:
        raise ArithmeticError(f"nonintegral formula value at {number}: {value}")
    return value.numerator


def theta_power_coefficients(cutoff: int) -> list[int]:
    theta = [0] * (cutoff + 1)
    theta[0] = 1
    for integer in range(1, int(cutoff**0.5) + 1):
        theta[integer * integer] = 2
    coefficients = [1] + [0] * cutoff
    for _ in range(16):
        next_coefficients = [0] * (cutoff + 1)
        for degree, coefficient in enumerate(coefficients):
            for shift, theta_coefficient in enumerate(theta[:cutoff - degree + 1]):
                next_coefficients[degree + shift] += coefficient * theta_coefficient
        coefficients = next_coefficients
    return coefficients


def check(cutoff: int) -> dict[str, object]:
    if cutoff < 1:
        raise ValueError("cutoff must be positive")
    coefficients = theta_power_coefficients(cutoff)
    comparisons = [
        {"n": number, "theta_coefficient": coefficients[number], "divisor_formula": milne_r16(number)}
        for number in range(1, cutoff + 1)
    ]
    if any(row["theta_coefficient"] != row["divisor_formula"] for row in comparisons):
        raise ArithmeticError("Milne formula mismatch")
    return {"cutoff": cutoff, "checked_coefficients": comparisons,
            "formula": "Milne (1.26), r_16 only"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cutoff", type=int, default=12)
    arguments = parser.parse_args()
    print(json.dumps(check(arguments.cutoff), ensure_ascii=False))


if __name__ == "__main__":
    main()
