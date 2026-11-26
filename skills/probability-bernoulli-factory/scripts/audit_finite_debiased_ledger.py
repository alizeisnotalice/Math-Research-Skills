#!/usr/bin/env python3
"""Exact finite ledger for the Koskela--Karvonen--Latuszynski--Spano debiasing form.

This audits a *finite truncation* of the lower-envelope telescoping formula.  It proves
only the listed finite-table claims at the supplied rational x; it deliberately cannot
certify an infinite Bernoulli factory or a limiting target without additional envelopes.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def parse_fraction(value: Any, *, unit: bool = False) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all numbers must be integers or string-rationals; floats/bools are rejected")
    if isinstance(value, int):
        result = Fraction(value)
    elif isinstance(value, str):
        result = Fraction(value)
    else:
        raise ValueError("all numbers must be integers or string-rationals")
    if unit and not 0 <= result <= 1:
        raise ValueError("a probability/coefficient must lie in [0,1]")
    return result


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def choose(n: int, k: int) -> int:
    return math.comb(n, k) if 0 <= k <= n else 0


def parse(document: dict[str, Any]) -> tuple[Fraction, dict[int, Fraction], dict[int, list[Fraction]], int, Fraction | None]:
    x = parse_fraction(document.get("x"), unit=True)
    raw_law = document.get("L_pmf")
    if not isinstance(raw_law, dict) or not raw_law:
        raise ValueError("L_pmf must be a nonempty object with positive integer keys")
    law: dict[int, Fraction] = {}
    for raw_level, raw_mass in raw_law.items():
        level = int(raw_level)
        if level < 1:
            raise ValueError("L support must consist of positive levels")
        if level in law:
            raise ValueError("duplicate L support level")
        law[level] = parse_fraction(raw_mass, unit=True)
    if sum(law.values(), Fraction(0)) != 1:
        raise ValueError("L_pmf masses must sum exactly to one")
    raw_coefficients = document.get("lower_coefficients")
    if not isinstance(raw_coefficients, dict):
        raise ValueError("lower_coefficients must be an object indexed by degree")
    coefficients: dict[int, list[Fraction]] = {}
    for raw_degree, raw_row in raw_coefficients.items():
        degree = int(raw_degree)
        if degree < 0 or not isinstance(raw_row, list) or len(raw_row) != degree + 1:
            raise ValueError("coefficient row at degree n must contain exactly n+1 entries")
        coefficients[degree] = [parse_fraction(value, unit=True) for value in raw_row]
    start = document.get("start_k")
    if isinstance(start, bool) or not isinstance(start, int) or start < 1:
        raise ValueError("start_k must be a positive integer")
    maximum = max(law)
    for degree in range(start - 1, maximum + 1):
        if degree not in coefficients:
            raise ValueError(f"missing lower coefficient row {degree}")
    target = parse_fraction(document["target_at_x"], unit=True) if "target_at_x" in document else None
    return x, law, coefficients, start, target


def H(level: int, degree: int, successes: int, coefficients: dict[int, list[Fraction]]) -> Fraction:
    """Hypergeometric thinning average H_level(degree, successes)."""
    denominator = choose(level, successes)
    return sum(
        Fraction(choose(level - degree, successes - i) * choose(degree, i), denominator) * coefficients[degree][i]
        for i in range(degree + 1)
    )


def binomial_mass(n: int, successes: int, x: Fraction) -> Fraction:
    return Fraction(choose(n, successes)) * x**successes * (1 - x) ** (n - successes)


def audit(document: dict[str, Any]) -> dict[str, Any]:
    x, law, coefficients, start, target = parse(document)
    maximum = max(law)
    survival = {n: sum((mass for level, mass in law.items() if level >= n), Fraction(0)) for n in range(start, maximum + 1)}
    compatibility_violations: list[dict[str, str]] = []
    for n in range(start - 1, maximum + 1):
        for m in range(start - 1, n + 1):
            for successes in range(n + 1):
                if coefficients[n][successes] < H(n, m, successes, coefficients):
                    compatibility_violations.append({"n": str(n), "m": str(m), "successes": str(successes)})
    outcomes: list[dict[str, str]] = []
    expectation = Fraction(0)
    pathwise_min, pathwise_max = Fraction(1), Fraction(0)
    increments_nonnegative = True
    for level, level_mass in sorted(law.items()):
        for successes in range(level + 1):
            base = H(level, start - 1, successes, coefficients)
            value = base
            for n in range(start, level + 1):
                increment = H(level, n, successes, coefficients) - H(level, n - 1, successes, coefficients)
                increments_nonnegative = increments_nonnegative and increment >= 0
                value += increment / survival[n]
            probability = level_mass * binomial_mass(level, successes, x)
            expectation += probability * value
            pathwise_min, pathwise_max = min(pathwise_min, value), max(pathwise_max, value)
            outcomes.append({"L": str(level), "S_L": str(successes), "probability_at_x": text(probability), "psi": text(value)})
    g_max = sum(binomial_mass(maximum, successes, x) * coefficients[maximum][successes] for successes in range(maximum + 1))
    expected_L = sum((Fraction(level) * mass for level, mass in law.items()), Fraction(0))
    result: dict[str, Any] = {
        "scope": "finite-support L and supplied lower-envelope rows at one rational x; this is a ledger, not a proof of an infinite Bernoulli factory",
        "x": text(x),
        "start_k": start,
        "L_support": [str(level) for level in sorted(law)],
        "a_s_termination_for_this_finite_proxy": True,
        "stopped_p_coin_cost_maximum": maximum,
        "expected_p_coin_cost": text(expected_L),
        "running_outcome_count": len(outcomes),
        "all_coefficients_in_unit_interval": True,
        "lower_compatibility_holds_on_supplied_rows": not compatibility_violations,
        "compatibility_violations": compatibility_violations,
        "all_realized_telescoping_increments_nonnegative": increments_nonnegative,
        "pathwise_psi_minimum": text(pathwise_min),
        "pathwise_psi_maximum": text(pathwise_max),
        "psi_is_unit_interval_valued_on_all_enumerated_outcomes": 0 <= pathwise_min and pathwise_max <= 1,
        "exact_E_psi_at_x": text(expectation),
        "exact_g_at_largest_degree_at_x": text(g_max),
        "finite_telescope_identity_holds": expectation == g_max,
        "outcomes": outcomes,
    }
    if target is not None:
        result["claimed_target_at_x"] = text(target)
        result["target_minus_exact_E_psi"] = text(target - expectation)
        result["finite_proxy_is_unbiased_for_claimed_target_at_x"] = target == expectation
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(document, dict):
            raise ValueError("top-level JSON must be an object")
        result = audit(document)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
