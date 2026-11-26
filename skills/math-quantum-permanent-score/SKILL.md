---
name: math-quantum-permanent-score
description: Check finite partition-score lower bounds from a supplied nonnegative orbital coefficient profile.
---

# Quantum-permanent score certificates

For a supplied rational probability distribution on partitions of `n`, evaluate the score
\[
 \sum_{\lambda\vdash n}\frac{(-1)^{n-\ell(\lambda)}}{\binom n{\ell(\lambda)}}w_\lambda.
\]
Use integer or rational-string weights and plus-separated partition labels. Different part orders are accepted for a single label, with one weight per underlying partition.

If the supplied square-free weight meets \(w_{(1^n)}\ge n!/n^n\), it also returns the resulting elementary lower bound.

The caller must establish that the profile comes from a positive bistochastic map. This checker does not establish the orbital-polynomial reduction, the square-free floor, or any map-realizability statement. See [the source scope](references/quantum-permanent-score.md).

Run `python3 scripts/quantum_permanent_score.py examples/n3-floor.json`.
