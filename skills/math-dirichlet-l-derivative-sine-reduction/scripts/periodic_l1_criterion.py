#!/usr/bin/env python3
"""Evaluate the finite rational data in Chatterjee--Murty Theorem 3."""

from __future__ import annotations

from fractions import Fraction
from math import gcd
import json
from pathlib import Path
import sys


def fraction(value: str | int) -> Fraction:
    return Fraction(str(value))


def prime_divisors(value: int) -> list[int]:
    factors: list[int] = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1 if divisor == 2 else 2
    if value > 1:
        factors.append(value)
    return factors


def multiply_by_prime(values: list[Fraction], modulus: int, prime: int) -> list[Fraction]:
    return [values[(residue * prime) % modulus] for residue in range(modulus)]


def solve_geometric_resolvent(values: list[Fraction], modulus: int, prime: int) -> list[Fraction]:
    """Solve y(a)-y(ap)/p=values(a) exactly on Z/modulus Z."""
    matrix = [[Fraction(int(row == column)) for column in range(modulus)] + [values[row]]
              for row in range(modulus)]
    for row in range(modulus):
        matrix[row][(row * prime) % modulus] -= Fraction(1, prime)
    for pivot_column in range(modulus):
        pivot = next(row for row in range(pivot_column, modulus) if matrix[row][pivot_column])
        matrix[pivot_column], matrix[pivot] = matrix[pivot], matrix[pivot_column]
        divisor = matrix[pivot_column][pivot_column]
        matrix[pivot_column] = [entry / divisor for entry in matrix[pivot_column]]
        for row in range(modulus):
            if row == pivot_column:
                continue
            coefficient = matrix[row][pivot_column]
            if coefficient:
                matrix[row] = [left - coefficient * right
                               for left, right in zip(matrix[row], matrix[pivot_column])]
    return [matrix[row][-1] for row in range(modulus)]


def encode(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def check(data: dict) -> dict:
    modulus = data["period"]
    if not isinstance(modulus, int) or modulus < 2:
        raise ValueError("period must be an integer at least 2")
    values = [fraction(value) for value in data["values"]]
    if len(values) != modulus:
        raise ValueError("values must give f(0),...,f(q-1)")
    primes = prime_divisors(modulus)
    all_resolvents = values
    for prime in primes:
        all_resolvents = solve_geometric_resolvent(all_resolvents, modulus, prime)
    units = [residue for residue in range(modulus) if gcd(residue, modulus) == 1]
    unit_conditions = {str(residue): all_resolvents[residue] for residue in units}
    logarithm_coefficients: dict[str, Fraction] = {}
    for prime in primes:
        shifted = [value / prime for value in multiply_by_prime(all_resolvents, modulus, prime)]
        derivative_term = solve_geometric_resolvent(shifted, modulus, prime)
        logarithm_coefficients[str(prime)] = sum((derivative_term[residue] for residue in units), Fraction()) / len(units)
    zero_average = sum(values, Fraction()) == 0
    theorem_conditions = zero_average and not any(unit_conditions.values()) and not any(logarithm_coefficients.values())
    return {
        "period": modulus,
        "prime_divisors": primes,
        "zero_average": zero_average,
        "unit_monoid_sums": {key: encode(value) for key, value in unit_conditions.items()},
        "log_prime_coefficients": {key: encode(value) for key, value in logarithm_coefficients.items()},
        "theorem_3_zero_conditions_satisfied": theorem_conditions,
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: periodic_l1_criterion.py INPUT.json")
    try:
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), ensure_ascii=False, indent=2))
    except (ValueError, KeyError, ZeroDivisionError) as error:
        print(json.dumps({"error": str(error)}))
        raise SystemExit(2)
