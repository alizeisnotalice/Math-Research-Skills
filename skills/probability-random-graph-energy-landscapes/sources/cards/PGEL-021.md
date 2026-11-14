> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-021 — Kuramoto Networks with Infinitely Many Stable Equilibria

## Identity and reading record
Davide Sclosa, “Kuramoto Networks with Infinitely Many Stable Equilibria,” read local arXiv:2207.08182v1 (17 July 2022); published as *SIAM Journal on Applied Dynamical Systems* 22(4):3267–3283 (2023), DOI [10.1137/23M155400X](https://doi.org/10.1137/23M155400X). [Official arXiv record](https://arxiv.org/abs/2207.08182); [SIAM publication page](https://epubs.siam.org/doi/10.1137/23M155400X). The exact local 17-page arXiv v1 author-version PDF, SHA-256 `e68915c58e27084a126226246d223a806815f428b3d3fed71dccdd8d2bc2b9da`, was read in physical-page order through references. The publisher full text was not read. The canonical full-read index had no exact title/hash match before this read. R05 helper stage passed; mother-hash binding is pending (R05 metadata_verified=false). The mathematical text of this passed card and its checked six-cycle calculation is unchanged in the mother copy.
## Model and stability meaning

The graph is finite, connected, undirected, and unweighted, and the homogeneous Kuramoto flow is

\[
\dot\theta_j=\sum_{k\in N(j)}\sin(\theta_k-\theta_j),\qquad \theta_j\in\mathbb T.
\]

The energy is (E(\theta)=\sum_{\{j,k\}\in E$G$}(1-\cos(\theta_j-\theta_k))), with the dynamics written as (\dot\theta=-\nabla E). A common phase shift is symmetry; “non-equivalent” means modulo that shift. The paper explicitly defines stable as **Lyapunov stable** (physical p. 1), not asymptotic stability modulo the phase orbit and not positive definiteness of the Hessian. Its analytic-gradient discussion (physical pp. 4–5) cites the equivalence between Lyapunov-stable equilibria and local minima for this setting; equilibrium manifolds can therefore be stable despite neutral tangent directions.

## Main results and proof route

**Theorem 1.1 (physical p. 2).** For each integer $d\ge1$, there is a connected graph $G$ for which the Kuramoto system contains a $d$-dimensional manifold of stable equilibria. The construction starts with $d$ disjoint six-cycles, each carrying phases $2k\pi/6+\alpha_i$. Connect opposite vertices of the first six-cycle to the corresponding opposite vertices of each other cycle, adding $4(d-1)$ cross-edges. At $\alpha_1=0$ and $\alpha_2=\cdots=\alpha_d=\pi/2$, every cross-edge has phase difference $\pi/2$, so its Jacobian weight is zero. Each cycle block has characteristic polynomial

\[
\lambda(\lambda+1/2)^2(\lambda+3/2)^2(\lambda+2).
\]

The (d) zero directions are tangent to the $d$-torus of equilibria; every other eigenvalue is strictly negative. The implicit spectral gap persists near the chosen parameter. Shoshitaishvili’s theorem gives a local foliation by stable manifolds; the paper uses that foliation to conclude every point in an open subset of the equilibrium manifold is Lyapunov stable (physical pp. 7–8). The theorem asserts existence of such a graph family; it is not a probability statement about typical graphs.

**Corollary 1.2 (physical p. 2).** The planar eye graph has infinitely many non-equivalent stable equilibria. In the two-cycle case, an open interval of relative phase shifts around $\pi/2$ remains stable (physical pp. 8–9).

Supporting structure: algebraic geometrization shows equilibria form an algebraic set; phase-shift symmetry contributes a common neutral direction; a balanced vertex subset satisfies $\sum_{k\in K}e^{i\theta_k}=0$. Lemma 3.3 (physical p. 6) says that when a vertex partition has balanced cross-neighborhoods and each part is internally at equilibrium, independent shifts of the parts produce a $d$-torus of equilibria. The stability proof then checks the transverse Jacobian spectrum and invokes the cited topological bifurcation theorem. The paper also states Kamiyama’s dimension theorem for balanced configurations (Theorem 3.4, physical p. 11) and classifies equilibrium forms in complete bipartite graphs (Proposition 4.3, physical pp. 12–13); those classifications are not general stability claims.

## What remains open or numerical

Conjecture 1.3 (physical p. 3)—that for every graph the equilibrium set is a finite union of manifolds—is explicitly an **open conjecture**, not proved here. Numerical eigenvalue computations for the larger $H_{36},H_{60},H_{90}$ examples and the RK4 heteroclinic plots for $K_4$ and the four-cycle (physical pp. 8–9, 14–15) are numerical illustrations; the main Theorem 1.1 does not rely on those computational observations. The theorem’s proof uses exact six-cycle spectrum plus a cited bifurcation result.

## Transfer limits

The construction is an explicit existence counterexample to finite-count expectations: stable equilibria need not be isolated or Hessian-nondegenerate. It does not imply that such manifolds are typical, that most initial conditions converge to a particular member, or that signed/asymmetric couplings have the same landscape. Keep it in the positive symmetric homogeneous model.

Coverage: all physical pages 1–17 were read, including all sections and references. Rendered pages and coverage detail are in the batch `../../reading_coverage.json` (mother entry; rendered images remain under `../renders/PGEL-021/`); exact six-cycle characteristic-polynomial verification is in `../math/exact_checks.py`. Review is pending.
