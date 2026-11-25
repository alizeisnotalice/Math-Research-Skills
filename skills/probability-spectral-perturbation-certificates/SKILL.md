---
name: probability-spectral-perturbation-certificates
description: Audit finite-dimensional parameter-dependent eigenvalues and reversible Markov spectral gaps, including changing stationary measures, crossings, Poisson response, and rigorous interval enclosures.
---

# Spectral perturbation and strict gap certificates

**Stage status (2026-11-16):** R01's compiler accepted 32 distinct source works for this entry, meeting the 30-work floor. The current source-use snapshot and all six G03 method interfaces are recorded in `evidence/accepted_source_uses.json`, `references/sources.md`, and `references/method_coverage.md`. The whole-entry review and root publication checks remain open; this is not released or installed.

Use this entry when a finite reversible Markov kernel or a finite-dimensional self-adjoint matrix varies with a parameter and the task asks for a spectral derivative, ordered gap, crossing, or certified eigenvalue interval. Start by fixing the state space, matrix convention, stationary law, inner product, update clock, and exact target (Poincaré gap, absolute gap, generator gap, or indexed eigenvalue).

For reversible kernels, the Dirichlet form and Rayleigh quotient give the fixed-kernel Poincaré gap. If the stationary law moves, either differentiate the full symmetric conjugate or work in the moving weighted inner product; at a repeated eigenvalue use an isolated spectral subspace and the directional compression. A stationary-law derivative or static correlation inequality alone is not a spectral-gap derivative.

Choose a certified enclosure route only when its full hypotheses and index-identification step are available. An all-index interval inclusion plus strict disjointness can isolate an ordered eigenvalue; a nearest-spectrum residual bound, an invariant-block interval, or an overlapping cluster inclusion cannot do so by itself. The source-specific conditions and limits are in the operator routes（本机附件：`references/l01-operator-perturbation-tools.md`） and [the source register](references/sources.md). See the method map（本机附件：`references/method_coverage.md`）, worked positive and failure cases（本机附件：`references/cases.md`）, and [the derivations and proof workflow](references/method.md).

Report exact arithmetic, validated interval arithmetic, and floating-point exploration separately. A finite exact calculation checks its displayed instance; it does not prove a uniform parameter claim or a general theorem.

## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).
