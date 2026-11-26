#!/usr/bin/env python3
"""Verify the integral-plane covolume identity from an exact integer basis."""

import json
import math
import sys
from pathlib import Path


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


def cross(x, y):
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]


def det3(rows):
    a, b, c = rows
    return dot(a, cross(b, c))


def gcd_all(values):
    result = 0
    for value in values:
        result = math.gcd(result, abs(value))
    return result


def egcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        return -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def mat_col_update(matrix, left, right, block):
    # Replace columns left,right by their product with the given 2 by 2 block.
    old_left = [row[left] for row in matrix]
    old_right = [row[right] for row in matrix]
    for i in range(3):
        matrix[i][left] = old_left[i] * block[0][0] + old_right[i] * block[1][0]
        matrix[i][right] = old_left[i] * block[0][1] + old_right[i] * block[1][1]


def kernel_coefficient_basis(a):
    # Construct a unimodular V with a V = (g,0,0); its last columns span ker(a).
    current = list(a)
    transform = [[1 if i == j else 0 for j in range(3)] for i in range(3)]
    for j in (1, 2):
        x, y = current[0], current[j]
        if x == 0 and y == 0:
            continue
        d, s, t = egcd(x, y)
        block = [[s, -y // d], [t, x // d]]
        mat_col_update(transform, 0, j, block)
        current[0], current[j] = d, 0
    if current[0] <= 0 or any(current[1:]):
        raise ValueError("could not construct an exact kernel basis")
    if abs(det3(transform)) != 1:
        raise ValueError("kernel coordinate transform was not unimodular")
    return current[0], [[transform[i][j] for i in range(3)] for j in (1, 2)]


def lincomb(coefficients, rows):
    return [sum(coefficients[i] * rows[i][j] for i in range(3)) for j in range(3)]


def verify(data):
    rows, normal = data.get("basis"), data.get("normal")
    if not (isinstance(rows, list) and len(rows) == 3 and all(isinstance(r, list) and len(r) == 3 for r in rows)):
        raise ValueError("basis must be a 3 by 3 integer row matrix")
    if not (isinstance(normal, list) and len(normal) == 3):
        raise ValueError("normal must be a length-three integer vector")
    if any(not isinstance(x, int) or isinstance(x, bool) for row in rows for x in row) or any(not isinstance(x, int) or isinstance(x, bool) for x in normal):
        raise ValueError("basis and normal entries must be integers")
    if gcd_all(normal) != 1:
        raise ValueError("normal must be primitive")
    determinant = det3(rows)
    if determinant == 0:
        raise ValueError("basis must have full rank")
    values = [dot(normal, row) for row in rows]
    g, coefficients = kernel_coefficient_basis(values)
    plane_basis = [lincomb(c, rows) for c in coefficients]
    actual_vector = cross(plane_basis[0], plane_basis[1])
    actual_sq = dot(actual_vector, actual_vector)
    index = abs(determinant)
    norm_sq = dot(normal, normal)
    numerator = index * index * norm_sq
    if numerator % (g * g):
        raise ValueError("integrality check failed for predicted squared covolume")
    predicted_sq = numerator // (g * g)
    return {
        "verified": actual_sq == predicted_sq,
        "index": index,
        "image_generator_g": g,
        "normal_norm_squared": norm_sq,
        "kernel_coefficients": coefficients,
        "plane_basis_rows": plane_basis,
        "actual_covolume_squared": actual_sq,
        "predicted_covolume_squared": predicted_sq,
    }


def main():
    if len(sys.argv) != 2:
        print("usage: check_plane_covolume.py INPUT.json", file=sys.stderr)
        return 2
    try:
        result = verify(json.loads(Path(sys.argv[1]).read_text()))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["verified"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
