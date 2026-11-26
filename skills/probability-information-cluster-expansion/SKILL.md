---
name: probability-information-cluster-expansion
description: Analyze entropy-rate variational problems, synchronization and deletion-channel capacity, renewal polling limits, and convergence of cluster or asymptotic expansions.
metadata:
  short-description: Entropy, deletion channels, renewal limits, and expansions
---

# Probability: information, renewal, and expansions

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill for information capacity with synchronization errors, entropy-rate variational arguments, renewal/regenerative limits in polling systems, and convergence questions for cluster or higher-order expansions.

## Active sources and historical provenance

Read [references/method.md](references/method.md) when working on a proof, asymptotic claim, or source-to-problem mapping. Use [references/sources.md](references/sources.md), `evidence/W16/reading_coverage.json`, and the source cards under the W16 dossier for exact theorem statements, physical-page coverage, and reading limits. The strict v2 source snapshot has 30 distinct source uses: 28 retained from the installed floor after excluding teaching fragments R02/R03, plus post-v1 R13 and Resing R07 canonical uses. R13 was separately accepted by R08; R04 accepted the canonical source uses in that snapshot. Neither reuse adds a new full-text read. The complete 324-page Gray book remains acquired; its full read unit is Chapter 2 §§2.1–2.7, with the separately partial Chapter 9 inspection retained. The old independent-review state is historical provenance only.

## Preserve the model

- Normalize information by input symbols when output length is random. State the input process class, deletion law, alphabet, logarithm base, and order of limits.
- For the binary deletion channel, do not assume the maximizing stationary input has independent run lengths unless the argument proves this. Near-capacity and stationary-source reductions have hypotheses and error terms.
- A finite-order asymptotic formula is not a convergent infinite series. In particular, Kanoria–Montanari establish the displayed expansion through the `d²` term with `O(d^(3−ε))` remainder for each `ε>0`; their higher-order coefficients and convergence question remain open in that source. Do not present the authors’ cluster-correlation heuristic as a proof.
- For general renewal arrivals, retain the age/residual-life state at polling epochs. Poisson large-switch-over limits do not automatically extend to renewal input, and simulations or a fluid heuristic do not prove the conjecture.
- A Gibbs, abstract-polymer, or virial criterion applies only after the target is represented in its stated model and every activity, stability, integrability, and incompatibility hypothesis is checked. The original Kotecký–Preiss source C01 is not readable in the current dossier; do not treat its withdrawn historical card as evidence. No such representation is established here for deletion-channel capacity.

## Calculation evidence

Use available local mathematical tools for coefficient checks, finite examples, optimization, and numerical exploration. Save runnable code and actual output with the work. Label these as numerical evidence; keep them separate from a proof of a limit, a tail estimate, or convergence.

## Examples

- [Positive example](examples/positive.md) shows how to handle the B051 higher-order/convergence question and A007 renewal polling question.
- [Negative example](examples/negative.md) shows common unsupported inferences to reject.
