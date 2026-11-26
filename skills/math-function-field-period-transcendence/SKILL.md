---
name: math-function-field-period-transcendence
description: 在已给定的正特征 Drinfeld 模、t-motive 与解析平凡化数据下，定位周期、准周期、第三类周期和 Carlitz 张量周期的条件性超越/代数独立接口。
---

# 正特征函数域周期超越性

本技能用于**已经明确编码**的正特征函数域对象。先固定底域、特征、Drinfeld 模秩、CM 状态、周期/对数的线性独立性所在的系数域，以及所用 Frobenius 差分系统或 t-motive。输出只能是满足全部来源门槛时可引用的超越度或代数独立结论；它不从数值近似、有限矩阵或形式等式自动认证这些门槛。

## Rank-two Drinfeld periods and logarithms

对 rank-two `F_q[t]`-Drinfeld 模，调用方必须先给出 odd characteristic、无 CM 证据、周期格基和所需的 `k`-线性独立对数数据。满足来源的 Frobenius 差分方程与最大 motivic-Galois-dimension 输入后，才可使用 period/quasi-period 或 logarithm/quasi-logarithm 的代数独立接口。不要以“rank two”或一个数值周期近似替代 no-CM、差分方程或 Galois 维数证明。

## Third-kind periods

对来源所给的 `alpha tau` 扩张，必须显式指定 t-module、选择的分支、`u`、`omega`、`F_tau`、`Delta` 与 Carlitz-period 项。其符号目标为

```text
lambda = -(u F_tau(omega) - omega F_tau(u))/root_{q-1}(-Delta)
         + f(theta) tilde_pi.
```

若要作代数独立推断，还必须另证 separable CM 及 `End(rho)`-线性独立性。该公式本身不是对任意输入值的独立性证书。

## Prolongations and Carlitz tensor periods

若输入 t-motive 给出 `det(Phi)=c(t-theta)^s`、`sigma(Psi)=Psi Phi`，以及来源要求的 analytic/entire trivialization，可按特化接口把超越度从 `bar K(t)(Psi)` 转到 `bar K(Psi(theta))`。对 `C^(tensor n)` 的周期格结论还须检查 `n` 与特征互素、使用的坐标和在 `t=theta` 的 hyperderivative 约定。有限矩阵代入不会认证解析平凡化，也不会证明代数独立性。

## 停止条件

缺少明确 Drinfeld/t-motive 数据、no-CM 或 separable-CM 证据、所需线性独立性、Frobenius 系统、motivic-Galois 维数或 analytic trivialization 时，只能报告条件未闭合。不得将本技能用于复指数、欧拉常数、一般 E/G-函数，或把期望的 Schanuel 型猜想写成无条件结论。

## 补充来源中的方法

- [Positive-characteristic period-transcendence source interfaces](references/c07-07-drinfeld-periods.md)

## 文献复核采用的构件

- [v-adic Carlitz multiple-polylogarithm period transfer](references/v-adic-carlitz-multiple-polylog-period-transfer-ext0126.md)

- [Anderson generating series from a Drinfeld module](references/anderson-generating-series-ext0104.md)
- [Anderson--Thakur omega interface](references/ext-0073-anderson-thakur-omega.md)
- [Quartic Laurent-series criterion over \(\mathbb F_3\)](references/ext0334-f3-quartic-continuous-fraction.md)
- [Positive-characteristic MZV threshold](references/positive-characteristic-mzv-threshold-ext0191.md)
- [Thakur-hypergeometric period admission](references/thakur-hypergeometric-period-interface.md)
- [Finite-place Carlitz period admission](references/v-adic-carlitz-chowla-selberg-interface.md)

- [Positive-characteristic Mahler specialization](references/hold-03-positive-characteristic-mahler-specialization.md)
