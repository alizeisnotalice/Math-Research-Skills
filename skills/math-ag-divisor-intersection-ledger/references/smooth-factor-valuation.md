# Gauss extension across one smooth factor

## Contract

Let `(Y,y)` be an `N`-dimensional klt germ over a characteristic-zero field,
with `N >= 1`, completed local ring `R`, and a supplied divisorial valuation
`v` centered at `y`. Assume it has finite log discrepancy `A>0` and that its
valuation ideals satisfy the volume asymptotic

\[
 \ell(R/\mathfrak a_s(v))=\frac{\sigma}{N!}s^N+o(s^N)
 \quad(s\to\infty),
\]

with the usual real-index convention. These are inputs, not checks performed
by this method. Let `a=A/N` and define `w=v\oplus a` on `R[[t]]` by the
Gauss formula in the skill entrypoint.

Then `w` is the monomial extension on a log model containing the divisor for
`v` and `t=0`, so

\[
 A(w)=A+a.
\]

For every positive cutoff `k`, decomposition by the powers of `t` gives

\[
 \ell\bigl(R[[t]]/\mathfrak a_k(w)\bigr)
 =\sum_{0\le i<k/a}\ell\bigl(R/\mathfrak a_{k-ia}(v)\bigr).
\]

Divide by `k^(N+1)/(N+1)!`. The assumed length asymptotic, with a finite
initial segment isolated if necessary, turns the right-hand side into the
Riemann sum

\[
 \frac{\sigma}{a N!}\int_0^1 x^N\,dx=\frac{\sigma}{a(N+1)!}.
\]

Hence `vol(w)=sigma/a`. Substitution of `a=A/N` now gives the exact identity

\[
 \frac{(A+A/N)^{N+1}(\sigma/(A/N))}{(N+1)^{N+1}}
 =\frac{A^N\sigma}{N^N}.
\]

This is an independent derivation of the reusable calculation. It is the
test-valuation step used in Lemma 2.1 of *The ordinary-double-point gap in
every dimension*, OpenAI pinned preprint commit
`3344da59991ed94f9ba711217b29c1d760badfa6`, SHA-256
`5e2cdac4857afef7065967c49c6f4f9a1aec01b0b776ce324220707545e8e114`,
physical pp. 7--8.

## Consequence and boundary

If a normalized invariant is defined as the infimum of
`A(u)^d vol(u)/d^d` over the relevant divisorial tests in dimension `d`, this
single test proves

\[
 d((y,0),Y\times\mathbb A^1)\le d(y,Y).
\]

It does **not** prove that `v` minimizes, that a minimizer exists or is unique,
that all valuations are divisorial, or an equality for the infima. It also
does not apply with `A<=0`, `N=0`, a non-divisorial supplied test without a
justified monomial model, or absent control of the stated length asymptotic.
