---
name: probability-variational-limits
description: Audit limits of stochastic optimization values, expectations, minimax problems, and selected optimizer laws; match weak convergence, uniform integrability, Gamma convergence, LDP/Laplace principles, and second-parameter estimates to their exact hypotheses.
metadata:
  short-description: Stochastic optimization limits and transfer checks
---

# Probability variational limits

Identify the target before choosing a transfer theorem. Record the varying law and feasible set, the decision topology, the sign and integrability of the objective, the order of all limits or suprema, and whether the conclusion concerns values, minimizing sequences, optimizer laws, or saddle points.

| Target | Conditions and route |
| --- | --- |
| Lower bound for a varying expectation | Use the [weak-law and integrand routes](references/source-applications.md#weak-convergence-and-unbounded-objectives). Check the joint lower envelope along moving states and the negative tail or integrable minorant. For equality also prove a matching upper bound, including a recovery statement when decisions vary. |
| Convergence of optima | Use [epi-convergence and stochastic optimization](references/source-applications.md#optimization-values-and-optimizers). For minimization, prove liminf on moving feasible decisions and recovery at a target near-optimal decision. Require an extra level-boundedness or tightness argument to extract near-minimizers. Reverse directions for maximization. |
| Stopping value or law of stopping rules | Fix the joint path/stop-time model and filtration. Check marginal support and adaptedness under weak limits. The [stopping examples](references/source-applications.md#optimization-values-and-optimizers) specify the time horizon, reward, process convergence and any uniqueness conditions. See [martingale and stopping methods](../probability-martingale-stopping/SKILL.md). |
| Finite decision set or random objectives | Match the iid law, support, uniformity, sharpness or function-space topology to the desired [sample-average and value-limit result](references/source-applications.md#optimization-values-and-optimizers). Only a distributional functional limit on the correct space supports a delta-method transfer. |
| Minimax interchange or saddle point | Verify the required topology, one-sided compactness, semicontinuity and convexity/concavity in the [minimax scope](references/source-applications.md#minimax-exchange). A finite exchange leaves any horizon or discretization limit to a separate argument. |
| Exponential scaling of integrals | Fix the LDP speed and topology, use the precise [Laplace-principle route](references/source-applications.md#ldp-and-laplace-principle), and control the exponential tail if the test is unbounded above. |

For a second parameter, write the needed uniform error with the parameter set and order of quantifiers. For selected optimizer laws also give the measurable selector, tie rule and limiting uniqueness or identification condition. Use finite primal/dual certificates to certify the chosen finite problem and record its relation to the limiting model.

Use the [problem map](references/method.md), [source index](references/sources.md) and [scoped source applications](references/source-applications.md) for theorem versions, counterexamples and historical proof boundaries.

## OpenAI 原稿中的方法

- [OpenAI wave-3 variational interfaces](references/openai-wave3.md)
