#!/usr/bin/env python3
"""Exact finite certificate for revealed paths in independent fair matching switches.

The program validates that feasible observed paths specify a cylinder of coin bits,
enumerates the remaining cube, compares the tagged-card law with the free-slot
averaging/transport recursion, and checks reindexed slot-kernel composition.
"""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path
from typing import Any


def qs(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def parse_fraction(x: Any) -> Fraction:
    if isinstance(x, bool) or isinstance(x, float):
        raise ValueError("signed entries must be exact integer/rational strings, not floats")
    return Fraction(x)


def maps_for_layers(n: int, layers: list[Any]) -> tuple[list[list[tuple[int, int]]], list[dict[int, tuple[int, int]]]]:
    parsed: list[list[tuple[int, int]]] = []
    locations: list[dict[int, tuple[int, int]]] = []
    for time, raw in enumerate(layers):
        if not isinstance(raw, list):
            raise ValueError("each layer must be a list of pairs")
        pairs: list[tuple[int, int]] = []
        slot_map: dict[int, tuple[int, int]] = {}
        for p, pair in enumerate(raw):
            if not isinstance(pair, list) or len(pair) != 2 or not all(isinstance(v, int) and not isinstance(v, bool) for v in pair):
                raise ValueError("each matching pair must contain two integer slots")
            a, b = pair
            if not (0 <= a < n and 0 <= b < n) or a == b or a in slot_map or b in slot_map:
                raise ValueError(f"layer {time} is not a disjoint matching of valid slots")
            pairs.append((a, b))
            slot_map[a] = (p, 0)
            slot_map[b] = (p, 1)
        if set(slot_map) != set(range(n)):
            raise ValueError(f"layer {time} must be a perfect matching of every slot")
        parsed.append(pairs)
        locations.append(slot_map)
    return parsed, locations


def image(pair: tuple[int, int], bit: int, slot: int) -> int:
    a, b = pair
    if slot not in pair:
        raise AssertionError("slot outside pair")
    return slot if bit == 0 else (b if slot == a else a)


def compose(later: tuple[int, ...], earlier: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(later[earlier[i]] for i in range(len(earlier)))


def enumerate_interval(n: int, pairs: list[list[tuple[int, int]]], fixed: dict[tuple[int, int], int], free_sets: list[set[int]], start: int, end: int) -> dict[tuple[int, ...], int]:
    free_coords = [(t, p) for t in range(start, end) for p in range(len(pairs[t])) if (t, p) not in fixed]
    if len(free_coords) > 20:
        raise ValueError("more than 20 unvisited coins: exact enumeration intentionally capped")
    source = sorted(free_sets[start])
    target = sorted(free_sets[end])
    target_index = {slot: i for i, slot in enumerate(target)}
    counts: dict[tuple[int, ...], int] = {}
    for bits in itertools.product((0, 1), repeat=len(free_coords)):
        assignment = fixed.copy()
        assignment.update(zip(free_coords, bits))
        current = source[:]
        for t in range(start, end):
            current = [
                image(pair, assignment[t, p], slot)
                for slot in current
                for p, pair in enumerate(pairs[t])
                if slot in pair
            ]
        if set(current) != set(target) or len(set(current)) != len(current):
            raise AssertionError("free-slot map is not a bijection")
        perm = tuple(target_index[slot] for slot in current)
        counts[perm] = counts.get(perm, 0) + 1
    return counts


def update_vector(vector: list[Fraction], t: int, pairs: list[list[tuple[int, int]]], fixed: dict[tuple[int, int], int], free_sets: list[set[int]]) -> list[Fraction]:
    before, after = free_sets[t], free_sets[t + 1]
    result = [Fraction(0) for _ in vector]
    for p, pair in enumerate(pairs[t]):
        free_inputs = [x for x in pair if x in before]
        if len(free_inputs) == 2:
            if any(x not in after for x in pair):
                raise AssertionError("free-free input must have two free outputs")
            value = (vector[pair[0]] + vector[pair[1]]) / 2
            result[pair[0]] = result[pair[1]] = value
        elif len(free_inputs) == 1:
            if (t, p) not in fixed:
                raise AssertionError("a mixed observed/free edge must be fixed by its observed path")
            out = image(pair, fixed[t, p], free_inputs[0])
            if out not in after:
                raise AssertionError("mixed edge did not map free input to free output")
            result[out] = vector[free_inputs[0]]
        elif len(free_inputs) == 0:
            continue
        else:
            raise AssertionError("invalid free-input count")
    if any(result[x] != 0 for x in range(len(vector)) if x not in after):
        raise AssertionError("update leaked mass outside free slots")
    return result


def certify(data: dict[str, Any]) -> dict[str, Any]:
    n = data.get("slot_count")
    if not isinstance(n, int) or isinstance(n, bool) or n < 2:
        raise ValueError("slot_count must be an integer at least 2")
    pairs, locations = maps_for_layers(n, data.get("layers", []))
    horizon = len(pairs)
    paths = data.get("observed_paths", {})
    if not isinstance(paths, dict):
        raise ValueError("observed_paths must be an object from names to slot paths")
    fixed: dict[tuple[int, int], int] = {}
    path_values: dict[str, list[int]] = {}
    for name, raw in paths.items():
        if not isinstance(name, str) or not name or not isinstance(raw, list) or len(raw) != horizon + 1 or not all(isinstance(x, int) and not isinstance(x, bool) and 0 <= x < n for x in raw):
            raise ValueError("each observed path must be named and give horizon+1 valid integer slots")
        path_values[name] = raw
        for t in range(horizon):
            p, side = locations[t][raw[t]]
            pair = pairs[t][p]
            if raw[t + 1] not in pair:
                raise ValueError(f"path {name} does not follow matching edge at time {t}")
            needed = 0 if raw[t + 1] == raw[t] else 1
            key = (t, p)
            if key in fixed and fixed[key] != needed:
                raise ValueError(f"paths demand contradictory coin values at time {t}, pair {p}")
            fixed[key] = needed
    for t in range(horizon + 1):
        occupied = [path[t] for path in path_values.values()]
        if len(set(occupied)) != len(occupied):
            raise ValueError(f"observed paths collide at boundary time {t}")
    free_sets = [set(range(n)) - {path[t] for path in path_values.values()} for t in range(horizon + 1)]
    tagged = data.get("tagged_start")
    if not isinstance(tagged, int) or isinstance(tagged, bool) or tagged not in free_sets[0]:
        raise ValueError("tagged_start must be an initially free slot")
    cuts = data.get("interval_cuts", [0, horizon])
    if not isinstance(cuts, list) or len(cuts) < 2 or cuts[0] != 0 or cuts[-1] != horizon or any(not isinstance(x, int) for x in cuts) or any(cuts[i] >= cuts[i + 1] for i in range(len(cuts) - 1)):
        raise ValueError("interval_cuts must be a strictly increasing list beginning 0 and ending horizon")
    # The exact cylinder has this many equally likely completions.
    all_coords = [(t, p) for t in range(horizon) for p in range(len(pairs[t]))]
    free_coords = [coord for coord in all_coords if coord not in fixed]
    full_counts = enumerate_interval(n, pairs, fixed, free_sets, 0, horizon)
    denominator = 2 ** len(free_coords)
    if sum(full_counts.values()) != denominator:
        raise AssertionError("cylinder enumeration size mismatch")
    # Tagged law by direct enumeration of its final index in the reindexed free slots.
    source = sorted(free_sets[0])
    tag_index = source.index(tagged)
    target = sorted(free_sets[-1])
    enumerated_tag = [Fraction(0) for _ in range(n)]
    for perm, count in full_counts.items():
        enumerated_tag[target[perm[tag_index]]] += Fraction(count, denominator)
    predicted = [Fraction(int(i == tagged)) for i in range(n)]
    uniform = [Fraction(1, len(free_sets[0])) if i in free_sets[0] else Fraction(0) for i in range(n)]
    signed = [predicted[i] - uniform[i] for i in range(n)]
    probability_history = [predicted]
    signed_history = [signed]
    energy = [sum(x * x for x in signed)]
    for t in range(horizon):
        predicted = update_vector(predicted, t, pairs, fixed, free_sets)
        uniform = update_vector(uniform, t, pairs, fixed, free_sets)
        signed = update_vector(signed, t, pairs, fixed, free_sets)
        if predicted != [signed[i] + uniform[i] for i in range(n)]:
            raise AssertionError("centered decomposition broke")
        if sum(signed) != 0:
            raise AssertionError("signed sum was not preserved")
        next_energy = sum(x * x for x in signed)
        if next_energy > energy[-1]:
            raise AssertionError("averaging/transport increased signed energy")
        probability_history.append(predicted)
        signed_history.append(signed)
        energy.append(next_energy)
    if predicted != enumerated_tag:
        raise AssertionError("enumerated conditional tag law differs from averaging/transport recursion")
    # Each interval has an independently reindexed slot kernel.  Compose in chronological order.
    interval_laws: list[dict[tuple[int, ...], Fraction]] = []
    for start, end in zip(cuts, cuts[1:]):
        counts = enumerate_interval(n, pairs, fixed, free_sets, start, end)
        local_free = sum(1 for t in range(start, end) for p in range(len(pairs[t])) if (t, p) not in fixed)
        interval_laws.append({perm: Fraction(count, 2 ** local_free) for perm, count in counts.items()})
    composed: dict[tuple[int, ...], Fraction] = {tuple(range(len(source))): Fraction(1)}
    for law in interval_laws:
        next_law: dict[tuple[int, ...], Fraction] = {}
        for earlier, p_earlier in composed.items():
            for later, p_later in law.items():
                key = compose(later, earlier)
                next_law[key] = next_law.get(key, Fraction(0)) + p_earlier * p_later
        composed = next_law
    full_law = {perm: Fraction(count, denominator) for perm, count in full_counts.items()}
    if composed != full_law:
        raise AssertionError("interval slot kernels did not compose to the full conditioned kernel")
    def perm_key(perm: tuple[int, ...]) -> str:
        return ",".join(map(str, perm))
    return {
        "certificate_kind": "finite independent matching-switch cylinder and reindexed slot kernel",
        "contract": {
            "network": "each layer is a perfect matching; each edge has an independent fair identity/swap coin",
            "exposure": "observed paths are feasible and collision-free; they fix exactly their visited time-edge coins",
            "conclusion": "unvisited coins remain independent fair; the free-slot map is a conditional random permutation and interval kernels compose",
            "scope": "finite exact conditional-modeling/energy certificate only; no spectral-gap, total-variation mixing, Fourier, or asymptotic claim",
        },
        "horizon": horizon,
        "free_slot_count": len(source),
        "fixed_cylinder_coins": [{"time": t, "pair": p, "value": fixed[t, p]} for t, p in sorted(fixed)],
        "unvisited_coin_count": len(free_coords),
        "conditional_cylinder_probability": qs(Fraction(1, 2 ** len(fixed))),
        "free_sets_by_boundary": [sorted(x) for x in free_sets],
        "tagged_final_law_enumerated": [qs(x) for x in enumerated_tag],
        "tagged_law_by_boundary_recursion": [[qs(x) for x in row] for row in probability_history],
        "signed_centered_vector_by_boundary": [[qs(x) for x in row] for row in signed_history],
        "signed_energy_by_boundary": [qs(x) for x in energy],
        "slot_kernel_full": {perm_key(k): qs(v) for k, v in sorted(full_law.items())},
        "slot_kernel_intervals": [{perm_key(k): qs(v) for k, v in sorted(law.items())} for law in interval_laws],
        "composition_verified": True,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()
    try:
        with args.input.open(encoding="utf-8") as handle:
            result = certify(json.load(handle))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
