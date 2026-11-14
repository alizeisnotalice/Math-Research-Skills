# Source card — Bérczi, Borbényi, Lovász & Tóth (2024), “Cycle Matroids of Graphings: From Convergence to Duality”

**Reading evidence.** Full physical-page read of the complete 19-page arXiv v3 article, including all proofs, acknowledgments, and references (PDF pp. 1–19). Local artifact SHA-256: `c57ef51bafad319a47f7b6dddb4a8755b9600f18f5ef66d67b87e0acb0942be0`. Identity/version checked against the PDF title page and [official arXiv record](https://arxiv.org/abs/2406.08945): arXiv:2406.08945v3, revised 14 Oct 2024; authors Kristóf Bérczi, Márton Borbényi, László Lovász, László Márton Tóth. Rendered and visually checked theorem pages physical pp. 4–5 (Theorems 1.2–1.8), p. 12 (Theorem 4.2 proof), p. 13 (Theorem 4.4 / weak exposure), pp. 17–18 (duality proofs and final theorem). Complete page coverage is recorded in `../reading_coverage.json (entry local_id=AUX-W07-CYCLE-MATROIDS-2024)`.

## Model

A graphing G=(J,mu,E) is a Borel graph on a standard Borel probability space, with finite degrees and the measure-preserving edge condition. Its edge measure is eta_G(F)=1/2 integral deg_F(x) dmu(x). For a Borel edge set F, its graphing rank is

    rho_G(F) = 1 − E_x[1 / |V(G_F^x)|],   with 1/infinity := 0.

This extends the finite cycle-matroid rank normalized by the number of vertices. The paper establishes rho_G is increasing and submodular and rho_G(F)≤eta_G(F). A forest is hyperfinite if, for every epsilon>0, deleting an edge set of eta-measure at most epsilon leaves only finite components. A hyperfinite essential spanning forest spans each finite component of G and has only infinite components inside each infinite G-component. Edge sets are identified up to null sets.

## Local-global limits and quotient convergence

**Theorem 1.1 (physical p. 3).** If finite graphs G_n have a common degree bound D and converge locally-globally to a graphing G, then their normalized cycle-matroid rank functions r_{G_n}/|V(G_n)| quotient-converge to rho_G. Here quotient convergence means, for each finite k, Hausdorff convergence of the set Q_k of all k-quotients (rank values on unions of cells of measurable k-partitions).

Proof route (Section 3, pp. 8–10): Theorem 3.2 shows that for any graphing parameter f continuous under local convergence, the setfunction F↦f(G_F) quotient-converges. For one direction of Hausdorff convergence, approximate a Borel edge coloring/partition of G by colorings of G_n using local-global convergence; continuity of f makes every coordinate on a union of color classes converge. For the reverse direction, take a convergent subsequence of colored graphings realizing candidate quotients; completeness supplies a colored limit, and local-global convergence approximates that coloring back on G, placing the limiting quotient in Q_k(f_G). Set f(G)=rho_G(E(G)); Proposition 3.1 supplies continuity of total rank under local convergence, completing Theorem 1.1.

The stronger local-global hypothesis matters. **Example 3.4 (physical p. 10)** interlaces a 3-regular expander sequence of girth tending to infinity with the disjoint union of two copies of each graph. Both have the same local limit (a 3-regular treeing), but a two-cell quotient of the doubled graph tends to singleton-cell ranks 1/2 and total rank 1. Expansion plus large girth forces a fixed gap epsilon=c/32 from this quotient for the connected expander. Therefore local convergence alone does not imply quotient convergence.

## Exposed measures, forests, and submodularity

Define the minorizing-measure set mm+(rho_G)={alpha measure: 0≤alpha≤rho_G}; its base set bmm+(rho_G) consists of alpha with alpha(E)=rho_G(E). Since alpha≤rho_G≤eta_G, each such measure has a Radon–Nikodym density f_alpha∈[0,1] with respect to eta_G.

**Theorem 1.2 (physical p. 4; proof pp. 11–14).** Exposed points of mm+(rho_G) are exactly edge-restriction measures eta_G|F for hyperfinite subforests F. Exposed points of bmm+(rho_G) are exactly eta_G|F for hyperfinite essential spanning forests F.

The proof of the hard direction appears as Theorems 4.2 and 4.4. Given a linear witness g in L-infinity, a weighted invasion/Prim–Kruskal construction selects a maximum-weight hyperfinite essential spanning forest F with a fixed Borel edge order breaking ties. A mass-transport token accounting proves eta_G(F)=rho_G(E), and hence F is hyperfinite. For every threshold t, its superlevel part F_{g≥t} is an essential spanning forest of the graphing restricted to {g≥t}; therefore eta_G(F∩{g≥t})=rho_G({g≥t}). Layer-cake integration then shows the indicator 1_F maximizes the witness among all densities in the base set. Uniqueness of the exposed maximizer forces f_alpha=1_F almost everywhere. For the non-base set, discard negative-g edges and apply the same layer-cake argument to positive levels. Conversely, an indicator density is exposed by the witness 1_F−1_{F^c}. Lemma 4.1 identifies the restrictions lying in the (base) minorizing set with hyperfinite (essential spanning) forests.

**Theorem 1.3 (physical p. 4; proof p. 14).** For Borel F⊆E, the following are equivalent: (i) F is a hyperfinite forest; (ii) F is a subset of a hyperfinite essential spanning forest; (iii) rho_G(F)=eta_G(F). Essential spanning is characterized by rho_G(F)=eta_G(F)=rho_G(E). The first equivalence follows from the hyperfinite-treeing rank/edge-measure criterion and the extension algorithm of Corollary 4.3; the essential version follows from the same criterion for full rank.

Theorem 4.7 and Corollary 4.8 (pp. 13–14) extend the 0–1 indicator conclusion to weakly exposed points and show they are strongly exposed. Theorem 4.13 (p. 15) proves submodularity again by identifying hyperfinite forests as independent sets of a measurable matroid: subset closure, increasing-union closure, and exchange imply the supremum-of-independent-measures rank is submodular.

**Open question, not a theorem:** Question 1.4 (p. 4) asks whether every extreme point of bmm+(rho_G) is exposed (and thus comes from a hyperfinite essential spanning forest). The authors do not resolve it.

## Planar duality and cost

The cocycle rank is rho*_G(F)=rho_G(E\\F)+eta_G(F)−rho_G(E). The paper proves planar duality under a deliberately restricted model: components are 2-vertex-connected planar maps with specified Borel embeddings, no vertex accumulation points, finite facial cycles, and uniformly bounded face lengths. A measure-preserving Borel edge bijection identifies primal and dual edges. The authors say these restrictions simplify technicalities; results are not stated here for arbitrary planar graphings.

- **Theorem 1.6 (physical p. 5; proof pp. 16–17).** For a hyperfinite dual planar pair G,G*, rho*_G=rho_{G*} and rho*_{G*}=rho_G. One proof uses Theorem 4.2: exposed base points are hyperfinite essential spanning forests, complements correspond between primal and dual, and hyperfiniteness ensures complements remain admissible. Equal exposed-point sets give equal base sets by weak-star closed convex hull, which determine the submodular rank. A second proof uses mass transport between finite dual components/faces and primal edges.
- **Theorem 1.7 (physical p. 5; proof p. 17).** For a non-hyperfinite dual planar pair, rho*_{G*} differs from rho_G and rho*_{G*}(E)=cost(G). The proof takes a one-ended hyperfinite spanning forest F* of G* (the cited existence theorem applies in this scope); its complementary primal set E\\F* is a treeing of G. Its edge measure is cost(G) by the cost-equals-edge-measure criterion for treeings, and the corresponding measure belongs to the dual base set.
- **Theorem 1.8 (physical pp. 5–6; proof p. 18).** For any Borel total edge order on a dual planar pair, the wired maximal spanning forest T_w of G is exposed in bmm+(rho_G), while the free maximal spanning forest T_f of G is exposed in bmm+(rho*_{G*}). The proof identifies T_f in G with the complement of the wired minimal spanning forest in G* under the corresponding order.

## Use and transfer limits

Use the rank formula and Theorems 1.1–1.3 for bounded-degree graph-limit / hyperfinite-cycle-matroid questions; use Theorems 1.6–1.8 only after checking the stated planar embedding, local finiteness/bounded-face, duality, and hyperfiniteness assumptions. The cycle-matroid rank of the full graphing edge set is at most 1; the dual rank can record cost above 1 in the non-hyperfinite case. The paper does not establish that all extreme base points are hyperfinite; that remains Question 1.4. Related source papers on graphings, one-ended spanning forests, and quotient convergence cited in the references are not treated as having their proofs read here.
