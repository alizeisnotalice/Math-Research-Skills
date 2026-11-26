---
name: probability-flow-poset-growth
description: Audit finite directed capacity flows, edge-disjoint path covers, Dilworth chain covers, LIS/RSK and sparse Poisson growth; keep boundary, model and double-limit hypotheses explicit.
metadata:
  short-description: Directed flow, posets and sparse growth
---

# Directed flow, poset covers and sparse growth

Use this skill when a problem connects a finite directed lattice max-flow to a path cover of defects, a finite poset chain cover, LIS/RSK, or a Poisson/Hammersley growth process. Start by fixing the exact finite graph, terminal sets, edge or vertex capacities, defect locations, and normalization.

Read [references/method.md](references/method.md) for the proof workflow and failure checks. Read [references/sources.md](references/sources.md) for source versions and each theorem's accepted scope. Use references/examples.md（本机附件：`references/examples.md`） for the continuum positive case and the exact finite counterexample.


## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).

## Required workflow

1. **Write the finite model.** Name the directed graph, source set, sink set, capacity law, and whether paths must be edge-disjoint or vertex-disjoint. Record all excluded corners and terminal overlaps.
2. **Apply finite flow duality only to the stated network.** Fulkerson's directed feasibility theorem supplies cut conditions and an integral-flow consequence under integral data. A lower-bound circulation with a return-arc cap k gives a derived finite decision test for covering all required marks in at most k edge-disjoint S–T paths; see its conditions and n=4 solver check in the method reference. Ford–Fulkerson (1956) is a separate undirected chain-flow formulation without an integrality claim; its one-chain-per-cut shortcut is planar-only. Menger's edge version counts edge-disjoint paths; its vertex version needs vertex splitting. None of these identifies the path-cover count with edge-poset width.
3. **Define the poset before invoking Dilworth.** Give the ground set and order. Dilworth equates width with a partition into chains for that finite poset. In the Aldous 4×4 boundary model, an exact reviewed counterexample has edge-poset width 5 but minimum edge-disjoint boundary-path cover 6. Thus the unrestricted finite equality is false for this order and terminal convention; chain comparability does not ensure simultaneous edge-disjoint extensions. Any revised theorem needs additional hypotheses or a quantified correction, plus exact terminal preservation. See the n=4 certificate（本机附件：`references/examples.md`）.
4. **Use LIS/RSK on the point-poset side.** Conditional on a Poisson count in a rectangle, coordinate ranks form a uniform permutation; an increasing chain is an LIS and the width is an LDS. State whether order reversal is being used and which Poissonized or fixed-size limit is invoked. Keep the two MMS (2023) interfaces separate: Theorem 1.1 treats bottom RSK rows for i.i.d. continuous input at fixed `k` and finitely many observation times; Theorem 2.2 gives its fixed-`k` total-variation decoupling; Corollary 1.4's raw local multi-line point sets use i.i.d. `Uniform(0,1)` coordinates with fixed `w∈(0,1)` and fixed observation windows (including only the paper's stated `w=1` boundary case). No growing-`k` or growing-window limit is claimed. Dauvergne–Nica–Virág are used here only for the finite deterministic càdlàg RSK/LPP isometry, the `W_t/G_t` inverse, and distinct ordinary/dual matrix embeddings; exclude the stochastic §7 Bernoulli Gibbs branch. None supplies a sparse edge-flow approximation.
5. **Keep classic HAD and other growth models separate.** Record jump rate, particle update, source/sink laws, drift, and initial condition. The classical source/sink process does not supply the invariant law of a drift-plus-jump process merely because both use a Poisson pull rule. Basdevant–Enriquez–Gerin–Gouéré’s discrete Bernoulli Hammersley models have their own strict/weak order and stationary boundary laws; they are neither continuous HAD nor A17.
6. **Audit every scale and limit order.** Distinguish a fixed-volume Poisson approximation from an error uniform enough in volume and defect density to exchange limits. Barbour–Brown's Palm bound yields `Σ q_e²` for independent Bernoulli marks on a fixed discrete support; it can grow with the number of sites and does not by itself control an unbounded path-cover functional. State boundary, orientation-mark, lattice-discretization, concentration, and diagonal-sequence costs.
7. **Use local mathematical tools for nontrivial algebra or finite examples.** Save code and exact output. Label finite enumeration and symbolic scaling as checks, not general proofs.
8. **Route undirected continuum-domain capacity flow as its own branch.** When the input matches that model, use §7 of [references/method.md](references/method.md) and carry the exact per-paper domain and terminal hypotheses. In particular, the Cerf–Théret LLN requires a bounded connected Lipschitz domain whose boundary is covered by finitely many mutually transverse oriented `C¹` patches, separated relatively open source/sink pieces, and null relative boundaries; “Lipschitz domain” alone is not enough. This branch gives no directed edge-poset path-cover transfer.

## A030 scope

Aldous’s discrete oriented-flow note defines the finite model and records the conjecture `1-v(p) ~ sqrt(2(1-p))`. AD95 supplies the continuum unit-intensity Poisson LIS constant 2; Dilworth gives the continuum point-chain cover consequence. These facts determine the continuum heuristic coefficient after the correct PPP scaling. The exact n=4 counterexample disproves the unrestricted finite edge-cover/poset equality; a sparse approximate bridge with controlled boundary cost and a uniform two-limit comparison remains unproved. See [references/method.md](references/method.md) and references/examples.md（本机附件：`references/examples.md`）.

## Historical provenance status

**Historical source audit.** All 30 required independent method-relevant works were accepted by R04; the source-count threshold was met and the R04 whole-entry science review passed. R04 accepted all 30 source-specific uses, including Boyd–Vandenberghe Chapter 5 as use 30: an L04-derived finite directed real-capacity max-flow/min-cut proof via LP duality. The book use reuses W19’s R08-accepted complete unit and claims no new full read. The Last–Penrose assigned chapters count as one book family; ADH §7.1 is only a model/condition/theorem-selection router and carries no Zhang proof/read credit. Cator–Groeneboom (2005) remains under the old R07 `needs_revision`; the n=4 counterexample is negative method evidence with zero source credit. The self-contained source/use index（本机附件：`references/source_use_index.json`） and provenance record（本机附件：`evidence/PROVENANCE.md`） carry the current evidence.

The accepted wave09 methods remain model-bounded. Temporal Dilworth is proved for temporal oriented trees and uses closed vertex-occupancy intervals; the paths in a path cover may overlap. Discrete Bernoulli Hammersley laws remain separate from continuous HAD and A17. Gaps 2019’s sparse theorem is continuous PPP with equal coordinate gaps only; the discrete theorem is a fixed-parameter Bernoulli-to-geometric **vertex**-LPP identity. Hassin’s positive finite-real criterion is a derived Farkas repair with zero potential difference on uncovered free arcs, not Theorem 4 verbatim and not an integrality result. DNV’s accepted use is finite deterministic RSK/LPP only; its §7 Bernoulli Gibbs branch is excluded. None yields the sparse A030 boundary-preserving edge-path bridge.

## Wave09 complete reads and accepted scoped uses

All five newly authorized works have complete page reads and source-specific freezes. R04 accepted all five; their exact scoped boundaries are recorded in the current cards and admission files.

- Chakraborty–Dailly–Foucaud–Klasing (2024): temporal oriented-tree path-cover/antichain equality through the temporal-connectivity/clique-cover reduction. Theorem 2 proof is pp. 7–11; closed vertex-occupancy endpoints count as intersections. No ordinary edge-disjointness transfer.
- Dauvergne–Nica–Virág (2021 v1): finite deterministic càdlàg RSK/LPP isometry and finite-time inverse via both `W_t` and `G_t` (Proposition 6.4); ordinary and dual matrix embeddings are kept distinct. The stochastic §7 Gibbs branch is excluded.
- Hassin (1981): derived finite-real grouped-circulation feasibility via Farkas, requiring `Bᵀt=Cᵀc` and zero potential difference on every uncovered free arc. No integrality or path decomposition.
- Basdevant–Enriquez–Gerin–Gouéré (2016): finite-box discrete Bernoulli Hammersley source/sink stationarity under two distinct strict/weak order and boundary-law conventions.
- Basdevant–Gerin (2019): continuous equal-gap PPP sparse scaling and a separate integer-threshold discrete Bernoulli/geometric vertex-LPP CDF coupling. No uniform Bernoulli diagonal or A030 transfer.

The 30-use source threshold is met, including the R04-accepted Boyd–Vandenberghe finite real-capacity LP-duality interface. It does not identify real flows with integer path families or prove the sparse boundary-preserving bridge. The unrestricted `n=4` width/path-cover identity is false; the uniform growing-volume `q↓0` comparison remains unproved.


## Accepted finite-flow LP-duality use

R04 accepted Boyd–Vandenberghe, *Convex Optimization*, Chapter 5 as G08 use 30. The complete chapter is reused from W19's R08-accepted reading, so this adds no new full read. The book supplies generic standard-form LP duality, strong duality for the feasible bounded network LP, and Farkas alternatives; the incidence formulation, multiplier elimination, potential clipping, and threshold-layer-cake identification of the finite directed real-capacity min-cut are derived here. The result is for finite nonnegative real capacities. It gives no total-unimodularity, integral-flow, Menger/path-decomposition, or poset edge-cover theorem and does not close the sparse A030 bridge. See the localized use card（本机附件：`references/use_cards/PR-2078d03826cd.md`） and local acceptance evidence（本机附件：`evidence/acceptance_index.json`）.
