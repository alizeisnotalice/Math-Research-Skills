---
name: probability-stationary-law-interfaces
description: Prove or audit stationary laws for Markov environments, tree flows, interacting systems, and drift-jump processes through generator, flux, coupling, Palm, regeneration, or prefix methods.
---

# Stationary-law interfaces

Use this skill to turn a proposed invariant distribution into a theorem with a
specified state space, transition rule, domain, normalization, and proof
route.  Read [method notes](references/method.md) and [sources](references/sources.md)
for source-specific hypotheses and limits.

## Identify the object and conclusion

State whether the object is a discrete kernel, continuous-time semigroup,
rooted environment chain, flow-rule subtree chain, induced return chain, or
finite-prefix projection.  Name the measurable state space and sigma-field.
For random trees, record the offspring law, survival conditioning, root
convention, and quenched or annealed law.

Stationarity, reversibility, ergodicity, uniqueness, and existence are distinct
conclusions.  Equivalence to a reference measure does not imply ergodicity.

## Proof gates

1. A generator identity \(\int Lf\,d\mu=0\) needs a core or domain,
   non-explosion or conservativeness, well-posedness, and integrability before
   it implies invariance.
2. For drift-jump systems, account for every boundary, collision, cut, and jump
   convention.  Include incoming and outgoing fluxes and the relevant trace
   terms.
3. A coupling, Palm, queueing, or regeneration construction must specify the
   map, rates, conditioning, stability, normalization, and return-time or
   holding-time integrability.  A Palm construction from an assumed stationary
   process does not establish existence of that process.
4. For prefix limits, prove semigroup intertwining and compatibility of both
   laws and transition kernels before Kolmogorov extension.  A stationary path
   process also requires compatible path laws and stated regularity or
   tightness conditions.
5. For a tree flow, define it on every descendant tree and check all child
   masses.  Strict child positivity, when required by the source, cannot be
   weakened to mere measure equivalence.

## Source-specific limits that remain active

- For the LPP Galton--Watson rerooting chain, Theorem 3.1 supplies
  stationarity and reversibility; path-shift ergodicity requires its later
  induced last-exit/tower argument, not Theorem 3.1 alone.  The
  equivalence-only flow question (A027) remains open when strict first-child
  positivity is absent.
- **G20.04** is available only for the stated Behme--Schnurr CIR example, and
  **G20.05** only for the Ferrari--Landim--Thorisson spatial Poisson
  replacement model.  They do not license generic generator, jump-core, or
  coordinate-prefix claims.  The G19.05 cocycle route and A17 positive-law
  transfer remain unsupported.
- A jump-law or reverse-process argument needs its displayed finite-flux or
  finite nonzero invariant-measure premise; do not infer it from stationarity.
  For the Holderrieth route, use only the bounded-rate, proper-jump,
  independent-core repair rather than its invalid differentiability shortcut.

Use [positive](examples/positive.md) and [negative](examples/negative.md)
examples to test the route.  The source-matched finite tools
[dyadic chord energy](references/dyadic-chord-energy.md) and
[departure-row factorization](references/departure-row-factorization.md)
address only their displayed preparatory tasks.

For historical materials outside this package, use
[the evidence guide](../math-research/references/evidence.md).
