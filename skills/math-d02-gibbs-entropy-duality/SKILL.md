---
name: math-d02-gibbs-entropy-duality
description: 推导 Gibbs 变分与熵对偶，检查参考测度、归一化、有限熵和等号条件。
---

> **本轮审核状态（2026-10-07）**：de Oliveira–Salinas 物理论文已逐页阅读，但不作为一般 Donsker–Varadhan 定理的证明来源。下面有限域恒等式按概率密度直接推导；候选来源相关性筛查仍在进行。
> 外部文献证据由第二证据包提供，是独立数据输入，不随单个 Skill 安装。合并交接包中 `EVIDENCE_ROOT` 指向完整包根（同时含 `workspace_revised/`、`audit_current/` 与 `evidence/`）；单独安装时由调用方传入该包根，按本地[证据索引](references/handoff-evidence-index.csv)中的 `portable_path` 查找。无需全局安装，也不要把外部 PDF 当作 Skill 内文件。


# D02 · Gibbs 变分与熵对偶

当前证据状态：**有限域 Gibbs 恒等式可独立使用；广义变分原理须另列可测性、积分和紧性条件**。本状态不表示候选来源筛查已结束。

## 输入与产出

参考概率Q、可测势V、Z=∫e^V dQ、绝对连续分布P及KL定义。

产出应包含适用性判断、使用的假设、数学步骤、证书或界的方向、常数依赖，以及尚未解决的缺口。

## 执行步骤

1. 固定概率测度 `Q`、实值 `Q`-几乎处处有限的可测势 `V`，并验证 `0<Z=∫e^VdQ<∞`。仅在 `P≪Q`、`KL(P‖Q)<∞` 且 `E_P|V|<∞` 时定义 `dQ_V/dQ=e^V/Z` 并逐项展开，得到有限值恒等式 `KL(P‖Q_V)=KL(P‖Q)−E_PV+log Z`。该假设也保证 `KL(P‖Q_V)` 有定义且有限；若任一项为无穷或不可积，不用该差式。
2. 在第1步有限域内由 KL 非负得 `E_PV−KL(P‖Q)≤log Z`。候选等号分布 `Q_V` 只有在允许分布类包含它且 `∫|V|e^VdQ<∞` 时才属于第1步的有限域并取到等号；`Z<∞` 单独不保证该可积性。若需在更大分布类上陈述 `log Z=sup_P(E_PV−KL(P‖Q))`，须单独处理 `E_PV` 的扩展积分及不可积的 `∞−∞` 项；本 Skill 当前不把这种扩展域公式作为已认证结论。该有限概率推导不来自物理论文。
3. 有限经典相空间密度：有限非零能壳体积给S_m−S=kD(ρ||ρ_m)，T>0且Z有限给F[ρ]−F_c=kT D(ρ||ρ_c)，F_c=−kTlogZ。对数和能量/熵的积分域必须匹配。
4. Gibbs–Bogoliubov试探界另检H₀的有限Z₀及E_{ρ₀}|H−H₀|<∞，再写F_c≤F₀+E_{ρ₀}(H−H₀)；该上界方向与正指数收益自由能约定分开。
5. 作者熵增/自由能降证明用对称或详细平衡跃迁、合法换序与无边界通量；Lyapunov单调及平稳性不保证唯一平衡或长时收敛。
6. 带温度或β时从明确的势V=βF或V=−βH重新缩放，保留参考测度与单位；Z无穷、零温或无定义积分只报缺口。

## 证据与失败处理

改变参考Q会改变熵罚；Z无穷时不能建立概率倾斜。

引用定理前按 [来源与阅读状态](references/provenance.md) 定位版本和证据。只有预印本支持的陈述须核对实际依赖的结论、证明步骤和假设。来源或适用范围未核实时，保留已独立推导的部分，并将相应陈述留作研究线索。
需要完整步骤时读 [方法说明](references/method.md)。只有当前请求明确涉及对应的中心立方体研究任务时，才使用 [历史课题接口](references/cube-interface.md)，并先复核当前问题与该接口的假设。
遇到定义缺失、条件不满足或来源未核验，指出具体缺项，保留可证明的弱结论。不得将迁移推断写成原文定理。
依赖表提供方法路线，不表示所有工具之间存在无条件定理蕴含。

用 [适用案例](examples/positive.md) 与 [条件缺失案例](examples/negative.md) 检查适用边界。

对块质量固定的熵正则更新，用[组内变差与熵势函数](references/fixed-block-entropy-updates.md)去掉各块的共同成本变化，核对真实组内范围。

## 有限倾斜树的 Hessian

给定倾斜概率和节点导数时，用[有限 log-power-mean Hessian](references/log-power-hessian.md)核对递推梯度和条件协方差。

## OpenAI 原稿中的方法

- [Finite conditional-entropy and fidelity components](references/openai-network-entropy-2026.md)

- [Finite-mode Fock energy and Gibbs regularization](references/openai-fock-entropy-2026.md)
