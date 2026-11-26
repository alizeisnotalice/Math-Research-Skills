#!/usr/bin/env python3
"""Exact primal--dual certificate for transport on a finite weighted *tree*.

The program deliberately has no general-graph mode.  A spanning tree of a graph is
not thereby optimal for that graph's shortest-path transport problem.
"""

from __future__ import annotations

import argparse
from collections import deque
import json
import sys
from collections import deque
from fractions import Fraction
from pathlib import Path
from typing import Any


class CertificateError(ValueError):
    """An input condition needed by the exact certificate did not hold."""


def q(value: Any, where: str) -> Fraction:
    if isinstance(value, bool):
        raise CertificateError(f"{where} must be an integer or rational string, not boolean")
    try:
        result = Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise CertificateError(f"{where} is not an exact rational: {value!r}") from exc
    return result


def show(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def sign(value: Fraction) -> int:
    return (value > 0) - (value < 0)


def require_tree(data: dict[str, Any]) -> tuple[list[str], str, dict[str, list[tuple[str, Fraction]]]]:
    if not isinstance(data, dict):
        raise CertificateError("top-level JSON must be an object")
    vertices = data.get("vertices")
    if not isinstance(vertices, list) or not vertices or any(not isinstance(v, str) or not v for v in vertices):
        raise CertificateError("vertices must be a nonempty list of distinct nonempty strings")
    if len(set(vertices)) != len(vertices):
        raise CertificateError("vertices contains a duplicate")
    root = data.get("root")
    if root not in vertices:
        raise CertificateError("root must be one of vertices")
    edges = data.get("edges")
    if not isinstance(edges, list) or len(edges) != len(vertices) - 1:
        raise CertificateError("a tree on |V| vertices must provide exactly |V|-1 edges")
    adj: dict[str, list[tuple[str, Fraction]]] = {v: [] for v in vertices}
    seen: set[frozenset[str]] = set()
    for i, edge in enumerate(edges):
        if not isinstance(edge, dict):
            raise CertificateError(f"edges[{i}] must be an object")
        u, v = edge.get("u"), edge.get("v")
        if not isinstance(u, str) or not isinstance(v, str) or u not in adj or v not in adj or u == v:
            raise CertificateError(f"edges[{i}] must join two distinct listed vertices")
        key = frozenset((u, v))
        if key in seen:
            raise CertificateError(f"edges[{i}] duplicates an undirected edge")
        seen.add(key)
        length = q(edge.get("length"), f"edges[{i}].length")
        if length <= 0:
            raise CertificateError(f"edges[{i}].length must be strictly positive")
        adj[u].append((v, length))
        adj[v].append((u, length))
    reached = {root}
    todo = [root]
    while todo:
        u = todo.pop()
        for v, _ in adj[u]:
            if v not in reached:
                reached.add(v)
                todo.append(v)
    if len(reached) != len(vertices):
        raise CertificateError("edges are not connected; this is not a tree")
    return vertices, root, adj


def measure(data: Any, vertices: list[str], name: str) -> dict[str, Fraction]:
    if not isinstance(data, dict):
        raise CertificateError(f"{name} must be an object mapping vertices to exact rationals")
    extra = set(data) - set(vertices)
    if extra:
        raise CertificateError(f"{name} assigns an unknown vertex: {sorted(extra)[0]!r}")
    result = {v: q(data.get(v, "0"), f"{name}[{v!r}]") for v in vertices}
    if any(x < 0 for x in result.values()):
        raise CertificateError(f"{name} must be nonnegative")
    if sum(result.values(), Fraction()) != 1:
        raise CertificateError(f"{name} must have total mass exactly 1")
    return result


def rooted_tree(vertices: list[str], root: str, adj: dict[str, list[tuple[str, Fraction]]]):
    parent: dict[str, str | None] = {root: None}
    edge_to_parent: dict[str, Fraction] = {}
    depth = {root: 0}
    dist_root = {root: Fraction()}
    order: list[str] = []
    todo: deque[str] = deque([root])
    while todo:
        u = todo.popleft()
        order.append(u)
        for v, length in adj[u]:
            if v in parent:
                continue
            parent[v] = u
            edge_to_parent[v] = length
            depth[v] = depth[u] + 1
            dist_root[v] = dist_root[u] + length
            todo.append(v)
    assert len(order) == len(vertices)  # established by require_tree
    return parent, edge_to_parent, depth, dist_root, order


def tree_distance(a: str, b: str, parent: dict[str, str | None], depth: dict[str, int], dist_root: dict[str, Fraction]) -> Fraction:
    x, y = a, b
    while depth[x] > depth[y]:
        assert parent[x] is not None
        x = parent[x]
    while depth[y] > depth[x]:
        assert parent[y] is not None
        y = parent[y]
    while x != y:
        assert parent[x] is not None and parent[y] is not None
        x, y = parent[x], parent[y]
    return dist_root[a] + dist_root[b] - 2 * dist_root[x]


def match_inside_subtrees(
    vertices: list[str], order: list[str], parent: dict[str, str | None], imbalance: dict[str, Fraction],
    depth: dict[str, int], dist_root: dict[str, Fraction],
) -> list[tuple[str, str, Fraction, Fraction]]:
    """Produce a coupling of residual supplies/demands, cancelling at each subtree."""
    supplies = {v: deque([[v, imbalance[v]]]) if imbalance[v] > 0 else deque() for v in vertices}
    demands = {v: deque([[v, -imbalance[v]]]) if imbalance[v] < 0 else deque() for v in vertices}
    plan: list[tuple[str, str, Fraction, Fraction]] = []
    for v in reversed(order):
        # At v, every possible source--sink pair is internal to its subtree; matching it
        # prevents unnecessary flow through the parent edge.
        while supplies[v] and demands[v]:
            source, have = supplies[v][0]
            target, need = demands[v][0]
            amount = min(have, need)
            distance = tree_distance(source, target, parent, depth, dist_root)
            plan.append((source, target, amount, distance))
            supplies[v][0][1] -= amount
            demands[v][0][1] -= amount
            if supplies[v][0][1] == 0:
                supplies[v].popleft()
            if demands[v][0][1] == 0:
                demands[v].popleft()
        p = parent[v]
        if p is not None:
            for residuals in (supplies, demands):
                child = residuals.pop(v)
                if len(child) > len(residuals[p]):
                    child.extend(residuals[p])
                    residuals[p] = child
                else:
                    residuals[p].extend(child)
    if supplies[order[0]] or demands[order[0]]:
        raise CertificateError("internal error: equal total masses did not balance")
    return plan


def certificate(data: dict[str, Any]) -> dict[str, Any]:
    vertices, root, adj = require_tree(data)
    mu = measure(data.get("mu"), vertices, "mu")
    nu = measure(data.get("nu"), vertices, "nu")
    parent, length, depth, dist_root, order = rooted_tree(vertices, root, adj)
    imbalance = {v: mu[v] - nu[v] for v in vertices}
    subtree = dict(imbalance)
    for v in reversed(order[1:]):
        assert parent[v] is not None
        subtree[parent[v]] += subtree[v]
    if subtree[root] != 0:
        raise CertificateError("internal error: probability totals did not cancel")

    potential = {root: Fraction()}
    cut_rows = []
    tree_cost = Fraction()
    for v in order[1:]:
        p = parent[v]
        assert p is not None
        potential[v] = potential[p] + length[v] * sign(subtree[v])
        term = length[v] * abs(subtree[v])
        tree_cost += term
        cut_rows.append({"child": v, "parent": p, "subtree_imbalance_mu_minus_nu": show(subtree[v]),
                         "edge_length": show(length[v]), "cut_cost": show(term)})

    shipments = match_inside_subtrees(vertices, order, parent, imbalance, depth, dist_root)
    coupling: list[dict[str, str]] = []
    for v in vertices:
        diagonal = min(mu[v], nu[v])
        if diagonal:
            coupling.append({"from": v, "to": v, "mass": show(diagonal), "distance": "0", "cost": "0"})
    transport_cost = Fraction()
    for source, target, amount, distance in shipments:
        cost = amount * distance
        transport_cost += cost
        coupling.append({"from": source, "to": target, "mass": show(amount), "distance": show(distance), "cost": show(cost)})
    rows = {v: Fraction() for v in vertices}
    cols = {v: Fraction() for v in vertices}
    for entry in coupling:
        amount = q(entry["mass"], "generated coupling mass")
        rows[entry["from"]] += amount
        cols[entry["to"]] += amount
    if rows != mu or cols != nu:
        raise CertificateError("internal error: generated coupling has wrong marginals")

    dual_value = sum((potential[v] * imbalance[v] for v in vertices), Fraction())
    edge_lipschitz = []
    for v in order[1:]:
        p = parent[v]
        assert p is not None
        gap = abs(potential[v] - potential[p])
        if gap > length[v]:
            raise CertificateError("internal error: dual potential violates a tree edge")
        edge_lipschitz.append({"u": p, "v": v, "absolute_potential_gap": show(gap), "edge_length": show(length[v])})
    if not (tree_cost == transport_cost == dual_value):
        raise CertificateError("internal error: exact primal/dual values disagree")

    return {
        "scope": "exact certificate for the metric induced by the supplied weighted tree only; no claim about an ambient graph or spanning-tree optimality",
        "root": root,
        "tree_wasserstein_1": show(tree_cost),
        "cut_formula": cut_rows,
        "potential_rooted_at_zero": {v: show(potential[v]) for v in vertices},
        "dual_value": show(dual_value),
        "tree_edge_lipschitz_certificate": edge_lipschitz,
        "all_tree_edge_cut_imbalances_nonzero": all(subtree[v] != 0 for v in order[1:]),
        "coupling": coupling,
        "transport_cost": show(transport_cost),
        "marginal_balance": {"mu_total": show(sum(rows.values(), Fraction())), "nu_total": show(sum(cols.values(), Fraction())), "verified": True},
        "primal_dual_exact_equality": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Exact finite-tree W1 primal--dual certificate (rationals only).")
    parser.add_argument("input", type=Path, help="JSON tree, measures mu and nu")
    parser.add_argument("--compact", action="store_true", help="emit one JSON line")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if not isinstance(data, dict):
            raise CertificateError("top-level JSON must be an object")
        result = certificate(data)
    except (OSError, json.JSONDecodeError, CertificateError) as exc:
        print(f"certificate error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=None if args.compact else 2, separators=(",", ":") if args.compact else None))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
