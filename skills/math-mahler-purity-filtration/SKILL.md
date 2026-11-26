---
name: math-mahler-purity-filtration
description: Apply the generalized-Mahler Hahn/Puiseux purity filtration to a supplied Mahler equation, while tracking exceptional arithmetic-growth layers and decomposition hypotheses.
---

# Mahler purity filtration

Use this skill for a specified Mahler equation together with a proved
generalized-series solution decomposition. State the Mahler operator, base,
Hahn or Puiseux support, arithmetic-growth filtration level and every minimal
equation before invoking a purity result.

The source theorem propagates its purity conclusion only through its stated
higher arithmetic-growth layers. It excludes the lowest exceptional layers.
The required Hahn-series summability, Puiseux decomposition and height-gap
conditions are proof obligations supplied with the target equation. A finite
coefficient prefix or a numerical Mahler value does not establish them.

Read the [source scope](references/ext0229-mahler-purity-filtration.md) for
the theorem version and its excluded layers. Questions about differential
transcendence of a solution continue to use the parameterized difference-Galois
route when its stronger hypotheses are available.
