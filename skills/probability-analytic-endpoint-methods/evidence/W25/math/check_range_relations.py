#!/usr/bin/env python3
"""Exact finite sanity checks for exponent-range comparisons in AEP-024.

This checks the algebraic equivalence q*=nq/(n-q) >= 2q iff q >= n/2
for rational q in 1<q<n. It is a finite exact-arithmetic consistency check,
not a proof of the paper's operator estimates or a general theorem.
"""
from fractions import Fraction
import json
from pathlib import Path

checks = 0
for n in range(2, 31):
    # Quarter-step rationals sample both sides of n/2 while keeping 1<q<n.
    for numerator in range(5, 4 * n):
        q = Fraction(numerator, 4)
        if not (1 < q < n):
            continue
        q_star = Fraction(n) * q / (Fraction(n) - q)
        left = q_star >= 2 * q
        right = q >= Fraction(n, 2)
        assert left == right, (n, q, q_star, left, right)
        checks += 1

examples = []
for n, q in [(4, Fraction(3, 2)), (4, Fraction(2)), (4, Fraction(3)),
             (5, Fraction(2)), (5, Fraction(5, 2)), (5, Fraction(4))]:
    q_star = Fraction(n) * q / (Fraction(n) - q)
    examples.append({
        "n": n,
        "q": str(q),
        "q_star": str(q_star),
        "two_q": str(2 * q),
        "q_star_ge_two_q": q_star >= 2 * q,
        "q_ge_n_over_two": q >= Fraction(n, 2),
    })

result = {
    "check": "q_star >= 2q iff q >= n/2, with q_star=nq/(n-q), 1<q<n",
    "exact_arithmetic": "fractions.Fraction",
    "rational_cases_checked": checks,
    "all_assertions_passed": True,
    "examples": examples,
    "scope": "finite algebraic sanity check only; no operator theorem is verified",
}
out = Path(__file__).with_name("check_range_relations.json")
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
