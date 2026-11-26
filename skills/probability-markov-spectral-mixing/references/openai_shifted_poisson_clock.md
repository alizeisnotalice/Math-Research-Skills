# Bounded-array shifted-Poisson clock transfer

## Admitted interface

Let \(q\in(0,1)\), let \(M_n\in\mathbb N\) with \(M_n\to\infty\), and let real arrays
\((a_{n,j})_{j\geq0}\) obey a common bound \(\lvert a_{n,j}\rvert\leq B<\infty\).
For every fixed real \(y\), set

\[
 N_{n,y}\sim\operatorname{Poisson}(qM_n+y\sqrt{M_n}),\qquad
 B_n\sim\operatorname{Binomial}(M_n,q).
\]

The Poisson mean need only be positive eventually.  If
\(\mathbb E a_{n,N_{n,y}}\to0\) for every fixed \(y\in\mathbb R\), then
\(\mathbb E a_{n,B_n}\to0\).  The conclusion is uniform for a family only when the
bound \(B\), the shifted-Poisson convergence (for every fixed shift), and
\(M_n\to\infty\) are all uniform over that family.

This is Lemma 2.3 (PDF p. 10; proof pp. 154--156) of OpenAI,
*Cutoff throughout the high-temperature Sherrington--Kirkpatrick phase*,
OpenAI Math Release preprint, 24 September 2026, pinned PDF SHA-256
`d99d391c8c3ed79f0dc70c9db4135300006e83dc4e09f9f3d7c5f71cda6230d5`.
Pinned official PDF:
`https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Cutoff-throughout-the-high-temperature-Sherrington-Kirkpatrick-phase-September-24-2026/paper.pdf`.
The original source attributes the clock comparison to Chen--Saloff-Coste,
but the bounded-array uniform formulation and its proof are present in this PDF.

## Transfer proof

For an integer-valued \(Z\), put its histogram density equal to
\(\sqrt M\,\Pr(Z=j)\) on
\([ (j-qM)/\sqrt M,(j+1-qM)/\sqrt M)\).  The source proves, for each fixed
\(y\), the whole-line \(L^1\) limits

\[
 p_{M,y}\longrightarrow\phi_q(\cdot-y),\qquad
 q_M\longrightarrow\phi_{q(1-q)}. \tag{1}
\]

Here \(p_{M,y}\) and \(q_M\) are respectively the shifted-Poisson and
binomial histograms.  Its proof uses successive probability ratios on
\(O(\sqrt M)\) central windows, normalization by Riemann sums, and Chebyshev
plus Gaussian tails for the complement.  Thus (1) is not an appeal to a
pointwise local CLT without tail control.

The key direction is that the narrower normal density is in the closed
\(L^1\) span of translates of the wider one:

\[
 \phi_{q(1-q)}\in\overline{\operatorname{span}}^{L^1}
 \{\phi_q(\cdot-y):y\in\mathbb R\}. \tag{2}
\]

Indeed finite-difference quotients put every derivative of \(\phi_q\) in
that closed span; its derivatives are polynomial multiples of \(\phi_q\).
Writing the ratio of the two normal densities as a constant times
\(e^{-cx^2}\), with \(c>0\), and using
\(e^{-cx^2}=\mathbb E\cos(Vx)\) for \(V\sim N(0,2c)\), first truncate the frequency to \(|V|\le R\), with error controlled by the omitted Gaussian mass. For fixed \(R\), expand the cosine in Taylor polynomials and use \(e^{R|x|}\phi_q(x)\) as an integrable dominant. This proves (2).  Consequently, for any \(\varepsilon>0\) one may choose
once and for all a finite signed sum
\(F=\sum_{\ell=1}^L c_\ell\phi_q(\cdot-y_\ell)\) with
\(\lVert\phi_{q(1-q)}-F\rVert_1<\varepsilon/(4B)\).

Extend the arrays by zero below zero and let \(U_n\) be their histogram-step
function.  Testing this *fixed* finite approximation gives

\[
 |\mathbb E a_{n,B_n}|
 \leq B\lVert q_{M_n}-\phi_{q(1-q)}\rVert_1
 +B\lVert\phi_{q(1-q)}-F\rVert_1
 +\sum_{\ell=1}^L |c_\ell|\bigl(
 |\mathbb E a_{n,N_{n,y_\ell}}|
 +B\lVert p_{M_n,y_\ell}-\phi_q(\cdot-y_\ell)\rVert_1\bigr).
\]

All terms vanish or are made small.  The finite choice before testing the
array is exactly why the stated uniform-family conclusion follows; it would
not follow from an array-dependent approximation.

## Correct use and boundary

Use this only after a continuous-time or Poisson-clock argument has supplied
the shifted averages for every fixed real shift.  It transfers those bounded
averages to the lazy/discrete binomial clock.  It supplies neither a
spectral-gap/mixing estimate nor the shifted-Poisson hypothesis, and it does
not cover unbounded observables, \(q=0,1\), a shift growing with \(n\), or a
family lacking the stated uniform controls.

As a direct diagnostic example, with \(q=1/3\), \(M=100\), and
\(a_j=(-1)^j\), the two averages are exactly
\(\exp(-2qM)=\exp(-200/3)\) at shift zero and
\((1-2q)^M=3^{-100}\) for the binomial clock.  This illustrates the two
clock formulas only; one finite calculation is not a proof of the limit
theorem.
