#!/usr/bin/env python3
"""Exact group-determinant replay for one H5 group-ring element."""
import argparse
import json


def product(left, right):
    a, b, c = left
    big_a, big_b, big_c = right
    return ((a + big_a) % 5, (b + big_b) % 5, (c + big_c + b * big_a) % 5)


def inverse(element):
    a, b, c = element
    return ((-a) % 5, (-b) % 5, (-c + b * a) % 5)


def bareiss(matrix):
    """Return det(matrix) over the integers, with exact row pivoting."""
    size = len(matrix)
    previous = 1
    sign = 1
    for pivot_index in range(size - 1):
        pivot_row = next(
            (row for row in range(pivot_index, size) if matrix[row][pivot_index]),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            matrix[pivot_index], matrix[pivot_row] = (
                matrix[pivot_row],
                matrix[pivot_index],
            )
            sign *= -1
        pivot = matrix[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    matrix[row][column] * pivot
                    - matrix[row][pivot_index] * matrix[pivot_index][column]
                )
                if numerator % previous:
                    raise ArithmeticError("Bareiss division was not exact")
                matrix[row][column] = numerator // previous
        for row in range(pivot_index + 1, size):
            matrix[row][pivot_index] = 0
        previous = pivot
    return sign * matrix[-1][-1]


def main(zero):
    elements = [(a, b, c) for a in range(5) for b in range(5) for c in range(5)]
    coefficients = {} if zero else {
        (0, 0, 0): 1,
        (1, 0, 0): 1,
        (0, 1, 0): 1,
        (0, 2, 0): 1,
        (1, 2, 0): 1,
    }
    matrix = [
        [coefficients.get(product(g, inverse(h)), 0) for h in elements]
        for g in elements
    ]
    determinant = bareiss(matrix)
    expected = 0 if zero else 11 * 5**28
    if determinant != expected:
        raise AssertionError(f"got {determinant}, expected {expected}")
    print(json.dumps({
        "dimension": 125,
        "determinant": determinant,
        "status": "verified",
        "witness": "zero" if zero else "1+x+y+y^2+xy^2",
    }, sort_keys=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--zero", action="store_true")
    main(parser.parse_args().zero)
