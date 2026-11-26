#!/usr/bin/env python3
"""Compute rational piecewise-affine torus-packet spectral densities exactly."""

import argparse
from collections import defaultdict
from fractions import Fraction
import json
from pathlib import Path


def rational(value, label):
    if isinstance(value, bool) or not isinstance(value, (int, str)):
        raise ValueError(f"{label} must be an integer or rational string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError(f"invalid rational {label}") from error


def interval(raw, label):
    if not isinstance(raw, list) or len(raw) != 2:
        raise ValueError(f"{label} must be a two-element interval")
    left, right = rational(raw[0], f"{label}[0]"), rational(raw[1], f"{label}[1]")
    if left >= right:
        raise ValueError(f"{label} must have positive length")
    return left, right


def floor_fraction(value):
    return value.numerator // value.denominator


def stringify(value):
    return str(value)


def parse_phi(payload):
    arc_left, arc_right = interval(payload.get("arc"), "arc")
    if arc_left < 0 or arc_right > 1:
        raise ValueError("arc must be a lift interval inside [0, 1]")
    raw_segments = payload.get("phi_segments")
    if not isinstance(raw_segments, list) or not raw_segments:
        raise ValueError("phi_segments must be a nonempty list")
    segments = []
    for index, raw in enumerate(raw_segments):
        if not isinstance(raw, dict):
            raise ValueError("each phi segment must be an object")
        left = rational(raw.get("left"), f"phi_segments[{index}].left")
        right = rational(raw.get("right"), f"phi_segments[{index}].right")
        slope = rational(raw.get("slope"), f"phi_segments[{index}].slope")
        intercept = rational(raw.get("intercept"), f"phi_segments[{index}].intercept")
        if left >= right or slope <= 0:
            raise ValueError("each phi segment needs positive length and positive slope")
        segments.append((left, right, slope, intercept))
    if segments[0][0] != arc_left or segments[-1][1] != arc_right:
        raise ValueError("phi segments must cover the declared arc exactly")
    for previous, current in zip(segments, segments[1:]):
        if previous[1] != current[0]:
            raise ValueError("phi segments must be consecutive")
        if previous[2] * previous[1] + previous[3] != current[2] * current[0] + current[3]:
            raise ValueError("phi lift must be continuous at every segment boundary")
    return arc_left, arc_right, segments


def parse_packets(raw_packets, arc_left, arc_right, label):
    if not isinstance(raw_packets, list) or not raw_packets:
        raise ValueError(f"{label} must be a nonempty list")
    packets = []
    by_frequency = defaultdict(list)
    for index, raw in enumerate(raw_packets):
        if not isinstance(raw, dict):
            raise ValueError(f"{label}[{index}] must be an object")
        color = raw.get("color")
        frequency = raw.get("frequency")
        if not isinstance(color, str) or not color:
            raise ValueError(f"{label}[{index}].color must be a nonempty string")
        if isinstance(frequency, bool) or not isinstance(frequency, int) or frequency == 0:
            raise ValueError(f"{label}[{index}].frequency must be a nonzero integer")
        left, right = interval(raw.get("support"), f"{label}[{index}].support")
        if left <= arc_left or right >= arc_right:
            raise ValueError("every packet support must be compactly inside the good arc")
        mass = rational(raw.get("mass_density"), f"{label}[{index}].mass_density")
        if mass <= 0:
            raise ValueError("mass_density must be positive")
        packet = {"color": color, "frequency": frequency, "left": left, "right": right, "mass": mass}
        packets.append(packet)
        by_frequency[frequency].append(packet)
    for same_frequency in by_frequency.values():
        for position, first in enumerate(same_frequency):
            for second in same_frequency[position + 1:]:
                if max(first["left"], second["left"]) < min(first["right"], second["right"]):
                    raise ValueError("same-frequency packet supports must be disjoint")
    return packets


def packet_contributions(packet, segments):
    contributions = []
    for left, right, slope, intercept in segments:
        source_left = max(left, packet["left"])
        source_right = min(right, packet["right"])
        if source_left >= source_right:
            continue
        image_left = packet["frequency"] * (slope * source_left + intercept)
        image_right = packet["frequency"] * (slope * source_right + intercept)
        low, high = min(image_left, image_right), max(image_left, image_right)
        density = packet["mass"] / abs(packet["frequency"] * slope)
        for integer in range(floor_fraction(low), floor_fraction(high) + 1):
            target_left = max(low, Fraction(integer)) - integer
            target_right = min(high, Fraction(integer + 1)) - integer
            if target_left < target_right:
                contributions.append((target_left, target_right, density, packet["color"]))
    return contributions


def steps(contributions):
    cuts = {Fraction(0), Fraction(1)}
    for left, right, _, _ in contributions:
        cuts.update((left, right))
    ordered = sorted(cuts)
    output = []
    for left, right in zip(ordered, ordered[1:]):
        midpoint = (left + right) / 2
        density = sum(weight for start, end, weight, _ in contributions if start < midpoint < end)
        if density:
            output.append({"left": stringify(left), "right": stringify(right), "density": stringify(density)})
    return output


def integrate(step_list):
    return sum(
        rational(step["density"], "step density")
        * (rational(step["right"], "step right") - rational(step["left"], "step left"))
        for step in step_list
    )


def build_density(packets, segments):
    contributions = [item for packet in packets for item in packet_contributions(packet, segments)]
    by_color = defaultdict(list)
    for item in contributions:
        by_color[item[3]].append(item)
    colors = {color: steps(items) for color, items in sorted(by_color.items())}
    total = steps(contributions)
    input_mass = sum(packet["mass"] * (packet["right"] - packet["left"]) for packet in packets)
    if integrate(total) != input_mass:
        raise AssertionError("exact pushforward failed to conserve packet mass")
    return colors, total, input_mass


def l1_difference(first, second):
    def unpack(step_list):
        return [(rational(row["left"], "left"), rational(row["right"], "right"), rational(row["density"], "density")) for row in step_list]
    first_rows, second_rows = unpack(first), unpack(second)
    cuts = {Fraction(0), Fraction(1)}
    for left, right, _ in first_rows + second_rows:
        cuts.update((left, right))
    total = Fraction(0)
    for left, right in zip(sorted(cuts), sorted(cuts)[1:]):
        midpoint = (left + right) / 2
        first_density = sum(value for start, end, value in first_rows if start < midpoint < end)
        second_density = sum(value for start, end, value in second_rows if start < midpoint < end)
        total += abs(first_density - second_density) * (right - left)
    return total


def verify(payload):
    if not isinstance(payload, dict):
        raise ValueError("input must be an object")
    arc_left, arc_right, segments = parse_phi(payload)
    packets = parse_packets(payload.get("packets"), arc_left, arc_right, "packets")
    colors, total, input_mass = build_density(packets, segments)
    result = {
        "arc": [stringify(arc_left), stringify(arc_right)],
        "packet_count": len(packets),
        "same_frequency_supports_disjoint": True,
        "color_densities": colors,
        "total_density": total,
        "input_mass": stringify(input_mass),
        "output_mass": stringify(integrate(total)),
    }
    if "comparison_packets" in payload:
        comparison = parse_packets(payload["comparison_packets"], arc_left, arc_right, "comparison_packets")
        _, comparison_total, comparison_mass = build_density(comparison, segments)
        result["comparison_total_density"] = comparison_total
        result["comparison_input_mass"] = stringify(comparison_mass)
        result["density_l1_difference"] = stringify(l1_difference(total, comparison_total))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    arguments = parser.parse_args()
    try:
        result = verify(json.loads(arguments.input.read_text(encoding="utf-8")))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
