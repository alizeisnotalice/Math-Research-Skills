---
name: math-q-series-rational-approximants
description: 对给定有理 q 和 z 生成 Tschakaloff 递推的精确多项式系数，核验有限整数化缩放及余项分离。
---

# q 级数的有理逼近构造

固定来源中的 \(|q|>1\) 与有理参数 \(z\)，按指定的 \(n\) 生成多项式系数。逐项复算约分前的 \(A_n,B_n\) 和带符号的整数化因子。保留缩放基底各因子的来源，记录是否需要额外的分母指数。

若目标涉及无理性度量，另行建立同一无穷指标集上的余项非零、衰减率、系数高度，以及所用常数的适用域。有限整数化可由本技能复算。

## 文献复核采用的构件

- [Tschakaloff finite q-polynomial certificate](references/candidate-04-tschakaloff-polynomial.md)

For a separate finite q-harmonic identity, use the [q-WZ pair](references/amdeberhan-zeilberger-q-wz-harmonic.md).
Provide the two indices and the allowed parameter, and check both the identity and its summation boundary.
