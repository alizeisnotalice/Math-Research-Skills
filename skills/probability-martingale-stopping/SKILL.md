---
name: probability-martingale-stopping
description: Analyze martingales, stopping rules, maximal inequalities, stochastic integrals, and martingale-problem limits with explicit filtration and integrability checks.
---

# Martingales, stopping, and stochastic integration

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when a probability argument depends on a martingale or supermartingale, a stopping time, a Doob/BDG bound, stochastic integration, or a diffusion martingale problem.

## First checks

State the filtration and time index, adaptedness, conditional mean, integrability class, and whether the process is a true martingale, local martingale, or supermartingale. Keep conditional variance, predictable bracket ⟨M⟩, optional quadratic variation [M], and realized squared increments distinct.

For optional stopping, state the exact sufficient hypothesis used: bounded stopping time, UI plus a limit argument, bounded process with a.s.-finite stop, integrable stop with controlled increments, or the theorem’s stated alternative. Almost-sure finiteness alone does not justify E[M_T]=E[M_0].

Keep classical martingale OST separate from demimartingale inequalities, which require coordinatewise monotonicity of the stopping events. For local martingales, distinguish endpoint integrability and true martingality from H¹ control; a bounded stochastic integrand need not preserve true martingality without the required integrator hypotheses.

## Match the theorem to the task

- For maxima, verify nonnegative submartingale or the required p-moment before using Doob.
- For variance-budget crossings with bounded increments, check centering, scale, and predictable conditional variance before using Freedman. Distinguish Fan–Grama–Liu results: S007 Theorem 2.1 uses a conditional exp{λξ−g(λ)ξ²} normalizer with separate realized-square and V-sum caps; S007 Corollary 2.7 uses a one-sided upper increment and its piecewise C² proxy; S010 Theorem 2.1 uses a positive-tail truncation with conditional second moments. Match the exact assumptions and budget. For time-uniform bounds construct the nonnegative exponential supermartingale and state ψ, intrinsic time V, and initial factor l0.
- For sub-ψ line crossing, keep the adapted pair (S,V), nondecreasing intrinsic time, initial factor l0, and the actual exponential-supermartingale domination condition. The probability bound controls the stated one-sided line crossing; use the source's filtration/path hypotheses in continuous time.
- For BDG, record continuity versus jumps, scalar versus Banach setting, p-range, localization, bracket, and constant dependence. UMD Banach bounds use the Gaussian-radonifying covariance characteristic; the cited 0<p<1 extension is for continuous local martingales, while the purely discontinuous bound is stated for p≥1. Do not transfer UMD constants to arbitrary spaces.
- For differential subordination, verify the bracket order ([X,X]-[Y,Y]) is nonnegative and increasing; the sharp (p^*-1) or orthogonal cotangent constants require the stated Hilbert/scalar setting. A sharp scalar Riesz component bound does not settle the vector (ell^2)-valued Riesz norm or its best dimension-free constant.
- For stochastic integrals, state predictability and integrability before defining the integral; distinguish existence from a norm estimate. The compensated-Poisson (L^q)-valued isomorphism uses simple adapted integrands, future-increment independence, UMD decoupling, and the appropriate intersection/sum of mixed norms; do not substitute scalar continuous-martingale BDG.
- For Snell envelopes, distinguish the class-D Doob–Meyer decomposition from generic OST. The compensator domination (dA\le dD^-) needs the source's special-semimartingale and (S^1\cap H^1_{loc}) hypotheses; the Markov generator and smooth-fit consequences have additional right-process or diffusion assumptions.
- For unbounded martingale increments, choose the tail theorem matching the moment and clock: S009's two-sided exponential-moment maximal theorem differs from its positive-part exponential-moment/Freedman truncation theorem. For a quantitative martingale CLT, retain both the conditional ((2+\rho))-moment condition and the predictable-bracket error, plus any maximum-increment term.
- For a martingale problem, specify the operator/test functions, prove tightness separately, pass identities with continuity and UI, and prove uniqueness before claiming a unique limit.
- For weak-limit martingale problems with controls or fixed jumps, carry the control laws, canonical test versions, determining class, uniform integrability, dense-time identities, and path-control assumptions through the limit step; J1 weak convergence alone does not identify a martingale problem.

Read [method.md](references/method.md) for proof routes and assumption audits, [sources.md](references/sources.md) for evidence and source status, and the positive/negative examples for tested use patterns. The strict W02 v2 candidate has 29 retained scholarly sources plus one approved Aldous canonical use (30 candidates); the full course-notes read remains background and excluded. The combined candidate is pending independent scope review. Finite enumeration is computational evidence only, not a proof of an infinite-time theorem.

## 有限 e-process 的逆矩和 II 类错误

对于独立且确定调度的二元乘子，用[有限逆矩审计](references/finite_inverse_moment_type_ii.md)核验条件 e-variable 约束、固定时域和时域内首次跨界的 II 类错误。
