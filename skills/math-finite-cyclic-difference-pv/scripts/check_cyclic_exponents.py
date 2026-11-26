#!/usr/bin/env python3
"""Verify the exponent-generation condition in the finite cyclic PV construction."""

from __future__ import annotations

import json
from pathlib import Path
import sys


def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (abs(a), 1 if a >= 0 else -1, 0)
    gcd, x1, y1 = egcd(b, a % b)
    return gcd, y1, x1 - (a // b) * y1


def check(payload: dict) -> dict:
    order = payload.get("order")
    exponents = payload.get("exponents")
    if type(order) is not int or order < 1:
        raise ValueError("order must be a positive integer")
    if not isinstance(exponents, list) or not exponents or any(type(e) is not int for e in exponents):
        raise ValueError("exponents must be a nonempty list of integers")
    gcd = order
    coeff_order = 1
    coeffs: list[int] = []
    for exponent in exponents:
        new_gcd, left, right = egcd(gcd, exponent)
        coeff_order *= left
        coeffs = [coefficient * left for coefficient in coeffs]
        coeffs.append(right)
        gcd = new_gcd
    if gcd != 1:
        raise ValueError("gcd(order, exponents) must be 1")
    identity = coeff_order * order + sum(c * e for c, e in zip(coeffs, exponents))
    assert identity == 1
    return {
        "order": order,
        "exponents_mod_order": [e % order for e in exponents],
        "gcd": gcd,
        "bezout_order_coefficient": coeff_order,
        "bezout_exponent_coefficients": coeffs,
        "identity": identity,
    }


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_cyclic_exponents.py INPUT.json")
    try:
        print(json.dumps(check(json.loads(Path(sys.argv[1]).read_text())), sort_keys=True))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
