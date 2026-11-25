#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import gcd


def local_total(prime, left, right):
    return sum(
        Fraction(a**3 * b**3, prime ** abs(i - j))
        for (i, a), (j, b) in product(enumerate(left), enumerate(right))
    )


def lift(at_two, at_three):
    return {
        2**i * 3**j: a * b
        for (i, a), (j, b) in product(enumerate(at_two), enumerate(at_three))
    }


def main():
    # u=3/4, s=1. The input masses are fourth powers of these weights.
    at_two = ((1, 4, 2), (3, 2))
    at_three = ((3, 1), (1, 3, 2))
    left = lift(at_two[0], at_three[0])
    right = lift(at_two[1], at_three[1])
    direct = sum(
        Fraction((a * b)**3 * gcd(n, m)**2, n * m)
        for (n, a), (m, b) in product(left.items(), right.items())
    )
    factored = local_total(2, *at_two) * local_total(3, *at_three)
    assert direct == factored
    print(f"Exact kernel product: pairs={len(left) * len(right)}, total={direct}")


if __name__ == "__main__":
    main()
