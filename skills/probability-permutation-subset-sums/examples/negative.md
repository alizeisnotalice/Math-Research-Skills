# Negative example — expected representation count is not a probability

For a uniform permutation of `[n]` and a fixed `k≤n`, let `R_k` be the number of invariant `k`-subsets. For each fixed `k`-subset `A`, the probability that a uniform permutation maps `A` to itself is `k!(n−k)!/n! = 1/binom(n,k)`. Summing its indicator over all `binom(n,k)` choices gives `E[R_k]=1`.

At `k=1`, however, `P(R_1≥1)` tends to `1−e^(−1)`, not 1. Therefore `E[R_k]=1` does not answer whether at least one cycle subcollection sums to `k`. The positive-probability event is Boolean reachability; multiple representations and their dependence cannot be ignored.

The argument computes a first moment and one limit exactly. It does not determine adjacent monotonicity for general `k`.
