---
name: probability-analytic-endpoint-methods
description: Audit weak-type endpoints, Lorentz and Hardy endpoint methods, and Riesz-transform claims by matching exact input class, output norm, domain, and theorem hypotheses.
metadata:
  short-description: Endpoint theorem routing and scope checks
---

# Analytic endpoint methods

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when a proof or claim depends on a weak-type endpoint, weak-Lp/Lorentz bound, martingale endpoint inequality, Hardy-space endpoint, or Riesz-transform estimate.

## Historical provenance status

R01 approved the exact W25 mother set of 30 distinct papers and 686 physical pages. Source binding confirms identity, full-text evidence, cards, and coverage. It does not certify every theorem proof or erase source-specific defects. Check the per-source approval matrix and read the card before relying on a result; the prior standalone-candidate review state is historical provenance only.

## Workflow

1. Specify the operator and claim: scalar coordinate or vector norm; real or complex input; domain and measure; strong-Lp, weak-Lp/Lorentz, weak-(1,1), or Hardy-space output; strict or non-strict threshold; dimension dependence; and whether an upper bound or sharp constant is requested.
2. Route to the closest source method in [method selection](references/method.md). Verify every hypothesis in that source’s card, including core/domain, truncation, semigroup, weight, regularity, and normalization assumptions.
3. State separately (a) what the source proves, (b) any reader-derived correction or external input, and (c) the unproved interface needed for the target. A numerical/algebraic check is not a general proof.
4. Stop the transfer when the source and target differ in field, output norm, endpoint, geometry, or operator. Use the [source guide](references/sources.md) and [full-text cards](evidence/W25/cards/) for exact theorem/page/coverage details.

## Required boundaries

- A scalar-coordinate weak estimate, a vector weak-(1,1) upper bound, a martingale event estimate, weighted strong-L2, and a vector strong-Lp best constant are different claims. Never transfer a constant or sharpness statement across these classes without a theorem that does so.
- Formal C207 asks for the best vector strong-Lp constant for 1<p<∞. This evidence is auxiliary calibration only; it does not determine that constant.
- C208 remains an isolated dossier. No formal mapping, dimension-free scalar weak-(1,1) conclusion, or resolution is asserted.
- Keep source statements, errata, independently derived repairs, and proof deferrals attributed to the correct author. In particular preserve the AEP-020 correction’s leading factor 2 and its same-work status; the AEP-016 p<2 supplement; the CZ-03 squared-L2-factor gap; the weighted AEP-009 proof quarantine; the AEP-014 non-self-adjoint Proposition 3.8 gap; and the AEP-040 shift-vs-operator endpoint distinction.

## Evidence and examples

- [30-source guide](references/sources.md)
- [Exact method routing and hypotheses](references/method.md)
- [Positive route](examples/positive.md)
- [Condition-missing cases](examples/condition-missing.md)
- Source records, per-source R01 decisions, PDF paths/hashes, and page-level coverage: [evidence/W25](evidence/W25/)

The prior review-candidate designation is historical provenance only; use the scoped method and source cards above for this installed entry.
