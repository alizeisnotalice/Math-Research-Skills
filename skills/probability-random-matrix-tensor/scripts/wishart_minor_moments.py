#!/usr/bin/env python3
"""Compute exact polynomial principal-minor moments of a central Wishart law."""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import cache
from itertools import permutations
import json
from pathlib import Path


Entry = tuple[int, int]
Monomial = tuple[Entry, ...]
Polynomial = dict[Monomial, int]


def rational(value: object) -> Fraction:
    if type(value) is int or isinstance(value, str):
        return Fraction(value)
    raise ValueError("exact rational input requires an integer or a string")


def parse_covariance(raw: object) -> list[list[Fraction]]:
    if not isinstance(raw, list) or not raw or any(
        not isinstance(row, list) or len(row) != len(raw) for row in raw
    ):
        raise ValueError("covariance must be a nonempty square matrix")
    sigma = [[rational(entry) for entry in row] for row in raw]
    n = len(sigma)
    if any(sigma[i][j] != sigma[j][i] for i in range(n) for j in range(i)):
        raise ValueError("covariance must be symmetric")
    remainder = [row[:] for row in sigma]
    for i in range(n):
        pivot = remainder[i][i]
        if pivot <= 0:
            raise ValueError("covariance must be positive definite")
        for j in range(i + 1, n):
            for k in range(i + 1, n):
                remainder[j][k] -= remainder[j][i] * remainder[i][k] / pivot
    return sigma


def entry(i: int, j: int) -> Entry:
    return (i, j) if i <= j else (j, i)


def determinant_polynomial(block: list[int]) -> Polynomial:
    coefficients: Counter[Monomial] = Counter()
    for perm in permutations(range(len(block))):
        inversions = sum(x > y for i, x in enumerate(perm) for y in perm[i + 1:])
        variables = tuple(sorted(entry(row, block[column]) for row, column in zip(block, perm, strict=True)))
        coefficients[variables] += (-1) ** inversions
    return {variables: coefficient for variables, coefficient in coefficients.items() if coefficient}


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    coefficients: Counter[Monomial] = Counter()
    for left_term, a in left.items():
        for right_term, b in right.items():
            coefficients[tuple(sorted(left_term + right_term))] += a * b
    return {variables: coefficient for variables, coefficient in coefficients.items() if coefficient}


def compute(payload: object) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    sigma = parse_covariance(payload.get("covariance"))
    alpha = rational(payload.get("degrees_of_freedom"))
    if alpha < 0 or (alpha.denominator != 1 and alpha <= len(sigma) - 1):
        raise ValueError("degrees_of_freedom must be a nonnegative integer or exceed dimension minus one")
    factors = payload.get("factors")
    if not isinstance(factors, list) or not factors:
        raise ValueError("factors must be a nonempty list of index-block/power objects")
    polynomial: Polynomial = {(): 1}
    degree = 0
    singular_block = False
    for factor in factors:
        if not isinstance(factor, dict):
            raise ValueError("every factor must be an object")
        block, power = factor.get("indices"), factor.get("power")
        if (not isinstance(block, list) or not block or
            any(type(i) is not int or not 0 <= i < len(sigma) for i in block) or len(set(block)) != len(block)):
            raise ValueError("indices must be distinct zero-based covariance coordinates")
        if type(power) is not int or power < 0:
            raise ValueError("every determinant power must be a nonnegative integer")
        singular_block |= power > 0 and alpha.denominator == 1 and len(block) > alpha
        degree += power * len(block)
    if singular_block:
        return {"status": "exact_moment", "value": "0", "polynomial_degree": degree,
                "reason": "a nontrivial determinant factor exceeds the Gaussian sample rank"}
    for factor in factors:
        if not factor["power"]:
            continue
        minor = determinant_polynomial(factor["indices"])
        for _ in range(factor["power"]):
            polynomial = multiply(polynomial, minor)

    @cache
    def moment(variables: Monomial) -> Fraction:
        if not variables:
            return Fraction(1)
        (i, j), *tail_entries = variables
        tail = tuple(tail_entries)
        value = alpha * sigma[i][j] * moment(tail)
        for index, (a, b) in enumerate(tail):
            remaining = tail[:index] + tail[index + 1:]
            if sigma[i][a]:
                value += sigma[i][a] * moment(tuple(sorted(remaining + (entry(j, b),))))
            if sigma[i][b]:
                value += sigma[i][b] * moment(tuple(sorted(remaining + (entry(j, a),))))
        return value

    value = sum((coefficient * moment(term) for term, coefficient in polynomial.items()), Fraction(0))
    return {"status": "exact_moment", "value": str(value), "polynomial_degree": degree,
            "monomial_count": len(polynomial), "cached_entry_moments": moment.cache_info().currsize}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = compute(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
