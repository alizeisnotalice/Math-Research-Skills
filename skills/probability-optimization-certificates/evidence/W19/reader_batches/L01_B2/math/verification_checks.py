"""Exact local checks supporting W19 L01_B2 source cards; not theorem proofs."""
from __future__ import annotations

import json
from pathlib import Path
import sympy as sp


def main() -> None:
    results = {}

    # S016: algebraic equivalence of each ball constraint and its lifted linear bound.
    x = sp.symbols("x0:3")
    c = sp.symbols("c0:3")
    rho = sp.symbols("rho", real=True)
    original = sum((x[i] - c[i]) ** 2 for i in range(3)) - rho**2
    lifted = sum(x[i] ** 2 for i in range(3)) - (
        rho**2 - sum(c[i] ** 2 for i in range(3)) + 2 * sum(c[i] * x[i] for i in range(3))
    )
    diff = sp.expand(original - lifted)
    assert diff == 0
    results["S016_ball_linearization"] = {
        "symbolic_difference": str(diff),
        "identity_holds": diff == 0,
        "interpretation": "||x-c||^2 <= rho^2 iff ||x||^2 <= rho^2-||c||^2+2c^T x."
    }

    # S018: build M_1(f_A y) directly from the exponential moments y_(a,b)=a!b!.
    exponents = [(0, 0), (1, 0), (0, 1)]
    f_terms = [((2, 0), sp.Integer(1)), ((0, 2), sp.Integer(1))]

    def moment(alpha: tuple[int, int]) -> sp.Expr:
        return sp.factorial(alpha[0]) * sp.factorial(alpha[1])

    entries = []
    for alpha in exponents:
        row = []
        for beta in exponents:
            val = 0
            for gamma, coeff in f_terms:
                total = (alpha[0] + beta[0] + gamma[0], alpha[1] + beta[1] + gamma[1])
                val += coeff * moment(total)
            row.append(sp.simplify(val))
        entries.append(row)
    moment_matrix = sp.Matrix(entries)
    expected = sp.Matrix([[4, 8, 8], [8, 28, 12], [8, 12, 28]])
    assert moment_matrix == expected
    principal_minors = []
    for k in range(1, 4):
        for idx in __import__("itertools").combinations(range(3), k):
            principal_minors.append(sp.factor(moment_matrix.extract(idx, idx).det()))
    assert all(m > 0 for m in principal_minors)
    results["S018_localizing_matrix"] = {
        "matrix": [[str(moment_matrix[i, j]) for j in range(3)] for i in range(3)],
        "principal_minors": [str(m) for m in principal_minors],
        "matches_rendered_formula_2_15_up_to_factor_2": True,
        "interpretation": "One exact n=2,d=1,A=I coefficient check only."
    }

    # M0349: exact scalar check that a pointwise feasible-point cap can make the
    # fixed trial expression exceed the true optimum. The source theorem prints
    # an infimum but does not name its index set in that theorem sentence.
    x2 = sp.symbols("x2", real=True)
    objective_on_feasible_set = -100 * x2  # x1=1-x2, x2 in [0,1]
    optimum = sp.minimum(objective_on_feasible_set, x2, sp.Interval(0, 1))
    known_feasible = (sp.Integer(1), sp.Integer(0))
    xbar = known_feasible
    y = sp.Integer(0)
    C = (sp.Integer(0), sp.Integer(-100))
    A = (sp.Integer(1), sp.Integer(1))
    D = tuple(C[j] - y * A[j] for j in range(2))
    d = D  # exact minimum eigenvalues of scalar blocks
    rhs = sum(sp.Integer(1) * min(sp.Integer(0), d[j]) * xbar[j] for j in range(2))
    assert known_feasible[0] + known_feasible[1] == 1
    assert optimum == -100
    assert D == (0, -100) and d == (0, -100)
    assert rhs == 0 and optimum < rhs
    results["M0349_theorem_14_2_fixed_trial_expression_check"] = {
        "primal": "minimize 0*x1-100*x2 subject to x1,x2>=0 and x1+x2=1",
        "true_optimum": str(optimum),
        "known_feasible_point": [str(v) for v in known_feasible],
        "pointwise_caps": [str(v) for v in xbar],
        "trial_dual_y": str(y),
        "D_scalar_blocks": [str(v) for v in D],
        "valid_lower_eigenvalue_bounds_d": [str(v) for v in d],
        "fixed_trial_expression_from_14_8": str(rhs),
        "fixed_trial_expression_is_a_lower_bound": bool(optimum >= rhs),
        "printed_infimum_domain_specified_in_theorem_sentence": False,
        "interpretation": "The feasible-point cap (1,0) does not cap the other feasible points. Thus the fixed trial expression 0 is not itself a lower bound for p*=-100. The source prints an infimum in (14.8), but the theorem sentence does not specify its index set; this check does not refute an independently defined infimum over a domain that enforces suitable uniform caps."
    }

    out = Path(__file__).with_suffix(".json")
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
