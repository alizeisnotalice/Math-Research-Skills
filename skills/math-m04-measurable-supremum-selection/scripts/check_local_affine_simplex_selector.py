#!/usr/bin/env python3
"""Certify an exact finite-dimensional local affine selector on a simplex.

The input uses only integer or ``p/q`` rational coordinates.  A supplied
``graph_polyhedron`` is an H-representation for the graph in the joint
``(x, y)`` coordinates.  Without it, the result is explicitly conditional on
the caller's declared convex-graph and vertex-membership contract.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path
from typing import Any


def rational(value: Any, label: str) -> Fraction:
    """Parse an exact rational, rejecting binary floating-point input."""
    if isinstance(value, bool) or isinstance(value, float):
        raise ValueError(f"{label} must be an integer or a p/q string, not a boolean or float")
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"{label} must be an integer or a p/q string") from error


def vector(value: Any, label: str, expected_length: int | None = None) -> list[Fraction]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must be a nonempty list")
    output = [rational(entry, f"{label}[{index}]") for index, entry in enumerate(value)]
    if expected_length is not None and len(output) != expected_length:
        raise ValueError(f"{label} must have length {expected_length}")
    return output


def vectors(value: Any, label: str, count: int | None = None) -> list[list[Fraction]]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{label} must be a nonempty list of vectors")
    output = [vector(entry, f"{label}[{index}]") for index, entry in enumerate(value)]
    dimension = len(output[0])
    if any(len(entry) != dimension for entry in output):
        raise ValueError(f"{label} vectors must have one common positive dimension")
    if count is not None and len(output) != count:
        raise ValueError(f"{label} must have {count} vectors")
    return output


def solve_square(matrix: list[list[Fraction]], right: list[Fraction], label: str) -> list[Fraction]:
    """Exact Gauss--Jordan solve, rejecting a singular square matrix."""
    size = len(matrix)
    if size == 0 or len(right) != size or any(len(row) != size for row in matrix):
        raise ValueError(f"{label} must be a nonempty square linear system")
    augmented = [row[:] + [right[index]] for index, row in enumerate(matrix)]
    for column in range(size):
        pivot = next((row for row in range(column, size) if augmented[row][column] != 0), None)
        if pivot is None:
            raise ValueError(f"{label} is singular")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [entry / pivot_value for entry in augmented[column]]
        for row in range(size):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor:
                augmented[row] = [entry - factor * pivot_entry for entry, pivot_entry in zip(augmented[row], augmented[column], strict=True)]
    return [row[-1] for row in augmented]


def barycentric_coordinates(vertices: list[list[Fraction]], point: list[Fraction]) -> list[Fraction]:
    dimension = len(point)
    if len(vertices) != dimension + 1:
        raise ValueError("a full-dimensional simplex in R^n needs exactly n+1 vertices")
    if any(len(vertex) != dimension for vertex in vertices):
        raise ValueError("simplex vertices and interior_point must have the same dimension")
    # The columns are (v_i, 1), so a solution is precisely the barycentric vector.
    system = [[vertices[column][row] for column in range(dimension + 1)] for row in range(dimension)]
    system.append([Fraction(1) for _ in vertices])
    return solve_square(system, [*point, Fraction(1)], "simplex vertex matrix")


def affine_combination(weights: list[Fraction], values: list[list[Fraction]]) -> list[Fraction]:
    return [sum((weights[index] * values[index][coordinate] for index in range(len(weights))), Fraction(0)) for coordinate in range(len(values[0]))]


def parse_polyhedron(value: Any, joint_dimension: int) -> tuple[list[list[Fraction]], list[Fraction]]:
    if not isinstance(value, dict):
        raise ValueError("graph_polyhedron must be an object with normals and bounds")
    normals = vectors(value.get("normals"), "graph_polyhedron.normals")
    if any(len(normal) != joint_dimension for normal in normals):
        raise ValueError(f"every graph_polyhedron normal must have joint dimension {joint_dimension}")
    bounds = vector(value.get("bounds"), "graph_polyhedron.bounds", len(normals))
    return normals, bounds


def satisfies_polyhedron(point: list[Fraction], normals: list[list[Fraction]], bounds: list[Fraction]) -> bool:
    return all(sum((normal[index] * point[index] for index in range(len(point))), Fraction(0)) <= bound for normal, bound in zip(normals, bounds, strict=True))


def certify(payload: object) -> dict[str, object]:
    if not isinstance(payload, dict):
        raise ValueError("top-level JSON value must be an object")
    vertices = vectors(payload.get("vertices"), "vertices")
    domain_dimension = len(vertices[0])
    if len(vertices) != domain_dimension + 1:
        raise ValueError("vertices must describe a full-dimensional simplex: exactly n+1 vertices in R^n")
    responses = vectors(payload.get("responses"), "responses", len(vertices))
    response_dimension = len(responses[0])
    point = vector(payload.get("interior_point"), "interior_point", domain_dimension)
    weights = barycentric_coordinates(vertices, point)
    if any(weight <= 0 for weight in weights):
        raise ValueError("interior_point is not in the strict interior of the supplied simplex")
    selector = affine_combination(weights, responses)
    graph_points = [vertex + response for vertex, response in zip(vertices, responses, strict=True)]
    selector_graph_point = point + selector

    polyhedron = payload.get("graph_polyhedron")
    if polyhedron is not None:
        normals, bounds = parse_polyhedron(polyhedron, domain_dimension + response_dimension)
        failed_vertices = [index for index, graph_point in enumerate(graph_points) if not satisfies_polyhedron(graph_point, normals, bounds)]
        if failed_vertices:
            raise ValueError(f"responses at vertices {failed_vertices} do not belong to graph_polyhedron")
        # Finite intersections of affine half-spaces are convex.  The following
        # direct check is redundant mathematically, but exposes an implementation
        # or encoding error in the certificate.
        if not satisfies_polyhedron(selector_graph_point, normals, bounds):
            raise ValueError("exact affine combination failed graph_polyhedron membership")
        graph_status = "polyhedral convex graph and all displayed memberships verified exactly"
        membership_status = "verified in supplied rational graph_polyhedron"
        certificate_status = "certified"
    else:
        if payload.get("declared_convex_graph_contract") is not True:
            raise ValueError("supply graph_polyhedron, or set declared_convex_graph_contract to true for a conditional result")
        graph_status = "caller-declared convex graph plus caller-declared vertex memberships; not independently verified"
        membership_status = "conditional on the declared contract"
        certificate_status = "conditional"

    return {
        "status": certificate_status,
        "domain_dimension": domain_dimension,
        "response_dimension": response_dimension,
        "barycentric_coordinates": [str(weight) for weight in weights],
        "strict_interior_verified": True,
        "local_affine_selector_at_interior_point": [str(value) for value in selector],
        "vertex_graph_membership": membership_status,
        "convexity_contract": graph_status,
        "proof": "The barycentric weights are positive and sum to one. Each (v_i, y_i) lies in the convex graph, so their same-weight affine combination (x_0, A(x_0)) lies in that graph.",
        "scope": "Finite-dimensional, one supplied full-dimensional rational simplex and one certified interior point only. This does not establish graph measurability, Borel/analytic selection, an argmax selector, a global selector, a patching theorem, or any infinite-dimensional result.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON certificate input")
    args = parser.parse_args()
    try:
        result = certify(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
