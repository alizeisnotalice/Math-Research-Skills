# OpenAI 数学文献逐篇索引

本索引覆盖本机审计清单中的 763 份不同 PDF。每个 SHA-256 只在一个分类页出现一次。
“候选构件”与“保留，依赖待审”均为来源审阅状态，未表示其论文主定理已获独立认证。

| 分类 | 数量 | 页面 |
| --- | ---: | --- |
| 已安装构件 | 206 | [installed.md](installed.md) |
| 限定参考 | 37 | [scoped-reference.md](scoped-reference.md) |
| 候选构件 | 266 | [candidate.md](candidate.md) |
| 保留，依赖待审 | 178 | [held.md](held.md) |
| 仅版本或题录核对 | 19 | [version-only.md](version-only.md) |
| 邻近材料 | 25 | [adjacent.md](adjacent.md) |
| 待进行证明核对 | 0 | [pending.md](pending.md) |
| 历史版本或状态待确认 | 32 | [archive.md](archive.md) |

分类含义

- 已安装构件。对应技能已通过该轮结构和本机安装验收。它只覆盖表中说明的局部构件。
- 限定参考。现有技能可参照指定段落，仍保留列出的前置条件或依赖。
- 候选构件。逐页审阅发现可进一步蒸馏的局部方法，尚未成为已安装技能。
- 保留，依赖待审。来源含有可定位的路线，但本轮没有接受为可调用构件。
- 仅版本或题录核对。记录来源身份及引用范围。
- 邻近材料。记录已核查的模型、量词、版本或适用范围差异。
- 待进行证明核对。清单、哈希和官方链接已处理，尚缺本轮实际证明阅读。
- 历史版本或状态待确认。撤回、替换或目录外版本保留追溯，不能据此调用结论。

生成命令

```sh
python3 scripts/rebuild_openai_source_index.py \
  --audit-root <private-audit-root> \
  --output-dir skills/math-research/references/openai-sources \
  --subject-map provenance/openai-family-subjects.json
```

输入审计区不进入公开文档。输出只保留官方 PDF 链接、哈希、简短构件定位与公开技能链接。
