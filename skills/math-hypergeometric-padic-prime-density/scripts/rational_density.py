#!/usr/bin/env python3
"""Exact residue-class calculation for rational {}_nF_{n-1} parameters.

Input JSON: {"numerators":["1/5",...], "denominators":["4/5",...]}
All entries must be rational strings strictly between zero and one.
"""
import json
import math
import sys
from fractions import Fraction


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def units(modulus):
    return [u for u in range(1, modulus) if math.gcd(u, modulus) == 1]


def frac_part(x):
    return x - math.floor(x)


def majorized(numerators, denominators, unit, modulus):
    """Tests all powers of unit modulo modulus using an exact matching search."""
    power, seen = 1, set()
    while power not in seen:
        seen.add(power)
        left = [frac_part(-power * b) for b in denominators]
        right = [frac_part(-power * a) for a in numerators]
        edges = [[j for j, x in enumerate(right) if y <= x] for y in left]
        match = [-1] * len(right)

        def augment(i, used):
            for j in edges[i]:
                if j in used:
                    continue
                used.add(j)
                if match[j] < 0 or augment(match[j], used):
                    match[j] = i
                    return True
            return False

        if not all(augment(i, set()) for i in range(len(left))):
            return False
        power = (power * unit) % modulus
    return True


def main():
    data = json.load(sys.stdin)
    numerators = data["numerators"]
    denominators = data["denominators"]
    if any(type(value) is not str for value in numerators + denominators):
        raise ValueError("supply exact rational strings for every parameter")
    alpha = [Fraction(value) for value in numerators]
    beta = [Fraction(value) for value in denominators]
    if len(alpha) != len(beta) + 1:
        raise ValueError("requires rational regular-singular nF_{n-1}: len(numerators)=len(denominators)+1")
    if any(not (0 < x < 1) for x in alpha + beta):
        raise ValueError("parameters must be normalized to the open interval (0,1)")
    if set(alpha) & set(beta):
        raise ValueError("coincident numerator/denominator parameters are outside this theorem interface")
    modulus = 1
    for x in alpha + beta:
        modulus = lcm(modulus, x.denominator)
    good = [u for u in units(modulus) if majorized(alpha, beta, u, modulus)]
    phi = len(units(modulus))
    print(json.dumps({"modulus": modulus, "bounded_unit_classes": good,
                      "density": str(Fraction(len(good), phi))}, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (TypeError, KeyError, ValueError, ZeroDivisionError) as error:
        raise SystemExit(str(error)) from error
