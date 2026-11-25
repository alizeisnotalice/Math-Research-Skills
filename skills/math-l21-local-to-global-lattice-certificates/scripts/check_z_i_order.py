#!/usr/bin/env python3
"""Exact additive-index and R-saturation checks for Z[i] over Z+2Zi."""

from itertools import combinations
from math import gcd


def multiply_by_i(vector):
    a, b = vector
    return -b, a


def lattice_index(vectors):
    determinants = [
        abs(left[0] * right[1] - left[1] * right[0])
        for left, right in combinations(vectors, 2)
    ]
    result = 0
    for determinant in determinants:
        result = gcd(result, determinant)
    return result


def r_span_index(generators):
    return lattice_index(generators + [multiply_by_i(vector) for vector in generators])


def main():
    unit_translate_one = [(1, 0), (0, 2)]
    unit_translate_i = [(0, 1), (-2, 0)]
    bad_same_index = [(1, 1), (0, 2)]

    for name, lattice, expected_saturation in [
        ("O", unit_translate_one, 1),
        ("iO", unit_translate_i, 1),
        ("bad", bad_same_index, 2),
    ]:
        assert lattice_index(lattice) == 2
        assert r_span_index(lattice) == expected_saturation
        print(f"{name}: [R:L]=2, [R:RL]={expected_saturation}")

    print("PASS: equal additive index does not certify R-saturation")


if __name__ == "__main__":
    main()
