"""Exact input validation shared by the finite reversible-chain tools."""

from fractions import Fraction


def rational(value: object) -> Fraction:
    if type(value) is int or isinstance(value, str):
        return Fraction(value)
    raise ValueError("use integers or exact rational strings")


def reversible_chain(transition, stationary, *, require_positive: bool = False):
    """Read a stochastic matrix, normalized law and its symmetric probability flow."""
    if not isinstance(transition, list) or not transition:
        raise ValueError("transition must be a nonempty square matrix")
    size = len(transition)
    if any(not isinstance(row, list) or len(row) != size for row in transition):
        raise ValueError("transition must be a nonempty square matrix")
    p = [[rational(x) for x in row] for row in transition]
    if any(any(x < 0 for x in row) or sum(row) != 1 for row in p):
        raise ValueError("transition rows must be probability vectors")
    if not isinstance(stationary, list) or len(stationary) != size:
        raise ValueError("stationary must have one weight per state")
    pi = [rational(x) for x in stationary]
    if any(x < 0 for x in pi) or sum(pi) != 1:
        raise ValueError("stationary weights must be nonnegative and sum to one")
    if require_positive and not all(pi):
        raise ValueError("this certificate requires positive stationary weights")
    flow = [[pi[i] * p[i][j] for j in range(size)] for i in range(size)]
    for i in range(size):
        for j in range(i):
            if flow[i][j] != flow[j][i]:
                raise ValueError(f"detailed balance fails at ({i}, {j})")
    return p, pi, flow
