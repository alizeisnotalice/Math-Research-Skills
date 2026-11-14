"""Finite/symbolic checks for W22 batch 2; calculations are not proofs."""
from fractions import Fraction
from math import pi
from pathlib import Path
import sys

import sympy as sp

OUT = Path(__file__).with_suffix(".txt")

lines = [
    "W22 batch 2 local mathematical checks (not proofs)",
    f"Runtime: Python {sys.version.split()[0]}; SymPy {sp.__version__}; fractions for exact rational identities; Python float for finite-chain decimals.",
    "Source equations: RT005 (1.1)–(1.3), (2.7)–(2.15); RT012 (3.2)–(3.5), (5.12), (3.3).",
    "",
]

# RT005: exact row normalization and finite-n occupation probabilities.
def harmonic_fraction(k):
    return sum((Fraction(1, j) for j in range(1, k + 1)), Fraction(0))

for j in range(2, 40):
    hj = harmonic_fraction(j - 1)
    row = sum((Fraction(1, (j - i)) / hj for i in range(1, j)), Fraction(0))
    assert row == 1
lines.append("RT005 transition p(j,i)=1/[(j-i)h_(j-1)] has exact rational row sum 1 for j=2,...,39.")

def occupation_from(N):
    # Propagate the probability of visiting each state in the strictly decreasing chain.
    mass = [0.0] * (N + 1)
    mass[N] = 1.0
    h = [0.0] * (N + 1)
    for k in range(1, N + 1):
        h[k] = h[k - 1] + 1.0 / k
    for j in range(N, 1, -1):
        for i in range(1, j):
            mass[i] += mass[j] / ((j - i) * h[j - 1])
    return mass

lines.append("RT005 finite-n occupation values versus Theorem 1.1 limits 6 h_(i-1)/(pi^2(i-1)):")
for N in (100, 300, 1000):
    occ = occupation_from(N)
    vals = []
    for i in (2, 3, 5, 10):
        limit = 6.0 * sum(1.0 / k for k in range(1, i)) / (pi * pi * (i - 1))
        vals.append(f"i={i}: a({N},{i})={occ[i]:.9f}, limit={limit:.9f}, diff={occ[i]-limit:+.3e}")
    lines.append(f" N={N}: " + "; ".join(vals))
lines.append("Finite values illustrate the stated limit and the recurrence only; they do not prove convergence or the coupling argument.")
lines.append("")

# RT012: reproduce the first second-order omega* constants from the exact recursion.
omega = {(1, 0): 1, (0, 1): 1}

def om(k, l):
    if (k, l) in omega:
        return omega[(k, l)]
    if k < 0 or l < 0:
        return 0
    total = 2 * (3 * k + 5 * l - 4) * om(k - 1, l)
    total += 2 * (3 * k + 5 * l - 6) * (3 * k + 5 * l - 4) * om(k, l - 1)
    for i in range(k + 1):
        for j in range(l + 1):
            if 0 < i + j < k + l:
                total += om(i, j) * om(k - i, l - j)
    omega[(k, l)] = total
    return total

for kl in ((2, 0), (1, 1), (0, 2)):
    om(*kl)
assert (omega[(2, 0)], omega[(1, 1)], omega[(0, 2)]) == (5, 26, 49)
lines.append(f"RT012 recursion (3.4) gives omega*20={omega[(2,0)]}, omega*11={omega[(1,1)]}, omega*02={omega[(0,2)]}; these agree with the rendered PDF p. 5 table/formulas.")

def E_moment(k, l):
    return sp.factorial(k) * sp.factorial(l) * sp.sqrt(sp.pi) * om(k, l) / (
        sp.Integer(2) ** sp.Rational(5 * k + 7 * l - 4, 2)
        * sp.gamma(sp.Rational(3 * k + 5 * l - 1, 2))
    )

checks = {
    "E[xi]": (E_moment(1, 0), sp.sqrt(sp.pi / 2)),
    "E[eta]": (E_moment(0, 1), sp.sqrt(sp.pi / 8)),
    "E[xi^2]": (E_moment(2, 0), sp.Rational(5, 3)),
    "E[xi eta]": (E_moment(1, 1), sp.Rational(13, 15)),
    "E[eta^2]": (E_moment(0, 2), sp.Rational(7, 15)),
}
for name, (lhs, rhs) in checks.items():
    assert sp.simplify(lhs - rhs) == 0, (name, lhs, rhs)
lines.append("SymPy exact simplification of the printed moment formula (3.3) reproduces E[xi]=sqrt(pi/2), E[eta]=sqrt(pi/8), E[xi^2]=5/3, E[xi eta]=13/15, E[eta^2]=7/15.")
assert sp.simplify(E_moment(2, 0) - 2 * E_moment(1, 1) + E_moment(0, 2) - sp.Rational(2, 5)) == 0
lines.append("Using zeta=xi-eta, the exact identity E[zeta^2]=E[xi^2]-2E[xi eta]+E[eta^2]=2/5 follows; hence the source's Theorem 3.4 gives EW(T_n)~sqrt(pi/(8 sigma^2))*n^(5/2) and EW(T_n)^2~2/(5 sigma^2)*n^5.")
lines.append("These checks verify algebraic substitutions into the printed recursion/formula and do not prove Brownian-excursion convergence, uniform integrability, or the limit theorem.")

OUT.write_text("\n".join(lines) + "\n")
print(OUT.read_text())
