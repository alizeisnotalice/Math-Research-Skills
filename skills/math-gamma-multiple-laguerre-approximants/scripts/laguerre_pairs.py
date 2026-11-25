"""Generate exact x=1 Wolfs–Van Assche mixed Laguerre approximants."""
import argparse
from fractions import Fraction
import json
from math import comb, factorial, gcd, lcm


def pair(n):
    harmonics = [Fraction()]
    for k in range(1, n + 1):
        harmonics.append(harmonics[-1] + Fraction(1, k))
    factorial_n = factorial(n)
    denominator = factorial_n * lcm(*range(1, n + 1))
    p = q = 0
    for k in range(n + 1):
        base = Fraction(comb(n, k) ** 2, factorial(k))
        middle = comb(n + k, k)
        correction = sum(
            Fraction((-1) ** ell * comb(n + k, n - ell), ell)
            for ell in range(1, n + 1)
        )
        second = base * middle
        first = base * (
            middle * (3 * harmonics[k] - 2 * harmonics[n - k]) + correction
        )
        if (factorial_n * second).denominator != 1 or (denominator * first).denominator != 1:
            raise ArithmeticError("coefficient integrality check failed")
        p += (denominator * first).numerator
        q += (denominator * second).numerator
    divisor = gcd(p, q)
    return {"n": n, "D": denominator, "P": p, "Q": q, "gcd": divisor,
            "reduced_P": p // divisor, "reduced_Q": q // divisor}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("n", nargs="+", type=int)
    args = parser.parse_args()
    if min(args.n) < 1:
        parser.error("n must be positive")
    print(json.dumps([pair(n) for n in args.n], indent=2))


if __name__ == "__main__":
    main()
