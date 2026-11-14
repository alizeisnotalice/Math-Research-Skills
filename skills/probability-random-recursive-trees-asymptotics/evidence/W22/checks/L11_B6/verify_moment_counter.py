#!/usr/bin/env python3
"""Exact finite-n check for the RT015 alpha=0 root-degree counterexample.

This verifies finite Bernoulli moment identities numerically/rationally; the
proof of the limiting bound is the analytic cumulant inequality in RT015.md.
"""
from fractions import Fraction
import json
from pathlib import Path

def record(n: int) -> dict:
    # At insertion j+1, the new node attaches to the root with probability 1/j.
    ps = [Fraction(1, j) for j in range(1, n)]
    mu = sum(ps, Fraction(0))
    variance = sum((p * (1-p) for p in ps), Fraction(0))
    kappa3 = sum((p * (1-p) * (1-2*p) for p in ps), Fraction(0))
    third_raw = mu**3 + 3*mu*variance + kappa3
    normalized = third_raw / mu**3
    error = abs(normalized - 1)
    bound = Fraction(3, 1)/mu + Fraction(1, 1)/mu**2
    return {
        "n": n,
        "mu_exact": str(mu),
        "variance_exact": str(variance),
        "third_cumulant_exact": str(kappa3),
        "normalized_third_moment_exact": str(normalized),
        "absolute_error_exact": str(error),
        "cumulant_bound_exact": str(bound),
        "bound_holds": error <= bound,
        "absolute_error_decimal": float(error),
        "bound_decimal": float(bound),
    }

rows = [record(n) for n in (2, 5, 20, 100)]
assert all(row["bound_holds"] for row in rows)
out = {
    "purpose": "finite exact-arithmetic consistency check only; not a proof of the asymptotic theorem",
    "model": "D_n=sum_{j=1}^{n-1} Bernoulli(1/j), independent",
    "identity": "E[D^3]=mu^3+3*mu*Var(D)+kappa_3(D)",
    "analytic_bound": "|E[(D/mu)^3]-1| <= 3/mu + 1/mu^2",
    "rows": rows,
}
Path(__file__).with_name("verify_moment_counter.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
