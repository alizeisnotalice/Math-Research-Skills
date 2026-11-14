---
name: probability-nonlinear-law-dynamics
description: Analyze fixed points and iteration of probability-law operators, including nested stationary-law maps, nonlinear Markov updates, and recursive distributional equations; use when the proof needs operator-specific existence, uniqueness, stability, or global convergence.
---

# Nonlinear probability-law dynamics

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when a probability distribution is itself the state of a nonlinear map and the task concerns its fixed points, basins, stability, or iterates. Start by writing the exact operator, its domain, and its topology. Read [references/method.md](references/method.md) for operator typing and proof gates; consult [references/sources.md](references/sources.md) for the evidence ledger and source status. The checked patterns in [examples/positive.md](examples/positive.md) and [examples/negative.md](examples/negative.md) show the scope limits.

Keep these three operators distinct:

1. **Nested stationary-law map:** `Phi(theta) = pi(K_theta)`, where `pi(K_theta)` is the invariant law of a Markov kernel with parameter `theta` frozen. An inner mixing theorem is about iterating `K_theta` at one fixed `theta`; it says nothing by itself about the outer iteration `theta[n+1] = Phi(theta[n])`.
2. **Nonlinear Markov law update:** commonly `mu[n+1] = mu[n] K_{mu[n]}`, or a law-dependent continuous-time evolution. Use its results only after verifying that this is the same update as the target map.
3. **Recursive distributional equation (RDE):** `T(mu) = Law(g(xi, X_1, ..., X_m))` with independent copies `X_i ~ mu` and specified innovations. RDE contraction/classification tools apply only if the target operator has this representation or a proved reduction to it.

Separate fixed-point existence, uniqueness, local stability, convergence of every orbit, and almost-everywhere basin claims. Do not promote numerical behavior, a density-only result, an inner-chain rate, or a result for a special polynomial/RDE class into a theorem for a different law operator.

The current evidence pack is a **pending research draft**: the 45-row W21 ledger records 31 complete full-text reads and 14 candidate-only records. The original screened candidate inventory has 38 works: 24 are full-text read and 14 remain candidate-only; five additional full-text method sources sit outside C001–C038. W21-001 and W21-002 are distinct works also canonicalized under W04; each counts once toward W21’s evidence quota but adds no new global unique work. D03 batches 01, 02, 03 and 05 supplied the source PDFs; batch05 upgraded C037/W21-039 and added five supplementary methods. Those five are provisionally eligible for the tool-level source count because they prove results for the exact smoothing-transform or centered-QSO classes covered by this skill, while their A121/A122 exact-interface flags remain false. R02 stage22 recorded 27 full-text entries passed, four requiring revision (W21-041/043/044/045), and 14 candidate-only sources unread. The four corrections are submitted for R02 re-review; W21's reader-status fields may remain pending until the next independent review binding. R02 controls review acceptance; this evidence draft is not a release or approval. C020 remains unacquired and no supplement replaces it. Candidate-only records are not proof cards. See the status and source ledger for exact scope; do not claim A121 or A122 is solved.
