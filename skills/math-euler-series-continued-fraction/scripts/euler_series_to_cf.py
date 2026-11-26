#!/usr/bin/env python3
"""Transform finite rational series data into Euler generalized-CF data exactly.

For a_0+...+a_N, this implements the finite identity behind equation
(3.2) of McLaughlin--Wyshinski. It is a finite algebraic transformer;
convergence of an infinite input series must be supplied separately.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def pair(x: Fraction) -> list[int]:
    return [x.numerator, x.denominator]


def parse_pair(x: object) -> Fraction:
    if not isinstance(x, list) or len(x) != 2 or not all(isinstance(y, int) for y in x):
        raise ValueError("every term must be a [numerator, denominator] integer pair")
    if x[1] == 0:
        raise ValueError("term denominator cannot be zero")
    return Fraction(x[0], x[1])


def euler_cf(terms: list[Fraction]) -> tuple[list[Fraction], list[Fraction]]:
    """Return generalized-CF numerator and denominator arrays, including b_0.

    The resulting value is b_0 + K_{i=1}^N A_i/B_i, where
    A_1=a_1, B_1=1, A_2=-a_2, and
    A_i=-a_{i-2}a_i, B_i=a_{i-1}+a_i for i>=3.
    Equation (3.2) requires nonzero successive series increments and its
    displayed denominators; reject inputs where this finite form degenerates.
    """
    if not terms:
        raise ValueError("at least a_0 is required")
    if len(terms) == 1:
        return [], [terms[0]]
    if any(x == 0 for x in terms[1:]):
        raise ValueError("Euler form requires each increment a_i (i>=1) nonzero")
    numerators = [terms[1]]
    denominators = [terms[0], Fraction(1)]
    if len(terms) >= 3:
        denominator = terms[1] + terms[2]
        if denominator == 0:
            raise ValueError("Euler denominator a_1+a_2 is zero")
        numerators.append(-terms[2])
        denominators.append(denominator)
    for i in range(3, len(terms)):
        denominator = terms[i - 1] + terms[i]
        if denominator == 0:
            raise ValueError(f"Euler denominator a_{i-1}+a_{i} is zero")
        numerators.append(-terms[i - 2] * terms[i])
        denominators.append(denominator)
    return numerators, denominators


def cf_value(numerators: list[Fraction], denominators: list[Fraction]) -> Fraction:
    """Evaluate b_0 + K A_i/B_i by exact canonical continuant recurrence."""
    if len(denominators) != len(numerators) + 1:
        raise ValueError("need b_0,...,b_N for A_1,...,A_N")
    p_prev2, p_prev1 = Fraction(1), denominators[0]
    q_prev2, q_prev1 = Fraction(0), Fraction(1)
    for a, b in zip(numerators, denominators[1:]):
        p_prev2, p_prev1 = p_prev1, b * p_prev1 + a * p_prev2
        q_prev2, q_prev1 = q_prev1, b * q_prev1 + a * q_prev2
    if q_prev1 == 0:
        raise ValueError("finite continued fraction has zero canonical denominator")
    return p_prev1 / q_prev1


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSON object containing a 'terms' list of [p,q] pairs")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text())
        values = [parse_pair(x) for x in data["terms"]]
        a, b = euler_cf(values)
        value = cf_value(a, b)
    except (OSError, KeyError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps({
        "status": "EXACT_FINITE_IDENTITY",
        "input_terms": [pair(x) for x in values],
        "series_partial_sum": pair(sum(values, Fraction())),
        "cf_numerators_A1_to_AN": [pair(x) for x in a],
        "cf_denominators_b0_to_bN": [pair(x) for x in b],
        "continued_fraction_value": pair(value),
        "scope": "finite Euler series-to-CF identity only; no convergence or irrationality claim",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
