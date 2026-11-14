#!/usr/bin/env python3
"""Read-only validation of source coverage and the selected translation results."""

import argparse
import json
import re
from collections import Counter
from pathlib import Path


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def validate(manifest, accepted, base_dir, allow_gaps=False):
    errors, gaps = [], []
    for label, document in (("manifest", manifest), ("accepted", accepted)):
        if (not isinstance(document, dict)
                or type(document.get("schema_version")) is not int
                or document["schema_version"] != 1):
            errors.append(f"{label}: schema_version must be 1")
        if not isinstance(document, dict) or not isinstance(document.get("units"), list):
            errors.append(f"{label}: units must be an array")
    if errors:
        return {"valid": False, "complete": False, "errors": errors, "gaps": gaps}

    source = manifest["units"]
    results = accepted["units"]
    if not source:
        errors.append("manifest: no source units; cannot claim complete coverage")
    if not nonempty(manifest.get("source_label")):
        errors.append("manifest: source_label required")
    glossary = manifest.get("glossary_version")
    if not nonempty(glossary):
        errors.append("manifest: glossary_version required")

    def ids_for(label, units):
        ids = []
        for index, unit in enumerate(units):
            if not isinstance(unit, dict) or not nonempty(unit.get("id")):
                errors.append(f"{label}[{index}]: object with nonempty id required")
                continue
            ids.append(unit["id"])
        duplicates = sorted(key for key, count in Counter(ids).items() if count > 1)
        if duplicates:
            errors.append(f"{label}: duplicate ids {duplicates}")
        return ids

    source_ids = ids_for("manifest", source)
    result_ids = ids_for("accepted", results)
    missing, extra = set(source_ids) - set(result_ids), set(result_ids) - set(source_ids)
    if missing:
        errors.append(f"missing ids: {sorted(missing)}")
    if extra:
        errors.append(f"unexpected ids: {sorted(extra)}")
    if source_ids != result_ids:
        errors.append("accepted ids must match manifest order exactly")
    by_id = {unit["id"]: unit for unit in results
             if isinstance(unit, dict) and nonempty(unit.get("id"))}

    for unit in source:
        if not isinstance(unit, dict) or not nonempty(unit.get("id")):
            continue
        unit_id = unit["id"]
        for field in ("kind", "locator"):
            if not nonempty(unit.get(field)):
                errors.append(f"{unit_id}: {field} required")
        digest = unit.get("source_sha256")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"{unit_id}: lowercase SHA-256 required")
        action = unit.get("action")
        if action not in ("translate", "preserve", "gap"):
            errors.append(f"{unit_id}: invalid action")
        result = by_id.get(unit_id)
        if result is None:
            continue
        if result.get("source_sha256") != digest:
            errors.append(f"{unit_id}: stale source digest")
        if result.get("glossary_version") != glossary:
            errors.append(f"{unit_id}: glossary review version mismatch")
        if action == "gap":
            gaps.append({"id": unit_id, "locator": unit.get("locator"),
                         "note": result.get("note")})
            if result.get("status") != "blocked" or not nonempty(result.get("note")):
                errors.append(f"{unit_id}: gap requires blocked status and note")
            if not allow_gaps:
                errors.append(f"{unit_id}: unresolved gap (use --allow-gaps for partial output)")
            continue
        if result.get("status") != "accepted":
            errors.append(f"{unit_id}: result not accepted")
        has_text = nonempty(result.get("text"))
        has_path = nonempty(result.get("content_path"))
        if not has_text and not has_path:
            errors.append(f"{unit_id}: nonempty text or content_path required")
        if has_path:
            try:
                content = Path(result["content_path"])
                if not content.is_absolute():
                    content = Path(base_dir) / content
                if not content.is_file() or content.stat().st_size == 0:
                    errors.append(f"{unit_id}: content_path missing or empty")
            except (OSError, ValueError):
                errors.append(f"{unit_id}: invalid content_path")

    return {"valid": not errors, "complete": not errors and not gaps,
            "source_units": len(source), "accepted_units": len(results),
            "gaps": gaps, "errors": errors}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("accepted", type=Path)
    parser.add_argument("--allow-gaps", action="store_true")
    args = parser.parse_args()
    try:
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        accepted = json.loads(args.accepted.read_text(encoding="utf-8"))
        report = validate(manifest, accepted, args.accepted.parent, args.allow_gaps)
    except (OSError, ValueError) as exc:
        report = {"valid": False, "complete": False, "errors": [str(exc)], "gaps": []}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
