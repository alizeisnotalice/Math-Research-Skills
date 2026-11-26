#!/usr/bin/env python3
"""Exact replay of Cogentic MaximinKiteNE Step 2 player-role normalization."""
import json
import sys
from kite_mixing import matrix, regrets, vector


def transpose(game):
    return [list(column) for column in zip(*game)]


def as_text(values):
    return [str(value) for value in values]


def check(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    R, C = matrix(data["R"], "R"), matrix(data["C"], "C")
    if len(R) != len(C) or len(R[0]) != len(C[0]):
        raise ValueError("R and C must have identical shape")
    x, y = vector(data["x"], len(R), "x"), vector(data["y"], len(R[0]), "y")
    swap = data["swap"]
    if not isinstance(swap, bool):
        raise ValueError("swap must be a Boolean")
    original = regrets(R, C, x, y)[:2]
    if swap:
        Rt, Ct, xt, yt = transpose(C), transpose(R), y, x
        expected = (original[1], original[0])
    else:
        Rt, Ct, xt, yt = R, C, x, y
        expected = original
    normalized = regrets(Rt, Ct, xt, yt)[:2]
    if normalized != expected:
        raise AssertionError("exact regret-transport identity failed")
    return {
        "valid": True,
        "swap": swap,
        "original_regrets": as_text(original),
        "normalized_regrets": as_text(normalized),
        "expected_normalized_regrets": as_text(expected),
        "normalized_shape": [len(Rt), len(Rt[0])],
        "normalized_x": as_text(xt),
        "normalized_y": as_text(yt),
    }


def main(argv):
    if len(argv) != 2:
        raise ValueError("usage: check_player_role_normalization.py INPUT.json")
    with open(argv[1], encoding="utf-8") as handle:
        print(json.dumps(check(json.load(handle)), sort_keys=True))


if __name__ == "__main__":
    try:
        main(sys.argv)
    except (AssertionError, KeyError, OSError, ValueError, ZeroDivisionError) as error:
        print(json.dumps({"valid": False, "error": str(error)}, sort_keys=True))
        raise SystemExit(2)
