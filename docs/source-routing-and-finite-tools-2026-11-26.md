# 文献来源规则与有限证书工具

现行且未撤回的 OpenAI Math 稿件默认按原文结论和显式假设采用。蒸馏记录固定版本、定理或公式定位、适用条件以及本地实现的验收结果。索引保留旧版本、撤回及已有的历史记录。其他来源按版本与实际使用的依赖处理。

## 直接蒸馏自 OpenAI 稿件

| 工具 | 适用条件 | 原文定位与操作 |
|---|---|---|
| 分割不等式与最小生成树 | 小规模连通有理加权图 | *A polynomial-time construction of strong thin trees*，物理页 19，Lemma 3.3。[按分割检验并输出违例](../skills/math-l04-mathematical-programming-workflow/references/partition-mst-separation.md) |
| Foulkes–Howe 双齐次下降算子 | 给定维数、双次数和精确有理系数 | *Quadratic stabilization of the canonical Foulkes–Howe map*，物理页 4，Lemma 2。[构造矩阵、作用和计算秩](../skills/math-l17-filtered-linear-algebra-certificates/references/foulkes-howe-lowering.md) |
| 嵌套 log-power Hessian | 有限支撑，给定倾斜概率、正质量及叶节点导数 | *The low-temperature Sherrington–Kirkpatrick fluctuation scale*，物理页 6–7，Lemma 2.1。[递归计算梯度和 Hessian](../skills/math-d02-gibbs-entropy-duality/references/log-power-hessian.md) |

[OpenAI 逐篇索引](../skills/math-research/references/openai-sources/README.md)仍含 763 份原件记录。209 份已有构件，37 份有适用范围说明，263 份待蒸馏，178 份待整理为具体方法。其余为引用、邻近或版本归档。

## 历史文献与欧拉常数

复核 51 份非 OpenAI 归档。四份来源落实为三个工具，28 份保留构件候选，3 份归入邻近材料，16 份继续保留待核条件。[完整历史文献条目](../skills/math-research/references/historical-sources/dependency-recheck/README.md)。

- [有限信息约束输运](../skills/math-d01-kantorovich-duality/references/finite-information-transport.md)用有理数校验显式路径上的因果、双因果和共同条件分层。638 组有限耦合的前缀等式与直接条件概率判据一致，两个原始与对偶问题的共同值分别为 1 和 2。
- [Horn 矩阵两锥 SPN 证书](../skills/math-c02-completely-positive-copositive/references/horn-two-cone-spn.md)核验给定两锥覆盖及各自的半正定加非负分解。修改矩阵或覆盖输入时拒绝证书。
- [偶数阶计数矩反射](../skills/probability-moment-polynomial-duality/references/even-count-moment-reflection.md)复算相邻成对基的权重及 (p) 与 (1-p) 之间的准确反射。有效范围为给定基、偶数阶及 (0<p<1)。
- [γ 路线的有理多项式定号](../skills/math-l03-rational-and-interval-certificates/references/rational-polynomial-sign.md)用 Bernstein 系数核验指定区间的定号。精确示例给出 (t(1-8t)>0) 于 ((0,1/16])，并识别闭区间左端点的零值。γ 的无理性仍未解决。
- [Bernoulli 和工具](../skills/probability-bernoulli-extremal-orders/SKILL.md)给出 18 页 Auld–Neammanee 稿 Lemma 3.4 所声称统一平方指数矩界的参数族反例。局部极限主定理保留原有待核状态。

[专项技能索引](../skills/math-research/references/research-specialists.md)按主题列出 33 项。高度方程与散度残差示例由 Python 工具入口选择具有 SymPy 的解释器。

[Google Cogentic 索引](../skills/math-research/references/google-cogentic-2026-11-25.md)登记六篇稿件的五个既有技能入口和复现记录。
