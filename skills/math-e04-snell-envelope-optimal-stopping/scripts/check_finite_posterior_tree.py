#!/usr/bin/env python3
"""Check exact posterior barycentres and a stopping policy on a finite tree."""

from __future__ import annotations

import argparse
from fractions import Fraction
import json
import re
from typing import Any


class CertificateError(ValueError):
    """The finite posterior-tree certificate has failed a required condition."""


def rational(value: Any, label: str) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise CertificateError(f"{label} must be a JSON integer or an exact rational string")
    if isinstance(value, str) and not re.fullmatch(r"[+-]?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", value):
        raise CertificateError(f"{label} must be an integer or a p/q string with positive q: {value!r}")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise CertificateError(f"{label} is not an exact rational: {value!r}") from error


def render(value: Any) -> Any:
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if isinstance(value, dict):
        return {key: render(item) for key, item in value.items()}
    if isinstance(value, list):
        return [render(item) for item in value]
    return value


def parse(data: dict[str, Any]) -> tuple[list[Fraction], dict[str, dict[str, Any]], str]:
    if not isinstance(data, dict):
        raise CertificateError("the JSON root must be an object")
    support_raw, raw_nodes = data.get("support"), data.get("nodes")
    if not isinstance(support_raw, list) or not support_raw:
        raise CertificateError("support must be a nonempty exact-rational list")
    support = [rational(item, "support entry") for item in support_raw]
    if len(set(support)) != len(support):
        raise CertificateError("support points must be distinct")
    if not isinstance(raw_nodes, list) or not raw_nodes:
        raise CertificateError("nodes must be a nonempty list")
    nodes: dict[str, dict[str, Any]] = {}
    for raw in raw_nodes:
        if not isinstance(raw, dict) or not isinstance(raw.get("id"), str) or not raw["id"]:
            raise CertificateError("each node needs a nonempty string id")
        identifier = raw["id"]
        if identifier in nodes:
            raise CertificateError(f"duplicate node id {identifier}")
        weights_raw = raw.get("weights")
        if not isinstance(weights_raw, list) or len(weights_raw) != len(support):
            raise CertificateError(f"{identifier}: weights need one entry per support point")
        weights = [rational(item, f"{identifier} weight") for item in weights_raw]
        if any(item < 0 for item in weights) or sum(weights, Fraction(0)) != 1:
            raise CertificateError(f"{identifier}: weights must be nonnegative and sum to one")
        children_raw = raw.get("children", [])
        if type(raw.get("stop")) is not bool or not isinstance(children_raw, list):
            raise CertificateError(f"{identifier}: stop must be boolean and children a list")
        children = []
        for edge in children_raw:
            if not isinstance(edge, dict) or not isinstance(edge.get("id"), str):
                raise CertificateError(f"{identifier}: child id is missing")
            children.append((edge["id"], rational(edge.get("prob"), f"{identifier} child probability")))
        nodes[identifier] = {"weights": weights, "reward": rational(raw.get("reward"), f"{identifier} reward"),
                             "stop": raw["stop"], "children": children}
    parents = {child for node in nodes.values() for child, _ in node["children"]}
    roots = set(nodes) - parents
    if len(roots) != 1:
        raise CertificateError("the certificate needs exactly one root")
    return support, nodes, next(iter(roots))


def inspect(data: dict[str, Any]) -> dict[str, Any]:
    support, nodes, root = parse(data)
    order = []
    visited = set()
    pending = [root]
    while pending:
        identifier = pending.pop()
        if identifier in visited:
            raise CertificateError("a posterior tree cannot contain cycles or merge histories")
        visited.add(identifier)
        order.append(identifier)
        node = nodes[identifier]
        children = node["children"]
        if not children:
            if not node["stop"]:
                raise CertificateError(f"{identifier}: a leaf must stop")
            continue
        if any(prob <= 0 for _, prob in children) or sum(prob for _, prob in children) != 1:
            raise CertificateError(f"{identifier}: child probabilities must be positive and sum to one")
        if any(child not in nodes for child, _ in children):
            raise CertificateError(f"{identifier}: unknown child")
        for coordinate, parent_weight in enumerate(node["weights"]):
            average = sum(prob * nodes[child]["weights"][coordinate] for child, prob in children)
            if average != parent_weight:
                raise CertificateError(f"{identifier}: posterior barycentre fails at support index {coordinate}")
        pending.extend(child for child, _ in reversed(children))
    if len(visited) != len(nodes):
        raise CertificateError("every node must be reachable from the root")

    means = {
        name: sum(point * weight for point, weight in zip(support, node["weights"], strict=True))
        for name, node in nodes.items()
    }
    snell = {}
    for identifier in reversed(order):
        node = nodes[identifier]
        children = node["children"]
        continuation = sum(prob * snell[child] for child, prob in children)
        snell[identifier] = max(node["reward"], continuation) if children else node["reward"]

    stopped = {}
    frontier = [(root, Fraction(1))]
    while frontier:
        identifier, mass = frontier.pop()
        node = nodes[identifier]
        if node["stop"]:
            stopped[identifier] = mass
        else:
            frontier.extend((child, mass * prob) for child, prob in node["children"])

    policy_reward = sum(mass * nodes[name]["reward"] for name, mass in stopped.items())
    stopped_mean = sum(mass * means[name] for name, mass in stopped.items())
    posterior_gaps = [
        sum(mass * nodes[name]["weights"][i] for name, mass in stopped.items()) - root_weight
        for i, root_weight in enumerate(nodes[root]["weights"])
    ]
    if sum(stopped.values()) != 1 or any(posterior_gaps):
        raise ArithmeticError("stopped paths do not preserve the root posterior")
    restricted_value = snell[root]
    return {
        "status": "finite-posterior-tree-certified",
        "root": root,
        "root_mean": means[root],
        "stopped_nodes": [{"id": name, "path_probability": mass, "mean": means[name],
                           "reward": nodes[name]["reward"]} for name, mass in sorted(stopped.items())],
        "policy_expected_reward": policy_reward,
        "tree_restricted_snell_value": restricted_value,
        "policy_is_tree_optimal": policy_reward == restricted_value,
        "optional_stopping_mean_gap": stopped_mean - means[root],
        "optional_stopping_posterior_gaps": posterior_gaps,
        "scope": "Exact finite posterior-tree check only. It does not optimize over continuous martingales or prove a global martingale-transport value.",
    }


def sample() -> dict[str, Any]:
    return {"support": ["-1", "0", "1"], "nodes": [
        {"id": "root", "weights": ["1/4", "1/2", "1/4"], "reward": "0", "stop": False,
         "children": [{"id": "left", "prob": "1/2"}, {"id": "right", "prob": "1/2"}]},
        {"id": "left", "weights": ["1/2", "1/2", "0"], "reward": "1", "stop": True, "children": []},
        {"id": "right", "weights": ["0", "1/2", "1/2"], "reward": "1", "stop": False,
         "children": [{"id": "zero", "prob": "1/2"}, {"id": "one", "prob": "1/2"}]},
        {"id": "zero", "weights": ["0", "1", "0"], "reward": "0", "stop": True, "children": []},
        {"id": "one", "weights": ["0", "0", "1"], "reward": "3", "stop": True, "children": []},
    ]}


def self_test() -> dict[str, Any]:
    positive = inspect(sample())
    assert positive["policy_expected_reward"] == Fraction(5, 4)
    assert positive["tree_restricted_snell_value"] == Fraction(5, 4)
    assert positive["optional_stopping_mean_gap"] == 0
    negative = sample()
    negative["nodes"][0]["weights"] = ["1/2", "1/2", "0"]
    try:
        inspect(negative)
    except CertificateError as error:
        rejected = "posterior barycentre fails" in str(error)
    else:
        rejected = False
    assert rejected
    return {"positive_policy_reward": Fraction(5, 4), "positive_tree_value": Fraction(5, 4),
            "optional_stopping_mean_gap": Fraction(0), "negative_barycentre_rejected": rejected}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test == (args.certificate is not None):
        parser.error("supply exactly one certificate or --self-test")
    try:
        answer = self_test() if args.self_test else inspect(json.loads(open(args.certificate, encoding="utf-8").read()))
    except (CertificateError, OSError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print(json.dumps(render(answer), ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
