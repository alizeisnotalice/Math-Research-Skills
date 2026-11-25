#!/usr/bin/env python3
"""Exact finite regression test for the two interfaces in this skill.

This checks one deliberately small instance through episode length 6.  It is
not a proof of the source lemmas for arbitrary prefix codes or sequences.
"""
from itertools import product

E = ("0", "10", "11")
D_PRIME = {"0"}
MAX_EPISODES = 6


def xor(*bits):
    return sum(bits) % 2


def state_update(episode, state):
    """A total two-state update used only for the split test: every episode -> 0."""
    assert episode in E and state in (0, 1)
    return 0


def affine_update(episode, value):
    """v |-> v L_e + b_e over F_2, returning (new_value, L_e, b_e)."""
    tables = {"0": (1, 0), "10": (1, 1), "11": (0, 0)}
    linear, shift = tables[episode]
    return xor(value * linear, shift), linear, shift


def affine_value(episode, value):
    return affine_update(episode, value)[0]


def graph(word, start, update):
    value = start
    for episode in word:
        value = update(episode, value)
    return value


def skipped_graph(word, start, end):
    return all(episode in D_PRIME for episode in word) and graph(word, start, state_update) == end


def split_rhs(word, start, end):
    """Direct finite semantics of the displayed split expression for P_x=E, Q_0={eps}."""
    n = len(word)
    # First branch W_{start,end}.
    if skipped_graph(word, start, end):
        return True
    # A nontrivial branch is a skipped run, then one or more explicit episodes,
    # with skipped runs between and after.  Q_0={eps} forces every explicit
    # episode's output to be 0; that is exactly this toy update.
    for first in range(n):
        if not all(episode in D_PRIME for episode in word[:first]):
            continue
        for last in range(first, n):
            explicit = word[first : last + 1]
            if not any(episode not in D_PRIME for episode in explicit):
                continue
            # Every non-skipped episode is split; zero episodes may instead be
            # absorbed into adjacent W-runs.  Thus this choice is valid exactly
            # when the suffix following the final explicit episode is skipped.
            if all(episode in D_PRIME for episode in word[last + 1 :]):
                return graph(word, start, state_update) == end
    return False


def linear_product(word):
    linear = 1
    shift = 0
    for episode in word:
        _, next_linear, next_shift = affine_update(episode, 0)
        shift = xor(shift * next_linear, next_shift)
        linear *= next_linear
    return linear, shift


def check():
    assert all(not a.startswith(b) for a in E for b in E if a != b), "E is not prefix-free"
    words = [tuple()] + [word for n in range(1, MAX_EPISODES + 1) for word in product(E, repeat=n)]
    split_cases = 0
    affine_cases = 0
    for word in words:
        for start, end in product((0, 1), repeat=2):
            lhs = graph(word, start, state_update) == end
            assert lhs == split_rhs(word, start, end), (word, start, end, lhs)
            split_cases += 1
        linear, _ = linear_product(word)
        for start, end in product((0, 1), repeat=2):
            lhs = start * linear == end
            rhs = any(
                graph(word, start, affine_value) == xor(end, f)
                and graph(word, 0, affine_value) == f
                for f in (0, 1)
            )
            assert lhs == rhs, (word, start, end, lhs, rhs)
            affine_cases += 1
    print(f"exact prefix-code split checks: {split_cases}")
    print(f"exact Boolean-affine recovery checks: {affine_cases}")
    print("all finite checks passed")


if __name__ == "__main__":
    check()
