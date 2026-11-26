# Selected-sequence and labelled-lift references

## Scoped reference. Bochner--Riesz particle-score compactness

Source: *Bochner--Riesz multipliers in three dimensions*, family 078, SHA-256 `ea18d159eefcdc7fff031ab14035ecba7205de156a7fcd747a6a9c6bd0d6762a`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026/Bochner-Riesz-Multipliers-in-Three-Dimensions-September-24-2026.pdf), physical pp. 2--4 and 15.

1. Input a scale-indexed finite family of particle/observation laws, compact parameter set, score envelopes, and the explicit stability estimate under convergent parameters.
2. First fix the requested output loss and all bounded-box enlargements. Then take a sequence approaching a putative envelope supremum; pass to the selected sequence only after checking the averaged conditional-law bound survives the conditioning partition.
3. Output is a selected-sequence reduction: a limsup estimate along every admissible selected sequence implies the stated `o(1)` envelope bound for that fixed construction.

Boundary: this reduction is conditional on the score/stability contract and does not supply the paper's planar Furstenberg input, packet capacity argument, or the \(L^3\) Bochner--Riesz theorem. The order is strict: do not let the loss tend to zero while claiming a uniform constant.

## Progression-separated first-match lift

Source: *An L3 bound for the trilinear Hilbert transform*, family 086, SHA-256 `24b584066ae76b2f28dc03d32a2b0a2cdc3b4f92e0e82f4a3d133f28ccc5a936`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-L3-bound-for-the-trilinear-Hilbert-transform-October-5-2026/paper.pdf), physical pp. 20--21 (Lemma 4.5) and pp. 65--66 (Lemma 8.1).

1. Input two bounded quadratic-chart atoms in distinct slots of a four-term progression, with declared Gevrey complexity and an interval-scale support condition.
2. Insert bounded coordinate partitions, use the affine progression identities to separate the two chart phases into the remaining two slots and the step variable, then Fourier-expand the compact coupled amplitude. Keep shellwise coefficient budgets and do not truncate before retaining the stated tail error.
3. At a permanently labelled first match, freeze one splitting, attach private mode coordinates, and build the pointwise lift using sufficiently small private weights. Output is a finite mode expansion with common quadratic coefficient per primary and a bounded cell-local synthesis operator.

Boundary: this is not an \(L^3\) trilinear Hilbert estimate. It requires the source's chart-complexity, coefficient, rank, and branch-budget data; a lift is pointwise and must not be commuted through an unrelated projection.
