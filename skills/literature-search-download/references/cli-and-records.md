# 命令与记录格式

用 Python 3.10+ 执行 `scripts/literature.py`。检索/解析只用标准库，PDF 下载校验需 PyMuPDF 或 pypdf；优先发现已有环境。下例从技能目录运行，实际使用改为绝对脚本路径与独立输出目录。

```bash
python3 scripts/literature.py search --source crossref --query 'quantum entanglement education' --limit 15 --output candidates.json
python3 scripts/literature.py search --source arxiv --query 'ti:"quantum entanglement" AND cat:quant-ph' --limit 10 --output arxiv.json
python3 scripts/literature.py resolve --doi '10.1038/nature12373' --output resolved.json
python3 scripts/literature.py download --manifest papers.json --out pdf --report download-results.json
```

`LITERATURE_EMAIL` 仅设为用户提供的联系邮箱；resolve 有此变量才用 Unpaywall，没有则正常解析 Crossref 并记 OA 跳过，可通过网页补查。不输出带邮箱或密钥的请求 URL。

search 返回 `{query, source, retrieved_at, papers, errors}`；resolve 返回 `{doi, retrieved_at, papers, errors, notes}`。题录始终为待核验候选；失败非零退出但仍保存结构化错误；成功空结果才表示查询无匹配。筛选、核验并合并为 `papers.json`，保留原结果作日志附件。

download 接受数组或 `{ "papers": [...] }`。示例仅说明格式，URL 是占位符，不能执行：

```json
{"papers": [{
  "id": "001", "title": "已核对的原题名",
  "authors": ["Family, Given"], "year": 2024, "venue": "发表来源",
  "doi": null, "verification_status": "pending_verification",
  "reading_scope": "metadata", "metadata_sources": ["https://example.org/record"],
  "relevance": "与研究问题的关系",
  "pdf_candidates": [{"url": "https://example.org/paper.pdf", "source": "机构仓储", "version": "acceptedVersion"}]
}]}
```

候选只放检查过的真实公开链接；resolve 的 `link_hints` 需检查后再加入候选。每篇最多 5 个候选、每链接一次，依序回退；单文件默认上限 100 MiB，socket 超时 30 秒，总传输窗口检查 120 秒，相邻请求间隔 3 秒。socket 读直到超时才返回，传输窗口不是硬实时截止。

下载报告记路径、来源、版本、页数、哈希、attempts 和 `identity_status`。成功状态 `downloaded_pending_identity` 仅表示结构通过；代理看首页后另行更新身份为 `verified` 或 `mismatch`，错论文隔离，不在取得数中计入。扫描件需视觉验收。工具不作语义身份判断或 BibTeX 导出。

已有同名文件不覆盖；重跑用 `--resume 旧报告.json`，只复用同 URL 且哈希一致、解析通过的文件，保持待核验身份状态；否则报告冲突。每次用新的报告路径，报告与 PDF 文件路径不得重叠。

最终 `papers.json` 保留核验出处/版本关系/阅读范围/下载结果，未知字段 null。代理按已核验版本生成 BibTeX，正确转义、完整作者、唯一引用键，待核验不导出。日志记录执行的查询、筛选去重和失败；Markdown 清单分开统计结构通过和身份核验，列补取路径。
