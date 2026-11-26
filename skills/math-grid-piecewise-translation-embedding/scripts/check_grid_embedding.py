#!/usr/bin/env python3
"""Construct an exact cellwise-translation injection for one finite grid."""
import argparse
import json
import sys


def fail(message):
    print(json.dumps({"verified": False, "error": message}, sort_keys=True))
    raise SystemExit(2)


def checked_cells(value, name, tracks, side):
    if not isinstance(value, list):
        fail(f"{name} must be a list")
    cells = []
    for item in value:
        if not isinstance(item, list) or len(item) != 3 or any(type(z) is not int for z in item):
            fail(f"{name} cells must be integer [track,x,y] triples")
        t, x, y = item
        if not (0 <= t < tracks and 0 <= x < side and 0 <= y < side):
            fail(f"{name} contains a cell outside the declared grid")
        cells.append((t, x, y))
    if len(set(cells)) != len(cells):
        fail(f"{name} contains a repeated cell")
    return sorted(cells)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="JSON grid certificate")
    args = parser.parse_args()
    try:
        with open(args.input, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read JSON input: {exc}")
    if not isinstance(data, dict):
        fail("input must be an object")
    tracks, side = data.get("tracks"), data.get("side")
    if type(tracks) is not int or tracks <= 0 or type(side) is not int or side <= 0:
        fail("tracks and side must be positive integers")
    source = checked_cells(data.get("source"), "source", tracks, side)
    target = checked_cells(data.get("target"), "target", tracks, side)
    if len(source) >= len(target):
        fail("strict comparison fails: source must have fewer cells than target")

    # Matching ordered distinct cells is an exact injection.  On each source
    # square it is the translation by the reported integer grid displacement.
    mappings = []
    for src, dst in zip(source, target):
        st, sx, sy = src
        dt, dx, dy = dst
        mappings.append({
            "source": [st, sx, sy],
            "target": [dt, dx, dy],
            "track_change": [st, dt],
            "translation": [dx - sx, dy - sy],
        })
    print(json.dumps({
        "verified": True,
        "source_cells": len(source),
        "target_cells": len(target),
        "unused_target_cells": len(target) - len(source),
        "mappings": mappings,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
