"""Certify Sondow's finite denominator exclusion by rational arithmetic."""
import argparse
from fractions import Fraction
import json
from math import comb, lcm


def log_unit_bounds(value, terms):
    """Enclose log(value) for 1 <= value <= 2."""
    t = (value - 1) / (value + 1)
    square = t * t
    power = t
    total = Fraction()
    for index in range(terms):
        total += power / (2 * index + 1)
        power *= square
    tail = power / ((2 * terms + 1) * (1 - square))
    return 2 * total, 2 * (total + tail)


def integer_log_bounds(value, terms, log_two):
    exponent = value.bit_length() - 1
    lower, upper = log_unit_bounds(Fraction(value, 1 << exponent), terms)
    return lower + exponent * log_two[0], upper + exponent * log_two[1]


def certificate(n, terms):
    harmonics = [Fraction()]
    denominator = 1
    for j in range(1, 2 * n + 1):
        denominator = lcm(denominator, j)
        harmonics.append(harmonics[-1] + Fraction(1, j))
    log_two = log_unit_bounds(Fraction(2), terms)
    bounds = [Fraction(), Fraction()]
    weights = {}
    for k in range(1, n + 1):
        weight = 2 * denominator * sum(
            comb(n, i) ** 2 * (harmonics[n - i] - harmonics[i])
            for i in range(min(k - 1, n - k) + 1)
        )
        if weight.denominator != 1 or weight < 0:
            raise ArithmeticError("unexpected nonintegral or negative weight")
        weights[n+k] = weight.numerator
        lower, upper = integer_log_bounds(n + k, terms, log_two)
        bounds[0] += weight * lower
        bounds[1] += weight * upper
    lower, upper = bounds
    floor = lower.numerator // lower.denominator
    fractional = [lower - floor, upper - floor] if upper < floor + 1 else None
    threshold = Fraction(1, 1 << n)
    proved = fractional is not None and fractional[0] >= threshold
    return {
        "n": n,
        "terms": terms,
        "weights": weights,
        "fractional_bounds": [str(value) for value in fractional] if fractional else None,
        "threshold": str(threshold),
        "certified": proved,
        "excluded_denominator_divisors_of": denominator * comb(2 * n, n) if proved else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", nargs="+", type=int)
    parser.add_argument("--terms", type=int, default=24)
    args = parser.parse_args()
    if min(args.n) < 1 or args.terms < 1:
        parser.error("n and terms must be positive")
    print(json.dumps([certificate(n, args.terms) for n in args.n], indent=2))


if __name__ == "__main__":
    main()
