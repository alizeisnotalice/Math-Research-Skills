# Recursive skew-Hadamard family: verified scope

Source: Hao Shen, Jiaqi Wang, and Lihong Zhi, *A Dimension-Independent Commutator Bound*,
author preprint (local SHA-256 `5e142fbf0cc1f7dfb6643c8f4d6360669c5aa8d93c9187f280f8062c28cf5eed`),
physical p. 18, equation (4.3), Lemma 4.1, and equation (4.5).

The source recursively defines `S_(2n)` from `S_n`, and proves that for powers of two it is real
skew-symmetric, zero diagonal, has off-diagonal signs, and obeys `S_n^2=−(n−1)I`.  Thus the
normalized `A_n=iS_n/sqrt(n−1)` is a Hermitian unitary with zero diagonal.

The paper's optimal-paving, diagonal-commutator, and global uniform-commutator claims need
additional sections, including a Marcus–Spielman–Srivastava vector-selection input.  This helper
does not certify those claims.
