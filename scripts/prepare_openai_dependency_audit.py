#!/usr/bin/env python3
"""Build a reproducible private OpenAI audit snapshot from validated reviews.

The source inventories and review queue stay private.  This program records a
new cohort beside the previous audits, gives selected finite components their
installed routes, and removes superseded cards so that every SHA has one
current classification.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil


ADOPTIONS = {
    "f80267eebc82a9b8905057b45b35ef8734485b2b0b7b809a3051c06240cf0b1e": {
        "skill": "math-l16-prime-sieve-certified-transfers",
        "scope": "有限等差坐标的 CRT 与容斥计数。仅核对给定模数、可逆步长和有限禁止余类，不采用 Jacobsthal 上界或素数计数主结论。",
    },
    "33e92f50d83f53439caa07ff0f71472694dc67d6d7c573e28cad30294b3eb1c0": {
        "skill": "math-honeycomb-finite-boundary-flux",
        "scope": "有限单连通三角域的边界通量精确检查。仅使用给定端口、相位与有限自避路径枚举，不采用条带渐近结论。",
    },
    "20041aa4df40c551ba66fd9629f70a2efbc7778d8ea4e85c8bcfca9519826623": {
        "skill": "probability-markov-spectral-mixing",
        "scope": "平稳可逆链的有限状态二阶增量与 Dirichlet 型界。SK 临界慢混合主定理及其高维随机输入不在范围内。",
    },
    "8d94e973e689e60bdd0443e0f466711519993188fb478dee573993afaf8ff896": {
        "skill": "math-l03-rational-and-interval-certificates",
        "scope": "一维分段有理 ODE 残差、端点屏障和正零阶系数给出的最大原理误差证书。感知机阈值与普适性主张不在范围内。",
    },
}

SCOPED = {
    "f5857c58037fa5289f2f9fe1fe4421af11df8d9fa9b2914ba041469f1195ea31": {
        "skill": "math-f08-matrix-trace-energy",
        "scope": "有限 PSD Gram 矩阵的 trace-energy 核心接口可作限定参考。三角 Hilbert 变差、热流和粗核全局链仍待独立审计。",
    }
}

DISPOSITIONS = {
    "hold": "held",
    "candidate": "candidate",
    "citation": "version-only",
    "adjacent": "adjacent",
}


def jsonl(path: Path):
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            yield number, json.loads(line)


def scrub(value: str) -> str:
    value = re.sub(r"/(?:Volumes|Users|private)/[^\s]+", "[private path omitted]", value)
    return " ".join(value.split())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-audit", type=Path, required=True)
    parser.add_argument("--validated-corpus", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.output.exists():
        shutil.rmtree(args.output)
    (args.output / "cohort-reviews").mkdir(parents=True)
    for name in ("openai-inventory.jsonl", "openai-review-queue.json"):
        shutil.copy2(args.source_audit / name, args.output / name)

    validated = [row for _, row in jsonl(args.validated_corpus)]
    current = {row["sha256"]: row["latest_review"] for row in validated if row["corpus"] == "openai"}
    if len(current) != 186:
        raise ValueError(f"expected 186 validated OpenAI cards, got {len(current)}")

    queue_path = args.output / "openai-review-queue.json"
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    queue["distilled_components"].update(ADOPTIONS)
    queue["reviewed_conditional_references"].update(SCOPED)
    queue_path.write_text(json.dumps(queue, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    retained = []
    seen = set()
    for path in sorted((args.source_audit / "cohort-reviews").glob("*.jsonl")):
        for _, record in jsonl(path):
            digest = record["sha256"]
            if digest not in current:
                if digest in seen:
                    raise ValueError(f"duplicate retained audit record: {digest}")
                retained.append(record)
                seen.add(digest)
    (args.output / "cohort-reviews" / "prior.jsonl").write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in retained),
        encoding="utf-8",
    )

    converted = []
    for digest, review in sorted(current.items()):
        if digest in ADOPTIONS or digest in SCOPED:
            continue
        disposition = DISPOSITIONS.get(review["disposition"])
        if disposition is None:
            raise ValueError(f"unexpected review disposition for {digest}: {review['disposition']}")
        converted.append({
            "sha256": digest,
            "family": next(row["family"] for row in validated if row["sha256"] == digest),
            "locator": scrub(review["locus"]),
            "component": scrub(review["finding"]),
            "dependency": scrub(review["limit"] + " Next review: " + review["next_dependency"]),
            "disposition": disposition,
        })
    if len(converted) != 183:
        raise ValueError(f"expected 183 converted cards, got {len(converted)}")
    (args.output / "cohort-reviews" / "current-validated.jsonl").write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in converted),
        encoding="utf-8",
    )
    print(json.dumps({"current": len(current), "converted": len(converted), "retained": len(retained)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
