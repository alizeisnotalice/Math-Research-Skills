# Palojärvi--Seppälä p-adic logarithm gate

## Publication and statement checked

N. Palojärvi and L. Seppälä, *A p-adic lower bound for a linear form in logarithms*,
*International Journal of Number Theory* **19** (2023), no. 2, 261--291,
DOI [10.1142/S1793042123500136](https://doi.org/10.1142/S1793042123500136).
The local arXiv:2107.00971v2 source states Theorem 2.1 on physical pp. 2--4.

Fix a prime `p`, rational pairwise-distinct nonzero `alpha_i`, and integer
`lambda_0,...,lambda_m`, and set

```
Lambda_p = lambda_0 + sum_i lambda_i log_p(1+alpha_i),
M = max_i |alpha_i|, alpha = max_i |alpha_i|_p, H = max_i |lambda_i|.
```

In its `M>1` branch, Theorem 2.1 requires `alpha<1`, `H>1`, a common denominator
integer `Q`, and each of its displayed conditions on `f(m,M,Q,alpha)` and
`R_1(m,M,Q,alpha)`. It then gives the explicit inequality
`|Lambda_p|_p > c_1(m,M,Q,alpha) H^(-omega_1(m,M,Q,alpha,H))`. Corollaries 2.2--2.6
are conditional simplifications, not replacements for their listed inequalities.

## Caller contract

Evaluate every real logarithm, exponential and Lambert-W threshold with directed
interval arithmetic (or independently justified bounds), while rational and p-adic
valuations remain exact. Also establish that the chosen branch of the p-adic logarithm
is the one in the source. This reference supplies no generic numerical evaluator and
does not cover `M<=1` via the displayed `M>1` theorem.
