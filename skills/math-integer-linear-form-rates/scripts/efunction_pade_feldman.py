#!/usr/bin/env python3
"""Exact finite Padé interpolation data from Väänänen's construction."""

from __future__ import annotations

from fractions import Fraction
from functools import reduce
from math import comb, factorial
import json
from pathlib import Path
import sys


def fraction(value: str | int) -> Fraction:
    return Fraction(str(value))


def falling(value: Fraction, degree: int) -> Fraction:
    result = Fraction(1)
    for offset in range(degree):
        result *= value - offset
    return result


def encode(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def construct(data: dict) -> dict:
    lambdas = [fraction(value) for value in data["lambdas"]]
    orders = data["orders"]
    if not lambdas or len(lambdas) != len(orders):
        raise ValueError("lambdas and orders must be nonempty lists of the same length")
    if any(type(order) is not int or order <= 0 for order in orders):
        raise ValueError("orders must be positive integers")
    for left in range(len(lambdas)):
        for right in range(left + 1, len(lambdas)):
            if (lambdas[right] - lambdas[left]).denominator == 1:
                raise ValueError("distinct lambda values must have nonintegral pairwise differences")

    total = sum(orders)
    outputs = []
    for selected, chosen_lambda in enumerate(lambdas):
        gamma_zero = Fraction(total + 1) + chosen_lambda
        gamma_nodes = []
        for index, (value, order) in enumerate(zip(lambdas, orders)):
            for nu in range(1, order + 1):
                gamma_nodes.append(Fraction(total + nu) + value + (index == selected))
        coefficients = []
        for degree in range(total + 1):
            numerator = sum(
                Fraction((-1) ** (degree - tau) * comb(degree, tau))
                * reduce(
                    lambda product, node: product * (tau - node) / (gamma_zero - node),
                    gamma_nodes,
                    Fraction(1),
                )
                for tau in range(degree + 1)
            )
            coefficients.append(numerator / factorial(degree))
        tests = [sum(coefficients[degree] * falling(gamma_zero, degree) for degree in range(total + 1))]
        tests.extend(sum(coefficients[degree] * falling(node, degree) for degree in range(total + 1)) for node in gamma_nodes)
        if tests[0] != 1 or any(value != 0 for value in tests[1:]):
            raise AssertionError("interpolation conditions failed")
        outputs.append({
            "selected_lambda": encode(chosen_lambda),
            "gamma_zero": encode(gamma_zero),
            "gamma_nodes": [encode(value) for value in gamma_nodes],
            "q_coefficients": [encode(value) for value in coefficients],
            "interpolation": {"at_gamma_zero": encode(tests[0]), "at_gamma_nodes": [encode(value) for value in tests[1:]]},
        })
    return {"family_size": len(lambdas), "total_order": total, "approximants": outputs}


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: efunction_pade_feldman.py INPUT.json")
    data = json.loads(Path(sys.argv[1]).read_text())
    print(json.dumps(construct(data), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except (KeyError, TypeError, ValueError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        raise SystemExit(2)
