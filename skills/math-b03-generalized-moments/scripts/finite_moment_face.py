#!/usr/bin/env python3
"""Exact finite-support extremality check for an equality-constrained moment polytope.

All numerical input is parsed as fractions.  No floating point arithmetic or LP solver is
used.  The input is JSON and has this shape:

{
  "atoms": [{"id": "x0", "moments": ["0", "0"]}, ...],
  "weights": ["1/4", "1/2", "1/4"],
  "target_moments": ["1", "2"],
  "inequalities": [{"coefficients": ["0", "1", "0"], "lower_bound": "1/2"}],
  "face_zero_indices": [1]
}

The moment equality matrix has a leading normalization row of ones.  Optional inequalities
are `coefficients dot weights >= lower_bound`.  `face_zero_indices` is only a consistency
check for a declared coordinate face; actual zero weights and active inequalities are detected
from the candidate and included in the exact extremality certificate.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any, Iterable


def frac(value: Any) -> Fraction:
    if isinstance(value, bool):
        raise ValueError("Boolean values are not rational numbers")
    if isinstance(value, int):
        return Fraction(value)
    if isinstance(value, str):
        return Fraction(value)
    raise ValueError("Numbers must be JSON integers or rational strings such as '3/7'")


def display(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def rref(matrix: list[list[Fraction]]) -> tuple[list[list[Fraction]], list[int]]:
    reduced = [row[:] for row in matrix]
    if not reduced:
        return reduced, []
    row_count, col_count = len(reduced), len(reduced[0])
    pivots: list[int] = []
    pivot_row = 0
    for col in range(col_count):
        selected = next((r for r in range(pivot_row, row_count) if reduced[r][col] != 0), None)
        if selected is None:
            continue
        reduced[pivot_row], reduced[selected] = reduced[selected], reduced[pivot_row]
        divisor = reduced[pivot_row][col]
        reduced[pivot_row] = [entry / divisor for entry in reduced[pivot_row]]
        for r in range(row_count):
            if r == pivot_row or reduced[r][col] == 0:
                continue
            multiplier = reduced[r][col]
            reduced[r] = [a - multiplier * b for a, b in zip(reduced[r], reduced[pivot_row])]
        pivots.append(col)
        pivot_row += 1
        if pivot_row == row_count:
            break
    return reduced, pivots


def null_direction(matrix: list[list[Fraction]]) -> list[Fraction]:
    """Return one nonzero vector in ker(matrix); caller ensures it is nontrivial."""
    reduced, pivots = rref(matrix)
    col_count = len(matrix[0]) if matrix else 0
    free = next(col for col in range(col_count) if col not in pivots)
    direction = [Fraction(0) for _ in range(col_count)]
    direction[free] = Fraction(1)
    for row, pivot in enumerate(pivots):
        direction[pivot] = -reduced[row][free]
    return direction


def matvec(matrix: list[list[Fraction]], vector: list[Fraction]) -> list[Fraction]:
    return [sum((a * x for a, x in zip(row, vector)), Fraction(0)) for row in matrix]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def parse_instance(raw: dict[str, Any]) -> tuple[list[str], list[list[Fraction]], list[Fraction], list[Fraction], list[tuple[list[Fraction], Fraction]], list[int]]:
    atoms = raw.get("atoms")
    weights_raw = raw.get("weights")
    target_raw = raw.get("target_moments")
    require(isinstance(atoms, list) and atoms, "atoms must be a nonempty list")
    require(isinstance(weights_raw, list), "weights must be a list")
    require(isinstance(target_raw, list), "target_moments must be a list")
    require(len(atoms) == len(weights_raw), "atoms and weights must have the same length")
    require(all(isinstance(atom, dict) for atom in atoms), "each atom must be an object")
    labels: list[str] = []
    columns: list[list[Fraction]] = []
    moment_count: int | None = None
    for index, atom in enumerate(atoms):
        atom_id = atom.get("id", f"atom_{index}")
        require(isinstance(atom_id, str) and atom_id, f"atom {index} has an invalid id")
        moment_raw = atom.get("moments")
        require(isinstance(moment_raw, list), f"atom {atom_id} needs a moments list")
        if moment_count is None:
            moment_count = len(moment_raw)
        require(len(moment_raw) == moment_count, "all atoms must have equally many moment coordinates")
        labels.append(atom_id)
        columns.append([Fraction(1)] + [frac(entry) for entry in moment_raw])
    require(len(target_raw) == moment_count, "target_moments length differs from atom moment dimension")
    require(len(set(labels)) == len(labels), "atom ids must be unique")
    weights = [frac(entry) for entry in weights_raw]
    target = [Fraction(1)] + [frac(entry) for entry in target_raw]
    inequalities_raw = raw.get("inequalities", [])
    require(isinstance(inequalities_raw, list), "inequalities must be a list")
    inequalities: list[tuple[list[Fraction], Fraction]] = []
    for index, inequality in enumerate(inequalities_raw):
        require(isinstance(inequality, dict), f"inequality {index} must be an object")
        coefficient_raw = inequality.get("coefficients")
        require(isinstance(coefficient_raw, list) and len(coefficient_raw) == len(atoms),
                f"inequality {index} coefficients must have one entry per atom")
        require("lower_bound" in inequality, f"inequality {index} needs lower_bound")
        inequalities.append(([frac(entry) for entry in coefficient_raw], frac(inequality["lower_bound"])))
    declared = raw.get("face_zero_indices", [])
    require(isinstance(declared, list) and all(isinstance(i, int) and not isinstance(i, bool) for i in declared),
            "face_zero_indices must be a list of integer indices")
    require(len(set(declared)) == len(declared), "face_zero_indices contains a duplicate")
    require(all(0 <= i < len(atoms) for i in declared), "face_zero_indices contains an out-of-range index")
    return labels, columns, weights, target, inequalities, declared


def analyze(raw: dict[str, Any]) -> dict[str, Any]:
    labels, columns, weights, target, inequalities, declared_zero = parse_instance(raw)
    nonnegative = all(weight >= 0 for weight in weights)
    rows = [[column[row] for column in columns] for row in range(len(target))]
    achieved = matvec(rows, weights)
    residual = [left - right for left, right in zip(achieved, target)]
    inequality_slacks = [sum((coefficient * weight for coefficient, weight in zip(coefficients, weights)), Fraction(0)) - lower
                         for coefficients, lower in inequalities]
    declared_face_ok = all(weights[index] == 0 for index in declared_zero)
    base: dict[str, Any] = {
        "arithmetic": "exact rational (fractions.Fraction)",
        "model": "{w >= 0 : A w = b}; A has normalization plus supplied moment rows",
        "atom_ids": labels,
        "target": [display(value) for value in target],
        "achieved": [display(value) for value in achieved],
        "active_nonnegativity_indices": [i for i, weight in enumerate(weights) if weight == 0],
        "positive_support_indices": [i for i, weight in enumerate(weights) if weight > 0],
        "inequality_slacks": [display(value) for value in inequality_slacks],
        "active_inequality_indices": [i for i, slack in enumerate(inequality_slacks) if slack == 0],
        "declared_face_zero_indices": declared_zero,
        "declared_coordinate_face_membership": declared_face_ok,
    }
    if not nonnegative or any(residual) or any(slack < 0 for slack in inequality_slacks):
        base.update({
            "status": "infeasible_candidate",
            "nonnegative": nonnegative,
            "inequalities_satisfied": all(slack >= 0 for slack in inequality_slacks),
            "residual_Aw_minus_b": [display(value) for value in residual],
            "message": "No extremality conclusion: the supplied weights are not feasible for the displayed finite equality model.",
        })
        return base
    support = base["positive_support_indices"]
    support_matrix = [[row[index] for index in support] for row in rows]
    _, equality_pivots = rref(support_matrix)
    equality_rank = len(equality_pivots)
    active_matrix = [row[:] for row in rows]
    active_labels = [f"equality_row_{i}" for i in range(len(rows))]
    for index, weight in enumerate(weights):
        if weight == 0:
            active_matrix.append([Fraction(int(i == index)) for i in range(len(weights))])
            active_labels.append(f"nonnegativity_w_{index}=0")
    for index, ((coefficients, _), slack) in enumerate(zip(inequalities, inequality_slacks)):
        if slack == 0:
            active_matrix.append(coefficients[:])
            active_labels.append(f"inequality_{index}_active")
    _, active_pivots = rref(active_matrix)
    active_rank = len(active_pivots)
    base.update({
        "status": "extreme" if active_rank == len(weights) else "not_extreme",
        "nonnegative": True,
        "residual_Aw_minus_b": [display(value) for value in residual],
        "rank_A_on_positive_support": equality_rank,
        "positive_support_size": len(support),
        "rank_active_constraint_matrix": active_rank,
        "active_constraint_rows": active_labels,
        "criterion": "extreme iff the equality rows, active nonnegativity rows, and active supplied inequality rows have full column rank",
        "scope": "This is an exact conclusion only for the listed finite atom set with the displayed linear equalities, inequalities, and coordinate nonnegativity.",
    })
    if active_rank == len(weights):
        base["certificate"] = {
            "type": "full_column_rank",
            "pivot_columns_of_active_constraint_matrix": active_pivots,
            "message": "All two-sided feasible perturbations vanish after enforcing the equalities and all active inequalities.",
        }
        return base
    direction = null_direction(active_matrix)
    positive_ratios = [weights[index] / abs(value) for index, value in enumerate(direction) if value != 0]
    inequality_ratios = [slack / abs(sum((coefficient * value for coefficient, value in zip(coefficients, direction)), Fraction(0)))
                         for (coefficients, _), slack in zip(inequalities, inequality_slacks)
                         if sum((coefficient * value for coefficient, value in zip(coefficients, direction)), Fraction(0)) != 0]
    epsilon = min(positive_ratios + inequality_ratios)
    plus = [weight + epsilon * value for weight, value in zip(weights, direction)]
    minus = [weight - epsilon * value for weight, value in zip(weights, direction)]
    midpoint = [(left + right) / 2 for left, right in zip(plus, minus)]
    base["certificate"] = {
        "type": "two_sided_feasible_perturbation",
        "kernel_direction": [display(value) for value in direction],
        "epsilon": display(epsilon),
        "weights_plus": [display(value) for value in plus],
        "weights_minus": [display(value) for value in minus],
        "A_direction": [display(value) for value in matvec(rows, direction)],
        "plus_residual": [display(value) for value in [a - b for a, b in zip(matvec(rows, plus), target)]],
        "minus_residual": [display(value) for value in [a - b for a, b in zip(matvec(rows, minus), target)]],
        "midpoint_equals_input": midpoint == weights,
        "both_nonnegative": all(value >= 0 for value in plus + minus),
        "plus_inequality_slacks": [display(sum((coefficient * value for coefficient, value in zip(coefficients, plus)), Fraction(0)) - lower)
                                     for coefficients, lower in inequalities],
        "minus_inequality_slacks": [display(sum((coefficient * value for coefficient, value in zip(coefficients, minus)), Fraction(0)) - lower)
                                      for coefficients, lower in inequalities],
        "message": "Distinct feasible endpoints have the input weights as their midpoint, so the input is not extreme.",
    }
    return base


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON instance using integer or rational-string coefficients")
    parser.add_argument("-o", "--output", type=Path, help="write JSON output here instead of stdout")
    args = parser.parse_args(argv)
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        require(isinstance(raw, dict), "top-level JSON value must be an object")
        result = analyze(raw)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(json.dumps({"status": "input_error", "message": str(error)}, ensure_ascii=False, indent=2), file=sys.stderr)
        return 2
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
