# Finite-scale quadratic exponential-sum tube-weight estimate

Source: Xuerui Yang, *Some Mizohata--Takeuchi-type estimate for exponential
sums*, arXiv:2511.00841v1 (2 November 2025), local SHA-256
`05e61d742fd53fe311c8aa1f5d6087538e48b9e7d755fb812b144a976def1480`.

## Caller contract

Let `sqrt(R)` be an integer, let `omega>=0` be a weight on the radius-`R`
ball `B_R` with `omega(B_R)<=R`, and let `(a_n)_{1<=n<=sqrt(R)}` be complex.
For

\[
 G(x,t)=\sum_{n=1}^{\sqrt R}a_n
 e\!\left(\frac n{\sqrt R}x+\frac {n^2}R t\right),
\]

the source's Theorem 1.5 states

\[
 \int_{B_R}|G|^2\omega
 \lesssim_\epsilon R^\epsilon
 \Bigl(\sup_{T:\,R\times R^{1/2}\ \mathrm{tube}}\omega(T)\Bigr)^{1/2}
 R\sum_n|a_n|^2.
\]

This is specific to this finite quadratic sum and this total-mass condition.
It does **not** prove the same assertion for a general convex curve; the
source gives a contrary construction in Lemma 6.2.

## Proof interface retained for use/audit

1. Rescale to `N=sqrt(R)` and select one `N^{-1} by N^{-2}` box from each
   horizontal strip.  Theorem 1.6 gives the discrete `L^4` estimate
   `||sum_{n<=N} a_n e(nx+n^2t)||_{L^4(E)} \lesssim N^{-1/4}||a||_2`
   (physical p. 3).
2. The proof converts it to a local `L^2` bound on any `M` selected strips
   through the locally constant property and duality (physical pp. 4, 7--8).
3. On the major arcs, circle-method kernel decomposition reduces the needed
   bilinear form to a rational-incidence count.  Lemma 4.1 bounds that count;
   the minor-arc part follows from the pointwise `N^{1/2}` kernel bound
   (physical pp. 5--10).
4. Decompose the weight into dyadic `|G|` levels.  The level-set count turns
   the selected horizontal-strip estimate into the theorem's tube supremum
   (physical pp. 4--5).

## Boundary

This reference is an analytic theorem with an `R^epsilon` implicit constant,
not a finite exact Schur certificate.  It must retain the integrality of
`sqrt(R)`, the precise phase scaling, and `omega(B_R)<=R`; checking sampled
tubes cannot establish its all-tube supremum.

Locators: physical pp. 2--5 and 8--11; Theorems 1.5--1.6, Lemmas 4.1 and
4.3, and Lemma 6.2.
