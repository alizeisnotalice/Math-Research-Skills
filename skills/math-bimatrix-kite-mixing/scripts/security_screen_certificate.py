#!/usr/bin/env python3
"""Verify an exact rational zero-sum security-screen certificate.

The input supplies primal and dual feasible strategies for R and C^T.  The
checker does not solve a linear program and does not assert a global
approximate-Nash algorithm.  It verifies the displayed inequalities and the
resulting regret upper bounds for (x_minimax, y_minimax).
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path
from typing import Any


def fraction(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("Boolean values are not rational data")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError(f"expected integer or p/q string, got {value!r}")


def probability_vector(values: Any, size: int, label: str) -> list[Fraction]:
    if not isinstance(values, list) or len(values) != size:
        raise ValueError(f"{label} must have length {size}")
    vector = [fraction(item) for item in values]
    if any(item < 0 for item in vector) or sum(vector, Fraction()) != 1:
        raise ValueError(f"{label} must be a probability vector")
    return vector


def payoff_matrix(values: Any, label: str) -> list[list[Fraction]]:
    if not isinstance(values, list) or not values or not all(isinstance(row, list) and row for row in values):
        raise ValueError(f"{label} must be a nonempty matrix")
    columns = len(values[0])
    if any(len(row) != columns for row in values):
        raise ValueError(f"{label} has inconsistent row widths")
    matrix = [[fraction(item) for item in row] for row in values]
    if any(item < 0 or item > 1 for row in matrix for item in row):
        raise ValueError(f"{label} entries must lie in [0, 1]")
    return matrix


def row_payoffs(matrix: list[list[Fraction]], y: list[Fraction]) -> list[Fraction]:
    return [sum((entry * y[j] for j, entry in enumerate(row)), Fraction()) for row in matrix]


def column_payoffs(matrix: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    return [sum((x[i] * matrix[i][j] for i in range(len(x))), Fraction()) for j in range(len(matrix[0]))]


def profile_regrets(
    R: list[list[Fraction]], C: list[list[Fraction]], x: list[Fraction], y: list[Fraction]
) -> tuple[Fraction, Fraction]:
    r_payoffs = row_payoffs(R, y)
    c_payoffs = column_payoffs(C, x)
    row_total = sum((x[i] * r_payoffs[i] for i in range(len(x))), Fraction())
    col_total = sum((y[j] * c_payoffs[j] for j in range(len(y))), Fraction())
    return max(r_payoffs) - row_total, max(c_payoffs) - col_total


def verify(data: dict[str, Any]) -> dict[str, Any]:
    R = payoff_matrix(data["R"], "R")
    C = payoff_matrix(data["C"], "C")
    if len(R) != len(C) or len(R[0]) != len(C[0]):
        raise ValueError("R and C must have the same shape")
    rows, columns = len(R), len(R[0])
    x_row = probability_vector(data["row_maximin"], rows, "row_maximin")
    y_min = probability_vector(data["row_minimax"], columns, "row_minimax")
    y_column = probability_vector(data["column_maximin"], columns, "column_maximin")
    x_min = probability_vector(data["column_minimax"], rows, "column_minimax")
    v_row = fraction(data["row_value"])
    v_column = fraction(data["column_value"])
    if not 0 <= v_row <= 1 or not 0 <= v_column <= 1:
        raise ValueError("security values must lie in [0, 1]")

    row_lower = min(column_payoffs(R, x_row))
    row_upper = max(row_payoffs(R, y_min))
    column_lower = min(row_payoffs(C, y_column))
    column_upper = max(column_payoffs(C, x_min))
    if row_lower < v_row or row_upper > v_row:
        raise ValueError("R witnesses fail their maximin/minimax inequalities")
    if column_lower < v_column or column_upper > v_column:
        raise ValueError("C^T witnesses fail their maximin/minimax inequalities")
    # Weak duality forces equality once both supplied values are feasible.
    if row_lower != row_upper or v_row != row_lower:
        raise ValueError("R witness values do not meet exactly")
    if column_lower != column_upper or v_column != column_lower:
        raise ValueError("C^T witness values do not meet exactly")
    regrets = profile_regrets(R, C, x_min, y_min)
    if regrets[0] > v_row or regrets[1] > v_column:
        raise AssertionError("security inequalities failed to bound profile regrets")
    return {
        "status": "certified",
        "row_value": str(v_row),
        "column_value": str(v_column),
        "profile_x": [str(item) for item in x_min],
        "profile_y": [str(item) for item in y_min],
        "exact_profile_regrets": [str(item) for item in regrets],
        "certified_regret_upper_bounds": [str(v_row), str(v_column)],
    }


def grid() -> list[list[Fraction]]:
    return [[Fraction(k, 2), Fraction(2 - k, 2)] for k in range(3)]


def zero_sum_witnesses(matrix: list[list[Fraction]]) -> tuple[list[Fraction], list[Fraction], Fraction]:
    strategies = grid()
    row_scores = [(min(column_payoffs(matrix, x)), x) for x in strategies]
    col_scores = [(max(row_payoffs(matrix, y)), y) for y in strategies]
    lower, x = max(row_scores, key=lambda item: item[0])
    upper, y = min(col_scores, key=lambda item: item[0])
    if lower != upper:
        raise AssertionError("grid did not contain an exact zero-sum witness")
    return x, y, lower


def self_test() -> None:
    total = 0
    for raw in itertools.product((0, 1), repeat=8):
        R = [[Fraction(raw[0]), Fraction(raw[1])], [Fraction(raw[2]), Fraction(raw[3])]]
        C = [[Fraction(raw[4]), Fraction(raw[5])], [Fraction(raw[6]), Fraction(raw[7])]]
        x_row, y_min, row_value = zero_sum_witnesses(R)
        y_column, x_min, column_value = zero_sum_witnesses([[C[j][i] for j in range(2)] for i in range(2)])
        # The transpose game's row vector is a column strategy in C and its
        # column vector is a row strategy in C.
        data = {
            "R": [[str(item) for item in row] for row in R],
            "C": [[str(item) for item in row] for row in C],
            "row_maximin": [str(item) for item in x_row],
            "row_minimax": [str(item) for item in y_min],
            "row_value": str(row_value),
            "column_maximin": [str(item) for item in y_column],
            "column_minimax": [str(item) for item in x_min],
            "column_value": str(column_value),
        }
        assert verify(data)["status"] == "certified"
        total += 1
    bad = {
        "R": [["1", "0"], ["0", "1"]], "C": [["0", "1"], ["1", "0"]],
        "row_maximin": ["1/2", "1/2"], "row_minimax": ["1", "0"], "row_value": "1/2",
        "column_maximin": ["1/2", "1/2"], "column_minimax": ["1/2", "1/2"], "column_value": "1/2",
    }
    try:
        verify(bad)
    except ValueError:
        pass
    else:
        raise AssertionError("invalid minimax witness was accepted")
    print(json.dumps({"binary_2x2_games_checked": total, "invalid_witness_rejected": True}, indent=2))


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
        print(json.dumps(verify(data), indent=2))
    except (OSError, ValueError, KeyError, ZeroDivisionError) as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
