"""Local Python arithmetic for the W15-023/W15-029 reader revisions.

The exponent threshold and all-horizon contradiction are proved analytically
in the cards; numerical values here are supporting checks, not the proofs.
"""
import json
import math
from fractions import Fraction
from pathlib import Path

# The displayed second term in W15-023 Thm. 3 is asymptotic to n^(-2(alpha-1)).
alpha_example = Fraction(11, 10)
second_term_exponent = 2 * (alpha_example - 1)
target_exponent = Fraction(1, 2)
ratio_exponent = target_exponent - second_term_exponent
rate_ratios = {}
for horizon in (10**6, 10**12):
    n = float(horizon)
    rate_ratios[str(horizon)] = {
        "alpha_11_over_10_ratio_second_term_to_target_scale": (
            n ** float(ratio_exponent) / math.sqrt(math.log(n))
        ),
        "alpha_5_over_4_ratio_at_boundary": 1 / math.sqrt(math.log(n)),
    }

# For W15-029 the endpoint ratio is bounded by 2x/(x+1)^2, which tends to zero.
endpoint_ratio_examples = {
    str(x): str(Fraction(2 * x, (x + 1) ** 2)) for x in (1, 16, 2**289)
}

# Two exact blocks for n=3, p=(1/5,4/5,1/2); arm 2 is optimal.
p = [Fraction(1, 5), Fraction(4, 5), Fraction(1, 2)]
T = 1
counts = [1, 0, 0]  # arbitrary initial arm 1
finite_schedule = []
for j in range(1, 3):
    arm = (j - 1) % 3
    endpoint = 2 ** ((T + 1) ** 2)
    counts[arm] += endpoint - T
    expected_regret = sum(
        counts[i] * (max(p) - p[i]) for i in range(3)
    )
    finite_schedule.append(
        {
            "block": j,
            "arm": arm + 1,
            "previous_endpoint": str(T),
            "endpoint": str(endpoint),
            "expected_regret": str(expected_regret),
            "optimal_arm_block": p[arm] == max(p),
            "expected_regret_le_previous_endpoint": (
                bool(expected_regret <= T) if p[arm] == max(p) else None
            ),
        }
    )
    T = endpoint

out = {
    "runtime": "Python standard library: Fraction and math",
    "W15_023": {
        "exact_second_term_exponent_at_alpha_11_over_10": str(second_term_exponent),
        "exact_ratio_exponent_to_sqrt_log_over_sqrt_n": str(ratio_exponent),
        "direct_bound_condition": "2(alpha-1) >= 1/2 iff alpha >= 5/4",
        "finite_rate_ratio_examples": rate_ratios,
        "scope": "Numerical exponent-scale checks only; not a counterexample to the algorithm's claimed rate.",
    },
    "W15_029": {
        "endpoint_bound_examples": endpoint_ratio_examples,
        "finite_three_arm_example": finite_schedule,
        "scope": "Exact finite arithmetic examples only; the all-p proof is stated in the card and R02 adjudication.",
    },
}
assert second_term_exponent == Fraction(1, 5)
assert ratio_exponent == Fraction(3, 10)
assert finite_schedule[1]["optimal_arm_block"]
assert finite_schedule[1]["expected_regret"] == "48/5"
assert finite_schedule[1]["expected_regret_le_previous_endpoint"]
Path(__file__).with_suffix(".out.json").write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps(out, indent=2))
