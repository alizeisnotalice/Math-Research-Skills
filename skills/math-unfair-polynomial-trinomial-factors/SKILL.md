---
name: math-unfair-polynomial-trinomial-factors
description: Apply the trinomial case of the unfair 0–1 polynomial theorem after checking its normalized finite-support and nonnegative-coefficient hypotheses.
---

# Unfair 0–1 polynomials with a trinomial factor

Use this route for a factorization
\[
 C(X)=(1+aX^r+X^m)B(X)
\]
where `C` is a polynomial with coefficients in \(\{0,1\}\), both factors are monic with nonnegative real coefficients, \(B\) has finite support, and \(0<r<m\). The source's theorem gives that the normalized middle coefficient is \(a=1\), hence both factors have binary coefficients.

Before using it, retain the normalization map from the supplied trinomial to this form. Check finite support, monicity, nonnegative coefficients and every coefficient of `C` exactly. The result is only the trinomial-factor case. It does not cover factors with four or more terms.

The proof route combines a finite coefficient-array recurrence with a conjugate-growth argument and the appendix's summable Fourier kernel. Its proof uses the stated algebraic-integrality consequence of a binary product. Read [the source scope and proof boundary](references/baravelli-trinomial-source.md) when applying the theorem.
