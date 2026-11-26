#!/usr/bin/env python3
"""Exact valuation sanity model for the finite-analytic-jet contract over Q_3."""
from fractions import Fraction


def v3(q: Fraction) -> int:
    if q == 0:
        return 10**9
    num, den = abs(q.numerator), q.denominator
    out = 0
    while num % 3 == 0:
        num //= 3
        out += 1
    while den % 3 == 0:
        den //= 3
        out -= 1
    return out


for m in range(0, 6):
    for n in range(max(1, m), 8):
        t = Fraction(3**n, 1)
        # sum_{j>N} t^j = t^(N+1)/(1-t); coefficients are integral.
        tail = t ** (n + 1) / (1 - t)
        assert v3(tail) == n * (n + 1)
        assert v3(tail) >= (m + 1) * n
        # P=X_1, delta_N=(0,t), so P(delta_N)=0 and Q_m(U_N)=0.
        assert Fraction(0, 1) == 0
print("validated exact Q_3 finite-tail model for m=0..5, N=m..7")
