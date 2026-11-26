#!/usr/bin/env python3
"""Exact finite audit for scheduled binary test-supermartingale products.

All probabilities and multipliers are parsed as Fraction.  The optional inverse-moment
bound is deliberately restricted to a positive *integer* order, so every reported value
is rational and no numerical logarithm is used.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path
from typing import Any


def fraction(value: Any, *, unit: bool = False, positive: bool = False) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("use integer or string-rational data; floats and booleans are rejected")
    if isinstance(value, int):
        answer = Fraction(value)
    elif isinstance(value, str):
        answer = Fraction(value)
    else:
        raise ValueError("use integer or string-rational data")
    if unit and not 0 <= answer <= 1:
        raise ValueError("a probability must lie in [0,1]")
    if positive and answer <= 0:
        raise ValueError("a multiplier must be strictly positive")
    return answer


def text(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def parse_step(raw: Any) -> dict[str, Fraction]:
    if not isinstance(raw, dict):
        raise ValueError("every step must be an object")
    required = ("p0_win", "p1_win", "e_win", "e_loss")
    if any(key not in raw for key in required):
        raise ValueError(f"step requires {', '.join(required)}")
    return {
        "p0": fraction(raw["p0_win"], unit=True),
        "p1": fraction(raw["p1_win"], unit=True),
        "win": fraction(raw["e_win"], positive=True),
        "loss": fraction(raw["e_loss"], positive=True),
    }


def expand_steps(raw_steps: Any) -> list[dict[str, Fraction]]:
    if not isinstance(raw_steps, list) or not raw_steps:
        raise ValueError("steps must be a nonempty array")
    answer: list[dict[str, Fraction]] = []
    for raw in raw_steps:
        repeats = raw.get("repeat", 1) if isinstance(raw, dict) else 1
        if isinstance(repeats, bool) or not isinstance(repeats, int) or repeats < 1:
            raise ValueError("repeat must be a positive integer")
        answer.extend(parse_step(raw) for _ in range(repeats))
    if len(answer) > 80:
        raise ValueError("at most 80 scheduled steps are accepted by this finite enumerator")
    return answer


def e_power_sign(step: dict[str, Fraction]) -> tuple[str, str]:
    """Return sign of p log(a)+(1-p)log(b), without evaluating a logarithm."""
    probability = step["p1"]
    denominator = probability.denominator
    wins = probability.numerator
    certificate = step["win"] ** wins * step["loss"] ** (denominator - wins)
    sign = "positive" if certificate > 1 else "zero" if certificate == 1 else "negative"
    return sign, f"log({text(certificate)})/{denominator}"


def audit(document: dict[str, Any]) -> dict[str, Any]:
    alpha = fraction(document.get("alpha"), unit=True, positive=True)
    order = document.get("inverse_moment_order")
    if isinstance(order, bool) or not isinstance(order, int) or order < 1:
        raise ValueError("inverse_moment_order must be a positive integer")
    steps = expand_steps(document.get("steps"))
    threshold = 1 / alpha
    wealth: dict[Fraction, Fraction] = {Fraction(1): Fraction(1)}
    alive: dict[Fraction, Fraction] = {Fraction(1): Fraction(1)}
    moment_product = Fraction(1)
    rows: list[dict[str, str]] = []
    all_e_values = True
    all_positive_e_power = True
    all_contracting = True
    for index, step in enumerate(steps, start=1):
        e0_mean = step["p0"] * step["win"] + (1 - step["p0"]) * step["loss"]
        e_value = e0_mean <= 1
        all_e_values = all_e_values and e_value
        sign, log_certificate = e_power_sign(step)
        all_positive_e_power = all_positive_e_power and sign == "positive"
        inverse_moment = step["p1"] * step["win"] ** (-order) + (1 - step["p1"]) * step["loss"] ** (-order)
        moment_product *= inverse_moment
        all_contracting = all_contracting and inverse_moment < 1
        next_wealth: defaultdict[Fraction, Fraction] = defaultdict(Fraction)
        next_alive: defaultdict[Fraction, Fraction] = defaultdict(Fraction)
        for amount, mass in wealth.items():
            next_wealth[amount * step["win"]] += mass * step["p1"]
            next_wealth[amount * step["loss"]] += mass * (1 - step["p1"])
        for amount, mass in alive.items():
            for multiplier, probability in ((step["win"], step["p1"]), (step["loss"], 1 - step["p1"])):
                next_amount = amount * multiplier
                if next_amount <= threshold:
                    next_alive[next_amount] += mass * probability
        wealth, alive = dict(next_wealth), dict(next_alive)
        rows.append({
            "step": str(index),
            "E0_multiplier": text(e0_mean),
            "is_conditional_e_variable": str(e_value).lower(),
            "e_power_sign_under_P1": sign,
            "e_power_exact_sign_certificate": log_certificate,
            f"E1[multiplier^-{order}]": text(inverse_moment),
        })
    fixed_error = sum((mass for amount, mass in wealth.items() if amount <= threshold), Fraction(0))
    sequential_error = sum(alive.values(), Fraction(0))
    raw_bound = alpha ** (-order) * moment_product
    return {
        "scope": "finite independent binary scheduled bets; deterministic schedules are a special case of predictable conditional e-variables",
        "alpha": text(alpha),
        "horizon": len(steps),
        "rejection_rule": "reject at first W_n > 1/alpha",
        "all_steps_are_e_variables_under_P0": all_e_values,
        "all_step_e_powers_positive_under_P1": all_positive_e_power,
        "inverse_moment_order": order,
        "all_inverse_moments_contract": all_contracting,
        "product_E1_W_minus_order": text(moment_product),
        "exact_fixed_horizon_type_II_error": text(fixed_error),
        "exact_sequential_type_II_error": text(sequential_error),
        "fixed_horizon_inverse_moment_bound_raw": text(raw_bound),
        "fixed_horizon_inverse_moment_bound_capped": text(min(Fraction(1), raw_bound)),
        "bound_rule": "P1(W_t <= 1/alpha) <= alpha^(-s) product_n E1[E_n^(-s)]; requires the displayed per-step inverse moments and independent scheduled steps here.",
        "steps": rows,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    try:
        parsed = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(parsed, dict):
            raise ValueError("top-level JSON must be an object")
        result = audit(parsed)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
