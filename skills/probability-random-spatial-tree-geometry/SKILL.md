---
name: probability-random-spatial-tree-geometry
description: Analyze spatial-network routes, random-tree walks, and boundary measures after fixing the exact model, observable, bias convention, and sampling law.
---

# Random spatial networks, tree walks, and boundary measures

Use this skill after writing down the model and the quantity to be proved.  The
source-specific routes are in [method notes](references/method.md), with the
versioned source cards in [sources](references/sources.md).  These records
preserve selected theorem interfaces and their hypotheses.  They do not turn
the historical reading archive into a general theorem library.

## Select the model

- **Spatial networks.** Distinguish a specified route, a typical Poisson pair,
  a window pair-sum, a truncated sampled network, and a maximum over endpoints
  sharing one network.  A one-route mean or pair-summed bound gives no maximum
  bound.
- **FPP and Poisson roads.** Keep nearest-neighbour lattice FPP, Poisson-line
  roads, Delaunay or RNG geodesics, and finite-city optimization separate.
  State the sampling law, metric, and finite-window observable before using a
  source card.
- **Tree walks.** State whether the parameter weights a parent or children,
  how the root and added parent are treated, whether leaves are allowed, the
  offspring law and conditioning, and whether the conclusion is quenched or
  annealed.  Transience, speed, maximal-speed rates, and harmonic measure are
  separate conclusions.
- **Boundary and flow laws.** Identify the boundary, metric, bias direction,
  offspring support and moments, and environment transformation.  Invariance,
  equivalence, and ergodicity require separate arguments.
- **Poisson identities.** Specify the point-process law and whether occurrence
  indices or locations are distinct.  Mecke or deletion identities do not
  provide route independence, uniform integrability, or a tail bound.

## Transfer gates

Read [positive examples](examples/positive.md) for source-matched use and
[negative examples](examples/negative.md) when a hypothesis or target changes.
Numerical calculations certify only the stated finite arithmetic.  They do not
prove a spatial-network, random-tree, or boundary theorem.

Keep parent bias and child bias, deterministic bias and vertex-weight RWRE,
finite critical trees and infinite supercritical boundaries, and a fixed pair
and an iid endpoint family in distinct arguments.  A fixed-bias dimension
comparison does not imply bias monotonicity.  Equivalence of stationary laws
does not imply ergodicity.

For historical PDFs and evidence that are deliberately outside the installed
package, follow [the evidence guide](../math-research/references/evidence.md).
