---
name: probability-nonlinear-law-dynamics
description: Analyze fixed points and iteration of probability-law operators, including nested stationary-law maps, nonlinear Markov updates, and recursive distributional equations; use when the proof needs operator-specific existence, uniqueness, stability, or global convergence.
---

# Nonlinear probability-law dynamics

Use this skill when a probability distribution is itself the state of a nonlinear map and the task concerns its fixed points, basins, stability, or iterates. Start by writing the exact operator, its domain, and its topology. Read [references/method.md](references/method.md) for operator typing and proof gates; consult [references/sources.md](references/sources.md) for the evidence ledger and source status. The checked patterns in [examples/positive.md](examples/positive.md) and [examples/negative.md](examples/negative.md) show the scope limits.

Keep these three operators distinct:

1. **Nested stationary-law map:** `Phi(theta) = pi(K_theta)`, where `pi(K_theta)` is the invariant law of a Markov kernel with parameter `theta` frozen. An inner mixing theorem is about iterating `K_theta` at one fixed `theta`; it says nothing by itself about the outer iteration `theta[n+1] = Phi(theta[n])`.
2. **Nonlinear Markov law update:** commonly `mu[n+1] = mu[n] K_{mu[n]}`, or a law-dependent continuous-time evolution. Use its results only after verifying that this is the same update as the target map.
3. **Recursive distributional equation (RDE):** `T(mu) = Law(g(xi, X_1, ..., X_m))` with independent copies `X_i ~ mu` and specified innovations. RDE contraction/classification tools apply only if the target operator has this representation or a proved reduction to it.

Separate fixed-point existence, uniqueness, local stability, convergence of every orbit, and almost-everywhere basin claims. Do not promote numerical behavior, a density-only result, an inner-chain rate, or a result for a special polynomial/RDE class into a theorem for a different law operator.

This owned revision preserves the original W21 modules and 31 complete full-text reads. The current R15 continuation now accepts all 31 distinct legacy source uses for their exact scoped interfaces under high-effort targeted review; it does not approve each whole legacy card. The scoped rows, hashes, and per-source limits are in the [portable source ledger](references/sources.md) and R15 union（本机附件：`evidence/review_authority/W21_all31_scoped_union.json`）. This adds no full reads or source-use credit. Historical R02 attribution remains low-effort; R13 v7 checked exact inheritance/preservation and was not a proof re-audit. R12 independently checked only the three local formulas W21-041/042/043. No W21 source is mapped to G21.01–.07, whose source credit remains zero. A121 remains conjectural outside exact source statements, and density-only criteria do not exclude singular or mixed full-support laws. The original screened candidate inventory has 38 works: 24 are full-text read and 14 remain candidate-only; five additional full-text method sources sit outside C001–C038. W21-001 and W21-002 are distinct works also canonicalized under W04. Five supplementary full-text sources remain method-specific and provide no A121/A122 representation by analogy. C020 remains unacquired; candidate-only records are not proof cards. Do not claim A121 or A122 is solved.


## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

## Added G21 method interfaces in this revision

This revision adds checklists for Markov-chain tree formulas, local stability, Lyapunov/recurrence arguments, order contractions, transfer operators, certified cycles, and semialgebraic basins. These are method gates, **not accepted theorem applications**: the current W21 read set does not supply a source for all seven new interfaces, and the new-method source credit remains zero pending exact primary-source reads and R13 review. See the [method gates](references/method.md#7-new-g21-method-interfaces-pending-source-review) and zero-mapping crosswalk（本机附件：`evidence/G21_new_method_zero_mapping.md`）.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。

## 归一化平方与尾质量

给定有限概率向量时，用[纯度更新证书](references/finite-purity-squaring.md)检查平方迭代中的缺陷下降与最大原子尾质量。小根分支要求当前缺陷严格小于 \(1/2\)。

## OpenAI 原稿中的方法

- [OpenAI tree-posterior components](references/openai-tree-posterior-components.md)
