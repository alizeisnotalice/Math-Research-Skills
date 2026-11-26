# Scoped reference. Multiple-harmonic-sum determinant

Source: Hirose--Murahara--Saito, *A determinant formula for multiple harmonic sums and their linear independence*, arXiv:2610.27767v1 (20 October 2026), local SHA-256 `a892e5d9090712505e3e623aa3fa17c60e40deaa426b86c4b76905df6176292e`, physical pp. 1--2.  A formal journal version was not located in the publication check.

For an index `k=(k_1,...,k_r)`, set `zeta_<n(k)=sum_{1<=n_1<...<n_r<n} 1/(n_1^k_1...n_r^k_r)`, with the empty index equal to one.  Enumerate indices by `k_0=empty`, `k_(2i)=k_i^up`, and `k_(2i+1)=k_i^right`, where up increments the final entry and right appends one.  The source's Theorem 1.2 gives a nonzero closed product for the `2^w` square matrix

`(zeta_<(N+r+1)(k_c))_(0<=r,c<2^w)`

for `w>=1`, `N>=0`, and hence its columns are linearly independent.

`scripts/supp_remaining_b_harmonic_determinant.py` computes the exact finite rational matrix and determinant for `w<=4`; it independently verifies only the supplied instance, not the all-`w,N` product formula.  The source's infinite-sequence corollary additionally cites earlier work, so do not use this finite replay to certify any infinite or analytic independence statement.
