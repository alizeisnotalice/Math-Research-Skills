---
name: probability-first-passage-growth
description: Analyze first-passage percolation, geodesics and Busemann functions, random growth and competition, and max-flow questions when the exact weight law, lattice, dimension, or direction hypotheses matter.
metadata:
  short-description: First-passage and growth models
---

# First-passage percolation and growth models

Use this skill for passage-time shape and fluctuation questions, geodesics or Busemann limits, Eden/Richardson growth and competition, and percolation max-flow. Start with the weight law, lattice, dimension, direction, time convention, and target observable. Read [model checks and transfer limits](references/method.md), then [source cards](references/sources.md) for the theorem-specific conditions.

Record theorem number, version, physical page, law, moment and atom assumptions, quantifiers, and imported proof steps. Distinguish a theorem from a numerical or finite-volume calculation and state what a calculation leaves open.

- Directed last-passage percolation, undirected first-passage percolation, Eden growth, and capacity max-flow have different couplings and observables.
- Eden growth with one clock per exposed edge makes a boundary vertex's rate its infected-neighbour count. This differs from uniform selection among frontier vertices.
- A statement for each deterministic direction can have a direction-dependent null set. Do not promote it to one event for all directions.
- The continuum Poisson-chain comparator in this entry does not prove a boundary-preserving directed edge-flow comparison. Use `probability-flow-poset-growth` for that model.

For OpenAI finite growth interfaces, read [the source notes](references/openai-200-226.md). The [positive](examples/positive.md) and [negative](examples/negative.md) examples exercise law and clock gates. Historical review material is available through [the central evidence guide](../math-research/references/evidence.md).
