#!/usr/bin/env python3
"""Certify the leaf-count balancing step for a supplied full binary tree."""

from __future__ import annotations

import argparse
import json
import sys
from functools import cache
from pathlib import Path
from typing import Any


def leaf_count(node: Any) -> int:
    """Validate the deliberately small JSON grammar and return the leaf count."""
    if node is None:
        return 1
    if not isinstance(node, dict) or set(node) != {"left", "right"}:
        raise ValueError("each internal node must have exactly the keys left and right; a leaf is null")
    return leaf_count(node["left"]) + leaf_count(node["right"])


def ceiling_log_three_halves(leaves: int) -> tuple[int, int, int]:
    """Return d and the exact certificate 3**d >= leaves * 2**d."""
    exponent, numerator, denominator = 0, 1, 1
    while numerator < leaves * denominator:
        exponent += 1
        numerator *= 3
        denominator *= 2
    return exponent, numerator, leaves * denominator


def balanced_child(tree: Any) -> dict[str, Any]:
    """Implement the walk in Proposition A.3 using only integer comparisons."""
    total = leaf_count(tree)
    if total < 2:
        raise ValueError("the balancing step requires a tree with at least two leaves")

    node = tree
    parent_path: list[str] = []
    while True:
        if node is None:
            raise AssertionError("a node above two-thirds of the root cannot be a leaf")
        left_leaves, right_leaves = leaf_count(node["left"]), leaf_count(node["right"])
        if left_leaves >= right_leaves:
            side, heavy, light = "left", left_leaves, right_leaves
        else:
            side, heavy, light = "right", right_leaves, left_leaves

        # heavy <= 2 total / 3 and heavy > total / 3, exactly as in the paper.
        if 3 * heavy <= 2 * total:
            if 3 * heavy <= total:
                raise AssertionError("the heavier child should be larger than one third of the root")
            return {
                "root_leaf_count": total,
                "parent_path": parent_path,
                "parent_leaf_count": left_leaves + right_leaves,
                "selected_child": side,
                "selected_leaf_count": heavy,
                "sibling_leaf_count": light,
                "selected_between_one_third_and_two_thirds": True,
                "remaining_tree_leaf_count": total - heavy,
                "remaining_tree_strictly_below_two_thirds": 3 * (total - heavy) < 2 * total,
            }

        # This child is still larger than two thirds of the root, so continue.
        node = node[side]
        parent_path.append(side)


def certify(tree: Any) -> dict[str, Any]:
    witness = balanced_child(tree)
    exponent, left_side, right_side = ceiling_log_three_halves(witness["root_leaf_count"])
    return {
        "tree_is_full_binary": True,
        "balancing_witness": witness,
        "two_membership_query_depth_upper_bound": 2 * exponent,
        "ceiling_log_three_halves": exponent,
        "exact_depth_bound_certificate": f"3^{exponent} = {left_side} >= {right_side} = L*2^{exponent}",
        "scope": (
            "Leaf-count certificate only. It does not verify that a tree is a communication protocol, "
            "that its leaves are monochromatic, or that a matrix has a uniform rectangle-density bound."
        ),
    }


@cache
def full_binary_shapes(leaves: int) -> tuple[Any, ...]:
    if leaves == 1:
        return (None,)
    shapes: list[Any] = []
    for left_leaves in range(1, leaves):
        for left in full_binary_shapes(left_leaves):
            for right in full_binary_shapes(leaves - left_leaves):
                shapes.append({"left": left, "right": right})
    return tuple(shapes)


def self_test() -> dict[str, int]:
    """Exhaustively exercise all ordered full binary shapes with 2 through 10 leaves."""
    checked = 0
    for leaves in range(2, 11):
        for tree in full_binary_shapes(leaves):
            result = certify(tree)
            witness = result["balancing_witness"]
            if not (3 * witness["selected_leaf_count"] > leaves and 3 * witness["selected_leaf_count"] <= 2 * leaves):
                raise AssertionError("selected child violates the one-third/two-thirds interval")
            if not witness["remaining_tree_strictly_below_two_thirds"]:
                raise AssertionError("replacement tree is not strictly below two thirds")
            checked += 1
    return {"leaf_counts_checked": 9, "ordered_full_binary_shapes_checked": checked}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, help="JSON object with a `tree` field")
    parser.add_argument("--self-test", action="store_true", help="exhaustively test shapes with 2..10 leaves")
    args = parser.parse_args()
    if args.self_test == (args.input is not None):
        parser.error("supply exactly one of an input JSON file or --self-test")
    try:
        if args.self_test:
            output: object = self_test()
        else:
            payload = json.loads(args.input.read_text(encoding="utf-8"))
            if not isinstance(payload, dict) or set(payload) != {"tree"}:
                raise ValueError("input must be an object with exactly one field: tree")
            output = certify(payload["tree"])
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(output, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
