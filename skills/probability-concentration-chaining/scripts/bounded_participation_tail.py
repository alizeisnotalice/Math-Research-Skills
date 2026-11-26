#!/usr/bin/env python3
"""Audit the declared interface of Lemma 4.3 (bounded participation)."""
import json
import math
import sys
from collections import Counter
from pathlib import Path


def fail(message):
    print(json.dumps({"ok": False, "error": message}, sort_keys=True))
    raise SystemExit(2)


def main(path):
    try:
        data = json.loads(Path(path).read_text())
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON input: {exc}")
    if set(data) - {"functions", "a", "p"}:
        fail("only functions, a, and optional p are allowed")
    functions = data.get("functions")
    a = data.get("a")
    if not isinstance(functions, list) or not functions:
        fail("functions must be a nonempty list")
    if not isinstance(a, (int, float)) or isinstance(a, bool) or not math.isfinite(a) or a <= 0:
        fail("a must be a finite positive number")
    uses = Counter()
    sum_b2 = 0.0
    for j, row in enumerate(functions, 1):
        if not isinstance(row, dict) or set(row) != {"inputs", "lower", "upper"}:
            fail(f"function {j} must have exactly inputs, lower, upper")
        ins = row["inputs"]
        lo, hi = row["lower"], row["upper"]
        if not isinstance(ins, list) or not all(isinstance(x, str) and x for x in ins):
            fail(f"function {j} inputs must be nonempty strings")
        if len(set(ins)) != len(ins):
            fail(f"function {j} repeats an input")
        if not all(isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) for x in (lo, hi)) or lo > hi:
            fail(f"function {j} needs finite lower <= upper")
        uses.update(ins)
        sum_b2 += (hi - lo) ** 2
    measured_p = max(uses.values(), default=0)
    declared_p = data.get("p", measured_p)
    if not isinstance(declared_p, (int, float)) or isinstance(declared_p, bool) or not math.isfinite(declared_p) or declared_p < 1:
        fail("p must be a finite real at least 1")
    if declared_p < measured_p:
        fail(f"declared p={declared_p} is below measured maximum input participation {measured_p}")
    bound = 0.0 if sum_b2 == 0 else math.exp(-2 * a * a / (declared_p * sum_b2))
    print(json.dumps({"ok": True, "a": a, "declared_p": declared_p, "measured_p": measured_p,
                      "sum_range_squares": sum_b2, "one_sided_tail_bound": bound,
                      "certificate": "Lemma 4.3 applies only if declared ranges and dependence sets are true for functions of independent inputs."}, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: bounded_participation_tail.py INSTANCE.json", file=sys.stderr)
        raise SystemExit(2)
    main(sys.argv[1])
