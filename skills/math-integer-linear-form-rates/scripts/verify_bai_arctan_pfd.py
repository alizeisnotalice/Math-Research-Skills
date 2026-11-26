#!/usr/bin/env python3
"""Exact finite checks for the scaling in Bai, Lemma 1.

Usage: python3 verify_bai_arctan_pfd.py 1 2
This tests only the supplied indices, not the source's all-n theorem.
"""

import argparse
import sys

import sympy as sp


def check(n: int) -> None:
    if n < 1:
        raise ValueError("Lemma-1 spot checks require n >= 1")
    x = sp.symbols("x")
    r_n = (
        x ** (2 * n)
        * ((x + 1) ** 2 + 16) ** (2 * n)
        * ((x - 1) ** 2 + 16) ** (2 * n)
        / ((17 + x) ** (3 * n + 1) * (17 - x) ** (3 * n + 1))
    )
    regular_part = sp.cancel((17 + x) ** (3 * n + 1) * r_n)
    for j in range(3 * n + 1):
        a_j = sp.cancel(
            sp.diff(regular_part, x, 3 * n - j).subs(x, -17)
            / sp.factorial(3 * n - j)
        )
        scaled = sp.cancel(
            a_j
            * sp.Integer(2) ** (-3 * n - 2 * j + 1)
            * sp.Integer(5) ** (n - j)
            * sp.Integer(17) ** (1 - j)
        )
        if not scaled.is_Integer:
            raise AssertionError(f"n={n}, j={j}: scaled coefficient is {scaled}")
    print(f"n={n}: all {3 * n + 1} scaled coefficients are integers")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, nargs="+", help="positive test indices")
    args = parser.parse_args()
    for n in args.n:
        check(n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
