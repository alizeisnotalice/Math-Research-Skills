#!/usr/bin/env python3
"""Construct and verify a rational formal Böttcher conjugacy at infinity."""

import argparse
from fractions import Fraction
import json
from pathlib import Path


def multiply(left, right, order):
    result = [Fraction(0)] * (order + 1)
    for i, a in enumerate(left[:order + 1]):
        if a:
            for j, b in enumerate(right[:order + 1 - i]):
                result[i + j] += a * b
    return result


def substitution(unit, lower, order):
    # z^d f(z^-1 u(z)), evaluated by truncated Horner multiplication.
    result = [Fraction(1)]
    for power, coefficient in enumerate(reversed(lower), 1):
        result = multiply(result, unit, order)
        if power <= order:
            result[power] += coefficient
    return result


def divided_argument_coefficient(unit, exponent, degree):
    index, remainder = divmod(exponent, degree)
    return unit[index] if remainder == 0 else Fraction(0)


def check(data):
    lower, order = data["lower"], data["order"]
    if not isinstance(lower, list) or len(lower) < 2:
        raise ValueError("lower must list at least two coefficients of the monic polynomial")
    if any(type(value) not in (str, int) for value in lower):
        raise ValueError("coefficients must be integers or rational strings")
    if type(order) is not int or order < 0:
        raise ValueError("order must be a nonnegative integer")
    coefficients = [Fraction(value) for value in lower]
    degree = len(coefficients)
    unit = [Fraction(1)]
    for exponent in range(1, order + 2):
        left = divided_argument_coefficient(unit, exponent, degree)
        right = substitution(unit, coefficients, exponent)[exponent]
        unit.append((left - right) / degree)

    right_prefix = substitution(unit, coefficients, order + 1)
    bad = [exponent - degree for exponent, value in enumerate(right_prefix)
           if value != divided_argument_coefficient(unit, exponent, degree)]
    return {
        "degree": degree, "order": order, "coefficients": [str(value) for value in unit[1:]],
        "checked_exponents": list(range(-degree, order - degree + 2)),
        "defect_zero": not bad, "bad": bad,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("example", type=Path)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.example.read_text(encoding="utf-8")))
    except (KeyError, TypeError, ValueError, ZeroDivisionError, OSError) as error:
        parser.error(str(error))
    print(json.dumps(result, sort_keys=True))
    return 0 if result["defect_zero"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
