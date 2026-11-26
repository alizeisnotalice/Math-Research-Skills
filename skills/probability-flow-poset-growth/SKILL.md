---
name: probability-flow-poset-growth
description: Audit finite directed capacity flows, edge-disjoint path covers, Dilworth chain covers, LIS/RSK and sparse Poisson growth; keep boundary, model and double-limit hypotheses explicit.
metadata:
  short-description: Directed flow, posets and sparse growth
---

# Directed flow, poset covers and sparse growth

Use this skill when finite directed lattice flow is related to defect path covers, finite-poset chain covers, LIS/RSK, or Poisson/Hammersley growth. First fix the graph, terminals, capacities, defect set, path-disjointness convention, boundary, and normalisation. Read [the workflow](references/method.md) and [source scopes](references/sources.md).

1. Apply integral directed-flow duality only to the stated network. Edge-disjoint and vertex-disjoint paths require different formulations. A return-arc lower-bound circulation is a finite decision test under its own conditions.
2. Define the poset before applying Dilworth. Comparability does not yield simultaneous edge-disjoint extensions. The unrestricted edge-poset/path-cover identity fails for the audited boundary convention, so retain exact terminal data.
3. Use LIS/RSK only on the point-poset route. State the conditioning, order direction, fixed parameters, observation windows, and which Poissonised or fixed-size limit is used. Do not convert fixed-window results into growing-window statements.
4. Separate continuous HAD, discrete Bernoulli Hammersley, and drift-plus-jump processes by their update law and boundary condition.
5. Audit every limit order. A fixed-volume Bernoulli-to-Poisson approximation need not control an unbounded path-cover functional or permit exchange of density and volume limits.

Run a local exact calculation for nontrivial finite algebra and label it as finite evidence. Use the [central evidence guide](../math-research/references/evidence.md) to locate historical certificates when a source card calls for them.
