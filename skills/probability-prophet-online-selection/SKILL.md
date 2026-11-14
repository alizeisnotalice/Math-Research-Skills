---
name: probability-prophet-online-selection
description: Analyze prophet inequalities, optimal thresholds, online resource allocation, and stochastic matching while preserving the arrival model and benchmark.
---

# Prophet inequalities and online selection

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when an online policy selects random rewards or allocates limited resources, especially when the claim compares it with an offline prophet, a fluid/ex-ante LP, or an omniscient dynamic benchmark.

Before transferring a theorem, write down (1) independence and distribution knowledge, (2) arrival order and who controls it, (3) capacity and whether decisions are irrevocable, (4) policy class, and (5) the exact denominator. These determine whether a quoted constant applies.

For the assigned A001/A002/A005 and online-allocation problems, the current evidence and unresolved interfaces are in [method.md](references/method.md), with source-by-source acquisition and reading status in [sources.md](references/sources.md). R07 independently approved 30 complete paper reads and one fully acquired book with complete selected Chapters 1 and 3, totaling 31 eligible sources. See the [final R07 review](evidence/review/review.json) for the exact version binding. Reader-ledger pending labels are retained as historical declarations; publication metadata is certified only where explicitly recorded. Partial and unread sources are excluded from the completed-source quota. `sources.json` preserves the full assigned M0034–M0090 ledger and 19 supplements.

## Non-negotiable distinctions

- Do not interchange IID, independent non-identical, random permutation, adversarial fixed order, and freely selected order. State whether policies are adaptive or static.
- Name the comparator: expected offline top-k prophet, online dynamic optimum, ex-ante/flow LP, or omniscient long-run reward-rate. Approximation ratios across different denominators are not directly comparable.
- In threshold arguments define strict exceedance counts explicitly. If distributions have atoms, state the tie convention or random tie-breaking probability.
- Keep a limit for one fixed distribution separate from an infimum over distributions that may vary with n. Do not infer termwise monotonicity from an equality of limit and infimum.
- A conjecture, open problem, finite numerical search, or first-page bibliographic inspection is not a theorem. For computational evidence, run the exact finite model where possible, save code/output, and label it numerical or finite-instance evidence.
- For matching and OCRS, specify the resource feasibility family, batch/arrival process, correlation assumption, and adversary model. Dynamic matching with departures, one-shot online matching, and static resource allocation use different state spaces and benchmarks.

When using an exact result, record the theorem/proposition number, PDF and printed page if both exist, all quantifiers and hypotheses, and the precise inequality. See the positive and negative examples for the A002 calibration and model-transfer checks.
