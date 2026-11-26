#!/usr/bin/env python3
"""Exact checker for rational Markov--Lukacs interval certificates.

The input is JSON.  Coefficients are in ascending powers of x and every
number must be an integer or a rational string understood by Fraction (for
example "-3/7").  Floating point input is rejected deliberately.

Certificate forms on [a,b]:
  even: p = S_free + (x-a)(b-x) S_weighted
  odd:  p = (x-a) S_left + (b-x) S_right
where each S is explicitly a finite sum of squares of rational polynomials.

This verifies a supplied proof object.  It neither finds an SDP solution nor
turns sampled/interpolated values into a bound for an arbitrary function.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


def rational(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all numbers must be exact integers or rational strings; floats are forbidden")
    if isinstance(value, (str, int)):
        return Fraction(value)
    raise ValueError(f"not an exact rational: {value!r}")


def polynomial(values: Iterable[Any]) -> list[Fraction]:
    result = [rational(value) for value in values]
    if not result:
        return [Fraction(0)]
    return trim(result)


def trim(p: list[Fraction]) -> list[Fraction]:
    p = p[:]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    r = [Fraction(0)] * max(len(p), len(q))
    for i, value in enumerate(p):
        r[i] += value
    for i, value in enumerate(q):
        r[i] += value
    return trim(r)


def multiply(p: list[Fraction], q: list[Fraction]) -> list[Fraction]:
    r = [Fraction(0)] * (len(p) + len(q) - 1)
    for i, left in enumerate(p):
        for j, right in enumerate(q):
            r[i + j] += left * right
    return trim(r)


def evaluate(p: list[Fraction], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(p):
        value = value * x + coefficient
    return value


def sum_of_squares(raw_terms: Any, field: str) -> list[Fraction]:
    if not isinstance(raw_terms, list):
        raise ValueError(f"{field} must be a list of polynomial coefficient lists")
    total = [Fraction(0)]
    for index, raw_term in enumerate(raw_terms):
        if not isinstance(raw_term, list):
            raise ValueError(f"{field}[{index}] must be a coefficient list")
        term = polynomial(raw_term)
        total = add(total, multiply(term, term))
    return total


def as_text(p: list[Fraction]) -> list[str]:
    return [str(value) for value in p]


def interval(payload: dict[str, Any]) -> tuple[Fraction, Fraction]:
    raw = payload.get("interval")
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError("interval must be [a, b]")
    a, b = rational(raw[0]), rational(raw[1])
    if not a < b:
        raise ValueError("the interval must satisfy a < b")
    return a, b


def verify_certificate(payload: dict[str, Any]) -> dict[str, Any]:
    a, b = interval(payload)
    p = polynomial(payload.get("polynomial", []))
    certificate = payload.get("certificate")
    if not isinstance(certificate, dict):
        raise ValueError("certificate must be an object")
    kind = certificate.get("type")
    if kind == "even":
        free = sum_of_squares(certificate.get("free_sos"), "free_sos")
        weighted = sum_of_squares(certificate.get("weighted_sos"), "weighted_sos")
        claimed = add(free, multiply([-a * b, a + b, -1], weighted))
        form = "p=S_free+(x-a)(b-x)S_weighted"
    elif kind == "odd":
        left = sum_of_squares(certificate.get("left_sos"), "left_sos")
        right = sum_of_squares(certificate.get("right_sos"), "right_sos")
        claimed = add(multiply([-a, 1], left), multiply([b, -1], right))
        form = "p=(x-a)S_left+(b-x)S_right"
    else:
        raise ValueError("certificate.type must be 'even' or 'odd'")
    if claimed != p:
        raise ValueError(
            "certificate identity failed: claimed coefficients "
            f"{as_text(claimed)} differ from polynomial coefficients {as_text(p)}"
        )
    return {
        "status": "verified-nonnegative",
        "method": "exact rational explicit-squares Markov--Lukacs form",
        "interval": [str(a), str(b)],
        "form": form,
        "polynomial_coefficients_ascending": as_text(p),
        "scope": "the polynomial p, exactly on the stated closed interval",
        "not_certified": "no approximation error, unsampled function, SDP optimum, or SIP optimum",
    }


def verify_negative_witness(payload: dict[str, Any]) -> dict[str, Any]:
    a, b = interval(payload)
    p = polynomial(payload.get("polynomial", []))
    x = rational(payload.get("witness"))
    if not a <= x <= b:
        raise ValueError("witness must lie in the stated closed interval")
    value = evaluate(p, x)
    if not value < 0:
        raise ValueError(f"witness does not refute nonnegativity: p({x}) = {value}")
    return {
        "status": "verified-negative-witness",
        "interval": [str(a), str(b)],
        "witness": str(x),
        "value": str(value),
        "conclusion": "p is not nonnegative on the stated interval",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="certificate or witness JSON file")
    parser.add_argument("--mode", choices=("auto", "certificate", "negative-witness"), default="auto")
    args = parser.parse_args()
    try:
        payload = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("top-level JSON must be an object")
        mode = args.mode
        if mode == "auto":
            mode = "certificate" if "certificate" in payload else "negative-witness"
        result = verify_certificate(payload) if mode == "certificate" else verify_negative_witness(payload)
    except (OSError, json.JSONDecodeError, ValueError, ZeroDivisionError) as error:
        print(json.dumps({"status": "rejected", "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
