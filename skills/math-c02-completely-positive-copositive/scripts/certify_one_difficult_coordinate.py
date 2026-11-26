#!/usr/bin/env python3
"""Exact finite enumeration certificate for a quadratic form with one difficult coordinate."""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import product
import json
from math import isqrt
from pathlib import Path
from typing import Any


def fraction(value: Any, label: str) -> Fraction:
    if isinstance(value, bool):
        raise ValueError(f"{label} must be a rational number")
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"{label} must be a rational number") from error


def vector(values: Any, label: str) -> list[Fraction]:
    if not isinstance(values, list):
        raise ValueError(f"{label} must be a list")
    return [fraction(value, f"{label}[{index}]") for index, value in enumerate(values)]


def matrix(values: Any) -> list[list[Fraction]]:
    if not isinstance(values, list) or not values:
        raise ValueError("Q must be a nonempty square matrix")
    output = [vector(row, f"Q[{index}]") for index, row in enumerate(values)]
    if any(len(row) != len(output) for row in output):
        raise ValueError("Q must be square")
    if any(output[i][j] != output[j][i] for i in range(len(output)) for j in range(len(output))):
        raise ValueError("Q must be symmetric")
    return output


def determinant(value: list[list[Fraction]]) -> Fraction:
    rows = [row[:] for row in value]
    product_diagonal = Fraction(1)
    sign = 1
    for column in range(len(rows)):
        pivot = next((index for index in range(column, len(rows)) if rows[index][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            rows[column], rows[pivot] = rows[pivot], rows[column]
            sign *= -1
        pivot_value = rows[column][column]
        product_diagonal *= pivot_value
        for index in range(column + 1, len(rows)):
            factor = rows[index][column] / pivot_value
            for entry in range(column, len(rows)):
                rows[index][entry] -= factor * rows[column][entry]
    return sign * product_diagonal


def positive_definite(value: list[list[Fraction]]) -> bool:
    return all(determinant([row[:size] for row in value[:size]]) > 0 for size in range(1, len(value) + 1))


def dot(left: list[Fraction], right: list[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(left, right, strict=True)), Fraction(0))


def quadratic(q: list[list[Fraction]], x: list[Fraction]) -> Fraction:
    return sum((x[i] * q[i][j] * x[j] for i in range(len(q)) for j in range(len(q))), Fraction(0))


def solve_linear(a: list[list[Fraction]], b: list[Fraction]) -> list[Fraction]:
    n = len(a)
    augmented = [row[:] + [b[index]] for index, row in enumerate(a)]
    for column in range(n):
        pivot = next((index for index in range(column, n) if augmented[index][column]), None)
        if pivot is None:
            raise ValueError("leading block is singular")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        scalar = augmented[column][column]
        augmented[column] = [entry / scalar for entry in augmented[column]]
        for index in range(n):
            if index == column:
                continue
            scalar = augmented[index][column]
            augmented[index] = [entry - scalar * pivot_entry for entry, pivot_entry in zip(augmented[index], augmented[column], strict=True)]
    return [row[-1] for row in augmented]


def floor_sqrt(value: Fraction) -> int:
    if value < 0:
        raise ValueError("square-root argument must be nonnegative")
    numerator = isqrt(value.numerator)
    denominator = isqrt(value.denominator)
    estimate = numerator // max(denominator, 1)
    while Fraction((estimate + 1) ** 2) <= value:
        estimate += 1
    while Fraction(estimate**2) > value:
        estimate -= 1
    return estimate


def ceil_sqrt(value: Fraction) -> int:
    estimate = floor_sqrt(value)
    return estimate if Fraction(estimate * estimate) == value else estimate + 1


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def floor_fraction(value: Fraction) -> int:
    return value.numerator // value.denominator


def certify(payload: object) -> dict[str, object]:
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")
    q = matrix(payload.get("Q"))
    if len(q) < 2:
        raise ValueError("Q must have at least two coordinates")
    bound = fraction(payload.get("lambda"), "lambda")
    if bound < 0:
        raise ValueError("lambda must be nonnegative")
    certificate = vector(payload.get("leading_minimizer"), "leading_minimizer")
    n = len(q)
    if len(certificate) != n - 1 or any(value < 0 for value in certificate):
        raise ValueError("leading_minimizer must be a nonnegative vector of length n-1")
    lower = fraction(payload.get("spectral_lower_bound"), "spectral_lower_bound")
    if lower <= 0:
        raise ValueError("spectral_lower_bound must be positive")
    leading = [row[:-1] for row in q[:-1]]
    shifted = [[leading[i][j] - (lower if i == j else 0) for j in range(n - 1)] for i in range(n - 1)]
    if not positive_definite(leading) or not positive_definite(shifted):
        raise ValueError("leading block and leading block minus spectral_lower_bound times I must be positive definite")
    cross = [row[-1] for row in q[:-1]]
    gradient = [2 * (dot(row, certificate) + cross[index]) for index, row in enumerate(leading)]
    if any(value < 0 for value in gradient) or any(certificate[index] * gradient[index] != 0 for index in range(n - 1)):
        raise ValueError("leading_minimizer must satisfy exact nonnegative quadratic KKT conditions")
    f_one = quadratic(q, [*certificate, Fraction(1)])
    if f_one <= 0:
        raise ValueError("the certified slice minimum f(1) must be positive")
    h = solve_linear(leading, cross)
    schur_value = q[-1][-1] - dot(cross, h)
    maximum_last = floor_sqrt(bound / f_one)
    maximum_count = int(payload.get("max_enumeration", 100000))
    if maximum_count < 1:
        raise ValueError("max_enumeration must be positive")
    candidates: list[list[int]] = []
    tested = 0
    for last in range(maximum_last + 1):
        residual = bound - schur_value * last * last
        radius = ceil_sqrt(residual / lower)
        intervals = []
        for coordinate in range(n - 1):
            center = -last * h[coordinate]
            intervals.append(range(max(0, ceil_fraction(center - radius)), floor_fraction(center + radius) + 1))
        for initial in product(*intervals):
            tested += 1
            if tested > maximum_count:
                raise ValueError("the certified box exceeds max_enumeration")
            point = [*initial, last]
            value = quadratic(q, [Fraction(entry) for entry in point])
            if value <= bound:
                candidates.append(point)
    candidates.sort()
    nonzero = [point for point in candidates if any(point)]
    values = [(quadratic(q, [Fraction(entry) for entry in point]), point) for point in nonzero]
    minimum = min(values) if values else None
    return {
        "status": "certified-one-difficult-coordinate-enumeration",
        "leading_block_positive_definite": True,
        "spectral_lower_bound": str(lower),
        "slice_minimum_f_one": str(f_one),
        "unconstrained_schur_value": str(schur_value),
        "last_coordinate_upper_bound": maximum_last,
        "tested_lattice_points": tested,
        "points_with_quadratic_at_most_lambda": candidates,
        "nonzero_minimum": None if minimum is None else {"value": str(minimum[0]), "point": minimum[1]},
        "scope": "Exact enumeration for supplied rational Q, lambda, KKT minimizer and spectral lower-bound certificate. It does not decide copositivity, construct an SPN decomposition, or bound a general multi-difficult-coordinate instance.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = certify(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
