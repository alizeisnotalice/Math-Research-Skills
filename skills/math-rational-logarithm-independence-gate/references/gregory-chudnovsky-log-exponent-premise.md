# Rational-ratio premise in `EXT-0378`

## Source status and exact use

`EXT-0378`, *Irrationality exponents of logarithmic numbers: Values,
quotients, and graded approximation* (Gregory V. Chudnovsky, 16 October
2026; arXiv:2610.28079v1), is a 110-page preprint.  Its scope table on
physical pages 4--6 states the individual-logarithm and rational-logarithm
ratio results.  Physical page 12 gives the elementary implication used for a
rational ratio: if positive rationals \(a,b\) are multiplicatively
independent, then \(\log a/\log b\) cannot be rational, since a rational
ratio would yield \(a^q=b^p\).  The rational-ratio exponent claim is developed
in the theorem section on pages 36--45.

The paper's appendix (physical pages 90--108) labels some endpoints as Lean
artifacts and other ingredients as cited classical interfaces.  Its ancillary
reproduction record is publicly supplied at
<https://arxiv.org/src/2610.28079v1/anc/REPRODUCTION.txt>.  That record pins a
Lean/Mathlib snapshot and reports author-side builds/audits; it is evidence
about the supplied artifact, not an independent local kernel replay.

## Admitted finite interface

For a finite list of supplied positive rationals, this skill independently
checks the exact hypothesis

\[
  \nexists h\in\mathbb Z^n\setminus\{0\}:\quad
  \prod_{j=1}^{n} a_j^{h_j}=1.
\]

Unique prime factorization proves that this is equivalent to full column rank
over \(\mathbb Q\) of the prime-valuation matrix.  The checker reports that
matrix and its exact rank.

This interface may screen the multiplicative-independence premise of a
rational-logarithm-ratio application.  It neither verifies the source's
irrationality-exponent estimates nor validates the ancillary Lean build,
classical rank inputs, or the source's logarithm conventions.
