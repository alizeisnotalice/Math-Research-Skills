---
name: probability-random-recursive-trees-asymptotics
description: Analyze asymptotic moments, profiles, fringe statistics, and limit laws for size-dependent or recursively grown random trees while preserving the construction, sampling rule, and theorem hypotheses.
---

# Random recursive-tree asymptotics

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

**Evidence state:** This immutable tool scope accepts 30 distinct complete works: 29 research articles and one complete standalone formal research chapter (RT007), not the edited book. RT025/RT026 count once. Exact scoped source decisions and coverage are retained with this release. Historical pending labels in reader records describe earlier snapshots. A127 fixed circular-separation joint law remains unproved.

Use this skill when a random-tree problem asks for height/profile moments, a fringe or additive statistic, pair distances/covariances, or a limit theorem. Start with the exact tree construction and statistic. Choose the proof route only after the model and sampling rule match the cited theorem.

**Input:** the tree family, its split/growth/offspring law, time or edge convention, label order, statistic/toll, sampling rule, and requested asymptotic. **Output:** the exact finite-size recurrence and boundary terms when available, a source-matched theorem with its hypotheses/constants/proof dependency, a model-specific transfer check, and any unproved interface. Keep numerical checks separate from proofs.

1. Fix the model: split/growth probabilities, rate or edge-length convention, rooted/ordered/unordered labels, toll/statistic, boundary values, and leaf/vertex sampling.
2. Write the exact finite-size recurrence, including the random child choice, hold time or edge increment, and any boundary term. Keep CTCS time-height (D_n), DTCS edge-height (L_n), maximum height and pair statistics separate.
3. Route by proof mechanism: recursive inequalities and Laplace transforms for height recurrences; harmonic descent and occupation probabilities for one-leaf chain laws; Mellin inversion for sharp one-leaf expansions; consistency/growth and exchangeable partitions for fringe structure; Markov-branching GHP limits only after verifying the weighted split-law hypothesis and leaf/vertex gate; contour and excursion methods for conditioned-GW pair-distance sums/profiles; indexed-profile covariance and width analysis for the exact RRT/BST level observable; function-valued contraction only for the source search-tree recurrence and stated parameter range; CMJ time changes for the RRT profile; fixed-fringe urn CLTs only under A1–A7 and spectral gates; split-vector toll, renewal, and pair-decomposition methods only after matching their source-specific tree construction; beta-splitting kernels only after an exact finite-n and label-order match; metric-tree limits only under the specified topology and sampling measure; finite-state conditioned-GW recursion only with coalescent spine coupling and its finite-variance hypotheses. Open [the method and model-gate reference](references/method.md) for dispatch rules; check [source status](references/sources.md) for R02-accepted source count and the remaining final-closure status. R02 now accepts RT007/RT037/RT042 within the 30-source stage; this source acceptance does not resolve A127, and final portable-scope hash closure/release approval remain pending.
4. Before transferring a theorem, check every hypothesis and variable match: tree family, label/order convention, time/edge metric, sampling design, admissible conditioning sizes, transform domain, moment/toll conditions, centering, variance, and asymptotic regime. Use [source cards and read coverage](references/sources.md) to locate the exact theorem, version, page, and proof chain.
5. Use local symbolic/numerical checks only to catch algebra, recurrence, or constant errors. Store the calculation and state that it is not a proof. The current reproducible checks are in [the W22 checks folder](evidence/W22/checks).

The current target A127 asks whether CTCS leaf heights of two leaves selected by a **uniform cyclic shift at specified circular separation** (r_n), with (log r_n/log n\to\alpha), have normalized covariance tending to (1-\alpha). Do not replace this with arbitrary label permutation, a pair sampled uniformly from all distinct leaves, a one-leaf CLT, or a branchpoint law for a random pair. The exact transfer gap is described in the method reference and the Beta-splitting cards.

See [positive examples](examples/positive.md) and [negative transfer examples](examples/negative.md) for a source-matched recurrence and two common failure modes.
