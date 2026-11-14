> Package binding: current R05 mother-final review accepts this read and binds the current PDF/card/coverage evidence. This package itself is pending R05 final-scope review. Any later-stage wording below records the source card's historical state; see [review index](../../audit/review-index.json).

# PGEL-026 — On the Typical and Atypical Solutions to the Kuramoto Equations

**Reader:** L09, W24 helper batch L09_B8; R08 helper-stage passed; mother hash binding pending.  
**Source version:** Tianran Chen, Evgeniia Korchevskaia, and Julia Lindberg, arXiv:2210.00784v3 (30-page PDF; revised 25 Sep 2024). The card’s theorem/page locators refer to that exact local author-version PDF, SHA-256 `6f820a5bd2a1a53929c58283c12ddd452ac2ab6f437954bd66b215b0789b3ca7`.

## Model and what is counted

For a connected undirected graph \(G\) on vertices \(\{0,1,\dots,n\}\), with symmetric nonzero couplings \(k_{ij}=k_{ji}\), the frequency-synchronization equations are rotated to \(\theta_0=0\) and expressed as the Laurent system (2.3), physical p. 3:

\[
f_{G,i}(x)=\bar w_i-\sum_{j\sim i}\frac{k_{ij}}{2i}
\left(\frac{x_i}{x_j}-\frac{x_j}{x_i}\right),\qquad x_0=1.
\]

Unit-torus roots \((|x_i|=1)\) correspond to real phase configurations. The paper’s generic root counts and exceptional-coupling criteria are for **all isolated roots in** \((\mathbb C^*)^n\), with multiplicity where stated; these may include non-unit, nonphysical complex roots. None of these counts classifies stable equilibria or local minima.

Let the adjacency polytope be \(\check\nabla_G=\operatorname{conv}(\{\pm(e_i-e_j):\{i,j\}\in E(G)\}\cup\{0\})\), with \(e_0=0\); \(\operatorname{Vol}\) denotes normalized volume \(n!\) times Euclidean volume. The paper recalls Bernshtein’s second theorem (Theorem 2.2, physical p. 4): if all nonzero initial systems have no \(\mathbb C^*\)-zero, the isolated root count with multiplicity equals the mixed volume; a nonzero initial-system root makes that count strictly smaller when the mixed volume is positive. Randomization by a nonsingular matrix preserves the zero set and exposes identical supports (pp. 4–5).

## Theorem 3.5: generic complex-root count

**Statement (physical pp. 7–8):** For generic real or complex natural-frequency constants and generic symmetric real or complex nonzero edge couplings, every \(\mathbb C^*\)-root of (2.3) is isolated and nonsingular, and the total count equals \(\operatorname{Vol}(\check\nabla_G)\). Corollary 3.6 (p. 9) identifies this with the BKK mixed volume and calls the system Bernshtein-general.

**Proof chain:**

1. Sard’s theorem makes roots isolated and regular for generic frequency constants (p. 8).
2. Choose a generic symmetric lifting function \(\omega(e_i-e_j)=\omega(e_j-e_i)\), near the constant lift, inducing a regular unimodular triangulation of the adjacency point configuration (Lemmas 3.1–3.2, pp. 6–7). The center point \(0\) lies in every cell. Each simplex corresponds by Lemma 3.3 to an acyclic directed subgraph whose underlying graph is a spanning tree (p. 7; elementary proof Lemma B.1, p. 26).
3. Deform the coefficients to \(a_{ij}t^{\omega_{ij}}\) while preserving the edge symmetry (p. 8). Along a ray avoiding the finite exceptional parameter set, homotopy continuation gives smooth solution paths. Puiseux leading terms satisfy the corresponding initial system.
4. For each simplex, the initial system is the tree Laurent system. Lemma 3.4 (p. 7) proves it has one regular \(\mathbb C^*\)-zero by induction on vertices: remove a leaf, fix the homogeneous scaling, and solve the resulting binomial; Appendix B supplies supporting combinatorial and face-reduction proofs (pp. 26–28).
5. Distinct simplices give distinct paths. Their number is the triangulation’s normalized volume, so the generic root count is at least \(\operatorname{Vol}(\check\nabla_G)\); BKK gives the opposite bound. This proves equality.

The conclusion concerns generic parameters. It is not an all-parameter claim: exceptional parameter choices are analyzed separately.

## Atypical couplings and circulation test

Definition 4.1 (physical p. 10) calls symmetric nonzero couplings exceptional when the isolated \(\mathbb C^*\)-root count is below the adjacency-polytope volume for every frequency choice. For a facial subsystem, Lemma 4.3 (p. 11) rewrites the initial equations as

\[
\check Q(\vec G_F)\bigl(x^{\check Q(\vec G_F)}\circ a(\vec G_F)\bigr)^\top=0,
\]

so edge quantities \(x^{\check Q}\circ a\) form a possibly complex-valued circulation. A weak spanning tree parameterizes every facial root (Definition 4.7 and Lemma 4.9, pp. 12–13); Corollary 4.10 gives the exact nonzero-parameter compatibility equations, with expanded proof in Corollary B.4 (p. 28).

For a cycle face, Definition 4.12 and Proposition 4.14 (physical p. 14) say exceptional couplings are exactly those for which the oriented cycle has equal numbers of clockwise/counterclockwise edges and

\[
\prod_{(i,j)\in E^+(\vec H)} k_{ij}
=(-1)^{N/2}\prod_{(i,j)\in E^-(\vec H)} k_{ij}.
\]

For a general bridgeless facial graph, Theorem 4.17 (pp. 15–16) characterizes exceptional couplings by balance of every cycle in a cycle basis with respect to one common nonzero circulation, using the ratios \(k_{ij}/\eta_{ij}\). If the facial subgraph has a bridge, there is no nonzero circulation supported on every edge and its facial system has no \(\mathbb C^*\)-root. Proposition 4.20 (p. 17) takes the union over bridgeless, maximally bipartite facial subgraphs. These are algebraic criteria for a fixed graph and its symmetric coupling parameters, not a random-sign probability estimate.

## Positive-dimensional solution families

In §5 (physical pp. 19–25), homogeneous natural frequencies reduce the algebraic system to zero constant terms; positive-dimensional \(\mathbb C^*\)-components therefore require exceptional couplings (Corollary 5.1, p. 19).

* **Even cycle (Proposition 5.3, physical p. 20):** for \(G=C_N\) with even \(N>2\), homogeneous oscillators and edge couplings \(k_{ij}\in\{+k,-k\}\), \(k\ne0\), a balanced subnetwork exists when the number of negative edges is even for \(N\equiv0\pmod4\), and odd for \(N\equiv2\pmod4\). This yields a positive-dimensional complex-root family. If $k\in\mathbb R\setminus\{0\}$, the source asserts existence of a positive-dimensional real zero set. For the raw parameter $\lambda$ in the displayed tree/cycle parametrization, the unit-torus restriction is the scaled circle $|\lambda|=|k|/2$ (for example $\lambda=k e^{it}/(2i)$); do not impose $|\lambda|=1$ on this raw parameter. The source’s p. 20 phrase “restricting $\lambda$ to the unit circle” must be read after this scaling/reparameterization. Proposition 5.2 is only a necessary condition for general cycle parameters.
* **C4 explicit curve (Example 5.4, physical pp. 20–21):** one balanced orientation with \(k_{10}k_{32}=k_{12}k_{30}\) gives
  \[
  (x_1,x_2,x_3)=\left(-\frac{2i\lambda}{k_{10}},-\frac{k_{12}}{k_{10}},\frac{2i\lambda}{k_{30}}\right),\quad \lambda\in\mathbb C^*.
  \]
  For all unit couplings, \(\lambda=i e^{it}/2\) produces \((x_0,x_1,x_2,x_3)=(1,e^{it},-1,-e^{it})\), a real-torus one-parameter family. Other C4 balanced orientations give different curves and constraints.
* **Several even cycles sharing one edge (Proposition 5.5, physical pp. 21–23):** for \(d\) independent even cycles sharing only one edge \(e\), the choice \(k_e=ds\), all other edge couplings \(s\ne0\), and homogeneous natural frequencies \(w\mathbf1\) yields a positive-dimensional complex root set. The proof specializes the tree-solution parameters to \(\lambda_1=\cdots=\lambda_d\), uses Proposition 4.18 to cancel one facet circulation term, and computes the opposite-face term as zero. The theorem does not assert a real-torus family for all complex \(s\); Example 5.6 gives a specific real restriction.
* **Lifting C\( _{4m}\) curves (Proposition 5.7, physical p. 23):** for \(m\ge2\), a graph containing a \(C_{4m}\), with the stated condition that every path joining its two bipartition classes contains a cycle edge, has a positive-dimensional complex family and a real family for the homogeneous, unit-coupling system. This is a sufficient structural condition, not a classification of all graphs with continua.

## Local symbolic verification

`math/verify_w24_examples.py` substitutes the source’s C4 curve into all three reduced Laurent equations (2.3) and obtains identically zero; it separately checks its unit-torus restriction. This is an exact finite-graph substitution, not a proof of Proposition 5.3 for arbitrary even cycles. The output is saved at `math/verification_results.json`. The rendered formula pages 7–9, 13–17, 20–22, and 27–28 were viewed; every physical PDF page is listed in `reading_coverage.json#sources.PGEL-026`.

## Boundary for W24/C118

This source offers a strong algebraic root-count and exceptional-parameter method for undirected graphs with symmetric nonzero couplings. It counts generic complex roots, not real local minima or second-order stable states. C118’s signed-complete-graph ensemble has a discrete coupling law and asks for a probability certificate over stable critical points; no transfer from this paper’s generic parameter result to that ensemble or probability statement is proved here.
