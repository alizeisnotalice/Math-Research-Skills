#!/usr/bin/env python3
"""Exact finite prefix evaluator for generalized Hofstadter functions F_k."""

import json
import sys


def values(k: int, limit: int) -> list[int]:
    table = [0]
    for n in range(1, limit + 1):
        argument = n - 1
        for _ in range(k):
            argument = table[argument]
        table.append(n - argument)
    return table


def main(k: int, limit: int) -> None:
    if k < 1 or limit < 0:
        raise ValueError("require k >= 1 and limit >= 0")
    lower = values(k, limit)
    upper = values(k + 1, limit)
    differences = [right - left for left, right in zip(lower, upper)]
    threshold = 12 * (k + 1) * (k + 6)
    strict_indices = list(range(threshold + 1, limit + 1))
    print(json.dumps({
        "k": k,
        "limit": limit,
        "threshold": threshold,
        "pointwise_order_on_prefix": all(delta >= 0 for delta in differences),
        "minimum_difference": min(differences),
        "strict_indices_checked": len(strict_indices),
        "strict_order_after_threshold_on_prefix": all(differences[n] > 0 for n in strict_indices),
        "sample_values": {"F_k": lower[:min(limit + 1, 16)], "F_k_plus_1": upper[:min(limit + 1, 16)]},
        "scope": "Exact finite prefix computation only."
    }, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit("usage: evaluate_hofstadter_family.py K LIMIT")
    main(int(sys.argv[1]), int(sys.argv[2]))
