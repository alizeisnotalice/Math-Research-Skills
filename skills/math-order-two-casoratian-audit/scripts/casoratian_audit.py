#!/usr/bin/env python3
"""Exact, finite Casoratian audit for supplied rational order-two recurrences.

Input convention: a[n] u_(n+1) = b[n] u_n + c[n] u_(n-1), starting at n=1.
No asymptotic, limit, integrality, or irrationality conclusion is produced.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def fraction(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("booleans are not rational input")
    return Fraction(str(value))


def display(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def list_of_fractions(payload: Any, label: str) -> list[Fraction]:
    if not isinstance(payload, list):
        raise ValueError(f"{label} must be a JSON array")
    return [fraction(x) for x in payload]


def audit(payload: dict[str, Any]) -> dict[str, Any]:
    recurrence = payload.get("recurrence")
    if not isinstance(recurrence, dict):
        raise ValueError("missing object recurrence")
    a = list_of_fractions(recurrence.get("a"), "recurrence.a")
    b = list_of_fractions(recurrence.get("b"), "recurrence.b")
    c = list_of_fractions(recurrence.get("c"), "recurrence.c")
    if not a or len(a) != len(b) or len(a) != len(c):
        raise ValueError("recurrence.a, b, c must be nonempty arrays of the same length")
    if any(x == 0 for x in a):
        first = next(i + 1 for i, x in enumerate(a) if x == 0)
        raise ValueError(f"recurrence.a[{first}] is zero; the order-two update is undefined")
    u0 = list_of_fractions(payload.get("u_initial"), "u_initial")
    v0 = list_of_fractions(payload.get("v_initial"), "v_initial")
    if len(u0) != 2 or len(v0) != 2:
        raise ValueError("u_initial and v_initial must each contain exactly two values")

    u, v = u0[:], v0[:]
    for i, (aa, bb, cc) in enumerate(zip(a, b, c), start=1):
        u.append((bb * u[i] + cc * u[i - 1]) / aa)
        v.append((bb * v[i] + cc * v[i - 1]) / aa)
    cas = [u[n] * v[n + 1] - u[n + 1] * v[n] for n in range(len(u) - 1)]
    predicted = [cas[0]]
    for i, (aa, cc) in enumerate(zip(a, c), start=1):
        predicted.append(-cc * predicted[i - 1] / aa)
    cas_ok = cas == predicted

    quotient_checks: list[dict[str, Any]] = []
    unresolved: list[int] = []
    for n in range(len(cas)):
        if u[n] == 0 or u[n + 1] == 0:
            unresolved.append(n)
            quotient_checks.append({"n": n, "status": "unresolved_zero_denominator"})
        else:
            left = v[n + 1] / u[n + 1] - v[n] / u[n]
            right = cas[n] / (u[n] * u[n + 1])
            quotient_checks.append({
                "n": n,
                "status": "verified",
                "difference": display(left),
                "casoratian_over_product": display(right),
                "matches": left == right,
            })

    expected = payload.get("expected", {})
    expected_ok = True
    if expected:
        if not isinstance(expected, dict):
            raise ValueError("expected must be an object when supplied")
        if "casoratian" in expected:
            expected_cas = list_of_fractions(expected["casoratian"], "expected.casoratian")
            expected_ok = expected_ok and cas == expected_cas
        if "quotient_differences" in expected:
            actual = [fraction(item["difference"]) for item in quotient_checks if item["status"] == "verified"]
            expected_q = list_of_fractions(expected["quotient_differences"], "expected.quotient_differences")
            expected_ok = expected_ok and actual == expected_q
        if "unresolved_quotient_indices" in expected:
            expected_ok = expected_ok and unresolved == expected["unresolved_quotient_indices"]

    return {
        "name": payload.get("name", "unnamed recurrence"),
        "scope": "finite exact algebra only; no limit, target identification, or irrationality conclusion",
        "terms": {"u": [display(x) for x in u], "v": [display(x) for x in v]},
        "casoratian": [display(x) for x in cas],
        "casoratian_propagation_matches": cas_ok,
        "quotient_checks": quotient_checks,
        "unresolved_quotient_indices": unresolved,
        "expected_fixture_matches": expected_ok,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON recurrence fixture")
    parser.add_argument("--require-complete-quotients", action="store_true",
                        help="return nonzero if any u_n or u_(n+1) is zero")
    args = parser.parse_args()
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(raw, dict):
            raise ValueError("top-level JSON must be an object")
        result = audit(raw)
    except (OSError, json.JSONDecodeError, ValueError, ZeroDivisionError) as exc:
        print(json.dumps({"status": "input_rejected", "reason": str(exc)}, indent=2))
        return 2
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["casoratian_propagation_matches"] or not result["expected_fixture_matches"]:
        return 1
    if args.require_complete_quotients and result["unresolved_quotient_indices"]:
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
