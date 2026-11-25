#!/usr/bin/env python3
"""Exact finite replay for the relation-corner isomorphism.

This enumerates every relation on H for |H|<=3; no floating-point arithmetic
or randomized sampling is used.
"""

from itertools import product


def compose(left: int, right: int, n: int) -> int:
    """Path-order Boolean relation product left followed by right."""
    answer = 0
    for source, middle, target in product(range(n), repeat=3):
        if (left >> (source * n + middle)) & 1 and (right >> (middle * n + target)) & 1:
            answer |= 1 << (source * n + target)
    return answer


def identity(mask: int, n: int) -> int:
    return sum(1 << (point * n + point) for point in range(n) if (mask >> point) & 1)


def restrict(relation: int, mask: int, n: int) -> int:
    return sum(
        ((relation >> (source * n + target)) & 1) << (source * n + target)
        for source in range(n)
        for target in range(n)
        if (mask >> source) & 1 and (mask >> target) & 1
    )


def corner(identity_relation: int, relation: int, n: int) -> int:
    return compose(compose(identity_relation, relation, n), identity_relation, n)


def check_size(n: int) -> int:
    all_relations = range(1 << (n * n))
    triples = 0
    for p in all_relations:
        if compose(p, p, n) != p:
            continue
        for subset in range(1 << n):
            subset_identity = identity(subset, n)
            if compose(compose(subset_identity, p, n), subset_identity, n) != subset_identity:
                continue
            q = compose(compose(p, subset_identity, n), p, n)
            assert compose(q, q, n) == q
            assert compose(p, q, n) == q == compose(q, p, n)

            q_corner = {corner(q, relation, n) for relation in all_relations}
            restricted_monoid = {
                relation for relation in all_relations if restrict(relation, subset, n) == relation
            }
            image = {restrict(z, subset, n) for z in q_corner}
            assert image == restricted_monoid
            assert len(image) == len(q_corner)

            for a in restricted_monoid:
                assert restrict(compose(compose(p, a, n), p, n), subset, n) == a
            for z, w in product(q_corner, repeat=2):
                assert restrict(compose(z, w, n), subset, n) == compose(
                    restrict(z, subset, n), restrict(w, subset, n), n
                )
            triples += 1
    return triples


def main() -> None:
    for n in (1, 2, 3):
        print(f"n={n}: exact checked corner triples={check_size(n)}")


if __name__ == "__main__":
    main()
