---
name: probability-first-passage-growth
description: Analyze first-passage percolation, geodesics and Busemann functions, random growth and competition, and max-flow questions when the exact weight law, lattice, dimension, or direction hypotheses matter.
metadata:
  short-description: First-passage and growth models
---

# First-passage percolation and growth models

Use this skill for passage-time shape and fluctuation questions, geodesic existence or coalescence, Busemann limits, Eden/Richardson growth and competition, and percolation max-flow. Start by identifying the model and exact hypotheses before selecting a theorem.

## Active sources and historical provenance

Read [references/method.md](references/method.md) for model checks and proof-transfer limits. Use [references/sources.md](references/sources.md) to locate the W06 full-text library and its reading history. The historical R03 baseline contains 30 distinct works (29 complete papers and one fully acquired book with the complete selected units); the [archived R03 review](evidence/review/review.json) binds that baseline. R04 has now accepted narrow, source-specific current uses for these same 30 works. Use the published method and source notes first. Retrieve the archived scoped-use register（本机附件：`references/current_scopes.md`）when applying a theorem whose scope requires that record. R04 reviewed the scientific scope and cases of the archived candidate02 snapshot. The exact n=4 finite negative-boundary certificate and its R04 review are available under `evidence/R04/n4_counterexample/`. For the install-facing canonical 30 and true W06-to-PR identity map, use current canonical sources（本机附件：`references/current_canonical_sources.md`）, the canonical index（本机附件：`evidence/R04/canonical_source_index30_portable.json`）, and the W06 alias map（本机附件：`evidence/R04/W06_source_alias_map.json`）. The historical 39-source listing remains context; held or unread entries are not part of the eligible 30. A citation alone does not settle an archived question. For a worked positive application, a missing-law case, and an exact finite clock-convention calculation, see verified cases（本机附件：`examples/verified_cases.md`）.

When applying a result, record its theorem number, source version, PDF and printed page, dimensions, law, moment/atom assumptions, quantifiers, and proof dependencies. Separate rigorously proved statements from numerical checks and conjectural KPZ predictions. For a numerical or finite-volume claim, run an appropriate local math tool and state what the calculation cannot establish.

Recurring boundaries:

- Directed last-passage percolation, undirected first-passage percolation, Eden growth, and capacity max-flow are different models. Transfer only a lemma whose hypotheses and coupling explicitly cover the target model.
- Eden growth may use one clock per exposed vertex or one clock per exposed edge. In the latter, infection rate of a boundary vertex is its number of infected neighbors; this is the exponential edge-FPP version. Keep it distinct from uniform choice among distinct frontier vertices.
- Preserve direction quantifiers. Archived C097 asks for uniqueness almost surely for each deterministic direction fixed in advance, with a possibly direction-dependent null event; it does not ask for one common event covering every direction simultaneously.

For directed Bernoulli edge-flow and poset-cover questions, use the separate `probability-flow-poset-growth` entry. W06-039 is only a continuum Poisson-chain comparator in this FPP entry; neither a finite-poset cover argument nor the continuum chain limit proves the discrete boundary-preserving edge-flow comparison. Keep this gap open.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。

## OpenAI 原稿中的方法

- [OpenAI direct source notes: finite growth interfaces](references/openai-200-226.md)
