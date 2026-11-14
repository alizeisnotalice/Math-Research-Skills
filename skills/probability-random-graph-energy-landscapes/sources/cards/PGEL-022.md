> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-022 — Completely Degenerate Equilibria of the Kuramoto Model on Networks

**Reader:** L09, W24 helper batch L09_B8; R08 helper-stage passed; mother hash binding pending.  
**Source version:** Davide Sclosa, arXiv:2112.12034v3 (8-page author-version PDF); published as *Nonlinearity* 37(9) (2024), 095021, DOI 10.1088/1361-6544/ad694a. The card’s theorem/page locators refer to the exact local arXiv v3 PDF, SHA-256 `a7fb5e229de6022d183afd5cbba3ed139a2be636015fbe2d25c63c6304538a65`.

## Model and scope

The paper studies the undirected Kuramoto network

\[
\dot\theta_k=\omega_k+K\sum_j a_{jk}\sin(\theta_j-\theta_k),\qquad \theta\in\mathbb T^N,
\]

with symmetric adjacency, and in its initial setup positive coupling strength. A **completely degenerate** equilibrium means that the whole Jacobian matrix is zero entry-by-entry, not merely that it has a zero eigenvalue or a semidefinite spectrum. The main stability conclusions are for this special degeneracy class.

For zero natural frequencies and a connected graph, Lemma 1 (physical p. 2; proof p. 3) says this is equivalent to every vertex having exactly half its neighbors at phase \(\theta_k+\pi/2\) and half at \(\theta_k-\pi/2\). In particular every degree is even. The proof uses the equilibrium condition \(\sum_j a_{jk}\sin(\theta_j-\theta_k)=0\) and the vanishing edge derivative \(\cos(\theta_j-\theta_k)=0\).

## Exact structural and stability statements

* **Theorem 2 (physical p. 3):** A connected graph admits a completely degenerate equilibrium at zero intrinsic frequencies iff it has an Euler circuit such that the number of steps between any two visits to the same vertex is divisible by 4. Given such a circuit, choose one phase freely and increase the phase by \(\pi/2\) at each step; this constructs the equilibrium. The converse decomposes the edges into edge-disjoint circuits with the phase-increment property and splices intersecting circuits until a circuit uses every edge.
* **Examples and rarity (physical pp. 3–4):** Proposition 5 constructs examples for every vertex count \(N\ge6\). Proposition 6 bounds the probability that a uniformly random labeled graph admits such an equilibrium by \((7/8)^{\lfloor N/3\rfloor}\), hence this special property is asymptotically rare. This is a graph-existence statement about complete degeneracy, not a general random-graph stability theorem.
* **Theorem 8 (physical p. 5, zero frequencies):** For every connected graph with at least one edge, every completely degenerate equilibrium is an energy saddle and therefore not Lyapunov stable. With \(E(\theta)=\sum_{\{p,q\}\in E(G)}(1-\cos(\theta_p-\theta_q))\), select consecutive vertices \(j,k\) on the Euler circuit and perturb \(\theta_j\mapsto\theta_j+x\), \(\theta_k\mapsto\theta_k-x\). The circuit cancellations leave the exact difference
  \[
  E(\theta)-E(\theta^x)=\sin(2x)-2\sin x=-x^3+\tfrac14x^5+O(x^7),
  \]
  which changes sign in every neighborhood of zero. The paper invokes the analytic-gradient result that Lyapunov-stable equilibria are exactly local minima for this gradient system; the saddle is thus unstable. The nonzero cubic term explains why a zero Hessian/linearization cannot decide the stability here.
* **Nonzero frequencies and Theorem 11 (physical pp. 5–7):** At a completely degenerate equilibrium, equations (8)–(9) require \(\sum_j a_{jk}\sin(\theta_j-\theta_k)=-\omega_k/K\) and every incident cosine to vanish. Proposition 9 concludes \(\omega_k/K\in\mathbb Z\), so generic frequency vectors admit no such equilibrium. Theorem 10 says a graph admits one for some frequencies and coupling iff it is bipartite.

  Theorem 11 is printed with the quantifier “every coupling strength \(K>1\)” and every real frequency vector. Its proof first rescales time to set \(K=1\), then either applies Theorem 8 (when the two neighbor classes balance at every vertex, forcing \(\omega=0\)) or chooses a vertex with counts \(d^+\ne d^-\). The local potential is \(E(\theta)=-\sum_k\omega_k\theta_k+\sum_{\{j,k\}}(1-\cos(\theta_j-\theta_k))\), defined locally because angles live on a torus. Perturbing only \(\theta_k\mapsto\theta_k+x\) gives
  \[
  E(\theta)-E(\theta^x)=\omega_kx+(d^+-d^-)\sin x
  =(d^+-d^-)(-x+\sin x),
  \]
  since \(d^+-d^-=-\omega_k\) at equilibrium. Its leading term is \(-(d^+-d^-)x^3/6\), again sign-changing. The printed theorem says \(K>1\), whereas the proof’s time rescaling appears to establish the same claim for any \(K>0\); the card preserves the printed bound and records the broader scope only as a proof-derived observation. The abstract and Corollary 12 say “any coupling strength,” under the paper’s positive-coupling setup.
* **Corollary 12 (physical p. 7):** Every Lyapunov-stable equilibrium of (7) on a graph with at least one edge has at least one strictly negative Jacobian eigenvalue. The center-manifold argument first gives all eigenvalues nonpositive; Theorem 11 rules out the all-zero case. The paper explicitly says strict negativity is necessary but not sufficient. This is not a positive-semidefinite/Hessian sufficiency test and does not settle nonlinear stability when the linearization is merely semidefinite.

## How to use this result

Use Theorems 8 and 11 as a **degenerate-case failure-mode test**: when the entire Kuramoto Jacobian vanishes, inspect the first nonzero higher-order energy variation along a valid perturbation; here it is cubic and changes sign, so the equilibrium is a saddle despite the zero linearization. Do not extend this conclusion to arbitrary equilibria with a semidefinite Hessian/Jacobian, to signed random ensembles, or to general potentials without the paper’s graph/coupling structure. The theorem establishes instability of the stated equilibrium, not a count or classification of stable equilibria beyond Corollary 12’s necessary eigenvalue condition.

## Verification and evidence

The local SymPy script `math/verify_w24_examples.py` expands the two displayed energy differences exactly and evaluates each at \(x=\pm0.1\). The opposite signs and Taylor series are a check of the source’s local formulas, not a substitute for its universal graph proof. The calculation output is in `math/verification_results.json`. Rendered source pages 3, 5, 6, and 7 were viewed; full page-by-page coverage is in `reading_coverage.json#sources.PGEL-022`.

## Boundary for W24/C118

The proof is specific to the Kuramoto sinusoidal edge energy and a completely degenerate equilibrium (or the one-vertex perturbation in Theorem 11). It supplies a nonlinear-stability warning against declaring zero curvature stable from a linear test. It does **not** give the C118 signed-complete-graph probability bound or a certificate for every second-order critical point.
