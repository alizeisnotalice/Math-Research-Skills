#!/usr/bin/env python3
"""Local arithmetic check for the Bernoulli Chernoff example in W15-026.

This checks one exact example only. It is not a proof of the paper's lemmas or
of its sample-complexity claims.
"""
from fractions import Fraction
from math import log, isclose


def bernoulli_kl(z: Fraction, x: Fraction) -> float:
    return float(z) * log(float(z / x)) + float(1 - z) * log(float((1 - z) / (1 - x)))


x = Fraction(1, 5)
y = Fraction(4, 5)
z = Fraction(1, 2)
d_x = bernoulli_kl(z, x)
d_y = bernoulli_kl(z, y)
exact = log(5 / 4)

assert isclose(d_x, d_y, rel_tol=0.0, abs_tol=1e-15)
assert isclose(d_x, exact, rel_tol=0.0, abs_tol=1e-15)

print(f"x={x}, y={y}, equalizer_candidate z={z}")
print(f"d(z,x)={d_x:.16f}")
print(f"d(z,y)={d_y:.16f}")
print(f"ln(5/4)={exact:.16f}")
print("arithmetic check: PASS")
print("scope: one evaluated Chernoff-information example; not theorem verification")
