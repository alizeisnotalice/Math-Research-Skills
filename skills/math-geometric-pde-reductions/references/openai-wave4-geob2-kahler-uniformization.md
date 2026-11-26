# Triangular logarithmic-Jacobian correction for a Kähler chart

Source: *Uniformization of complete Kähler manifolds with positive bisectional
curvature*, OpenAI (23 September 2026), SHA-256
`2960f958368ee0ab8b9b2dd15b236d634b64595f29812035e12e2c705b207cdb`,
[official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Uniformization-of-complete-Kahler-manifolds-with-positive-bisectional-curvature-September-23-2026/paper.pdf).

## Scoped interface

This is a source-bound chart-normalization step, not a general Kähler
uniformization routine.  Use it only after the paper's preceding grid,
transition, and polynomial-degree hypotheses have supplied a truncated
logarithmic Jacobian `ell_k` with no constant term and degree at most `d`.

On physical p. 63, the transition identity is

\[
 \ell_k=J^{d-1}(P_k+\ell_{k+1}\circ F_k). \tag{8.9}
\]

With `E_k=J^{d-1}\exp(ell_k)`, form the triangular polynomial change

\[
 A_k(z)=\left(z_1,\ldots,z_{n-1},
 \int_0^{z_n}E_k(z_1,\ldots,z_{n-1},\zeta)\,d\zeta\right).
\]

The source records that it is tangent to the identity, has degree at most
`d`, and satisfies `J^{d-1} log det A'_k=ell_k`.  Retain the source's
coefficient and inverse-jet bounds: they use telescoping step lengths only in
the stated short regime and summability of the displayed exponential beyond
it.  Do not infer them from formal truncation alone.

## Noncommuting-rate branch

For an interval of logarithmic time length `T`, choose the endpoint singular
value coordinates so that

\[
 D=\operatorname{diag}(e^{-\mu_1T/2},\ldots,e^{-\mu_nT/2}),\quad
 0\leq\mu_1\leq\cdots\leq\mu_n,\quad
 \sum_i\mu_i=\Delta_sT. \tag{8.11}
\]

The source explicitly treats this as an **order statement for rate forms**,
not merely a statement about ordered eigenvalues; volume corrections do not
alter these linear parts.  On the regular macro intervals it derives the
two-sided rate window (physical p. 65)

\[
 b_0Q_j-N\leq\mu_i\leq Q_{j+1},\qquad
 bQ_j\leq\mu_i\leq b^{-1}Q_j, \tag{8.15}
\]

after the stated parameter choices.  The bounded increasing multipliers have
`lambda_{j+1}/lambda_j=1+K_0/j^2`; boundedness relies on
`sum j^{-2}<infinity`.

## Record boundary

The source-level input is positive bisectional curvature together with the
earlier chart construction; pp. 63--65 alone do not establish those global
inputs.  This reference therefore transfers neither a complete
uniformization theorem nor a commuting-matrix argument.

Locators: physical pp. 63--65, especially (8.9), (8.11), and (8.15).
