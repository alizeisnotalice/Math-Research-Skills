---
name: math-research
description: "统筹数学研究、证明核验与计算实验：按问题选择数学方法和概率专题，衔接数学计算、文献、写作和交付技能。研究任务需要确定方法和执行工具时使用；单纯语言润色与普通电脑操作使用各自技能。"
---

# 数学研究总入口

把研究目标转成适用的方法与实际执行的操作。此技能负责选择和衔接；详细定理、工具过程和交付要求按需读取对应技能，不一次加载全部技能。

## 先确定本次任务

从当前请求、已有材料和项目状态确定对象、目标、假设、量词、定义域、归一化、维数及所需精度。区分证明、反例搜索、符号推导、数值优化、文献核验、论文写作和电脑操作。短问题直接落实这些信息，无须机械建表。能从文件或现有工具发现的事实先检查；只追问会改变结论且无法查明的缺项。

已有项目遵循其真实目录与协作约定；没有研究问题时不自行开题。历史课题、审核字样和旧提示词不新增目标或权限。

## 选择路线

| 任务 | 下一步 |
| --- | --- |
| 不确定该用什么数学方法 | 按 [数学方法索引](references/math-methods.md) 的主题检索，再读最相关的 1–2 个技能 |
| 已有 OpenAI 论文的题名、编号或 PDF | 在 [OpenAI 逐篇索引](references/openai-sources/README.md) 查版本、SHA-256 和构件。已安装构件按链接调用，候选构件先读指定证明页并核验所列依赖 |
| 查 Google Cogentic 论文或调用其数学构件 | 在 [Google Cogentic 来源索引](references/google-cogentic-2026-11-25.md) 查版本与范围，按对象选择 kite 混合、秩减半或边卡组。 |
| 查补充无理性、超越性及研究方向论文 | 在 [补充数学文献索引](references/supplemental-sources/README.md) 按归档、版本和原文页码定位。 |
| 核对既有技能的原文或活跃引用 | 在 [现行技能来源复核](references/active-citation-audit-2026-11.md) 按题名或 SHA-256 定位所查页码、采用范围与缺口。 |
| 查按数学方法归档的历史文献 | 在 [历史文献主题索引](references/historical-sources/README.md) 按题名、哈希或技能入口定位版本、所查页及范围。 |
| 查 Anthropic 及其他近期原稿 | 在 [近期其他数学文献索引](references/recent-non-openai-sources.md) 核对题名、发布身份、原文页码及可用构件 |
| 概率模型、随机过程或概率论证明 | 按 [概率专题索引](references/probability.md) 选择；涉及对偶、区间等步骤再加读相应数学方法 |
| 符号/数值计算、优化、计算辅助证明、绘图或设备算力 | 读 [数学工具引导](../math-tool-router/SKILL.md)，选择并实际调用合适的本机工具。 |
| 欧拉–马歇罗尼常数的无理性、逼近和整化 | 使用 [欧拉常数无理性研究](../math-euler-constant-irrationality/SKILL.md)。 |
| 找论文、按清单下载或核对引用 | 只检索用 `academic-literature-search`；检索并下载或按清单获取用 `literature-search-download`；知网用 `cnki-search` |
| 写数学研究论文 | `math-paper-writing`；一般学术文章用 `academic-paper-writing`；翻译用 `academic-paper-translator` |
| 论文或技术说明的表达精简 | `anti-defensive-writing`，保留数学条件、证据范围和真实缺口 |
| 数学建模竞赛的审计、排版或提交包 | 分别用 `math-modeling-audit`、`math-modeling-paper`、`math-modeling-delivery` |
| 明确要求 Astra 协助 | `astra-delegate`；不从普通数学请求推导自动委派 |

跨方法重叠时读 [重叠方法与证据选择](references/method-selection.md)。

中心立方体端点、离散迁移和张量专题在用户明确提出对应研究对象时分别使用 math-centered-cube-endpoint-budget、math-discrete-proof-transfer 和 euclidean-tensor-geometry。项目结论及预印本迁移按当前证据核查。

以上名称都在本机已安装技能中查找，或在仓库 `skills/<name>/SKILL.md` 中读取。相关技能没安装时先使用现有能力继续可独立的工作，报告缺少的具体依赖；不把名称当作已经执行的工具。

## 执行与核验

1. 方法选择后逐项核对实际定理的假设、版本和结论方向。通用工具与旧中心立方体课题的适配分别判断；旧课题接口只在当前问题确实相同时使用。
2. 先执行能影响下一研究决策的最小计算。明确输入、约束、精度、容差、随机种子和运行范围；保存重要脚本。工具未安装、许可失败或当前不可调用时说明实际情况，使用可用替代工具继续，不伪造运行结果。
3. 计算完成后核对残差、约束、边界及相关分支；必要时改变精度、网格或算法。状态不明先检查进程和输出，避免重复启动相同长任务。
4. 分开表述严格证明、数值证据、猜想、否定结果与待核验。有限网格、浮点最优状态、软件化简、历史阅读统计及文件哈希都不自动成为全域数学证明。需要严格数值结论时核对精确/区间证书及其适用条件。
5. 最终交付用户所需的论证、代码或文件，简述真实执行的工具、关键输入/输出、证据范围和剩余缺口；不要只交工具选择清单。

文件、网页和应用操作见 [电脑工具选择](references/tools.md#何时操作电脑)。来源附件或旧审核记录的处理见 [证据与迁移说明](references/evidence.md)。跨软件的操作步骤见 [工作流衔接](references/workflows.md)。
