#!/usr/bin/env python3
"""Exact finite-atomic ideal-sparsity decomposition along maximal graph cliques.

Input JSON has edges (zero-based vertex pairs), weighted rational-coordinate atoms, and
optionally monomial exponent vectors to recombine exactly.  Example:
{
  "edges": [[0, 1], [1, 2]],
  "atoms": [{"id": "a", "point": [1, 2, 0], "weight": "1/3"}],
  "monomials": [[0, 0, 0], [1, 1, 0]]
}

The tool only certifies a listed finite measure supported on the variety x_i*x_j=0 for
graph nonedges.  It does not test unspecified semialgebraic constraints or solve an SDP.
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
    raise ValueError("Coordinates and weights must be JSON integers or rational strings")


def show(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def maximal_cliques(vertex_count: int, edges: set[tuple[int, int]]) -> list[tuple[int, ...]]:
    neighbors = {vertex: set() for vertex in range(vertex_count)}
    for left, right in edges:
        neighbors[left].add(right)
        neighbors[right].add(left)
    result: list[tuple[int, ...]] = []

    def bron_kerbosch(current: set[int], candidates: set[int], excluded: set[int]) -> None:
        if not candidates and not excluded:
            result.append(tuple(sorted(current)))
            return
        union = candidates | excluded
        pivot = min(union, key=lambda vertex: (-len(candidates & neighbors[vertex]), vertex)) if union else None
        expansion = sorted(candidates - (neighbors[pivot] if pivot is not None else set()))
        for vertex in expansion:
            bron_kerbosch(current | {vertex}, candidates & neighbors[vertex], excluded & neighbors[vertex])
            candidates.remove(vertex)
            excluded.add(vertex)

    bron_kerbosch(set(), set(range(vertex_count)), set())
    return sorted(set(result))


def monomial_value(point: list[Fraction], exponents: list[int]) -> Fraction:
    value = Fraction(1)
    for coordinate, exponent in zip(point, exponents):
        value *= coordinate ** exponent
    return value


def zero_extended_monomial_value(local_point: list[Fraction], clique: tuple[int, ...], exponents: list[int]) -> Fraction:
    """Evaluate after the local point is zero-padded back to the full coordinate space."""
    local_map = dict(zip(clique, local_point))
    value = Fraction(1)
    for index, exponent in enumerate(exponents):
        coordinate = local_map.get(index, Fraction(0))
        value *= coordinate ** exponent
    return value


def analyze(raw: dict[str, Any]) -> dict[str, Any]:
    atoms_raw = raw.get("atoms")
    edges_raw = raw.get("edges")
    require(isinstance(atoms_raw, list) and atoms_raw, "atoms must be a nonempty list")
    require(isinstance(edges_raw, list), "edges must be a list")
    require(all(isinstance(atom, dict) for atom in atoms_raw), "each atom must be an object")
    first_point = atoms_raw[0].get("point")
    require(isinstance(first_point, list) and first_point, "each atom needs a nonempty point list")
    dimension = len(first_point)
    atoms: list[tuple[str, list[Fraction], Fraction]] = []
    seen_ids: set[str] = set()
    for index, atom in enumerate(atoms_raw):
        label = atom.get("id", f"atom_{index}")
        point_raw = atom.get("point")
        require(isinstance(label, str) and label and label not in seen_ids, "atom ids must be nonempty and unique")
        require(isinstance(point_raw, list) and len(point_raw) == dimension, "all atom points must have the same dimension")
        require("weight" in atom, f"atom {label} needs weight")
        seen_ids.add(label)
        atoms.append((label, [frac(value) for value in point_raw], frac(atom["weight"])))
    edges: set[tuple[int, int]] = set()
    for index, edge in enumerate(edges_raw):
        require(isinstance(edge, list) and len(edge) == 2 and all(isinstance(v, int) and not isinstance(v, bool) for v in edge),
                f"edge {index} must be a pair of integer vertices")
        left, right = edge
        require(0 <= left < dimension and 0 <= right < dimension and left != right, f"edge {index} has invalid endpoints")
        normalized = (min(left, right), max(left, right))
        require(normalized not in edges, "edges must not be repeated")
        edges.add(normalized)
    monomials_raw = raw.get("monomials", [[0 for _ in range(dimension)]])
    require(isinstance(monomials_raw, list) and monomials_raw, "monomials must be a nonempty list")
    monomials: list[list[int]] = []
    for index, exponent in enumerate(monomials_raw):
        require(isinstance(exponent, list) and len(exponent) == dimension and all(isinstance(v, int) and not isinstance(v, bool) and v >= 0 for v in exponent),
                f"monomial {index} must be a nonnegative integer exponent vector of the point dimension")
        monomials.append(exponent)
    nonedges = [(left, right) for left in range(dimension) for right in range(left + 1, dimension) if (left, right) not in edges]
    violations: list[dict[str, Any]] = []
    for label, point, _ in atoms:
        for left, right in nonedges:
            product = point[left] * point[right]
            if product != 0:
                violations.append({"atom_id": label, "nonedge": [left, right], "product": show(product)})
    base: dict[str, Any] = {
        "arithmetic": "exact rational (fractions.Fraction)",
        "dimension": dimension,
        "edges": [list(edge) for edge in sorted(edges)],
        "nonedges": [list(edge) for edge in nonedges],
        "total_weight": show(sum((weight for _, _, weight in atoms), Fraction(0))),
        "negative_weight_atom_ids": [label for label, _, weight in atoms if weight < 0],
        "ideal_nonedge_violations": violations,
    }
    if violations:
        base.update({
            "status": "not_ideal_feasible",
            "message": "At least one listed atom has nonzero coordinates on a graph nonedge, so its support is not a clique and no clique decomposition is certified.",
        })
        return base
    if any(weight < 0 for _, _, weight in atoms):
        base.update({
            "status": "not_positive_measure",
            "message": "The listed atoms satisfy the ideal but at least one has negative weight; this is not a finite positive measure in the source GMP model.",
        })
        return base
    cliques = maximal_cliques(dimension, edges)
    clique_atoms: list[list[tuple[str, list[Fraction], Fraction]]] = [[] for _ in cliques]
    atom_assignments: list[dict[str, Any]] = []
    for label, point, weight in atoms:
        support = tuple(index for index, value in enumerate(point) if value != 0)
        chosen = next((index for index, clique in enumerate(cliques) if set(support).issubset(clique)), None)
        if chosen is None:
            raise AssertionError("ideal constraints should make every atom support lie in a maximal clique")
        clique_atoms[chosen].append((label, point, weight))
        atom_assignments.append({"atom_id": label, "support_indices": list(support), "clique_index": chosen, "clique_vertices": list(cliques[chosen])})
    local_measures: list[dict[str, Any]] = []
    for index, (clique, entries) in enumerate(zip(cliques, clique_atoms)):
        local_measures.append({
            "clique_index": index,
            "clique_vertices": list(clique),
            "total_weight": show(sum((weight for _, _, weight in entries), Fraction(0))),
            "atoms": [{"id": label, "local_point": [show(point[v]) for v in clique], "weight": show(weight)} for label, point, weight in entries],
        })
    recombination: list[dict[str, Any]] = []
    for exponent in monomials:
        original = sum((weight * monomial_value(point, exponent) for _, point, weight in atoms), Fraction(0))
        assembled = Fraction(0)
        for clique, entries in zip(cliques, clique_atoms):
            assembled += sum((
                weight * zero_extended_monomial_value([point[vertex] for vertex in clique], clique, exponent)
                for _, point, weight in entries
            ), Fraction(0))
        recombination.append({"exponents": exponent, "original_moment": show(original), "recombined_moment": show(assembled), "matches": original == assembled})
    base.update({
        "status": "decomposed",
        "maximal_cliques": [list(clique) for clique in cliques],
        "assignment_rule": "Lexicographically first maximal clique containing the atom support; this is a deterministic finite analogue of the source partition.",
        "atom_assignments": atom_assignments,
        "clique_measures": local_measures,
        "monomial_recombination": recombination,
        "all_requested_moments_match": all(record["matches"] for record in recombination),
        "scope": "Only finite listed atoms on the displayed bilinear-monomial variety are certified; unspecified g_j constraints, optimization, SDP relaxations, and hierarchy bounds are outside this result.",
    })
    return base


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON graph and finite atomic measure")
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
