# 分块记录与覆盖校验

## 用途与所有权

长文、多个 subagent 或断点续译采用以下最小记录；短文允许用等价清单。所有文件放在本次任务的工作目录，主 agent 单独维护 manifest、术语表、任务状态及 accepted.json。subagent 只写各自的 attempt 文件。

- `manifest.json`：按源文顺序列出本次范围内的所有内容单元；排除项在单独范围说明中记录。
- `glossary.md`：主 agent 发布带版本号的术语表，保留英文、中文、适用含义及定位。
- `tasks.json`：主 agent 记录每块的任务 ID、单元 ID、源文摘要、术语版本、模型路由、尝试编号、状态与结果路径。状态至少区分 pending/running/produced/accepted/failed；produced 不等于通过验收。
- `attempts/<任务ID>-<尝试编号>.json`：独立不可混写的候选结果，并附候选术语和疑问。重试写新文件；取消或晚到的任务仍需比对当前尝试及来源版本。
- `accepted.json`：主 agent 选择并复核的唯一有效结果，按 manifest 顺序展开。不得把全部尝试直接拼接。

## 最小合同

manifest 顶层包含 `schema_version: 1`、`source_label`、`glossary_version`、`units`。每个 unit：

| 字段 | 含义 |
| --- | --- |
| `id` | 文献内稳定唯一 ID，例如 `s02-p003`、`fig02-labels`、`eq04` |
| `kind` | 标题、正文、脚注、图、图题、图内文字、表、公式、附录、参考文献等非空类别 |
| `action` | `translate`、`preserve` 或 `gap` |
| `locator` | 可回查的源页/章节/表号/区域 |
| `source_sha256` | 当前单元原文的 SHA-256；文本使用 UTF-8 原文，图片使用源裁剪字节，多个相关资源先按固定顺序合并。保留被哈希的快照，不只哈希 ID |

accepted 顶层包含 `schema_version: 1` 和 `units`。每项包含同一 `id`、`source_sha256`、已复核的 `glossary_version` 和 `status`。非缺口项的 `status` 为 `accepted`，并须有非空 `text` 或 `content_path` 至少一个；`content_path` 相对 accepted 文件目录解析，可以指向图、公式或表格内容文件，文件必须非空。缺口项用 `status: blocked` 并提供非空 `note`，无需伪造 text 或资源文件。

```json
{
  "schema_version": 1,
  "source_label": "用户提供的论文 第2节",
  "glossary_version": "v1",
  "units": [
    {
      "id": "s02-p001",
      "kind": "paragraph",
      "action": "translate",
      "locator": "第2页 第2节 第1段",
      "source_sha256": "由对应原文计算的64位十六进制摘要"
    }
  ]
}
```

以上摘要文字仅解释字段，实际记录必须使用真实哈希。任务分配保留“输出 ID 清单”和“只读上下文”两个字段；上下文页、相邻段落不进入本任务输出。

## 验收与恢复

1. 验证候选任务/尝试是当前有效分配，输出 ID 恰好等于分配范围，没有上下文混入。核对源摘要；只接受当前来源的结果。
2. 对照原文检查译文并解决候选术语，再标记 accepted。术语修订后回查已接受内容；确认不受影响的块可更新复核版本，受影响的块先修正，不能只机械改版本号。
3. 源文改变时比较单元快照。重新处理变化的单元，同时检查受影响的上下文、编号与术语；其他已验收块可复用。章节插入不能导致旧 ID 被赋给新内容。
4. 合并只选已接受的一个结果。任务错误、超时和取消均保留尝试记录；先确认远端状态，不能无限重试或让两次尝试竞争写入。
5. 对 manifest 的完整性先做源文人工检查：校验器不知道清单中未曾登记的脚注或图表，不能检测这种遗漏。

## 运行只读校验

使用环境可用 Python 3，`<skill_dir>` 指当前技能目录：

```bash
python3 <skill_dir>/scripts/check_coverage.py manifest.json accepted.json
```

脚本检查 schema、ID 唯一性、覆盖范围、顺序、来源摘要、术语复核版本、验收状态及内容文件可用性。退出码 0 表示这些结构检查通过，1 表示需修复；不检查译文准确性或最终 Word 是否渲染正确。

明确交付含缺口的部分结果时使用 `--allow-gaps`，缺口仍必须登记为 `action: gap`、`status: blocked` 并有原因。输出 `complete: false` 和缺口列表，不能将这种成功检查声称为全文完成。
