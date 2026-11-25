#!/usr/bin/env python3
"""Exact finite check for the E06 pathwise lazy-following inequality.

The test uses integer distances on {0, ..., 4}, k=2.  It exhausts all
initial/three simulated configurations and both selected request copies at
each of two service times.  This is a finite sanity check, not a proof for
arbitrary metrics or horizons.
"""

from itertools import combinations_with_replacement, permutations


POINTS = range(5)
K = 2
CONFIGURATIONS = tuple(combinations_with_replacement(POINTS, K))


def distance(x, y):
    return abs(x - y)


def minimum_matching(left, right):
    """Return (cost, permutation), where left[i] matches right[perm[i]]."""
    return min(
        (
            sum(distance(left[i], right[perm[i]]) for i in range(K)),
            perm,
        )
        for perm in permutations(range(K))
    )


def matching_distance(left, right):
    return minimum_matching(left, right)[0]


def lazy_follow(actual, simulated, request_index):
    """Perform the E06 move for one fixed, labelled request copy."""
    request = simulated[request_index]
    if request in actual:
        return actual, 0
    matching_cost, permutation = minimum_matching(actual, simulated)
    server_index = permutation.index(request_index)
    move = distance(actual[server_index], request)
    updated = list(actual)
    updated[server_index] = request
    updated = tuple(updated)
    assert move + matching_distance(updated, simulated) <= matching_cost
    return updated, move


triangle_cases = 0
for first in CONFIGURATIONS:
    for middle in CONFIGURATIONS:
        for last in CONFIGURATIONS:
            assert matching_distance(first, last) <= (
                matching_distance(first, middle) + matching_distance(middle, last)
            )
            triangle_cases += 1

path_cases = 0
for actual0 in CONFIGURATIONS:
    for simulated0 in CONFIGURATIONS:
        initial_potential = matching_distance(actual0, simulated0)
        for simulated1 in CONFIGURATIONS:
            for request1_index in range(K):
                actual1, move1 = lazy_follow(actual0, simulated1, request1_index)
                for simulated2 in CONFIGURATIONS:
                    for request2_index in range(K):
                        actual2, move2 = lazy_follow(actual1, simulated2, request2_index)
                        simulated_cost = (
                            matching_distance(simulated0, simulated1)
                            + matching_distance(simulated1, simulated2)
                        )
                        final_potential = matching_distance(actual2, simulated2)
                        assert move1 + move2 + final_potential <= initial_potential + simulated_cost
                        path_cases += 1

print(
    "PASS: exact integer checks on a five-point line, "
    f"k={K}; triangle cases={triangle_cases}; two-request paths={path_cases}."
)
