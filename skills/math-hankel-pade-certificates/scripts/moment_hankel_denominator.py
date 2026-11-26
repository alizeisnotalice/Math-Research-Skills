"""Clear the affine moment Hankel denominators in Zudilin's log-integral example."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
from math import comb, lcm, prod

from sympy import Matrix, Poly, Symbol, ZZ

from hankel_pade_certificate import hankel


def log_affine_moment(index: int, argument: int) -> tuple[int, Fraction]:
    """Return (a,b) such that I_index(argument) = a*log(argument) + b."""
    if index < 0 or argument < 2:
        raise ValueError("require nonnegative index and integer log argument at least two")
    coefficient = sum(comb(index, u)**2 * argument**u for u in range(index + 1))
    constant = Fraction(0)
    for u in range(index + 1):
        for v in range(index + 1):
            power = u + v - index
            if power:
                sign = -1 if (index + u + v) % 2 else 1
                constant += sign * comb(index, u) * comb(index, v) * Fraction(
                    argument**u - argument**(index - v), power
                )
    return coefficient, constant


def integer_hankel_polynomial(
    coefficients: list[tuple[int | Fraction, int | Fraction]],
    denominators: list[int],
    order: int,
    shift: int = 0,
) -> tuple[int, Poly]:
    """Return D and the integer polynomial D*det(m_(shift+i+j)(X))."""
    end = shift + 2 * order - 1
    if order < 1 or shift < 0 or len(coefficients) < end or len(denominators) < end:
        raise ValueError("insufficient input for positive order and nonnegative shift")
    scales = denominators[shift:end]
    if any(type(d) is not int or d <= 0 for d in scales):
        raise ValueError("denominators must be positive integers")
    if any(right % left for left, right in zip(scales, scales[1:])):
        raise ValueError("need the given consecutive divisibility chain")
    for pair, scale in zip(coefficients[shift:end], scales):
        if any((Fraction(value) * scale).denominator != 1 for value in pair):
            raise ValueError("input scale fails to clear an affine moment coefficient")

    symbol = Symbol("X")
    rows = []
    row_scales = []
    for row in range(order):
        scale = denominators[shift + row + order - 1]
        row_scales.append(scale)
        entries = coefficients[shift + row:shift + row + order]
        rows.append([int(scale*a)*symbol + int(scale*b) for a,b in entries])
    return prod(row_scales), Poly(Matrix(rows).det(method="domain-ge"), symbol, domain=ZZ)


def examples(order: int, argument: int) -> dict:
    moments = [log_affine_moment(k, argument) for k in range(2 * order - 1)]
    denominators = [1]
    for index in range(1, len(moments)):
        denominators.append(lcm(denominators[-1], index))
    scale, polynomial = integer_hankel_polynomial(moments, denominators, order)

    # The point measure at 1/2 has decaying moments but vanishing 2-by-2 determinant.
    rank_one = hankel([Fraction(1, 2)**index for index in range(3)], 2)
    return {
        "order": order,
        "log_argument": argument,
        "row_clearing_multiplier": scale,
        "integer_polynomial_coefficients_low_to_high": [int(c) for c in reversed(polynomial.all_coeffs())],
        "rank_one_boundary_H2": str(rank_one),
        "scope": "exact finite determinants and row clearing; the infinite-support and asymptotic hypotheses are separate",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, default=2)
    parser.add_argument("--log-argument", type=int, default=3)
    args = parser.parse_args()
    if args.order < 1 or args.log_argument < 2:
        parser.error("require order >= 1 and log argument >= 2")
    print(json.dumps(examples(args.order, args.log_argument), indent=2))


if __name__ == "__main__":
    main()
