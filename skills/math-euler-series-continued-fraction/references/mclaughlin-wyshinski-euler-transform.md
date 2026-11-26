# Exact Euler transform: rational series to generalized continued fractions

## Pinned published source

J. McLaughlin and N. J. Wyshinski, *Real numbers with polynomial continued
fraction expansions*, **Acta Arithmetica** 116(1) (2005), 63--79,
DOI [10.4064/aa116-1-6](https://doi.org/10.4064/aa116-1-6).
The local journal PDF has SHA-256
`95b8f20823b88239388d96b4c2b60a23739babe576f1efde8d70ec896c6a48e5`.
Its title page and the journal archive identify the published volume, issue, and
page range.

## Callable finite identity

Source pp. 69--70, Proposition 2 and equation (3.2), state that for a
convergent series \(\sum_{i\ge0}a_i\), subject to the nondegeneracy
conditions in the displayed continued fraction,

\[
\sum_{i\ge0}a_i=a_0+\cfrac{a_1}{1+
\cfrac{-a_1a_3}{a_2+a_3+\ddots}}}.
\cfrac{-a_2}{a_1+a_2+
\cfrac{-a_1a_3}{a_2+a_3+\ddots}}}.
\cfrac{-a_1a_3}{a_2+a_3+\ddots}}}.
\]

The script exposes the **finite** version only. Given exact rational
\(a_0,\ldots,a_N\), it emits the generalized-CF coefficients and independently
re-evaluates its \(N\)-th convergent using exact continuants. The result must
equal \(\sum_{i=0}^Na_i\).

It deliberately rejects zero series increments and zero displayed denominators
\(a_{i-1}+a_i\), because then this particular Euler representation degenerates.

## Scope boundary

The equality of finite convergents is algebraic. Turning it into an infinite
identity additionally requires convergence of the original series and of the
continued fraction as supplied by Proposition 2; a finite input does not prove
either. This tool also supplies no positivity, integrality, nonvanishing, or
irrationality conclusion.
