#!/usr/bin/env python3
"""Compile finite conditional or causal transport equalities and verify a witness."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path

from finite_constrained_transport_certificate import certify, q, qs


def read_marginals(data: dict) -> list[list[Fraction]]:
    raw = data.get("marginals")
    if not isinstance(raw, list) or len(raw) != 2 or any(not isinstance(row, list) or not row for row in raw):
        raise ValueError("marginals must contain exactly two nonempty mass arrays")
    result = [[q(value) for value in row] for row in raw]
    if any(any(value < 0 for value in row) or sum(row) != 1 for row in result):
        raise ValueError("each marginal must be a probability vector")
    return result


def read_labels(values: object, count: int, label: str) -> list[str]:
    if not isinstance(values, list) or len(values) != count or any(not isinstance(v, str) or not v for v in values):
        raise ValueError(f"{label} must contain {count} nonempty strings")
    return values


def read_paths(raw: object, count: int, label: str) -> list[tuple[str, ...]]:
    if not isinstance(raw, list) or len(raw) != count or not isinstance(raw[0], list) or not raw[0]:
        raise ValueError(f"{label} must contain {count} nonempty paths on one finite grid")
    width = len(raw[0])
    paths = [tuple(read_labels(row, width, label)) for row in raw]
    if len(set(paths)) != count:
        raise ValueError(f"{label} must have distinct paths")
    return paths


def prefix_groups(paths: list[tuple[str, ...]], mass: list[Fraction], time: int) -> list[list[int]]:
    groups: dict[tuple[str, ...], list[int]] = defaultdict(list)
    for index, (path, probability) in enumerate(zip(paths, mass, strict=True)):
        if probability > 0:
            groups[path[:time]].append(index)
    return list(groups.values())


def causal_rows(x_paths: list[tuple[str, ...]], y_paths: list[tuple[str, ...]],
                mu: list[Fraction], nu: list[Fraction], reverse: bool = False):
    if reverse:
        x_paths, y_paths, mu, nu = y_paths, x_paths, nu, mu
    n_x, n_y = len(mu), len(nu)
    n_target = n_x if reverse else n_y
    direction = "reverse" if reverse else "forward"
    for time in range(1, len(x_paths[0])):
        x_groups = prefix_groups(x_paths, mu, time)
        y_groups = prefix_groups(y_paths, nu, time)
        for group in x_groups:
            total = sum(mu[i] for i in group)
            for selected in group[:-1]:
                for targets in y_groups[:-1]:
                    values = ["0"] * (n_x * n_y)
                    for i in group:
                        coefficient = qs((total if i == selected else 0) - mu[selected])
                        for j in targets:
                            offset = j * n_target + i if reverse else i * n_target + j
                            values[offset] = coefficient
                    yield {"name": f"{direction}:t{time}:i{selected}:j{targets[0]}", "values": values, "target": "0"}


def stratum_rows(data: dict, mu: list[Fraction], nu: list[Fraction]) -> list[dict]:
    left = read_labels(data.get("source_strata"), len(mu), "source_strata")
    right = read_labels(data.get("target_strata"), len(nu), "target_strata")
    left_mass: dict[str, Fraction] = defaultdict(Fraction)
    right_mass: dict[str, Fraction] = defaultdict(Fraction)
    for label, mass in zip(left, mu, strict=True):
        left_mass[label] += mass
    for label, mass in zip(right, nu, strict=True):
        right_mass[label] += mass
    if any(left_mass.get(label, 0) != right_mass.get(label, 0) for label in left_mass.keys() | right_mass.keys()):
        raise ValueError("the two marginals must have the same mass in each stratum")
    values = [str(int(a != b)) for a in left for b in right]
    return [{"name": "within-strata", "values": values, "target": "0"}] if "1" in values else []


def constraints(data: object) -> list[dict]:
    if not isinstance(data, dict):
        raise ValueError("input must be a JSON object")
    if "constraints" in data:
        raise ValueError("this interface generates the full constraint list")
    mu, nu = read_marginals(data)
    model = data.get("model")
    if model == "conditional":
        return stratum_rows(data, mu, nu)
    if model not in ("causal", "bicausal"):
        raise ValueError("model must be conditional, causal or bicausal")
    x_paths = read_paths(data.get("source_paths"), len(mu), "source_paths")
    y_paths = read_paths(data.get("target_paths"), len(nu), "target_paths")
    if len(x_paths[0]) != len(y_paths[0]):
        raise ValueError("source and target paths must use the same grid length")
    rows = list(causal_rows(x_paths, y_paths, mu, nu))
    if model == "bicausal":
        rows.extend(causal_rows(x_paths, y_paths, mu, nu, reverse=True))
    return rows


def audit(data: dict) -> dict:
    compiled = constraints(data)
    result = certify({**data, "constraints": compiled})
    return {"model": data["model"], "compiled_constraint_names": [row["name"] for row in compiled], **result}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--constraints-only", action="store_true")
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        if args.constraints_only:
            print(json.dumps({"constraints": constraints(data)}, indent=2))
            return 0
        result = audit(data)
    except (OSError, TypeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["attainment_witness"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
