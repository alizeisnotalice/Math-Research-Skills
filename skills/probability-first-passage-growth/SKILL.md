---
name: probability-first-passage-growth
description: Analyze first-passage percolation, geodesics and Busemann functions, random growth and competition, and max-flow questions when the exact weight law, lattice, dimension, or direction hypotheses matter.
metadata:
  short-description: First-passage and growth models
---

# First-passage percolation and growth models

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill for passage-time shape and fluctuation questions, geodesic existence or coalescence, Busemann limits, Eden/Richardson growth and competition, and percolation max-flow. Start by identifying the model and exact hypotheses before selecting a theorem.

Read [references/method.md](references/method.md) for model checks and proof-transfer limits. Use [references/sources.md](references/sources.md) to locate the W06 full-text library and its current reading status. R03 independently accepted 30 eligible sources: 29 complete papers and one fully acquired book with complete selected sections. The [final review](evidence/review/review.json) binds the approved versions. A citation in the library does not by itself settle an archived question; the recorded version and transfer gaps remain in force.

When applying a result, record its theorem number, source version, PDF and printed page, dimensions, law, moment/atom assumptions, quantifiers, and proof dependencies. Separate rigorously proved statements from numerical checks and conjectural KPZ predictions. For a numerical or finite-volume claim, run an appropriate local math tool and state what the calculation cannot establish.

Two recurring boundaries are especially important:

- Directed last-passage percolation, undirected first-passage percolation, Eden growth, and capacity max-flow are different models. Transfer only a lemma whose hypotheses and coupling explicitly cover the target model.
- Eden growth may use one clock per exposed vertex or one clock per exposed edge. In the latter, infection rate of a boundary vertex is its number of infected neighbors; this is the exponential edge-FPP version. Keep it distinct from uniform choice among distinct frontier vertices.
- Preserve direction quantifiers. Archived C097 asks for uniqueness almost surely for each deterministic direction fixed in advance, with a possibly direction-dependent null event; it does not ask for one common event covering every direction simultaneously.

For oriented Bernoulli flow, the continuum Poisson chain-cover constant 2 is now supported by Aldous–Diaconis (1995), Theorem 5, combined with the finite-poset chain-cover identity. Keep the discrete edge-disjoint path approximation and the two-limit interchange marked unproved.
