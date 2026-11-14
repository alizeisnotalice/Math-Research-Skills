---
name: probability-queueing-heavy-traffic
description: Analyze queueing-network stability and heavy-traffic limits using fluid/Lyapunov methods, polling models, state-space collapse, BAR, and reflected diffusions.
---

# Queueing stability and heavy traffic

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when a problem depends on queueing stability, polling disciplines, heavy-traffic scaling, SSC, a basic adjoint relationship (BAR), or a reflected Brownian limit. Start by fixing the state, observation epoch, arrival/service assumptions, and the exact stability or convergence notion. Do not transfer a result across a change in discipline, input dependence, CRP status, or limit mode without proving that interface.

Read [references/method.md](references/method.md) for the proof routes and domain-specific checks. Read [references/sources.md](references/sources.md) for the 44-source evidence index, each item's reading status, and the physical-page coverage map for complete reads. Full-text PDFs from the D01 handoff are linked in the source index. The corresponding source cards are in `evidence/W14/cards/`; fulltext copies, when present, are in `evidence/W14/data/`.

For transform or diffusion work, derive the generator/steady-state identity from the actual model and boundary convention before solving it. Keep the probability-derived transform class distinct from a larger analytic function class. Treat finite-dimensional numerics as consistency checks only; do not use them as a stability proof, a limit theorem, or a transform-uniqueness argument. See [examples/positive.md](examples/positive.md) and [examples/negative.md](examples/negative.md) for scope checks.

For B054 Eq. (7), state the intended uniqueness class explicitly: the literal Eq. (8) analytic class has a scalar-normalization ambiguity, the augmented analytic class adds \(L(0)=1\), and probability-admissible uniqueness also requires transform positivity/support and unused-service boundary-measure conditions. The scaling observation identifies a source-formulation gap; it does not solve the intended probability-class problem.

This skill's direct open-problem coverage is A006, A007, A008, A011, B054, and B157. Its cited literature is an evidence snapshot from 2026-11-14; open/solved status needs fresh source verification before reuse.
