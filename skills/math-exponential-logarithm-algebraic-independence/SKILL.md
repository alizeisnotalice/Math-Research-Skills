---
name: math-exponential-logarithm-algebraic-independence
description: 核对 Mahler 1931/32 指数与对数代数独立性及多项式非消失下界的精确适用条件。
---

# Mahler exponential--logarithm independence

Use this skill only after the input has been proved to meet one of the exact
source hypotheses.  It has two narrow theorem interfaces.

1. For algebraic \(\vartheta_1,\ldots,\vartheta_N\) linearly independent
   over \(\mathbb Q\), and a Liouville number \(\lambda\), the tuple
   \((e^{\vartheta_1},\ldots,e^{\vartheta_N},\lambda)\) is algebraically
   independent over \(\overline{\mathbb Q}\).  Likewise, if \(z\) is the
   real logarithm of a positive rational other than one, or \(z=\pi\), then
   \((z,\lambda)\) is algebraically independent over
   \(\overline{\mathbb Q}\).  See
   [Part I scope](references/mahler-part-i-independence.md).
2. For nonzero \(z\) which is either the real logarithm of a positive
   rational or \(2\pi i\), Part II supplies a non-effective lower bound for
   every nonzero **integer-coefficient** polynomial in \(z\), with exponent
   exponential in its degree.  See
   [Part II polynomial lower bound](references/mahler-part-ii-polynomial-lower-bound.md).

Neither interface covers Euler's constant merely because it occurs with
logarithms in another construction.  In particular, neither replaces the
separate task of producing a gamma identity satisfying the theorem's exact
input conditions, and the Part II constants are not supplied as a numerical
certificate.  Clearing denominators changes the height and must be accounted
for before applying its integer-coefficient form.
