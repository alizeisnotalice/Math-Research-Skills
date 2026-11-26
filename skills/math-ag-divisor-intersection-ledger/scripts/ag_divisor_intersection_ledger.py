#!/usr/bin/env python3
"""Exact finite ledger checks for supplied algebraic-geometric divisor data.

This checks rational coefficient tables and stated finite pairings.  It does
not construct resolutions, maps, divisors, sections, or intersection products.
"""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path


class InputError(ValueError):
    pass


def rat(value):
    if isinstance(value, bool) or isinstance(value, float):
        raise InputError("all scalar values must be exact integers or rational strings, never bool/float")
    try:
        return Fraction(value)
    except (TypeError, ValueError, ZeroDivisionError) as exc:
        raise InputError(f"invalid exact rational {value!r}") from exc


def show(value):
    if isinstance(value, Fraction):
        return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if isinstance(value, dict):
        return {key: show(item) for key, item in value.items()}
    if isinstance(value, list):
        return [show(item) for item in value]
    return value


def divisor(value, label):
    if not isinstance(value, dict):
        raise InputError(f"{label} must be an object mapping prime ids to exact coefficients")
    result = {}
    for prime, coeff in value.items():
        if not isinstance(prime, str) or not prime:
            raise InputError(f"{label} has a non-string or empty prime id")
        parsed = rat(coeff)
        if parsed:
            result[prime] = parsed
    return result


def require_attestations(task, names):
    flags = task.get("attestations")
    if not isinstance(flags, dict):
        raise InputError("attestations must be an object")
    missing = [name for name in names if flags.get(name) is not True]
    if missing:
        raise InputError("missing caller-supplied geometric attestations: " + ", ".join(missing))


def result(kind, valid, checks, conclusion=None):
    answer = {"kind": kind, "valid": valid, "checks": checks}
    if conclusion is not None:
        answer["conditional_conclusion"] = conclusion
    return answer


def intersection_zero_sum(task):
    kind = "intersection_zero_sum"
    require_attestations(task, ["effective_nef_cartier_divisor", "ample_cartier_divisor",
                                "complete_prime_component_list"])
    components = task.get("components")
    if not isinstance(components, list) or not components:
        raise InputError("components must be a nonempty list")
    seen, total, degrees, errors = set(), Fraction(0), {}, []
    for item in components:
        ident = item.get("id")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise InputError("component ids must be unique nonempty strings")
        seen.add(ident)
        multiplicity = rat(item.get("multiplicity"))
        degree = rat(item.get("degree"))
        if multiplicity <= 0 or multiplicity.denominator != 1:
            errors.append(f"{ident}: multiplicity must be a positive integer")
        if degree < 0:
            errors.append(f"{ident}: supplied nef intersection degree is negative")
        total += multiplicity * degree
        degrees[ident] = degree
    if total != 0:
        errors.append(f"weighted component sum is {show(total)}, not 0")
    if not errors:
        return result(kind, True, {"weighted_sum": total, "component_degrees": degrees},
                      "All listed component degrees are 0. Under the supplied effective-nef/ample "
                      "geometric contract, this is the componentwise consequence of N^2.H=0.")
    return result(kind, False, {"weighted_sum": total, "component_degrees": degrees, "errors": errors})


def common_resolution_forms(task):
    kind = "common_resolution_forms"
    require_attestations(task, ["common_smooth_resolution", "proper_normal_integral_resolution",
                                "forms_trivialize_stated_boundaries"])
    degree = task.get("degree")
    if isinstance(degree, bool) or not isinstance(degree, int) or degree <= 0:
        raise InputError("degree must be a positive integer")
    x = divisor(task.get("pulled_back_divisor_theta_x"), "pulled_back_divisor_theta_x")
    y = divisor(task.get("pulled_back_divisor_theta_y"), "pulled_back_divisor_theta_y")
    difference = {prime: y.get(prime, Fraction(0)) - x.get(prime, Fraction(0))
                  for prime in sorted(set(x) | set(y))}
    difference = {prime: coeff for prime, coeff in difference.items() if coeff}
    if difference:
        return result(kind, False, {"ratio_divisor": difference},
                      None)
    return result(kind, True, {"ratio_divisor": {}},
                  "The quotient of the two supplied pulled-back forms has zero divisor.  Under the "
                  "attested proper normal integral-resolution hypotheses it is a nonzero scalar; with "
                  "the stated boundary trivializations this passes the B-birational form criterion.")


def vertical_divisor(task):
    kind = "vertical_divisor"
    require_attestations(task, ["contraction_of_normal_projective_varieties", "normal_projective_generic_fibre",
                                "complete_prime_divisor_support"])
    components = task.get("components")
    if not isinstance(components, list):
        raise InputError("components must be a list")
    horizontal = {}
    all_coefficients = {}
    seen = set()
    for item in components:
        ident, location = item.get("id"), item.get("location")
        if not isinstance(ident, str) or not ident or ident in seen:
            raise InputError("component ids must be unique nonempty strings")
        if location not in ("horizontal", "vertical"):
            raise InputError("location must be horizontal or vertical")
        seen.add(ident)
        coeff = rat(item.get("coefficient"))
        all_coefficients[ident] = coeff
        if location == "horizontal" and coeff:
            horizontal[ident] = coeff
    if horizontal:
        return result(kind, False, {"horizontal_coefficients": horizontal,
                                    "all_coefficients": all_coefficients})
    return result(kind, True, {"horizontal_coefficients": {}, "all_coefficients": all_coefficients},
                  "The supplied divisor has no horizontal component.  For the caller-supplied rational "
                  "function, the stated normal-projective generic-fibre lemma therefore identifies it with "
                  "an element of the base function field.")


def same_degree_principal_descent(task):
    kind = "same_degree_principal_descent"
    require_attestations(task, ["geometrically_integral_normal_projective", "characteristic_zero",
                                "integral_weil_divisor", "base_change_indexing_verified"])
    geometric = divisor(task.get("base_changed_divisor"), "base_changed_divisor")
    principal = divisor(task.get("principal_witness_divisor"), "principal_witness_divisor")
    difference = {prime: geometric.get(prime, Fraction(0)) - principal.get(prime, Fraction(0))
                  for prime in sorted(set(geometric) | set(principal))}
    difference = {prime: coeff for prime, coeff in difference.items() if coeff}
    if difference:
        return result(kind, False, {"base_change_minus_principal_witness": difference})
    return result(kind, True, {"base_change_minus_principal_witness": {}},
                  "The supplied base-changed integral divisor equals a principal witness.  Under the "
                  "attested characteristic-zero geometric hypotheses, same-degree principal descent applies "
                  "to the original divisor.")


def mixed_intersection_table(task):
    kind = "mixed_intersection_table"
    require_attestations(task, ["smooth_projective_source", "birational_map_to_normal_projective_target",
                                "globally_generated_cartier_D", "very_ample_cartier_A",
                                "exceptional_divisors_complete", "base_pairing_established_geometrically"])
    d, k, y = task.get("dimension"), task.get("image_dimension"), task.get("base_dimension")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in (d, k, y)) or not (0 <= k < y <= d):
        raise InputError("require integer dimensions 0 <= image_dimension < base_dimension <= dimension")
    exceptional = divisor(task.get("exceptional_pairings"), "exceptional_pairings")
    nonzero_exceptional = {name: value for name, value in exceptional.items() if value}
    semiample = rat(task.get("semiample_pairing"))
    base = rat(task.get("base_pairing"))
    errors = []
    if nonzero_exceptional:
        errors.append("some supplied exceptional pairings are nonzero")
    if semiample != 0:
        errors.append("the supplied q^*D pairing is nonzero")
    if base <= 0:
        errors.append("the supplied h^*H pairing is not strictly positive")
    checks = {"exceptional_pairings": exceptional, "semiample_pairing": semiample, "base_pairing": base}
    if errors:
        checks["errors"] = errors
        return result(kind, False, checks)
    return result(kind, True, checks,
                  "The supplied finite pairing ledger has the vanishing/positivity pattern of the mixed "
                  "intersection test.  It may be used only together with the attested geometric construction "
                  "of C=(q^*D)^k(q^*A)^(d-k-1).")


CHECKERS = {
    "intersection_zero_sum": intersection_zero_sum,
    "common_resolution_forms": common_resolution_forms,
    "vertical_divisor": vertical_divisor,
    "same_degree_principal_descent": same_degree_principal_descent,
    "mixed_intersection_table": mixed_intersection_table,
}


def check(document):
    tasks = document.get("tasks") if isinstance(document, dict) else None
    if not isinstance(tasks, list) or not tasks:
        return {"valid": False, "errors": ["input must be an object with a nonempty tasks list"]}
    results = []
    for index, task in enumerate(tasks):
        if not isinstance(task, dict):
            results.append({"index": index, "valid": False, "errors": ["task must be an object"]})
            continue
        kind = task.get("kind")
        try:
            if kind not in CHECKERS:
                raise InputError(f"unknown task kind {kind!r}")
            item = CHECKERS[kind](task)
        except (InputError, KeyError) as exc:
            item = {"kind": kind, "valid": False, "errors": [str(exc)]}
        item["index"] = index
        results.append(item)
    return show({"valid": all(item["valid"] for item in results), "results": results,
                 "scope": "Exact finite-table audit only; every geometric attestation remains caller-supplied."})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="JSON ledger")
    parser.add_argument("-o", "--output", type=Path, help="result JSON path (default stdout)")
    args = parser.parse_args()
    try:
        document = json.loads(args.input.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"cannot read JSON: {exc}")
    answer = check(document)
    text = json.dumps(answer, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        sys.stdout.write(text)
    raise SystemExit(0 if answer["valid"] else 1)


if __name__ == "__main__":
    main()
