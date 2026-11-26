---
name: probability-bernoulli-factory
description: Select and audit exact coin factories, fixed-depth event representations, and random-stopping constructions with assumptions, output types, and cost clocks explicit.
metadata:
  short-description: Exact Bernoulli factories and stopping rules
---

# Bernoulli-factory analysis

Use this skill when a problem asks for an exact output from biased coins, a finite-depth event representation, or a stopping-time factory. Start by fixing the unknown parameter set, the input coin model, allowed auxiliary randomness, output type, endpoint values, and the cost clock. A Bernoulli factory for `f` must return a bit with probability exactly `f(p)`; a nonnegative unbiased estimator, a categorical/vector output, or an exponential acceptance event is a different output contract.

Choose a method by its assumptions, randomness, output, and cost clock. Use the source cards to verify which theorem supports the selected construction.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

## First choose the output and stopping model

- For a fixed number `N` of unknown-`p` tosses, express the event as a degree-`N` Bernstein polynomial. With only p-tosses, its unnormalized coefficients must be integer event counts between `0` and `binom(N,j)`. If independent auxiliary randomness is allowed, a finite-depth Bernstein coefficient in `[0,1]` can be used by the matching finite-depth construction.
- For an almost-surely finite random stopping time, use a source-specific envelope, series, reverse-time, recursive, or residual-mixture construction. Prove almost-sure termination separately from finite expected cost or tail bounds.
- For a categorical or vector-valued output, use a finite polynomial race only when the weights satisfy the stated balance and positivity requirements.
- For a nonnegative unbiased real estimator, do not call it a Bernoulli coin. For diffusion acceptance, Poisson zero events and uniform-point alternating events have their own geometric assumptions. For MCMC odds aggregation, verify the input factorization and every leaf coin first.

## Keep the model and cost clock visible

Record whether cost means unknown-p tosses, fair bits or uniforms, iterations, Poisson points, leaf calls, or all primitive random operations. Do not convert a paper’s iteration index to toss count unless its algorithm supplies that conversion. A.s. termination does not imply finite mean cost. Endpoint claims must be checked at `p=0` and `p=1`; a bound using an interior positive minimum does not cover endpoint zeros.

See [method selection](references/method.md), cost and assumptions（本机附件：`references/cost-and-assumptions.md`）, the exact 30-row source-use index（本机附件：`references/runtime_source_uses.json`）, [source bibliography and cards](references/sources.md), open claims（本机附件：`references/open-claims.md`）, and the [positive](examples/positive.md) and [negative](examples/negative.md) examples.

## Evidence scope

For debiasing, the compatible-envelope existence and rate are supplied by the [HNP dependency audit](references/hnp-envelope-adjudication.md). The operational proof also needs the actual coefficient arrays, remainder bound, and starting index for the selected function. The sharp degree and general moment-classification problems remain open in the historical project scope.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。

## 有限支撑随机截断的精确账本

给定有限 Bernstein 下系数、有理参数与有限支撑截断时，用[去偏账本](references/finite_debiased_ledger.md)核对路径范围、有限期望恒等式、目标点偏差和未知硬币成本。
