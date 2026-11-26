---
name: math-gfunction-representability-obstructions
description: Apply a Picard--Vessiot obstruction to a proposed rational representation of a G-function by supplied solution families, singularity bounds and differential-Galois data.
---

# G-function representability obstructions

Use this skill when a proposed representation puts a nonzero target solution
in \(\mathbb C(x)(f_1,\ldots,f_k)\), where every source equation and its
Picard--Vessiot extension are specified. Record the target equation, a
fundamental solution containing the target, every proposed generating solution
and the representation class before applying the obstruction.

If the target differential-Galois group is noncommutative and has no proper
nontrivial normal algebraic subgroup, the supplied representation forces its
Picard--Vessiot field to lie in one of the proposed source extensions. This
turns a representation claim into a containment test. It does not compute a
differential-Galois group, prove that a target is a G-function, or decide
arbitrary functional representations.

For bounded-singularity hypergeometric families, read the [source theorem and
Apéry witness](references/ext0220-gfunction-pv-obstruction.md). A singularity
count must concern the actual pulled-back equations, including all finite and
infinite singularities. A conclusion about a special value requires a separate
specialization theorem.
