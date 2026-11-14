# Positive example: derive the uniform-leaf Beta-splitting recurrence

Suppose the target is (D_n), the continuous-time height of one uniformly chosen leaf in the critical Beta-splitting tree. Preserve the ordered split kernel
\[
q(n,i)=\frac{n}{2h_{n-1}i(n-i)}
\]
and the independent root holding time (	au_n\sim\operatorname{Exp}(h_{n-1})). Given a split of sizes (i,n-i), a uniform leaf enters the first child with probability (i/n), otherwise the second. By symmetry, the probability that its selected child has size (k) is
\[
2q(n,k)\frac{k}{n}=\frac1{h_{n-1}(n-k)}.
\]
Therefore, with (D_1=0),
\[
D_n\overset d=\tau_n+D_{K_n},\quad \mathbb P(K_n=k)=\frac1{h_{n-1}(n-k)},\quad 1\le k<n,
\]
and hence
\[
\mathbb ED_n=\frac1{h_{n-1}}\left(1+\sum_{k<n}\frac{\mathbb ED_k}{n-k}\right).
\]
This is the recurrence in RT002, PDF p. 6, equation (2.3); RT002's proof supplies the needed asymptotics and CLT. The kernel and small-(n) recurrence checks in W22's saved numeric artifact are verification aids, not a replacement for that proof.

The statement is source-matched because it retains critical Beta kernel, CTCS time, one uniform leaf and the source boundary value. It says nothing by itself about the maximum height or any pair covariance.
