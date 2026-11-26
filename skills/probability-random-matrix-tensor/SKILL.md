---
name: probability-random-matrix-tensor
description: Prove or audit random matrix and tensor norm bounds, Banach type-2 estimates, and noncommutative martingale inequalities. Use when the norm, covariance model, or row/column square-function assumptions need precise source-based checking.
---

# Random matrices, tensors, and noncommutative martingales

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when a problem combines random matrix/tensor series, injective norms, Banach-space type constants, or noncommutative martingale square functions. First fix the random model and the norm; the available estimates change when either changes.

Before moving a theorem between formulations, record:

- tensor order (r), geometric exponent (p), and (if present) a separate moment exponent (q);
- full multilinear versus diagonal symmetric injective norm;
- Gaussian, Rademacher, independent-entry, or general subgaussian coefficients;
- for matrices, self-adjoint versus rectangular and row/column variance;
- for noncommutative martingales, the trace algebra, filtration, Orlicz-index range around 2, and whether the conclusion is a norm or a Φ-moment inequality.

For C120, compare the target to the type-2 bounds and keep the low-(p) exponent gap visible. The full and diagonal symmetric ℓp injective norms are equivalent up to an order-dependent polarization factor, but they are not equal in general. The spectral norm is the ℓ(_2) matrix operator norm, not a synonym for a tensor injective norm at other (p,r). See [method](references/method.md) and [norm examples](examples/negative.md).

Keep matrix spectral comparisons one- or two-sided exactly as stated: W12-009 Theorem 2.1 gives a one-sided spectrum inclusion, while its Theorem 2.7 is a separate two-sided Schatten-moment comparison; W12-010 Theorem 2.2 is a distinct two-sided spectral result. For noncommutative Orlicz martingales, retain the exact diagonal modular term: W12-021 Theorem 4.4 uses \(\sum_n\tau\Phi(|dx_n|)\), and its indices satisfy \(2<p_\Phi\le q_\Phi<\infty\). Strong \(L_p\) Doob/Rosenthal estimates do not automatically extend to a cross-2 \(\Phi\)-moment inequality.

Keep the other matrix comparisons distinct as well: W12-011 Theorem 2.6 is a two-sided Hausdorff comparison of (X) with a covariance-matched Gaussian matrix, while Theorem 2.16 is a one-sided inclusion near a free model. W12-012 assumes heterogeneous independent Gaussian entries. W12-027 is for continuous finite-dimensional Brownian matrix integrals; Theorem 1.4 bounds \(\mathbb E\|X_t\|_{S_{2p}}^2\) by \((2p-1)\mathbb E\int_0^t\|\sum_iH_{i,s}^2\|_{S_p}\,ds\). The integrand is not raised to power \(p\), and the bound is not a norm of the integrated quadratic variation. Cadilhac W12-025 gives K-functional and strong-(L_p) decompositions under its own hypotheses, not the B171/B172 Orlicz modular conclusions.

For C205/C206, keep positive determinant moments separate from determinant lower-orthant event association. A two-block moment formula, integer-exponent recursive evaluation, completely-monotone-function bounds, or scalar Gaussian product inequality each has a different scope. See [method](references/method.md) and [sources](references/sources.md).

For an exact polynomial moment of specified Wishart principal minors, use the [rational moment tool](references/wishart-polynomial-moments.md). The recurrence is derived from Gaussian integration by parts and polynomial continuation in the degrees of freedom.

For noncommutative martingale estimates, preserve the row/column square-function definitions and the (p=2) split. Strong (L_p) equivalences and weak-Φ moment bounds do not automatically yield the same Orlicz endpoint decomposition or cross-2 modular estimate. The historical B171/B172 clues are retained as leads, not as verified current open-status claims.

The current inventory has 33 complete local PDFs: 30 full-text sources and their theorem/proof cards have passed R06 independent review. W12-016, W12-026 and W12-033 have identity-page checks only and are excluded from the completed-source quota. No book chapter is claimed as a selected full reading. D03 matched W12-032's title, authors, abstract, version, page count, and PDF hash to the official arXiv record and v1 PDF; the 27 July date with identifier prefix 2609 is retained as a chronology anomaly, not an identity mismatch. Its theorem is used only within the scalar jointly-Gaussian-coordinate scope and does not imply Wishart determinant claims. Read [sources](references/sources.md) for exact evidence coverage before relying on a claim.

## 对称二点乘积模型的有限余秩律

给定独立上三角二点律和有理对称偏移时，用[余秩尾界](references/symmetric-binary-corank-tail.md)在小维数中枚举实际余秩，并核对主子块的并集上界。

For a finite rational Hermitian sign series, read [the OpenAI matrix-sign audit](references/openai_matrix_sign_estimate.md) before applying a Rademacher spectral-norm estimate. Its exact checker verifies the supplied sum_i L_i^2 <= vI certificate by principal minors and enumerates the input's even sign trace moment; it reports, but does not replace, the Gaussian moment step in Lemma 3.1 of the pinned OpenAI source.

## OpenAI 原稿中的方法

- [Ordered Gaussian cascade derivative interface](references/openai-ordered-gaussian-cascade.md)
