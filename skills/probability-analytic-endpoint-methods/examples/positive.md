# Positive route: scalar Calderón–Zygmund weak type

**Request.** Audit a proposed weak-(1,1) estimate for a scalar-output operator T on Euclidean R^n.

**Source match.** AEP-009 Theorem 1 applies when T has the source’s kernel size estimate and two-variable Hölder smoothness, is bounded on L2, and has the stated off-support integral representation. The proof uses Whitney good/bad decomposition, matched-measure cancellation sets, kernel smoothness and an L2 estimate. Under those assumptions, report an implicit weak-(1,1) constant depending on T and n; the theorem does not claim a sharp or dimension-free constant.

**Check before transfer.** State the input class and dense extension, truncation realization, threshold convention, and all kernel/L2 constants. If the desired measure is w(x)dx, do not reuse the paper’s printed weighted proof until its arbitrary-set affine-dilation step is independently established; doubling alone does not imply it. The source and proof boundary are in the [AEP-009 card](../evidence/W25/cards/AEP-009.md).

**Related scalar-coordinate request.** For a real scalar Riesz coordinate and 1<p<infinity, AEP-007 can be used only with its f** rearrangement weak-Lp quantity. Its positive-part constant is the one claimed sharp; the full absolute-value estimate has twice that upper constant. This does not give p=1 or a vector norm estimate.
