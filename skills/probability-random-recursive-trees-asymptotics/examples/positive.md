# Positive examples: source-matched recurrence and scoped routes

## Critical Beta-splitting CTCS mean recurrence

Use the critical split kernel
\[
q(n,i)=\frac{n}{2H_{n-1}i(n-i)},\qquad 1\le i<n,
\]
with independent root holding time `τ_n ~ Exp(H_(n−1))`. If one leaf is selected uniformly, the probability that its child has size `k` is
\[
\mathbb P(K_n=k)=2q(n,k)\frac{k}{n}=\frac{1}{H_{n-1}(n-k)}.
\]
Thus, with `D_1=0`,
\[
D_n\overset d=\tau_n+D_{K_n},\qquad
\mathbb E D_n=\frac1{H_{n-1}}\left(1+\sum_{k=1}^{n-1}\frac{\mathbb E D_k}{n-k}\right).
\]
This is the exact recurrence admitted from RT002, physical p. 6, Eqs. (2.1)–(2.3). RT004's separately accepted finite harmonic-binomial identity gives
\[
\mathbb E D_n=\sum_{j=1}^{n-1}\frac{(-1)^{j-1}\binom{n-1}{j}}{H_j}.
\]
The finite identity has the R10-audited convolution proof; the Mellin route in RT004 additionally requires its stated strip, integrability and fixed-truncation conditions. This interface does not certify RT002's held p. 24 uniform edge-variance remainder, a CLT, or a pair theorem.

The L12 exact-rational check at recursive_cases.py（本机附件：`evidence/calculations/recursive_cases.py`） verifies normalization, size-biasing and equality of the two mean expressions for `n=2,…,20`; the output is saved here（本机附件：`evidence/calculations/recursive_cases.actual.json`）. The finite calculation is not the proof of either source theorem.

## Weighted recursive comparison: one lineage only

For the exact Kolesnik uniform-leaf child-size law `P(I_n=i)=1/[H_(n−1)(n−i)]`, a nonnegative finite sequence with the stated `ell_n=log(n)+1_(n=1)` weight, finite initial bounds and forcing `O(log^(-5/2)n)` satisfies the admitted Claim 3.5 comparison error `O(log^(-1/2+epsilon)n)` for sufficiently small `epsilon>0`. This is one G23.03 lineage interface. It supplies neither the paper's unaccepted CTCS coefficient/adaptation nor a two-leaf fixed-gap limit. See the internal Kolesnik usage card（本机附件：`evidence/r12_usage_cards/EXSRC-3a876a54df00ac46.md`）.
