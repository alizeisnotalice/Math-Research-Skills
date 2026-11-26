---
name: probability-stochastic-geometry-localization
description: Prove or audit Poisson growing-ball cover-time and spatial-network localization claims, including measure optimization, Poissonization, and boundary tails, while checking the exact model and transfer hypotheses.
---

# Stochastic geometry, coverage, and localization

Use this skill for growing-ball Poisson cover processes, optimization of their seed law, or asymptotics of random spatial-network spans. Choose the route by the point-process law and the observable. Read the method gates（本机附件：`references/methods.md`） for the relevant proof obligations and [the source ledger](references/sources.md) for source status.

## Historical provenance status

**Historical source audit:** R12 checkpoint 2 accepts a deduplicated union of 31 distinct work families and 31 distinct PDFs for this skill; all 341 path/hash bindings pass. The source13 addition is one narrow G22.02 Poisson-energy interface. The exact source/use conditions are in [the 31-row source ledger](references/sources.md), bound matrix（本机附件：`references/source_bound_matrix.json`）, and scope snapshot（本机附件：`evidence/entry_scope.json`）. Five method IDs still lack an accepted source row: G22.05, G22.06, G24.03, G24.05, and G24.06. Keep them as explicit gaps or conditional gates. B42 support remains 0. Source12 Thm.3.3 remains limited to deterministic local deletion-cost; its [1]/[19] tail dependencies remain unverified. A124, A125, A136, and A137 remain open. The former whole-entry, publication, and installation state is historical provenance only.

1. **Growing-ball cover (G22):** write the marked Poisson process as `dt × μ(dx)`, specify growth speed, metric, boundary, and cover time. Separate the probability one fixed point remains uncovered from the event the entire space is not covered. For measure optimization, establish existence and prove the exact averaging inequality for the cover-time functional before concluding that Haar measure is optimal.
2. **Spatial network (G24):** identify the actual SIRSN or other network law, endpoint sampling design, shared network realization, finite-window observable, and normalization. Do not infer stabilization from stationarity, isotropy, scaling, or finite intensity.
3. **Poisson-to-fixed-size transfer:** state the Poisson functional and fixed-k functional separately. Prove a coupling or de-Poissonization estimate for the target observable, then control window-exit routes, boundary contributions, and uniform integrability before transferring expectations.
4. **Unresolved maximum:** for a countable family of endpoints in one network, keep a one-route marginal, finite pair expectation, and the supremum over all endpoints as separate random quantities. Without a proved maximal or tail estimate, preserve the open status.

The skill does not cover recursive-tree two-leaf limits; route A127 to `probability-random-recursive-trees-asymptotics`. See [positive usage](examples/positive.md) and [negative transfers](examples/negative.md).

## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).
