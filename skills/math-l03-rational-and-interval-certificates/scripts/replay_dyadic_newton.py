#!/usr/bin/env python3
'''Exact-rational replay of bounded precision and integer correction.'''

from fractions import Fraction
from math import isqrt
from random import Random


def floor_dyadic(value, bits):
    return Fraction((value.numerator << bits) // value.denominator, 1 << bits)


def precision_steps(target):
    precision = 1
    yield 6
    while precision < target:
        precision = min(2 * precision, target)
        yield precision + 5


def reciprocal(c, target):
    assert 1 <= c < 2 and target >= 1
    x = Fraction(5, 8)
    for bits in precision_steps(target):
        c_prefix = floor_dyadic(c, bits)
        product = floor_dyadic(c_prefix * x, bits)
        x = floor_dyadic(x * (2 - product), bits)
        assert abs(1 - c * x) <= Fraction(1, 1 << (bits - 4))
    return x


def square_root(c, target):
    assert 1 <= c < 4 and target >= 1
    x = Fraction(3, 2)
    for bits in precision_steps(target):
        shift = -1 if x < 1 else (1 if x >= 2 else 0)
        factor = Fraction(2) ** shift
        inverse = reciprocal(x / factor, bits) / factor
        q = floor_dyadic(floor_dyadic(c, bits) * inverse, bits)
        x = floor_dyadic((x + q) / 2, bits)
        error = Fraction(1, 1 << (bits - 4))
        assert (x - error)**2 <= c <= (x + error)**2
    return x


def integer_divide(a, b, bits):
    shift = b.bit_length() - 1
    c = Fraction(b, 1 << shift)
    estimate = Fraction(a, 1 << shift) * reciprocal(c, 2 * bits + 4)
    q = estimate.numerator // estimate.denominator
    r = a - b * q
    if r < 0:
        return q - 1, r + b
    if r >= b:
        return q + 1, r - b
    return q, r


def integer_sqrt(a, bits):
    if a == 0:
        return 0
    shift = (a.bit_length() - 1) // 2
    c = Fraction(a, 1 << (2 * shift))
    estimate = (1 << shift) * square_root(c, 2 * bits + 4)
    s = estimate.numerator // estimate.denominator
    if s**2 > a:
        return s - 1
    if (s + 1)**2 <= a:
        return s + 1
    return s


if __name__ == '__main__':
    rng = Random(109)
    divisions = roots = 0
    for width in (2, 6, 8, 16, 31, 53):
        maximum = (1 << width) - 1
        values = [0, 1, 2, maximum - 1, maximum]
        values.extend(rng.randrange(1 << width) for _ in range(64))
        values.extend(x*x for x in (1, 2, isqrt(maximum)) if x*x <= maximum)
        for a in values:
            assert integer_sqrt(a, width) == isqrt(a)
            roots += 1
            for b in (1, 2, maximum, rng.randrange(1, maximum + 1)):
                assert integer_divide(a, b, width) == divmod(a, b)
                divisions += 1
    print(f'Exact checks passed: {divisions} divisions, {roots} integer square roots')
