# Tamed Lévy-Euler freezing-error ledger

## Source and scope

H. Zhang and M. Zhang, *Tamed Euler Schemes for Singular SDEs with
Multiplicative Lévy Noise*, arXiv:2607.18862v1, 21 July 2026. The supplied
83-page preprint is used at physical pp. 62--69.

This note is a conditional bookkeeping method for a tamed Euler scheme after
the source's Zvonkin transform. It separates two small-jump freezing errors. It
does not certify general strong convergence of a Lévy SDE or a compensator for
an arbitrary random measure.

## Conditional error split

Require a caller to provide the exact source model and verify Conditions
`(H_gsigma)`, `(cH_gsigma)`, `(H_b)`, the transformed solution `u`, the
predictability and integrability of the Poisson integrands, and the stated
increment estimates for the frozen Euler path.

For the transformed error, retain separate entries:

- `W8`, the compensated-Poisson martingale freezing term; and
- `W9`, the deterministic nonlocal compensator freezing term.

For exponent `pbar >= 2`, Proposition 8.7 gives

`E W8_1 <= C_J^(m) n^(-(1-1/q))`

and

`E W9_1 <= C_J^(c) n^(-(1-1/q)(1-d/p))`.

For `1 < pbar < 2`, the respective powers are `n^(-pbar/2)` and
`n^(-(pbar/2)(1-d/p))`. The `W8` bound uses the compensated-Poisson maximal
inequality in Lemma 8.4 and the spatial maximal-function estimate. The `W9`
bound uses the source's second-order nonlocal increment estimate and the
Euler-path Krylov/increment input. Neither term may be silently merged into a
Brownian discretization rate.

## Closure boundary

Proposition 8.8 may place the two terms in a stochastic-Gronwall closure only
after the required exponential integrability of its random controls has been
established. The headline rate also contains drift approximation, Zvonkin,
Brownian, taming, ellipticity and parameter restrictions. In particular, the
source's Corollary 2.9 imports its estimate for `varpi_b^n`; it is not a
standalone rate certificate.

## Dependency boundary

The caller must certify the source form of the compensated-Poisson maximal
inequality, its predictable integrand conditions, the nonlocal increment
estimate, and the claimed Euler increment/Krylov estimates. This reference
does not apply to large jumps, another truncation convention, state-dependent
random compensators, or a model without the displayed Sobolev and
integrability conditions.
