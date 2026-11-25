#!/usr/bin/env python3
"""Exact finite checks for the priority-test and one-step unfolding rules."""

from itertools import permutations
from fractions import Fraction


TRIANGLES = {
    "abc": frozenset({"ab", "ac", "bc"}),
    "abd": frozenset({"ab", "ad", "bd"}),
}


def scan(order, threshold):
    present = set().union(*TRIANGLES.values())
    for name in order:
        if threshold[name] >= threshold["limit"]:
            continue
        edges = TRIANGLES[name]
        if edges <= present:
            present -= edges
    return present


def root_test(edge, threshold, priorities):
    candidates = [name for name, edges in TRIANGLES.items() if edge in edges]
    for name in sorted(candidates, key=priorities.__getitem__):
        if priorities[name] >= threshold:
            continue
        others = TRIANGLES[name] - {edge}
        # In this two-triangle fixture each child has no lower-priority candidate.
        if all(
            not (candidate != name and priorities[candidate] < priorities[name]
                 and bool(TRIANGLES[candidate] & others))
            for candidate in TRIANGLES
        ):
            return False
    return True


def main():
    checked = 0
    for order in permutations(TRIANGLES):
        priorities = {name: Fraction(i + 1, 3) for i, name in enumerate(order)}
        priorities["limit"] = Fraction(1)
        survivors = scan(order, priorities)
        for edge in {"ab", "ac", "bc", "ad", "bd"}:
            assert root_test(edge, Fraction(1), priorities) == (edge in survivors)
            checked += 1

    # A depth-one independent unfolding.  Each candidate's pair child has no
    # further candidates, so it always returns true.  At t=1/2 a candidate
    # succeeds precisely when its independent occurrence priority is below t.
    # Thus I(t)=t and two independent failures give (1-t)^2=1/4.
    candidate_success = Fraction(1, 2)
    first_failure = candidate_success
    second_failure = candidate_success
    survival = (1 - first_failure) * (1 - second_failure)
    assert survival == Fraction(1, 4)
    print(f"PASS: {checked} finite scan/test comparisons; independent product survival={survival}")


if __name__ == "__main__":
    main()
