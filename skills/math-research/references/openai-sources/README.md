# OpenAI 数学文献逐篇索引

本索引覆盖本机文献清单中的 763 份不同 PDF。每个 SHA-256 只在一个分类页出现一次。
OpenAI 现行未撤回稿件默认按原文陈述与假设直接蒸馏。这里的分类描述构件整理、参考和安装状态。

| 分类 | 数量 | 页面 |
| --- | ---: | --- |
| 已安装构件 | 209 | [installed.md](installed.md) |
| 限定参考 | 37 | [scoped-reference.md](scoped-reference.md) |
| 待蒸馏构件 | 263 | [candidate.md](candidate.md) |
| 待整理来源 | 178 | [held.md](held.md) |
| 仅版本或题录核对 | 19 | [version-only.md](version-only.md) |
| 邻近材料 | 25 | [adjacent.md](adjacent.md) |
| 待标构件位置 | 0 | [pending.md](pending.md) |
| 历史版本或状态待确认 | 32 | [archive.md](archive.md) |

分类含义

- 已安装构件。对应技能已通过该轮结构和本机安装验收。它只覆盖表中说明的局部构件。
- 限定参考。现有技能可参照指定段落，仍保留列出的前置条件或依赖。
- 待蒸馏构件。已登记原文位置及可提取方法，等待接入数学技能。
- 待整理来源。保留原文链接及历史线索，具体方法可按原文陈述和适用条件提取。
- 仅版本或题录核对。记录来源身份及引用范围。
- 邻近材料。记录已核查的模型、量词、版本或适用范围差异。
- 待标构件位置。原件与官方链接已登记，尚待补充对应页。
- 历史版本或状态待确认。撤回、替换或目录外版本保留追溯，不能据此调用结论。

生成命令

```sh
python3 scripts/rebuild_openai_source_index.py \
  --audit-root <private-audit-root> \
  --output-dir skills/math-research/references/openai-sources \
  --subject-map provenance/openai-family-subjects.json
```

公开索引提供官方 PDF 链接、哈希、构件位置和技能链接。历史整理数据留在本机。
