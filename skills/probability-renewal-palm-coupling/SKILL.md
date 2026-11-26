---
name: probability-renewal-palm-coupling
description: Analyze renewal and Palm sampling, queue recurrence and stationary limits, and couplings that establish exact or total-variation convergence.
---

# Renewal, Palm, and coupling routes

Use this skill when a proof changes the sampling epoch of a renewal or queueing
model, establishes a stationary limit, or uses a coupling to claim convergence.
Start with the input law, full state, observation epoch, and requested
conclusion.  The retained source interfaces and their limits are in
[method notes](references/method.md) and [sources](references/sources.md).

## Keep the targets distinct

- Sampling identities and input-process limits do not construct a stationary
  queue law.
- Recurrence, fluid stability, tightness, and existence of a stationary
  solution have separate hypotheses.
- A path coupling, weak convergence, and total-variation convergence are
  different conclusions.  Exact coalescence requires an actual meeting time.

## Required checks

State all age, residual-life, phase, service, discipline, and environmental
coordinates that determine the conditional future law.  Do not call a
stationary-ergodic input Markov after adding only its last-event age.  Preserve
arrival-epoch, visit-epoch, cycle-biased, batch-biased, and arbitrary-time
laws as distinct distributions.

PASTA requires Poisson arrivals with its nonanticipation conditions.  An
epoch-specific PGF identity is conditional on the joint steady state it names,
and does not establish stability or an epoch conversion.  Use
[positive examples](examples/positive.md) and [negative examples](examples/negative.md)
to test a proposed transfer.

The **G10.05** Markov-renewal-kernel and **G12.05** periodic-phase or
singular-support routes have no accepted portable theorem interface.  Keep a
claim on either route conditional or open; an adjacent coupling theorem does
not fill the gap.  For **A006**, the G09 PGF/kernel route retains the
source-defined polling/server-arrival epoch, joint-steady-state assumption,
phase-specific joint PGFs, and the `F_2(z_1,0)` boundary term.  It proves
neither stability nor an epoch conversion.
For historical evidence kept outside the package, use
[the evidence guide](../math-research/references/evidence.md).
