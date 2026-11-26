#!/usr/bin/env python3
"""Exact finite-law certificate for the fixed-coordinate sampling lemma."""
import argparse
import itertools
import json
import sys
from fractions import Fraction


def fraction(value):
    try:
        return Fraction(str(value))
    except (ValueError, ZeroDivisionError) as exc:
        raise ValueError("expected an exact rational string: %r" % (value,)) from exc


def ceiling(x):
    return -((-x.numerator) // x.denominator)


def load_law(path):
    with open(path, encoding="utf-8") as handle:
        raw = json.load(handle)
    q0, q, epsilon = (fraction(raw[key]) for key in ("q0", "q", "epsilon"))
    if not (Fraction(0) < q0 < q < Fraction(1) and Fraction(0) < epsilon < Fraction(1)):
        raise ValueError("require 0 < q0 < q < 1 and 0 < epsilon < 1")
    atoms = []
    width = None
    for atom in raw["atoms"]:
        bits = atom["bits"]
        if not isinstance(bits, str) or not bits or set(bits) - {"0", "1"}:
            raise ValueError("every atom needs a nonempty 0/1 bits string")
        if width is None:
            width = len(bits)
        if len(bits) != width:
            raise ValueError("all bit strings must have the same length")
        probability = fraction(atom["probability"])
        if probability < 0:
            raise ValueError("atom probabilities must be nonnegative")
        atoms.append((tuple(int(bit) for bit in bits), probability))
    if not atoms or sum(probability for _, probability in atoms) != 1:
        raise ValueError("atom probabilities must sum exactly to 1")
    return q0, q, epsilon, atoms, width


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("law", help="JSON finite rational binary law")
    parser.add_argument("--ell", type=int, required=True, help="nonnegative tested-draw bound")
    args = parser.parse_args()
    try:
        q0, q, epsilon, atoms, k = load_law(args.law)
        if args.ell < 0:
            raise ValueError("ell must be nonnegative")
        high_cutoff = ceiling(q * k)
        p_high = sum(probability for bits, probability in atoms if sum(bits) >= high_cutoff)
        if p_high == 0:
            raise ValueError("upper-tail event has probability zero")
        if (q / q0) ** args.ell < Fraction(4, 1) / (epsilon * p_high):
            raise ValueError("ell does not meet (q/q0)^ell >= 4/(epsilon*pH)")
        lower_bound = p_high * q ** args.ell / 2
        found = None
        for size in range(min(args.ell, k) + 1):
            for coordinates in itertools.combinations(range(k), size):
                p_c = sum(probability for bits, probability in atoms if all(bits[i] for i in coordinates))
                b_c = sum(probability for bits, probability in atoms if all(bits[i] for i in coordinates) and sum(bits) * q0.denominator < q0.numerator * k)
                if p_c >= lower_bound and b_c <= epsilon * p_c:
                    found = coordinates, p_c, b_c
                    break
            if found:
                break
        if found is None:
            raise AssertionError("no witness found; this contradicts the checked lemma preconditions")
        coordinates, p_c, b_c = found
        payload = {
            "status": "certified-finite-law",
            "k": k,
            "ell": args.ell,
            "p_H": str(p_high),
            "event": "sum(bits) >= %d" % high_cutoff,
            "C_zero_based": list(coordinates),
            "p_C": str(p_c),
            "required_p_C_at_least": str(lower_bound),
            "conditional_lower_tail": str(b_c / p_c),
            "epsilon": str(epsilon),
        }
        print(json.dumps(payload, sort_keys=True))
    except (KeyError, ValueError, AssertionError) as exc:
        print("rejected: %s" % exc, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
