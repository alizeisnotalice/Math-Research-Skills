# OpenAI: `L log L` Fourier-layer assembly

**Source.** *Almost-everywhere Fourier convergence in L log L*, SHA-256
`9a77d41e5b9b9bebd18d958c58bbbd02facb910ede62e549b8887c877b3d6492`;
physical pp. 64--68, 74--75.

**Input/model.** On the unit circle with normalized measure, let `S_N` be
ordinary symmetric Fourier partial sums and let `f` be complex-valued in
`L log L`.  Split it into a bounded part and disjoint height layers

\[
 f=f_{bd}+\sum_{j\ge1}f_j,\quad
 f_{bd}=f1_{|f|<e^2},\quad f_j=f1_{e^{2j}\le|f|<e^{2j+1}}.
\]

For each real/imaginary signed nonnegative component `q_j`, put
`m_j=integral q_j`, discard zero masses, set `rho_j=q_j/m_j`, and use
`d_j=2j+1+log(1/m_j)`.

**Steps.** The source's dyadic procedure supplies a good set `G_j` for each
normalized bounded density, with a summable exceptional-set bound, and a
maximal integral controlled by `m_j d_j`.  The layer calculation records
`sum_j m_j d_j<infinity`: the term `2j m_j` is paid by
`integral |f|log|f|`; when `m_j>=e^{-2j}`, use
`m_j log(1/m_j)<=2j m_j`, and otherwise use
`m_j log(1/m_j)<=2j e^{-2j}`.  Borel--Cantelli makes all but finitely many
good sets available, Tonelli makes the tail maxima summable a.e., and finite
layer limits plus the uniform-in-`N` tail recover `S_N f→f` a.e.

The same source applies the translation-invariant Banach-space maximal
principle to `Phi(t)=t log(2+t)` and the sequence
`S_0,-S_0,S_1,-S_1,...`, obtaining

\[
 \sup_{\lambda>0}\lambda\,\mu\{\sup_N|S_Nf|>\lambda\}
 \le C\|f\|_{L\log L}.
\]

**Output/boundary.** Scoped reference. The assembly needs the source's
bounded-density good-set/maximal estimates (Theorems 10.1 and Proposition
10.2) and the cited maximal principle; the finite ordered-orthogonal
Rademacher--Menshov estimate alone does not supply them.  Do not apply this
to arbitrary partial-sum systems, non-symmetric Fourier truncations, or a
different endpoint space without corresponding hypotheses.

## 固定来源

- 物理页 64, 65, 66, 67, 68, 74, 75。Sections 9--10; Theorem 1.1; Corollary 10.3 SHA-256 `9a77d41e5b9b9bebd18d958c58bbbd02facb910ede62e549b8887c877b3d6492`。[Almost-everywhere Fourier convergence in L log L](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf)
