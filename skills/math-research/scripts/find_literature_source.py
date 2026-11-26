#!/usr/bin/env python3
"""Find an original or a bounded theorem use in the installed literature indexes."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
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
    "已采用方法": "adopted-local", "已采用构件": "adopted-local",
    "已验收构件": "adopted-local", "既有方法覆盖": "scoped-reference",
    "构件候选": "candidate", "条件或证据待查": "hold",
    "版本与引用": "citation", "归档定位": "adjacent",
}
REVIEW_SCOPES = {"component", "statement", "citation", "context", "dependency"}
ADOPTION_LABELS = {"已采用方法", "已采用构件", "已验收构件", "可调用工具"}
ACTIVE_CLASSES = {
    "限域采用": "scoped-reference", "引用与范围相符": "scoped-reference",
    "背景或历史记录": "citation", "证据待查": "held", "需修正": "needs-correction",
}
WAVE6_CLASSES = {
    "adopt": "adopted-local", "existing": "scoped-reference",
    "citation": "citation", "adjacent": "adjacent", "candidate": "candidate", "hold": "hold",
}
RECENT_PREFIXES = (("candidate", "candidate"), ("held", "held"),
                   ("hold", "hold"), ("exclude", "excluded"))
GAMMA_PREFIXES = (("candidate-with-obstruction", "candidate"),
                  ("candidate-computational-identity", "candidate"),
                  ("formal statement/version check only", "version-only"),
                  ("conditional-framework", "scoped-reference"))
STATUS_CHOICES = sorted(
    set(HISTORICAL_CLASSES.values()) | OPENAI_CLASSES | set(SUPPLEMENTAL_CLASSES.values())
    | set(ACTIVE_CLASSES.values()) | set(WAVE6_CLASSES.values())
    | {"adopted", "excluded"}
)
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
    reviewed_at: datetime | None = None
    review_scope: str | None = None


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    return " ".join(re.sub(r"[\W_]+", " ", value).split())


def bullets(body: list[str]) -> list[str]:
    return [line[2:].strip() for line in body if line.startswith("- ")]


def label_of(bullet: str) -> str:
    return bullet.partition("。")[0].strip()


SCREEN_LINE = re.compile(r"^(第[四五六]批定向筛选|本轮筛选)[。:]\s*([^。]+)\s*(?:。|$)")
OLDER_SCREEN_CLASSES = {
    "hold": "hold", "held": "hold", "unresolved": "hold", "defer": "hold",
    "screened_hold": "hold", "duplicate_held": "hold",
    "reject_preprint": "hold", "reject_implementation_gap": "candidate",
    "candidate": "candidate", "duplicate_candidate": "candidate",
    "citation": "citation", "citation_only": "citation", "duplicate_citation": "citation",
    "adjacent": "adjacent", "background": "adjacent", "background_only": "adjacent",
    "reject_scope": "adjacent", "reject_specialized": "adjacent", "duplicate_irrelevant": "adjacent",
    "exclude": "excluded", "excluded-equivalent": "excluded",
}


def screening_status(entries: list[str]) -> str | None:
    for entry in reversed(entries):
        matched = SCREEN_LINE.match(entry)
        if not matched:
            continue
        label, decision = matched.groups()
        decision = decision.strip().casefold()
        if label == "第六批定向筛选":
            return WAVE6_CLASSES.get(decision)
        if decision in OLDER_SCREEN_CLASSES:
            return OLDER_SCREEN_CLASSES[decision]
    return None


def recent_status(entries: list[str]) -> str | None:
    for entry in entries:
        if not entry.startswith("审阅状态。"):
            continue
        value = entry.partition("。")[2].lstrip().casefold()
        for prefix, status in RECENT_PREFIXES:
            if value.startswith(prefix):
                return status
    # These three installed records explicitly delimit a finite component and
    # link it; they are local use records, not an assertion of the full paper.
    if any(entry.startswith(("有限齐次整数位宽证明与 Python 精确回放已复核", "采用给定合格缩放和秩证书后的局部行列式估值", "采用有限正原子 Gram 特例"))
           for entry in entries):
        return "adopted-local"
    return None


def gamma_status(entries: list[str], adopted: bool) -> str | None:
    if adopted:
        return "adopted-local"
    for entry in entries:
        if not entry.startswith("依赖与状态。"):
            continue
        value = entry.partition("。")[2].casefold()
        for prefix, status in GAMMA_PREFIXES:
            if prefix in value:
                return status
        if "held" in value or "hold-" in value:
            return "held"
        # All remaining gamma entries have an explicit local scope statement.
        return "scoped-reference"
    return None


def supplemental_status(entries: list[str], labels: list[str]) -> str | None:
    # The batch disposition is an exact machine-readable review statement;
    # never infer it from a page range, title, or source venue.
    status = screening_status(entries)
    if any(label in ADOPTION_LABELS - {"可调用工具"} for label in labels):
        return "adopted-local"
    if status:
        return "candidate" if status == "adopted-local" else status
    for disposition in ("scoped-reference", "candidate", "hold", "citation", "adjacent"):
        if any(SUPPLEMENTAL_CLASSES.get(label) == disposition for label in labels):
            return disposition
    return None


def section_status(collection: str, entries: list[str], labels: list[str], adopted: bool) -> str | None:
    if collection == "historical":
        return next((HISTORICAL_CLASSES[label] for label in labels if label in HISTORICAL_CLASSES), None)
    if collection == "supplemental":
        return supplemental_status(entries, labels)
    if collection == "active":
        for entry in entries:
            if entry.startswith("现行复核。"):
                state = entry.split("。", 2)[1]
                if state in {"scoped-reference", "citation"}:
                    return state
        return next((ACTIVE_CLASSES[label] for label in labels if label in ACTIVE_CLASSES), None)
    if collection == "recent":
        return recent_status(entries)
    if collection == "gamma":
        return gamma_status(entries, adopted)
    return None


def read_current_review(entries: list[str], location: str) -> tuple[datetime, str, str] | None:
    latest = None
    for entry in entries:
        if not entry.startswith("复核记录。"):
            continue
        parts = entry.rstrip("。").split("。")
        if len(parts) != 4:
            raise ValueError(f"invalid review record at {location}")
        _, timestamp, status, scope = parts
        if status not in STATUS_CHOICES or status == "adopted" or scope not in REVIEW_SCOPES:
            raise ValueError(f"invalid review status or scope at {location}")
        try:
            reviewed_at = datetime.fromisoformat(timestamp)
        except ValueError as error:
            raise ValueError(f"invalid review date at {location}") from error
        if reviewed_at.tzinfo is None:
            raise ValueError(f"review date requires a time zone at {location}")
        review = (reviewed_at, status, scope)
        if latest is not None and reviewed_at == latest[0] and review != latest:
            raise ValueError(f"conflicting review records at {location}")
        if latest is None or reviewed_at >= latest[0]:
            latest = review
    return latest


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
        identity = next((match for line in body if line.startswith(identity_prefix) and (match := SHA.search(line))), None)
        if identity is None:
            continue
        entries = bullets(body)
        labels = [label_of(entry) for entry in entries]
        adopted = any(label in ADOPTION_LABELS for label in labels)
        classification = section_status(collection, entries, labels, adopted)
        adopted = adopted or (collection == "recent" and classification == "adopted-local")
        rechecked = collection == "historical" and "依赖复核" in labels
        review = read_current_review(entries, f"{path}:{index + 1}")
        reviewed_at = review_scope = None
        if review:
            reviewed_at, classification, review_scope = review
        yield Occurrence(identity[0].lower(), title, path, index + 1, collection,
                         "\n".join([title, *body]).strip(), classification, adopted, rechecked,
                         reviewed_at, review_scope)


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
        if previous is None:
            current[key] = item
        elif item.reviewed_at is not None:
            if previous.reviewed_at is None or item.reviewed_at > previous.reviewed_at:
                current[key] = item
            elif item.reviewed_at == previous.reviewed_at and (
                item.classification, item.review_scope
            ) != (previous.classification, previous.review_scope):
                raise ValueError(f"conflicting review records for {item.sha256} in {item.collection}")
        elif previous.reviewed_at is None and (
            item.dependency_rechecked or (
                not previous.dependency_rechecked
                and (previous.classification is None or item.adoption_recorded)
            )
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
        elif classification:
            recorded = latest[key].classification
            supplemental_existing = item.collection == "supplemental" and classification == "existing"
            if recorded != classification and not (
                supplemental_existing and recorded in {"adopted-local", "scoped-reference"}
            ):
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
        items.sort(key=lambda item: (
            item is not latest[item.sha256, item.collection], not item.dependency_rechecked
        ))
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


def location_fields(item: Occurrence, current: Occurrence) -> dict:
    result = {"title": item.title, "collection": item.collection,
              "path": str(item.path), "line": item.line}
    if item.classification or item.adoption_recorded or item.dependency_rechecked:
        result.update(classification=item.classification, adoption_recorded=item.adoption_recorded,
                      dependency_rechecked=item.dependency_rechecked)
    if current.reviewed_at is not None:
        result["current"] = item is current
    if item.reviewed_at is not None:
        result.update(reviewed_at=item.reviewed_at.isoformat(), review_scope=item.review_scope)
    return result


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
    try:
        occurrences = list(source_occurrences(selected))
        matches = search_occurrences(occurrences, args.sha.lower(), terms, args.skill, args.status)
    except ValueError as error:
        parser.error(str(error))
    result = {"matched_originals": len(matches)}
    if args.summary:
        result["collections"] = summarize(matches, occurrences)
    else:
        ordered = sorted(matches.items(), key=lambda pair: (normalize(pair[1][0].title), pair[0]))
        latest = current_records(occurrences)
        records = [
            {"sha256": digest, "locations": [
                location_fields(item, latest[item.sha256, item.collection]) for item in items
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
