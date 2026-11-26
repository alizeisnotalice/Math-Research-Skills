#!/usr/bin/env python3
"""Verify an exact finite constrained-transport primal/dual attainment witness.

For finite product supports, this is a linear program.  A certificate contains a
coupling, marginal potentials, and *free-sign* equality multipliers for explicitly
listed linear constraints.  It proves optimality only when primal feasibility, dual
feasibility, and the exact zero gap all check; it never silently drops a constraint.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


def sm(values: Iterable[Fraction]) -> Fraction:
    return sum(values, Fraction(0))


def q(value: Any) -> Fraction:
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError("all numerical values must be exact integer/rational strings, not floats")
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise ValueError(f"invalid rational value: {value!r}") from exc


def qs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def parse(data: dict[str, Any]) -> tuple[list[list[Fraction]], list[Fraction], list[Fraction], list[dict[str, Any]], list[list[Fraction]], list[Fraction]]:
    raw_marginals = data.get("marginals")
    if not isinstance(raw_marginals, list) or len(raw_marginals) < 2:
        raise ValueError("marginals must list at least two nonempty probability vectors")
    marginals: list[list[Fraction]] = []
    for k, raw in enumerate(raw_marginals):
        if not isinstance(raw, list) or not raw:
            raise ValueError(f"marginal {k} must be nonempty")
        row = [q(v) for v in raw]
        if any(v < 0 for v in row) or sm(row) != 1:
            raise ValueError(f"marginal {k} must be a nonnegative probability vector")
        marginals.append(row)
    n_cells = 1
    for row in marginals:
        n_cells *= len(row)
    cost = [q(v) for v in data.get("cost", [])]
    plan = [q(v) for v in data.get("primal_plan", [])]
    if len(cost) != n_cells or len(plan) != n_cells:
        raise ValueError(f"cost and primal_plan must each contain {n_cells} entries in lexicographic cell order")
    if any(v < 0 for v in plan):
        raise ValueError("primal_plan must be nonnegative")
    raw_constraints = data.get("constraints", [])
    if not isinstance(raw_constraints, list):
        raise ValueError("constraints must be a list")
    constraints: list[dict[str, Any]] = []
    names: set[str] = set()
    for pos, raw in enumerate(raw_constraints):
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str) or not raw["name"]:
            raise ValueError("each constraint needs a nonempty name")
        if raw["name"] in names:
            raise ValueError("constraint names must be distinct")
        names.add(raw["name"])
        values = [q(v) for v in raw.get("values", [])]
        if len(values) != n_cells:
            raise ValueError(f"constraint {raw['name']} needs {n_cells} cell values")
        constraints.append({"name": raw["name"], "values": values, "target": q(raw.get("target", "0"))})
    raw_potentials = data.get("dual_potentials")
    if not isinstance(raw_potentials, list) or len(raw_potentials) != len(marginals):
        raise ValueError("dual_potentials must have one potential vector per marginal")
    potentials: list[list[Fraction]] = []
    for k, raw in enumerate(raw_potentials):
        if not isinstance(raw, list) or len(raw) != len(marginals[k]):
            raise ValueError(f"potential {k} has wrong length")
        potentials.append([q(v) for v in raw])
    multipliers = [q(v) for v in data.get("equality_multipliers", [])]
    if len(multipliers) != len(constraints):
        raise ValueError("equality_multipliers must align one-for-one with constraints")
    return marginals, cost, plan, constraints, potentials, multipliers


def certify(data: dict[str, Any]) -> dict[str, Any]:
    marginals, cost, plan, constraints, potentials, multipliers = parse(data)
    cell_order = list(itertools.product(*(range(len(mu)) for mu in marginals)))
    # Primal marginal and additional-equality residuals.
    marginal_actual: list[list[Fraction]] = []
    marginal_residuals: list[list[Fraction]] = []
    for k, mu in enumerate(marginals):
        actual = [sm(plan[p] for p, cell in enumerate(cell_order) if cell[k] == index) for index in range(len(mu))]
        marginal_actual.append(actual)
        marginal_residuals.append([actual[index] - mu[index] for index in range(len(mu))])
    constraint_actual = [sm(item["values"][p] * plan[p] for p in range(len(plan))) for item in constraints]
    constraint_residuals = [constraint_actual[i] - constraints[i]["target"] for i in range(len(constraints))]
    primal_feasible = all(value == 0 for row in marginal_residuals for value in row) and all(value == 0 for value in constraint_residuals)
    # With equality Ax=b and W x=d, the correct minimization dual is
    # max b.y+d.lambda subject to A^T y+W^T lambda <= c.  Lambdas are free.
    dual_lhs: list[Fraction] = []
    slack: list[Fraction] = []
    for p, cell in enumerate(cell_order):
        lhs = sm(potentials[k][cell[k]] for k in range(len(marginals))) + sm(multipliers[r] * constraints[r]["values"][p] for r in range(len(constraints)))
        dual_lhs.append(lhs)
        slack.append(cost[p] - lhs)
    dual_feasible = all(value >= 0 for value in slack)
    primal_value = sm(cost[p] * plan[p] for p in range(len(plan)))
    marginal_objective = sm(potentials[k][i] * marginals[k][i] for k in range(len(marginals)) for i in range(len(marginals[k])))
    multiplier_objective = sm(multipliers[r] * constraints[r]["target"] for r in range(len(constraints)))
    dual_value = marginal_objective + multiplier_objective
    gap = primal_value - dual_value
    complementarity = [plan[p] * slack[p] for p in range(len(plan))]
    identity_rhs = sm(complementarity) + sm(multipliers[r] * constraint_residuals[r] for r in range(len(constraints))) + sm(potentials[k][i] * marginal_residuals[k][i] for k in range(len(marginals)) for i in range(len(marginals[k])))
    # In general c.pi - [b.y+d.lambda] equals pi.slack plus potential/multiplier
    # residual terms; exact equality detects sign/order implementation mistakes.
    if gap != identity_rhs:
        raise AssertionError("internal primal-dual identity failure")
    attained = primal_feasible and dual_feasible and gap == 0
    return {
        "certificate_kind": "finite multi-marginal transport with explicit linear equalities (exact rationals)",
        "cell_order": [list(cell) for cell in cell_order],
        "convention": {
            "primal": "min c.pi subject to fixed marginals, W_r.pi=target_r, pi>=0",
            "dual": "max sum_k <phi_k,mu_k> + sum_r lambda_r target_r subject to sum_k phi_k(x_k)+sum_r lambda_r W_r(x)<=c(x)",
            "multiplier_sign": "equality multipliers lambda_r are free signed. For Zaev annihilation constraints target_r=0, their objective contribution is zero but their pointwise term must remain.",
        },
        "primal": {
            "feasible": primal_feasible,
            "objective": qs(primal_value),
            "marginal_actual": [[qs(v) for v in row] for row in marginal_actual],
            "marginal_residual": [[qs(v) for v in row] for row in marginal_residuals],
            "constraint_actual": {constraints[r]["name"]: qs(constraint_actual[r]) for r in range(len(constraints))},
            "constraint_residual": {constraints[r]["name"]: qs(constraint_residuals[r]) for r in range(len(constraints))},
        },
        "dual": {
            "feasible": dual_feasible,
            "objective": qs(dual_value),
            "marginal_potential_objective": qs(marginal_objective),
            "equality_multiplier_objective": qs(multiplier_objective),
            "equality_multipliers": {constraints[r]["name"]: qs(multipliers[r]) for r in range(len(constraints))},
            "lhs_by_cell": [qs(v) for v in dual_lhs],
            "slack_c_minus_lhs_by_cell": [qs(v) for v in slack],
        },
        "weak_duality": {
            "primal_minus_dual": qs(gap),
            "exact_decomposition": "sum_cell pi_cell*slack_cell + sum_r lambda_r*(W_r.pi-target_r) + sum_ki phi_ki*(marginal_actual_ki-mu_ki)",
            "decomposition_value": qs(identity_rhs),
            "complementarity_products_by_cell": [qs(v) for v in complementarity],
        },
        "attainment_witness": attained,
        "limits": [
            "A true attainment certificate requires all three checks: primal feasible, dual feasible, and exact zero gap. A supplied pair with one failing check is not optimal.",
            "This finite LP verifier is independent of the infinite Polish-space topology/CL(mu) gates in Zaev's Theorem 2.1; it does not certify general dual attainment, c-monotonicity sufficiency, or unlisted nonlinear constraints.",
            "For Zaev's source model use target=0. Nonzero targets are a finite affine-equality LP extension and their lambda*target term is retained explicitly.",
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
    payload = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
