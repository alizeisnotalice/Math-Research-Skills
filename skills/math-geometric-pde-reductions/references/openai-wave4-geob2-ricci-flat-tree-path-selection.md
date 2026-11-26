# Exponentially weighted path selection on Ricci-flat trees

Source: *Path selection and an elliptic inequality on degenerating Ricci-flat
trees*, OpenAI (24 September 2026), SHA-256
`a49f3dc92b22b888e356c7d8e02620683b9e1c00ca1b28212cf800dd4d692327`,
[official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Path-selection-and-an-elliptic-inequality-on-degenerating-Ricci-flat-trees-September-24-2026/paper.pdf).

## Scoped geometric interface

Use this only for a fixed finite rooted tree of four-dimensional Ricci-flat
vertex models with the paper's order-20 end bounds.  For an edge from parent
`p` to child `c`, the gluing scale is

\[
 x_p=e^{-2L_e}x_c,\qquad a_c=a_pe^{-2L_e},\qquad a_{root}=1. \tag{2.2}
\]

Assume every `L_e -> infinity`, compact vertex convergence, and the stated
weighted Ricci estimate through order ten.  Define the mass-subtracted
functional

\[
 E(g)=\lim_{D\to\infty}\left\{\int_{r<D}R(g)\,d\mu_g-
 \int_{r=D}(\partial_jg_{ij}-\partial_ig_{jj})n_i\,dS_\delta\right\}. \tag{2.4}
\]

The source records the first variation

\[
 DE_g(\dot g)=\int\langle\tfrac12R(g)g-\operatorname{Ric}(g),\dot g\rangle_g\,d\mu_g. \tag{2.5}
\]

Under those inputs it first gets `|E(g)|<=CM`, then its fixed-tree statement
is `E(g_j)=o(M_j)` (Theorem 2.2).  The little-oh is explicitly not uniform
over changing trees.

## Analytic path-selection subroutine

For each length variable, an admissible family has a locally finite expansion

\[
 P(L,z)\sim\sum_{d\in D_i}e^{-dL_i}\sum_{k=0}^{k_d}L_i^kP_{dk}(\widehat L_i,z), \tag{3.1}
\]

with the common-tail holomorphy and grouped-weight requirements of Definition
3.1 (physical pp. 7--8).  Theorem 3.2 converts a finite Boolean combination
of signs/equalities holding along `L_i^(n)->infinity`, `z^(n)->z_0` into a
real-analytic tail path whose actual coordinates are eventually monotone or
constant.

To use Corollary 3.3, establish the source's differential estimate

\[
 |dF|\le C\sqrt J\left(\sum_a|dz_a|+\sum_i e^{-cL_i}|dL_i|\right).
\]

Along the selected path, each ordinary coordinate has finite variation and
`integral e^{-cL_i}|L'_i|=c^{-1}e^{-cL_i(u_0)}`.  Hence the assumption
`F!=0`, `F^2>=c_0J`, `F->0` contradicts finite total variation of
`log|F|` (physical pp. 8--9).

Locators: physical pp. 5--9; (2.2), (2.4)--(2.6), Definition 3.1,
Theorem 3.2, and Corollary 3.3.
