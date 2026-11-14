"""Exact two-state reversible-chain arithmetic sanity check.

This verifies elementary quantities for one lazy kernel only. It is not a proof
of Paulin's general concentration/mixing theorem or of any Ising monotonicity.
"""
from fractions import Fraction
import json
from pathlib import Path

import sympy as sp

p = sp.Rational(1, 8)
P = sp.Matrix([[1 - p, p], [p, 1 - p]])
pi = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])
q0 = sp.Matrix([[1, 0]])

assert all(sum(P.row(i)) == 1 for i in range(2))
assert pi * P == pi
assert pi[0] * P[0, 1] == pi[1] * P[1, 0]

eigenvalues = sorted((sp.simplify(x) for x in P.eigenvals().keys()), key=lambda x: float(x))
assert eigenvalues == [sp.Rational(3, 4), sp.Integer(1)]
poincare_gap = sp.simplify(1 - eigenvalues[0])
absolute_gap = sp.simplify(1 - max(abs(x) for x in eigenvalues if x != 1))
assert poincare_gap == absolute_gap == sp.Rational(1, 4)

rows = []
for n in range(13):
    qn = q0 * P**n
    tv = sp.simplify(sum(abs(qn[0, i] - pi[0, i]) for i in range(2)) / 2)
    formula = sp.Rational(1, 2) * (sp.Rational(3, 4) ** n)
    assert tv == formula
    rows.append({"n": n, "tv_exact": str(tv), "formula_exact": str(formula), "equal": True})

result = {
    "status": "passed_exact_arithmetic",
    "kernel": [[str(x) for x in P.row(i)] for i in range(2)],
    "stationary_distribution": [str(x) for x in pi],
    "eigenvalues": [str(x) for x in eigenvalues],
    "poincare_gap": str(poincare_gap),
    "absolute_gap": str(absolute_gap),
    "tv_identity": "TV(delta_0 P^n, pi) = (3/4)^n / 2 for this p=1/8 kernel",
    "checks": rows,
    "scope_limit": "One two-state lazy reversible kernel; arithmetic sanity check only, not a proof of a general Markov-chain theorem or Ising edge-gap monotonicity.",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "checks"}, indent=2))
