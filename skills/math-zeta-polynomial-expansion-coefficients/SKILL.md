---
name: math-zeta-polynomial-expansion-coefficients
description: 精确生成指定 Riemann ζ 多项式展开系数中的 γ、ζ(2),…,ζ(m+1) 与有理余项；不数值求 ζ，也不认证无穷级数收敛。
---

# ζ 多项式展开的精确系数

Use this skill when the requested object is the finite coefficient (x_m) in
the source's critical-strip polynomial expansion, rather than a numerical
evaluation of ζ or a claim about Euler's constant.

For (m=0), the coefficient is

\[
x_0=\gamma-1.
\]

For (m\geq1), retain the symbolic identity

\[
x_m=\gamma+\sum_{k=1}^{m}\binom{m}{k}(-2)^k\zeta(k+1)+r_m,
\qquad
r_m=(-1)^{m+1}+\sum_{k=1}^{m}\frac{1+(-1)^{k-1}}{k}.
\]

Generate the integer coefficients and reduced rational remainder without
approximating the constants:

```bash
python3 scripts/zeta_polynomial_coefficient.py 4
```

The output is an exact JSON expression. The script validates only the finite
binomial/rational transformation. To invoke the source's infinite expansion,
separately check its domain (0<\Re(s)<1), its polynomial basis, and the
convergence proof; no finite coefficient calculation establishes convergence,
irrationality, or a relation among the constants.

## Source

- [Exact zeta-polynomial coefficient transform](references/ext-0033-zeta-polynomial-coefficients.md)
