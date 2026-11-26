---
name: math-hypergeometric-padic-prime-density
description: Compute the eventual congruence classes and Dirichlet density of p-adically bounded primes for a supplied rational regular-singular hypergeometric series nF_{n-1}.
---

# Rational hypergeometric p-adic prime density

Use this skill only for a series \( {}_nF_{n-1}(\alpha;\beta;z)\) whose parameters
are rational, normalized into \((0,1)\), with no numerator parameter equal to a
denominator parameter. It computes the finite numerator-majorization test behind the
eventual classification of primes outside an explicit finite exceptional set.

Run [the exact class calculator](scripts/rational_density.py) with JSON input. Its
output is the modulus \(N\), the accepted unit classes, and \(|B|/\varphi(N)\). The
script proves only the finite residue-class computation. To use the theorem, separately
record the given hypergeometric parameters, the normalization, and the finite-prime
cutoff; it does not test coefficients for all primes.

Do not use this for quadratic-irrational parameters: the source's exact quadratic
density formula depends on its stated p-adic digit conjecture. For \(m\ne n+1\), the
specialized residue-class calculator is deliberately inapplicable; use the separate
valuation regime instead.

Read [source scope and theorem gate](references/ext0298-rational-parameter-density.md)
for the carry criterion, parameter hypotheses and conditional quadratic boundary.
