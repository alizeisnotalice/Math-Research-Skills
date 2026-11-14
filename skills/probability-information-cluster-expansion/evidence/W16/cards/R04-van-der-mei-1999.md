<!-- Reader: W15; full-text read of shared author PDF; review pending. -->
# R. D. van der Mei (1999), “Delay in Polling Systems with Large Switch-over Times”

- Source: *Journal of Applied Probability* 36(1), 232–243 (1999), DOI [10.1239/jap/1032374244](https://doi.org/10.1239/jap/1032374244). Read copy: 12-page author-hosted PDF `evidence/fulltexts/R04.pdf`, SHA-256 `846a78b0c7e5bb2ef77becc3113d4ef8feb403fd2a4485b82296b2b154fae90a`.
- Reader: W15; PDF pp. 1–12 read from the D01 handoff; no second download.
- Model: `N` infinite-buffer cyclic queues; independent Poisson arrival streams at rates `λᵢ`; independent M/G/1 service times with finite first and second moments; total load `ρ=Σᵢρᵢ<1`; fixed, deterministic switch-over times `rᵢ`, total cycle switch-over `r=Σᵢrᵢ`; each queue uses a fixed gated or exhaustive policy. The theorem sends `r→∞` while the setup proportions remain fixed.

## Results and proof path

Theorem 1 (PDF p. 6, Eq. (10)) shows that the queue population at a polling instant obeys

`Xᵢ/r → λᵢ(1−ρᵢ 1{i∈E})/(1−ρ)` almost surely,

where `E` is the set of exhaustively served queues. For the scaled steady-state delay, Theorem 2 (PDF pp. 7–8, Eqs. (15)–(16)) gives convergence in distribution to a uniform law. If queue `i` is gated, the interval is `[ρᵢ/(1−ρ), 1/(1−ρ)]`; if it is exhaustive, the interval is `[0,(1−ρᵢ)/(1−ρ)]`. Theorem 3 gives the corresponding moments (PDF p. 8).

The proof uses the Descendant Set Approach: customers arriving during deterministic switch-over periods are originators; their descendant populations are independent. A renewal-reward strong law gives the limit contribution from each switch-over cycle. The recursive descendant PGFs/moments are used to show the infinite-cycle sum converges (the proof controls `Σ_c E[Y_c²]` via the second factorial moments), yielding Theorem 1. A polling-epoch waiting-time/queue-length transform relation and a limiting Laplace–Stieltjes transform then give the uniform law in Theorem 2. The source assumes deterministic setups for this argument. In §6 (PDF pp. 10–12) it gives a random-switch-over counterexample to the key relation and explicitly leaves stochastic setup extensions open.

## Full-text map

| Section | PDF pages | Coverage |
|---|---:|---|
| §1, Introduction | 1–3 | Motivation, prior branching-process work and paper organization. |
| §2, Model description | 3–4 | Poisson inputs, service policies, deterministic setups, load and steady-state model. |
| §3, Descendant-set approach | 4–6 | Originators, descendant populations, recursive PGFs and first/second moments. |
| §4, Analysis | 6–8 | Almost-sure polling-queue limit and scaled waiting-time distribution. |
| §5, Numerical examples | 8–9 | Illustrative parameter choices and finite-system comparisons. |
| §6, Implications | 9–12 | Properties, limits, stochastic-setup counterexample, open extensions and references. |

## Transfer limit

The theorem does not establish a general-renewal arrival result, stochastic setup limit at fixed load, or the general A007 stationary-to-fluid exchange. Its Poisson input, deterministic setup, gated/exhaustive and branching structure are material assumptions. The paper notes that finite-setup waiting-time tails need not be bounded even though the limiting scaled law has bounded support.
