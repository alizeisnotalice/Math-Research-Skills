#!/usr/bin/env python3
"""Evaluate Hardy's quadratic defect for a rational step function on (0, infinity)."""
from __future__ import annotations

import argparse
from fractions import Fraction
import json
from pathlib import Path


def rational(value: object) -> Fraction:
    if type(value) not in (int, str):
        raise ValueError("endpoints and heights must be integers or rational strings")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError("invalid rational endpoint or height") from error


def expression(constant: Fraction, logarithms: dict[Fraction, Fraction]) -> dict:
    return {
        "constant": str(constant),
        "log_terms": [
            {"coefficient": str(coefficient), "argument": str(argument)}
            for argument, coefficient in sorted(logarithms.items()) if coefficient
        ],
    }


def certify(payload: object) -> dict:
    if not isinstance(payload, dict) or not isinstance(steps := payload.get("steps"), list) or not steps:
        raise ValueError("supply a nonempty steps array")
    slope_energy = Fraction(0)
    inverse_square_energy = Fraction(0)
    log_coefficients: dict[Fraction, Fraction] = {}
    left = Fraction(0)
    primitive = Fraction(0)
    for step in steps:
        if not isinstance(step, dict):
            raise ValueError("each step must give end and value")
        right, height = rational(step.get("end")), rational(step.get("value"))
        if right <= left:
            raise ValueError("endpoints must increase strictly from zero")
        intercept = primitive - height * left
        slope_energy += height**2 * (right - left)
        if left > 0:
            inverse_square_energy += intercept**2 * (1 / left - 1 / right)
            argument = right / left
            log_coefficients[argument] = log_coefficients.get(argument, Fraction(0)) + 2 * height * intercept
        primitive += height * (right - left)
        left = right
    tail = primitive**2 / left
    h_constant = slope_energy + inverse_square_energy + tail
    residual_logs = {argument: -coefficient for argument, coefficient in log_coefficients.items()}
    deficit_constant = 4 * slope_energy - h_constant
    if deficit_constant != h_constant:
        raise AssertionError("telescoping endpoint contributions did not cancel")
    return {
        "f_l2_squared": str(slope_energy),
        "primitive_after_last_endpoint": str(primitive),
        "tail_energy": str(tail),
        "hardy_l2_squared": expression(h_constant, log_coefficients),
        "residual_l2_squared": expression(h_constant, residual_logs),
        "deficit": expression(deficit_constant, residual_logs),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = certify(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
