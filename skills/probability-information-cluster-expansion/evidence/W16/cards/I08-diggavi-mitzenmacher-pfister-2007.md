<!-- Reader: W15; full-text read of the shared D01 conference PDF; review pending. -->
# Suhas Diggavi, Michael Mitzenmacher, and Henry D. Pfister (2007), “Capacity Upper Bounds for the Deletion Channel”

- Source identity: ISIT 2007, pp. 1716–1720, DOI [10.1109/ISIT.2007.4557469](https://doi.org/10.1109/ISIT.2007.4557469). The title is singular (“Channel”).
- Read copy: `evidence/fulltexts/I08.pdf`, 5 PDF pages, SHA-256 `4c24d1553249bc804b1cca3e9aeb80950dc281ab1986d9fc436a46ffb6447f7e`. W15 read pp. 1–5, all sections.
- Model: binary i.i.d. deletion channel; each bit is independently deleted with probability (d). The paper provides converse bounds using genie side information, not a bandit feedback model.

## Full-text coverage and results

| Source section | PDF pages | What the source does |
|---|---:|---|
| I, Introduction | 1 | States two upper-bound regimes and motivates the run-length genie. |
| II, Preliminaries | 2 | Defines run-length channel notation and capacity-per-unit-cost tools. |
| III, general upper bound | 2–4 | Gives a genie identifying fully deleted runs, reduces to a run-length channel, and states Theorem 2; numerical values are obtained by optimization. |
| IV, high-deletion asymptotic | 4–5 | Uses marker/channel reduction and Lemmas 3–4 to prove a limiting upper bound (0.7918(1-d)) as (d\to1). |
| V, discussion/references | 5 | Summarizes the result and references. |

The data-processing/converse step is that revealing deletion-run information to the decoder yields a more capable channel and hence an upper bound on the original capacity. The run-length channel’s capacity-per-unit-cost expression is bounded using an output distribution and a finite numerical optimization; the stated numbers depend on the chosen computation. The (0.7918) coefficient is specifically a (d\to1) asymptotic bound.

## Transfer boundary

The paper is a deletion-channel converse only. It has no action selection, regret, RKHS geometry, or per-arm Bernoulli KL allocation. It does not address small-(d) higher-order terms or capacity-series convergence.
