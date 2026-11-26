# 现行引用复核与补取文献蒸馏

本轮将 371 份既有技能原件与冻结版本中的 507 处引用位置逐条对照，另为 63 份补取原件建立可检索来源卡。434 份原件的 SHA-256 和所查物理页均经过校验。已发表论文按版本和实际引用范围处理，预印本卡另记所查结论、证明依赖和缺口。[现行引用](../skills/math-research/references/active-citation-audit-2026-11.md) · [补取文献](../skills/math-research/references/supplemental-sources/recovered-compendium.md)

## 可调用工具及本机验收

| 工具 | 适用范围和实际回放 |
| --- | --- |
| [Euler–Maclaurin 求积误差](../skills/math-euler-maclaurin-quadrature-certificates/SKILL.md) | 根据 Bailey–Borwein 原稿式 (2) 与 Theorem 3 检查有理多项式的端点消失。用 SymPy 生成 36 组多项式、区间及网格，有理误差均落在界内。示例余项恰为 (-181/1419264)。误差包围依赖另行认证的 (pi) 区间。 |
| [标准化单峰分布尾界](../skills/probability-unimodal-tail-certificates/SKILL.md) | 按 Ion–Klaassen–van den Heuvel 的单侧与非对称双侧定理选择分段。6 个取等样例的质量、均值、二阶矩及事件概率残差均精确为零。另验算双侧分界并检查 3 个域外输入。正式版使用 Theorems 5.2、5.5。 |
| [正矩 Hankel 行列式](../skills/math-hankel-pade-certificates/references/moment-hankel-irrationality-gates.md) | 核验 Zudilin 的行整化。对数参数 (a=2,3,4) 和阶数 (1)–(5) 共 15 个精确行列式通过两种算法对照。另复算三组参数各前五个积分矩。(a=3,n=2) 得 (12X^2+16X-32)，(X=log3)。用于 (gamma) 仍需正矩表示和全局速率。 |
| [Gale 的非紧截断](../skills/math-b02-semi-infinite-exchange/references/gale-truncation-boundary.md) | 原例中有限对偶值为 1、完整对偶值为 0。对 (M=1,dots,128) 检查有限最优点在第 (M+1) 条的违约量均恰为 1。 |

实际运行环境为 Python 3.13.18 和 SymPy 1.14.0。有限回放检查确切算术与输入范围。解析假设和全域证明按各技能的来源卡核对。

## 既有技能修正

- 线性扩张现行 CFTP 接口经出版方原文 §4、Theorems 2–3 和 Lemma 1 复核后保留，已修正指向无关论文的旧链接。独立随机块给出正概率合并及有限期望，并保留连续精确采样与近似计数各自的范围。[校正记录](../skills/probability-poset-counting-sampling/references/active-citation-adjudication-20261126.md)
- 分支定界区分采用严格点态不等式的理想 GLB 上确界与有限阶 SOS 截断二次模。半无限交换按 Wang–Guo Theorem 3.4 逐项记录紧性、全局求解及非空迭代输出。带跳输运列出混合阶跳矩的一致界。[GLB 更正](../skills/math-c04-branch-and-bound/references/source-completeness-correction.md) · [交换](../skills/math-b02-semi-infinite-exchange/SKILL.md) · [输运](../skills/math-d01-kantorovich-duality/SKILL.md)
- 行列式依赖恢复四个可直接定位的来源条目。Carcara 更正作者，整数规划证书分列报告修订与 arXiv 上传日期，BAR 引文分列 2024 年在线与 2025 年正式卷期。旧发布清单用于追溯原快照，当前文件以仓库总清单为准。[行列式来源](../skills/probability-determinantal-dependence/references/sources.md) · [优化来源](../skills/probability-optimization-certificates/references/sources.md) · [重交通来源](../skills/probability-queueing-heavy-traffic/references/sources.md)

## Google 下载件和余下资料

共享文献库现有 Google Cogentic 目录为六份 PDF。重新计算的哈希均匹配索引，复跑了 kite 混合、单色矩形秩分裂、边卡组和给定有限群见证。六篇论文的全局新定理仍依赖各自尚未完成的独立审查。[Google 来源与构件](../skills/math-research/references/google-cogentic-2026-11-25.md) · [Google 固定发布](https://github.com/google-research/google-research/commit/4a7bc8ab0bc7)

共享文献库这次盘点有 5,410 个 PDF 文件，按内容哈希去重后为 5,389 份。六类专门来源索引涉及 1,574 个哈希，现行引用复核另登记 371 个，余下 3,444 个哈希尚未进入这些索引或本轮记录。此数字用于安排后续阅读，含有旧技能历史上已引用的文献。
