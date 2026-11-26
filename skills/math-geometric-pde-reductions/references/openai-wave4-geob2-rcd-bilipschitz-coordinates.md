# Cumulative Bochner-mass normalization for RCD coordinates

Source: *Bi-Lipschitz Coordinates at Regular Points of Noncollapsed RCD
Spaces*, OpenAI (25 September 2026), SHA-256
`5500abd2391d238779793572caf1df5270a1ac488f6d88cc897d5cf51ac33093`,
[official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Bi-Lipschitz-Coordinates-at-Regular-Points-of-Noncollapsed-RCD-Spaces-September-25-2026/paper.pdf).

## Scoped interface

Use only at a regular point of a noncollapsed RCD space along the source's
late rescalings, harmonic columns, local volume comparison, and rescaled
curvature regime.  Regularity by itself does not give the summability needed
here.

For a harmonic column `u=(u_1,...,u_n)^T`, set

\[
 G=(\Gamma(u_j,u_k))_{j,k},\qquad M=(M(u_j,u_k))_{j,k}; \tag{2.4}
\]

then positivity gives, for Borel `E`,

\[
 |M(v,w)|(E)\le\sqrt{M[v](E)M[w](E)}. \tag{2.5}
\]

At dyadic scales `r_i=2^{-i}`, form the mean Gram matrices `R_i(y)` and the
heat-normalized quantities of Section 3.  The source's weighted accumulation
lemma writes `B_i=H_{i+1}-H_i`, `Delta_i=Q_i-Q_{i+1}`, `a_i=H_i xi` and proves

\[
 H_i\Delta_iH_i\le B_i\le(1+C\epsilon_\nu)H_i\Delta_iH_i,\quad
 \sum_{i<k}F_i[a_i]\le CH_k[\xi],\quad
 C^{-1}H_k\le I+\sum_{i<k}H_iN_iH_i\le CH_k. \tag{3.25--3.27}
\]

These are quadratic-form inequalities on the fixed finite-dimensional
coordinate space; do not commute the matrices.

## Coordinate construction

1. Use Bochner mass forms and the source's heat comparison to prescribe
   affine stretches at all dyadic scales.
2. Control changes of mean normalization via the cumulative matrices, retaining
   the directional defects and their summability.
3. Pass to `F=lim_i h_i circ u` only after the source's uniform bounds.  The
   endpoint metric conclusion is
   `1/(4 sqrt A) d(x,z) <= |F(x)-F(z)| <= 4 sqrt A d(x,z)` on `B_rho(p)`
   (physical p. 41), followed by invariance of domain for openness.

## Record boundary

This is not a generic construction on an RCD space and does not promote an
ordinary dyadic Gromov--Hausdorff approximation to a bi-Lipschitz chart
without the paper's summable directional-defect input.

Locators: physical pp. 3--6, 10--18, and 41; (2.4)--(2.5),
(3.25)--(3.27), and (5.42).
