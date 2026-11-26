---
name: math-cmzv-rational-pullback
description: Place specified iterated integrals or multiple polylogarithms in a cyclotomic MZV space through a verified rational-pullback criterion.
---

# Cyclotomic MZV rational pullbacks

Use this skill for a concrete rational map and a convergent iterated integral
whose poles and endpoint values have already been specified. It records a
source theorem placing the value in a named cyclotomic multiple-zeta space.

For an integer \(N\ge3\), set
\[
 S_N=\{0,\infty,1,e^{2\pi i/N},\ldots,e^{2\pi i(N-1)/N}\}.
\]
The source criterion requires a rational function \(R\) with
\(R^{-1}(R(S_N))=S_N\) and \(\{0,1,\infty\}\subset R(S_N)\). For a word
of forms \(dx/(x-a_i)\), also check \(a_1\ne1\), \(a_k\ne0\), convergence,
and \(a_i\in R(S_N)\). It then places the integral in the weight-\(k\)
level-\(N\) cyclotomic MZV space.

This is a membership route. It does not compute a basis, prove relations among
CMZVs, settle a Galois-descent conjecture, or convert a CMZV into an Euler
constant linear form. Read [the source contract](references/au-cmzv-rational-pullback.md)
before using it.
