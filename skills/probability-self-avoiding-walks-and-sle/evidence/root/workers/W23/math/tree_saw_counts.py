"""Exact finite-depth enumeration of SAWs in the 3-regular tree.

Only an arithmetic/example check for W23S006, not a proof of a general theorem.
Vertices are finite edge-label sequences in the rooted regular tree.  At the
root there are Delta children; at each non-root vertex there are Delta-1 new
children, in addition to its parent (which is already visited).
"""

from __future__ import annotations

import json
from pathlib import Path


def count_tree_saws(delta: int, n: int) -> int:
    if delta < 2 or n < 0:
        raise ValueError("require delta >= 2 and n >= 0")

    def walk(vertex: tuple[int, ...], depth: int) -> int:
        if depth == n:
            return 1
        child_count = delta if not vertex else delta - 1
        return sum(walk(vertex + (j,), depth + 1) for j in range(child_count))

    return 1 if n == 0 else walk((), 0)


if __name__ == "__main__":
    delta = 3
    counts = {str(n): count_tree_saws(delta, n) for n in range(0, 11)}
    expected = {"0": 1, **{str(n): delta * (delta - 1) ** (n - 1) for n in range(1, 11)}}
    assert counts == expected
    result = {
        "example": "infinite 3-regular tree, rooted SAWs",
        "delta": delta,
        "counts_by_n": counts,
        "closed_form_checked_for_n_1_to_10": "c_n = Delta*(Delta-1)^(n-1)",
        "nth_root_values_n_1_to_10": {str(n): counts[str(n)] ** (1 / n) for n in range(1, 11)},
        "interpretation": "Finite enumeration confirms the recurrence on these depths and the tree equality boundary mu=Delta-1=2; it does not establish Theorem 4.2 or any non-tree bound.",
    }
    out = Path(__file__).with_name("tree_saw_counts_result.json")
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
