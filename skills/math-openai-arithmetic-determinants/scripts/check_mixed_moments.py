"""Check the exact zeta(2) cancellation in Family 005 raw columns."""
import argparse
from fractions import Fraction
from math import comb

from check_taylor_contact import scaled_chebyshev, shift_and_multiply


def inverse_sqrt_coefficient(degree):
    if degree < 0 or degree % 2:
        return Fraction()
    return Fraction(comb(degree, degree // 2), 2**degree)


def check(scale):
    size, shift, cap, power = 48*scale, 4*scale, 63*scale, 2*scale
    first_column, stop_column = 7*scale, 59*scale
    coefficients = {
        degree: inverse_sqrt_coefficient(degree) for degree in range(stop_column)
    }
    for row in range(size):
        order = abs(row-shift)
        p = shift_and_multiply(scaled_chebyshev(order, False), cap-1-order, power)
        d = shift_and_multiply(scaled_chebyshev(order-1, True), cap-order, power,
                               1 if row>shift else -1) if order else {}
        for column in range(first_column, stop_column):
            coefficient = sum(value*coefficients[column-k-1]
                              for k,value in p.items() if k < column)
            if coefficient != d.get(column, 0):
                raise ArithmeticError(f"nonzero zeta coefficient: row {row}, column {column}")
    return size * (stop_column-first_column)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scale", type=int)
    args = parser.parse_args()
    if args.scale < 1:
        parser.error("scale must be positive")
    print(f"Verified zeta(2) cancellation in all {check(args.scale)} raw entries")
