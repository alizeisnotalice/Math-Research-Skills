"""Exact small-n Walsh enumeration for the Fourier-support examples in W10.

All transforms are kept as integer numerators: for f in {0,1},
    hat f(S) = numerator[S] / 2**n.
This verifies finite examples only; it is not evidence for an asymptotic bound.
"""
from __future__ import annotations

import json
from pathlib import Path


def walsh_numerators(values: list[int]) -> list[int]:
    a = values[:]
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return a


def transformed_truth(mask: int, n: int) -> list[int]:
    return [(mask >> x) & 1 for x in range(1 << n)]


def depends_on_coordinate(values: list[int], n: int, i: int) -> bool:
    bit = 1 << i
    return any(values[x] != values[x ^ bit] for x in range(1 << n) if not (x & bit))


def gf2_rank(masks: list[int]) -> int:
    """Return the dimension of the span of coordinate masks over F_2."""
    pivots: dict[int, int] = {}
    for mask in masks:
        value = mask
        while value:
            pivot = value.bit_length() - 1
            if pivot in pivots:
                value ^= pivots[pivot]
            else:
                pivots[pivot] = value
                break
    return len(pivots)


rows = []
for n in range(1, 5):
    num_inputs = 1 << n
    min_support_all_singletons_nonzero = num_inputs + 1
    qualifying = 0
    witness = None
    min_support_depends_all = num_inputs + 1
    dependent_witness = None
    for mask in range(1 << num_inputs):
        values = transformed_truth(mask, n)
        spectrum = walsh_numerators(values)
        support = [s for s, v in enumerate(spectrum) if v]
        first_nonzero = all(spectrum[1 << i] != 0 for i in range(n))
        if first_nonzero:
            qualifying += 1
            if len(support) < min_support_all_singletons_nonzero:
                min_support_all_singletons_nonzero = len(support)
                witness = {"truth_mask": mask, "truth_values": values,
                           "nonzero_spectrum_masks": support,
                           "walsh_numerators": spectrum}
        if all(depends_on_coordinate(values, n, i) for i in range(n)):
            if len(support) < min_support_depends_all:
                min_support_depends_all = len(support)
                dependent_witness = {"truth_mask": mask, "truth_values": values,
                                     "nonzero_spectrum_masks": support,
                                     "walsh_numerators": spectrum}
    rows.append({
        "n": n,
        "boolean_functions_checked": 1 << num_inputs,
        "functions_with_each_singleton_coefficient_nonzero": qualifying,
        "minimum_fourier_l0_with_each_singleton_nonzero": min_support_all_singletons_nonzero,
        "witness_each_singleton_nonzero": witness,
        "minimum_fourier_l0_among_functions_depending_on_every_coordinate": min_support_depends_all,
        "witness_depends_on_every_coordinate": dependent_witness,
    })

# Exact canonical parity example. Here a truth table uses {-1,+1} values,
# with x represented by its n-bit integer and chi_[n](x)=(-1)^popcount(x).
n = 5
parity_coefficients = [0] * (1 << n)
parity_coefficients[(1 << n) - 1] = 1
parity = {
    "n": n,
    "boolean_range": [-1, 1],
    "nonzero_fourier_masks": [(1 << n) - 1],
    "fourier_l0": 1,
    "fourier_l1": 1,
    "fourier_degree": n,
    "linear_span_dimension_over_F2": gf2_rank([(1 << n) - 1]),
    "depends_on_all_coordinates": True,
    "all_singleton_fourier_coefficients_nonzero": False,
    "all_coordinate_influences": [1] * n,
}

out = {
    "method": "exhaustive integer Walsh transform; no floating point",
    "normalization": "0/1-valued functions: coefficient = Walsh numerator / 2**n",
    "scope_limit": "finite n <= 4 only; does not establish the open asymptotic claim",
    "enumeration": rows,
    "parity_counterexample_to_conflating_dependence_and_singletons": parity,
}
path = Path(__file__).with_name("a165_enum_n1_n4.json")
path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n")
print(path)
for row in rows:
    print(row["n"], row["boolean_functions_checked"],
          row["functions_with_each_singleton_coefficient_nonzero"],
          row["minimum_fourier_l0_with_each_singleton_nonzero"],
          row["minimum_fourier_l0_among_functions_depending_on_every_coordinate"])
print("parity", json.dumps(parity, ensure_ascii=False))
