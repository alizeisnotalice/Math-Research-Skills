---
name: probability-markov-spectral-mixing
description: Analyze finite reversible Markov-chain mixing and spectral gaps, especially heat-bath Glauber dynamics for ferromagnetic Ising models; use when a claim depends on update clocks, graph geometry, or correlation inequalities.
---

# Markov spectral gaps and Ising Glauber dynamics

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill for finite-state reversible-chain spectral-gap or mixing questions, with focused guidance for Ising heat-bath Glauber dynamics and equilibrium GKS/FKG/Holley inequalities. This research pack is an interim distillation: 33 source records include 31 candidate records, 31 local PDFs, 28 completed full-paper reads, two books with complete selected reading units, one targeted partial cross-tool read, and two unread metadata-only Griffiths records. The documented evidence tally is 28 full papers plus two books with fully read selected units (30 source units); W04S025's specific A121/A122 mapping relevance remains for R02's independent determination. The source ledger remains reader-side pending; independent decisions are authoritative. There is no separate 30-full-text-paper target.

Before applying a theorem, pin down the state space, Gibbs law and fields, update rule, vertex rates, and discrete-time versus continuous-time convention. Write the generator or kernel and its Dirichlet form explicitly; compare gaps only under a common clock. Read [references/method.md](references/method.md) for exact formulas and correlation-inequality hypotheses.

For Ising edge-parameter claims, distinguish stationary correlation monotonicity from finite-time behavior and from eigenvalue monotonicity. A040 remains open here for arbitrary finite graphs: Nacu verifies cycles at zero field. Kargin's printed theorem states a uniform-field homogeneous result, but the audited proof's reflection step `f_k=−f_{n−k}` is justified here only at zero field; the nonzero-field proof remains unresolved and is not treated as a refutation. Shirai's counterexample concerns a stronger fixed-time spin-expectation claim, not the spectral-gap question. Use [references/sources.md](references/sources.md) for theorem scope and page locators; the examples show correct and incorrect transfers.

Treat finite enumeration, floating-point eigensolvers, and high-precision point checks as search evidence only. They can locate candidate behavior but cannot prove an all-graphs theorem. For the saved MATLAB scan and its precise limits, see `evidence/W04/numerical/a040_scan.json` and `evidence/W04/numerical/a040_exact_chain_scan.m` in the project.
