---
name: probability-bandit-information-bounds
description: Analyze stochastic bandit regret and best-arm identification using KL change of measure, structured alternatives, RKHS confidence regions, and sampling allocations; use for direct Bernoulli-mean kernel bandits or fixed-budget versus fixed-confidence distinctions.
---

# Bandit information bounds

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when deriving or checking bandit regret/sample-complexity bounds, Bernoulli-KL confidence regions, structured RKHS allocations, or fixed-budget best-arm identification.

Start by writing the exact feedback model, objective, action set, and function/parameter class. Keep direct Bernoulli mean observations \(Y\sim\mathrm{Ber}(f(x))\) separate from logistic observations \(Y\sim\mathrm{Ber}(\sigma(g(x)))\), and from additive subgaussian RKHS observations \(Y=f(x)+\epsilon\). Do not transfer a theorem across these models without proving the link and noise assumptions.

For a lower bound, define the alternatives that change the decision of interest, factor trajectory KL into expected action counts and per-action KL, then solve the resulting allocation problem. For a structured bandit, the alternative set must preserve the stated structure. Check uniqueness and oracle assumptions before applying asymptotic optimal allocation results.

Distinguish cumulative-regret asymptotics, finite-time regret, fixed-confidence stopping complexity, and fixed-budget error exponents. The current B056/OSSB crosswalk is a candidate transfer with unresolved interfaces, not a claim that B056 is solved. Read the relevant protocol in [method.md](references/method.md); source roles and evidence status are in [sources.md](references/sources.md). See the [positive](examples/positive.md) and [negative](examples/negative.md) model-transfer examples.
