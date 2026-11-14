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

For USF end statements, keep the proof interface tied to its exact model. Morris’s conductance martingale is for weighted UST/FSF/WSF and its recurrence corollary assumes uniformly bounded edge conductances. Hutchcroft’s wired cycle-breaking dynamics prove WUSF one-endedness for transient reversible random rooted networks when \(\mathbb E[c(\rho)^{-1}]<\infty\); stationarity plus update-tolerance is the key step. Neither result is automatically a WMSF theorem. Hutchcroft–Peres component-graph ubiquity criteria concern USF on transitive polynomial-growth graphs: for $d_1\ge d_2\ge9$, ubiquity in dimension $d_1$ implies ubiquity in $d_2$, and the separating witness is ubiquitous only in the lower dimension. Their coarsening merges hyperedges while quotient merges vertices. Proposition 2.2 is only for its simultaneous distinct-component event: every prescribed set $K_i$ lies in one USF component, and those components are pairwise different. It does not give an unqualified product bound for arbitrary disjoint-set connection events. These results do not determine minimal-forest connectivity.

Hutchcroft’s interlacement Aldous–Broder Theorem 1.1 defines the oriented WUSF as $AB_t(\mathcal I)=\{-e_t(v):v\in V\}$: reverse the trajectory edge that first enters $v$, so the forest arrow points from $v$ to its predecessor. His WUSF one-endedness criteria are Theorem 2.1 with its anchored-isoperimetric integral conditions and Theorem 2.4 for transient unimodular random rooted networks; preserve the wired model and its hypotheses. In the recurrent unimodular **unweighted graph** setting, van Engelenburg–Hutchcroft prove equality of UST and graph end counts (Theorem 1, p. 3). Theorem 15 (p. 18) is the one-ended iff unique-harmonic-measure criterion; Proposition 12 (p. 16) is a one-sided lower bound from extremal measures to UST ends. For high-dimensional WUSF scaling, Theorem 1.5 requires controlled stationary measure, $d$-Ahlfors regularity for $d>4$, and Gaussian heat-kernel estimates. Theorem 1.6 additionally uses finite bubble norm and uniform ballisticity along with controlled stationary measure. Keep these assumptions, $q(v)$ lower-bound factors, past intrinsic/extrinsic diameter, volume, tree walk dimension, and avalanche quantities separate. None of these uniform-forest results supplies an FMSF/WMSF conclusion.

## 3. Electrical-network checks

For conductance $c(e)$, use resistance $r(e)=1/c(e)$. In a finite weighted UST, $\mathbb P(e\in T)=c(e)R_{\rm eff}(s,t)$, equivalently $C_{\rm eff}(s,t)=c(e)/\mathbb P(e\in T)$; an identity printed without $c(e)$ uses a fixed-edge unit-conductance normalization. State current orientation and normalization (unit current, unit voltage, or unit edge flow). In finite weighted UST, the distinct-edge determinant is the unnumbered Transfer Current Theorem in BLPS equations (4.4)–(4.5), PDF p. 12 (proof pp. 12–13); BLPS Theorem 4.1, p. 10, is the single-edge current identity. In the resistance-energy flow space of an infinite network, free current is the projection onto the cycle-flow orthogonal complement, while wired current is the projection onto the star-flow space. Accordingly FSF uses the projection-DPP kernel P_{Diamond^perp}, and WSF uses P_star. Check the weighted-coordinate convention and prove the relevant limit along the correct exhaustion.

Useful interfaces from the read textbook card:

- FSF=WSF iff currents are unique iff (HD=\mathbb R) (Theorem 10.14 / Chapter 9 equivalent).
- Equality of laws is not mutual singularity when the laws differ; PTN Corollary 10.19 requires that **every vertex** have an infinite orbit under the acting group for its mixing/ergodicity and singularity conclusion. Do not weaken this to “some infinite orbit.”
- Aldous–Lyons Theorem 3.1 for a fixed connected graph also requires finite normalizer (c=\sum_i |\mathrm{Stab}(o_i)|^{-1}<\infty); then the unique unimodular root law is proportional to inverse stabilizer Haar measure.
- For FUSF component indistinguishability on a unimodular random network, Hutchcroft–Nachmias require \(\mathbb E[c(\rho)]<\infty\). Their WUSF tail-property theorem has a different interface: stationarity and one-ended WUSF components.
- Planar duality exchanges free/wired boundary conditions and swaps conductance with resistance; it needs an actual plane dual satisfying the hypotheses.

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

Lyons's projection-DPP representation can encode a finite weighted UST by multiplying reduced-incidence columns by $\sqrt{c(e)}$. Teufl–Wagner supplies all-minors rooted-forest counts and a three-terminal identity, with broader determinant and resistance-reconstruction claims explicitly left conjectural. These are exact-law and electrical inputs for A141; neither addresses random disjoint witnesses or proves weighted-UST BK.

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
