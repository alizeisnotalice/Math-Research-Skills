---
name: probability-renewal-palm-coupling
description: Analyze renewal and Palm sampling, queueing recurrence and stationary limits, and when a coupling yields exact or total-variation convergence.
---

# Renewal, Palm, and exact coupling

**Candidate status.** R06 accepted the complete G10/G11/G12 entry and cases for the exact 32 source/work-family scopes below. Format and relocation review is pending; this candidate is not installed. Three method-fit holds remain uncounted; Ferrari–Martin remains on its R07 read gate; Boon is boundary context; Zverkina has two printed K=k=2 polynomial-rate claims rejected in a scoped non-entry and no admitted method use.

Use this skill when a proof moves between renewal, Palm, cycle, or arbitrary-time sampling; establishes queue stability or a stationary limit; or uses coupling to claim convergence. First name the input law, the complete state, the observation epoch, and the requested conclusion. Keep these targets distinct:

- **G10:** convert among source-defined sampling laws or prove an input-process limit. These identities do not create a stationary queue law.
- **G11:** establish a stationary solution, recurrence, fluid stability, or tightness under a specific model and transfer theorem. These conclusions are not interchangeable.
- **G12:** compare specified processes, prove exact coalescence, derive a TV bound, or bound a dependence coefficient. Weak convergence and close paths alone do not prove meeting or TV convergence.

Choose a route in method selection（本机附件：`references/method_selection.md`）, then read its exact assumptions and limits in the accepted source/use index（本机附件：`references/accepted_scope_index.md`）. The machine-readable index is a 32-entry scope projection, not a replacement for the original admissions; each entry points to its exact R06 export and one-based row number, and records the source PDF hash, conditions, transfer limits, and review pointer. For detailed proof interfaces see [method notes](references/method.md) and, for coupling-specific cases, the G12 entry（本机附件：`references/g12_method_entry.md`）. Use the [positive examples](examples/positive.md) and [negative examples](examples/negative.md) to check whether the requested conclusion follows.

Do not treat an arbitrary stationary-ergodic input as Markov after adding only its last-event age. Add age, residual-life, phase, service, and discipline coordinates only when they determine the conditional future law; otherwise use a theorem stated for the original dependence structure. PASTA requires Poisson arrivals and its nonanticipation conditions. Preserve cycle-length and batch-size bias, and keep arrival-epoch, visit-epoch, and arbitrary-time statements separate.

Two positive-method gaps remain explicit: **G10.05** (Markov-renewal kernel) and **G12.05** (periodic-phase/singular-support method) have zero accepted source uses. Do not fill them with adjacent-topic sources.

For **A006**, L05 owns the G09 PGF/kernel method. L06 contributes only the named source-defined polling/server-arrival epoch after joint steady state is assumed, with phase-specific joint PGFs and the `F_2(z_1,0)` boundary term retained. No stability result or epoch conversion follows; see the A006 boundary note（本机附件：`references/method_selection.md`） and W14 method revision（本机附件：`references/a006_boundary.md`）. A020 remains with L08; A027/A127/A137 tree and spatial proofs remain with L11/L12.

## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).
