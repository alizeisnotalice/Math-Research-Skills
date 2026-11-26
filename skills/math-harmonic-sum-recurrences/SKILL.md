---
name: math-harmonic-sum-recurrences
description: 用精确有理算术生成和核对广义超调和数的有限系数。适用于需要把嵌套调和定义化为有限递推、初等对称和或普通调和数的场景；不用于无限 Euler 和、zeta 值化简或无理性结论。
---

# 有限调和和递推

当问题给出正整数 \(m,n\) 与阶数 \(k\)，并需要精确计算广义超调和
系数 \(h_n^{(m)}(k)\) 时，调用本技能。先确认所需对象是有限系数，
而不是其无穷求和或渐近极限。

## 精确接口

运行：

```sh
python3 -B scripts/hyperharmonic_exact.py <m> <n> <order>
```

其中 `m,n >= 1` 且 `order >= 0`。输出的分子、分母均为整数对，值按

\[
h_n^{(m)}(k)=\binom{m+n-1}{m-1}
 e_k\!\left(\frac1m,\frac1{m+1},\ldots,\frac1{m+n-1}\right)
\]

用精确有理算术给出。这里 \(e_k\) 是初等对称多项式，脚本以倒序动态
规划计算它，避免浮点舍入。

对 `order=1,2,3,4`，输出还会给出来源普通调和数公式的
`source_formula_contact`；应检查它与 `value` 一致。最小复现例：

```sh
python3 -B scripts/hyperharmonic_exact.py 2 3 2
```

应返回 `value` 与 `source_formula_contact` 都为 `[3, 2]`。

## 来源与验收

采用的有限构件来自 Ce Xu，*Euler sums of generalized hyperharmonic
numbers*, arXiv:1701.00391v2，原文 Lemma 2.1 与式 (2.3)--(2.11)，
并以式 (2.12)--(2.15) 的前四阶公式交叉核验。完整出处、SHA-256 和
适用范围见 [来源说明](references/xu-hyperharmonic-finite-coefficients.md)。

可运行私有验收：

```sh
python3 -B checks/test_hyperharmonic_exact.py
```

该验收对 \(1\le m\le3\)、\(1\le n\le4\)、\(1\le k\le4\) 的有限
网格逐项比对两种精确公式，并检查非法参数被拒绝。

## 范围边界

- 该接口只认证一个给定 \((m,n,k)\) 的有限有理系数。
- 它不自动求值 \(\sum_n h_n^{(m)}(k)/n^p\)，也不认证相关 zeta 值恒等式；
  这些需要另外给出收敛条件和独立的级数化简证明。
- `Euler`、`Gamma` 或 `Euler--Mascheroni` 的同名出现不能扩展本技能的
  有限范围，更不提供无理性或超越性结论。
