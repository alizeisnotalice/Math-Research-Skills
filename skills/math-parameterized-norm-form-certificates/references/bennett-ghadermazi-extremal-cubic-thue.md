# Bennett--Ghadermazi extremal cubic family

## Publication check

M. A. Bennett and A. Ghadermazi, *Extremal families of cubic Thue equations*,
*Journal de théorie des nombres de Bordeaux* **27** (2015), no. 2, 389--403,
DOI [10.5802/jtnb.907](https://doi.org/10.5802/jtnb.907). The local source is
arXiv:1402.2005v1; its physical pp. 2--3 state the same Theorem 1.2 used here.

## Exact statement used

For every integral `t`, Theorem 1.2 states that

```
F_{3,t}(x,y) = x^3 - (t^4-t)x^2 y + (t^5-2t^2)xy^2 + y^3 = 1
```

has the five integral solutions

```
(1,0), (0,1), (t,1), (t^4-2t,1), (1-t^3, t^8-3t^5+3t^2),
```

and, only when `t=-1`, the additional solution `(6,-5)`. The local PDF derives the
large-parameter route through root types, units, logarithmic forms and lattice reduction
(pp. 3--11); the installed exact evaluator checks the displayed identities alone.

## Non-transfer

No completeness statement follows from evaluating these candidates. The theorem does
not cover different cubic coefficients, a right-hand side other than `1`, or nonintegral
parameters.
