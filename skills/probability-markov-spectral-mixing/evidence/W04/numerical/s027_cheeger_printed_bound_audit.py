"""Exact audit of Diaconis–Stroock (1991), printed Proposition 6 upper bound.

Uses rational arithmetic and symbolic eigenvalues for a finite reversible,
irreducible, aperiodic four-state kernel. This is source-proof audit evidence,
not an Ising spectral-gap result.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

R = sp.Rational
lam = sp.symbols("lambda")
# Symmetric edge conductances 1/10, 2, 10 on a four-vertex path, and a
# positive self-loop of 1/1000 times each original weighted degree.
q_raw = sp.Matrix([
    [R(1, 10000), R(1, 10), 0, 0],
    [R(1, 10), R(21, 10000), 2, 0],
    [0, 2, R(3, 250), 10],
    [0, 0, 10, R(1, 100)],
])
row_masses = [sum(q_raw.row(i)) for i in range(4)]
total = sum(row_masses)
pi = [sp.factor(x / total) for x in row_masses]
P = sp.diag(*[1 / x for x in row_masses]) * q_raw

# Enumerate all nonempty subsets of stationary mass at most 1/2.
cut_table = []
for mask in range(1, 1 << 4):
    vertices = [i for i in range(4) if (mask >> i) & 1]
    mass = sum(row_masses[i] for i in vertices)
    if mass * 2 > total:
        continue
    complement = [i for i in range(4) if i not in vertices]
    flow = sum(q_raw[i, j] for i in vertices for j in complement)
    ratio = sp.factor(flow / mass)
    cut_table.append({
        "vertices": vertices,
        "stationary_mass": str(sp.factor(mass / total)),
        "unnormalized_row_mass": str(mass),
        "cut_flow_unnormalized": str(flow),
        "flow_over_mass": str(ratio),
    })
h = min(sp.Rational(row["flow_over_mass"]) for row in cut_table)
assert h == R(10000, 11011)

# The no-holding path kernel has eigenvalues ±1, ±sqrt(5/126). The added
# holding probability is exactly 1/1001, so the second-largest eigenvalue is:
beta1 = sp.factor(R(1, 1001) + R(1000, 1001) * sp.sqrt(R(5, 126)))
charpoly = sp.factor(P.charpoly(lam).as_expr())
printed_threshold = sp.factor(1 - h**2)
safe_threshold = sp.factor(1 - h**2 / 2)
violation = sp.factor(beta1 - printed_threshold)
assert violation > 0
assert 1 - beta1 >= h**2 / 2

result = {
    "source": "Diaconis & Stroock (1991), Proposition 6, printed p.52 / local scan physical p.18",
    "model": "Four-state path with symmetric edge conductances (1/10, 2, 10), plus self-loop conductance 1/1000 times each original weighted degree; normalize q_raw by its total to obtain pi(x)P(x,y).",
    "q_raw": [[str(q_raw[i, j]) for j in range(4)] for i in range(4)],
    "normalization_total": str(total),
    "pi": [str(x) for x in pi],
    "transition_matrix": [[str(P[i, j]) for j in range(4)] for i in range(4)],
    "irreducible": True,
    "aperiodic": True,
    "eigenvalue_characteristic_polynomial": str(charpoly),
    "second_largest_eigenvalue_exact": str(beta1),
    "second_largest_eigenvalue_decimal": str(sp.N(beta1, 16)),
    "conductance_cut_enumeration": cut_table,
    "h_exact": str(h),
    "h_decimal": str(sp.N(h, 16)),
    "printed_upper_bound_threshold_1_minus_h2": str(printed_threshold),
    "printed_bound_violation_beta1_minus_threshold_exact": str(violation),
    "printed_bound_violation_decimal": str(sp.N(violation, 16)),
    "safe_threshold_from_source_displayed_proof_1_minus_h2_over_2": str(safe_threshold),
    "safe_bound_holds_exactly": bool(1 - beta1 >= h**2 / 2),
    "conclusion": "Exact counterexample to the printed Proposition 6 upper inequality beta_1 <= 1-h^2 as transcribed from the scanned page; the paper's displayed short proof (equation (3.4), physical p.24) supports the weaker beta_1 <= 1-h^2/2. Use the weaker proved form pending independent review; this does not affect the canonical-path or lower Cheeger statements.",
    "evidence_type": "exact rational cut enumeration plus exact algebraic eigenvalue comparison; not floating-point-only evidence",
}
out = Path(__file__).with_name("s027_cheeger_printed_bound_audit.json")
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({k: result[k] for k in ["h_exact", "second_largest_eigenvalue_exact", "printed_upper_bound_threshold_1_minus_h2", "printed_bound_violation_beta1_minus_threshold_exact", "safe_threshold_from_source_displayed_proof_1_minus_h2_over_2", "conclusion"]}, ensure_ascii=False, indent=2))
