"""Exact finite arithmetic checks for B18 examples.

The output verifies arithmetic in displayed examples; it is not a proof of any
general convergence theorem.
"""
from fractions import Fraction
import json
from pathlib import Path

out = {}

# B18-002 Example 3.2: keep the source's printed +1/2 separate from the
# value obtained by direct substitution.  For n>=2 the first branch has
# Lebesgue mass 1/2, density 1/n, and f_n=-n; the other branch has f_n>=-1.
sign_rows = []
for K in (Fraction(3, 2), Fraction(2), Fraction(5, 2), Fraction(4)):
    for n in range(1, 13):
        if n >= K:
            first_branch_tail_integral = Fraction(-n) * Fraction(1, n) * Fraction(1, 2)
        else:
            first_branch_tail_integral = Fraction(0)
        # For K>1, the second branch f_n=-1/(2-1/n) is at least -1,
        # so it contributes no points to {f_n <= -K}.
        second_branch_tail_integral = Fraction(0)
        sign_rows.append({
            "K": str(K),
            "n": n,
            "source_printed_all_n_infimum": "+1/2",
            "computed_first_branch_tail_integral": str(first_branch_tail_integral),
            "computed_second_branch_tail_integral": str(second_branch_tail_integral),
            "computed_total_tail_integral": str(first_branch_tail_integral + second_branch_tail_integral),
        })
out["B18-002_example_3_2_printed_vs_derived_sign"] = {
    "source_printed_value": "+1/2 (PDF p.13; transcribed unchanged)",
    "derived_identity": "for every K>1, terms with n>=K have tail integral (-n)*(1/n)*(1/2)=-1/2 and all other terms are 0; hence inf over all n is -1/2",
    "sampled_exact_fraction_rows": sign_rows,
    "scope_note": "The rows verify selected finite (K,n) substitutions with exact Fraction arithmetic. The all-n conclusion follows from the source's two-branch definitions and the stated symbolic calculation; the source display remains +1/2 and is not altered.",
}

# B18-001: mu_n=delta_(1/n), mu=delta_0, f_n=f=1_{0}.
# Pointwise liminf violates classical Fatou, while the two-parameter envelope
# at 0 is zero: choose s'_n=1/(2n), where f_n(s'_n)=0.
weak_rows = []
for n in (1, 2, 10, 100, 1000):
    weak_rows.append(
        {
            "n": n,
            "pointwise_left_integral": 1,
            "right_integral": 0,
            "test_x_integral_under_mu_n": Fraction(1, n),
            "test_x_integral_under_mu": 0,
            "approaching_point": Fraction(1, 2 * n),
            "f_n_at_approaching_point": 0,
        }
    )
out["B18-001_point_mass_example"] = {
    "identity": "pointwise-liminf left=1 > 0=liminf integral; joint (n,s'->s) lower envelope at 0=0",
    "rows": [
        {k: (str(v) if isinstance(v, Fraction) else v) for k, v in row.items()}
        for row in weak_rows
    ],
    "scope_note": "Exact evaluation of the paper's counterexample; weak convergence of delta_(1/n) to delta_0 follows analytically by continuity of test functions.",
}

# B18-002: Example 3.3. On each dyadic interval, g_n=1/2 on the first half
# and 3/2 on the second; mu_n=g_n*Lebesgue and f_n=1/g_n.
# Midpoint quadrature on the exact dyadic partition integrates these
# piecewise-constant functions exactly.
tv_rows = []
for n in range(1, 9):
    pieces = 2 ** (n + 1)
    g_values = [Fraction(1, 2) if j % 2 == 0 else Fraction(3, 2) for j in range(pieces)]
    f_values = [1 / g for g in g_values]
    mu_total = sum(g_values, Fraction(0)) / pieces
    integral_fn_dmun = sum(
        (f * g for f, g in zip(f_values, g_values)), Fraction(0)
    ) / pieces
    bad_event_mass = Fraction(sum(1 for f in f_values if f <= Fraction(2, 3)), pieces)
    tv_norm = sum((abs(g - 1) for g in g_values), Fraction(0)) / pieces
    half_set_discrepancy = Fraction(1, 4)
    tv_rows.append(
        {
            "n": n,
            "pieces": pieces,
            "mu_n_total": str(mu_total),
            "integral_f_n_dmu_n": str(integral_fn_dmun),
            "integral_f_dmu": "1",
            "mu_of_f_n_le_2_3": str(bad_event_mass),
            "total_variation_bounded_test_norm": str(tv_norm),
            "measure_discrepancy_on_g_equals_1_2_set": str(half_set_discrepancy),
        }
    )
out["B18-002_example_3_3"] = {
    "rows": tv_rows,
    "identity": "all rows give mu_n(S)=1, int f_n dmu_n=int 1 dmu=1, mu{f_n<=2/3}=1/2, and bounded-test TV norm=1/2",
    "scope_note": "Exact dyadic-partition arithmetic only; the paper supplies the separate approximation argument establishing setwise convergence for every Borel set.",
}

# B18-003: Example 6.1. mu_n has density n on [0,1/n], mu=delta_0,
# f_n(s)=min(ns,1), and f=1_{(0,1]}. Integrate the source formulas exactly.
mct_rows = []
for n in (1, 2, 10, 100, 1000):
    integral = Fraction(1, 2)
    test_x = Fraction(1, 2 * n)
    mct_rows.append(
        {
            "n": n,
            "integral_f_n_dmu_n": str(integral),
            "integral_f_dmu": "0",
            "continuous_test_x_under_mu_n": str(test_x),
            "continuous_test_x_under_mu": "0",
        }
    )
out["B18-003_example_6_1"] = {
    "rows": mct_rows,
    "identity": "the varying-measure integrals remain 1/2 although the limit integral is 0; the example violates the required upper-semicontinuity of f",
    "scope_note": "Exact integration of the displayed piecewise-linear density/function; weak convergence is justified analytically by the support shrinking to 0.",
}

out["interpretation"] = (
    "All arithmetic is an example-level consistency check. It verifies neither "
    "weak/setwise convergence for arbitrary test sets nor any theorem."
)

output = Path(__file__).with_suffix(".json")
output.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(output)
