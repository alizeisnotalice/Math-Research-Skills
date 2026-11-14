#!/usr/bin/env python3
"""Numerical sanity check only; not a proof of Tropp's theorem."""
from fractions import Fraction
from math import exp, comb

n = 20
t = Fraction(5, 1)
# X_i = Bernoulli(1/2)-1/2 are independent centered 1x1 self-adjoint matrices.
# X_i^2 = 1/4, so use A_i^2=1/4 and sigma^2=sum A_i^2=n/4.
exact = sum(Fraction(comb(n, k), 2**n) for k in range(15, n + 1))
sigma2 = Fraction(n, 4)
tropp_rhs = exp(-float(t * t / (8 * sigma2)))
print(f"model: n={n}, p=1/2, event=sum(X_i)>=5 (equiv. Bin(20,1/2)>=15)")
print(f"exact binomial probability = {float(exact):.12g} ({exact})")
print(f"P001 Theorem 1.3 scalar RHS = exp(-t^2/(8 sigma^2)) = {tropp_rhs:.12g}")
print(f"numerical comparison exact <= RHS: {float(exact) <= tropp_rhs}")
print("This finite calculation checks one instance only; theorem validity comes from the source proof, not this output.")
