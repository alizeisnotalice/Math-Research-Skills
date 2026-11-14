"""Exact algebraic check for the W21-044 noise-factor counterexample."""
from fractions import Fraction


def variance_factor(n: int) -> Fraction:
    # G^{ {n} } sums n independent generations; generation j is the
    # average of 2**j iid N(m, sigma^2) variables.
    return sum((Fraction(1, 2**j) for j in range(n)), Fraction(0))


for n in (1, 2, 5, 20, 50):
    v = variance_factor(n)
    expected = Fraction(2) - Fraction(1, 2 ** (n - 1))
    assert v == expected
    print(f"n={n}: mean coefficient={n}; variance/sigma^2={v} (<2)")

print("For m != 0, mean(G^{ {n} })=n*m and variances stay below 2*sigma^2.")
print("Chebyshev: P(|G^{ {n} }|<=R) <= 2*sigma^2/(n*|m|-R)^2 -> 0 for fixed R.")
print("Hence the noise-factor sequence is not tight and has no weak limit.")
