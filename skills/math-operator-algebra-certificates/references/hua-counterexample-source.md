# Hua–Bellman counterexample: verified scope

Source: Suvrit Sra, *Positive definite functions of noncommuting contractions, Hua-Bellman
matrices, and a new distance metric*, v1 author preprint (local SHA-256
`6d80f678b88c39a0f1f764aca1439ab53cabb1aeddae8f8fcc224ea941c58a62`), physical p. 3.

The source lists six integer `2 x 2` matrices, scales each as `A_j = raw_j/(2||raw_j||_op)`, and
claims the associated `6 x 6` matrix with entries `det(I-A_i^T A_j)^(-1/2)` has a negative least
eigenvalue.  The supplied script independently recomputes this with ball arithmetic; at 256 bits it
encloses the least real eigenvalue near `-0.0012065843326792777`, strictly below zero.

This verifies only the displayed finite counterexample.  The preprint’s positive-definiteness
ranges rely separately on alpha-permanent and cone-theoretic inputs and are not certified here.
