---
name: probability-boolean-fourier-invariance
description: Analyze Boolean-cube Fourier, coordinate influence, noise stability, low-influence invariance, and bounded-independence PTF questions. Use when the model is a Boolean function or product-space polynomial transfer; use the Gaussian approximation skill for sharp Hermite or Gaussian sign-approximation constants.
---

# Boolean Fourier, influence, noise, and invariance

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Start by writing the domain, probability measure, Fourier basis, codomain, and normalization. For each hypothesis, distinguish coordinate influence, total influence, Fourier degree, support size, spectral norm, Fourier dimension, and exact dependence on every coordinate. Use [the method reference](references/method.md) for definitions and transfer checks.

For an invariance or PTF argument, verify bounded degree or an explicit smoothing/truncation step, low **individual** influences, moment-matching and hypercontractivity assumptions, and the anti-concentration needed near the threshold. For k-wise independence, state which marginals are matched and whether the coordinates are Boolean or Gaussian. Read [the source guide](references/sources.md) for the verified theorem boundaries and incomplete reading queue.

Treat open-problem statements as conjectures until a primary proof is found. The current coalition literature separates discrete-cube fixed-error tribes from continuous-cube coalitions; do not merge their conclusions. Follow [the positive workflow](examples/positive.md) for a correctly scoped transfer and [the negative example](examples/negative.md) for common false implications.
