#!/usr/bin/env python3
"""Numerical consistency check for the finite-candidate Hoeffding formula."""
import json
import math
from pathlib import Path

n = 2
N = 10_000
M = 100
delta = 0.05
epsilon = math.sqrt(2 * math.log(2 * M / delta) / N)
union_bound = 2 * M * math.exp(-N * epsilon**2 / 2)
rescaled_error = (2 * math.pi) ** n * epsilon
result = {
    "check_type": "numerical_formula_consistency_only",
    "formal_dimension_n": n,
    "validation_sample_count_N": N,
    "candidate_count_upper_bound_M": M,
    "confidence_delta": delta,
    "mean_scale_epsilon": epsilon,
    "union_bound_at_epsilon": union_bound,
    "target_delta": delta,
    "absolute_union_bound_difference": abs(union_bound - delta),
    "integral_scale_multiplier": (2 * math.pi) ** n,
    "integral_scale_error_threshold": rescaled_error,
    "scope": "Finite pre-fixed candidate list only; no all-partition or optimizer claim.",
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
