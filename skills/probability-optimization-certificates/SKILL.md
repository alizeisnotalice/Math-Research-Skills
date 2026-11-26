---
name: probability-optimization-certificates
description: Assemble and audit a finite optimization certificate inside a probability proof after the stochastic model, encoded finite problem, proof type, and remaining transfer are explicit.
metadata:
  short-description: Certificate assembly for probability proofs
---

# Probability optimization certificates

Use this skill when a probability argument needs a finite optimization encoding **and** a ledger explaining what the certificate proves about the stochastic model. It is an assembly and transfer skill, not the default implementation route for every LP, SDP, moment problem, interval computation, or integer program.

First freeze the finite item set, variables/domains, objective direction, coefficient type, sign conventions, rounding, and precise encoded claim. Separately state the model-to-process reduction and every unproved stochastic, asymptotic, infinite-dimensional, convergence, minimax, or attainment step. A certificate for the encoding does not establish that the encoding models the desired process.

## Choose the proof type before an algorithm

Read [the proof-type taxonomy](references/proof-type-taxonomy.md), then delegate the certificate kernel:

- exact rational residuals, finite LP/cone primal-dual witnesses, or directed interval enclosures to [L03](../math-l03-rational-and-interval-certificates/SKILL.md);
- quadratic/rank/PSD lift, Shor SDP, or rank-one recovery to [C01](../math-c01-semidefinite-lifting/SKILL.md);
- unknown-law generalized moment measure, conditional ratio, or measure-level attainment/duality to [B03](../math-b03-generalized-moments/SKILL.md);
- fully enumerated Boolean/count/marginal moment laws with pointwise polynomial duals to [finite moment duality](../probability-moment-polynomial-duality/SKILL.md); and
- polynomial SOS/moment hierarchies to [moment-SOS certificates](../math-c03-moment-sos-certificates/SKILL.md).

For a finite cover, MIP, branch tree, SAT/SMT, Sturm, Krawczyk, or source-specific probability encoding, retain this skill's [method guide](references/method.md). Check exact feasibility, signs, branch coverage, certificate identity, and objective direction; solver output is only a candidate. Treat strong duality, attainment, complementary slackness, relaxation exactness, and limiting transfer as separate claims.

## Evidence and source scope

[Source records](references/sources.md) govern theorem-specific use; the original W19 baseline has 30 current R04 high-reviewed scoped uses, while six prior R15 G32 uses remain supplemental. [Positive](examples/positive.md) and [negative](examples/negative.md) cases are executable finite examples only. See [evidence access](../math-research/references/evidence.md) for local attachments.
