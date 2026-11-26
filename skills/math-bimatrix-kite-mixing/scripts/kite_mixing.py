#!/usr/bin/env python3
"""Exact Lemma-2.3(a) kite mixing for rational bimatrix games.

This validates the local conversion only.  It does not implement or validate the
paper's global MaximinKiteNE algorithm or its claimed 1/5 guarantee.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path
from typing import Any


def rational(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("Boolean values are not rational data")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"expected integer or p/q string, got {value!r}")


def vector(values: Any, dimension: int, label: str) -> list[Fraction]:
    if not isinstance(values, list) or len(values) != dimension:
        raise ValueError(f"{label} must have length {dimension}")
    result = [rational(v) for v in values]
    if any(v < 0 for v in result) or sum(result, Fraction()) != 1:
        raise ValueError(f"{label} must be a probability vector")
    return result


def matrix(values: Any, label: str) -> list[list[Fraction]]:
    if not isinstance(values, list) or not values or not all(isinstance(row, list) and row for row in values):
        raise ValueError(f"{label} must be a nonempty matrix")
    width = len(values[0])
    if any(len(row) != width for row in values):
        raise ValueError(f"{label} has inconsistent row widths")
    result = [[rational(item) for item in row] for row in values]
    if any(item < 0 or item > 1 for row in result for item in row):
        raise ValueError(f"{label} entries must lie in [0, 1]")
    return result


def payoff_left(row: list[Fraction], other: list[Fraction]) -> Fraction:
    return sum((a * b for a, b in zip(row, other)), Fraction())


def regrets(R: list[list[Fraction]], C: list[list[Fraction]], x: list[Fraction], y: list[Fraction]) -> tuple[Fraction, Fraction, int, int]:
    row_payoffs = [payoff_left(row, y) for row in R]
    column_payoffs = [sum((x[i] * C[i][j] for i in range(len(x))), Fraction()) for j in range(len(y))]
    row_total = sum((x[i] * row_payoffs[i] for i in range(len(x))), Fraction())
    column_total = sum((y[j] * column_payoffs[j] for j in range(len(y))), Fraction())
    best_row = max(range(len(x)), key=lambda i: (row_payoffs[i], -i))
    best_column = max(range(len(y)), key=lambda j: (column_payoffs[j], -j))
    return row_payoffs[best_row] - row_total, column_payoffs[best_column] - column_total, best_row, best_column


def in_kite(r1: Fraction, r2: Fraction, s: Fraction) -> bool:
    return (1 - s) * r1 + s * r2 <= s and s * r1 + (1 - s) * r2 <= s


def transform(R: list[list[Fraction]], C: list[list[Fraction]], x: list[Fraction], y: list[Fraction], s: Fraction) -> dict[str, Any]:
    if not 0 < s < Fraction(1, 2):
        raise ValueError("s must satisfy 0 < s < 1/2")
    r1, r2, best_row, best_column = regrets(R, C, x, y)
    result: dict[str, Any] = {"input_regrets": [str(r1), str(r2)], "in_kite": in_kite(r1, r2, s)}
    if not result["in_kite"]:
        result["status"] = "not-certified"
        result["reason"] = "The input regret pair is outside K_s."
        return result
    xout, yout = x[:], y[:]
    if r1 > s:
        weight = 1 - s / r1
        xout = [(1 - weight) * entry + (weight if index == best_row else 0) for index, entry in enumerate(x)]
        result["operation"] = {"player": "row", "best_response": best_row, "weight": str(weight)}
    elif r2 > s:
        weight = 1 - s / r2
        yout = [(1 - weight) * entry + (weight if index == best_column else 0) for index, entry in enumerate(y)]
        result["operation"] = {"player": "column", "best_response": best_column, "weight": str(weight)}
    else:
        result["operation"] = {"player": "none"}
    out1, out2, _, _ = regrets(R, C, xout, yout)
    if max(out1, out2) > s:
        raise AssertionError("a kite conversion exceeded s")
    result.update({"status": "certified", "output_x": [str(v) for v in xout], "output_y": [str(v) for v in yout], "output_regrets": [str(out1), str(out2)]})
    return result


def simplex_grid() -> list[list[Fraction]]:
    return [[Fraction(a, 4), Fraction(4 - a, 4)] for a in range(5)]


def self_test() -> None:
    s = Fraction(1, 5)
    checked = 0
    for raw in itertools.product((0, 1), repeat=8):
        R = [[Fraction(raw[0]), Fraction(raw[1])], [Fraction(raw[2]), Fraction(raw[3])]]
        C = [[Fraction(raw[4]), Fraction(raw[5])], [Fraction(raw[6]), Fraction(raw[7])]]
        for x in simplex_grid():
            for y in simplex_grid():
                r1, r2, _, _ = regrets(R, C, x, y)
                outcome = transform(R, C, x, y, s)
                if in_kite(r1, r2, s):
                    assert outcome["status"] == "certified"
                    vector(outcome["output_x"], len(x), "output_x")
                    vector(outcome["output_y"], len(y), "output_y")
                    assert max(Fraction(v) for v in outcome["output_regrets"]) <= s
                    checked += 1
    diagonal = [[Fraction(1), Fraction(0)], [Fraction(0), Fraction(1)]]
    anti_diagonal = [[Fraction(0), Fraction(1)], [Fraction(1), Fraction(0)]]
    boundary = transform(diagonal, anti_diagonal, [Fraction(1), Fraction(0)], [Fraction(1), Fraction(0)], s)
    assert boundary["status"] == "not-certified"
    print(json.dumps({"finite_kite_cases_checked": checked, "outside_kite_status": boundary["status"]}, indent=2))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    if args.input is None:
        parser.error("provide INPUT.json or --self-test")
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise ValueError("input must be a JSON object")
        R, C = matrix(data["R"], "R"), matrix(data["C"], "C")
        if len(R) != len(C) or len(R[0]) != len(C[0]):
            raise ValueError("R and C must have the same shape")
        x, y = vector(data["x"], len(R), "x"), vector(data["y"], len(R[0]), "y")
        result = transform(R, C, x, y, rational(data["s"]))
    except (OSError, ValueError, KeyError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
