#!/usr/bin/env python3
"""Check the finite algebraic gates for Akhtari's binary-form unit bound."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp


def analyse(coefficients: list[object]) -> dict[str, object]:
    if len(coefficients) < 4:
        raise ValueError("coefficients must describe a degree at least three binary form")
    if any(not isinstance(value, int) for value in coefficients):
        raise ValueError("coefficients must be integers in descending x-power order")
    if coefficients[0] == 0:
        raise ValueError("the leading coefficient must be nonzero")

    degree = len(coefficients) - 1
    x = sp.symbols("x")
    polynomial = sp.Poly.from_list(coefficients, gens=x, domain=sp.ZZ)
    factors = sp.factor_list(polynomial.as_expr(), extension=None)[1]
    irreducible = len(factors) == 1 and factors[0][1] == 1 and sp.degree(factors[0][0], x) == degree
    discriminant = int(sp.discriminant(polynomial.as_expr(), x))
    threshold = 2**22 * (degree + 1) ** 10 * degree**degree
    return {
        "degree": degree,
        "polynomial_F_x_1": str(polynomial.as_expr()),
        "irreducible_over_Q": irreducible,
        "discriminant": discriminant,
        "absolute_discriminant": abs(discriminant),
        "source_threshold_D0": threshold,
        "theorem_hypotheses_met": irreducible and abs(discriminant) > threshold,
        "solution_count_convention": "identifies (x,y) with (-x,-y)",
        "conclusion_if_hypotheses_met": f"at most {11 * degree - 2} classes for |F(x,y)|=1",
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: check_binary_form_unit_bound.py input.json")
    data = json.loads(Path(sys.argv[1]).read_text())
    if set(data) != {"coefficients"}:
        raise SystemExit("input must contain only coefficients")
    print(json.dumps(analyse(data["coefficients"]), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
