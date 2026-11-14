"""Exact/symbolic audit of the printed MDP Corollary 2.2 scale conditions.

This checks the Rademacher counterexamples against the displayed A1/A2
conditions and records the algebraic main-tail sufficient scaling.  The script
is a finite/symbolic consistency check; the universal implication from the
main theorem's tail estimate to an MDP is explained separately in the card.
"""
from pathlib import Path
import json
import sympy as sp

n = sp.symbols("n", integer=True, positive=True)
k = sp.symbols("k", integer=True, positive=True)
eps = 1 / sp.sqrt(n)
delta = sp.exp(-n)
gamma = 1 / sp.sqrt(n)
B = sp.sqrt(n)
rho = sp.Integer(1)
a = n

# P027: for even k, |E[(R/sqrt(n))^k]| = n^{-k/2};
# the (A1) right-hand side is (k!/2)*eps^(k-2)*(1/n).
p027_even_ratio = sp.simplify((sp.factorial(k) / 2 * eps ** (k - 2) / n) / (n ** (-k / 2)))
# For k=2,4,6 the exact coefficient ratio is k!/2 >= 1; odd moments vanish.
p027_even_examples = {
    str(j): str(sp.simplify((sp.factorial(j) / 2 * eps ** (j - 2) / n) / (n ** (-j / 2))))
    for j in (2, 4, 6, 8)
}

# P028: rho=1, E|R|^3=E R^2=1 and (gamma*B)^rho=1.
p028_a2_lhs = sp.Integer(1)
p028_a2_rhs = sp.simplify((gamma * B) ** rho * sp.Integer(1))

# Both predictable brackets are exact, so the A2/A1 concentration event is empty.
p027_bracket = sp.simplify(n * (1 / n))
p028_bracket = sp.simplify(n * 1)
p027_support_over_a = sp.simplify((n / sp.sqrt(n)) / a)
p028_support_over_a = sp.simplify((n / sp.sqrt(n)) / a)
printed_min_product = sp.simplify(a * sp.Min(eps, delta))

result = {
    "method": "SymPy exact/symbolic checks; not a substitute for source reading or a general theorem proof",
    "P027": {
        "increments": "xi_i=R_i/sqrt(n), natural filtration",
        "epsilon": str(eps),
        "A1_even_k_rhs_over_lhs": "k!/2 >= 1 for every even integer k>=2; odd conditional moments are zero",
        "A1_even_examples": p027_even_examples,
        "bracket": str(p027_bracket),
        "A2_event_probability": 0,
        "delta": str(delta),
    },
    "P028": {
        "increments": "X_i=R_i, natural filtration",
        "rho": 1,
        "B": str(B),
        "gamma": str(gamma),
        "A2_moment_lhs": str(p028_a2_lhs),
        "A2_moment_rhs": str(p028_a2_rhs),
        "bracket": str(p028_bracket),
        "A1_event_probability": 0,
        "delta": str(delta),
    },
    "both": {
        "printed_min_product": "n*exp(-n) -> 0 for n>=1",
        "support_bound_for_normalized_statistic_divided_by_a": str(p027_support_over_a),
        "open_set": "(1,2)",
        "probability": 0,
        "required_Gaussian_MDP_lower_bound": "-1/2",
        "actual_log_probability_limit": "-infinity",
        "eventually_a_max_parameter": "a*max(epsilon,delta) does not tend to 0; it equals sqrt(n) for all sufficiently large n",
    },
    "safe_scale_from_main_tail_range": {
        "P027": "a*max(epsilon,delta)->0",
        "P028": "a*max(gamma,delta)->0",
        "status": "derived sufficient condition, conditional on the respective main tail theorem; distinct from printed Corollary 2.2",
    },
}

out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps(result, indent=2, ensure_ascii=False))
