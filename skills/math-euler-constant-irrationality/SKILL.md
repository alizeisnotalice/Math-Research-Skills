---
name: math-euler-constant-irrationality
description: 研究欧拉–马歇罗尼常数 γ 的无理性。构造或审计 γ 的 Padé、多重正交、超几何、递推、整数线性形式、分母消去与 Sondow 型判据，也用于核对 E/G 函数、算术 Gevrey 与 Stokes 常数方法能否转移到 γ。
---

# 欧拉常数无理性

用于研究 \(\gamma=\lim_n(H_n-\log n)\) 的逼近、分母排除或无理性路线。先固定本轮结论是有限恒等式/区间、分母排除、无理性，还是无理性指数；候选递推或高精度吻合只是有限证据。[方法和来源选择](references/methods.md) 与 [逐篇来源范围](references/source-scope-gamma.md) 给出按需材料。

## 按输入路由

- **Sondow 分数部分或对数线性形式：** 用 [Sondow 证书](../math-sondow-log-fractional-certificate/SKILL.md)；有限 \(n\) 只排除列明的有理分母，门槛必须在无穷子列上证明。
- **Hessami Pilehrood 收敛子和非简单连分数：** 用 [欧拉常数连分数递推](../math-gamma-continued-fraction-recurrence/SKILL.md) 生成精确有限对象；它不自行给出无理性。
- **有限 \([n/m]\) 指数 Padé 与 Hurwitz 余项：** 用 [Prévost–Hurwitz](../math-prevost-hurwitz-pade-remainder/SKILL.md) 核对接触阶及有符号余项，保留 \(H_s\)、对数和 Hurwitz 值。
- **多重 Laguerre、Hankel、Meijer G 或行列式候选：** 分别用 [多重 Laguerre 逼近](../math-gamma-multiple-laguerre-approximants/SKILL.md)、[Hankel 正矩工具](../math-hankel-pade-certificates/SKILL.md)、[Meijer G 保守矩阵场](../math-gamma-meijer-cmf/SKILL.md) 或 [OpenAI 算术行列式构造](../math-openai-arithmetic-determinants/SKILL.md)。先分开记录原始系数、共同约分、余项和高度。
- **给定指标的严格有限证据：** 用 [Brent–McMillan 有理区间](references/brent-mcmillan-enclosure.md)、[Poisson 调和区间](references/poisson-harmonic-enclosures.md)、[Elsner 变换](references/elsner-transform.md)、[混合形式和高度](references/mixed-log-height-audit.md)、[有限有理级数](references/finite-rational-series.md) 或 [Gregory 系数区间](../math-gamma-gregory-series-interval/SKILL.md)。
- **有限 Euler 级数转广义连分数：** 用 [Euler 级数连分数](../math-euler-series-continued-fraction/SKILL.md)；它只认证选择的有限恒等式。
- **给定二阶递推和相邻解商：** 用 [Casoratian 精确检查](../math-order-two-casoratian-audit/SKILL.md) 核对 Wronskian 型数量的传播与商增量，再独立确认目标极限。
- **交错倒数/Pierce 级数：** 用 [交错倒数连分数判据](../math-alternating-reciprocal-criteria/SKILL.md)；必须证明其全指标增长或整条简单连分数条件。
- **已得到整系数形式的高度与余项界：** 用 [整数线性形式的指数率](../math-integer-linear-form-rates/SKILL.md)。

## γ 路线的证明门槛

先确认目标余项只含 \(\gamma\)，或明确保留所有额外 \(\log\)、\(\zeta\) 或辅助常数并改写结论；不能把多常数逼近当作 \(\gamma\) 的无理性证明。随后按[共享整数线性形式门槛](../math-integer-linear-form-rates/references/integer-linear-form-proof-gates.md)在同一指标子列上处理归一化、整化、非零和趋零。

对于 E/G 函数、算术 Gevrey、1-求和或 Stokes 常数路线，先核对对象类、取值点、奇点、扇区和归一化；读[算术 Gevrey 与 CDT 接口](references/arithmetic-gevrey.md)、[E-算子与和乐界准入](references/e-operator-holonomy-admission.md)及[E-value 归一化门槛](references/e-value-normalization-gate.md)。这些准入条件本身不提供 \(\gamma\) 的表示或无理性。

## 有限余项与补充接口

相邻首项已化为有理多项式时，按 [Bernstein 区间定号](../math-l03-rational-and-interval-certificates/references/rational-polynomial-sign.md)认证指定区间；存在性、整化和无限指标适用性仍分别证明。Prévost 路线使用[有限分母排除](../math-sondow-log-fractional-certificate/references/prevost-legendre-fractional-gate.md)或[二进 Padé 区间](../math-sondow-log-fractional-certificate/references/prevost-pade-rational-interval.md)。

按需要读取：[阶乘分数部分判据](references/hancl-kristensen-factorial-fractional-criterion.md)、[有理调和残数](references/rational-harmonic-residue-algorithm-ext0062.md)、[全 \(n\) 多重校正区间](references/c07-multiple-correction-certified-gamma-bound.md)、[微解/有理逆 Laplace](references/microsolution-rational-laplace-admission.md)、[广义常数线性形式](references/supp-c07-05-linear-forms.md)、[Mahler 专化](references/supp-c07-05-mahler.md)、[调和-\(\zeta\)/log-sine 接口](references/supp-c07-09.md)与[非 holonomic 拒绝边界](references/supp-c07-10-nonholonomic-sequences.md)。

## 补充来源中的方法

- [Quantitative size gate for a Nilsson--Gevrey decomposition](references/supp08-g-operator-size.md)
- [Hypergeometric mod-℘ Frobenius gate](references/supp08-hypergeometric-frobenius.md)
- [Strict E-function logarithm admission gate](references/supp19-e-function-logarithm-admission.md)

## 文献复核采用的构件

- [Brent--McMillan B1 的有限递推](references/brent-mcmillan-b1-1980.md)
- [E-function exceptional-value admission](references/e-function-exceptional-value-admission.md)
- [Euler--Mascheroni 指数动机的条件结论门槛](references/exponential-motive-conditional-gate-fresan-jossen.md)

- [`Ein(1)` as the unique analytic cancellation of gamma and delta](references/ein-gamma-delta-uniqueness-ext0360.md)
- [Rational-term Newton series for Euler's constant](references/rational-newton-gamma-series-ext0023.md)
