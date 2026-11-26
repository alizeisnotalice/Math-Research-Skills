# Newton-series finite-harmonic duality for multiple-zeta relations

## Source and verification

- Gaku Kawashima, *A class of relations among multiple zeta values*, **Journal of Number Theory** 129(4) (2009), 755--788, DOI `10.1016/j.jnt.2008.11.002`; inspected local arXiv:math/0702824v3, SHA-256 `23bf9292e11c2dd178c702e87d9408f7d936148a2587dd4a32384373047d904b`.
- Physical PDF pp. 2--3 define the finite sums, binomial inversion, Newton interpolation, and the linear relation interface. PDF p. 14 proves Theorem 3.8 by the stated two-variable generating-function induction; p. 15 gives Corollaries 3.9--3.10. The source's broad MZV-relations claim is not re-proved here.

## Exact finite identity

For a positive index `mu=(mu_1,...,mu_p)`, let

\[
s_\mu(n)=\sum_{0\le n_1\le\cdots\le n_p=n}
\frac1{(n_1+1)^{\mu_1}\cdots(n_p+1)^{\mu_p}}.
\]

If `mu*` is the composition whose cut set is the complement of the cut set
of `mu` in `{1,...,|mu|-1}`, Corollary 3.9 states

\[
 (\nabla s_\mu)(n)=\sum_{k=0}^n(-1)^k\binom nk s_\mu(k)=s_{\mu^*}(n).
\]

The associated Newton coefficients for `S_mu(n)=sum_{0<=k<n}s_mu(k)` are
`(nabla S_mu)(0)=0` and `-(s_{mu*})(n-1)` for `n>=1` (Corollary 3.10).

## Scope

The included exact checker validates finite instances of the displayed
identity. It can support symbolic generation of Kawashima-relation inputs,
but it does not numerically establish MZV linear independence, exhaust all
MZV relations, or transfer an MZV identity to Euler's constant.
