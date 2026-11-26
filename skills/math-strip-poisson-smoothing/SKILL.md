---
name: math-strip-poisson-smoothing
description: Transfer a symmetric complex-center profile in a fixed strip to complete monotonicity using hyperbolic-secant Poisson smoothing.
---

# Strip Poisson smoothing

For symmetric centers whose imaginary displacements satisfy \(|d|<a\), use
\[
 K_a(z)=\frac1{2a}\operatorname{sech}\!\left(\frac{\pi z}{2a}\right).
\]
Its shifted real part is positive,
\[
 \Re K_a(x+id)=\frac{\cosh(\pi x/(2a))\cos(\pi d/(2a))}
 {2a(\sinh^2(\pi x/(2a))+\cos^2(\pi d/(2a)))}.
\]
When the caller supplies the needed locally uniform convergence and symmetric-pair summability, pairwise positivity gives a nonnegative profile. The Laplace substitution then yields complete monotonicity for the associated heat sum and its divided-by-time form.

This does not supply a verified list of zeta zeros, a narrower prime-based certificate, or a Riemann-hypothesis conclusion. Read [the exact scope](references/strip-poisson-smoothing.md) before applying it to an infinite source family.
