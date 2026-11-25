#!/usr/bin/env python3
'''Replay the two rational digit congruences on complete finite grids.'''

from fractions import Fraction
from math import comb


def boundary_arrays(height):
    moments = [Fraction(0) for _ in range(height + 1)]
    minus = [Fraction(0) for _ in moments]
    plus = [Fraction(0) for _ in moments]
    moments[0] = minus[1] = Fraction(2)
    for u in range(2, height + 1):
        moments[u] = Fraction(u, u + 1) * moments[u - 2]
        minus[u] = ((u - 1) * minus[u - 2] + moments[u - 2] + moments[u - 1]) / u
        plus[u] = ((u - 2) * plus[u - 2] + Fraction(2, u - 1)) / (u - 1)
    return moments, minus, plus


def moment_rows(height, arrays):
    moments, minus, plus = arrays
    row = plus[:height]
    yield row
    for i in range(1, height):
        row = [minus[i]] + [row[j - 1] - moments[i - 1] / j for j in range(1, height)]
        yield row


def harmonic_sums(height, degree):
    partial = [Fraction(0)]
    for k in range(1, height):
        partial.append(partial[-1] + Fraction(1, k**degree))
    return partial


def scaled_residue(value, p):
    if value.denominator % p == 0:
        raise ArithmeticError('nonintegral scaled entry')
    return (value.numerator * pow(value.denominator, -1, p)) % p


def verify_grid(p, height):
    if not p <= height or not 4 * height < p**2:
        raise ValueError('the source requires 2 sqrt(H) < p <= H')
    arrays = boundary_arrays(height)
    _, _, plus = arrays
    reduced_size = (height - 1) // p + 1
    reduced = list(moment_rows(reduced_size, arrays))
    b1, b2 = (harmonic_sums(height, degree) for degree in (1, 2))
    e = [((-1)**(d // 2) * comb((p - 1) // 2, d // 2)) % p if d % 2 == 0 else 0
         for d in range(p)]

    def z0(i, j):
        if i == j:
            return -b2[i]
        return (b1[i] - b1[j]) / (i - j)

    boundary_count = 0
    for i, row in enumerate(moment_rows(height, arrays)):
        for j, value in enumerate(row):
            high_j, low_j = divmod(j, p)
            high_i, low_i = divmod(i, p)
            digit = (j - i - 1) % p
            reduced_i = (i - low_j) // p
            if reduced_i == -1:
                value_reduced = plus[high_j + 1]
                boundary_count += 1
            else:
                value_reduced = reduced[reduced_i][high_j]
            expected_m = scaled_residue(e[digit] * value_reduced, p)
            assert scaled_residue(p**2 * value, p) == expected_m, ('M0', p, i, j)
            expected_z = scaled_residue(z0(high_i, high_j), p) if low_i == low_j else 0
            assert scaled_residue(p**2 * z0(i, j), p) == expected_z, ('Z0', p, i, j)
    return height**2, boundary_count


if __name__ == '__main__':
    for prime, h in ((17, 65), (29, 195), (53, 650)):
        entries, boundary = verify_grid(prime, h)
        print(f'p={prime}, H={h}: {entries} checks each for M0 and Z0; {boundary} exterior-index checks')
