#!/usr/bin/env python3
"""Exact layer-count certificate for a supplied two-generator semigroup."""

from math import comb, gcd
import json
import sys


def in_semigroup(value, a, b):
    return any((value - multiple * a) >= 0 and (value - multiple * a) % b == 0 for multiple in range(value // a + 1))


def layer_size(total, dimension):
    return comb(total + dimension - 1, dimension - 1)


def check(a, b, dimension):
    if not (2 <= a < b and dimension >= 1 and gcd(a, b) == 1):
        raise ValueError("require coprime integers 2 <= a < b and dimension >= 1")
    frobenius = a * b - a - b
    allowed = [total for total in range(frobenius + 1) if in_semigroup(total, a, b)]
    c = comb(frobenius + dimension, dimension)
    n = sum(layer_size(total, dimension) for total in allowed)
    e = layer_size(a, dimension) + layer_size(b, dimension)
    lower_layer = layer_size(frobenius - 1, dimension) if frobenius else 0
    return {
        "a": a, "b": b, "dimension": dimension, "frobenius": frobenius,
        "c": c, "n": n, "e": e, "full_F_minus_1_layer": lower_layer,
        "wilf_left": dimension * c, "wilf_right": e * n,
        "wilf_holds": dimension * c <= e * n,
    }


if __name__ == "__main__":
    if len(sys.argv) != 4:
        raise SystemExit("usage: check_two_generator_graded_wilf.py a b dimension")
    try:
        result = check(*(int(value) for value in sys.argv[1:]))
    except ValueError as error:
        raise SystemExit(str(error))
    print(json.dumps(result, sort_keys=True))
