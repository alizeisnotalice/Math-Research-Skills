#!/usr/bin/env python3
"""Check a bounded 3-adic algebraic-square witness on a small explicit input.

Polynomials are coefficient lists in ascending order.  This is a finite
certificate checker, not a factorization or Newton--Hensel implementation.
"""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path


def die(message: str) -> None:
    raise ValueError(message)


def as_int_list(value: object, name: str) -> list[int]:
    if not isinstance(value, list) or not value or any(
        not isinstance(x, int) or isinstance(x, bool) for x in value
    ):
        die(f"{name} must be a nonempty list of integers")
    return list(value)


def reduce_poly(poly: list[int], f: list[int], modulus: int) -> tuple[int, ...]:
    """Reduce poly modulo a monic f and modulus, returning degree < deg(f)."""
    degree = len(f) - 1
    work = [x % modulus for x in poly]
    if len(work) < degree:
        work += [0] * (degree - len(work))
    for power in range(len(work) - 1, degree - 1, -1):
        lead = work[power] % modulus
        if lead:
            for index in range(degree):
                work[power - degree + index] = (
                    work[power - degree + index] - lead * f[index]
                ) % modulus
    return tuple(x % modulus for x in work[:degree])


def square_mod(poly: list[int], f: list[int], modulus: int) -> tuple[int, ...]:
    product = [0] * (2 * len(poly) - 1)
    for i, left in enumerate(poly):
        for j, right in enumerate(poly):
            product[i + j] += left * right
    return reduce_poly(product, f, modulus)


def has_root_mod_3(f: list[int]) -> bool:
    return any(sum(coefficient * x**i for i, coefficient in enumerate(f)) % 3 == 0
               for x in range(3))


def main(path: Path) -> int:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        die("top-level JSON value must be an object")
    f = as_int_list(raw.get("f"), "f")
    beta = as_int_list(raw.get("beta"), "beta")
    gamma = as_int_list(raw.get("gamma"), "gamma")
    exponent = raw.get("precision_exponent")
    bound = raw.get("coefficient_bound")
    enumerate_roots = raw.get("enumerate_roots", False)
    if not isinstance(exponent, int) or isinstance(exponent, bool) or exponent < 1:
        die("precision_exponent must be a positive integer")
    if not isinstance(bound, int) or isinstance(bound, bool) or bound < 0:
        die("coefficient_bound must be a nonnegative integer")
    if not isinstance(enumerate_roots, bool):
        die("enumerate_roots must be boolean")
    degree = len(f) - 1
    if degree not in (2, 3) or f[-1] != 1:
        die("f must be monic of degree 2 or 3")
    if has_root_mod_3(f):
        die("f modulo 3 has a root, so this small-degree input is not irreducible")
    if len(beta) > degree:
        die("beta must have degree below deg(f)")
    modulus = 3**exponent
    beta_reduced = reduce_poly(beta, f, modulus)
    gamma_reduced = reduce_poly(gamma, f, modulus)
    square = square_mod(list(beta_reduced), f, modulus)
    within_bound = all(abs(coefficient) <= bound for coefficient in beta)
    beta_unit_mod_3 = any(reduce_poly(beta, f, 3))
    result: dict[str, object] = {
        "classification": "square_certificate" if square == gamma_reduced and within_bound and beta_unit_mod_3 else "not_square_certificate",
        "modulus": modulus,
        "f_mod_3_irreducible": True,
        "beta_unit_mod_3": beta_unit_mod_3,
        "within_coefficient_bound": within_bound,
        "beta_squared_mod_f": list(square),
        "gamma_mod_f": list(gamma_reduced),
        "square_congruence": square == gamma_reduced,
    }
    if enumerate_roots:
        count = modulus**degree
        if count > 100_000:
            die("enumeration exceeds the 100000-residue small-instance limit")
        roots = []
        for coefficients in itertools.product(range(modulus), repeat=degree):
            if square_mod(list(coefficients), f, modulus) == gamma_reduced:
                roots.append(coefficients)
        positive = tuple(x % modulus for x in beta_reduced)
        negative = tuple((-x) % modulus for x in beta_reduced)
        result.update(
            enumerated_residue_classes=count,
            enumerated_root_count=len(roots),
            contains_beta=positive in roots,
            contains_negative_beta=negative in roots,
            roots_exactly_plus_minus_beta=set(roots) == {positive, negative},
        )
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError(f"usage: {Path(sys.argv[0]).name} INPUT.json")
        raise SystemExit(main(Path(sys.argv[1])))
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
