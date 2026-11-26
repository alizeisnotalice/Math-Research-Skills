#!/usr/bin/env python3
"""Exact L-infinity residual certificate for piecewise polynomial 1D ODEs."""
import argparse
import json
import math
import sys
from fractions import Fraction


def q(value):
    if type(value) is int or isinstance(value, (str, Fraction)):
        return Fraction(value)
    raise ValueError("coefficients and endpoints must be exact integer or rational values")


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


def scale(a, factor):
    return poly([factor * value for value in a])


def mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, left in enumerate(a):
        for j, right in enumerate(b):
            out[i + j] += left * right
    return poly(out)


def derivative(a):
    return poly([i * a[i] for i in range(1, len(a))]) if len(a) > 1 else [Fraction(0)]


def value(a, t):
    result = Fraction(0)
    for coefficient in reversed(a):
        result = result * t + coefficient
    return result


def bernstein(a):
    degree = len(a) - 1
    return [sum((a[i] * Fraction(math.comb(k, i), math.comb(degree, i))
                 for i in range(k + 1)), Fraction(0)) for k in range(degree + 1)]


def fmt(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def fail(message):
    raise ValueError(message)


def certify(data):
    if not isinstance(data, dict):
        fail("input must be a JSON object")
    if data.get("operator") != "u'' + b u' - c u = 0":
        fail("operator must be exactly u'' + b u' - c u = 0")
    pieces = data.get("segments")
    if not isinstance(pieces, list) or not pieces:
        fail("segments must be a nonempty list")
    endpoint_bound = q(data["endpoint_error_bound"])
    if endpoint_bound < 0:
        fail("endpoint_error_bound must be nonnegative")
    previous = None
    all_residual_coeffs = []
    all_c_coeffs = []
    detail = []
    for number, item in enumerate(pieces):
        left, right = q(item["left"]), q(item["right"])
        width = right - left
        if width <= 0:
            fail(f"segment {number}: right must exceed left")
        if any(not isinstance(item[key], list) or not item[key] for key in ("approx", "b", "c")):
            fail(f"segment {number}: approx, b, and c must be nonempty coefficient lists")
        v, b, c = poly(item["approx"]), poly(item["b"]), poly(item["c"])
        vt = derivative(v)
        residual = add(scale(derivative(vt), Fraction(1, 1) / (width * width)),
                       add(scale(mul(b, vt), Fraction(1, 1) / width), scale(mul(c, v), -1)))
        residual_coeffs, c_coeffs = bernstein(residual), bernstein(c)
        if previous is not None:
            if left != previous["right"]:
                fail(f"segment {number}: interval does not meet preceding segment")
            if value(previous["v"], Fraction(1)) != value(v, Fraction(0)):
                fail(f"segment {number}: value join is not C0")
            if value(derivative(previous["v"]), Fraction(1)) / previous["width"] != value(vt, Fraction(0)) / width:
                fail(f"segment {number}: derivative join is not C1")
        previous = {"right": right, "v": v, "width": width}
        all_residual_coeffs.extend(residual_coeffs)
        all_c_coeffs.extend(c_coeffs)
        detail.append({"segment": number, "residual_bernstein": [fmt(x) for x in residual_coeffs],
                       "c_bernstein": [fmt(x) for x in c_coeffs]})
    mu = min(all_c_coeffs)
    if mu <= 0:
        fail(f"coercivity fails: exact Bernstein lower bound for c is {fmt(mu)}")
    rho = max(abs(x) for x in all_residual_coeffs)
    bound = max(endpoint_bound, rho / mu)
    return {"status": "PASS", "profile_error_bound": fmt(bound), "rho": fmt(rho), "mu": fmt(mu),
            "endpoint_error_bound": fmt(endpoint_bound), "derivative_certificate": "not_provided", "segments": detail}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="JSON certificate input")
    args = parser.parse_args()
    try:
        with open(args.input, encoding="utf-8") as handle:
            data = json.load(handle)
        print(json.dumps(certify(data), ensure_ascii=False, indent=2))
    except (OSError, KeyError, TypeError, ValueError, ZeroDivisionError) as error:
        print(json.dumps({"status": "REJECT", "reason": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
