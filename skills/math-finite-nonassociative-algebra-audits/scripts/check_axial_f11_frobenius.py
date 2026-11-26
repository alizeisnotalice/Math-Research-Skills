#!/usr/bin/env python3
"""Exact replay of the four-dimensional F_11 axial-algebra data."""

import json

P = 11
N = 4
PERMUTATION = (1, 0, 3, 2)


def add(left, right):
    return tuple((x + y) % P for x, y in zip(left, right))


def scale(value, vector):
    return tuple(value * x % P for x in vector)


def basis(index):
    return tuple(int(index == other) for other in range(N))


PRODUCTS = {
    (0, 0): basis(0), (1, 1): basis(1), (2, 2): basis(2), (3, 3): basis(3),
    (0, 1): (0, 0, 1, 1), (0, 2): (0, -1, 0, -1), (0, 3): (0, 1, 1, 0),
    (1, 2): (1, 0, 0, 1), (1, 3): (-1, 0, -1, 0), (2, 3): (1, 1, 0, 0),
}


def multiply_basis(left, right):
    return tuple(value % P for value in PRODUCTS[tuple(sorted((left, right)))])


def multiply(left, right):
    result = (0,) * N
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result = add(result, scale(x * y, multiply_basis(i, j)))
    return result


def swap(vector):
    result = [0] * N
    for source, target in enumerate(PERMUTATION):
        result[target] = vector[source]
    return tuple(result)


def bilinear(left, right, gram):
    return sum(left[i] * gram[i][j] * right[j] for i in range(N) for j in range(N)) % P


def rank(matrix):
    rows = [list(row) for row in matrix]
    pivot_row = 0
    for column in range(len(rows[0]) if rows else 0):
        pivot = next((row for row in range(pivot_row, len(rows)) if rows[row][column] % P), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        inverse = pow(rows[pivot_row][column] % P, -1, P)
        rows[pivot_row] = [(inverse * value) % P for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row != pivot_row and rows[row][column] % P:
                factor = rows[row][column] % P
                rows[row] = [(value - factor * pivot_value) % P for value, pivot_value in zip(rows[row], rows[pivot_row])]
        pivot_row += 1
    return pivot_row


def main():
    gram = [[0] * N for _ in range(N)]
    for index, value in enumerate((1, -1, 1, -1)):
        gram[index][index] = value % P
    associativity = all(
        bilinear(multiply(basis(i), basis(j)), basis(k), gram)
        == bilinear(basis(i), multiply(basis(j), basis(k)), gram)
        for i in range(N) for j in range(N) for k in range(N)
    )
    automorphism = all(
        multiply_basis(PERMUTATION[i], PERMUTATION[j]) == swap(multiply_basis(i, j))
        for i in range(N) for j in range(N)
    )
    # Associative bilinear forms are the nullspace of the 64 linear conditions.
    equations = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                row = [0] * (N * N)
                for u, coefficient in enumerate(multiply_basis(i, j)):
                    row[u * N + k] += coefficient
                for v, coefficient in enumerate(multiply_basis(j, k)):
                    row[i * N + v] -= coefficient
                equations.append(tuple(value % P for value in row))
    form_dimension = N * N - rank(equations)
    transformed = [basis(PERMUTATION[i]) for i in range(N)]
    flips_form = all(
        bilinear(transformed[i], transformed[j], gram) == (-bilinear(basis(i), basis(j), gram)) % P
        for i in range(N) for j in range(N)
    )
    left_multiplication_invertible = []
    for i in range(N):
        matrix = [[multiply_basis(i, j)[k] for j in range(N)] for k in range(N)]
        left_multiplication_invertible.append(rank(matrix) == N)
    print(json.dumps({
        "field": "F_11", "idempotents": all(multiply_basis(i, i) == basis(i) for i in range(N)),
        "commutative": all(multiply_basis(i, j) == multiply_basis(j, i) for i in range(N) for j in range(N)),
        "frobenius_identity": associativity, "associative_form_space_dimension": form_dimension,
        "swap_is_automorphism": automorphism, "swap_negates_form": flips_form,
        "all_axis_multiplications_invertible": all(left_multiplication_invertible),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
