---
name: probability-percolation-renormalization
description: Analyze iid percolation, finite-range block arguments, bootstrap closure, and random-host propagation only after matching the model, observable, and hypotheses to an exact source interface.
---

# Percolation and renormalization methods

Use this skill for percolation events and percolation-style growth where the random model, update rule, geometry, and observable can be stated precisely. Begin by recording: (1) site or bond variables and their dependence, (2) the graph and boundary convention, (3) the update rule and clock, (4) the observable, and (5) the parameter range and limiting order. Then select a source interface from [the 30 scoped uses](references/sources.md) and check every listed hypothesis before transferring it.

This candidate is based on the original W05 baseline: 30 source uses received current independent high review for their individual scopes, with zero new full-text reads. The set comprises 29 complete research articles/manuscripts and one acquired monograph with complete use of Chapter 4. The signed admissions and exact evidence are in the evidence bundle（本机附件：`evidence/README.md`）. Historical W05 review was low; it is not counted as this round's high review.

For infection-witness workflows, use the separately installed `probability-infection-witness-methods` skill. This entry retains only the percolation-tool scopes listed in its source index; it does not import infection sources into the W05 baseline count.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

## Model and observable gates

- Independent bond/site percolation, oriented percolation, dependent edge laws, and random initial sets are different inputs. Marginals alone do not give independence or product-measure positive association.
- Vertex bootstrap, graph-bootstrap edge infection, weak saturation, and probabilistic zero forcing use different rules and clocks. A sequential legal edge order is not a synchronous-round trajectory.
- Distinguish a critical point, a finite-set sharpness criterion, one-arm decay, chemical distance, complete occupation, final cluster size, extinction time, and maximum stabilization time.
- For a block proof, specify its exact block event, separation/dependence range, bad-contour estimate, and map back to the original model. A high marginal for each block is not an iid domination theorem.
- For an enhancement argument, use the signed Russo derivative and verify the pivotal-surgery comparison under its stated uniform geometry. Do not infer monotonicity in the original site parameter just because the enhanced event is increasing in the enhancement parameter.
- For bootstrap closure, name the lattice/host, threshold, seed model, and whether the theorem concerns a finite box or an infinite system. Preserve the external layer, boundary, minimum-degree, and dimension hypotheses used in the proof.

## Proof routes supported by the reviewed source set

1. **Independent Bernoulli sharpness and product tools.** Use finite-set criteria and the source's correctly weighted Russo/BK inequalities on the stated independent models. Duminil-Copin–Tassion's accepted row uses the final finite-set inequality and isolates its intermediate display; exponential spatial decay requires finite-range couplings. Aizenman–Barsky's ghost-field route is limited to the source's summable-coupling class and small positive field. Kesten Chapter 4 supplies product coupling, FKG, and finite-coordinate Russo interpolation, not dependent-law FKG or an infinite-volume derivative interchange. See [individual scopes](references/sources.md#independent-product-and-sharpness-tools).
2. **Block renormalization and geometry.** Antal–Pisztora's chemical-distance estimate uses its specified iid nearest-neighbour blocks, conditional domination, bad-cluster repair, and exponential cluster-mass moments. Durrett's contour proof is for 1+1-dimensional oriented iid bonds and its explicit finite-range 1-dependence budget. Balister's admitted interface is the two-dimensional stable/forbidden-direction and local healthy-barrier recursion; the complete triangle-cover indexing branch is outside its current row. Never replace these model-specific hypotheses with high block marginals alone. See [block and contour scopes](references/sources.md#block-renormalization-and-path-geometry).
3. **Enhancement transport.** Let r(p,s) be a finite connection probability. The source's derivatives have signed form ∂p r=E(Np+)−E(Np−) and ∂s r=E(Ns+). A strict shift follows only after a separate uniform surgery comparison such as E(Ns+)≥g E(Np+) on the relevant parameter region and an integration along (p′,s′)=(g,−1). The reviewed AG91 interface is conditional; Grimmett's selected-problems article records the non-touching, exterior-uniform radius needed for the missing geometry as a negative boundary, not as a proved all-dimensional surgery theorem. See [enhancement scopes](references/sources.md#enhancement-conditions).
4. **Bootstrap and graph-host propagation.** Use each source's exact rule and size scale. The admitted papers cover the two-neighbour finite-size rectangle mechanism, critical update-family lower-time mechanism, selected Hamming-box blockers, synchronous graph-bootstrap bounds, fixed-density weak-saturation ordering, and the exact independent-mark exploration for G(n,p). The accepted Holroyd row contributes the integral/convex variational cost only, not the complete hierarchy-to-threshold chain. A graph-bootstrap upper bound from supersaturation is not a lower bound, and a weak-saturation ordering is not synchronous time. See [bootstrap and random-host scopes](references/sources.md#bootstrap-and-random-host-interfaces).

## Conditions, examples, and evidence

Read [method routing](references/method.md) before reusing an inequality. Check [positive examples](examples/positive.md) for scoped applications and [negative examples](examples/negative.md) for common assumption failures. They distinguish source theorems, reader-derived consequences, and finite computations. Computation files under `evidence/computations/` are finite consistency checks only.

The full per-source scope index links the approved card, exact local PDF, and independent R14 report. The historical source card and read-coverage record are archived separately and retain their original hashes. Do not promote excluded theorem branches in those historical cards to current high review.

For a finite Ising interface encoded by a dual contour, or a finite tree factor represented with private centered bits, read [finite Ising contour and bit realizations](references/finite-ising-contour-realization.md). It applies only with its stated boundary completion, finite tree, positivity, and pin-incidence conditions.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
