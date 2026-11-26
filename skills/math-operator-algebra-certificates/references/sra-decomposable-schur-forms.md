# Decomposable-curvature Schur-form source contract

Source: Suvrit Sra, *Weak positivity of Schur forms under decomposable curvature*, author preprint v1, 37 physical pages; reviewed physical pp. 1--5 and 19--21.  Local source identity: SHA-256 `25eb3c90d1d5d56ef9e46e27761a82369e027bad5425e410e40621cee64ccf52`.

For a curvature map with a supplied decomposition

\[
H(X)=\sum_a A_aXA_a^*+\sum_b B_bX^TB_b^*,
\]

the source states nonnegativity of its double mixed determinant and weak nonnegativity of all Schur forms.  The determinant route uses a quaternionic Gaussian formula.  The move from determinant positivity to all Schur forms uses Finski's quotient stability and incidence construction.

## Use boundary

Verify the actual finite-dimensional Kraus decomposition and all input/output dimensions for the caller.  Keep the result confined to decomposable curvature; the source itself records obstructions outside that cone.  The Gaussian determinant identity and Finski inputs are dependencies, not certificates produced by this reference.
