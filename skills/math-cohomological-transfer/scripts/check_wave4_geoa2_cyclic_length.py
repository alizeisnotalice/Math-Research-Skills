#!/usr/bin/env python3
"""Exact finite abelian p-group chain check for the scoped chromatic reference."""
import argparse
import json
from itertools import product


def add(x, y, moduli):
    return tuple((a + b) % m for a, b, m in zip(x, y, moduli))


def generated(gens, moduli):
    zero = tuple(0 for _ in moduli)
    out = {zero}
    changed = True
    while changed:
        changed = False
        for x in tuple(out):
            for g in gens:
                z = add(x, g, moduli)
                if z not in out:
                    out.add(z)
                    changed = True
    return frozenset(out)


def is_prime_power(m, p):
    if m < 1:
        return False
    while m % p == 0:
        m //= p
    return m == 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input")
    args = ap.parse_args()
    data = json.load(open(args.input, encoding="utf-8"))
    p = data["prime"]
    moduli = tuple(data["moduli"])
    if any(m < 1 or not is_prime_power(m, p) for m in moduli):
        raise SystemExit("invalid: moduli must be positive powers of the supplied prime")
    whole = frozenset(product(*(range(m) for m in moduli)))
    H = generated([tuple(g) for g in data["subgroup_generators"]], moduli)
    subgroups = {H}
    frontier = [H]
    while frontier:
        S = frontier.pop()
        for x in whole:
            T = generated(list(S) + [x], moduli)
            if T not in subgroups:
                subgroups.add(T)
                frontier.append(T)
    dist = {H: 0}
    queue = [H]
    while queue:
        S = queue.pop(0)
        if S == whole:
            print(json.dumps({"valid": True, "group_order": len(whole), "H_order": len(H), "cyclic_chain_length": dist[S]}, sort_keys=True))
            return
        for T in subgroups:
            quotient_is_cyclic = any(generated(list(S) + [x], moduli) == T for x in T)
            if S < T and quotient_is_cyclic:
                if T not in dist:
                    dist[T] = dist[S] + 1
                    queue.append(T)
    raise SystemExit("invalid: no chain found")


if __name__ == "__main__":
    main()
