# Midpoint convexity from bounded tree potentials

**Status:** proposed skill, not installed.

**Pinned original:** *Midpoint convexity from bounded tree potentials and path costs*, SHA-256 `965c8f078bcaef0396003b94e27549eb15318b32ec27b7f467f26746af6c3f2c`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Midpoint-convexity-from-bounded-tree-potentials-and-path-costs-September-27-2026/manuscript.pdf), physical pp. 4–7, 14, 17, Lemma 2.2 and (10.3)–(10.5).

With source-defined norming sets and head/potential budgets certified, the portable local inequality is

`(||x+t y||+||x-t y||)/2 >= sqrt(1-theta^2)||x||+t theta^2||y||`, for `0<=theta<=1/2`.

At `theta=t/sqrt(4+t^2)`, the source obtains an average at least `sqrt(1+t^2/4)` and records the quadratic lower gate `delta(t)>=t^2/16` in its regime. The procedural stop condition is absence of the norming/ancestral-head certificate: an abstract norm alone is insufficient.
