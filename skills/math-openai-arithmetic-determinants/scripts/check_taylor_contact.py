"""Check Family 005 polynomial support and exact Taylor contact."""
import argparse
from fractions import Fraction
from math import comb


def scaled_chebyshev(degree, second_kind):
    previous = {0: 1}
    if degree == 0:
        return previous
    current = {0: 2 if second_kind else 1}
    for _ in range(2, degree + 1):
        next_poly = {k: 2*v for k, v in current.items()}
        for k, value in previous.items():
            next_poly[k+2] = next_poly.get(k+2, 0) - value
        previous, current = current, next_poly
    return current


def shift_and_multiply(poly, shift, h, sign=1):
    result = {}
    for degree, coefficient in poly.items():
        for j in range(h+1):
            k = degree + shift + j
            result[k] = result.get(k, 0) + sign*coefficient*(-1)**j*comb(h, j)
    return {k: value for k, value in result.items() if value}


def check(scale):
    n, g, cap, h, contact = 48*scale, 4*scale, 63*scale, 2*scale, 59*scale
    sqrt_coefficients = [Fraction(1)]
    for k in range(1, (contact+n)//2 + 1):
        sqrt_coefficients.append(sqrt_coefficients[-1] * Fraction(2*k-3, 2*k))
    for r in range(n):
        d = abs(r-g)
        p = shift_and_multiply(scaled_chebyshev(d, False), cap-1-d, h)
        q = shift_and_multiply(
            scaled_chebyshev(d-1, True), cap-d, h, 1 if r>g else -1
        ) if d else {}
        assert all(19*scale <= k < 65*scale for k in p)
        assert all(19*scale < k < 65*scale for k in q)
        degree = contact+r
        residual = {k+1: Fraction(v) for k, v in p.items() if k+1 <= degree}
        for k, value in q.items():
            for j in range((degree-k)//2 + 1):
                power = k+2*j
                residual[power] = residual.get(power, 0) - value*sqrt_coefficients[j]
        assert all(power==degree or not v for power,v in residual.items()), r
        assert residual[degree] == Fraction(2)**(g-r), r
    return n


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scale", type=int)
    args = parser.parse_args()
    if args.scale < 1:
        parser.error("scale must be positive")
    print(f"Verified exact contact and support for all {check(args.scale)} rows")
