> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-004 — A global synchronization theorem for oscillators on a random graph

## Identity and reading record

- Martin Kassabov, Steven H. Strogatz, and Alex Townsend. Source read: arXiv:2203.03152v1 (submitted 7 March 2022), [official arXiv record](https://arxiv.org/abs/2203.03152); published DOI recorded by D02: [10.1063/5.0090443](https://doi.org/10.1063/5.0090443). The local source is the 9-page arXiv author-version PDF; journal-version equivalence was not checked.
- Local PDF: `../pdfs/PGEL-004.pdf`; SHA-256 `115182e6aeb65b31726d8e4ebdc409133ce14b79537ca72fe18a91d7fccb36b2`.
- Strict PDF parse, page count, and hash checked. Read all 9 physical pages in order, including references. Rendered PDF pp. 7–8 to check Theorem 11 and the finite-size inequalities. For this correction, also rendered and inspected pp. 2, 5, and 8: Eq. (2), Lemma 4’s edge-cut deviation, and §VI/§VII finite bounds and Table I. Coverage is in `../../reading_coverage.json`.
- Review pending.

## Model and quantifiers

The homogeneous Kuramoto equation is \(\dot\theta_j=\sum_k A_{jk}\sin(\theta_k-\theta_j)\), with symmetric, nonnegative, unit-strength undirected edges. For \(G(n,p)\), the authors use the unusual convention that diagonal entries are independent Bernoulli-\(p\) self-loops; the loops do not change the dynamics because \(\sin(\theta_j-\theta_j)=0\), but they affect degree/matrix conventions. For a fixed graph, global synchronization means convergence to full synchrony for almost every initial phase. The graph-whp and initial-state-a.e. probability layers must remain separate.

## Deterministic spectral criterion

For a graph of size \(n\), the paper allows a parameter \(0<p<1\). It defines
\[
\Delta_A=A-pJ_n,
\]
where \(L=D-A\) is the positive graph Laplacian. The source has a sign-convention inconsistency in (2), PDF p. 2: it prints \(\Delta_L^{\rm print}=L-pJ_n+npI_n\) and states \(\mathbb E L=pJ_n-npI_n\), even though its stated \(L=D-A\) and self-loop model give \(\mathbb E L=npI_n-pJ_n\). We use the consistently centered positive-Laplacian matrix
\[
\Delta_L^\circ=L-npI_n+pJ_n=L-\mathbb E L.
\]
This equals the negative of the centered matrix formed with the opposite convention \(A-D\), so its spectral norm is unchanged under a consistent sign convention. The displayed edge-cut deviation in Lemma 4 (PDF p. 5), centered at (p|C_1||C_2|), aligns with this corrected center; its adjacent printed quadratic-form evaluation also carries the opposite sign. The literal printed shift is \(\Delta_L^\circ+2(npI_n-pJ_n)\); on \(\mathbf1^\perp\), its quadratic form is \(x^TLx+np\|x\|^2\), so its norm is at least \(np\) for \(n\ge2\). Thus the printed shift cannot be the small centered norm in Theorem 11. This records a source notation defect; it is not a claim that the synchronization result is false. In the \(G(n,p)\) application, \(p\) is the edge probability. The criterion is intended as a deterministic sufficient condition.

**Theorem 11 (PDF p. 7; sign-consistent reading).** With \(\Delta_L^\circ\) above, if
\[
\frac{\|\Delta_A\|}{np}<\frac1{12},\qquad
\frac{\|\Delta_L^\circ\|}{np}<\frac14,
\]
and
\[
\frac{\pi/4}{\sin^{-1}\!\left(12\|\Delta_A\|/(np)\right)}
>
\frac{\log(n/6)}{\log\!\left(np/(2\|\Delta_L^\circ\|)-1\right)}+1,
\]
then the only stable equilibrium is the all-in-phase state. The theorem is a sufficient condition, not a threshold characterization.

The proof first uses stability and the first two order parameters to lower-bound \(\rho_1\), then bounds the number of phases outside an arc. Lemma 7 gives a stable-state kernel inequality; Lemma 8 converts it to an edge-count comparison between nested arc-defined vertex sets. Corollary 9 and Lemma 10 amplify the shrinking outlier-set bound until no phase remains outside the half-circle. Theorem 11 combines these estimates. The gradient-flow/measure-zero-saddle discussion in the introduction explains the passage from stable-equilibrium exclusion to the a.e.-initial-condition global property; the theorem is not an assertion that every critical point is synchronous.

## Random-graph consequences and numerical boundary

Section VI gives the explicit norm bound (read for \(\Delta_L^\circ\) under the consistent centering above)
\[
f(n,p)=2\sqrt{n\log n\,p(1-p)}+\frac{4\log n}{3},
\]
with \(\Pr\{\|\Delta_A\|\ge f(n,p)}<2/n\) and \(\Pr\{\|\Delta_L^\circ\|\ge2f(n,p)}<2/n\). Substituting these into the sign-consistent reading of Theorem 11 gives the displayed finite-parameter example: at \(n=10^6\), \(p>0.256\) suffices with probability \(>0.999996\). The authors then invoke stronger asymptotic spectral-norm estimates to obtain \(p\gg(\log n)^2/n\) as a sufficient condition whp. This is an improvement over the prior \(p\gg(\log n)/n^{1/3}\) result, not the conjectured connectivity-scale threshold.

The finite-n example, equation (12), the iterative procedure, and Table I are on physical PDF p. 8. The table reports better finite-\(n\) values (including \(p>0.01117\) for \(n=10^6\)) from iterating the paper’s inequalities over many angle values; the authors state the program can be turned into a proof but do not write out that iteration as a short closed-form argument. The same discussion says \(p\gg\log n/n\) is supported by computation but remains an unproved conjectural scale. A local check of the displayed Theorem 11 inequalities using the consistently centered \(\Delta_L^\circ\) at \(n=10^6,p=0.256\), including the probability lower bound, is saved in ../math/pgel_batch2_checks.py and its JSON output; it checks this example only.

This is a positive, symmetric graph theorem. It is not evidence for a signed model or an oriented system, and its graph threshold should not be confused with an all-critical-points landscape classification.
