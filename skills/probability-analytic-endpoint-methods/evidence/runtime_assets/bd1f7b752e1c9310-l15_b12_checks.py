"""Finite local checks for the L15_B12 source cards; not proofs of the papers."""
import json
import math
from pathlib import Path

# Exact parameter identities and numerical constants appearing in Bañuelos.
martingale_checks = []
for p in (4 / 3, 2.0, 4.0):
    p_star = max(p, p / (p - 1))
    cot_constant = 1.0 / math.tan(math.pi / (2 * p_star))
    comparison = (math.tan(math.pi / (2 * p)) if p <= 2 else 1.0 / math.tan(math.pi / (2 * p)))
    martingale_checks.append({
        "p": p,
        "p_star": p_star,
        "p_star_minus_1": p_star - 1,
        "orthogonal_cot_constant": cot_constant,
        "dual_identity_comparison": comparison,
        "identity_abs_error": abs(cot_constant - comparison),
    })

# Check that a norm-bound factor c becomes c^p in the p-th moment difference.
norm_moment_checks = []
for c, p in ((2.0, 2), (2.0, 3), (1.5, 4)):
    moment_coefficient = c ** p
    recovered_norm_factor = moment_coefficient ** (1.0 / p)
    norm_moment_checks.append({
        "norm_factor_c": c,
        "p": p,
        "moment_coefficient_c_to_p": moment_coefficient,
        "recovered_norm_factor": recovered_norm_factor,
        "absolute_error": abs(recovered_norm_factor-c),
    })

# Check the source-reported numerical approximation to D1 against its displayed formula.
# beta(2) is the Catalan constant; use the source-printed approximation.
catalan_source_approx = 0.9159655
d1_from_displayed_formula = math.pi ** 2 / (8 * catalan_source_approx)
d1_source_printed_approx = 1.328434313301

# Finite counterexample to any universal weak-L1 -> weak-L1 contraction claim
# for conditional expectation: f_N(x)=x^{-1} 1_[1/N,1] on [0,1],
# and conditioning on the trivial sigma-field.
N = 256
input_weak_l1_quasinorm = 1.0 - 1.0 / N  # sup_lambda lambda |{f_N>lambda}|
conditional_mean = math.log(N)
output_weak_l1_quasinorm = conditional_mean  # constant on a unit-measure space

# Summability mechanism in Hytönen: representation decay 2^{-m alpha/2}
# and testing growth 2^{m gamma N/2} times u*v. For one valid example
# N=1, alpha=1, gamma=alpha/(2(N+alpha))=1/4, grouped coefficient is
# m^3 2^{-m delta}, delta=alpha/2-gamma*N/2=3/8.
dimension = 1
alpha = 1.0
gamma = alpha / (2 * (dimension + alpha))
delta = alpha / 2 - gamma * dimension / 2
partial = sum((m ** 3) * (2.0 ** (-delta * m)) for m in range(1, 101))

result = {
    "date": "2026-11-14",
    "runtime": "Python 3 standard library, math",
    "scope": "Finite arithmetic/numerical checks only; no universal theorem is proved or independently re-proved.",
    "AEP-026": {
        "orthogonal_constant_checks": martingale_checks,
        "norm_to_moment_coefficient_checks": norm_moment_checks,
        "D1_source_decimal_check": {
            "source_equation": "D1=pi^2/(8 beta(2))",
            "source_printed_beta2_approx": catalan_source_approx,
            "source_printed_D1_approx": d1_source_printed_approx,
            "formula_evaluated_from_printed_beta2": d1_from_displayed_formula,
            "absolute_discrepancy": abs(d1_from_displayed_formula-d1_source_printed_approx),
            "meaning": "The source formula plus its printed Catalan approximation evaluates to about 1.346885, not the source-printed 1.328434; preserve the formula and flag the decimal inconsistency, without revising the theorem statement.",
        },
        "weak_L1_conditional_expectation_example": {
            "space": "([0,1], Lebesgue measure)",
            "N": N,
            "input": "f_N(x)=x^(-1) 1_[1/N,1](x)",
            "input_weak_L1_quasinorm_exact": input_weak_l1_quasinorm,
            "conditional_sigma_field": "trivial",
            "conditional_expectation_constant": conditional_mean,
            "output_weak_L1_quasinorm_exact": output_weak_l1_quasinorm,
            "ratio_output_to_input": output_weak_l1_quasinorm / input_weak_l1_quasinorm,
            "meaning": "A weak-L1 bound on a martingale-transform output cannot simply be passed through conditional expectation as a weak-L1 operator bound; this finite N example is illustrative, while N can be increased without bound.",
        },
    },
    "AEP-040": {
        "dimension": dimension,
        "kernel_Holder_alpha": alpha,
        "source_gamma": gamma,
        "representation_decay_exponent_alpha_over_2": alpha / 2,
        "weighted_testing_growth_exponent_gamma_N_over_2": gamma * dimension / 2,
        "net_decay_exponent_delta": delta,
        "strict_source_inequality_alpha_over_2_minus_gamma_N_over_2_gt_alpha_over_4": delta > alpha / 4,
        "grouped_uv_sum_first_100_levels": partial,
        "grouping_identity": "For max(u,v)=m and nonnegative integer u,v, sum u*v over that level is m^3; the resulting series is sum_m m^3 2^(-delta*m).",
    },
}
out = Path(__file__).with_name("l15_b12_checks.json")
out.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(out)
print(json.dumps(result, indent=2, ensure_ascii=False))
