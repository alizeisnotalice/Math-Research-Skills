---
name: probability-reflected-diffusion-coupling
description: Model and audit couplings of reflected diffusions when boundary geometry, the coupling class, coalescence, meeting tails, or Neumann spectra affect the proof.
---

# Reflected diffusion couplings

Use this skill to build or audit a reflected-diffusion coupling with explicit boundary behavior and quantitative meeting or spectral claims.

First specify one marginal: domain, drift, covariance, reflection directions, regulator support, and the Skorokhod convention at corners. Verify existence and uniqueness under a theorem that matches that exact model. Keep standard finite-variation Skorokhod problems separate from extended Skorokhod problems, whose constraining terms may have infinite variation.

Name the coupling class and check both path laws. For a co-adapted construction, identify the joint filtration and prove each declared driver is Brownian there. An unrestricted coupling needs correct marginal path laws but does not require a common-filtration Brownian representation. State the meeting time and whether the pair remains together afterward.

Keep three conclusions distinct: a boundary or Skorokhod theorem for one marginal, a coupling construction for two marginals, and an estimate on the meeting-time tail. A tail upper bound for a coalescing coupling can imply a total-variation upper bound. A Neumann eigenfunction instead supplies a necessary tail lower bound for any coupling that stays together after meeting. Neither direction constructs a coupling with a matching spectral rate. A killed-pair generator/spectrum argument applies only after selecting a Markov joint process and verifying its two marginals, product reflection rules, killing boundary, and spectral hypotheses; it does not make an unrestricted target coupling Markov.


## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).

## Method coverage

- **G16.01 — Skorokhod problems and local time:** specify the exact one-marginal reflection problem, regulator support, corner rule, and existence/uniqueness conditions.
- **G16.02 — Synchronous and mirror couplings:** name the coupling class, verify both path laws, and state the first meeting and post-meeting rule.
- **G16.03 — Neumann heat kernels and spectral expansions:** normalize the generator and distinguish survival lower bounds from coupling-tail upper bounds.
- **G16.04 — Poincaré variation and strict spectral bounds:** keep one-particle inequalities within their domain and eigenvalue hypotheses.
- **G16.05 — Nodal domains, reflection geometry, and domain comparison:** preserve the exact separating-barrier and mixed-boundary assumptions.
- **G16.06 — Coupled generators and killed-pair principal eigenvalues:** use only after selecting a Markov joint process and verifying covariance, both marginals, product reflection, killing, and spectral boundary conditions. The symmetric-interval supplement is accepted by R08 as a derived G16.06 method replacement on the already-counted Loper work; it does not narrow unrestricted coupling targets and adds no distinct source-work increment.

For proof details, read [references/method.md](references/method.md). The [source index](references/sources.md) contains source IDs, reviewed conditions, transfer limits, and the remaining Lundström–Önskög scope hold. Use [positive cases](examples/positive.md) and [missing-condition cases](examples/negative.md) to check transfers. Polyhedral sensitivity results are admitted here only in their explicitly reviewed special models; smooth-domain flow results do not settle polygon-corner behavior.
