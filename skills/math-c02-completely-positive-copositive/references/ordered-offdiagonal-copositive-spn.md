# Ordered off-diagonal copositive matrices

Source: G. Blekherman, P. Parrilo, and R. Thomas, *Copositive Matrices with
Ordered Off-Diagonal Entries*, arXiv:2605.15970v1, Theorem 3.5 and Lemma 3.6
(physical pp. 5--7).  This is a preprint source statement.

## Narrow rule

For a symmetric matrix whose off-diagonal entries have first been put in the
paper's prescribed order, use the paper's induction only when copositivity is
already an independently established premise.  The conclusion is that the
matrix is SPN in the source's ordered class.  The induction removes the
prescribed row/column and invokes the low-dimensional identity
`COP_4 = SPN_4`.

This is a classification implication, not a copositivity test and not a
rational SPN-decomposition algorithm.  Preserve the ordering permutation,
the exact matrix convention, and the caller's copositivity certificate.
