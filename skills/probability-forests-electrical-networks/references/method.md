# Method guide

## 1. Separate the models

| Object | Definition | Typical theorem interface |
|---|---|---|
| Weighted finite UST | A spanning tree (T) has mass proportional to (\prod_{e\in T}c(e)). | Matrix-tree and transfer-current determinants; finite graph assumptions. |
| FSF / WSF | Weak limits of USTs along free or wired exhaustions. | Infinite connected network; retain each theorem’s local-finiteness or finite-vertex-conductance assumptions. |
| FMSF / WMSF | Keep an iid-label edge unless it is maximal on a cycle, or on a cycle/bi-infinite path for the wired rule. | Percolation thresholds (p_c,p_u), invariant geometry, often unimodularity. |

Never transfer an FSF/WSF theorem to FMSF/WMSF solely because both are forests. In particular, a theorem about UST negative association does not imply an MST analogue.

## 2. Audit hypotheses before using MTP

Write the transport (f(G,x,y)), the root law, and the desired equality. Confirm unimodularity, or use the orbit-weighted form for a quasi-transitive action. Transitivity alone is insufficient. For a rooted random network, the required expectation may include (\mathbb E[c(\rho)]<\infty); retain it where the theorem states it.

MTP arguments often contradict a proposed finite witness by sending unit mass from infinitely many vertices to that witness. Check that the selected witness is invariant/equivariant and measurable. If choosing a representative would require a forbidden global choice, the transport is not justified.

BLPS uses connected conductance networks with finite total incident conductance at each vertex, but does not require the underlying graph to be globally locally finite. In its Corollary 8.2, “some vertex orbit is infinite” still implies every vertex orbit is infinite: if a finite orbit exists, choose a positive conductance threshold along a path to it. The threshold subgraph is locally finite and automorphism-invariant, so each vertex orbit lies in a finite-radius finite ball union there. Do not infer finite balls in the original weighted graph.

For USF end statements, keep the proof interface tied to its exact model. Morris’s conductance martingale is for weighted UST/FSF/WSF and its recurrence corollary assumes uniformly bounded edge conductances. Hutchcroft’s wired cycle-breaking dynamics prove WUSF one-endedness for transient reversible random rooted networks when \(\mathbb E[c(\rho)^{-1}]<\infty\); stationarity plus update-tolerance is the key step. Neither result is automatically a WMSF theorem. Hutchcroft–Peres component-graph results use infinite connected locally finite transitive graphs with polynomial volume growth. The Theorem 2.1/Proposition 2.2 spread bounds used here require $d>4$ (where FUSF=WSF); Theorem 2.1’s constant depends on $G$ and $|K|$, while Proposition 2.2’s constant depends on $G$, the number of indexed sets, and their sizes. For $d_1\ge d_2\ge9$, Theorem 1.1 says ubiquity in dimension $d_1$ implies ubiquity in $d_2$, and the separating witness is ubiquitous only in the lower dimension. Their coarsening merges hyperedges while quotient merges vertices. Proposition 2.2 is only for its simultaneous distinct-component event: every prescribed set $K_i$ lies in one USF component, and those components are pairwise different. It does not give an unqualified product bound for arbitrary disjoint-set connection events. These results do not determine minimal-forest connectivity.

Hutchcroft’s interlacement Aldous–Broder Theorem 1.1 defines the oriented WUSF as $AB_t(\mathcal I)=\{-e_t(v):v\in V\}$: reverse the trajectory edge that first enters $v$, so the forest arrow points from $v$ to its predecessor. His WUSF one-endedness criteria are Theorem 2.1 with its anchored-isoperimetric integral conditions and Theorem 2.4 for transient unimodular random rooted networks; preserve the wired model and its hypotheses. In the recurrent unimodular **unweighted graph** setting, van Engelenburg–Hutchcroft prove equality of UST and graph end counts (Theorem 1, p. 3). Theorem 15 (p. 18) is the one-ended iff unique-harmonic-measure criterion; Proposition 12 (p. 16) is a one-sided lower bound from extremal measures to UST ends. For high-dimensional WUSF scaling, Theorem 1.5 requires controlled stationary measure, $d$-Ahlfors regularity for $d>4$, and Gaussian heat-kernel estimates. Theorem 1.6 additionally uses finite bubble norm and uniform ballisticity along with controlled stationary measure. Keep these assumptions, $q(v)$ lower-bound factors, past intrinsic/extrinsic diameter, volume, tree walk dimension, and avalanche quantities separate. None of these uniform-forest results supplies an FMSF/WMSF conclusion.

## 3. Electrical-network checks

For conductance $c(e)$, use resistance $r(e)=1/c(e)$. In a finite weighted UST, $\mathbb P(e\in T)=c(e)R_{\rm eff}(s,t)$, equivalently $C_{\rm eff}(s,t)=c(e)/\mathbb P(e\in T)$; an identity printed without $c(e)$ uses a fixed-edge unit-conductance normalization. State current orientation and normalization (unit current, unit voltage, or unit edge flow). In finite weighted UST, the distinct-edge determinant is the unnumbered Transfer Current Theorem in BLPS equations (4.4)–(4.5), PDF p. 12 (proof pp. 12–13); BLPS Theorem 4.1, p. 10, is the single-edge current identity. In the resistance-energy flow space of an infinite network, free current is the projection onto the cycle-flow orthogonal complement, while wired current is the projection onto the star-flow space. Accordingly FSF uses the projection-DPP kernel P_{Diamond^perp}, and WSF uses P_star. Check the weighted-coordinate convention and prove the relevant limit along the correct exhaustion.

Primary-paper interfaces already covered by complete reads:

- BLPS Theorem 7.3 (PDF p. 24) gives, under the paper's connected-network and finite-incident-conductance assumptions, `FSF=WSF` iff free and wired currents agree iff `HD(G)` is trivial modulo constants. This is equality of laws/currents, not a singularity criterion.
- BLPS Corollary 8.2 (PDF p. 26) gives ergodicity of each law and mutual singularity when the laws differ, under the stated infinite-vertex-orbit automorphism hypothesis. Under the paper's network assumptions, one infinite orbit forces every vertex orbit to be infinite. Without that action hypothesis, the general distinct-law singularity problem remains open in BLPS.
- Aldous–Lyons Definition 2.1 (PDF pp. 10–11) is the general MTP statement. Their Theorem 3.1 (PDF pp. 14–16) says a fixed-graph unimodular root law exists iff `Aut(G)` is unimodular and, for a complete orbit section and one common Haar measure on compact-open stabilizers, the normalizer `c=Σ_i |Stab(o_i)|^{-1}` is finite. The formula gives rooted orbit-class mass; finite `c` alone is insufficient for a nonunimodular automorphism group. The corrected L10 use card v4 is accepted supplemental support; see the version-bound card in the source guide.
- Hutchcroft–Nachmias Theorem 1.9 applies to either FUSF or WUSF on a unimodular random network when `E[c(ρ)]<∞`; this skill's scoped card invokes the FUSF case. Their WUSF tail-property result is separate and requires its stationarity and one-ended-component assumptions.
- BLPS Theorem 12.2 gives free/wired planar duality for a proper planar network and its specified planar dual. Use the theorem's duality and conductance/resistance correspondence only when that dual setup is present.

## 4. Minimal-forest pipeline

Couple all Bernoulli percolations by the same continuous edge labels. Use cycle thresholds for FMSF and extended-cycle thresholds for WMSF. State (p_c) and (p_u) separately. LPS Proposition 3.6 relates equality of the forests to almost-everywhere uniqueness; Theorem 3.12 needs unimodular quasi-transitivity and (\theta(p_c)=0) for one-ended WMSF trees.

For Proposition 3.6, “almost everywhere” means Lebesgue-a.e. percolation parameter \(p\in(0,1)\), with a.s. at most one infinite open component at each such \(p\). Do not replace this with uniqueness a.s. at every \(p\).

When changing finitely many labels, cite the finite-change lemma and track which edges can change membership. For Theorem 3.22 of Lyons–Peres–Schramm, retain the exact conditional law from Lemma 3.23: on a finite edge set absent from FMSF, the normalized complementary labels \((1-U(e))/(1-Z_f(e))\) are conditionally i.i.d. uniforms. For a claimed end argument, identify which component is preserved and where MTP is used. Timár 2006 proves an end result under transitive unimodularity; that does not settle the nonunimodular case. Timár’s WIT map inserts e and, when needed, removes f∈C_x∩B(x,r)^c; this is not a local modification preserving all edges outside B(x,r). Keep Theorem 1.2/Corollary 1.5 (FMSF≠WMSF) separate from Lemma 1.4’s θ(p_c)=0 assumption. Alexander’s planar duality/invasion statements likewise require their stated lattice-like embedding and strict simultaneous uniqueness hypotheses; see the source card before using them.

## 5. Spanning-tree BK questions

Define disjoint occurrence using two disjoint edge sets that separately force the increasing events. Contrast it with ordinary intersection and with negative association for events supported on two fixed disjoint coordinate sets. The latter does not sum over all random witness choices. Do not cite product-measure BK/Reimer as a proof for a UST law.

For the BKPS USF component-distance theorem, the composition of independent component relations only yields an expanded random set. To bound edges outside a fixed first forest, invoke their Theorem 4.1 stochastic domination: the independent-copy expansion is coupled inside the adjacent-component expansion of the first WSF; each expansion level supplies at most one ambient connector. An independent union-path argument alone does not establish this edge count.

For Hutchcroft–Peres Proposition 2.2, retain the exact simultaneous event
\[
\bigcap_{i,j\in I}\{\mathcal F(K_i\cup K_j)\text{ iff }i=j\}.
\]
Each indexed set is internally in one USF component and different indices occupy pairwise distinct components; the sets need not themselves be disjoint. The proof uses Wilson's algorithm to include this event in the intersection of per-index connection events generated by independent walk families, then Theorem 2.1 and independence give the product spread bound. Do not generalize it to arbitrary disjoint-set connection events.

Lyons's projection-DPP representation can encode a finite weighted UST by multiplying reduced-incidence columns by $\sqrt{c(e)}$. Teufl–Wagner Theorem 1 supplies the finite unweighted all-minors rooted-forest count; Theorem 2 is a separate root-count formula under the full symmetric or alternating action on a distinguished boundary set. The three-terminal identity is proved separately, while the broader identities and resistance-reconstruction question remain conjectural. These are exact-law and electrical inputs for A141; neither addresses random disjoint witnesses or proves weighted-UST BK.

For B064, Archer–Nachmias–Shalev–Tang prove a lattice special case: on $\mathbb Z^d$, $d\ge3$, an everywhere-percolating base union an independently thinned WUSF is a.s. connected and transient. Taking the base to be a WUSF sample gives an invariant augmentation with per-edge probability at most its thinning parameter. This leaves the arbitrary-Cayley-graph question open and gives no minimal-forest conclusion.

## 6. Induced-component graphs of USFs

If \(H\subseteq G\), define \(I_G(H)\) by adding every ambient \(G\)-edge whose endpoints lie in the same component of \(H\). The induced graph has the same connected components as \(H\), but is generally not the raw forest. In Lyons–Peres–Sun, recurrence and effective resistance statements for the induced WSF component, and FSF/WSF resampling identities, must retain \(I_G(H)\) (the paper's overbar) in the object. Do not describe these as new recurrence results about the raw WSF tree.

## 7. Evidence and numerical checks

For each theorem card record: version, theorem/proposition number, PDF and printed pages where available, all hypotheses, proof dependency chain, key inequality, and what the result does not imply. For finite weighted examples, enumerate trees or solve the reduced Laplacian with exact rational arithmetic. Save the script and result; label them as finite checks. `evidence/W07/examples/verify_finite_examples.py` verifies a weighted-triangle transfer-current determinant and reproduces the LPS minimal-tree positive-correlation example over all (10!) label orders.


## 8. Reflected walks, planar Dirichlet data, finite CRSFs, and graphings

- **Reflected walk at infinity.** The construction assumes a connected transient conductance network and a pointwise lower bound $w\ge w_*$ on the continuous-time holding rates. Its energy-minimizing harmonic hitting law underlies the Aldous–Broder FUSF result. Keep local-finiteness assumptions for the forest/end applications. The Wilson construction gives the FUSF only on the event that the FUSF is connected; it is not an unconditional identity. The supercritical-LQG phase statements in §6 are conjectures. See the `AUX-W07-REFLECTED-INFINITY-2025` card.
- **Planar harmonic Dirichlet functions.** Apply the discrete/continuous HD isomorphism only to transient weighted polyhedral planar maps with the paper’s bounded-degree/codegree and conductance assumptions and an admissible double circle packing. Douglas’s equality is $D(\phi)=E_{\rm disk}(H)$ for the continuous disk harmonic extension $H$; the discrete graph function $h$ has comparable energy through a bounded isomorphism, not an energy isometry. Retain $D_0$/quasi-asymptotic language generally; the pointwise asymptotic upgrade requires bounded functions and a uniformly transient domain.
- **CyclePopping and CRSFs.** This is a finite connected simple weighted graph algorithm. For the magnetic determinantal law and the walk-step MGF, check Assumptions 1 and 3; use the magnetic operator $\Delta=D-W\circ\Phi$ and the normalized operator $\Delta_N=D^{-1/2}\Delta D^{-1/2}$ only where the source defines it. For general cycle weights, the loop-measure Poisson runtime uses Assumption 4. Distinguish $T$ (Markov-chain steps) from cycle/scope resampling counts. Do not infer an infinite-volume or reflection theorem.
- **Cycle matroids of graphings.** Use the rank and quotient-convergence results for finite-degree measure-preserving graphings and keep hyperfiniteness explicit. The planar duality/cost results require the restricted dual planar graphing hypotheses; Theorem 1.6 additionally assumes hyperfiniteness. Question 1.4 (all extreme base points exposed) remains unresolved. Do not transfer these graphing results directly to percolation thresholds or arbitrary Cayley graphs.

## 9. Cross-scope boundary: finite SAP counting is not a random forest law

Panagiotis, “Self-avoiding walks and polygons on hyperbolic graphs,” Theorem 6, is a G17 finite-plane-map inequality for a self-avoiding polygon's inner chords and inner vertex boundary. Its auxiliary graph is a finite forest of pieces used to count shared edges and close the constant. This combinatorial acyclicity argument supplies no probability law on spanning forests, transfer-current kernel, electrical-network statement, or MTP result. Keep it with G17's Euler/incidence and SAP-decomposition interface; it is neither a W07 source-count use nor evidence for G18. The L10 cross-scope record links to the original G17 use card without changing L09 files.


## L10 exact holds and planar geometry

- **Partial-book boundary.** PTN2026 is a partial book read; no positive theorem from its chapters is used as an active method in this guide. Its Chapter 11 label-domain issue is kept only as a non-counted boundary record, with the independent neutral review and L10 evidence at `expansions/20261115/reviews/R10/PTN11_neutral/` and `expansions/20261115/readers/L10/forests_revision/batch2/non_counted_boundaries/PTN2026_chapter11.md`. Do not use that chapter as a complete-book source or as positive quota evidence.
- For the weighted-triangle example, the transfer-resistance matrix is not itself the current matrix; the actual transfer current includes the edge conductance in its oriented edge coordinate. See the exact finite arithmetic output in `expansions/20261115/readers/L10/G18_determinantal_dependence/analysis/finite_transfer_check.json`; it checks a finite graph only.
- **Schramm planar UST scaling.** The 2011 Selected Works chapter reprints the 2000 Israel J. Math. paper. Theorem 10.7 (PDF p. 49 / printed p. 269) gives trunk/dual-trunk disjointness in planar subsequential UST scaling limits. Theorem 11.1 (PDF p. 61 / printed p. 281) assumes a C¹-smooth simple closed boundary. Theorem 11.3 (PDF pp. 63–64 / printed pp. 283–284) assumes Conjecture 1.2. These are two-dimensional scaling-limit results, not general infinite-network forest statements.
- **Aldous–Lyons and Alexander holds.** Aldous–Lyons Theorem 7.4 retains extremality, unimodularity, infinite sampled networks, and absence of an infinite critical cluster. Alexander Theorem 4.2(ii) concerns the locally `f`-minimax path `γ_(x,∞)`, not a “strict-critical cluster”; keep strict simultaneous uniqueness and the random Euclidean graph hypotheses.
- **Timár identity and WIT.** The read artifact is arXiv:1506.01370v3 (4 February 2016), although the bibliographic work is the 2018 Annals paper. Do not assert theorem-text equivalence with the journal version unless checked. WIT may delete an edge in `C_x∩B(x,r)^c`; it is not a local modification.
