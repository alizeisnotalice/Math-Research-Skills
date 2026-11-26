#!/usr/bin/env python3
"""Verify a supplied finite monochromatic protocol partition with rank-halving splits."""

from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path


def exact_rank(rows: list[list[int]]) -> int:
    if not rows or not rows[0]:
        return 0
    matrix = [[Fraction(entry) for entry in row] for row in rows]
    pivot_row = 0
    for column in range(len(matrix[0])):
        source = next((index for index in range(pivot_row, len(matrix)) if matrix[index][column]), None)
        if source is None:
            continue
        matrix[pivot_row], matrix[source] = matrix[source], matrix[pivot_row]
        pivot = matrix[pivot_row][column]
        matrix[pivot_row] = [entry / pivot for entry in matrix[pivot_row]]
        for index, row in enumerate(matrix):
            if index != pivot_row and row[column]:
                factor = row[column]
                matrix[index] = [entry - factor * basis for entry, basis in zip(row, matrix[pivot_row])]
        pivot_row += 1
        if pivot_row == len(matrix):
            break
    return pivot_row


def submatrix(matrix: list[list[int]], rows: list[int], columns: list[int]) -> list[list[int]]:
    return [[matrix[row][column] for column in columns] for row in rows]


def indices(value: object, permitted: list[int], field: str) -> list[int]:
    if not isinstance(value, list) or not value:
        raise ValueError(f"{field} must be a nonempty list")
    if any(type(index) is not int or index not in permitted for index in value):
        raise ValueError(f"{field} contains an index outside its parent rectangle")
    if len(set(value)) != len(value):
        raise ValueError(f"{field} has repeated indices")
    return sorted(value)


def verify_node(
    matrix: list[list[int]],
    node: object,
    rows: list[int],
    columns: list[int],
    depth: int,
) -> tuple[list[dict], list[dict]]:
    if not isinstance(node, dict):
        raise ValueError("each tree node must be an object")
    kind = node.get("kind")
    values = {matrix[row][column] for row in rows for column in columns}
    if kind == "leaf":
        if len(values) != 1:
            raise ValueError("a leaf rectangle is not monochromatic")
        return ([{"rows": rows, "columns": columns, "value": values.pop(), "area": len(rows) * len(columns)}], [])
    if kind != "split":
        raise ValueError("node kind must be leaf or split")
    a_rows = indices(node.get("a_rows"), rows, "a_rows")
    b_columns = indices(node.get("b_cols"), columns, "b_cols")
    block_values = {matrix[row][column] for row in a_rows for column in b_columns}
    if len(block_values) != 1:
        raise ValueError("the announced monochromatic rectangle is not monochromatic")
    a_set, b_set = set(a_rows), set(b_columns)
    ac_rows = [row for row in rows if row not in a_set]
    bc_columns = [column for column in columns if column not in b_set]
    parent_rank = exact_rank(submatrix(matrix, rows, columns))
    cross_ranks = {
        "A_x_Bc": exact_rank(submatrix(matrix, a_rows, bc_columns)),
        "Ac_x_B": exact_rank(submatrix(matrix, ac_rows, b_columns)),
    }
    branch = node.get("low_rank_branch")
    if branch not in cross_ranks:
        raise ValueError("low_rank_branch must be A_x_Bc or Ac_x_B")
    if cross_ranks[branch] > (parent_rank + 1) // 2:
        raise ValueError("the selected cross block does not satisfy the rank-halving bound")
    if branch == "A_x_Bc":
        low_rows, low_columns = a_rows, bc_columns
        residual_rows, residual_columns = ac_rows, columns
    else:
        low_rows, low_columns = ac_rows, b_columns
        residual_rows, residual_columns = rows, bc_columns
    low_child = node.get("low_child")
    residual_child = node.get("residual_child")
    if low_rows and low_columns:
        if low_child is None:
            raise ValueError("a nonempty low-rank block needs low_child")
        low_leaves, low_splits = verify_node(matrix, low_child, low_rows, low_columns, depth + 1)
    elif low_child is not None:
        raise ValueError("an empty low-rank block cannot have low_child")
    else:
        low_leaves, low_splits = [], []
    if residual_rows and residual_columns:
        if residual_child is None:
            raise ValueError("a nonempty residual block needs residual_child")
        residual_leaves, residual_splits = verify_node(matrix, residual_child, residual_rows, residual_columns, depth + 1)
    elif residual_child is not None:
        raise ValueError("an empty residual block cannot have residual_child")
    else:
        residual_leaves, residual_splits = [], []
    rectangle_leaf = {"rows": a_rows, "columns": b_columns, "value": block_values.pop(), "area": len(a_rows) * len(b_columns)}
    split = {
        "depth": depth,
        "parent_rows": rows,
        "parent_columns": columns,
        "parent_rank": parent_rank,
        "rectangle_uniform_density": str(Fraction(rectangle_leaf["area"], len(rows) * len(columns))),
        "complementary_block_ranks": cross_ranks,
        "low_rank_branch": branch,
        "rank_halving_bound": (parent_rank + 1) // 2,
        "selected_rank": cross_ranks[branch],
        "area_partition_verified": rectangle_leaf["area"]
        + len(low_rows) * len(low_columns)
        + len(residual_rows) * len(residual_columns)
        == len(rows) * len(columns),
    }
    return [rectangle_leaf] + low_leaves + residual_leaves, [split] + low_splits + residual_splits


def validate(payload: object) -> dict:
    if not isinstance(payload, dict):
        raise ValueError("input must be a JSON object")
    matrix = payload.get("rows")
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) and row for row in matrix):
        raise ValueError("rows must be a nonempty rectangular list")
    width = len(matrix[0])
    if any(len(row) != width or any(type(entry) is not int or entry not in (0, 1) for entry in row) for row in matrix):
        raise ValueError("rows must be a rectangular Boolean matrix")
    leaves, splits = verify_node(matrix, payload.get("tree"), list(range(len(matrix))), list(range(width)), 0)
    total_area = sum(leaf["area"] for leaf in leaves)
    expected_area = len(matrix) * width
    if total_area != expected_area:
        raise ValueError("leaf areas do not cover the input matrix")
    leaf_cells = {(row, column) for leaf in leaves for row in leaf["rows"] for column in leaf["columns"]}
    if len(leaf_cells) != expected_area:
        raise ValueError("leaf rectangles overlap or fail to partition the input matrix")
    if not all(split["area_partition_verified"] for split in splits):
        raise ValueError("a split does not partition its parent rectangle")
    return {
        "shape": [len(matrix), width],
        "input_rank": exact_rank(matrix),
        "split_count": len(splits),
        "leaf_count": len(leaves),
        "partition_verified": True,
        "maximum_selected_rank": max((split["selected_rank"] for split in splits), default=0),
        "splits": splits,
        "leaves": leaves,
        "scope": "A supplied finite protocol partition. It does not find rectangles or establish a uniform density theorem.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = validate(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
