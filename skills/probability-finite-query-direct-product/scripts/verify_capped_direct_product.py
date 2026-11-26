#!/usr/bin/env python3
"""Exact finite audit for the capped direct-product decision-tree lemma."""
import json
import sys
from fractions import Fraction
from functools import lru_cache
from itertools import product
from pathlib import Path


class InvalidTree(ValueError):
    pass


def load(path):
    data = json.loads(Path(path).read_text())
    domain = data["domain"]
    probs = tuple(Fraction(x) for x in data["probabilities"])
    values = tuple(int(x) for x in data["values"])
    cap, copies = int(data["cap"]), int(data["copies"])
    if not domain or len(domain) != len(probs) or len(domain) != len(values):
        raise ValueError("domain, probabilities, and values must be nonempty and matched")
    if len(set(domain)) != len(domain) or any(set(x) - {"0", "1"} for x in domain):
        raise ValueError("domain must contain distinct binary strings")
    if len({len(x) for x in domain}) != 1 or any(p < 0 for p in probs) or sum(probs) != 1:
        raise ValueError("bad bit length or probability law")
    if any(v not in (0, 1) for v in values) or cap < 0 or copies < 1:
        raise ValueError("values must be Boolean; cap/copies out of range")
    return domain, probs, values, cap, copies, data["tree"]


def one_copy_optimum(domain, probs, values, cap):
    n = len(domain[0])

    @lru_cache(None)
    def best(indices, budget):
        mass0 = sum((probs[i] for i in indices if values[i] == 0), Fraction())
        mass1 = sum((probs[i] for i in indices if values[i] == 1), Fraction())
        if budget == 0 or len(indices) <= 1:
            return max(mass0, mass1)
        answer = max(mass0, mass1)
        for coordinate in range(n):
            split0 = tuple(i for i in indices if domain[i][coordinate] == "0")
            split1 = tuple(i for i in indices if domain[i][coordinate] == "1")
            if split0 and split1:
                answer = max(answer, best(split0, budget - 1) + best(split1, budget - 1))
        return answer

    return best(tuple(range(len(domain))), cap)


def walk(node, inputs, domain, values, cap, counts):
    if "output" in node:
        out = tuple(node["output"])
        if set(node) != {"output"} or len(out) != len(inputs) or any(x not in (0, 1) for x in out):
            raise InvalidTree("malformed output leaf")
        return tuple(values[i] for i in inputs) == out
    if set(node) != {"query", "zero", "one"}:
        raise InvalidTree("node must be exactly query/zero/one or output")
    query = node["query"]
    if not isinstance(query, list) or len(query) != 2:
        raise InvalidTree("query must be [copy, coordinate]")
    h, coordinate = query
    if not isinstance(h, int) or not isinstance(coordinate, int) or h < 0 or h >= len(inputs):
        raise InvalidTree("copy index out of range")
    if coordinate < 0 or coordinate >= len(domain[0]):
        raise InvalidTree("coordinate out of range")
    next_counts = list(counts)
    next_counts[h] += 1
    if next_counts[h] > cap:
        raise InvalidTree("per-copy query cap violated")
    branch = "one" if domain[inputs[h]][coordinate] == "1" else "zero"
    return walk(node[branch], inputs, domain, values, cap, tuple(next_counts))


def audit(path):
    domain, probs, values, cap, copies, tree = load(path)
    beta = one_copy_optimum(domain, probs, values, cap)
    success = Fraction()
    for inputs in product(range(len(domain)), repeat=copies):
        weight = Fraction(1)
        for i in inputs:
            weight *= probs[i]
        if weight and walk(tree, inputs, domain, values, cap, (0,) * copies):
            success += weight
    bound = beta ** copies
    print(f"beta={beta}; copies={copies}; beta^r={bound}; tree_success={success}")
    if success > bound:
        raise AssertionError("tree exceeds the capped direct-product bound")


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError("usage: verify_capped_direct_product.py INPUT.json")
        audit(sys.argv[1])
    except (ValueError, InvalidTree, AssertionError, KeyError, json.JSONDecodeError) as exc:
        print(f"REJECT: {exc}", file=sys.stderr)
        sys.exit(2)
