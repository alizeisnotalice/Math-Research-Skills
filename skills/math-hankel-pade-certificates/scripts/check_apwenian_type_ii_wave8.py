#!/usr/bin/env python3
"""Exact finite checks for the odd type-II apwenian admission predicate."""

import argparse
from fractions import Fraction
import json


def bareiss_det(matrix):
    work = [row[:] for row in matrix]
    sign, previous = 1, 1
    for k in range(len(work) - 1):
        if work[k][k] == 0:
            pivot = next((r for r in range(k + 1, len(work)) if work[r][k] != 0), None)
            if pivot is None:
                return 0
            work[k], work[pivot] = work[pivot], work[k]
            sign *= -1
        pivot = work[k][k]
        for i in range(k + 1, len(work)):
            for j in range(k + 1, len(work)):
                work[i][j] = (work[i][j] * pivot - work[i][k] * work[k][j]) // previous
        previous = pivot
        for i in range(k + 1, len(work)):
            work[i][k] = 0
    return sign * work[-1][-1]


def require_admissible(v):
    p = len(v)
    if p < 3 or p % 2 != 1 or v[0] != 1 or any(x not in (-1, 1) for x in v):
        raise ValueError("require odd p>=3 and a +/-1 word with v[0]=1")
    for j in range(p - 1):
        numerator = v[j] + v[(j + 1) % p] - v[(2 * j + 1) % p] - v[(2 * j + 2) % p]
        if numerator % 2 or (numerator // 2) % 2 != 1:
            raise ValueError(f"source parity condition fails at j={j}")


def coefficients(v, count):
    p = len(v)
    out = [0] * count
    out[0] = 1
    for n in range(1, count):
        out[n] = v[n % p] * out[n // p]
    return out


def hankel(coeffs, n):
    return bareiss_det([[coeffs[i + j] for j in range(n)] for i in range(n)])


def certify_polynomial_nonzero_for_base(v, base):
    if base < 2:
        raise ValueError("base must be at least 2")
    # At x=b^(-p^m), x<=1/b.  The displayed rational upper bound is <1.
    x = Fraction(1, base)
    tail_bound = sum((x ** j for j in range(1, len(v))), Fraction())
    assert tail_bound < 1
    return tail_bound


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--word", default="1,1,-1", help="comma-separated signs")
    parser.add_argument("--through", type=int, default=7, help="largest finite Hankel order")
    parser.add_argument("--base", type=int, default=2)
    args = parser.parse_args()
    try:
        word = [int(value) for value in args.word.split(",")]
        require_admissible(word)
        if args.through < 1:
            raise ValueError("through must be positive")
        bound = certify_polynomial_nonzero_for_base(word, args.base)
    except ValueError as error:
        parser.error(str(error))
    coeffs = coefficients(word, 2 * args.through - 1)
    determinants = [hankel(coeffs, n) for n in range(1, args.through + 1)]
    for n, determinant in enumerate(determinants, 1):
        if determinant % (2**n) != 2**(n - 1):
            raise ArithmeticError(f"finite Hankel valuation disagrees with the source at order {n}")
    print(json.dumps({"word": word, "hankel_determinants": determinants,
                      "nonzero_polynomial_tail_bound": str(bound),
                      "base": args.base, "source_residue_predicate": True}))


if __name__ == "__main__":
    main()
