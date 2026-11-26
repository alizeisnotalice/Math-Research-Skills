# Aptekarev gamma pairs from a finite Jacobi--Laguerre formula

## Source and actual proof step

Khodabakhsh Hessami Pilehrood and Tatiana Hessami Pilehrood, *Rational
approximations for values of the digamma function and a denominators
conjecture*, arXiv:1004.0578v1 (2010), local PDF SHA-256
`225d48f305e7709c3b0a80c216f50ac8bdf18500c160aecfea213e57a112714b`.
This component uses the pinned preprint text, rather than assuming that its
pagination is the same as a later publication.

Physical pp. 3--4, Theorem 1 and its `a=0,b=1` specialization (5), give
the finite sequences

\[
 q_n=\sum_{k=0}^n {n\choose k}^2(n+k)!,
\]

\[
\begin{aligned}
 p_n={}&\sum_{k=0}^n {n\choose k}^2(n+k)!H_{n+k}\\
 &-2\sum_{k=1}^n\sum_{m=0}^k\sum_{\ell=0}^{n-k}
 \frac{(-1)^{m+k}}{k}{n\choose k+\ell}{k\choose m}
 {n-k\choose\ell}(m+n+\ell)! .
\end{aligned}
\]

They give the Aptekarev rational approximants `p_n/q_n` to \(\gamma\).
The source's proof of the displayed finite identity is read at physical
pp. 8--10: Lemma 3 reduces the Jacobi--Laguerre integral to `p_n,q_n` by
integration by parts, then evaluates the finite terms using Lemmas 1--2 and
the digamma shift identity.  The source's asymptotics are proved separately
by saddle/Laplace analysis on pp. 11--12; this component does not use those
asymptotics as a finite certificate.

## Exact finite use

The companion script evaluates these finite sums with SymPy integers and
rationals.  It checks the known initial values

\[
 (p_0,p_1,p_2)=(0,2,31),\qquad(q_0,q_1,q_2)=(1,3,50),
\]

and reports the exact reduced rational `p_n/q_n`.  It is appropriate for
coefficient generation, recurrence comparison, or finite denominator/gcd
experiments.  It deliberately does not evaluate \(\gamma\) or infer an
error bound from the finite data.

## Boundary

Although the preprint states a subexponential approximation asymptotic,
that fact alone is insufficient for irrationality after a chosen integer
scaling.  A claimed irrationality application must separately establish its
actual integral linear form, all denominator clearing, nonvanishing, and
smallness after the same scaling.  No such conclusion follows from a finite
replay of these coefficient sums.
