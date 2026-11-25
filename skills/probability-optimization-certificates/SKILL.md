---
name: probability-optimization-certificates
description: Build and audit finite-dimensional optimization bounds and proof certificates used inside probability arguments, including duality, interval validation, and exact LP/MIP checks.
metadata:
  short-description: Certified optimization bounds for probability proofs
---

# Probability optimization certificates

Use this skill when a probability argument relies on a finite LP, convex program, SDP, or integer program as a rigorous bound or computational certificate. Keep the encoded finite problem distinct from the stochastic, asymptotic, or infinite-dimensional statement it is intended to support.

First record the objective direction, variables and domains, all constraints, coefficient type, sign conventions, and the precise claim being certified. Derive weak duality for that model. Treat strong duality, attainment, complementary slackness, minimax exchange, and convergence as separate claims with their own hypotheses.

Treat solver output as a candidate. For rational finite models, check feasibility, signs, branch coverage, certificate identities, and objective gaps with exact arithmetic where practical. For floating-point input, use outward-rounded intervals or a proved residual bound. Report exploratory numerics separately from exact or interval-certified evidence. An exact finite certificate says nothing by itself about a model encoding, an all-size theorem, or a limit.

For conic and polynomial models, identify the cone, dual cone, compactness or Archimedean assumptions, face-reduction conditions, degree, and relaxation order. SOS is an SDP certificate; DSOS/SDSOS are conservative inner certificates. In branch-and-bound, prove that pruning preserves a globally minimizing point or covers every feasible integer branch.

Read [references/method.md](references/method.md) for detailed certificate routes and failure boundaries. Use [references/sources.md](references/sources.md) for the exact source identities, accepted theorem scopes, page locators, and evidence links. The original W19 baseline has 30 current R04 high-reviewed scoped uses (29 complete papers and one acquired book with complete Chapter 5 read). Six existing R15 G32 uses are listed separately and do not substitute for or enlarge the original baseline count. Source-by-source scopes, not the mere presence of a PDF or a source-wide citation, govern transfer.

For finite infection or online-selection encodings, state the finite item set, variables, domains, constraints, objective direction, rounding convention, and checker. A certificate for that encoding does not establish that it models the desired process. Use the exact finite cover, interval, SOS, Sturm, SAT/SMT, Krawczyk, and enumeration interfaces only within the conditions in [the method guide](references/method.md) and the accepted scoped records in [the source register](references/sources.md).

The [positive cases](examples/positive.md) and [negative cases](examples/negative.md) give executable rational certificates and common missing-condition failures. The cases verify only their displayed finite instances.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
