---
name: probability-stochastic-geometry-localization
description: Prove or audit Poisson growing-ball coverage and spatial-network localization claims while checking the point-process model, observable, and transfer conditions.
---

# Stochastic geometry, coverage, and localization

Use this skill for a Poisson growing-ball cover process, seed-law optimization,
or spatial-network span/localization problem.  State the point-process law,
growth speed, metric, boundary, observation window, and target observable.
The scoped source interfaces and their hypotheses are in
[sources](references/sources.md).

## Choose the route

1. **Growing-ball coverage.** Write the marked process as `dt × μ(dx)`.  Keep
   the event that one fixed point remains uncovered separate from failure to
   cover the whole space.  An optimality statement for Haar or another seed law
   needs existence and the exact averaging inequality for the cover-time
   functional.
2. **Spatial networks.** Identify the particular SIRSN or other network law,
   endpoint sampling, whether one network realization is shared, the finite
   window observable, and normalization.  Stationarity, isotropy, scaling, or
   finite intensity alone do not give stabilization.
3. **Poissonization.** State the Poisson and fixed-size functionals separately.
   Supply a coupling or de-Poissonization estimate, control boundary and
   window-exit terms, and establish the required uniform integrability before
   transferring expectations.
4. **Maxima.** A one-route marginal and a finite pair expectation do not bound
   the supremum over countably many endpoints in one network.  Preserve the
   maximum as open until a maximal or tail estimate is proved.

This skill excludes recursive-tree two-leaf limits.  Route that problem to
`probability-random-recursive-trees-asymptotics`.  Use
[positive examples](examples/positive.md) and [negative transfers](examples/negative.md)
to check the model match.

The **G22.05**, **G22.06**, **G24.03**, **G24.05**, and **G24.06** method
branches have no accepted portable source interface; leave them conditional
instead of filling them from an adjacent coverage or network result.  The
open A124/A125/A136/A137 transfers remain outside this skill.  In particular,
**A127** is the excluded recursive-tree route above, not a spatial-network
consequence.

For historical PDFs and evidence held outside the installed package, use
[the evidence guide](../math-research/references/evidence.md).
