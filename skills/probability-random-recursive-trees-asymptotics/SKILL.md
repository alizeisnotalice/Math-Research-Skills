---
name: probability-random-recursive-trees-asymptotics
description: Analyze asymptotic moments, profiles, fringe statistics, and limit laws for size-dependent or recursively grown random trees while preserving the construction, sampling rule, and theorem hypotheses.
---

# Random recursive-tree asymptotics

Use this skill for height and profile moments, fringe or additive statistics, pair distances or covariances, and random-tree limit laws. State the tree construction, split or offspring law, time or edge convention, labels and order, statistic or toll, sampling rule, and requested asymptotic. Read [method and model gates](references/method.md) for the compatible proof route and [source ledger](references/sources.md) for theorem-specific versions and hypotheses. [Positive](examples/positive.md) and [negative](examples/negative.md) examples show source-matched recurrence and transfer checks.

Write the exact finite-size recurrence before applying an asymptotic result. Keep CTCS time-height, DTCS edge-height, maximum height, one-leaf observables, and pair statistics separate. Match the source's construction, leaf or vertex sampling, label order, conditioning sizes, transform domain, moment conditions, centering, variance, and limiting regime.

Use recursive inequalities or Laplace transforms only for the stated height recurrence. Use Mellin inversion for the source's one-leaf expansion. Use Markov-branching, contour, excursion, urn, contraction, CMJ, renewal, beta-splitting, or metric-tree tools only after their split law, topology, sampling measure, and moment assumptions match. The source ledger records restricted uses and excluded transfers.

The A127 target concerns two CTCS leaves selected by a uniform cyclic shift at prescribed circular separation. The cited heuristic does not prove its fixed-gap covariance claim. A uniformly chosen pair, arbitrary label permutation, one-leaf CLT, or random-pair branchpoint law does not supply that missing dependence argument.

Local symbolic or numerical checks may catch recurrence or constant mistakes. They do not prove an asymptotic theorem.
