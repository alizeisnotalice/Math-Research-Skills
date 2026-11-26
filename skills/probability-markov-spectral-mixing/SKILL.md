---
name: probability-markov-spectral-mixing
description: Analyze finite reversible Markov-chain mixing and spectral gaps, especially heat-bath Glauber dynamics for ferromagnetic Ising models; use when a claim depends on update clocks, graph geometry, or correlation inequalities.
---

# Markov spectral gaps and Ising Glauber dynamics

## Historical provenance status

**Historical source audit (2026-11-16):** the R02 W04 release/source-file ledger is historical completeness evidence; that review used low reasoning effort, not current high-scoped source review. R01 has now accepted exact scoped uses for all 30 W04 baseline works (28 complete papers plus two acquired books with completed used units), and its aggregate contains 37 distinct eligible works including seven expansion sources. Every accepted use is limited to the exact row conditions and transfer limits in the 37-work accepted-use register（本机附件：`references/accepted_scope_register.md`）; source-level high matching does not certify every old theorem or claim. No new full-text/global credit is claimed. The earlier 11-row L01 expansion count is historical: R01 now unions those interfaces with 26 newly high-scoped W04 baseline works for 37 distinct accepted works. The separate 32-work G03 entry is not merged into this count. Whole-entry and release records are historical provenance only.

Use this skill for finite-state reversible-chain spectral-gap or mixing questions, with focused guidance for Ising heat-bath Glauber dynamics and the accepted FKG/Holley association interfaces. Before applying a theorem, pin down the state space, Gibbs law and fields, update rule, vertex rates, and discrete-time versus continuous-time convention. Write the generator or kernel and its Dirichlet form explicitly; compare gaps only under a common clock. Read [references/method.md](references/method.md) for exact formulas and correlation-inequality hypotheses.

For Ising edge-parameter claims, distinguish stationary correlation monotonicity from finite-time behavior and from eigenvalue monotonicity. A040 remains open here for arbitrary finite graphs: Nacu verifies cycles at zero field. Kargin's printed theorem states a uniform-field homogeneous result, but the audited proof's reflection step `f_k=-f_(n-k)` is certified here only at zero field. The nonzero-field proof remains unresolved; this is not a refutation. Shirai's counterexample concerns a stronger fixed-time spin-expectation claim, not the spectral-gap question. Use [references/sources.md](references/sources.md) for theorem scope and page locators.

When differentiating a reversible family with Gibbs law `pi_theta`, state the fixed state space and regularity. A symmetric conjugate `D_theta^(1/2)P_theta D_theta^(-1/2)` has derivative terms from both `D_theta` factors as well as `P_theta`. Along a differentiable normalized simple eigenbranch those measure/eigenvector terms cancel in the scalar eigenvalue derivative; at a repeated eigenvalue use an isolated spectral subspace and a directional compressed derivative. A stationary-law bound and static correlation signs alone do not establish gap monotonicity. See the L01 perturbation supplement（本机附件：`references/l01-perturbation-boundaries.md`） and the continuation audit（本机附件：`references/l01-continuation-audit.md`） for the current source-use state.

Treat finite enumeration, floating-point eigensolvers, and high-precision point checks as search evidence only. They can locate candidate behavior but cannot prove an all-graphs theorem.

For an exact-uniform output from a finite rational kernel, after separately certifying a sufficiently accurate finite-time law, use the rare residual correction in [references/exact-residual-sampling.md](references/exact-residual-sampling.md). It requires a concrete size bound, a total-variation/pointwise certificate, and an integer denominator `qP`, then samples the residual only on an exponentially rare branch. This is an exact-sampling wrapper, not a new spectral-gap or switch-chain mixing theorem; it does not establish the hypotheses needed to use it for an arbitrary graph-switch chain.

## Finite stationary additive tails

For a finite stationary reversible chain with a rational kernel and an integer observable, use the [exact Chernoff certificate](references/finite-markov-chernoff.md) to verify a proposed tilted operator upper bound and its resulting additive upper-tail bound.

For a stationary reversible chain and an explicitly given real observable, use the [exact stationary increment audit](references/openai_critical_slowing_stationary_increment.md) to check the discrete \(k\)-step second moment and the one-step Dirichlet-form bound.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
