#!/usr/bin/env python3
"""Expand the finite q-integer defect identity with integer coefficient lists."""

from __future__ import annotations

import json
from pathlib import Path
import sys


def add(left: list[int], right: list[int], shift: int = 0) -> list[int]:
    result = [0] * max(len(left), len(right) + shift)
    for index, value in enumerate(left):
        result[index] += value
    for index, value in enumerate(right):
        result[index + shift] += value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return result


def q_integer(number: int) -> list[int]:
    return [0] if number == 0 else [1] * number


def divide_by_one_minus_q(numerator: list[int]) -> list[int]:
    quotient: list[int] = []
    running = 0
    for coefficient in numerator:
        running += coefficient
        quotient.append(running)
    if quotient[-1] != 0:
        raise ValueError("numerator is not divisible by 1-q")
    quotient.pop()
    if not quotient:
        return [0]
    while len(quotient) > 1 and quotient[-1] == 0:
        quotient.pop()
    return quotient


def check(payload: dict) -> dict:
    r, m = payload.get("r"), payload.get("m")
    if type(r) is not int or type(m) is not int or r < 1 or m < 1:
        raise ValueError("r and m must be positive integers")
    product = multiply(q_integer(r), q_integer(m))
    rm = q_integer(r * m)
    numerator = add(product, [-x for x in rm])
    left = divide_by_one_minus_q(numerator)
    right = [0]
    for j in range(1, m):
        term = multiply(q_integer(r), q_integer(j * (r - 1)))
        right = add(right, term, shift=j)
    if left != right or any(value < 0 for value in left):
        raise AssertionError("q-integer identity failed")
    return {"r": r, "m": m, "coefficients_low_to_high": left, "nonnegative": True}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_q_integer_defect.py INPUT.json")
    try:
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
