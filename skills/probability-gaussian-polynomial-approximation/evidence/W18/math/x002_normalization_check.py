"""Exact finite check of the W18-X002 scaling example; not a theorem proof."""
from fractions import Fraction


def convolve(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


g = [Fraction(2), Fraction(2)]
h = [Fraction(1, 2), Fraction(0), Fraction(1, 2)]
product = convolve(g, h)
g_monic = [x / g[-1] for x in g]
h_monic = [x * g[-1] for x in h]
assert product == [1, 1, 1, 1]
assert convolve(g_monic, h_monic) == product
assert g_monic == [1, 1] and h_monic == [1, 0, 1]
print("exact coefficients:", product)
print("monic reciprocal rescaling:", g_monic, h_monic)
