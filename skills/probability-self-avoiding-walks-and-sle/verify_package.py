#!/usr/bin/env python3
"""Verify the self-contained W23 final-scope package after copying or relocation."""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def load(name: str):
    return json.loads((ROOT / name).read_text())

def need(ok: bool, message: str):
    if not ok:
        raise SystemExit("FAIL: " + message)

def resolve_live_path_ref(value: str, context: str, reader_batch: str | None = None) -> Path:
    """Resolve a portable live path, including original-root snapshots and batch-local artifacts."""
    ref = value.strip().strip("\"'").rstrip(".,;:)")
    ref = ref.split("#", 1)[0]
    if ref.startswith("evidence/root/"):
        return ROOT / ref
    if ref.startswith(("reading_coverage.json", "sources.json", "mapping.json", "status.json", "review-index.json")):
        return ROOT / ref
    if ref.startswith(("catalogue/", "downloads/", "reviews/", "workers/", "inputs/")):
        return ROOT / "evidence/root" / ref
    if ref.startswith(("rendered/", "text/")) and reader_batch:
        return ROOT / "evidence/root/workers/W23/reader_batches" / reader_batch / ref
    return ROOT / ref

def validate_nested_live_paths(name: str, value):
    """Check path-bearing fields and every nested evidence/root path, not just top-level PDFs/cards."""
    path_key = re.compile(r"(?:path|paths|file|files|extract|artifact|artifacts|snapshot|record|identity|card|pdf|text|render|coverage|math_check|report|log)$", re.I)
    repo_path_token = re.compile(r"evidence/root/[A-Za-z0-9._/-]+\.(?:pdf|json|md|txt|png|m|csv|tex)", re.I)
    path_suffix = re.compile(r"(?:^|/)[A-Za-z0-9_.-]+\.(?:pdf|json|md|txt|png|m|csv|tex)$", re.I)

    def validate(ref: str, context: str, batch: str | None):
        if not ref or "://" in ref:
            return
        resolved = resolve_live_path_ref(ref, context, batch)
        need(resolved.exists(), f"broken nested live path in {name}{context}: {ref}")

    def walk(node, context="$", inherited_key="", batch=None):
        if isinstance(node, dict):
            local_batch = node.get("reader_batch", batch)
            for key, child in node.items():
                walk(child, context + "/" + str(key), str(key), local_batch)
        elif isinstance(node, list):
            for index, child in enumerate(node):
                walk(child, f"{context}/{index}", inherited_key, batch)
        elif isinstance(node, str):
            # Prose fields sometimes embed one or more repository-relative evidence paths.
            for match in repo_path_token.findall(node):
                validate(match, context, batch)
            # Direct path-valued fields include refs with fragments such as JSON pointers or source IDs.
            direct = node.strip()
            direct_base = direct.split("#", 1)[0]
            if path_key.search(inherited_key) and path_suffix.search(direct_base):
                validate(direct, context, batch)

    walk(value)

# Verify the package-wide freeze manifest first.
manifest_path = ROOT / "integrity_manifest.json"
manifest_sha_path = ROOT / "integrity_manifest.sha256"
need(manifest_path.is_file() and manifest_sha_path.is_file(), "freeze manifest or checksum is missing")
expected_manifest_sha = manifest_sha_path.read_text().split()[0]
need(sha(manifest_path) == expected_manifest_sha, "integrity_manifest.json checksum mismatch")
manifest = json.loads(manifest_path.read_text())
manifest_entries = manifest["files"]
need(isinstance(manifest_entries, list), "manifest.files must be an array")
listed = set()
for row in manifest_entries:
    rel = row["path"]
    need(not Path(rel).is_absolute(), f"manifest path must be relative: {rel}")
    path = ROOT / rel
    need(path.is_file(), f"manifest file is missing: {rel}")
    need(path.stat().st_size == row["bytes"], f"size mismatch: {rel}")
    need(sha(path) == row["sha256"], f"SHA-256 mismatch: {rel}")
    listed.add(rel)
expected_files = {
    p.relative_to(ROOT).as_posix()
    for p in ROOT.rglob("*")
    if p.is_file() and p.name not in {"integrity_manifest.json", "integrity_manifest.sha256"}
}
need(listed == expected_files, "manifest does not cover exactly all payload files")

# Verify source counts and accepted R03 mother-binding evidence.
sources = load("sources.json")
status = load("status.json")
coverage = load("reading_coverage.json")
review_index = load("review-index.json")
need(len(sources) == 30 and len({s["local_id"] for s in sources}) == 30, "expected 30 distinct source records")
need(sum(s["reading_status"] == "fulltext_read" for s in sources) == 28, "expected 28 independent full-text reads")
need(sum(s["reading_status"] == "reuses_canonical" for s in sources) == 2, "expected two canonical reuse records")
need(status["r03_mother_binding_status"] == "passed" and status["r03_mother_accepted_source_count"] == 30, "final R03 mother binding is not recorded as passed")
need(status["publication_approved"] is False and status["scope_review_status"] == "pending_R03_final_scope_review", "scope review/release state is wrong")
need(set(coverage["sources"]) == {s["local_id"] for s in sources if s["reading_status"] == "fulltext_read"}, "coverage must match exactly the 28 full reads")

# All source PDFs and cards must resolve within the relocated package and match their bound hashes.
for s in sources:
    pdf = ROOT / s["local_pdf"]
    card = ROOT / s["card_path"]
    need(pdf.is_file(), f"source PDF missing for {s['local_id']}: {s['local_pdf']}")
    need(card.is_file(), f"source card missing for {s['local_id']}: {s['card_path']}")
    need(sha(pdf) == s["sha256"], f"source PDF hash mismatch for {s['local_id']}")
    decision = s["r03_source_review"]
    need(decision["decision"] == "passed", f"R03 source decision not passed for {s['local_id']}")
    if s["reading_status"] == "reuses_canonical":
        need(decision["usage_evidence_accepted"] and not decision["reading_evidence_accepted"], f"reuse status conflated with a new full read for {s['local_id']}")
    else:
        need(decision["reading_evidence_accepted"], f"full-read evidence not accepted for {s['local_id']}")

# R03 review snapshots must be verbatim hash-bound and final approval must remain non-release.
final_review_path = ROOT / review_index["final_mother_review"]["path"]
need(final_review_path.is_file(), "final R03 mother review missing")
need(sha(final_review_path) == review_index["final_mother_review"]["sha256"], "final R03 review hash mismatch")
final_review = json.loads(final_review_path.read_text())
need(final_review["decision"] == "passed" and final_review["mother_accepted_stage_count"] == 30, "final R03 mother review does not pass 30 sources")
need(final_review["publication_approved"] is False, "R03 publication state must remain unapproved")
for group in (review_index["immutable_R03_W23_review_snapshot_files"] + review_index["canonical_reuse_R05_review_snapshots"]):
    p = ROOT / group["path"]
    need(p.is_file() and sha(p) == group["sha256"], f"review snapshot mismatch: {group['path']}")

# All source-root mirror bindings and the final 76 R03 file bindings must resolve after relocation.
path_bindings = load("portable_path_bindings.json")["source_root_relative_paths"]
for original, row in path_bindings.items():
    p = ROOT / row["scope_path"]
    need(p.is_file() and p.stat().st_size == row["bytes"] and sha(p) == row["sha256"], f"portable source binding mismatch: {original}")
protection = load("protection_check.json")
need(protection["all_76_final_mother_bindings_match"], "final 76-file R03 manifest was not fully bound")
need(protection["all_30_source_pdfs_byte_identical"] and protection["all_pdf_page_counts_match_record"], "source PDF byte or page-count check failed")
need(protection["all_30_source_cards_byte_identical"] and protection["all_W23_math_artifacts_byte_identical"], "card/math byte protection check failed")
copy_check = load("evidence_copy_check.json")
need(copy_check["all_packaged_source_path_snapshots_match_pathmap"], "an immutable evidence snapshot differs from its recorded hash")
need(copy_check["all_current_supplemental_snapshots_match"], "a later current R05/canonical-index snapshot differs from its source copy")
need({a["path"] for a in copy_check["source_current_differences"]} == {"catalogue/canonical_read_index.json", "reviews/R05/review.json"}, "unexpected current source changes outside the two documented R05/canonical-index transitions")
canonical = load("canonical_reuse_evidence.json")
need({a["w23_local_id"] for a in canonical} == {"W23S004", "W23S005"}, "canonical reuse evidence must cover exactly the two reuse records")
for entry in canonical:
    need(not entry["w23_new_fulltext_read_claimed"] and entry["R03_usage_accepted"], f"canonical reuse credit is misclassified for {entry['w23_local_id']}")
    need(entry["canonical_R05_decision"]["reading_evidence_accepted"], f"canonical full-read evidence was not accepted for {entry['w23_local_id']}")

# The live package records and Markdown entrypoints are portable; immutable raw review snapshots remain exact archive bytes.
live_json_names = ["sources.json", "reading_coverage.json", "mapping.json", "status.json", "review-index.json", "canonical_reuse_evidence.json", "dedup_and_version_registry.json", "portable_path_bindings.json", "evidence_copy_check.json", "historical_snapshot_index.json", "path_revision_report.json", "revision_freeze.json", "revision_diff.json"]
for name in live_json_names:
    value = load(name)
    def walk(v, path=""):
        if isinstance(v, dict):
            for k, x in v.items(): walk(k, path + "/<key>"); walk(x, path + "/" + str(k))
        elif isinstance(v, list):
            for i, x in enumerate(v): walk(x, path + f"/{i}")
        elif isinstance(v, str):
            need(not v.startswith("/Volumes/") and not v.startswith("/Users/"), f"absolute local path in live {name}{path}")
    walk(value)
    validate_nested_live_paths(name, value)

# Every finding in the immutable 833-binding review's broken-path report must be resolved in this revision.
broken_path_report = json.loads((ROOT / "evidence/root/reviews/R03/w23_final_v1/broken_live_paths.json").read_text())
need(len(broken_path_report) == 17, "expected the archived R03 report with exactly 17 path findings")
for finding in broken_path_report:
    parts = finding["field"].split("/")
    need(parts[0] == "sources.json" and parts[1].isdigit(), f"unexpected archived R03 path finding pointer: {finding['field']}")
    current = sources[int(parts[1])]
    for part in parts[2:]:
        current = current[part]
    need(isinstance(current, str), f"R03 finding does not resolve to a current path string: {finding['field']}")
    old_ref = finding["path"]
    refs = [old_ref] if old_ref in current else re.findall(r"evidence/root/[A-Za-z0-9._/-]+\.(?:pdf|json|md|txt|png|m|csv|tex)", current, re.I)
    need(bool(refs), f"R03 live path finding has no replacement path in {finding['field']}: {current}")
    for ref in refs:
        target = resolve_live_path_ref(ref, finding["field"])
        need(target.exists(), f"R03 live path finding was not rebound to an existing target at {finding['field']}: {ref}")

# Historical pool/review snapshots are verbatim archives, not upgraded live records.
snapshot_index = load("historical_snapshot_index.json")
need(len(snapshot_index["entries"]) == 6, "historical provenance index must contain exactly six added snapshots")
need("does not update source claims" in snapshot_index["semantics"], "archival snapshot semantics are missing")
for entry in snapshot_index["entries"]:
    archived = ROOT / entry["package_path"]
    need(archived.is_file() and archived.stat().st_size == entry["bytes"] and sha(archived) == entry["sha256"], f"archival provenance snapshot mismatch: {entry['package_path']}")
for rel in ["SKILL.md", "source-guide.md", "scope-review-note.md", "examples/positive.md", "examples/conditional.md", "examples/missing-interface.md"]:
    text = (ROOT / rel).read_text()
    need("/Volumes/data/" not in text and "/Users/zzh/" not in text, f"absolute local path in live Markdown {rel}")
    for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", text):
        if "://" in target:
            continue
        need((ROOT / target).exists(), f"broken relative Markdown target in {rel}: {target}")

print(f"PASS: {len(sources)} works; 28 full reads + 2 accepted canonical usages; final R03 mother binding passed; scope review pending; 17/17 prior live-path findings resolved; nested live paths verified; {len(manifest_entries)} payload files hash-verified.")
