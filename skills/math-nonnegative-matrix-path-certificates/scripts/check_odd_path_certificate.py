#!/usr/bin/env python3
"""Exact finite replays for the odd nonnegative-matrix path certificate."""

from fractions import Fraction


def matrix_product(left, right):
    return [
        [sum(left[i][h] * right[h][j] for h in range(len(right)))
         for j in range(len(right[0]))]
        for i in range(len(left))
    ]


def identity(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def power(matrix, exponent):
    answer = identity(len(matrix))
    for _ in range(exponent):
        answer = matrix_product(answer, matrix)
    return answer


def bilinear(left, matrix, right):
    return sum(left[i] * matrix[i][j] * right[j]
               for i in range(len(left)) for j in range(len(right)))


def euclidean_square(vector):
    return sum(x * x for x in vector)


def require_path_hypotheses(factors, left, right, exponent):
    if exponent < 1 or exponent % 2 != 1:
        raise ValueError("the path certificate requires a positive odd exponent")
    n = len(left)
    if len(right) != n or not factors:
        raise ValueError("incompatible endpoints or empty factor list")
    for factor in factors:
        if len(factor) != n or any(len(row) != n for row in factor):
            raise ValueError("factors must be square of the endpoint order")
        if any(x < 0 for row in factor for x in row):
            raise ValueError("factors must be entrywise nonnegative")
        if any(factor[i][j] != factor[j][i] for i in range(n) for j in range(n)):
            raise ValueError("factors must be symmetric")
    if any(x < 0 for x in left + right):
        raise ValueError("endpoints must be entrywise nonnegative")


def path_certificate(factors, left, right, exponent):
    require_path_hypotheses(factors, left, right, exponent)
    r = (exponent - 1) // 2
    short = identity(len(left))
    long = identity(len(left))
    for factor in factors:
        short = matrix_product(short, factor)
        long = matrix_product(long, power(factor, exponent))
    z = bilinear(left, short, right)
    q = bilinear(left, long, right)
    lhs = z ** exponent
    rhs = euclidean_square(left) ** r * euclidean_square(right) ** r * q
    return lhs, rhs


def frobenius_square(matrix):
    return sum(x * x for row in matrix for x in row)


def main():
    f = Fraction
    c1 = [[f(1), f(2)], [f(2), f(1)]]
    c2 = [[f(2), f(1)], [f(1), f(3)]]
    lhs, rhs = path_certificate([c1, c2], [f(1), f(2)], [f(3), f(1)], 3)
    assert lhs <= rhs and lhs > 0

    zero_lhs, zero_rhs = path_certificate([c1], [f(0), f(0)], [f(1), f(2)], 3)
    assert (zero_lhs, zero_rhs) == (0, 0)

    try:
        path_certificate([c1], [f(1), f(0)], [f(0), f(1)], 2)
    except ValueError:
        pass
    else:
        raise AssertionError("even exponent was incorrectly accepted")

    # Source p. 5, Remark 3.4: an even-exponent three-factor norm analogue fails.
    z = f(0); o = f(1)
    d1 = [[z, z, z], [z, z, o], [z, o, z]]
    d2 = [[z, z, o], [z, z, z], [o, z, z]]
    d3 = [[z, o, z], [o, z, z], [z, z, z]]
    short = matrix_product(matrix_product(d1, d2), d3)
    long = matrix_product(matrix_product(power(d1, 2), power(d2, 2)), power(d3, 2))
    assert frobenius_square(short) == 1 and frobenius_square(long) == 0

    print("positive", lhs, rhs)
    print("zero-boundary", zero_lhs, zero_rhs)
    print("even-three-factor-frobenius-squares", frobenius_square(short), frobenius_square(long))


if __name__ == "__main__":
    main()
