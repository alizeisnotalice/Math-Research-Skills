---
name: probability-queueing-heavy-traffic
description: Analyze queueing-network stability and heavy-traffic limits using fluid/Lyapunov methods, polling models, state-space collapse, BAR, and reflected diffusions. Renewal/Palm epoch conversion and exact coupling/total-variation questions are out of scope here.
---

# Queueing stability and heavy traffic

Use this skill for queue stability, polling, heavy-traffic scaling, state-space collapse, BAR, or reflected-Brownian limits. Fix the state, observation epoch, arrival and service assumptions, discipline, CRP status, and requested stability or convergence notion. Read [method guidance](references/method.md) for route-specific model checks and [source cards](references/sources.md) for scoped theorem uses. Do not transfer across a change in discipline, input dependence, or limit mode without a proved interface.

For renewal input, record the interarrival law, dependence, age or residual life, and observation epoch. PASTA applies to Poisson arrivals under nonanticipation. It does not extend automatically to renewal input.

For transform or diffusion work, derive the generator or steady-state identity from the actual boundary convention before solving it. Keep the probability-derived transform class separate from a larger analytic class. Numerical work is a consistency check, not a stability proof, limit theorem, or uniqueness result. See the [positive](examples/positive.md) and [missing-condition](examples/negative.md) examples.

For B054 Eq. (7), specify the uniqueness class. The literal analytic Eq. (8) class has scalar-normalization ambiguity. Adding `L(0)=1` resolves that ambiguity only inside the augmented analytic class. Probability-law uniqueness still needs positivity, support, and unused-service boundary-measure conditions.

The current source snapshot records scope and versions only. Verify publication and open-problem status afresh before relying on it.
