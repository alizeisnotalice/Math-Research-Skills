---
name: probability-bernoulli-factory
description: Select and audit exact coin factories, fixed-depth event representations, and random-stopping constructions with assumptions, output types, and cost clocks explicit.
metadata:
  short-description: Exact Bernoulli factories and stopping rules
---

# Bernoulli-factory analysis

Use this skill when a problem asks for an exact output from biased coins, a finite-depth event representation, or a stopping-time factory. Start by fixing the unknown parameter set, the input coin model, allowed auxiliary randomness, output type, endpoint values, and the cost clock. A Bernoulli factory for `f` must return a bit with probability exactly `f(p)`; a nonnegative unbiased estimator, a categorical/vector output, or an exponential acceptance event is a different output contract.

There is no single algorithm behind the 30 admitted source uses. Choose a method only when the source card’s theorem, hypotheses, randomness, and output agree with the problem. The **source-use index** and 30 scoped use cards are the controlling evidence; each card states what was accepted and what remains outside its scope.

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

The active index contains 30 distinct complete-read works with current, narrowly scoped use decisions: 27 new R13 high audits and 3 exact matched prior high uses. This is not a claim that every theorem in every paper passed High review. There are zero new full reads and zero new 198-method closures in this whole-entry stage. The skill leaves the sharp/effective degree problem A202, the general moment-classification claim C204, and unapproved method branches open. See the outer evidence freeze for exact reviewer records and hashes.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
