# Guillera--Sondow 双积分的高维提升：可安全调用的部分

## 来源、版本与范围

本页固定的实际依赖是 Sergey Zlobin, *Generalizations of
Guillera--Sondow's double integral formulas*,
[arXiv:math/0606287v3](https://arxiv.org/abs/math/0606287v3), 19 Aug 2006。
本地原件为 `EXT-0016_Generalizations_of_Guillera_Sondow_s_double_integral_formulas.pdf`：
SHA-256 `3a46cdd2f9c24953f866d0127385d40a7ef46b016de791945bac7f60c78d6e30`，
共 6 页。以下的页码是该 PDF 的页码。

这是预印本依赖，不应误写为 Guillera--Sondow 的另一篇已发表论文。作者的
[文章页](https://wain.mi-ras.ru/zlobin/indexrus.html)把这一题名列入“some notes
(not planned for publication)”；本次核对没有找到该**题名**的正式期刊版本。
与之不同，Guillera--Sondow 的 *Double integrals and infinite products for
some classical constants via analytic continuations of Lerch's transcendent*
发表于 *Ramanujan Journal* **16** (2008), 247--270；Zlobin 本文第 6 页参考文献
[2] 正是在引用那一篇。因而此处正式书目状态为“arXiv 预印本”，而不是把后者的
期刊信息移植过来。

本文只提供积分恒等式、其分支/定义域，以及可作为正积分检查的接口。它**不**证明
Euler 常数 `gamma` 无理，也不授权把这些立方体积分任意解析延拓到未列出的参数域。

## 记号、分支与严格可用的参数域

令 `m>1` 为整数，`P_j=x_1...x_j`，`P=P_m`，并采用论文的 Lerch 函数
`Phi(z,s,u)`。对复幂，论文取主支

`zeta^s = exp(s Log zeta)`

（`Log` 为主对数；第 3 页 Lemma 1）。因此不能跨过 `z in [1,infinity)` 的割线而
不重新说明边值。其 Theorem 3（第 1--2 页）的两个基本条件为

* `Re(u)>0`；若出现差商，还要 `Re(v)>0`、`u != v`；
* 若 `z in C minus [1,infinity)`，要求 `Re(s)>-m`；若 `z=1`，要求
  `Re(s)>1-m`（Theorem 3 的差商式）。

Theorem 4（第 2 页）的加权式在 `z in C minus [1,infinity)` 时要求
`Re(s)>-m-1`，在 `z=1` 时要求 `Re(s)>-m`。证明先在较小的绝对收敛区域操作，
再在这些明确的全纯域内延拓（第 3--5 页）；这不是“任意解析延拓”的许可。

在本页最常用的实变量专门化中 `0<x_j<1`、`z=1`、`u=1`，所以 `P in (0,1)` 且
`-log(P)>0`：实幂没有支路歧义。

## `gamma` 的正积分接口

Theorem 4 在 `z=1,u=1,s=1-m` 的可去极限给出 Example 2（第 3 页）：

```text
gamma = (m-2)! int_[0,1]^m
  [m-1 - P_1 - P_2 - ... - P_(m-1)]
  / [(1-P)(-log P)^(m-1)] dx_1...dx_m,       m=2,3,... .
```

这里分子在开立方体内严格为正：每个 `P_j in (0,1)`，且
`P_1+...+P_(m-1)<m-1`；分母也正。因此这是 `gamma` 的**正积分表示**，适合做
符号、截断误差或候选构造的正性审计。它来自

```text
Gamma(s+m)(m-2)! [ zeta(s+m) - 1/(s+m-1) ]
```

在 `s+m -> 1` 的极限，使用 `zeta(r)-1/(r-1) -> gamma`；这也解释了为何端点
虽然有表面奇性，整体积分仍有限。

为了和分母证书技能正确衔接，要保持一个限制：此高维表示本身没有一个随 `n`
变化的有限有理系数、最小公倍数或整数线性型。因此它不能单独推出新的
`{log S_n}=...` 型分母排除。只有在另外导出了有限的有理/整数变形，并逐项核实
其对数系数和公分母后，才可把正核用于估计；现有 Sondow 证书的整数性结论仍须
逐字使用其原始有限和，而不能由本页“提升”。

## 一个可复核的局部回放

取 `m=2`，再作三角域代换 `x_1=t_1, x_2=t/t_1`。其 Jacobian 给出

```text
int_[0,1]^2 (1-x_1)/((1-x_1x_2)(-log(x_1x_2))) dx_1 dx_2
 = int_0^1 [-log t - 1 + t]/[(1-t)(-log t)] dt
 = int_0^infinity e^(-u)(u-1+e^(-u))/(u(1-e^(-u))) du.
```

后一个被积函数在 `u>0` 为正（`e^(-u)>1-u`），并在 `u=0` 有可去极限 `1/2`。
2026-11-25 在本机以 Python `decimal`（110 位工作精度）实施独立的
Euler--Maclaurin 回放：`n=10000` 的调和和，加上精确有理 Bernoulli
`B_2,...,B_60` 的 30 个校正项，得到

```text
0.57721566490153286060651209008240243104215933593992359880576723488486772677766467093694706329174674951463144982
```

与上式由 Theorem 4 导出的 `gamma` 一致。此运行是高精度数值交叉核对，不是新的
无理性证明，也不把数值小数升级为严格证书。

## 结构性来源定位

* p. 1--2, Theorem 3：`m` 维 Lerch 差商及单参数积分；
* p. 2, Theorem 4：带 `m-1-P_1-...-P_(m-1)` 核的恒等式；
* p. 3, Example 2：上述 `gamma` 正积分；Lemma 1：主支约定；Lemma 2：单纯形对数
  体积公式；
* p. 3--5：代换 `x_1=t_1, x_j=t_j/t_(j-1)`、Jacobian 与延拓证明；
* p. 6：参考文献中 Guillera--Sondow 文章仍标作 “to appear”，不能作为 Zlobin
  本文的期刊出处。
