# bbmhd10 — Bootstrap percolation in high dimensions

**Reading status:** `fulltext_read`; complete 51-page local paper read, PDF pp. 1–51. The displayed threshold formulas and the critical-droplet estimate were checked on rendered original PDF pp. 3 and 5; Theorem 38 was checked on p. 41. R03 approved the strict-v2 scope; the reading status and source-specific limits above remain unchanged.

**Reference:** József Balogh, Béla Bollobás, and Robert Morris, “Bootstrap Percolation in High Dimensions,” arXiv:0907.3097v3 (14 July 2010); *Combinatorics, Probability and Computing* 19(5–6) (2010), 643–692, DOI [10.1017/S0963548310000271](https://doi.org/10.1017/S0963548310000271). Local PDF SHA-256: `6d08d1fac61c45173971194526b8d867c481656ee805462f638ab558761e56b8`.

## Model and main results

The model is two-neighbour vertex-bootstrap percolation on ([n]^d): iid Bernoulli((p)) initial infected sites, nearest-neighbour graph, and an empty site becomes infected once it has two infected neighbours. Throughout the paper, (log) is base 2 unless stated otherwise, and (d\gg\log n\ge1).

Let λ≈1.16577 be the smallest positive root of

\[
\sum_{k=0}^{\infty}\frac{(-1)^k\lambda^k}{2^{k^2-k}k!}=0.
\]

Theorem 1 gives, for sufficiently large (d),

\[
\frac{16\lambda}{d^2}\left(1+\frac{\log d}{\sqrt d}\right)2^{-2\sqrt d}
\le p_c([2]^d,2)\le
\frac{16\lambda}{d^2}\left(1+\frac{5(\log d)^2}{\sqrt d}\right)2^{-2\sqrt d}.
\]

Theorem 2, for every (n=n(d)) with (d\gg\log n\ge1), gives

\[
p_c([n]^d,2)=(4\lambda+o(1))\left(\frac n{n-1}\right)^2\frac1{d^2}
2^{-2\sqrt{d\log_2 n}}.
\]

Here (p_c) is the paper’s median percolation threshold, not a running time. Theorem 3 controls the probability (P(\ell,p)) that a small hypercube is internally spanned and (Q(\ell,p)) for the more restrictive sequential-spanning event, under its stated smallness hypothesis `ℓ² 2^(2ℓ) p ≤ δ`. This critical-droplet estimate is the main technical input to the lower threshold bound.

## Proof route and scope

Section 3 proves the critical-droplet estimates by counting sequentially spanning sets, classifying possible final pairs, and deriving recurrences for the spanning probabilities. A delicate induction bounds even- and odd-dimensional cases; the proof explicitly depends on accurate constants and small base cases. Section 4 uses internally spanned subcubes, a second-moment estimate and sprinkling to obtain the upper threshold. Section 5 uses a cube-merging process, comparison of internally spanned shapes, disjoint-pair counting and BK to show that below the stated scale no critical droplet is likely.

The theorem is specific to iid two-neighbour bootstrap percolation on grids in the high-dimensional regime. It does not extend the fixed-dimensional three-neighbour result, does not give infection-time tails, and does not justify claims for tori where the paper notes its lower-bound coupling can fail (with a concrete failure at side length 3).

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/bbmhd10`).
