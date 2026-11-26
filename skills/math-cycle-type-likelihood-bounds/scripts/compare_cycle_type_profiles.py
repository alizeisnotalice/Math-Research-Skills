#!/usr/bin/env python3
"""Compute exact symbolic Hellinger/Bayes bounds for two finite iid laws."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import sympy as sp


def probability(value: object) -> sp.Rational:
    parsed = sp.Rational(str(value))
    if parsed < 0:
        raise ValueError("probabilities must be nonnegative")
    return parsed


def read_profile(raw: object) -> dict[str, sp.Rational]:
    if not isinstance(raw, dict) or not raw:
        raise ValueError("each profile must be a nonempty object")
    profile = {str(label): probability(value) for label, value in raw.items()}
    if sum(profile.values()) != 1:
        raise ValueError("each profile must sum exactly to 1")
    return profile


def report(payload: dict[str, object], digits: int) -> dict[str, object]:
    profiles = payload.get("profiles")
    if not isinstance(profiles, dict) or len(profiles) != 2:
        raise ValueError("profiles must contain exactly two named laws")
    names = sorted(str(name) for name in profiles)
    left, right = (read_profile(profiles[name]) for name in names)
    observations = payload.get("observations")
    if not isinstance(observations, list) or not observations:
        raise ValueError("observations must be a nonempty list")
    alphabet = set(left) | set(right)
    if any(str(item) not in alphabet for item in observations):
        raise ValueError("every observation must occur in at least one profile")
    rho = sp.simplify(sum(sp.sqrt(left.get(label, 0) * right.get(label, 0)) for label in alphabet))
    m = len(observations)
    upper = sp.simplify(rho**m / 2)
    lower = sp.simplify((1 - sp.sqrt(1 - rho ** (2 * m))) / 2)
    return {
        "laws": names,
        "observations": m,
        "hellinger_affinity": str(rho),
        "bayes_error_upper_bound": str(upper),
        "bayes_error_lower_bound": str(lower),
        "decimal": {
            "hellinger_affinity": str(sp.N(rho, digits)),
            "bayes_error_upper_bound": str(sp.N(upper, digits)),
            "bayes_error_lower_bound": str(sp.N(lower, digits)),
        },
        "model": "equal-prior iid product laws supplied by the caller",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--digits", type=int, default=50)
    args = parser.parse_args()
    if args.digits < 1:
        raise SystemExit("--digits must be positive")
    try:
        result = report(json.loads(args.input.read_text()), args.digits)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        raise SystemExit(str(error)) from error
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
