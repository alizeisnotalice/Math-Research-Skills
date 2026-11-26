---
name: probability-percolation-renormalization
description: Analyze iid percolation, finite-range block arguments, bootstrap closure, and random-host propagation only after matching the model, observable, and hypotheses to an exact source interface.
---

# Percolation and renormalization methods

Use this skill for percolation events and related growth models after fixing the site or bond law, dependence, graph and boundary convention, update rule and clock, observable, and parameter regime. Select a source interface from the [source index](references/sources.md), then verify its listed hypotheses. [Method routing](references/method.md), [positive cases](examples/positive.md), and [negative cases](examples/negative.md) distinguish a transferable theorem from a finite consistency check.

## Model gates

- Independent bond/site percolation, oriented percolation, dependent edge laws, and random initial sets have different inputs. Marginals do not give product-measure positive association.
- Vertex bootstrap, graph-bootstrap edge infection, weak saturation, and probabilistic zero forcing have different rules and clocks. A legal sequential edge order does not give a synchronous-round trajectory.
- Specify whether the assertion concerns a critical point, finite-set sharpness, one-arm decay, chemical distance, occupation, cluster size, extinction, or stabilization time.
- A block proof needs its block event, separation range, bad-contour estimate, and a map back to the original model. Large block marginals alone do not give iid domination.
- An enhancement proof needs the signed Russo derivative and a uniform pivotal-surgery comparison. Monotonicity in an enhancement parameter does not imply monotonicity in the base site parameter.

## Source-matched routes

For independent sharpness, retain the source's finite-set criterion and weighted Russo/BK inequalities. Finite-range couplings are additionally needed for the recorded spatial-decay conclusion. For block geometry, retain the exact iid block law, conditional domination, repair step, and cluster-mass estimate. For bootstrap or random-host arguments, retain the host, threshold, seed model, boundary layer, scale, and whether the conclusion is sequential or synchronous. The [source index](references/sources.md) gives the available scoped routes and their excluded branches.

For a finite dual-contour Ising interface or a finite tree factor with private centered bits, read [the contour and bit-realization contract](references/finite-ising-contour-realization.md) and preserve its boundary, positivity, tree, and pin-incidence assumptions.

## OpenAI components

- [Annular screening and single-bit planar transfer](references/openai-wave4-pa3.md)
- [Finite percolation interfaces](references/openai-wave3.md)
- [Finite planar spin and percolation identities](references/openai-200-226.md)
