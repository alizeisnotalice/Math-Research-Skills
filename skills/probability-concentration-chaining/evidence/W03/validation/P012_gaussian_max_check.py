"""Numerical sanity check for P012 Theorem 2.1; not a proof."""
from math import erf, exp, pi, sqrt

EPSILONS = (0.01, 0.1)
SIZES = (1, 10, 100)
SQRT2 = sqrt(2.0)

def cdf(x):
    return 0.5 * (1.0 + erf(x / SQRT2))

def expected_max(n, step=0.002, limit=10.0):
    # Composite Simpson quadrature of E M = int_0^inf(1-F^n)dx-int_-inf^0 F^n dx.
    def simpson(a, b, f):
        panels = int(round((b - a) / step))
        if panels % 2:
            panels += 1
        h = (b - a) / panels
        acc = f(a) + f(b)
        for i in range(1, panels):
            acc += (4.0 if i % 2 else 2.0) * f(a + i * h)
        return acc * h / 3.0
    positive = simpson(0.0, limit, lambda x: 1.0 - cdf(x) ** n)
    negative = simpson(-limit, 0.0, lambda x: cdf(x) ** n)
    return positive - negative

def golden_max(f, left=-8.0, right=8.0, tol=1e-10):
    ratio = (sqrt(5.0) - 1.0) / 2.0
    x1 = right - ratio * (right - left)
    x2 = left + ratio * (right - left)
    y1, y2 = f(x1), f(x2)
    while right - left > tol:
        if y1 < y2:
            left, x1, y1 = x1, x2, y2
            x2 = left + ratio * (right - left)
            y2 = f(x2)
        else:
            right, x2, y2 = x2, x1, y1
            x1 = right - ratio * (right - left)
            y1 = f(x1)
    x = 0.5 * (left + right)
    return x, f(x)

def concentration(n, epsilon):
    def interval_mass(x):
        return cdf(x + epsilon) ** n - cdf(x) ** n
    return golden_max(interval_mass)

print("P012 finite iid standard-Gaussian maxima: numerical check only")
for n in SIZES:
    a = expected_max(n)
    for epsilon in EPSILONS:
        center, mass = concentration(n, epsilon)
        bound = 4.0 * epsilon * (a + 1.0)
        print(f"n={n:3d}, eps={epsilon:.3f}, E[max]={a:.9f}, maximizing-left-end~{center:.6f}, interval-mass={mass:.9f}, theorem-rhs={bound:.9f}, satisfied={mass <= bound + 1e-10}")
