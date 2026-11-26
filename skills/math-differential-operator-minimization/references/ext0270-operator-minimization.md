# Exact minimization for a specified differential-equation solution

Bost, Rivoal and Salvy, arXiv:2209.01827v3, define homogeneous minimization for
a polynomial-coefficient operator and a uniquely specified rational formal solution.
Physical pages 6--9 give Algorithm 1 and Theorem 2.2. For each candidate order, the
algorithm obtains a degree bound, an approximant basis for the solution and its
derivatives, takes a greatest common right divisor with the input operator, and tests
the selected solution's initial data. The theorem proves a nonzero minimal-order right
factor once these exact subroutines and the source termination argument are used.

The interface requires an exact \(\mathbb Q[z]\langle\partial_z\rangle\) operator,
the indicial data at zero, initial data for a unique \(\mathbb Q[[z]]\) solution, the
source degree-bound computation, exact Ore GCRD arithmetic, and a sufficiently precise
series extension. The source's Maple implementation is evidence for its examples only.
No finite truncation or generic operator factorization by itself certifies minimization.

For E-functions, the paper's later algebraic-value algorithm has additional
desingularization and specialization conditions. This reference imports only the
minimization theorem.
