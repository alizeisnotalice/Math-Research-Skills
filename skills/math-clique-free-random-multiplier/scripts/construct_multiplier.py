#!/usr/bin/env python3
"""Exact finite-support multiplier construction for a rational weighted K_r-free graph."""
from __future__ import annotations

import itertools
import json
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


class InputError(ValueError):
    pass


def frac(value: object) -> Fraction:
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as error:
        raise InputError(f"not a rational number: {value!r}") from error


def render(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def has_clique(vertices: tuple[str, ...], adjacency: dict[str, set[str]], r: int) -> bool:
    return any(all(b in adjacency[a] for a, b in itertools.combinations(group, 2))
               for group in itertools.combinations(vertices, r))


def edge_mass(vertices: tuple[str, ...], adjacency: dict[str, set[str]], values: dict[str, Fraction]) -> Fraction:
    return sum(values[u] * values[v] for u, v in itertools.combinations(vertices, 2) if v in adjacency[u])


def merge(atoms: list[tuple[Fraction, dict[str, Fraction]]]) -> list[tuple[Fraction, dict[str, Fraction]]]:
    merged: dict[tuple[tuple[str, Fraction], ...], Fraction] = defaultdict(Fraction)
    for probability, multiplier in atoms:
        merged[tuple(sorted(multiplier.items()))] += probability
    return [(probability, dict(key)) for key, probability in sorted(merged.items()) if probability]


def construct(vertices: tuple[str, ...], adjacency: dict[str, set[str]], weights: dict[str, Fraction], r: int,
              epsilon: Fraction, max_outcomes: int) -> list[tuple[Fraction, dict[str, Fraction]]]:
    if r == 2:
        if edge_mass(vertices, adjacency, weights):
            raise InputError("internal error: K_2-free recursion received an edge")
        return [(Fraction(1), {v: Fraction(1) for v in vertices})]
    total = sum(weights[v] for v in vertices)
    eta = epsilon / 4
    remaining = set(vertices)
    parts: list[tuple[str, ...]] = []
    while True:
        selected = next((v for v in sorted(remaining)
                         if sum(weights[u] for u in adjacency[v] & remaining) > eta * total), None)
        if selected is None:
            break
        part = tuple(sorted(adjacency[selected] & remaining))
        parts.append(part)
        remaining.difference_update(part)
    if not parts:
        return [(Fraction(1), {v: Fraction(1) for v in vertices})]
    part_weights = [sum(weights[v] for v in part) for part in parts]
    removed_weight = sum(part_weights)
    atoms: list[tuple[Fraction, dict[str, Fraction]]] = []
    atom_r = {v: Fraction(2) if v in remaining else Fraction(0) for v in vertices}
    atoms.append((Fraction(1, 2), atom_r))
    for part, part_weight in zip(parts, part_weights):
        probability = part_weight / (2 * removed_weight)
        local = construct(part, adjacency, weights, r - 1, epsilon / 4, max_outcomes)
        for local_probability, local_multiplier in local:
            atom = {v: Fraction(0) for v in vertices}
            for v in part:
                atom[v] = local_multiplier[v] / probability
            atoms.append((probability * local_probability, atom))
            if len(atoms) > max_outcomes:
                raise InputError(f"finite support exceeds max_outcomes={max_outcomes}")
    atoms = merge(atoms)
    if len(atoms) > max_outcomes:
        raise InputError(f"finite support exceeds max_outcomes={max_outcomes}")
    return atoms


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: construct_multiplier.py INPUT.json", file=sys.stderr)
        return 2
    try:
        payload = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
        vertices = tuple(str(v) for v in payload["vertices"])
        if not vertices or len(set(vertices)) != len(vertices):
            raise InputError("vertices must be a nonempty list of distinct names")
        vertex_set = set(vertices)
        weights = {v: frac(payload["weights"][v]) for v in vertices}
        if any(value <= 0 for value in weights.values()):
            raise InputError("all vertex weights must be positive")
        r = int(payload["r"])
        epsilon = frac(payload["epsilon"])
        if r < 2 or not (0 < epsilon <= Fraction(1, 2)):
            raise InputError("require r >= 2 and 0 < epsilon <= 1/2")
        adjacency = {v: set() for v in vertices}
        seen: set[tuple[str, str]] = set()
        for raw_u, raw_v in payload["edges"]:
            u, v = str(raw_u), str(raw_v)
            if u not in vertex_set or v not in vertex_set or u == v:
                raise InputError("edges must join two distinct listed vertices")
            edge = tuple(sorted((u, v)))
            if edge in seen:
                raise InputError("duplicate undirected edge")
            seen.add(edge)
            adjacency[u].add(v)
            adjacency[v].add(u)
        if has_clique(vertices, adjacency, r):
            raise InputError(f"graph is not K_{r}-free")
        max_outcomes = int(payload.get("max_outcomes", 10000))
        if max_outcomes < 1:
            raise InputError("max_outcomes must be positive")
        atoms = construct(vertices, adjacency, weights, r, epsilon, max_outcomes)
        if sum(probability for probability, _ in atoms) != 1:
            raise AssertionError("probabilities do not sum to one")
        means = {v: sum(probability * multiplier[v] for probability, multiplier in atoms) for v in vertices}
        expected_mass = sum(probability * edge_mass(vertices, adjacency,
                            {v: weights[v] * multiplier[v] for v in vertices}) for probability, multiplier in atoms)
        total_weight = sum(weights.values())
        bound = epsilon * total_weight * total_weight
        if any(mean != 1 for mean in means.values()) or expected_mass > bound:
            raise AssertionError("constructed law failed its exact certificate")
        result = {
            "atoms": [{"probability": render(probability), "multiplier": {v: render(multiplier[v]) for v in vertices}}
                      for probability, multiplier in atoms],
            "expected_edge_mass": render(expected_mass),
            "mean_multipliers": {v: render(means[v]) for v in vertices},
            "bound": render(bound),
            "support_size": len(atoms),
        }
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except (KeyError, TypeError, json.JSONDecodeError, InputError) as error:
        print(f"input error: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
