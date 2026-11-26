---
name: math-semiclassical-orthogonal-deformations
description: 对给定半经典正交权及移动奇点，核验递推系数的 Toda 变形方程和 Freud 权的 Painleve IV 化简。
---

# 半经典正交多项式变形

用于正规半经典正交多项式，权的对数导数必须为有理函数。固定正交弧、分支、全部奇点及其留数，再给出三项递推的归一化。

- 对广义 Jacobi 权，按 [Toda 变形门槛](references/magnus-semiclassical-toda-ext0612.md) 构造 \(W,V,\Theta_n,\Omega_n\)，验证奇点互异和非整数留数，才可使用其中的 \(\dot a_n,\dot b_n\) 方程。
- 对 \(\exp(-x^4/4-tx^2)\) 的实轴权，文中的 Freud 关系与 \(a_n\) 的 Painleve IV 形式可作已给定初值的方程审计。正性、全局存在性和所选 Painleve 解仍需来自权的正交性和边界条件。

不能把任意三项递推、退化奇点或未指定的复路径输入到此接口。
