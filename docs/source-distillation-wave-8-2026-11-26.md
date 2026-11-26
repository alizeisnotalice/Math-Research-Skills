# 补充文献复核与分析、概率技能整合

本轮逐份重新计算 299 份 PDF 的 SHA-256，并核对物理页数、原文位置和调用条件。队列覆盖补充分册在上轮结束时登记的 120 份候选与 179 份待核来源。15 份提取新构件，7 份确认现行技能已覆盖，26 份留作引用，30 份归入邻近主题。剩余 85 份为候选，136 份保留具体待核依赖。全库候选与待核的不同 SHA-256 从 410 份降至 332 份。[补充分册](../skills/math-research/references/supplemental-sources/README.md)

## 实际校正和计算

- **等差类欧拉积。** Ramaré 的角色展开给出乘积对数的负号。\(q=1\) 的精确归一化检出显示公式与证明的符号差异。用首项加积分上界导出独立尾界，精确回放给出 \(4/2511\)。输入主和的有理区间另作定向认证，并用 24 组 90 位计算作数值交叉核对。[方法与代码](../skills/math-l16-prime-sieve-certified-transfers/references/euler-products-ap-explicit-tail-ext0045.md) · [原刊](https://ramare-olivier.github.io/Maths/FA1853.pdf)
- **扩展的欧拉常数接口。** Padé 工具验证有限接触阶、显式 Hurwitz 系数及有符号余项。在 \(m=n=1,s=0\) 分支给出严格区间 \(1/2<\gamma<3/4\)。其他分支保留辅助常数。Casoratian 工具可核对任意给定有理二阶递推，并明确报告零商分母及零领先系数。欧拉常数无理性所需的全指标整性、非零和衰减仍待建立。[Padé–Hurwitz 入口](../skills/math-prevost-hurwitz-pade-remainder/SKILL.md) · [Casoratian 入口](../skills/math-order-two-casoratian-audit/SKILL.md)
- **斐波那契文献的版面校正。** 原式为 \(3^x-F_n2^y=1\)。纯文本提取容易把 \(2\) 误接到 \(F_n\) 的指数上。按原式代回七组列举解，全部精确相符；来源卡登记了原稿与刊载版身份。[原稿](https://arxiv.org/abs/2401.08205) · [刊载版](https://doi.org/10.1007/s41478-024-00779-4)
- **有限整数与有理工具。** 用实际输入回放了 Apwenian 有限 Hankel 行列式、Tschakaloff 逼近分母、q-stuffle、超几何尾和与概率 Markov 桥。Apwenian 的多项式不消失估计使用有理数，估计范围与依赖源定理的全阶非零结论分别说明。[Hankel 与 Padé](../skills/math-hankel-pade-certificates/SKILL.md)

## 技能入口

- 集中不等式按独立固定时域、过滤固定终点、相对正态尾、鞍点及过程上确界分流。逐步条件 MGF 仍为条件 Hoeffding 的必要输入。保留既有公式、来源和命令。[集中不等式分流](../skills/probability-concentration-chaining/references/deviation-regime-routing.md)
- 将队列生成函数入口由约 15.6 KB 压缩至 5.2 KB。详细模型分支、公式和证据入口迁入按需阅读页。实际符号复算验证了 1-limited 回访中轴项和可去奇点的保留。[队列生成函数入口](../skills/probability-generating-function-boundaries/SKILL.md)
