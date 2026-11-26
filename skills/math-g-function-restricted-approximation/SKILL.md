---
name: math-g-function-restricted-approximation
description: 对已认证为有理系数非有理 G-函数的有理值，调用有效的固定基底分母逼近下界；也用于限制其 b 进制展开中的长重复数字块。
---

# G-function fixed-base approximation gate

Use this only after the caller supplies a rational-coefficient G-function presentation for
`F`, a proof that `F(z) notin Q(z)`, and integers `a != 0`, `b,B >= 1`. The source theorem
provides effectively computable constants depending on `F` (and on `t` for one threshold),
but this skill does not manufacture those constants from a bare power series.

1. Check the G-function data: algebraic Taylor coefficients with its growth and common
   denominator controls, plus a homogeneous differential equation over `Q(z)`.
2. Prove `F(z) notin Q(z)`, fix `t >= 0`, and verify `b > (c1 |a|)^c2`, `B <= b^t`, and the
   stated lower threshold for `m`.
3. Only then invoke the source inequality for fractions `n/(B b^m)`. A weaker
   `b^(-m(1+epsilon))` corollary has further sufficiently-large thresholds in `F,a,epsilon,t`.
4. Treat digit-block conclusions as consequences for the exact base and evaluation point
   in the source, not as an irrationality test for arbitrary analytic functions.

Read [the source statement and version record](references/fischler-rivoal-g-function-fixed-base.md)
before claiming a numerical bound.
