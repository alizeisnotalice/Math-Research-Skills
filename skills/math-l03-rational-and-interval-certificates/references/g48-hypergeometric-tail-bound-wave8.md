# Hypergeometric tail certificate (G48)

Source: [F. Johansson, *Computing hypergeometric functions rigorously*,
arXiv:1606.06977v2](https://arxiv.org/abs/1606.06977v2), physical p. 7,
Theorem 1 and its ratio-test proof.  Source byte SHA-256:
`20467d7a2378c13f48b9e8ceb1e6fc330205c26b4a40cf4903a8b462e6764078`.

## Narrow transferable statement

Let `T(k)` be the hypergeometric summand in the paper's equation (1), with
parameters `a_1,...,a_p`, `b_1,...,b_{q+1}`, and argument `z`.  For an
integer `N`, assume

1. `p <= q + 1`;
2. `Re(b_i + N) > 0` for every denominator parameter; and
3. the following explicit factor is strictly below one:

   \[
   D=|z|\prod_{i=1}^p\left(1+\frac{|a_i-b_i|}{|b_i+N|}\right)
      \prod_{i=p+1}^{q+1}\frac1{|b_i+N|}<1.
   \]

Then the source proves
\[
 \left|\sum_{k=N}^{\infty}T(k)\right|\le C|T(N)|,
 \qquad C=(1-D)^{-1}.
\]

The proof step is a direct upper bound on every subsequent term ratio by
`D`, followed by summing the resulting geometric majorant.  Thus a caller
must independently establish the exact summand convention and compute or
enclose `T(N)`; this component only certifies the tail multiplier.

## Exact finite specialization

`scripts/hypergeometric_tail_bound_wave8.py` evaluates `D` and `C` with
`fractions.Fraction` when all supplied parameters are rational real numbers.
It accepts a certificate only when all `b_i+N` are positive and `D<1`; it is
not an interval implementation for complex parameters, a branch-selection
routine, or a replacement for Arb's directed arithmetic.

Reproduce the included positive and boundary fixtures:

```sh
python3 scripts/hypergeometric_tail_bound_wave8.py --a 1 --b 2,3 --n 2 --z 1
python3 scripts/hypergeometric_tail_bound_wave8.py --a 1 --b 1 --n 0 --z 1
```

The first prints `D = 1/4` and `C = 4/3`; the second rejects the endpoint
`D = 1`, where this geometric certificate supplies no finite bound.
