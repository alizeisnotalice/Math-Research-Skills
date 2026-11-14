> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-012 — Phase Synchronization in Random Geometric Graphs on the 2D Sphere

## Identity and reading record
Cecilia De Vita, Pablo Groisman, and Ruojun Huang, “Phase Synchronization in Random Geometric Graphs on the 2D Sphere,” arXiv:2504.01151v2 (1 October 2025); [official arXiv record](https://arxiv.org/abs/2504.01151). R05 verified source identity; metadata is not independently verified. The D02 sourcepool/local first page give the same title, authors, and v2. The exact 18-physical-page author-version PDF has SHA-256 `c9e66d032a0100724fef45d3fb174ae7fa49a0ff99bbc57b06777bb8efd5c887`. Reader L03 read all 18 pages in order, including the Appendix, acknowledgments, and references. No accepted canonical full-read match was found by exact title or PDF hash. R05 L03_B4 helper-stage review passed; mother-card hash binding is pending.
## Model and main result

For each (n), the vertices (x_1,\ldots,x_n\) are i.i.d. uniform on the unit sphere (S^2\subset\mathbb R^3\). For a bandwidth parameter \(\epsilon=\epsilon(n)>0\), connect (i,j\) when \(\|x_i-x_j\|^2<\epsilon\), and weight the edge by \(K(\|x_i-x_j\|^2/\epsilon)\). The kernel is bounded, supported in \([0,1]\), positive on \([0,1)\), and is assumed either to have bounded derivatives or to be the indicator \(1_{[0,1]}\). With \(N_i\) the unweighted neighbor count and \(c_2\) the source’s geometric/kernel constant, the ODE (2.1), physical p. 4, is

\[
\dot u_n(t,x_i)=\frac1{\epsilon\,\mathbb E N_i}\sum_{j\ne i}\sin(u_n(t,x_j)-u_n(t,x_i))K(\|x_i-x_j\|^2/\epsilon).
\]

Equation (2.2), physical p. 5, prints \(\mathbb E N_i=c_2\epsilon n/(4\pi)\). Here \(\sigma\) is unnormalized surface area (total mass \(4\pi\)), sampling is uniform probability \(\sigma/(4\pi)\), and \(N_i\) counts the other vertices in the unweighted neighborhood. For \(K=1_{[0,1]}\), the cap-area coefficient is \(c_2=\pi\), so Eq. (2.2) prints \(n\epsilon/4\); the exact mean over the \(n-1\) other points is \((n-1)\epsilon/4\). This finite-size difference \(\epsilon/4\) is asymptotically negligible, but the two expressions are not exactly equal. The separate p. 3 statement about the probability \(p\) is discussed under source issues below. The scaling regime is

\[
\epsilon\to0,\qquad \liminf_{n\to\infty}\frac{\epsilon^2n}{\log n}=\infty. \tag{1.3}
\]

Theorem 2.1 (physical p. 7) fixes \(T>0\), takes \(u_0\in C^{2,\alpha}(S^2)\), \(0<\alpha<1\), and assumes for every \(\delta>0\)

\[
\sum_{n=1}^{\infty}\mathbb P\!\left(\sup_{1\le i\le n}|u^n_0(x_i)-u_0(x_i)|>\delta\right)<\infty. \tag{2.7}
\]

Theorem 2.1 states that the graph ODE solution converges almost surely, uniformly over vertices and \(t\in[0,T]\), to the solution of \(\partial_tu=\kappa\Delta_{S^2}u\), where the paper prints

\[
\kappa=\frac14\int_{\mathbb R^2}\|z\|^2K(\|z\|^2)\,dz. \tag{2.6}
\]

The coefficient above is **source-reported, not independently validated**: the displayed Eq. (2.6) coefficient does not match the operator normalization in Eqs. (2.1), (2.2), (2.8), and Lemma 3.7 under the source's unit-sphere convention. In particular, the exact permitted-indicator test recorded below gives a nonvanishing discrepancy. Therefore the precise heat-equation target and the quantitative Theorem 2.1/Lemma 3.7 interface remain pending normalization reconciliation; do not silently replace the printed coefficient. Theorem 2.4 (physical pp. 7, 14) states eventual synchronization almost surely for the specified sequence of initial data. It is **not** a no-spurious-local-minima or all-initial-data landscape theorem: the authors explicitly say on physical p. 15 that it gives no such conclusion for nonsmooth limiting data or i.i.d. random phases. The normalization finding does not by itself establish that this qualitative Theorem 2.4 is false, but its printed proof's finite-time convergence step depends on the exact heat clock and needs reconciliation before the quantitative argument is reused. No complete corrected proof is claimed here.

## Proof chain and exact dependencies

The source's Theorem 2.1 proof compares (i) the finite random graph system, (ii) a nonlinear integral equation on (S^2), and (iii) the heat equation. Proposition 2.2 bounds the nonlinear integral-equation error by \(C\epsilon^{\alpha/2}\); Proposition 2.3 gives almost-sure graph-to-integral convergence under (1.3) and (2.7). The proof uses concentration of neighbor counts and comparison principles. Proposition 3.1 (physical p. 8) lifts continuous (S^1)-valued functions on simply connected (S^2) to continuous real-valued functions, allowing the order comparison argument. Proposition 3.6 gives a uniform Lipschitz bound; Lemma 3.7 claims the nonlocal graph operator approximates \(\kappa\Delta_{S^2}\), and the error is absorbed by a spatially constant barrier. Treat the exact coefficient/interface in this last step as unresolved in light of the explicit test below; no repaired version of the proposition is inferred.

For Theorem 2.4, the heat flow converges uniformly to its spatial mean. Choose a finite (T) when the heat profile lies within \(\pi/8\) of that mean; Theorem 2.1 puts all graph phases within \(\pi/4\) of the mean for large (n\), so every pairwise difference is less than \(\pi/2\). In regime (1.3), the paper cites \(\mathbb P(G_n\text{ disconnected})\le e^{-\sqrt n}\) for large (n\); on a connected graph this phase-cohesive set lies in the basin of the synchronized state. The failure probabilities are summable, and Borel–Cantelli yields eventual synchronization almost surely. These are finite-time convergence and connectedness inputs; no claim is made about arbitrary initial conditions.

The Appendix (physical pp. 15–16) separately handles the discontinuous indicator kernel by deriving the needed contraction estimate for neighborhoods \(B_{\sqrt\epsilon}(x)\cap S^2\). It asserts the earlier theorems then hold for equal edge weights, so the indicator kernel used in the check below is within the source's stated scope. References occupy physical pp. 16–18.

## Source issues and scope boundaries

1. **Physical p. 3: cap area versus probability.** The page says “in this case, \(p=\pi\epsilon\)” while describing \(p\) as the probability that two independent uniform points on \(S^2\) are within chord distance \(\sqrt\epsilon\). The unnormalized cap area is \(\pi\epsilon\); dividing by \(4\pi\) gives probability \(\epsilon/4\). Preserve this as a local printed normalization defect.
2. **Physical p. 5: finite-size expected-degree distinction.** Equation (2.2) prints \(c_2\epsilon n/(4\pi)\); with indicator kernel \(c_2=\pi\), this is \(n\epsilon/4\). Since \(N_i\) excludes \(i\), the exact conditional mean is \((n-1)\epsilon/4\). The difference \(\epsilon/4\) is asymptotically negligible, but it is not exact equality.
3. **Physical pp. 6–7 and 14: unresolved operator normalization.** The paper defines \(\sigma\) as surface area, samples from \(\sigma/(4\pi)\), uses unweighted \(N_i\), allows \(K=1_{[0,1]}\), prints \(\kappa=\frac14\int_{\mathbb R^2}\|z\|^2K(\|z\|^2)\,dz=\pi/8\) for that kernel (Eq. 2.6, p. 6), and divides the nonlocal integral by \(c_2\epsilon^2=\pi\epsilon^2\) in Eq. (2.8), p. 7. For \(x=(0,0,1)\), \(v(y)=y_3\), the exact cap integral is \(-\pi\epsilon^2/4\); the Eq. (2.8) operator is therefore \(-1/4\), while the standard unit-sphere \(\Delta v(x)=-2\) gives printed \(\kappa\Delta v=-\pi/4\). The residual is \((\pi-1)/4\) in absolute value and does not tend to zero. This conflicts with the vanishing-error approximation claimed in Lemma 3.7 (p. 14) for an allowed smooth test and kernel. An independent neutral assessment (`../../audit/review-index.json` and `.json`) corroborates this exact test under the standard geometric Laplacian convention. The value \(1/8\), obtained by matching this one test (equivalently dividing printed \(\kappa\) by \(c_2\)), is only a candidate for this test, not a source correction or a generally proved replacement coefficient. Keep the printed coefficient source-reported and isolate exact diffusivity / Theorem 2.1 / Lemma 3.7 reuse pending reconciliation; do not declare Theorem 2.4 false or claim a complete general repair.
4. **Terminology versus theorem scope.** Physical p. 2 says the authors use “spontaneous synchronization,” “global synchronization,” and “benign landscape” interchangeably for a unique-global-minimum property. The actual Theorem 2.4 is conditioned on one sequence of initial data; physical p. 15 explicitly disclaims the general global-synchronization conclusion. Do not cite it as exclusion of every nonsynchronous local minimum.
5. The graph has symmetric nonnegative weights and a gradient-flow potential. The low-dimensional result relies on \(S^2\)'s simply connected topology and smooth limiting initial data. It does not transfer directly to signed coupling, nonpotential orientation, arbitrary initial phases, or an energy-landscape theorem.

## Actual mathematical check

`../math/pgel_012_normalization_check.py` was run with the project’s local SymPy runtime; the saved output is `../math/pgel_012_normalization_check.json`. It gives cap area \(\pi\epsilon\), normalized edge probability \(\epsilon/4\), exact mean degree \((n-1)\epsilon/4\), and the source-reported Eq. (2.6) value \(\pi/8\) for \(K=1_{[0,1]}\). On the north-pole coordinate test, the source Eq. (2.8) operator equals \(-1/4\), while printed \(\kappa\Delta v=-\pi/4\); the exact residual is \((\pi-1)/4\). The same check gives the nonlinear sine-operator value \(2(\cos(\epsilon/2)-1)/\epsilon^2\to-1/4\), as an independent check of the local limit, not a full nonlinear theorem. The single-test matching coefficient is \(1/8\), explicitly not a general repair. The same script checks the PGEL-009 sparse Fourier formula for \(n=8,16\) and the \(n=2\) boundary case. These exact calculations diagnose the printed interface; they do not prove a corrected scaling theorem.

Complete physical-page and section coverage is recorded in `../../reading_coverage.json` (mother source entry PGEL-012; rendered images remain in `../renders/PGEL-012/`).
