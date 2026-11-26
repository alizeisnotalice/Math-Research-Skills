# Fischler--Rivoal: fixed-base rational approximation of G-values

## Checked source and version

S. Fischler and T. Rivoal, *Rational approximation to values of G-functions, and
their expansions in integer bases*, arXiv:1512.06534v2 (11 October 2017), local PDF
physical pp. 1--6. The author publication list identifies the version of record as
*Manuscripta Mathematica* **155** (2018), no. 3--4, 579--595; the same listing records
an addendum at pp. 597--598. The local source's title page, Theorem 2 and Corollary 1
agree on the fixed-base approximation interface used here.

## Admitted statement

For a G-function `F` with rational Taylor coefficients and `F(z) notin Q(z)`, and a
fixed `t >= 0`, Theorem 2 (physical p. 3) supplies positive effectively computable
constants `c1,c2,c3,c4`, depending only on `F` (and `t` for `c3`). If `a != 0`,
`b,B >= 1`,

```
b > (c1 |a|)^c2,     B <= b^t,
m >= c3 log(b) / log(|a|+1),
```

then every integer `n` satisfies the displayed lower bound for
`|F(a/b) - n/(B b^m)|`; equivalently it has denominator factor `B b^m` and an additional
`(|a|+1)^(c4 m)` factor. Corollary 1 (physical p. 4) gives a simpler
`b^(-m(1+epsilon))` lower bound only after its own sufficiently-large requirements.

The digit statement is Theorem 3 (physical pp. 5--6). It concerns the b-ary expansion
of the stated rational evaluation and has source-dependent lower bounds on the relevant
base power and position. It is not a claim about an arbitrary real number or arbitrary
analytic function.

## Boundary

This reference is a conditional theorem interface. It neither computes the constants
from an informal differential equation nor proves that a caller's series is a G-function
or non-rational. In particular, no threshold may be replaced by a numerical guess.
