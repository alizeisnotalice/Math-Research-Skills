#!/usr/bin/env python3
"""Check the finite algebra in the auxiliary-polynomial normalization contract."""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from math import prod
from pathlib import Path

import sympy as sp


def factors(n: int) -> dict[int, int]:
    if n < 1:
        raise ValueError("positive integer required")
    return {int(p): int(e) for p, e in sp.factorint(n).items()}


def crt_representative(l: int, roots: dict[str, dict[str, int]]) -> int:
    mods, vals = [], []
    for p, e in factors(l).items():
        data = roots[str(p)]
        modulus = int(data["modulus"])
        if modulus % (p**e):
            raise ValueError(f"root modulus for p={p} lacks p^{e} precision")
        mods.append(p**e)
        vals.append(int(data["residue"]) % (p**e))
    if not mods:
        return 0
    residue, modulus = sp.ntheory.modular.crt(mods, vals, check=True)
    residue = int(residue)
    return residue if residue == 0 else residue - int(modulus)


def lam(n: int, multiplicities: dict[str, int]) -> int:
    return prod(p ** (int(multiplicities[str(p)]) * e) for p, e in factors(n).items())


def polynomial(coefficients: list[int]) -> sp.Expr:
    x = sp.symbols("x")
    return sum(sp.Integer(c) * x**j for j, c in enumerate(coefficients))


def integral_coefficients(expr: sp.Expr) -> list[int]:
    x = sp.symbols("x")
    values = []
    for c in sp.Poly(sp.expand(expr), x).all_coeffs()[::-1]:
        q = Fraction(str(c))
        if q.denominator != 1:
            raise ValueError(f"nonintegral coefficient {c}")
        values.append(q.numerator)
    return values


def check(payload: dict) -> dict:
    coefficients = payload["coefficients"]
    if not isinstance(coefficients, list) or len(coefficients) < 2:
        raise ValueError("coefficients must be a nonconstant increasing-degree list")
    if not all(isinstance(c, int) for c in coefficients):
        raise ValueError("coefficients must be integers")
    if coefficients[-1] <= 0:
        raise ValueError("leading coefficient must be positive")
    l, d = int(payload["l"]), int(payload["D"])
    roots, multiplicities = payload["roots"], payload["multiplicities"]
    degree = len(coefficients) - 1
    for p, e in factors(l * d).items():
        if str(p) not in roots or str(p) not in multiplicities:
            raise ValueError(f"missing root or multiplicity for p={p}")
        m = int(multiplicities[str(p)])
        if not 1 <= m <= degree:
            raise ValueError(f"multiplicity for p={p} must lie in [1,{degree}]")
        modulus = int(roots[str(p)]["modulus"])
        if modulus <= 0 or modulus % (p**e):
            raise ValueError(f"root modulus for p={p} must be divisible by p^{e}")
        if set(factors(modulus)) != {p}:
            raise ValueError(f"root modulus for p={p} must be a power of p")
    h, x = polynomial(coefficients), sp.symbols("x")
    finite_roots = {}
    for p in factors(l * d):
        root = roots[str(p)]
        modulus, residue = int(root["modulus"]), int(root["residue"])
        if int(h.subs(x, residue)) % modulus:
            raise ValueError(f"h(residue) is not 0 modulo the supplied p-power at p={p}")
        finite_roots[str(p)] = {"residue": residue % modulus, "modulus": modulus}
    r_l, r_ld = crt_representative(l, roots), crt_representative(l * d, roots)
    lambda_l, lambda_d, lambda_ld = lam(l, multiplicities), lam(d, multiplicities), lam(l * d, multiplicities)
    hl = sp.expand(h.subs(x, r_l + l * x) / lambda_l)
    hld = sp.expand(h.subs(x, r_ld + l * d * x) / lambda_ld)
    hl_coefficients, hld_coefficients = integral_coefficients(hl), integral_coefficients(hld)
    delta = r_l - r_ld
    if delta % l:
        raise ValueError("CRT representatives do not have the required common class modulo l")
    i = delta // l
    if not 0 <= i < d:
        raise ValueError("derived progression shift is outside [0,D)")
    identity = sp.expand(hl.subs(x, d * x - i) - lambda_d * hld)
    if identity != 0:
        raise ValueError(f"progression identity failed: {identity}")
    if lambda_d % d or lambda_d > d**degree or set(factors(lambda_d)) != set(factors(d)):
        raise ValueError("lambda(D) fails a divisor, degree, or radical invariant")
    return {"status": "pass", "finite_root_congruences": finite_roots, "r_l": r_l,
            "r_lD": r_ld, "lambda_l": lambda_l, "lambda_D": lambda_d, "i": i,
            "h_l_coefficients_increasing_degree": hl_coefficients,
            "h_lD_coefficients_increasing_degree": hld_coefficients,
            "assumption_not_checked": "compatible p-adic roots at every precision and their exact multiplicities"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON: coefficients, l, D, multiplicities, roots")
    args = parser.parse_args()
    try:
        print(json.dumps(check(json.loads(args.input.read_text())), sort_keys=True))
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "reject", "reason": str(exc)}, sort_keys=True))
        raise SystemExit(2)


if __name__ == "__main__":
    main()
