#!/usr/bin/env python3
"""Exact verifier for a supplied finite HBL graph presentation.

All input scalars are integers or rational strings accepted by Fraction.  The
program verifies a *witness*; it never searches for one or computes an HBL
constant.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


class InputError(ValueError):
    pass


def q(x):
    if isinstance(x, bool) or isinstance(x, float):
        raise InputError("scalars must be exact integers or rational strings, never bool/float")
    try:
        return Fraction(x)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise InputError(f"not an exact rational: {x!r}") from exc


def rref_rank(rows):
    """Exact row rank over Q; the zero-by-d matrix has rank zero."""
    a = [list(row) for row in rows]
    if not a:
        return 0
    m, n, lead = len(a), len(a[0]), 0
    for col in range(n):
        pivot = next((r for r in range(lead, m) if a[r][col] != 0), None)
        if pivot is None:
            continue
        a[lead], a[pivot] = a[pivot], a[lead]
        p = a[lead][col]
        a[lead] = [x / p for x in a[lead]]
        for r in range(m):
            if r != lead and a[r][col] != 0:
                f = a[r][col]
                a[r] = [a[r][c] - f * a[lead][c] for c in range(n)]
        lead += 1
        if lead == m:
            break
    return lead


def matrix(value, ncols, label):
    if not isinstance(value, list):
        raise InputError(f"{label} must be a list of rows")
    ans = []
    for r, row in enumerate(value):
        if not isinstance(row, list) or len(row) != ncols:
            raise InputError(f"{label}[{r}] must have exactly {ncols} entries")
        ans.append([q(x) for x in row])
    return ans


def image_rank(map_rows, subspace_rows):
    # A subspace row b represents b in H; its image is A b^T.
    images = [[sum(a[j] * b[j] for j in range(len(b))) for a in map_rows]
              for b in subspace_rows]
    return rref_rank(images)


def serialize(x):
    if isinstance(x, Fraction):
        return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x, dict):
        return {k: serialize(v) for k, v in x.items()}
    if isinstance(x, list):
        return [serialize(v) for v in x]
    return x


def scalar_chain_decomposition(edge_ids, edges, incoming, outgoing, zero, top, weights):
    """Greedy exact path-flow decomposition (the scalar instance of Prop. 1)."""
    rem = dict(weights)
    pieces = []
    while any(rem[e] > 0 for e in edge_ids):
        first = next(e for e in edge_ids if rem[e] > 0)
        chain = [first]
        vertex = edges[first][0]
        while vertex != zero:
            candidates = [e for e in incoming[vertex] if rem[e] > 0]
            if not candidates:
                raise InputError("positive flow cannot be extended backward; balance was not established")
            edge = candidates[0]
            chain.insert(0, edge)
            vertex = edges[edge][0]
        vertex = edges[first][1]
        while vertex != top:
            candidates = [e for e in outgoing[vertex] if rem[e] > 0]
            if not candidates:
                raise InputError("positive flow cannot be extended forward; balance was not established")
            edge = candidates[0]
            chain.append(edge)
            vertex = edges[edge][1]
        delta = min(rem[e] for e in chain)
        for edge in chain:
            rem[edge] -= delta
        pieces.append({"coefficient": delta, "edge_ids": chain})
    return pieces


def check(data):
    errors = []
    try:
        d = data["ambient_dimension"]
        if isinstance(d, bool) or not isinstance(d, int) or d <= 0:
            raise InputError("ambient_dimension must be a positive integer")
        vertices_raw = data["vertices"]
        if not isinstance(vertices_raw, list) or not vertices_raw:
            raise InputError("vertices must be a nonempty list")
        vertices, dims = {}, {}
        for item in vertices_raw:
            ident = item["id"]
            if not isinstance(ident, str) or not ident or ident in vertices:
                raise InputError("vertex ids must be unique nonempty strings")
            basis = matrix(item.get("basis", []), d, f"basis of {ident}")
            vertices[ident] = basis
            dims[ident] = rref_rank(basis)
        zero, top = data["zero_vertex"], data["ambient_vertex"]
        if zero not in vertices or top not in vertices or zero == top:
            raise InputError("zero_vertex and ambient_vertex must be distinct listed vertices")
        if dims[zero] != 0:
            errors.append("zero_vertex does not have rank 0")
        if dims[top] != d:
            errors.append("ambient_vertex does not have rank ambient_dimension")

        edges_raw = data["edges"]
        if not isinstance(edges_raw, list) or not edges_raw:
            raise InputError("edges must be a nonempty list")
        edges, edge_ids = {}, []
        incoming, outgoing = defaultdict(list), defaultdict(list)
        for item in edges_raw:
            ident, u, v = item["id"], item["source"], item["target"]
            if not isinstance(ident, str) or not ident or ident in edges:
                raise InputError("edge ids must be unique nonempty strings")
            if u not in vertices or v not in vertices:
                raise InputError(f"edge {ident} references an unknown vertex")
            edges[ident] = (u, v); edge_ids.append(ident)
            incoming[v].append(ident); outgoing[u].append(ident)
            if dims[v] != dims[u] + 1:
                errors.append(f"edge {ident}: target rank is not source rank plus one")
            if rref_rank(vertices[u] + vertices[v]) != dims[v]:
                errors.append(f"edge {ident}: source row-space is not contained in target row-space")
        edge_ids.sort()
        for ident in vertices:
            incoming[ident].sort(); outgoing[ident].sort()
            if ident != zero and not incoming[ident]:
                errors.append(f"vertex {ident}: missing incoming edge")
            if ident != top and not outgoing[ident]:
                errors.append(f"vertex {ident}: missing outgoing edge")

        maps_raw = data["maps"]
        theta_raw = data["theta"]
        if not isinstance(maps_raw, list) or not maps_raw or not isinstance(theta_raw, dict):
            raise InputError("maps must be a nonempty list and theta an object")
        maps, theta, taus = {}, {}, {}
        for item in maps_raw:
            ident = item["id"]
            if not isinstance(ident, str) or not ident or ident in maps:
                raise InputError("map ids must be unique nonempty strings")
            rows = matrix(item["matrix"], d, f"matrix of {ident}")
            if not rows:
                raise InputError(f"matrix of {ident} must have at least one codomain row")
            tau = q(item["tau"])
            if not (0 <= tau <= 1):
                errors.append(f"map {ident}: tau is outside [0,1]")
            if ident not in theta_raw or not isinstance(theta_raw[ident], dict):
                raise InputError(f"theta[{ident}] must be an object with every edge id")
            if set(theta_raw[ident]) != set(edge_ids):
                raise InputError(f"theta[{ident}] must supply exactly the listed edge ids")
            values = {e: q(theta_raw[ident][e]) for e in edge_ids}
            for e, value in values.items():
                if value < 0:
                    errors.append(f"theta[{ident}][{e}] is negative")
            maps[ident], theta[ident], taus[ident] = rows, values, tau
        if set(theta_raw) != set(maps):
            raise InputError("theta must contain no map ids other than the listed maps")

        def balance(label, values, expected_mass):
            mass = sum(values[e] for e in outgoing[zero])
            if mass != expected_mass:
                errors.append(f"{label}: total mass {mass} is not {expected_mass}")
            terminal = sum(values[e] for e in incoming[top])
            if terminal != mass:
                errors.append(f"{label}: mass entering ambient vertex {terminal} differs from source mass {mass}")
            for vertex in vertices:
                if vertex not in (zero, top):
                    left = sum(values[e] for e in incoming[vertex])
                    right = sum(values[e] for e in outgoing[vertex])
                    if left != right:
                        errors.append(f"{label}: unbalanced at {vertex} ({left} in, {right} out)")

        for ident in maps:
            balance(f"theta[{ident}]", theta[ident], taus[ident])
        summary = {}
        changed = {ident: {} for ident in maps}
        for edge, (u, v) in edges.items():
            summary[edge] = Fraction(0)
            for ident, rows in maps.items():
                changed[ident][edge] = image_rank(rows, vertices[u]) != image_rank(rows, vertices[v])
                if changed[ident][edge]:
                    summary[edge] += theta[ident][edge]
        balance("summary", summary, Fraction(1))

        result = {
            "valid": not errors,
            "errors": errors,
            "vertex_dimensions": dims,
            "summary_weights": summary,
            "image_changes": changed,
        }
        if not errors:
            decompositions = {}
            for ident in maps:
                parts = scalar_chain_decomposition(edge_ids, edges, incoming, outgoing, zero, top, theta[ident])
                rebuilt = {e: sum(p["coefficient"] for p in parts if e in p["edge_ids"]) for e in edge_ids}
                if rebuilt != theta[ident]:
                    raise AssertionError("internal exact reconstruction failure")
                decompositions[ident] = parts
            result["scalar_chain_decompositions"] = decompositions
            result["scope"] = ("Exact verification of a supplied rational graph presentation; "
                               "not a witness search or a numerical HBL-constant computation.")
        return serialize(result)
    except (KeyError, InputError) as exc:
        return {"valid": False, "errors": [str(exc)]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON graph-presentation witness")
    parser.add_argument("-o", "--output", type=Path, help="write JSON result here (default: stdout)")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"cannot read input JSON: {exc}")
    result = check(data)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    raise SystemExit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
