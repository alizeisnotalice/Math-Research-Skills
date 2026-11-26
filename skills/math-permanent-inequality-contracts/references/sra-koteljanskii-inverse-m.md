# Koteljanskii inequality for symmetrizable inverse M-matrices

Source: Suvrit Sra, *A Koteljanskii inequality for permanents*, author preprint v1, 9 physical pages; reviewed physical pp. 1--6.  Local source identity: SHA-256 `783c4168003ca8ba2325f17e3b6eb1a56c5058cff63e73835978d670a94ae484`.

For a positively diagonally symmetrizable inverse M-matrix (A), the source states log-supermodularity of principal permanents:

\[
\operatorname{per}(A_{S\cup T})\operatorname{per}(A_{S\cap T})
\geq \operatorname{per}(A_S)\operatorname{per}(A_T).
\]

Here the stated matrix class includes entrywise nonnegativity, an inverse with nonpositive off-diagonal entries, and a positive diagonal similarity to a symmetric matrix.  The proof represents permanents as complex-Gaussian moments and invokes Ginibre correlation and the Karlin--Rinott MTP2/FKG result.  The source includes a nonsymmetrizable counterexample, so the similarity premise must not be dropped.

## Finite-instance contract

`scripts/check_koteljanskii_inverse_m.py` verifies the rational matrix-class premises and every subset-pair inequality for a supplied finite matrix.  That output is an exact certificate for that matrix only; it is not an independent proof of the Gaussian, Ginibre, or FKG inputs behind the general theorem.
