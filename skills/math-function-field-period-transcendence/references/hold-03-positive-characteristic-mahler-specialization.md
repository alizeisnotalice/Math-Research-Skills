# Positive-characteristic Mahler specialization

## Status and source

Scoped reference. This is a conditional specialization theorem for analytic
Mahler systems in positive characteristic; it is not a characteristic-zero
Mahler-number procedure and it supplies no automatic test for regularity.

M. A. Fernandes, [*Methode de Mahler en caracteristique non nulle : un
analogue du Theoreme de Ku. Nishioka*](https://www.numdam.org/articles/10.5802/aif.3216/),
*Annales de l'Institut Fourier* 68(6) (2018), 2553--2580,
DOI 10.5802/aif.3216.  The supplied 22-page source is a later local version;
the adoption is limited to its displayed Theorem 1.1 (physical p. 3) and the
dependencies identified below.

## Callable interface

Use this reference only after the caller has supplied all of the following in
the source's positive-characteristic setting:

1. a finite extension `K` of the relevant base field, an integer `d >= 2`,
   and functions `f_1(z), ..., f_n(z)` analytic in a neighbourhood of zero;
2. a `d`-Mahler system for that vector in exactly the form required by the
   source;
3. a point `alpha in K` with `0 < |alpha|_infty < 1`; and
4. a proof that `alpha` is regular for that system (in particular, the
   iterated Mahler orbit does not meet the singular locus specified by the
   system).

Under precisely those supplied hypotheses, Theorem 1.1 identifies the
transcendence degree over `K` of the specialized tuple
`f_1(alpha), ..., f_n(alpha)` with that of the function tuple over `K(z)`.
It is therefore a transfer step: it can convert a separately established
functional algebraic-independence result into a value statement.  It neither
establishes the functional result nor relaxes the regularity condition.

## Dependency boundary

The source explicitly routes the theorem through its Philippon criterion
(Theorem 3.1, p. 6), auxiliary-polynomial/height estimates in the proof
(p. 15), and the characteristic-positive analytic setting.  Treat those as
the published theorem's proof dependencies, not as checks performed by this
reference.  The concrete application in Theorem 5.2 (p. 20) has additional
parameters and must not be generalized beyond its stated range.

## Non-use cases

Do not use this entry for complex or `p`-adic characteristic-zero Mahler
systems, for arbitrary formal power series, or when regularity at `alpha` is
only numerical.  In those cases retain the result as an unproved candidate
until a compatible specialization theorem and its hypotheses are supplied.
