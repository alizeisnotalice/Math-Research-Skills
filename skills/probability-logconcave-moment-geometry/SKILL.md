---
name: probability-logconcave-moment-geometry
description: Analyze moment comparisons, centroid-body expansion, convex geometry, and transport or functional inequalities for log-concave laws.
---

# Log-concave moments and convex geometry

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill for weak-versus-strong moment bounds, Lp centroid bodies, concentration by convex-body enlargement, or transport/function inequalities for log-concave measures.

This skill has 31 complete source readings independently accepted by R06. The five partial readings and remaining unread catalogue entries are excluded from the completed-source quota. The ledger retains every assigned record M0258–M0344 and its actual version and scope. See [the method note](references/method.md), [the source/status ledger](references/sources.md), and [source cards](evidence/W11/cards).

## Keep the problem's full scope

- Record whether the law is merely log-concave, centered, symmetric, isotropic, unconditional, product, or rotationally invariant. These assumptions are not interchangeable.
- For a norm $||\cdot||$, define its weak moment as $\sigma_{||\cdot||,X}(p)=\sup_{||v||_*\le1}(E|\langle v,X\rangle|^p)^{1/p}$. Distinguish a mean-centered deviation estimate from a bound on $(E||X||^p)^{1/p}$.
- Define $Z_p(\mu)$ by its full support function $h_{Z_p(\mu)}(v)=(\int|\langle v,x\rangle|^p\,d\mu(x))^{1/p}$. Preserve the quantifiers over every $p\ge2$ and every Borel set when checking CI($\beta$).
- Do not infer the arbitrary-norm C153 conclusion from the Euclidean Paouris theorem, an $\ell_r$ estimate with a factor depending on $r$, a result for isotropic laws under a fixed coordinate norm, or a dimension-dependent bound.
- Do not replace C154's $Z_p(\mu)$ enlargement by a Euclidean ball, an $\ell_1+\ell_2$ product-scale estimate, a packing bound, or KLS/Cheeger concentration without proving the missing set inclusion and preserving its constants.

## Work with proof dependencies

For weak/strong moments and norm scope, consult [the C153 card](evidence/W11/cards/M0258.md), [the exact conjecture source](evidence/W11/cards/M0260.md), [Paouris' Euclidean estimate](evidence/W11/cards/M0280.md), [Sudakov/coordinate maxima](evidence/W11/cards/M0282.md), [the independent-coordinate theorem](evidence/W11/cards/M0285.md), and [the centroid-entropy result](evidence/W11/cards/M0296.md). For order statistics, keep [M0274's one-sided count](evidence/W11/cards/M0274.md) separate from [M0290's decorrelation and mean-zero results](evidence/W11/cards/M0290.md). For transport/functional inequalities and conditional transfer to norms, consult [M0315](evidence/W11/cards/M0315.md), [M0316](evidence/W11/cards/M0316.md), and [M0322's product convex-ICI theorem](evidence/W11/cards/M0322.md). For entropy jumps, [M0333](evidence/W11/cards/M0333.md) retains its isotropy, log-concavity and spectral-gap assumptions. Check each theorem's law class, moment range, dimension dependence, and whether its cost inequality is convex or unrestricted.

The stored finite-dimensional calculation in evidence/W11/notes/numeric-check.txt is a sanity check for a square example. Treat it only as numerical/symbolic evidence; it is not a proof of either open problem.
