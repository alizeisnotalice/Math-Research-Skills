#!/usr/bin/env python3
"""Exact Bernstein certificates for the strict sign of a rational polynomial."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import math
from pathlib import Path


# These exact rational primitives are retained from the L03 piecewise-ODE
# checker.  This standalone overlay has no runtime dependency on a live skill.
def q(value):
    if type(value) is int or isinstance(value, (str, Fraction)):
        return Fraction(value)
    raise ValueError("coefficients, endpoints, and partition knots must be exact integers or rationals")


def poly(values):
    out = [q(v) for v in values]
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out or [Fraction(0)]


def add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, value in enumerate(a):
        out[i] += value
    for i, value in enumerate(b):
        out[i] += value
    return poly(out)


def mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return poly(out)


def bernstein(a):
    degree = len(a) - 1
    return [sum((a[i] * Fraction(math.comb(k, i), math.comb(degree, i))
                 for i in range(k + 1)), Fraction(0)) for k in range(degree + 1)]


def fmt(value):
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def evaluate(a, x):
    result = Fraction(0)
    for coefficient in reversed(a):
        result = result * x + coefficient
    return result


def affine_restrict(a, left, right):
    """Return p(left + (right-left) u) in ascending powers of u."""
    width = right - left
    result = [Fraction(0)]
    affine = [left, width]
    for coefficient in reversed(a):
        result = add(mul(result, affine), [coefficient])
    return result


def strict_sign(values):
    if all(value >= 0 for value in values) and any(value > 0 for value in values):
        return "POSITIVE"
    if all(value <= 0 for value in values) and any(value < 0 for value in values):
        return "NEGATIVE"
    return None


def certify(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    coefficients = data.get("polynomial")
    if not isinstance(coefficients, list) or not coefficients:
        raise ValueError("polynomial must be a nonempty ascending-coefficient list")
    a = poly(coefficients)
    interval = data.get("interval")
    if not isinstance(interval, dict):
        raise ValueError("interval must be an object")
    left, right = q(interval.get("left")), q(interval.get("right"))
    if left >= right:
        raise ValueError("interval must satisfy left < right")
    if type(interval.get("left_included")) is not bool or type(interval.get("right_included")) is not bool:
        raise ValueError("left_included and right_included must be booleans")
    knots_raw = data.get("partition")
    if not isinstance(knots_raw, list) or len(knots_raw) < 2:
        raise ValueError("partition must explicitly list at least the two rational outer endpoints")
    knots = [q(value) for value in knots_raw]
    if knots[0] != left or knots[-1] != right:
        raise ValueError("partition endpoints must equal interval endpoints exactly")
    if any(first >= second for first, second in zip(knots, knots[1:])):
        raise ValueError("partition knots must be strictly increasing")

    pieces = []
    local_signs = []
    for number, (start, end) in enumerate(zip(knots, knots[1:])):
        local = affine_restrict(a, start, end)
        controls = bernstein(local)
        sign = strict_sign(controls)
        local_signs.append(sign)
        pieces.append({
            "piece": number,
            "left": fmt(start),
            "right": fmt(end),
            "bernstein": [fmt(value) for value in controls],
            "interior_sign": sign or "UNRESOLVED",
        })

    # Every internal partition knot belongs to the union of the closed pieces.
    # The outer knots are required only when their declared endpoint is included.
    required_knots = [(knots[index], True, "internal") for index in range(1, len(knots) - 1)]
    required_knots.insert(0, (left, interval["left_included"], "left"))
    required_knots.append((right, interval["right_included"], "right"))
    endpoint_values = []
    endpoint_signs = []
    for knot, required, role in required_knots:
        value = evaluate(a, knot)
        sign = "POSITIVE" if value > 0 else "NEGATIVE" if value < 0 else "ZERO"
        endpoint_values.append({"knot": fmt(knot), "role": role, "included": required,
                                "value": fmt(value), "sign": sign})
        if required:
            endpoint_signs.append(sign)

    nonempty_signs = [sign for sign in local_signs if sign]
    all_local_same = len(nonempty_signs) == len(local_signs) and len(set(nonempty_signs)) == 1
    proposed = nonempty_signs[0] if all_local_same else None
    endpoints_match = proposed is not None and all(sign == proposed for sign in endpoint_signs)
    if proposed and endpoints_match:
        status = proposed
        reason = "exact Bernstein coefficients certify the strict sign on each open piece; all required knots have the same strict sign"
    else:
        status = "INCONCLUSIVE"
        if not all_local_same:
            reason = "at least one piece has mixed Bernstein coefficients; refine the explicit rational partition or supply another proof"
        else:
            reason = "a required outer endpoint or an included internal partition knot is zero or has the opposite sign"
    return {
        "status": status,
        "scope": "finite exact certificate for the supplied rational polynomial and explicit partition only",
        "interval": {"left": fmt(left), "right": fmt(right),
                     "left_included": interval["left_included"], "right_included": interval["right_included"]},
        "partition": [fmt(knot) for knot in knots],
        "endpoint_values": endpoint_values,
        "pieces": pieces,
        "reason": reason,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON certificate input")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(certify(data), ensure_ascii=False, indent=2))
    except (OSError, TypeError, ValueError, ZeroDivisionError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "REJECT", "reason": str(error)}, ensure_ascii=False))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
