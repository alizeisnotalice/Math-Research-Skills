#!/usr/bin/env python3
"""Find an original or a bounded theorem use in the installed literature indexes."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
import re
import unicodedata


SKILLS = Path(__file__).resolve().parents[2]
SHA = re.compile(r"(?<![a-f0-9])[a-f0-9]{64}(?![a-f0-9])", re.IGNORECASE)
HEADING = re.compile(r"^#{2,3} (.+)$")
TITLE_LINK = re.compile(r"^\[([^\]]+)\]\(")
HISTORICAL_CLASSES = {
    "引用核对": "citation",
    "已有技能": "existing",
    "构件候选": "candidate",
    "邻近材料": "adjacent",
    "待核": "hold",
}
OPENAI_CLASSES = {"adjacent", "archive", "candidate", "held", "installed", "pending",
                  "scoped-reference", "version-only"}
SUPPLEMENTAL_CLASSES = {
    "已采用方法": "existing",
    "已采用构件": "existing",
    "已验收构件": "existing",
    "既有方法覆盖": "existing",
    "构件候选": "candidate",
    "条件或证据待查": "hold",
}
ADOPTION_LABELS = {"已采用方法", "已采用构件", "已验收构件", "可调用工具"}
STATUS_CHOICES = sorted(set(HISTORICAL_CLASSES.values()) | OPENAI_CLASSES | {"adopted"})
COLLECTIONS = {
    "historical": ("math-research/references/historical-sources/**/*.md", "- 原件"),
    "supplemental": ("math-research/references/supplemental-sources/*.md", "- 原件"),
    "active": ("math-research/references/active-citation-audit-2026-11.md", "- 原件"),
    "recent": ("math-research/references/recent-non-openai-sources.md", "- 来源与本机版本"),
    "gamma": ("math-euler-constant-irrationality/references/source-scope-gamma.md", "- 版本与身份"),
    "openai": ("math-research/references/openai-sources/*.md", None),
    "cogentic": ("math-research/references/google-cogentic-2026-11-25.md", None),
}


@dataclass(frozen=True)
class Occurrence:
    sha256: str
    title: str
    path: Path
    line: int
    collection: str
    evidence: str
    classification: str | None = None
    adoption_recorded: bool = False
    dependency_rechecked: bool = False


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(re.sub(r"[\W_]+", " ", value).split())


def table_occurrences(path: Path, lines: list[str], collection: str):
    for number, line in enumerate(lines, 1):
        if not line.startswith("| "):
            continue
        cells = [cell.strip() for cell in line.strip("| ").split("|")]
        if len(cells) < 3:
            continue
        digest = SHA.search(cells[2])
        if not digest:
            continue
        title_index = 1 if collection == "openai" else 0
        if collection == "cogentic" and len(cells) >= 5:
            title_index = 3
        title = cells[title_index]
        linked = TITLE_LINK.match(title)
        if linked:
            title = linked[1]
        status = path.stem if collection == "openai" and path.stem in OPENAI_CLASSES else None
        adopted = status == "installed"
        if collection == "cogentic" and len(cells) >= 6 and cells[5] in ADOPTION_LABELS:
            status = "existing"
            adopted = True
        yield Occurrence(digest[0].lower(), title, path, number, collection, line,
                         classification=status, adoption_recorded=adopted)


def section_occurrences(path: Path, lines: list[str], collection: str, identity_prefix: str):
    headings = [(index, m[1]) for index, line in enumerate(lines) if (m := HEADING.match(line))]
    headings.append((len(lines), ""))
    for (index, title), (end, _) in zip(headings, headings[1:]):
        body = lines[index + 1:end]
        identity = next((match for line in body if line.startswith(identity_prefix)
                         and (match := SHA.search(line))), None)
        if identity is None:
            continue
        labels = [entry[2:].partition("。")[0] for entry in body if entry.startswith("- ")]
        adopted = any(label in ADOPTION_LABELS for label in labels)
        classification = None
        rechecked = collection == "historical" and "依赖复核" in labels
        if collection == "historical":
            classification = next((HISTORICAL_CLASSES[label] for label in labels
                                   if label in HISTORICAL_CLASSES), None)
        if collection == "supplemental":
            classification = next((status for status in ("existing", "candidate", "hold")
                                   if any(SUPPLEMENTAL_CLASSES.get(label) == status for label in labels)), None)
        if collection == "gamma" and adopted:
            classification = "existing"
        yield Occurrence(identity[0].lower(), title, path, index + 1, collection,
                         "\n".join([title, *body]).strip(), classification, adopted, rechecked)


def source_occurrences(selected: list[str]):
    for collection in selected:
        pattern, prefix = COLLECTIONS[collection]
        for path in sorted(SKILLS.glob(pattern)):
            lines = path.read_text(encoding="utf-8").splitlines()
            if prefix is None:
                yield from table_occurrences(path, lines, collection)
            else:
                yield from section_occurrences(path, lines, collection, prefix)


def current_records(occurrences: list[Occurrence]) -> dict[tuple[str, str], Occurrence]:
    current = {}
    for item in occurrences:
        key = item.sha256, item.collection
        previous = current.get(key)
        if previous is None or item.dependency_rechecked or (
            not previous.dependency_rechecked
            and (previous.classification is None or item.adoption_recorded)
        ):
            current[key] = item
    return current


def search_occurrences(occurrences: list[Occurrence], sha_prefix: str, terms: list[str],
                       skill: str | None, classification: str | None = None):
    matches: dict[str, list[Occurrence]] = defaultdict(list)
    skill_marker = re.compile(rf"(?<![a-z0-9-]){re.escape(skill)}(?![a-z0-9-])") if skill else None
    latest = current_records(occurrences)
    adopted = {(item.sha256, item.collection) for item in occurrences if item.adoption_recorded}
    for item in occurrences:
        key = item.sha256, item.collection
        if classification == "adopted":
            if key not in adopted:
                continue
        elif classification and classification != latest[key].classification:
            continue
        if sha_prefix and not item.sha256.startswith(sha_prefix):
            continue
        if skill_marker and not skill_marker.search(item.evidence):
            continue
        title = normalize(item.title)
        if terms and not all(term in title for term in terms):
            body = normalize(item.evidence)
            if not all(term in body for term in terms):
                continue
        matches[item.sha256].append(item)
    for items in matches.values():
        items.sort(key=lambda item: not item.dependency_rechecked)
    return matches



def search(selected: list[str], sha_prefix: str, terms: list[str], skill: str | None,
           classification: str | None = None):
    occurrences = list(source_occurrences(selected))
    return search_occurrences(occurrences, sha_prefix, terms, skill, classification)


def summarize(matches: dict[str, list[Occurrence]], occurrences: list[Occurrence]) -> dict[str, dict]:
    matched_keys = {(digest, item.collection) for digest, items in matches.items() for item in items}
    by_collection = defaultdict(Counter)
    for key, item in current_records(occurrences).items():
        if key in matched_keys:
            by_collection[item.collection][item.classification or "unclassified"] += 1
    adopted_keys = {(item.sha256, item.collection) for item in occurrences if item.adoption_recorded}
    adopted = Counter(collection for _, collection in matched_keys & adopted_keys)
    return {
        collection: {"originals": counts.total(),
                     "statuses": dict(sorted(counts.items())),
                     "recorded_adoptions": adopted[collection]}
        for collection, counts in sorted(by_collection.items())
    }


def find_archive_pdf(root: Path, sha256: str) -> str | None:
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise ValueError("archive root must be an existing directory")
    candidates = sorted(path for path in root.rglob("*") if path.suffix.lower() == ".pdf" and path.is_file())
    named = [path for path in candidates if sha256[:16] in path.name.lower()]
    visited = set(named)
    for group in (named, (path for path in candidates if path not in visited)):
        for path in group:
            with path.open("rb") as handle:
                if hashlib.file_digest(handle, "sha256").hexdigest() == sha256:
                    return str(path)
    return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sha", default="", help="SHA-256 prefix of at least 8 hex digits")
    parser.add_argument("--text", default="", help="words to match in titles and source evidence")
    parser.add_argument("--skill", help="exact skill slug named by the recorded evidence")
    parser.add_argument("--collection", action="append", choices=sorted(COLLECTIONS))
    parser.add_argument("--status", choices=STATUS_CHOICES,
                        help="filter explicitly recorded classifications or adoptions")
    parser.add_argument("--summary", action="store_true",
                        help="count distinct matches and classified states per collection")
    parser.add_argument("--archive-root", type=Path, help="locate a local PDF by a full SHA-256 in this directory")
    parser.add_argument("--limit", type=int, default=20, help="maximum distinct original identities printed")
    args = parser.parse_args()
    terms = normalize(args.text).split()
    if args.sha and not re.fullmatch(r"[0-9a-fA-F]{8,64}", args.sha):
        parser.error("--sha requires at least 8 and at most 64 hex digits")
    if args.archive_root and len(args.sha) != 64:
        parser.error("--archive-root requires a full --sha SHA-256")
    if args.limit < 1:
        parser.error("--limit must be positive")
    if not any((args.sha, terms, args.skill, args.collection, args.status, args.summary)):
        parser.error("provide --sha, --text, --skill, --collection, --status, or --summary")
    selected = list(dict.fromkeys(args.collection or COLLECTIONS))
    occurrences = list(source_occurrences(selected))
    matches = search_occurrences(occurrences, args.sha.lower(), terms, args.skill, args.status)
    result = {"matched_originals": len(matches)}
    if args.summary:
        result["collections"] = summarize(matches, occurrences)
    else:
        ordered = sorted(matches.items(), key=lambda pair: (normalize(pair[1][0].title), pair[0]))
        records = [
            {"sha256": digest, "locations": [
                {"title": item.title, "collection": item.collection, "path": str(item.path), "line": item.line,
                 **({"classification": item.classification, "adoption_recorded": item.adoption_recorded,
                     "dependency_rechecked": item.dependency_rechecked}
                    if item.classification or item.adoption_recorded or item.dependency_rechecked else {})}
                for item in items
            ]}
            for digest, items in ordered[:args.limit]
        ]
        result.update({"returned_originals": len(records), "records": records})
    if args.archive_root:
        try:
            result["verified_archive_pdf"] = find_archive_pdf(args.archive_root, args.sha.lower())
        except (ValueError, OSError) as error:
            parser.error(str(error))
    print(json.dumps(result, ensure_ascii=False, indent=2))



if __name__ == "__main__":
    main()
