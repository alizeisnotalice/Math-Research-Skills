# OpenAI 原稿方法、Bernoulli 分布与欧拉常数证书

七组并行处理固定版本的 OpenAI 数学稿件，按原文定理、公式和显式假设提取方法，验收本地实现。和既有逐篇索引去重后，53 份原件更新了归属，其中 52 份已绑定构件，1 份绑定限定参考。32 份方法说明归入 31 个现有技能。索引当前包含 763 份原件，其中 261 份已绑定构件，38 份有限定参考，210 份待蒸馏，178 份待定位具体方法。[逐篇索引](../skills/math-research/references/openai-sources/README.md)。

## 已实现的方法

| 所用资料 | 有限工具范围 |
| --- | --- |
| 代数中的稳定坐标 | 用 SymPy 精确核验给定行列式为一的替换矩阵和逆。[坐标环](../skills/math-l19-coordinate-ring-certificates/references/stable-coordinate-four-variables.md) |
| 二叉树上的凸性亏损 | 对整数指数和有理子质量验算亏损与轻子结点的下界。[树预算](../skills/math-e03-tree-bellman-cross-layer-budget/references/openai-direct-wave-2.md) |
| 随机簇与树后验 | 给定边外连通性计算一条边的条件概率，或用有理数直接校验两个二元对称信道的后验合成。[随机簇](../skills/probability-percolation-renormalization/references/openai-200-226.md) · [树后验](../skills/probability-nonlinear-law-dynamics/references/openai-tree-posterior-components.md) |
| 谱隙与 Einstein 曲率块 | 对给定对角基准矩阵计算核上的压缩 Schur 项，或由两个有理谱块核验归一化四维 Einstein 模型的最小截面曲率。[谱隙](../skills/math-c01-semidefinite-lifting/references/openai-kernel-gap-perturbation-2026.md) · [曲率块](../skills/math-geometric-pde-reductions/references/openai-geometry-wave-2.md) |
| 有限域 Hamming 过滤 | 核验词长 `2p−1` 上区分距离 0 和 `p` 的算式，在 `p=3,q=2` 重放 1,024 对词。[张量过滤](../skills/math-l06-tensor-rank-accounting/references/openai-equal-or-far-filter.md) |

## 已改写的既有入口

[独立 Bernoulli 分布](../skills/probability-bernoulli-extremal-orders/SKILL.md)以输入模型和目标选择方法，原有来源范围和案例汇入可独立打开的参考页。计算器共享原 Kleiner 工具的有理系数递推，输出精确质量与尾概率，并比较随机序、凸序、似然比序和反风险率序。实际比对 341 组精确枚举分布及 400 对分布，原 Kleiner 三个算例输出一致。

欧拉常数路线新增 [Prévost 的有理余项与分母排除](../skills/math-sondow-log-fractional-certificate/references/prevost-legendre-fractional-gate.md)。核对本机原稿作者及所用积分公式后，用 Beta 积分推出有限显式上界。(n=4,m=1) 时上界为 (81/17920)，精确排除既约分母整除 12 的情形。54 组高精度计算用于交叉诊断，严格界来自积分推导和有理区间。一般分母仍待处理。[Prévost 原稿](https://arxiv.org/abs/math/0507231v1)。

从补充无理性文献中更新两份正式发表来源的用途。平衡次数 PCF 指数公式需先证明收敛、阶乘约化及非等性。广义 q-对数定理可用于符合原文条件的有理参数。[连分数接口](../skills/math-gamma-continued-fraction-recurrence/references/pcf-factorial-reduction-admission.md) · [q-对数接口](../skills/math-sondow-log-fractional-certificate/references/generalized-q-log-irrationality.md)。

本机盘点包含 5,389 份不同 PDF。补充无理性与超越性集合有 498 份原件，其中的逐篇来源定位和蒸馏状态按实际已采用的方法记录。[补充索引](../skills/math-research/references/supplemental-sources/README.md)。
