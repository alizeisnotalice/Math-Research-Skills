#!/usr/bin/env python3
"""Exact finite audit of the two-recursive-potential energy lemma.

The input is JSON.  Each node has ``id``, ``parent`` (null only at the root),
and rational nonnegative fields ``P``, ``Q``, ``P_prime``, ``Q_prime``.
``selected_leaves`` specifies the set J in Lemma 3.1 of the source.

The checker certifies all *supplied-field* hypotheses and then exactly checks
    sum_{b in J} d_b^2 <= [d_o(2P_o+d_o)(2Q_o+d_o)]^(2/3).
It does not construct fields from a normed space or infer any infinite-tree,
completion, or midpoint-modulus statement.
"""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


FIELDS = ("P", "Q", "P_prime", "Q_prime")


def rational(x: Any) -> Fraction:
    if isinstance(x, bool):
        raise ValueError("Boolean is not a rational field value")
    return Fraction(str(x))


def parse(payload: dict[str, Any]) -> tuple[str, dict[str, dict[str, Fraction]], dict[str, list[str]], set[str]]:
    if not isinstance(payload.get("nodes"), list) or not payload["nodes"]:
        raise ValueError("nodes must be a nonempty list")
    nodes: dict[str, dict[str, Fraction]] = {}
    parent: dict[str, str | None] = {}
    for raw in payload["nodes"]:
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str) or not raw["id"]:
            raise ValueError("each node needs a nonempty string id")
        name = raw["id"]
        if name in nodes:
            raise ValueError(f"duplicate node id: {name}")
        if set(FIELDS) - raw.keys():
            raise ValueError(f"node {name} lacks one of P,Q,P_prime,Q_prime")
        if raw.get("parent") is not None and not isinstance(raw.get("parent"), str):
            raise ValueError(f"parent of {name} must be a string or null")
        nodes[name] = {field: rational(raw[field]) for field in FIELDS}
        if any(value < 0 for value in nodes[name].values()):
            raise ValueError(f"all fields must be nonnegative at {name}")
        parent[name] = raw.get("parent")
    roots = [name for name, above in parent.items() if above is None]
    if len(roots) != 1:
        raise ValueError("the data must have exactly one root")
    root = roots[0]
    children = {name: [] for name in nodes}
    for name, above in parent.items():
        if above is not None:
            if above not in nodes:
                raise ValueError(f"parent {above} of {name} is absent")
            if above == name:
                raise ValueError(f"self-parenting node: {name}")
            children[above].append(name)
    # A finite parent graph with a unique root is a rooted tree exactly when all
    # nodes reach it; this also rejects disconnected cycles.
    for name in nodes:
        trail: set[str] = set()
        cursor = name
        while cursor != root:
            if cursor in trail:
                raise ValueError(f"cycle above {name}")
            trail.add(cursor)
            above = parent[cursor]
            if above is None:
                raise ValueError(f"node {name} is disconnected from root")
            cursor = above
    chosen = payload.get("selected_leaves")
    if not isinstance(chosen, list) or not chosen or not all(isinstance(x, str) for x in chosen):
        raise ValueError("selected_leaves must be a nonempty list of ids")
    selected = set(chosen)
    if len(selected) != len(chosen) or not selected <= nodes.keys():
        raise ValueError("selected_leaves must be distinct node ids")
    if any(children[name] for name in selected):
        raise ValueError("each selected node must be a graph leaf")
    return root, nodes, children, selected


def certify(root: str, nodes: dict[str, dict[str, Fraction]], children: dict[str, list[str]], selected: set[str]) -> dict[str, Any]:
    defects: dict[str, Fraction] = {}
    for name, values in nodes.items():
        d_p = values["P_prime"] - values["P"]
        d_q = values["Q_prime"] - values["Q"]
        if d_p != d_q or d_p < 0:
            raise ValueError(f"P_prime-P != Q_prime-Q = d>=0 at {name}")
        defects[name] = d_p
    for name, kids in children.items():
        if not kids:
            continue
        tight = False
        for field in FIELDS:
            left = nodes[name][field] ** 2
            right = sum(nodes[child][field] ** 2 for child in kids)
            if left < right:
                raise ValueError(f"{field} squared child superadditivity fails at {name}")
            if field in ("P", "Q") and left == right:
                tight = True
        if not tight:
            raise ValueError(f"neither P nor Q is tight at internal node {name}")
    for leaf in selected:
        if nodes[leaf]["P"] != 0 or nodes[leaf]["Q"] != 0:
            raise ValueError(f"selected leaf {leaf} must have P=Q=0")
    energy = sum(defects[leaf] ** 2 for leaf in selected)
    root_values = nodes[root]
    root_product = defects[root] * (2 * root_values["P"] + defects[root]) * (2 * root_values["Q"] + defects[root])
    # No floating cube root: for nonnegative quantities E <= R^(2/3) iff E^3 <= R^2.
    if energy ** 3 > root_product ** 2:
        raise AssertionError("the exact Lemma 3.1 energy conclusion failed")
    return {
        "certificate": "two_recursive_potential_tree_energy",
        "root": root,
        "selected_leaf_count": len(selected),
        "boundary_energy_sum_d_squared": str(energy),
        "root_product_d_2P_d_2Q_d": str(root_product),
        "comparison_checked_as_energy_cubed_le_root_product_squared": True,
        "lemma_bound": f"({root_product})^(2/3)",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    args = parser.parse_args()
    try:
        raw = json.loads(args.input.read_text(encoding="utf-8"))
        root, nodes, children, selected = parse(raw)
        print(json.dumps(certify(root, nodes, children, selected), indent=2, sort_keys=True))
    except (OSError, ValueError, TypeError, json.JSONDecodeError) as exc:
        print(f"input rejected: {exc}", file=sys.stderr)
        raise SystemExit(2) from exc


if __name__ == "__main__":
    main()
