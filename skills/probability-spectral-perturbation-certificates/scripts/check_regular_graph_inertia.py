#!/usr/bin/env python3
"""Exact congruence inertia for the strict nontrivial spectrum test."""
from fractions import Fraction


def cycle_adjacency(size):
    matrix = [[0 for _ in range(size)] for _ in range(size)]
    for vertex in range(size):
        matrix[vertex][(vertex - 1) % size] = 1
        matrix[vertex][(vertex + 1) % size] = 1
    return matrix


def contrast_matrix(size):
    return [
        [int(row == column) - int(row == size - 1) for column in range(size - 1)]
        for row in range(size)
    ]


def multiply(left, right):
    return [
        [sum(left[row][index] * right[index][column] for index in range(len(right)))
         for column in range(len(right[0]))]
        for row in range(len(left))
    ]


def transpose(matrix):
    return [list(column) for column in zip(*matrix)]


def inertia(matrix):
    """Return the exact congruence inertia using 1x1 and 2x2 pivots."""
    remaining = [[Fraction(entry) for entry in row] for row in matrix]
    positive = negative = zero = 0
    while remaining:
        diagonal = next((index for index, row in enumerate(remaining) if row[index]), None)
        if diagonal is not None:
            order = [diagonal] + [index for index in range(len(remaining)) if index != diagonal]
            remaining = [[remaining[row][column] for column in order] for row in order]
            pivot = remaining[0][0]
            positive += pivot > 0
            negative += pivot < 0
            remaining = [
                [remaining[row][column] - remaining[row][0] * remaining[0][column] / pivot
                 for column in range(1, len(remaining))]
                for row in range(1, len(remaining))
            ]
            continue

        pair = next(
            ((row, column) for row in range(len(remaining)) for column in range(row + 1, len(remaining))
             if remaining[row][column]),
            None,
        )
        if pair is None:
            zero += len(remaining)
            break
        first, second = pair
        order = [first, second] + [index for index in range(len(remaining)) if index not in pair]
        remaining = [[remaining[row][column] for column in order] for row in order]
        off_diagonal = remaining[0][1]
        # A zero-diagonal symmetric 2x2 pivot has one positive and one negative direction.
        positive += 1
        negative += 1
        trailing = [row[2:] for row in remaining[2:]]
        cross = [row[:2] for row in remaining[2:]]
        inverse = [[Fraction(0), Fraction(1, off_diagonal)], [Fraction(1, off_diagonal), Fraction(0)]]
        remaining = [
            [trailing[row][column] - sum(cross[row][u] * inverse[u][v] * cross[column][v]
                                          for u in range(2) for v in range(2))
             for column in range(len(trailing))]
            for row in range(len(trailing))
        ]
    return positive, negative, zero


def test_cycle(size, expected):
    adjacency = cycle_adjacency(size)
    degree = sum(adjacency[0])
    squared = multiply(adjacency, adjacency)
    base = [[4 * (degree - 1) * int(row == column) - squared[row][column]
             for column in range(size)] for row in range(size)]
    contrast = contrast_matrix(size)
    certificate = multiply(multiply(transpose(contrast), base), contrast)
    outcome = inertia(certificate)
    assert outcome == expected, (size, certificate, outcome)
    print(f"C_{size}: exact inertia={outcome}")


if __name__ == "__main__":
    test_cycle(5, (4, 0, 0))
    test_cycle(6, (4, 0, 1))
