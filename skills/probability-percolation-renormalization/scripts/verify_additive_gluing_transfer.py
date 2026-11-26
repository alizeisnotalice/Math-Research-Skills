"""Exact sanity checks for the scalar bridge AdditiveGluing -> NearOneGluing.

This is not a finite-graph proof of AdditiveGluing.  It checks the only scalar
strict/weak inequality transition used by the conditional bridge, with exact
rational arithmetic.  The general bridge is proved in the accompanying note.
"""
from fractions import Fraction as Q


def main():
    cases = 0
    for den in range(2, 18):
        for num in range(1, 2 * den):
            epsilon = Q(num, den)
            delta = epsilon / 2
            for step in range(1, 10):
                hit = 1 - delta + delta * Q(step, 10)
                # Least admissible probability under the additive conclusion.
                target = max(Q(0), hit - delta)
                assert 0 < delta and 0 <= hit <= 1 and 0 <= target <= 1
                assert 1 - delta < hit and hit - delta <= target
                assert 1 - epsilon < target
                cases += 1

    # Strictness at P(o<->A) is indispensable: weak input cannot yield the
    # strict near-one conclusion at the equality boundary.
    epsilon = Q(2, 5)
    delta = epsilon / 2
    hit = 1 - delta
    target = hit - delta
    assert target == 1 - epsilon
    return {"exact_rational_cases": cases, "strictness_boundary_rejected": True}


if __name__ == "__main__":
    print(main())
