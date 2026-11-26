---
name: math-c03-moment-sos-certificates
description: 构建或核验矩与 SOS 层级，检查正多项式证书、截断阶数、紧性和解恢复。
---

> 外部文献证据由第二证据包提供，是独立数据输入，不随单个 Skill 安装。合并交接包中 `EVIDENCE_ROOT` 指向完整包根（同时含 `workspace_revised/`、`audit_current/` 与 `evidence/`）；单独安装时由调用方传入该包根，按本地[证据索引](references/handoff-evidence-index.csv)中的 `portable_path` 查找。无需全局安装，也不要把外部 PDF 当作 Skill 内文件。


# C03 · 矩层级、平方和与正多项式证书

当前证据状态：**条件化可用**。SOS Gram 证书方向与该来源的特定逼近定理已核；这不认证任意半代数集合上的有限阶表示，也不表示候选来源筛查已结束。历史审核记录保存在 `references/verification-log-20261006.md`。

## 输入与产出

多项式目标、变量域/半代数支持集、优化方向与层级阶数；若目标是中心立方体极大算子，另给函数f和中心/尺度定义。

产出应包含适用性判断、使用的假设、数学步骤、证书或界的方向、常数依赖，以及尚未解决的缺口。

## 执行步骤

1. 先定义实际证书锥和次数截断，并区分多项式非负、SOS、模理想SOS及SOS层级等不同命题。
2. 对于矩方法，写明矩变量y、支持和归一化，形成矩矩阵/局部化矩阵并检查所需次数。
3. 对于SOS方法，使用单项式向量和PSD Gram矩阵；最小化下界检查p−γ的证书，最大化上界检查γ−p的证书。
4. 约束集合需要乘子表示时逐项验证Positivstellensatz类型及其次数；有限阶证书与渐近收敛分开陈述。
5. 调用层级收敛定理前核验紧性/Archimedean等具体假设；原子恢复另查平坦延拓条件。
6. 数值Gram矩阵先视为候选；有理化后精确展开多项式或用区间界确认PSD与系数恒等。
7. 若连接中心立方体极大算子，将算子目标保留为外层接口，并独立定义其空间、中心、尺度与可行立方体族；SOS证书只承担已证明的多项式子问题。

## 证据与失败处理

非负多项式未必是SOS；没有相应紧性/Archimedean条件不能任意引用层级收敛。系数ℓ1最佳SOS逼近（Lasserre Theorem 2.1）不等于任意域上的正性证书；浮点PSD容差也不等于精确证书。

引用定理前按 [来源与阅读状态](references/provenance.md) 定位版本和证据。只有预印本支持的陈述须核对实际依赖的结论、证明步骤和假设。来源或适用范围未核实时，保留已独立推导的部分，并将相应陈述留作研究线索。
需要完整步骤时读 [方法说明](references/method.md)。只有当前请求明确涉及对应的中心立方体研究任务时，才使用 [历史课题接口](references/cube-interface.md)，并先复核当前问题与该接口的假设。
遇到定义缺失、条件不满足或来源未核验，指出具体缺项，保留可证明的弱结论。不得将迁移推断写成原文定理。
依赖表提供方法路线，不表示所有工具之间存在无条件定理蕴含。

用 [适用案例](examples/positive.md) 与 [条件缺失案例](examples/negative.md) 检查适用边界。

## 单项归一的 \(x\)-对称双二次型

用 [Kronecker Gram 核验](references/qi-cui-xu-monic-xsymmetric-gram.md)对照显式张量系数与两个有理 PSD 小块。核对目标多项式的逐项一致性和可构造 SOS 的秩上界。

## 对角占优双二次型的 SOS 分解

用[对角占优证书](references/biquadratic-dd-sos.md)核对交叉项分配、系数余量和 SOS 展开。

## 文献复核采用的构件

- [Exact SDP for piecewise SOS-convex moment optimization](references/piecewise-sos-convex-moment-sdp.md)

- [Split full-cross Gram certificate](references/split-full-cross-biquadratic.md)

- [Boolean SOS mixed-derivative gate for submodularity](references/historical-03-boolean-sos-submodularity.md)
- [Congruence-to-diagonal-dominance Gram certificate](references/recent01-congruence-diagonal-dominance.md)
