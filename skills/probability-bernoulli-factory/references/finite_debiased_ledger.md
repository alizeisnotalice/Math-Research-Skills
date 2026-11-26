# 有限随机截断 debiasing ledger

Koskela--Karvonen--Łatuszyński--Spanò 的 Theorem 2 使用无限支撑的独立随机层数 `L`、兼容 Bernstein 下包络系数以及其收敛/间隙率，构造 `[0,1]` 值的无偏估计量。现有 W17-N003 来源卡已保存该完整定理。本组件只对用户给定的**有限** `L` 支撑和有限 coefficient table 作精确有理审计。

对 `L<=K`，把原文式 (7) 的 survival weight 换成所给有限 `L` 的真实 `P(L>=n)`。若 `H_l(n,s)` 是将 degree-`n` 下系数对给定 `(l,s)` 作 hypergeometric thinning 的平均，则脚本逐条列出

`psi(l,s)=H_l(k-1,s)+sum_{n=k}^l (H_l(n,s)-H_l(n-1,s))/P(L>=n)`。

在独立 `x`-coin 下，有限求和严格给出

`E_x[psi(L,S_L)]=g_K(x)`，

而不是一般的极限目标 `f(x)`。因此 ledger 分开报告：

- **stopped evidence**：本有限 proxy 必停、最大未知 `x`-coin 数 `K`；
- **expectation evidence**：精确 `E[psi]`、`g_K(x)` 及（若给定）目标点值的偏差；
- **running/pathwise evidence**：全部 `(L,S_L)` 的 `psi`、增量符号和 `[0,1]` 范围；
- **cost evidence**：精确 `E[L]`，绝不由必停推出一般无限方案的有限均值。

`lower_compatibility_holds_on_supplied_rows` 只检查提供的有限行，不能证明存在满足 Theorem 1 的无限 upper envelope、统一 gap rate或 (g_n\to f)。即使有限 ledger 的输出范围是 `[0,1]` 且一个 `x` 点无偏，也不等于一般 Bernoulli factory。

## 样例

```sh
python3 scripts/audit_finite_debiased_ledger.py --input examples/affine_exact_finite_ledger.json
python3 scripts/audit_finite_debiased_ledger.py --input examples/finite_table_not_a_factory.json
```

第一个样例使用仿射函数 `f(x)=1/4+x/2`；Bernstein reproduction 使每个 `g_n=f`，所以有限 proxy 在给定点确实无偏。第二个样例所有有限 lower rows 均为零而声称目标为 `1/2`：范围、停止和有限 telescope 都成立，但输出期望是零。这是专门防止把有限表格检查误写成无限 factory 的反例。

## 来源与版本

- Jere Koskela, Toni Karvonen, Krzysztof Łatuszyński, Dario Spanò, *A debiased Bernoulli factory and unbiased estimation of a probability*, arXiv:2510.01941v2，2026-09-01（本地 PDF dated 2026-09-02），SHA-256 `85bc6a2ec6b57416f3b492bb6d45d5fe0cd5353061f77f95ac2a946cb95bca18`。Theorem 2 及证明为 pp. 4--7，Corollaries 1--2 和成本限制为 pp. 7--9。
- 原文允许 `1<lambda<(rho-1)/2`；其 `L` 的均值不是 Theorem 2 自动保证。由幂和可独立推得 `E[L^r]<∞` 需要 `lambda>r+1`，所以该特定 power-law 方案要能选择有限均值时需 `rho>5`。这是充分的 construction-specific 成本结论，不是一般 factory 下界或存在性判据。
