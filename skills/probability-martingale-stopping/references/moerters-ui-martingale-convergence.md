# Uniformly integrable discrete-time martingale convergence

## Source and identity

Peter Mörters, *Lecture Notes on Martingale Theory*, Chapter 1, *Martingales:
Basic Properties and Stopping Theory*. The notes are linked as “Lecture Notes
on Martingale Theory” from the author's University of Cologne homepage. The
supplied 32-page PDF has the same pagination as that hosted source; Theorem
2.6 was visually checked on physical p. 17 and Theorem 2.7 on physical p. 19.

## Callable result

For a discrete-time martingale `(X_n,F(n))`, first certify that the family
`{X_n:n>=0}` is uniformly integrable. Then Theorem 2.6 supplies an almost
surely finite integrable random variable `X` such that

`X_n -> X` almost surely and in L1,

and, for every `n`,

`X_n = E[X | F(n)]`.

Conversely, if `X` is integrable, `F(n)` is an increasing filtration, and `X`
is measurable with respect to `sigma(union_n F(n))`, then Theorem 2.7 says
that `E[X | F(n)]` is a uniformly integrable martingale converging to `X`
almost surely and in L1.

## Boundary

This is a discrete-time theorem. L1 boundedness alone gives at most the
source's almost-sure martingale-convergence route and does not replace uniform
integrability for the asserted L1 convergence or terminal conditional-
expectation representation. Continuous-time processes, local martingales,
non-nested sigma-algebras, and stopping-time limit passages require separate
hypotheses and results.
