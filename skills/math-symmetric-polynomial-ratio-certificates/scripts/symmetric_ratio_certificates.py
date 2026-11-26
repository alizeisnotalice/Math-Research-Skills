#!/usr/bin/env python3
"""Exact finite evaluations for two symmetric-polynomial ratios."""

from __future__ import annotations

from fractions import Fraction
import json
from pathlib import Path
import sys


def rational(value: str | int) -> Fraction:
    if type(value) not in (int, str):
        raise ValueError("use integers or exact rational strings for evaluation points")
    return Fraction(value)


def integer(value: object, name: str) -> int:
    if type(value) is not int:
        raise ValueError(f"{name} must be an integer")
    return value


def complete(values: list[Fraction], degree: int) -> Fraction:
    if degree < 0:
        return Fraction()
    coefficients = [Fraction(1)] + [Fraction() for _ in range(degree)]
    for value in values:
        next_coefficients = []
        for index in range(degree + 1):
            next_coefficients.append(sum(
                coefficients[index - power] * value**power
                for power in range(index + 1)
            ))
        coefficients = next_coefficients
    return coefficients[degree]


def determinant(matrix: list[list[Fraction]]) -> Fraction:
    size = len(matrix)
    result = Fraction(1)
    for column in range(size):
        pivot = next((row for row in range(column, size) if matrix[row][column]), None)
        if pivot is None:
            return Fraction()
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            result = -result
        pivot_value = matrix[column][column]
        result *= pivot_value
        for row in range(column + 1, size):
            if not matrix[row][column]:
                continue
            multiplier = matrix[row][column] / pivot_value
            for entry in range(column + 1, size):
                matrix[row][entry] -= multiplier * matrix[column][entry]
    return result


def schur(partition: list[int], values: list[Fraction]) -> Fraction:
    width = len(values)
    padded = partition + [0] * (width - len(partition))
    if len(partition) > width or any(item < 0 for item in partition):
        raise ValueError("partition must have at most len(values) nonnegative parts")
    return determinant([
        [complete(values, padded[row] - row + column) for column in range(width)]
        for row in range(width)
    ])


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def mcleod_power(data: dict) -> dict:
    ell = integer(data["ell"], "ell")
    power = integer(data["r"], "r")
    values = [rational(value) for value in data["x"]]
    if ell < 0 or power < 1 or not values or any(value < 0 for value in values):
        raise ValueError("ell >= 0, r >= 1 and a nonempty nonnegative vector are required")
    denominator = complete(values, ell)
    if not denominator:
        raise ValueError("h_ell(x) is zero")
    ratio = complete(values, ell + power) / denominator
    return {"kind": "mcleod_power", "ell": ell, "r": power,
            "h_ell": text(denominator), "G_power": text(ratio)}


def turan_pair(data: dict) -> dict:
    partition = [integer(value, "lambda part") for value in data["lambda"]]
    count = integer(data["n"], "n")
    index = integer(data["i"], "i")
    left, right = rational(data["x_left"]), rational(data["x_right"])
    if count < 2 or not 1 <= index < count or not (1 < left < right):
        raise ValueError("need n >= 2, 1 <= i < n and 1 < x_left < x_right")
    padded = partition + [0] * (count - len(partition))
    if len(partition) > count or padded != sorted(padded, reverse=True) or padded[0] == padded[-1]:
        raise ValueError("lambda must be a nonconstant partition padded to n parts")

    def ratio(value: Fraction) -> Fraction:
        def specialized(multiplicity: int) -> Fraction:
            return schur(partition, [Fraction(1)] * (count - multiplicity) + [value] * multiplicity)
        numerator = specialized(index)
        return numerator * numerator / (specialized(index - 1) * specialized(index + 1))

    lower, upper = ratio(left), ratio(right)
    return {"kind": "turan_pair", "lambda": partition, "n": count, "i": index,
            "x_left": text(left), "x_right": text(right),
            "T_left": text(lower), "T_right": text(upper), "strictly_increases_on_this_pair": lower < upper}


def evaluate(data: dict) -> dict:
    kind = data.get("kind")
    if kind == "mcleod_power":
        return mcleod_power(data)
    if kind == "turan_pair":
        return turan_pair(data)
    raise ValueError("kind must be mcleod_power or turan_pair")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: symmetric_ratio_certificates.py INPUT.json")
    try:
        output = evaluate(json.loads(Path(sys.argv[1]).read_text()))
    except (OSError, KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        raise SystemExit(str(error)) from error
    print(json.dumps(output, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
