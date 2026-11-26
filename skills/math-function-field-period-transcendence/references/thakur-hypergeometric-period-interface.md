# Thakur-hypergeometric period admission

Source checked: Ryotaro Harada, *On the period interpretation for some special values of Thakur hypergeometric functions*, arXiv:2205.00649v1 (2022), physical pp. 3--4 and 7--18 of the local copy.

## Admissible input

Work over `k = F_q(theta)`. Supply ordered positive tuples
`a = (a_1,...,a_{s+1})` and `b = (b_1,...,b_s)`, an `alpha` in `k`, and an integer
`d >= max(a_i,b_j)`. Check the source convergence condition

```text
|alpha|_infinity < q^(sum_j(b_j-1) - sum_i(a_i-1)).
```

The intended object is the source's normalized `q^(d-1)`-power of the indicated Thakur hypergeometric value, including its explicit `D` and Carlitz-period factors. Do not silently substitute a classical hypergeometric function.

## Callable conclusion

After constructing the source pre-`t`-motive `M_(a,b)` and its Frobenius system, Theorem 0.2 identifies that normalized value as a period of `M_(a,b)`. The construction uses a matrix/trivialization satisfying the relevant Frobenius difference relation; refined ABP lifting is then the available route for the stated transcendence or linear-independence consequences.

For the source's individual transcendence criterion, additionally use its ordered-parameter convention, nonzero `alpha`, and the selected theorem's comparison condition on the entries of `a` and `b`. For a multi-value linear-independence conclusion, separately check all listed point-independence and auxiliary `c(m)` inequalities. The period representation alone does not prove those stronger conclusions.

## Stop conditions

Stop at “hypotheses not certified” if the norm bound, `d`, coefficient field, Frobenius matrix, analytic trivialization, or a theorem-specific independence hypothesis is missing. This interface concerns positive-characteristic function fields only; it gives no conclusion about Euler's constant, classical gamma values, or decimal approximations.
