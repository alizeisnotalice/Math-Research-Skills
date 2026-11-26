# Prime-order affine medial-rack replay

Scoped reference for Horace Maxwell, *The smallest non-2-reductive medial racks*
(November 2026 author manuscript), SHA-256
`f957e18c52d09b7cabea84f1e1ea36e4bd7e6e0225373d85bdf8de6372ebe36d`.

## Source locus and extracted operation

Theorem 7 (p. 1; proof pp. 4--6) identifies the prime-order non-2-reductive
medial example with the affine operation on \(\mathbb Z/p\mathbb Z\)

\[
 x*y=(1-\lambda)x+\lambda y,
 \qquad \lambda\in(\mathbb Z/p\mathbb Z)^\times\setminus\{1\}.
\]

For a supplied prime \(p\) and residue \(\lambda\), the replay enumerates the
finite operation table and checks idempotence, bijectivity of every left
translation, left self-distributivity, mediality, and failure of the displayed
2-reductive identity.  Thus it validates a concrete affine witness rather than
relying on a diagram or informal table transcription.

## Replay boundary

`scripts/check_recent05_affine_prime_medial_rack.py --self-test` uses integer
modular arithmetic and exhaustively checks the finite identities.  Its negative
test sets \(\lambda=1\), which must be rejected because the operation becomes
2-reductive.  It does not decide whether an arbitrary supplied rack is affine,
prove the source's classification theorem, or compare isomorphism classes.
