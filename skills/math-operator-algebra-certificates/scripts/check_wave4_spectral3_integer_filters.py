#!/usr/bin/env python3
"""Exact finite algebra checks for the wave4 spectral-3 integer filters."""

from fractions import Fraction


def add(left, right):
    out = [Fraction(0)] * max(len(left), len(right))
    for i, value in enumerate(left):
        out[i] += value
    for i, value in enumerate(right):
        out[i] += value
    return out


def mul(left, right):
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i + j] += x * y
    return out


def scale(poly, scalar):
    return [scalar * x for x in poly]


def evaluate(poly, value):
    result = Fraction(0)
    for coefficient in reversed(poly):
        result = result * value + coefficient
    return result


def chebyshev(degree):
    if degree == 0:
        return [Fraction(1)]
    first, second = [Fraction(1)], [Fraction(0), Fraction(1)]
    for _ in range(1, degree):
        first, second = second, add(scale(mul([Fraction(0), Fraction(1)], second), 2), scale(first, -1))
    return second


def compose_affine(poly, constant, linear):
    answer = [Fraction(0)]
    for coefficient in reversed(poly):
        answer = add(mul(answer, [constant, linear]), [coefficient])
    return answer


def main():
    # A finite exact instance of the root-times-Chebyshev construction.  It
    # checks algebraic invariants only, not the source's asymptotic budgets.
    roots = [Fraction(1)]
    for integer in range(1, 5):
        roots = mul(roots, [Fraction(1), Fraction(-1, integer)])
    cheb = compose_affine(chebyshev(5), Fraction(9, 5), Fraction(-2, 5))
    denominator = evaluate(cheb, 0)
    assert denominator != 0
    zero_filter = scale(mul(roots, cheb), Fraction(1, 1) / denominator)
    assert evaluate(zero_filter, 0) == 1
    assert all(evaluate(zero_filter, integer) == 0 for integer in range(1, 5))
    assert chebyshev(0) == [Fraction(1)]
    assert chebyshev(1) == [Fraction(0), Fraction(1)]
    assert evaluate(chebyshev(5), Fraction(3, 2)) == Fraction(123, 2)
    assert evaluate(zero_filter, 5) != 0  # Reject a false claim of an extra root.
    print("exact integer-filter algebra: PASS; roots=1,2,3,4; normalized_at_zero=1")


if __name__ == "__main__":
    main()
