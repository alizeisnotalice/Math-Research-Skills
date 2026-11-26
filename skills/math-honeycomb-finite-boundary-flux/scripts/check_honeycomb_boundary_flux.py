#!/usr/bin/env python3
"""Evaluate finite honeycomb exit flux in Q[z]/(z^8+1) exactly."""

from collections import defaultdict
from fractions import Fraction
from functools import cache
import argparse
import json
from pathlib import Path

ONE = (Fraction(1),) + (Fraction(0),) * 7
RHO = tuple(Fraction(c, 2) for c in (0, 1, 0, -1, 0, 1, 0, -1))


def vector(left, right):
    return right[0] - left[0], right[1] - left[1]


def cross(left, right):
    return left[0] * right[1] - left[1] * right[0]


def vertex(raw):
    if not isinstance(raw, list) or len(raw) != 2 or any(type(x) is not int for x in raw):
        raise ValueError("vertices must be two integer triangular-lattice coordinates")
    return tuple(raw)


def edge_key(a, b):
    return tuple(sorted((a, b)))


def read_domain(payload):
    if not isinstance(payload, dict) or not isinstance(payload.get("triangles"), list) or not payload["triangles"]:
        raise ValueError("input requires a nonempty list of triangles")
    faces = []
    seen = set()
    incidences = defaultdict(list)
    for index, raw in enumerate(payload["triangles"]):
        if not isinstance(raw, list) or len(raw) != 3:
            raise ValueError("every triangle must list three vertices")
        a, b, c = map(vertex, raw)
        sides = [vector(a, b), vector(b, c), vector(c, a)]
        if any(x*x + x*y + y*y != 1 for x, y in sides):
            raise ValueError("only unit triangular-lattice faces are allowed")
        if cross(sides[0], sides[1]) < 0:
            b, c = c, b
        face = (a, b, c)
        label = frozenset(face)
        if label in seen:
            raise ValueError("duplicate triangle")
        seen.add(label)
        faces.append(face)
        for side in range(3):
            e = face[side], face[(side + 1) % 3]
            incidences[edge_key(*e)].append((index, side))
    if any(len(pair) > 2 for pair in incidences.values()):
        raise ValueError("an edge belongs to more than two faces")
    adjacency = {face: {other for side in range(3)
                        for other, _ in incidences[edge_key(v[side], v[(side+1)%3])]
                        if other != face} for face, v in enumerate(faces)}
    reached = {0}
    fringe = [0]
    while fringe:
        new = adjacency[fringe.pop()] - reached
        reached.update(new)
        fringe.extend(new)
    if len(reached) != len(faces):
        raise ValueError("face adjacency must be connected")

    boundary = {}
    for mates in incidences.values():
        if len(mates) == 1:
            face, side = mates[0]
            a, b = faces[face][side], faces[face][(side + 1) % 3]
            if a in boundary:
                raise ValueError("boundary must be a simple oriented cycle")
            boundary[a] = b
    if not boundary or set(boundary) != set(boundary.values()):
        raise ValueError("boundary edges do not form an oriented cycle")
    beginning = next(iter(boundary))
    ordered = [beginning]
    cursor = boundary[beginning]
    while cursor != beginning:
        ordered.append(cursor)
        cursor = boundary[cursor]
    if len(ordered) != len(boundary):
        raise ValueError("boundary has more than one cycle")
    vertices = {v for face in faces for v in face}
    if len(vertices) - len(incidences) + len(faces) != 1:
        raise ValueError("Euler characteristic is not one")
    convex = all(cross(vector(ordered[i-1], v), vector(v, boundary[v])) >= 0
                 for i, v in enumerate(ordered))
    raw_port = payload.get("entry_edge")
    if not isinstance(raw_port, list) or len(raw_port) != 2:
        raise ValueError("entry_edge must list two boundary vertices")
    ports = incidences.get(edge_key(*map(vertex, raw_port)), ())
    if len(ports) != 1:
        raise ValueError("entry_edge must be an actual boundary edge")
    return faces, incidences, ports[0], convex


def multiply(left, right):
    result = [Fraction(0)] * 8
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            power = i+j
            result[power % 8] += a*b if power < 8 else -a*b
    return tuple(result)


def coefficient_sum(terms):
    result = [Fraction(0)] * 8

    @cache
    def rho_power(exponent):
        value, power = ONE, RHO
        while exponent:
            if exponent % 2:
                value = multiply(value, power)
            exponent //= 2
            if exponent:
                power = multiply(power, power)
        return value

    for (length, turn), count in terms.items():
        for index, coeff in enumerate(rho_power(length)):
            power = (index+turn) % 16
            result[power % 8] += count*coeff if power < 8 else -count*coeff
    return tuple(result)


def verify(payload):
    faces, incidences, entry, convex = read_domain(payload)
    exits, collisions = defaultdict(int), defaultdict(int)
    stack = [(entry, frozenset((entry[0],)), 0)]
    while stack:
        (face, arrival), seen, turn = stack.pop()
        for step in (-1, 1):
            side = (arrival+step) % 3
            a, b = faces[face][side], faces[face][(side+1) % 3]
            mates = incidences[edge_key(a, b)]
            winding = turn-step
            if len(mates) == 1:
                exits[(len(seen), winding)] += 1
                continue
            other = next(mate for mate in mates if mate[0] != face)
            if other[0] in seen:
                collisions[(len(seen), winding)] += 1
            else:
                stack.append((other, seen | {other[0]}, winding))

    flux = coefficient_sum(exits)
    collision_flux = coefficient_sum(collisions)
    return {
        "triangles": len(faces),
        "convex_boundary": convex,
        "exiting_paths": sum(exits.values()),
        "collision_paths": sum(collisions.values()),
        "basis": "coefficients of 1,z,...,z^7 where z=exp(i*pi/8)",
        "exit_flux": list(map(str, flux)),
        "collision_flux": list(map(str, collision_flux)),
        "signed_identity_verified": flux == ONE and not any(collision_flux),
        "all_exit_turns_at_most_pi": all(abs(turn) <= 3 for _, turn in exits),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        result = verify(json.loads(args.input.read_text(encoding="utf-8")))
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0 if result["signed_identity_verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
