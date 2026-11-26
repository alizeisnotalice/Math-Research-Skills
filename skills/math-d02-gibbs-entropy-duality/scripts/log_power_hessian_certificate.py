#!/usr/bin/env python3
"""Exact finite nested log-power-mean gradient/Hessian certificate.

An internal node represents T_m F=m^{-1}log E exp(mF), with supplied
tilted child probabilities.  It verifies grad T_m F=E_m grad F and
Hess T_m F=E_m Hess F+m Cov_m(grad F), recursively over a finite tree.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def f(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all numerical entries must be exact integer/rational strings, not floats")
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"invalid rational: {value!r}") from exc


def fs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def vector(raw: Any, d: int, label: str) -> list[Fraction]:
    if not isinstance(raw, list) or len(raw) != d:
        raise ValueError(f"{label} must be a vector of length {d}")
    return [f(x) for x in raw]


def matrix(raw: Any, d: int, label: str) -> list[list[Fraction]]:
    if not isinstance(raw, list) or len(raw) != d or any(not isinstance(row, list) or len(row) != d for row in raw):
        raise ValueError(f"{label} must be a {d} by {d} matrix")
    ans = [[f(x) for x in row] for row in raw]
    if any(ans[i][j] != ans[j][i] for i in range(d) for j in range(d)):
        raise ValueError(f"{label} must be exactly symmetric")
    return ans


def zero_matrix(d: int) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(d)] for _ in range(d)]


def add_scaled(target: list[list[Fraction]], scale: Fraction, source: list[list[Fraction]]) -> None:
    for i in range(len(target)):
        for j in range(len(target)):
            target[i][j] += scale * source[i][j]


def serial_vector(v: list[Fraction]) -> list[str]:
    return [fs(x) for x in v]


def serial_matrix(a: list[list[Fraction]]) -> list[list[str]]:
    return [[fs(x) for x in row] for row in a]


def certify(data: dict[str, Any]) -> dict[str, Any]:
    d = data.get("dimension")
    if not isinstance(d, int) or isinstance(d, bool) or d < 1:
        raise ValueError("dimension must be a positive integer")
    near = f(data.get("near_zero_mass", "1/1000000"))
    if near <= 0:
        raise ValueError("near_zero_mass must be positive")
    raw_nodes = data.get("nodes")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise ValueError("nodes must be a nonempty list in child-before-parent order")
    computed: dict[str, tuple[list[Fraction], list[list[Fraction]]]] = {}
    reports: dict[str, Any] = {}
    for raw in raw_nodes:
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str) or not raw["id"] or raw["id"] in computed:
            raise ValueError("each node needs a unique nonempty id")
        name = raw["id"]
        claim_g = vector(raw.get("gradient"), d, f"node {name} gradient")
        claim_h = matrix(raw.get("hessian"), d, f"node {name} hessian")
        children = raw.get("children")
        if children is None:
            computed[name] = (claim_g, claim_h)
            reports[name] = {"kind": "terminal", "gradient": serial_vector(claim_g), "hessian": serial_matrix(claim_h)}
            continue
        if not isinstance(children, list) or not children or not all(isinstance(x, str) and x in computed for x in children):
            raise ValueError(f"internal node {name} must name already-defined children")
        probs = raw.get("tilted_probabilities")
        if not isinstance(probs, list) or len(probs) != len(children):
            raise ValueError(f"internal node {name} needs one tilted probability per child")
        weights = [f(x) for x in probs]
        if any(x < 0 for x in weights) or sum(weights, Fraction(0)) != 1:
            raise ValueError(f"tilted probabilities at {name} must be nonnegative and sum exactly to 1")
        mass = f(raw.get("mass"))
        if mass <= 0:
            raise ValueError(f"mass at {name} must be strictly positive")
        child_values = [computed[x] for x in children]
        avg_g = [sum(weights[k] * child_values[k][0][i] for k in range(len(children))) for i in range(d)]
        avg_h = zero_matrix(d)
        for k in range(len(children)):
            add_scaled(avg_h, weights[k], child_values[k][1])
        covariance = zero_matrix(d)
        for k in range(len(children)):
            delta = [child_values[k][0][i] - avg_g[i] for i in range(d)]
            for i in range(d):
                for j in range(d):
                    covariance[i][j] += weights[k] * delta[i] * delta[j]
        hessian = [[avg_h[i][j] + mass * covariance[i][j] for j in range(d)] for i in range(d)]
        if claim_g != avg_g or claim_h != hessian:
            raise ValueError(f"claimed derivative arrays at {name} do not satisfy the exact tilted mean/covariance recursion")
        near_h = [[avg_h[i][j] + near * covariance[i][j] for j in range(d)] for i in range(d)]
        quotient = [[(hessian[i][j] - avg_h[i][j]) / mass for j in range(d)] for i in range(d)]
        if quotient != covariance or any(near_h[i][j] != near_h[j][i] for i in range(d) for j in range(d)):
            raise AssertionError("near-zero covariance linearization/symmetry failure")
        computed[name] = (avg_g, hessian)
        reports[name] = {
            "kind": "log_power_mean",
            "mass": fs(mass),
            "children": children,
            "tilted_probabilities": serial_vector(weights),
            "gradient": serial_vector(avg_g),
            "mean_child_hessian": serial_matrix(avg_h),
            "conditional_covariance_of_child_gradients": serial_matrix(covariance),
            "hessian": serial_matrix(hessian),
            "near_zero_mass": fs(near),
            "fixed_weight_hessian_at_near_zero_mass": serial_matrix(near_h),
            "exact_difference_quotient_equals_covariance": True,
            "near_zero_hessian_symmetric": True,
        }
    root = data.get("root")
    if not isinstance(root, str) or root not in computed:
        raise ValueError("root must name a supplied node")
    root_g, root_h = computed[root]
    return {
        "certificate_kind": "finite nested log-power-mean derivative and conditional-covariance recursion (exact rationals)",
        "formula": "For T_m F=m^(-1) log E exp(mF), grad T_m F=E_m grad F and Hess T_m F=E_m Hess F+m Cov_m(grad F), m>0.",
        "root": root,
        "root_gradient": serial_vector(root_g),
        "root_hessian": serial_matrix(root_h),
        "nodes": reports,
        "scope": [
            "This verifies supplied finite tilted transition probabilities and derivative arrays exactly; it does not construct the underlying Gaussian/spin hierarchy or prove a SK/Parisi comparison.",
            "Zero tilted child probabilities are permitted. Positive masses are required for every log-power-mean node; the displayed near-zero matrix varies only the explicit mass factor, holding the supplied tilted probabilities and child derivatives fixed.",
            "Exact symmetry of every supplied and propagated Hessian is required. The covariance contribution is explicitly retained at every nested level.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    try:
        with args.input.open(encoding="utf-8") as handle:
            result = certify(json.load(handle))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
