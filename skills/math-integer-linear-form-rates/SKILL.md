---
name: math-integer-linear-form-rates
description: 用已经证明的整数线性形式高度与双边余项界，生成给定分母的有理逼近下界或推导无理性指数上界。适用于核对 Apéry 型证据和同时逼近的非消失条件。
---

# 整数线性形式的高度与余项

仅在算术前提已由原文或独立证明给出后使用：固定同一序列的实际整数形式 \(\ell_n=q_n\xi-p_n\)，相同指标范围内的高度与双边余项界，以及要证明的结论。完整的归一化、整化、非零、趋零和速率验收见[共享证明门槛](references/integer-linear-form-proof-gates.md)。

## 选择后端

- 若已证明对全部 \(n\ge n_0\)，有 \(0<Lr^n\le|\ell_n|\le Us^n\)、\(0<|q_n|\le QA^n\)，其中 \(0<r\le s<1\le A\)，用[精确下界工具](scripts/linear_form_bound.py)把已证数据转换为给定分母、全体分子有效的下界。
- 若只有高度上界及 \(\log|\ell_n|/n\) 的严格极限，读[指数率与行列式证明](references/rates-and-independence.md)；该推导仍要求同一形式和统一量词。
- 对共享分母的多条余项，逐个证明每个整数线性组合最终非零；单条非零不排除组合抵消。

脚本只处理输入的精确已证界；观测斜率、有限样例和格式校验是有限证据。欧拉常数输入先由[欧拉常数入口](../math-euler-constant-irrationality/SKILL.md)核对是否已隔离为单常数整系数形式。

## 按需来源

[Apéry 超同余有限审计](references/apery-supercongruence-finite-audit.md)、[Apéry \(\zeta(3)\) 完整线性形式](references/apery-zeta3-integrality-and-contraction.md)、[p-adic 收缩和分母账本](references/beukers-padic-contraction-and-denominators.md)、[p-adic L-value 维数界](references/supp-remaining-b-padic-l-values.md)、[向量 Nesterenko 判据](references/supp-remaining-b-vector-nesterenko.md)、[分离指标选择](references/fischler-separated-zeta-index-selection.md)、[高 twist 整除性](references/sprang-higher-twist-divisibility.md)、[移位 Legendre 核](references/supp-c07-08-shifted-legendre-moments.md)、[递推对数约化](references/supp-c07-10-recurrence-log-reduction.md)、[Mellin 矩阵/Minkowski](references/wave5-c08-01-mellin-transfinite-diameter.md)、[Minkowski 独立性准则](references/wave5-c08-01-nesterenko-fischler-zudilin.md)与[奇 \(\zeta\) 形式维数](references/wave5-c08-01-rivoal-odd-zeta.md)。

## 补充来源中的方法

- [Vasilyev--Sorokin multiple-integral coordinate transfer](references/polyzeta-integral-coordinate-transfer-ext0158.md)
- [Tribonacci dominant-root height gate](references/supp-12-tribonacci-dominant-root-height.md)
- [Scoped reference: cubic-Thue to Mordell covariant bridge](references/supp13-mordell-cubic-thue-bridge.md)
- [Thue–hypergeometric lower bounds over imaginary quadratic fields](references/thue-hypergeometric-imaginary-quadratic-wave6-supp10.md)
- [Simultaneous lower bounds for algebraic logarithmic forms](references/wave6-supp-11-gaudron-simultaneous-log-lower.md)
