# Adaptive-metric outer approximation: conditioned transfer only

Local source: M. Alshahrani, *Adaptive Metrics for
Norm-Minimization-Based Outer Approximation in Convex Vector Optimization*,
arXiv:2605.14320v3 as identified in the supplied PDF, Lemmas 11 and 13 and
Theorems 12 and 14 (physical pp. 14--18).  The public arXiv landing page
currently displays materially different older claims, so this reference is to
the checked local v3 bytes only, not a claim about the current online version.

## Conditioned rule

For a compact convex slice `A`, exact norm-minimization scalarizations, valid
dual supporting cuts, and the farthest-vertex rule, assume every adaptive
matrix satisfies

`m I <= M_k <= M I` with `0 < m <= M < infinity`.

Then Rayleigh quotients give
`sqrt(m) d_2(v,A) <= d_Mk(v,A) <= sqrt(M) d_2(v,A)`.  A vertex maximizing the
metric distance has Euclidean distance at least `sqrt(m/M)` times the maximum
Euclidean vertex error.  The source's nested exact-cut argument then gives
Euclidean Hausdorff convergence; its packing proof gives the stated improved
rate only under the same uniform conditioning.

The local source obtains the bound from `M_k = epsilon_0 I + Sigma_k`, namely
`epsilon_0 I <= M_k <= (epsilon_0+1) I`.  Without a uniform positive lower
spectral bound, a small metric residual does not control Euclidean error and
neither convergence rate nor empirical improvement is licensed here.
