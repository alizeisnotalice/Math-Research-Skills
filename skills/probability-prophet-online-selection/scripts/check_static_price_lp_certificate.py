#!/usr/bin/env python3
"""Check the supplied finite inequality from Cogentic Lemma 2.1 exactly."""

from fractions import Fraction
import argparse
import json
from pathlib import Path


def rational(value):
    if type(value) not in (int, str):
        raise ValueError("expected an integer or a rational string")
    return Fraction(value)


def all_masks(item_count):
    return range(1 << item_count)


def parse_mask(value, item_count):
    if not isinstance(value, list) or any(type(index) is not int for index in value):
        raise ValueError("subset must be a list of integer item indices")
    if len(set(value)) != len(value) or any(index < 0 or index >= item_count for index in value):
        raise ValueError("subset contains a repeated or out-of-range index")
    return sum(1 << index for index in value)


def mask_name(mask, item_count):
    return [index for index in range(item_count) if mask & (1 << index)]


def subset_table(rows, field, item_count):
    result = {}
    for row in rows:
        mask = parse_mask(row["subset"], item_count)
        if mask in result:
            raise ValueError(f"{field} table contains a repeated subset")
        value = rational(row[field])
        if value < 0:
            raise ValueError(f"{field} table contains a negative entry")
        result[mask] = value
    count = len(result)
    if count.bit_length() - 1 != item_count or count != (1 << item_count):
        raise ValueError(f"{field} table must give every subset")
    return result


def check(data):
    item_count = data["item_count"]
    if type(item_count) is not int or item_count < 1:
        raise ValueError("item_count must be a positive integer")
    metadata = data.get("mechanism_metadata", {})
    if not isinstance(metadata, dict) or any(
        not isinstance(metadata.get(key), str) or not metadata[key].strip()
        for key in ("arrival_order", "tie_rule")
    ):
        raise ValueError("mechanism_metadata must describe arrival_order and tie_rule")
    values = subset_table(data["values"], "value", item_count)
    caps = [rational(value) for value in data["marginal_caps"]]
    prices = [rational(value) for value in data["prices"]]
    if len(caps) != item_count or len(prices) != item_count:
        raise ValueError("marginal_caps and prices must have item_count entries")
    if any(cap < 0 or cap > 1 for cap in caps) or any(price < 0 for price in prices):
        raise ValueError("caps must lie in [0,1] and prices must be nonnegative")
    probabilities = subset_table(data["lambda"], "probability", item_count)
    if sum(probabilities.values()) != 1:
        raise ValueError("lambda probabilities do not sum to one")
    marginals = [sum(probabilities[mask] for mask in all_masks(item_count) if mask & (1 << index)) for index in range(item_count)]
    if any(marginal > cap for marginal, cap in zip(marginals, caps)):
        raise ValueError("lambda violates a marginal cap")
    gamma = rational(data["gamma"])
    subset_prices = [sum(prices[index] for index in mask_name(mask, item_count)) for mask in all_masks(item_count)]
    inequalities = []
    for removed in all_masks(item_count):
        lhs = subset_prices[removed] + sum(
            probability * (values[selected & ~removed] - subset_prices[selected])
            for selected, probability in probabilities.items()
        )
        inequalities.append({"T": mask_name(removed, item_count), "lhs": str(lhs), "holds": lhs >= gamma})
    return {
        "valid": all(row["holds"] for row in inequalities),
        "gamma": str(gamma),
        "marginals": [str(value) for value in marginals],
        "inequalities": inequalities,
        "arrival_order": data["mechanism_metadata"]["arrival_order"],
        "tie_rule": data["mechanism_metadata"]["tie_rule"],
    }



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    try:
        result = check(json.loads(args.certificate.read_text(encoding="utf-8")))
    except (KeyError, TypeError, OSError, ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))
    return 0 if result["valid"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
