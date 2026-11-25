---
name: math-l11-gaussian-projection-density
description: 在精确 Gaussian 线性观测下建立或审查局部质量到投影密度、共同标签纤维与有限状态选择界。用于有限状态回归下界的局部几何步骤，不把预印本中的完整流式下界当作默认定理。
---

# L11 · 精确 Gaussian 投影密度与共同标签

用于对象是有限正 Borel 测度或有限状态学习器的成功质量，观测为独立标准 Gaussian 矩阵 A 及**精确**标签 As 的情形。先写明 (d,m,p,\beta,H,R)、支持球、局部质量不等式，以及是要控制矩阵–标签空间的 a.e. 密度还是指定约束标签上的量。

1. 对一般局部质量测度，使用[精确投影密度](references/projection-density.md)。它给出 γ_m(dA)dy 下的联合 Borel density、完整的半径幂和共同椭球支持。先逐项核对余量 β>m+p-2；没有这个余量，不得套用逆仿射距离矩。
2. 若多个 replicas 共用同一精确标签，读[共同标签纤维](references/equal-label-fibers.md)。只在有限测度恒等式指定的参考测度及其“几乎处处约束标签”范围内取 density 值；不得把 Lebesgue-a.e. 的任意版本代入固定的零测标签。
3. 若一个完整 block 路由至有限个目的地，先给出每个未来成功函数的共同 local-mass scale 和可测 routing kernel。随后可用 backward block estimate；其代价是 (N^{1/q})，不是把状态熵或状态数免费忽略。
4. 面向有限状态流式问题时，状态必须是有限值、初始状态与未观测信号/rows 独立、持久状态数和停止/时钟标签须计入 (N)。当前 block 内可允许任意可测计算与新鲜随机性；这不等于允许保留连续历史。
5. 若需复跑代数和归一化例子，可运行 `scripts/replay_projection_identities.py`，实际应用仍按来源页码核对参数。该 replay 仅检查有限维的 Gram–Schmidt、positive-semidefinite determinant monotonicity、Gaussian difference covariance 和椭球体积；它不是一般定理或流式下界的证明。

## 严格边界

- 本 skill 的默认可用内容仅是 references 中由本地 PDF 逐页核对的 density、support、equal-label finite-measure 及有限状态 block 接口。
- 6 篇同系列预印本的 Ω\((d\log(1/\epsilon))\) 流式 lower bounds、information iteration、critical-radius replacement 和 subsphere recurrences只能作为**待复核的条件性路线**。使用它们前，逐一核对其额外的 entropy、prior、维数余量、版本及跨论文依赖。
- 不适用于有噪声、近似标签、非 Gaussian rows、无限状态/实数寄存器，或只有全局 (L^p) 而无所需 ambient ball-growth 的问题；这些变更需要新的论证。
- 数值积分、模拟或有限 replay 只能提供诊断证据。严格结论仍需引用的测度论、近似恒等式与 Tonelli/duality 步骤完整成立。

本 skill 的固定来源、SHA-256 与已审页码见[来源清单](references/sources.md)。
