# AUX-W07-UNIVERSALITY-2018 — high-dimensional WUSF scaling

**Source and read copy.** Tom Hutchcroft, “Universality of High-Dimensional Spanning Forests and Sandpiles,” arXiv:1804.04120v2 (30 May 2019), accepted author version; published in *Probability Theory and Related Fields* 176 (2020), 533–597. Read the complete 61-physical-page PDF at evidence/fulltexts/AUX-W07-UNIVERSALITY-2018.pdf, SHA-256 d5a4c15a73698fdf69379688f8a58707b17b852c83225d38b4029f54758afdcf, including references. D05 checked identity and acquisition only; W07 read the complete paper. Render-checked physical pp. 9–13, 24, 44, 47, 55, 57, and 58, including theorem hypotheses, constants/normalizations, and key proof steps.

## Model and hypotheses

The results concern the wired uniform spanning forest on connected networks with finite vertex conductance \(c(v)=\sum_{e\ni v}c(e)\); theorem-specific assumptions are stronger as indicated below. The simple-random-walk transition operator is \(P\), and the bubble norm is
\[
\|P\|_{\mathrm{bub}}=\sum_{n\ge0}(n+1)\|P^n\|_{1\to\infty},\qquad \|P^n\|_{1\to\infty}=\sup_{u,v}p_n(u,v).
\]
The controlled-stationary-measure condition is \(C^{-1}\le c(v)\le C\). For a vertex \(v\), \(q(v)\) is the probability that two independent walks started at \(v\) never return to \(v\) after time zero and never intersect each other after time zero. Constants implicit in \(\preceq\) may depend on the fixed network and its stated regularity constants; the lower bounds display \(q(v)\) explicitly.

## Main conclusions and exact scope

- **Theorem 1.1 (PDF p. 9).** On a transitive network with finite bubble norm, the past \(\mathcal P(v)\) has \(\mathbb P(\operatorname{diam}_{int}\mathcal P(v)\ge R)\asymp R^{-1}\) and \(\mathbb P(|\mathcal P(v)|\ge R)\asymp R^{-1/2}\) for \(R\ge1\). The paper notes that transitive graphs with at least quintic volume growth satisfy the hypothesis.
- **Theorem 1.2 (PDF p. 10).** With controlled stationary measure and finite bubble norm,
  \[
  q(v)R^{-1}\preceq\mathbb P(\operatorname{diam}_{int}\mathcal P(v)\ge R)\preceq R^{-1},\qquad
  q(v)^{5/2}R^{-1/2}\preceq\mathbb P(|\mathcal P(v)|\ge R)\preceq R^{-1/2}.
  \]
  The vertex-dependent \(q(v)\) is part of the lower bound; it need not be uniformly positive at every vertex (for example, a pendant location can have \(q(v)=0\)).
- **Theorem 1.3 (PDF p. 11).** Under controlled stationary measure and finite bubble norm, every WUSF tree has volume-growth dimension 2, spectral dimension \(4/3\), and walk dimension 3 almost surely, with the paper's intrinsic tree metric conventions.
- **Theorems 1.4–1.6 (PDF pp. 12–13).** For \(d\ge5\), the WUSF on \(\mathbb Z^d\) has extrinsic past-diameter tail \(\asymp R^{-2}\) (Theorem 1.4). Theorem 1.5 assumes a controlled-stationary-measure network that is \(d\)-Ahlfors regular for some \(d>4\) and satisfies Gaussian heat-kernel estimates; it gives \(q(v)^2R^{-2}\preceq\mathbb P(\operatorname{diam}_{ext}\mathcal P(v)\ge R)\preceq R^{-2}\log R\). Theorem 1.6 assumes controlled stationary measure, finite bubble norm, and uniform ballisticity, defined by \(\sup_v\mathbb E_v[\sup\{n\ge0:d(v,X_n)\le r\}]\le Cr\) for every \(r\ge1\); it gives \(q(v)^2R^{-1}\preceq\mathbb P(\operatorname{diam}_{ext}\mathcal P(v)\ge R)\preceq R^{-1}\).
- **Theorems 1.7–1.9 (PDF pp. 14–15).** Burning-bijection and Green-function comparisons transfer selected past-size/diameter estimates to Abelian sandpile avalanche radius, cluster size, and total topplings. These are avalanche conclusions under the separate graph hypotheses in the statements; they are not forest-connectivity claims.

## Proof dependency chain

Sections 2–4 establish Wilson/v-rooted WUSF comparisons and interlacement Aldous–Broder identities. Proposition 4.1 obtains intrinsic-diameter lower bounds by forcing an interlacement trajectory to hit the past at a controlled capacity; Proposition 4.3 uses last visits to obtain extrinsic lower bounds. Section 5 bounds the length and capacity of loop-erased random walk: conditional independence after erased gaps is controlled by the bubble norm, and the variational estimate \(\operatorname{Cap}(A)\ge |A|_c^2/I(A)\) converts intersection energy into capacity. Section 6 uses Wilson's algorithm and stochastic domination to derive moments/tails for rooted WUSF balls. In Section 7, interlacement slicing and a capacity split give a recurrence of the form \(Q(3n)\le C/n+Q(n)/6\), yielding the intrinsic upper tail and volume exponent. The sharp \(\mathbb Z^d\) extrinsic estimate uses pioneer vertices and diagrammatic loop bounds; \(d=5\) needs the two-loop terms retained in the paper. Section 8 invokes the Barlow–Járai–Kumagai–Slade criterion: high-probability volume \(\asymp n^2\) and resistance to the intrinsic sphere at least of order \(n\) give spectral dimension \(4/3\) and walk dimension 3. Section 9 uses the burning bijection and the Green-function identity \(\mathbb E[\mathrm{Av}_v(H,u)]=G(v,u)/c(u)\).

## W07 use boundary

These are quantitative and geometric theorems for WUSF, not FMSF/WMSF. They are useful as an explicit comparison showing which exponents and proof tools belong to the uniform model. They do not prove a minimal-forest threshold, connectivity, or end theorem, and do not resolve C105. Keep intrinsic tree diameter, extrinsic graph diameter, past volume, and avalanche observables separate.

## Full reading coverage

All 61 physical pages were read. evidence/W07/reading_coverage.json records the full introduction and statements (pp. 1–15), background/Wilson and v-WUSF domination (pp. 16–18), interlacement dynamics (pp. 19–23), diameter lower bounds (pp. 23–27), LERW length/capacity (pp. 28–32), volume bounds (pp. 33–42), critical exponents (pp. 43–54), spectral dimension/diffusion (pp. 55–56), sandpiles (pp. 57–58), and references (pp. 59–61). Review status is pending.
