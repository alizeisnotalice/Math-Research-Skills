---
name: probability-boolean-fourier-invariance
description: Analyze Boolean-cube Fourier, coordinate influence, noise stability, low-influence invariance, and bounded-independence PTF questions. Use when the model is a Boolean function or product-space polynomial transfer; use the Gaussian approximation skill for sharp Hermite or Gaussian sign-approximation constants.
---

# Boolean Fourier, influence, noise, and invariance

Start by writing the domain, probability measure, Fourier basis, codomain, and normalization. For each hypothesis, distinguish coordinate influence, total influence, Fourier degree, support size, spectral norm, Fourier dimension, and exact dependence on every coordinate. Use [the method reference](references/method.md) for definitions and transfer checks.

For an invariance or PTF argument, verify bounded degree or an explicit smoothing/truncation step, low **individual** influences, moment-matching and hypercontractivity assumptions, and the anti-concentration needed near the threshold. For k-wise independence, state which marginals are matched and whether the coordinates are Boolean or Gaussian. Read [the source guide](references/sources.md) for the verified theorem boundaries and incomplete reading queue.

Treat open-problem statements as conjectures until a primary proof is found. The current coalition literature separates discrete-cube fixed-error tribes from continuous-cube coalitions; do not merge their conclusions. For Gaussian k-wise PTFs, use only the positive-kernel smoothed Taylor interface with an explicit zero-boundary and kernel-tail gate; do not infer the full Kane headline. For symmetry/self-duality, use only the stated Walsh parity filter and finite-group invariant projections, not a full irreducible decomposition. Follow [the positive examples](examples/positive.md) and [negative examples](examples/negative.md) for exact cases and common false implications.
For Boolean-square identities, keep the 0/1 convolution equation from \(f^2=f\) separate from the sign-valued equation from \(F^2=1\); see the method reference for both right-hand sides and their scope.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
