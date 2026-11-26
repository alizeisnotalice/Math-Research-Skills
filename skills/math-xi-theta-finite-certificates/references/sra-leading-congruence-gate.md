# Leading-principal-minor congruence gate

Source: Suvrit Sra, *On some positivity properties of the Riemann Xi function*, author preprint v3 / arXiv:2611.02944v1, local SHA-256 `d3cd19f47a11051eb024ca7f81e9f7c799c1e407ad076a3f3854975873fdcab4`, physical p. 50.  The source says that its fixed lower-triangular polynomial-basis congruence preserves the signs of all leading determinants of its normalized derivative matrix.

The exact finite statement is as follows.  Let \(A\in\mathbb R^{n\times n}\), let \(L\) be lower triangular with every diagonal entry nonzero, and set \(B=LAL^{\mathsf T}\).  Denote the leading \(k\)-by-\(k\) blocks by \(A_k,L_k,B_k\).  Lower triangularity gives

\[
B_k=L_kA_kL_k^{\mathsf T},\qquad
\det B_k=(\det L_k)^2\det A_k
=\left(\prod_{i=1}^k L_{ii}\right)^2\det A_k.
\]

Thus every leading determinant has the same strict sign before and after the congruence; a zero is preserved too.  The proof is the displayed block identity followed by multiplicativity of determinant.  `scripts/check_leading_congruence.py` uses exact `fractions.Fraction` arithmetic to replay the block identity and determinant formula for mixed-sign and singular-leading dyadic examples.

## Required caller evidence

For a source-specific matrix certificate, supply the fixed basis matrix \(L\), prove it is lower triangular with nonzero diagonal, and supply the matrix enclosure \(A\) with a determinant-sign certificate.  This gate transfers those already-certified leading-minor signs only.  It does not evaluate Xi, certify any zero, bound a remainder, establish a PF order, or repair the missing v3 selected-zero/interval/cover payload.
