#!/usr/bin/env python3
"""Build a public, source-by-source OpenAI mathematics manuscript index.

The input audit area is deliberately kept private.  This program copies only
the short, human-written audit fields needed to identify the source, its
current review status, and an applicable public skill.  It never publishes a
local PDF path, an extraction path, or the private audit ledger itself.
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import re
from typing import Any


AUDIT_FIELDS = {
    "sha256",
    "family",
    "locator",
    "component",
    "dependency",
    "disposition",
}
REVIEW_DISPOSITIONS = {"candidate", "held", "version-only", "adjacent"}
CURRENT_SOURCES = {"catalogued", "standalone-official-CDN"}

STATUS_LABELS = {
    "installed": "已安装构件",
    "scoped-reference": "限定参考",
    "candidate": "候选构件",
    "held": "保留，依赖待审",
    "version-only": "仅版本或题录核对",
    "adjacent": "邻近材料",
    "pending": "待进行证明核对",
    "archive": "历史版本或状态待确认",
}


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"missing required audit file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON: {path}: {exc}") from exc


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    records = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError as exc:
        raise ValueError(f"missing required inventory: {path}") from exc
    for number, line in enumerate(lines, 1):
        if not line.strip():
            continue
        try:
            value = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at {path}:{number}: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"expected object at {path}:{number}")
        records.append(value)
    return records


def md(value: str) -> str:
    value = re.sub(r"/(?:Volumes|Users|private)/[^\s|]+", "[本机路径已省略]", value)
    value = re.sub(r"(?<!\w)\.local/[^\s|]+", "[私有审计路径已省略]", value)
    return (
        " ".join(value.split())
        .replace("|", "\\|")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("[", "\\[")
        .replace("]", "\\]")
    )


def official_pdf(source: dict[str, Any]) -> str | None:
    value = source.get("official_pdf")
    if source.get("status") == "catalogued":
        pattern = r"https://raw\.githubusercontent\.com/openai/math/[0-9a-f]{40}/preprints/[^\s()<>]+\.pdf"
    elif source.get("status") == "standalone-official-CDN":
        pattern = r"https://cdn\.openai\.com/pdf/[^\s()<>]+\.pdf"
    else:
        return None
    if not isinstance(value, str) or re.fullmatch(pattern, value) is None:
        return None
    # Escape the hyphen when the end of a long title word resembles a token prefix.
    return re.sub(r"(?<=[A-Za-z])sk-(?=[A-Za-z0-9_-]{32})", "sk%2D", value)


def load_subjects(path: Path | None) -> dict[str, str]:
    if path is None:
        return {}
    raw = load_json(path)
    if not isinstance(raw, dict):
        raise ValueError("subject map must be a JSON object")
    if "subjects" in raw:
        subjects = raw["subjects"]
        if not isinstance(subjects, list):
            raise ValueError("subject map subjects must be a list")
        result: dict[str, str] = {}
        labels: dict[str, str] = {}
        for entry in subjects:
            if not isinstance(entry, dict) or not isinstance(entry.get("label"), str):
                raise ValueError("each subject needs a nonempty label")
            label = entry["label"].strip()
            ranges = entry.get("ranges")
            subject_id = entry.get("id")
            if not label or not isinstance(ranges, list):
                raise ValueError("each subject needs nonempty label and ranges")
            if not isinstance(subject_id, str) or subject_id in labels:
                raise ValueError("each subject needs a unique ID")
            labels[subject_id] = label
            for value in ranges:
                if not (
                    isinstance(value, list)
                    and len(value) == 2
                    and all(isinstance(bound, int) for bound in value)
                    and 1 <= value[0] <= value[1]
                ):
                    raise ValueError("subject ranges must be inclusive positive integer pairs")
                for number in range(value[0], value[1] + 1):
                    family = f"{number:03d}"
                    if family in result:
                        raise ValueError(f"overlapping subject range for family: {family}")
                    result[family] = label
        overrides = raw.get("source_overrides", {})
        if not isinstance(overrides, dict):
            raise ValueError("subject source overrides must be an object")
        for digest, subject_id in overrides.items():
            if not re.fullmatch(r"[0-9a-f]{64}", digest) or subject_id not in labels:
                raise ValueError(f"invalid subject override: {digest}")
            result[digest] = labels[subject_id]
        return result
    result = {}
    for family, subject in raw.items():
        if not isinstance(family, str) or not isinstance(subject, str) or not subject.strip():
            raise ValueError("subject map entries must be nonempty string pairs")
        result[family] = subject.strip()
    return result


def load_audits(root: Path, inventory: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    reviews: dict[str, dict[str, Any]] = {}
    review_dir = root / "cohort-reviews"
    for path in sorted(review_dir.glob("*.jsonl")):
        for number, review in enumerate(load_jsonl(path), 1):
            missing = AUDIT_FIELDS - review.keys()
            if missing or any(not isinstance(review[key], str) for key in AUDIT_FIELDS):
                raise ValueError(f"invalid audit fields at {path}:{number}: missing {sorted(missing)}")
            route = review.get("route", "")
            if not isinstance(route, str) or (route and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", route)):
                raise ValueError(f"invalid related skill at {path}:{number}: {route!r}")
            digest = review["sha256"]
            if not isinstance(digest, str) or digest not in inventory:
                raise ValueError(f"unknown source SHA at {path}:{number}: {digest!r}")
            if review["family"] != inventory[digest].get("family", ""):
                raise ValueError(f"family mismatch at {path}:{number}: {digest}")
            if review["disposition"] not in REVIEW_DISPOSITIONS:
                raise ValueError(f"invalid disposition at {path}:{number}: {digest}")
            previous = reviews.get(digest)
            if previous is not None and previous != review:
                raise ValueError(f"conflicting duplicate audit records for SHA: {digest}")
            reviews[digest] = review
    return reviews


def classify(
    source: dict[str, Any], queue: dict[str, Any], reviews: dict[str, dict[str, Any]]
) -> tuple[str, dict[str, str]]:
    digest = source["SHA256"]
    components = queue.get("distilled_components", {})
    conditional = queue.get("reviewed_conditional_references", {})
    historical = source.get("status") not in CURRENT_SOURCES
    if historical and (digest in components or digest in conditional):
        raise ValueError(f"unconfirmed historical source is bound to a skill: {digest}")
    if digest in components:
        record = components[digest]
        if not isinstance(record, dict) or not isinstance(record.get("skill"), str):
            raise ValueError(f"invalid installed component record: {digest}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", record["skill"]):
            raise ValueError(f"invalid installed skill name: {digest}")
        return "installed", {
            "skill": record["skill"],
            "reference": str(record.get("reference", "")),
            "scope": str(record.get("scope", "限定构件已登记。")),
            "commit": str(record.get("latest_commit", "")),
        }
    if digest in conditional:
        record = conditional[digest]
        if not isinstance(record, dict):
            raise ValueError(f"invalid scoped reference record: {digest}")
        if record.get("skill") and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(record["skill"])):
            raise ValueError(f"invalid scoped skill name: {digest}")
        return "scoped-reference", {
            "skill": str(record.get("skill", "")),
            "reference": str(record.get("reference", "")),
            "scope": str(record.get("scope", "限定参考，依赖仍需核对。")),
            "commit": str(record.get("commit", "")),
        }
    if digest in reviews:
        review = reviews[digest]
        return "archive" if historical else review["disposition"], {
            "locator": str(review["locator"]),
            "component": str(review["component"]),
            "dependency": str(review["dependency"]),
            "route": review.get("route", ""),
        }
    return "archive" if historical else "pending", {}


def source_row(source: dict[str, Any], category: str, detail: dict[str, str]) -> str:
    digest = source["SHA256"]
    url = official_pdf(source)
    title = md(str(source.get("title", "untitled source")))
    title_cell = f"[{title}]({url})" if url else title
    family = str(source.get("family", "")) or "未归类"
    inventory_status = md(str(source.get("status", "unknown")))
    source_cell = f"`{digest}`<br>{inventory_status}"
    if category in {"installed", "scoped-reference"}:
        skill = detail.get("skill", "")
        if skill:
            skill_cell = f"[{md(skill)}](../../../{skill}/SKILL.md)"
        else:
            skill_cell = "限定参考未绑定技能"
        reference = detail.get("reference", "")
        if reference and reference != "SKILL.md":
            if not skill or not re.fullmatch(r"(?:references|scripts)/[a-zA-Z0-9_.-]+(?:/[a-zA-Z0-9_.-]+)*\.(?:md|py)", reference) or ".." in reference.split("/"):
                raise ValueError(f"invalid public component reference: {digest}")
            skill_cell += f" · [构件说明](../../../{skill}/{reference})"
        scope = md(detail.get("scope", ""))
        commit = detail.get("commit", "")
        if commit:
            scope = f"{scope}<br>提交 `{md(commit)}`"
        note = f"{skill_cell}<br>{scope}"
    elif category in REVIEW_DISPOSITIONS or "locator" in detail:
        note = (
            f"定位 {md(detail['locator'])}<br>构件 {md(detail['component'])}"
            f"<br>依赖或边界 {md(detail['dependency'])}"
        )
        if skill := detail.get("route"):
            note += f"<br>相关技能 [{md(skill)}](../../../{skill}/SKILL.md)"
    elif category == "pending":
        note = "已完成来源清单与字节身份核对，尚未完成本轮证明构件审阅。"
    else:
        note = "保留版本记录。按当前目录状态核对后再选择可引用的原文。"
    return f"| {family} | {title_cell} | {source_cell} | {STATUS_LABELS[category]} | {note} |"


def section(title: str, entries: list[tuple[dict[str, Any], dict[str, str]]], category: str, subjects: dict[str, str]) -> list[str]:
    lines = [f"# {title}", "", "[返回 OpenAI 文献索引](README.md)"]
    grouped: dict[str, list[tuple[dict[str, Any], dict[str, str]]]] = defaultdict(list)
    for source, detail in entries:
        subject = subjects.get(source["SHA256"], subjects.get(source["family"], "未分配专题"))
        grouped[subject].append((source, detail))
    for subject in sorted(grouped):
        lines.extend([
            "", f"## {md(subject)}", "",
            "| 家族 | 文献 | SHA-256 与目录状态 | 本轮分类 | 构件、定位与边界 |",
            "| --- | --- | --- | --- | --- |",
        ])
        for source, detail in grouped[subject]:
            lines.append(source_row(source, category, detail))
    if not entries:
        lines.extend(["", "本分类目前没有文献。"])
    return lines + [""]


def write(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--audit-root", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--subject-map", type=Path)
    args = parser.parse_args()

    inventory_rows = load_jsonl(args.audit_root / "openai-inventory.jsonl")
    inventory: dict[str, dict[str, Any]] = {}
    for source in inventory_rows:
        digest = source.get("SHA256")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError(f"invalid source SHA-256: {digest!r}")
        if digest in inventory:
            raise ValueError(f"duplicate source SHA-256 in inventory: {digest}")
        for field in ("family", "title", "status"):
            if field not in source:
                raise ValueError(f"missing inventory field {field!r}: {digest}")
        inventory[digest] = source

    queue = load_json(args.audit_root / "openai-review-queue.json")
    if not isinstance(queue, dict):
        raise ValueError("review queue must be a JSON object")
    for key in ("distilled_components", "reviewed_conditional_references"):
        if not isinstance(queue.get(key, {}), dict):
            raise ValueError(f"queue field must be an object: {key}")
        unknown = set(queue.get(key, {})) - set(inventory)
        if unknown:
            raise ValueError(f"queue contains source not in inventory: {sorted(unknown)[0]}")

    reviews = load_audits(args.audit_root, inventory)
    subjects = load_subjects(args.subject_map)
    classified: dict[str, list[tuple[dict[str, Any], dict[str, str]]]] = defaultdict(list)
    for source in sorted(inventory.values(), key=lambda item: (str(item.get("family", "")), item["title"], item["SHA256"])):
        category, detail = classify(source, queue, reviews)
        classified[category].append((source, detail))

    if sum(map(len, classified.values())) != len(inventory):
        raise AssertionError("each inventory source must have exactly one classification")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    category_paths = {
        category: f"{category}.md" for category in STATUS_LABELS
    }
    for category, label in STATUS_LABELS.items():
        write(args.output_dir / category_paths[category], section(f"OpenAI 数学文献 · {label}", classified[category], category, subjects))

    summary = Counter({category: len(classified[category]) for category in STATUS_LABELS})
    overview = [
        "# OpenAI 数学文献逐篇索引",
        "",
        f"本索引覆盖本机审计清单中的 {len(inventory)} 份不同 PDF。每个 SHA-256 只在一个分类页出现一次。",
        "“候选构件”与“保留，依赖待审”均为来源审阅状态，未表示其论文主定理已获独立认证。",
        "",
        "| 分类 | 数量 | 页面 |",
        "| --- | ---: | --- |",
    ]
    for category, label in STATUS_LABELS.items():
        overview.append(f"| {label} | {summary[category]} | [{category_paths[category]}]({category_paths[category]}) |")
    overview.extend([
        "",
        "分类含义",
        "",
        "- 已安装构件。对应技能已通过该轮结构和本机安装验收。它只覆盖表中说明的局部构件。",
        "- 限定参考。现有技能可参照指定段落，仍保留列出的前置条件或依赖。",
        "- 候选构件。逐页审阅发现可进一步蒸馏的局部方法，尚未成为已安装技能。",
        "- 保留，依赖待审。来源含有可定位的路线，但本轮没有接受为可调用构件。",
        "- 仅版本或题录核对。记录来源身份及引用范围。",
        "- 邻近材料。记录已核查的模型、量词、版本或适用范围差异。",
        "- 待进行证明核对。清单、哈希和官方链接已处理，尚缺本轮实际证明阅读。",
        "- 历史版本或状态待确认。撤回、替换或目录外版本保留追溯，不能据此调用结论。",
        "",
        "生成命令",
        "",
        "```sh",
        "python3 scripts/rebuild_openai_source_index.py \\",
        "  --audit-root <private-audit-root> \\",
        "  --output-dir skills/math-research/references/openai-sources \\",
        "  --subject-map provenance/openai-family-subjects.json",
        "```",
        "",
        "输入审计区不进入公开文档。输出只保留官方 PDF 链接、哈希、简短构件定位与公开技能链接。",
        "",
    ])
    write(args.output_dir / "README.md", overview)
    print(json.dumps({"sources": len(inventory), "reviews": len(reviews), "counts": summary}, ensure_ascii=False))


if __name__ == "__main__":
    main()
