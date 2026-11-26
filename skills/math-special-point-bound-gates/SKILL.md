---
name: math-special-point-bound-gates
description: Apply Paulin's explicit special-point discriminant and root-of-unity order bounds to a supplied curve in P1 x Gm after checking its field, polynomial and geometric hypotheses.
---

# Explicit special-point bound gates

Use this skill for a curve \(F(X,Y)=0\) over a number field that contains a point
\((j(\tau),\lambda)\), where \(j(\tau)\) is a singular modulus and \(\lambda\) is a
root of unity.  Supply the degree \(d=[K:\mathbb Q]\), a nonconstant
\(F\in K[X,Y]\), \(\delta_1=\deg_XF\), \(\delta_2=\deg_YF\), and its projective
coefficient height \(h(F)\).  Establish that the zero set has no horizontal or
vertical line, equivalently that \(F\) has no nonconstant divisor in \(K[X]\) or
\(K[Y]\).

With those caller-certified data, [Paulin's bound](references/paulin-andre-oort-bound.md)
sets
\[
C=2^{36}d^3\delta_2^3\log(4d\delta_2)^2
\max\{dh(F)+(d-1)(\delta_1+\delta_2)\log2,1\}.
\]
It gives \(|\Delta|<(C\log C/(d\delta_2))^2\) and
\(N<C(\log C)^2\log\log C\).  These bounds reduce special-point enumeration to
finite CM discriminants and roots of unity.  A usable enumeration still needs exact
number-field arithmetic, CM-class-polynomial data, and direct evaluation of \(F\).

This skill does not decide irreducibility, find horizontal or vertical components,
enumerate singular moduli, or supply a general André--Oort algorithm.
