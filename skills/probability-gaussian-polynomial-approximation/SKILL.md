---
name: probability-gaussian-polynomial-approximation
description: Analyze Hermite expansions, Gaussian polynomial moments and tails, anti-concentration, and approximation of Gaussian sign or indicator functions. Use when the input is a real polynomial under standard Gaussian measure; keep low-influence invariance and PTF boundary results within their stated hypotheses.
---

# Gaussian polynomial and Hermite approximation

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Fix the Gaussian normalization, total polynomial degree, and orthonormal Hermite basis before writing a tail or approximation claim. For a sign approximation objective, set $f=\operatorname{sgn}p$ and use $\mathbb E[(|p|-1)^2]=\|p-f\|_2^2$, handling the polynomial zero set under the stated Gaussian model. For Kane’s M0236 Gaussian PTF noise bound, restrict $\epsilon$ to $[0,1]$: the source coupling is defined through $\epsilon\le2$, but its displayed arcsin bound/proof only works through $\epsilon=1$.

Use [the method reference](references/method.md) to separate Hermite-tail lower bounds, anti-concentration estimates, chaos moment bounds, and PTF noise/surface-area bounds. For Hermite function/polynomial conversions, check the M0250 measure-versus-isometry discrepancy recorded there and in the source guide. An invariance theorem requires its independent-coordinate, moment-matching, degree, and individual-influence assumptions; it is not automatic for an arbitrary multivariate Gaussian polynomial. Consult [the source guide](references/sources.md) for exact theorem pages and the remaining reading queue.

Do not infer a sharp leading constant from a big-$\Omega$ Hermite-tail theorem or a one-dimensional trial polynomial. The B167 source states a sharp-constant problem; this stage derives only the $d^{-1/2}$ lower-order bound. The Gaussian kernel problem C168 is mapped here only as auxiliary Hermite-expansion context, not as a consequence of the B167 result.

## Historical provenance status

**Evidence stage:** 28 distinct full-text reads plus two R06-accepted canonical-use records give 30 tool-specific evidence entries. The W18 mother snapshot lacks a recorded final independent R06 hash binding; source rows may retain `review_status=pending` under the ledger convention. `evidence/W18/status.json` records the separate read and reuse counts. The former release-decision wording is historical provenance only.
