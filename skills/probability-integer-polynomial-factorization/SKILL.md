---
name: probability-integer-polynomial-factorization
description: Analyze finite-support integer convolution and the unfair 0–1 polynomial factorization problem, including exact coefficient recurrences and bounded semialgebraic searches. Use when a 0–1 polynomial is factored into monic nonnegative real polynomials; epsilon-relaxations with signed factors require an explicit boundary check.
---

# Integer convolution and 0–1 polynomial factors

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

First translate the probabilistic statement exactly: supports may have gaps, factor coefficients are real and nonnegative, and “uniform” is on the support. Use the monic-factor convention (or positively rescale the two factors reciprocally to make both monic) when applying 0–1 factor results; raw nonnegative factorizations are scale-sensitive. Use [the method reference](references/method.md) for the probability-generating-function equivalence and bounded-search formulation.

Separate results for one proposed factor family from the general conjecture. Trinary propagation, Gröbner reduction, quantifier elimination, and finite degree enumeration can certify bounded instances; they do not settle an unbounded statement. Keep the coefficient domain explicit: an ε-relaxation allowing negative coefficients is not a counterexample to the nonnegative-factor problem.

Use [the source guide](references/sources.md) to check the source version, exact theorem boundary, read status, and pending literature. Follow [the positive example](examples/positive.md) for the support-aware generating-function reduction and [the negative example](examples/negative.md) to reject a signed-factor false counterexample.

**Evidence stage:** W18 has 37 complete A175 full-text reads; R06 accepted 33 as quota-eligible, while four full-text background sources remain excluded. M0147 is the sole partial read and does not count. The source ledger retains its review lifecycle fields; skill release still awaits final hash binding and the release decision.
