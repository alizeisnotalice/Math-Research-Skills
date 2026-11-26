---
name: math-cycle-weighted-permanent
description: Compute finite Macdonald cycle-weighted permanents and their scalar normalizations exactly for rational q and t.
---

# Cycle-weighted permanents

For rational `q,t` with `q**j != 1 for every 1 <= j <= n`, compute
\[
 \operatorname{per}_{q,t}(A)=\sum_{\sigma\in S_n}\prod_{C\in\operatorname{Cyc}(\sigma)}\frac{1-t^{|C|}}{1-q^{|C|}}\prod_i a_{i,\sigma(i)}
\]
by exact permutation enumeration. This is appropriate for small supplied matrices, for testing a proposed specialization, and for checking the scalar factor
\(H_n=(t;q)_n/(q;q)_n\).

The calculator does not decide the all-size kernel or PSD positivity regions. For a source-derived sign claim, separately establish the applicable rank and parameter hypotheses. Read [the two source identities](references/macdonald-permanent-finite-identities.md) when those identities are used.

Run `python3 scripts/cycle_weighted_permanent.py examples/rank-one.json`.

## 文献复核采用的构件

- [Ryser identity by exact coefficient cancellation](references/ryser-coefficient-cancellation.md)

- [Paper I finite cycle sum](references/macperm1-finite-cycle-sum.md)
- [Paper II scalar normalization](references/macperm2-scalar-normalization.md)
