> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-031 — graphon spectra as bifurcation thresholds for Kuramoto graph limits

## Identity and reading evidence

- **Mother mirror status:** R02 final helper-stage passed; mother hash binding pending; no quota increment.
- **Read file:** `../pdfs/PGEL-031.pdf`
- **Exact local version:** arXiv:1805.03786v1; first-page stamp 10 May 2018 (the page body is dated 11 May 2018); 18 physical pages; SHA-256 `47db43994c0bb652c0eae136c3038d8d334c60a7926a790202c0c6a08cce0ee8`.
- **Metadata:** The local first page, D02 identity manifest, and official arXiv record agree on title, authors, and work. DOI 10.1063/1.5039609 is listed in D02 metadata. The body read here is the exact 18-page v1 arXiv PDF.
- **Reading status:** Complete physical PDF pp. 1–18, including all equations, examples, discussion, acknowledgments, and references. The graphon and spectrum formulas were checked against rendered pages 8, 11–13.

## Finite-graph model and limit model

The finite graph Kuramoto model in (2.1) is
\[
\dot u_{n,i}=\omega_i+\frac{K}{n\alpha_n}\sum_j a_{n,ij}\sin(u_{n,j}-u_{n,i}),\qquad i\in[n].
\]
The paper’s frequency variables are i.i.d. with a **smooth, even density** $g$. It treats deterministic weighted discretizations $H(n,W)$, dense random $W$-graphs, and sparse random $W$-graphs with $\alpha_n\downarrow0$ and $n\alpha_n\to\infty$. The random-graph examples are symmetric; the spectral bifurcation discussion explicitly uses a symmetric graphon $W$ so its integral operator is compact self-adjoint. The more general “weighted directed graph” notation in (2.1) does not make the self-adjoint spectral claims valid for an arbitrary directed graph.

The limiting object is a transport/continuity PDE for a conditional phase-frequency density $\rho(t,u,\omega,x)$ on the continuum location space $x\in[0,1]$ and phase circle. The paper says empirical measures converge weakly to this density when the initial empirical data converge weakly; that convergence result is **cited** to [4, Theorem 2.2] (and [8]), not proved in this 18-page paper. Therefore graphon-limit claims must not be turned into finite-$n$ uniform or high-probability statements without the separate graph-convergence theorem and its assumptions.

## Spectral thresholds and exact small-world spectrum

For a symmetric compact graphon operator $W$ with largest positive eigenvalue $\mu_{\max}$ and smallest eigenvalue $\mu_{\min}\le0$, the article quotes the linear stability result from [4]: the incoherent state is stable for
\[
K\in[K_c^-,K_c^+],\qquad K_c^- = \frac{2}{\pi g(0)\mu_{\min}},\quad K_c^+ = \frac{2}{\pi g(0)\mu_{\max}}.
\]
When $\mu_{\min}=0$, the paper separately states that the incoherent state is stable for $K\le K_c^+$; the displayed fraction for $K_c^-$ is not evaluated at zero. This threshold theorem is quoted background here; the paper uses it and computes spectra for selected graphons.

For the circular small-world graphon (physical pp. 11–13), with $r\in(0,1/2)$ and $p\in[0,1/2]$,
\[
W_{r,p}(x,y)=\begin{cases}1-p,&d_{\mathbb T}(x,y)\le r,\\p,&d_{\mathbb T}(x,y)>r,\end{cases}
\]
the convolution operator has Fourier eigenvectors $e^{2\pi ikx}$ and eigenvalues
\[
\mu_0=2r+p-4rp,\qquad
\mu_k=\frac{1-2p}{\pi k}\sin(2\pi kr),\quad k\ne0.
\]
Thus $\mu_0$ is the largest positive eigenvalue and the positive-coupling onset calculated in the paper is
\[
K_c^+ = \frac{2}{\pi g(0)(2r+p-4rp)}.
\]
This is an exact calculation for the continuum kernel. In the power-law graphon example $W_\gamma(x,y)=(xy)^{-\gamma}$, $0<\gamma<1/2$, the cited operator calculation gives $\mu_{\max}=(1-2\gamma)^{-1}$ and hence $K_c^+=2(1-2\gamma)/(\pi g(0))$; the sparse random graph sequence also has its separate $\beta$ and $n\alpha_n\to\infty$ constraints from §2.

## What this paper proves, quotes, and simulates

- Sections 2–3 set out the graph models and mean-field PDE. Weak empirical-measure convergence is invoked from prior work, not reproved.
- The stability interval and critical threshold formulas are imported from [4]. The article derives explicit Fourier eigenvalues for the small-world kernel, which makes that quoted threshold computable.
- The branch near $K_c^+$ and the negative-eigenvalue twisted branch near $K_c^-$ are attributed to center-manifold reduction in [5]. The article states the multiplicity assumption for $\mu_{\min}$ and displays the branch, but does not prove the center-manifold reduction itself.
- Section 4 is explicitly a numerical-results section. The ER, Paley, bipartite, stochastic-block, and power-law comparisons and all simulation plots are examples, not finite-$n$ probability theorems. For ER and Paley, both graph sequences have constant limiting graphon $W\equiv1/2$, so they share the **mean-field** threshold $4/(\pi g(0))$; this does not say the finite graphs are identical or that their finite-$n$ dynamics have the same sample paths.
- For small-world graphs, the continuum operator has negative eigenvalues and the paper discusses a branch of noisy twisted states for negative coupling. The plotted states, GPU performance and finite simulation conclusions are numerical. Do not report them as an all-initial-data attraction theorem.

## Scope boundary for energy-landscape use

This is useful as a graphon/Fourier-spectrum method and as a careful boundary between finite random graphs and their continuum limit. It does **not** prove that every local minimum or second-order stationary point of a finite graph energy is synchronized; it does not prove a high-probability statement for random signed graphs; and it does not apply the self-adjoint spectrum formulas to arbitrary directed/asymmetric weights. Any proposed interface to C118 must separately bridge sign randomness, finite-$n$ uniformity, and the energy-landscape quantifier.
