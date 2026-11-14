"""Exact two-state audit of Aldous–Fill Lemma 3.29's printed lower side."""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
edge = sp.Rational(1, 1)
edge_star = sp.Rational(1, 2)
loop = sp.Rational(2, 1)
# Weighted random walk: from each vertex, normalize the incident loop and
# connecting-edge conductances. The stationary law is uniform by symmetry.
P = sp.Matrix([[loop / (loop + edge), edge / (loop + edge)],
               [edge / (loop + edge), loop / (loop + edge)]])
P_star = sp.Matrix([[loop / (loop + edge_star), edge_star / (loop + edge_star)],
                    [edge_star / (loop + edge_star), loop / (loop + edge_star)]])
assert P.row_join(sp.ones(2, 1)).shape[0] == 2
assert all(sum(P.row(i)) == 1 for i in range(2))
assert all(sum(P_star.row(i)) == 1 for i in range(2))
assert P == P.T and P_star == P_star.T

def tau2(K):
    vals = [sp.factor(v) for v in K.eigenvals().keys()]
    gap = min((1-v for v in vals if v != 1), key=lambda x: float(x))
    return sp.factor(1/gap)

tau, tau_star = tau2(P), tau2(P_star)
ratio = sp.factor(tau/tau_star)
vertex_ratio = sp.factor((loop+edge)/(loop+edge_star))
edge_ratio = sp.factor(edge/edge_star)
printed_lower = sp.factor(edge_ratio/vertex_ratio)
proof_lower = sp.factor(vertex_ratio/edge_ratio)
printed_upper = proof_lower
assert (P, P_star) == (sp.Matrix([[sp.Rational(2,3), sp.Rational(1,3)],
                                   [sp.Rational(1,3), sp.Rational(2,3)]]),
                      sp.Matrix([[sp.Rational(4,5), sp.Rational(1,5)],
                                 [sp.Rational(1,5), sp.Rational(4,5)]]))
assert (tau, tau_star, ratio) == (sp.Rational(3,2), sp.Rational(5,2), sp.Rational(3,5))
assert printed_lower == sp.Rational(5,3) and proof_lower == ratio == printed_upper
out = {
    "source": "Aldous & Fill, Reversible Markov Chains and Random Walks on Graphs, Lemma 3.29, physical PDF p.93 (proof continues p.94)",
    "source_sha256": "8f9b934111c30b3f8fd29d94a18794d4b86f824b19f7a3c27b1153cdfac08e79",
    "model": "Two states with loop conductance 2 at each state; connecting-edge conductance 1 in P and 1/2 in P_star; loops are excluded from edge extrema but included in vertex weights.",
    "P": [[str(P[i,j]) for j in range(2)] for i in range(2)],
    "P_star": [[str(P_star[i,j]) for j in range(2)] for i in range(2)],
    "stationary_law": ["1/2", "1/2"],
    "relaxation_times": {"tau2": str(tau), "tau2_star": str(tau_star), "ratio": str(ratio)},
    "weights": {"vertex_ratio_w_over_wstar": str(vertex_ratio), "edge_ratio_w_over_wstar": str(edge_ratio)},
    "lemma_3_29_printed_lower": str(printed_lower),
    "proof_derived_lower": str(proof_lower),
    "printed_upper": str(printed_upper),
    "result": "Printed lower 5/3 exceeds actual ratio 3/5; the proof-derived lower and printed upper both equal 3/5 in this example.",
    "scope_limit": "Exact two-state counterexample to the printed lower formula only; the corrected lower follows generally from the displayed proof's comparison for tau2_star and algebraic inversion."
}
(ROOT/'workers/W04/numerical/s002_lemma329_lower_audit.json').write_text(json.dumps(out, ensure_ascii=False, indent=2)+'\n')
print(json.dumps({"tau2": str(tau), "tau2_star": str(tau_star), "ratio": str(ratio),
                  "printed_lower": str(printed_lower), "proof_derived_lower": str(proof_lower)}, indent=2))
