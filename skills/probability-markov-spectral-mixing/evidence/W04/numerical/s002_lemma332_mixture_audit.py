"""Exact audit of the mixture remark following Aldous–Fill Lemma 3.32."""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
P = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)],
               [sp.Rational(1, 2), sp.Rational(1, 2)]])
P_star = sp.Matrix([[sp.Rational(9, 10), sp.Rational(1, 10)],
                    [sp.Rational(1, 10), sp.Rational(9, 10)]])
delta = sp.Rational(4, 5)
Q = (P - delta * P_star) / (1 - delta)
uniform = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)]])

assert all(sum(P.row(i)) == 1 for i in range(2))
assert all(sum(P_star.row(i)) == 1 for i in range(2))
assert P == P.T and P_star == P_star.T
assert uniform * P == uniform and uniform * P_star == uniform
assert P[0, 1] >= delta * P_star[0, 1]
assert P[1, 0] >= delta * P_star[1, 0]
assert Q.row(0) == sp.Matrix([[sp.Rational(-11, 10), sp.Rational(21, 10)]])
assert Q.row(1) == sp.Matrix([[sp.Rational(21, 10), sp.Rational(-11, 10)]])
assert all(sum(Q.row(i)) == 1 for i in range(2))
assert Q[0, 0] < 0 and Q[1, 1] < 0

def gap(K):
    vals = [sp.factor(v) for v in K.eigenvals().keys()]
    return min((1 - v for v in vals if v != 1), key=lambda x: float(x))

gap_P = gap(P)
gap_star = gap(P_star)
tau_P = sp.factor(1 / gap_P)
tau_star = sp.factor(1 / gap_star)
assert tau_P == 1 and tau_star == 5
assert tau_P <= delta**-1 * tau_star

out = {
    "source": "Aldous & Fill, Reversible Markov Chains and Random Walks on Graphs, Lemma 3.32 and following remark, physical PDF p.94",
    "source_sha256": "8f9b934111c30b3f8fd29d94a18794d4b86f824b19f7a3c27b1153cdfac08e79",
    "P": [[str(P[i, j]) for j in range(2)] for i in range(2)],
    "P_star": [[str(P_star[i, j]) for j in range(2)] for i in range(2)],
    "common_stationary_law": ["1/2", "1/2"],
    "delta": str(delta),
    "off_diagonal_domination_holds": True,
    "Q_from_printed_mixture": [[str(Q[i, j]) for j in range(2)] for i in range(2)],
    "Q_row_sums": [str(sum(Q.row(i))) for i in range(2)],
    "Q_nonnegative": False,
    "relaxation_times": {"tau2_P": str(tau_P), "tau2_P_star": str(tau_star)},
    "lemma_bound": "tau2(P) <= delta^(-1) tau2(P_star)",
    "lemma_bound_check": f"1 <= {sp.factor(delta**-1 * tau_star)}",
    "result": "The lemma's off-diagonal hypothesis and conclusion hold in this example, but the following remark's proposed Q has negative diagonal entries and is not a Markov kernel.",
    "scope_limit": "Exact audit of the mixture interpretation only; it does not refute Lemma 3.32. The direct Dirichlet-form comparison needs only the stated off-diagonal domination and common stationary law."
}
(ROOT / "workers/W04/numerical/s002_lemma332_mixture_audit.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=2) + "\n"
)
print(json.dumps({"Q": out["Q_from_printed_mixture"], "Q_nonnegative": out["Q_nonnegative"],
                  "tau2_P": str(tau_P), "tau2_P_star": str(tau_star),
                  "lemma_bound_check": out["lemma_bound_check"]}, indent=2))
