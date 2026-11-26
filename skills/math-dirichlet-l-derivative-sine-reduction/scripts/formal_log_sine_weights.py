#!/usr/bin/env python3
"""Emit exact formal log-sine weights for the source's equations (6) and (15).

The input is JSON with an integer q>1 and a mapping values_on_units from every
reduced residue a modulo q (written as a decimal string) to [numerator,
denominator].  Values must be even: f(a)=f(q-a).  This is a coefficient
transform only; it neither evaluates logarithms nor decides a linear relation.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import gcd
from pathlib import Path


def parse_fraction(value: object) -> Fraction:
    if not isinstance(value, list) or len(value) != 2 or not all(type(x) is int for x in value):
        raise ValueError("each value must be an integer [numerator, denominator] pair")
    if value[1] == 0:
        raise ValueError("a value denominator cannot be zero")
    return Fraction(value[0], value[1])


def pair(value: Fraction) -> list[int]:
    return [value.numerator, value.denominator]


def is_prime_power(q: int) -> bool:
    remaining = q
    prime_count = 0
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            prime_count += 1
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1 if divisor == 2 else 2
    if remaining > 1:
        prime_count += 1
    return prime_count == 1


def read_values(q: int, raw: object) -> dict[int, Fraction]:
    if not isinstance(raw, dict):
        raise ValueError("values_on_units must be an object")
    units = {a for a in range(1, q) if gcd(a, q) == 1}
    keys = {str(a) for a in units}
    if set(raw) != keys:
        missing = sorted(keys - raw.keys())
        extra = sorted(raw.keys() - keys)
        raise ValueError(f"values_on_units must cover exactly the reduced residues; missing={missing}, extra={extra}")
    values = {a: parse_fraction(raw[str(a)]) for a in units}
    for a in units:
        if values[a] != values[(q - a) % q]:
            raise ValueError(f"evenness fails at residues {a} and {(q - a) % q}")
    return values


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="JSON input with q and values_on_units")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.input).read_text())
        q = data["q"]
        if type(q) is not int or q <= 1:
            raise ValueError("q must be an integer greater than one")
        values = read_values(q, data["values_on_units"])
    except (OSError, KeyError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))

    half_units = [a for a in range(1, q // 2 + 1) if gcd(a, q) == 1]
    equation_6 = []
    for a in half_units:
        if values[a] == 0:
            continue
        multiplicity = 1 if 2 * a == q else 2
        equation_6.append([a, pair(-multiplicity * values[a] / 2)])
    output: dict[str, object] = {
        "q": q,
        "half_reduced_residues": half_units,
        "equation_6_log_sine_weights": equation_6,
        "scope": "exact formal coefficient transform only; no logarithm evaluation, nonvanishing, or transcendence claim",
    }
    if q == 2:
        output["equation_6_note"] = "singleton residue, using (1-2**(-s))*zeta(s)"
    if not is_prime_power(q):
        equation_15 = [[a, pair(values[a] - values[1])] for a in half_units if a >= 2 and values[a] != values[1]]
        output["equation_15_normalized_log_sine_weights"] = equation_15
    else:
        output["equation_15_normalized_log_sine_weights"] = None
        output["equation_15_note"] = "not emitted: this source reduction is for moduli with at least two distinct prime factors"
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
