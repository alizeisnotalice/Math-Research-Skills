---
name: math-elliptic-quasielliptic-function-independence
description: 对已给定椭圆格、指数参数和 Serre 函数参数，依据经认证的线性无关条件调用函数层面的代数独立性；不从数值特殊值或“几乎处处”结论推断特定点独立性。
---

# Elliptic and quasi-elliptic function independence

Start with a specified elliptic lattice (\Omega), an ordered basis
(\omega_1,\omega_2), its Weierstrass functions, source-normalized Serre
functions (f_u), and all parameters. This skill certifies only function
fields over \(\mathbb C\), not values at a chosen point.

For the non-CM route, certify that (t_1,\ldots,t_r) are
\(\mathbb Q\)-linearly independent and that
\(\omega_1,\omega_2,u_1,\ldots,u_s\) are
\(\mathbb Q\)-linearly independent. The cited theorem gives algebraic
independence of

\[
z,\wp(z),\zeta(z),\sigma(z),e^{t_1z},\ldots,e^{t_rz},
f_{u_1}(z),\ldots,f_{u_s}(z).
\]

The CM extension additionally requires the source's endomorphism-field
linear independence and \(\alpha_i\in\operatorname{End}(E)\setminus\mathbb Z\).
Keep the CM and non-CM hypotheses separate. A finite-precision lattice,
unproved linear independence, or an almost-everywhere statement is not a
certificate for either route.

## Source

- [Function-level elliptic/quasi-elliptic independence](references/ext-0074-elliptic-quasielliptic-function-independence.md)
