#!/usr/bin/env python3
"""Finite check of Aptekarev v2 determinant identities and normalizations."""

import argparse
from fractions import Fraction
from math import factorial


def original_coefficients(n: int) -> tuple[int, int, int, int]:
    return (
        16 * n - 15,
        128 * n**3 + 40 * n**2 - 82 * n - 45,
        -n**2 * (256 * n**3 - 240 * n**2 + 64 * n - 7),
        n**2 * (n - 1)**2 * (16 * n + 1),
    )


def determinant_coefficients(n: int) -> tuple[int, int, int, int]:
    return (
        (16 * n + 1) * (16 * n - 15),
        (16 * n - 15) * (256 * n**3 + 528 * n**2 + 352 * n + 73),
        -(16 * n + 17) * (128 * n**3 + 40 * n**2 - 82 * n - 45),
        n**2 * (16 * n + 17) * (16 * n + 1),
    )


def sequence(initial, coefficients, last):
    values = [Fraction(value) for value in initial]
    for n in range(2, last):
        leading, first, second, third = coefficients(n)
        value = first * values[n] + second * values[n - 1] + third * values[n - 2]
        values.append(value / leading)
    return values


def delta(a, b, n):
    return a[n + 1] * b[n] - a[n] * b[n + 1]


def approximate_residuals(p, q, r):
    try:
        import mpmath as mp
    except ImportError as error:
        raise SystemExit("--numeric requires mpmath in the selected Python environment") from error

    mp.mp.dps = 320
    gompertz = mp.e * mp.e1(1)

    def real(x):
        return mp.mpf(x.numerator) / x.denominator

    f = [real(pn) - mp.euler * real(qn) for pn, qn in zip(p, q)]
    g = [mp.e * fn - gompertz * real(qn) + real(rn) for fn, qn, rn in zip(f, q, r)]
    print("Finite high-precision comparisons using the printed (9) normalization:")
    for n in (6, 10, 20, 30, 40):
        ell = delta(f, g, n) / factorial(n)**2
        scaled = ell * mp.exp(mp.sqrt(2 * n)) * 4**n / n**mp.mpf("1.25")
        print(f"n={n}: 16^n*g_n={mp.nstr(16**n * g[n], 14)}, scaled l_n={mp.nstr(scaled, 14)}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--numeric", action="store_true", help="also run the mpmath comparison")
    args = parser.parse_args()
    p = sequence((0, 2, 31), original_coefficients, 41)
    q = sequence((1, 3, 50), original_coefficients, 41)
    r = sequence((0, 1, 24), original_coefficients, 41)
    for a, b, initial in ((q, p, (-2, 7, 558)), (q, r, (-1, -22, -1518)), (p, r, (0, -17, -1209))):
        expected = sequence(initial, determinant_coefficients, 40)
        actual = [delta(a, b, n) / factorial(n)**2 for n in range(41)]
        assert actual == expected
        assert all(value.denominator == 1 for value in actual)
    print("Exact replay: all 123 normalized determinants agree with (2) at n=0,...,40.")
    if args.numeric:
        approximate_residuals(p, q, r)


if __name__ == "__main__":
    main()
