# Positive examples

## A fixed-depth endpoint-zero event

`f(p)=p²` is the event “both of two independent p-coins are heads.” Its degree-2 unnormalized Bernstein counts are `(0,0,1)` for head counts `0,1,2`; these satisfy `0≤A_(2,j)≤binom(2,j)`. Its complement uses counts `(1,2,0)`. This exact event includes the endpoint `f(0)=0` without any positive interior-minimum assumption.

## A geometric mixture when the data are supplied

For the N002 interface set `f_k(p)=p²` and `η_k=2` for every `k`. The threshold event `[(S_2/2)²≥1/2]` occurs exactly when both tosses are heads, so `q_k(p)=p²`. The residual is `3p²/4`, hence the recurrence returns `f_(k+1)=p²` and the geometric series equals `p²`. This checks the source’s conditional interface; it does not establish arrays for arbitrary `f`.

## A non-affine debiased coefficient example

For N003 take `f(p)=1/4+p²/2`, `c_(n,j)=1/4+j(j−1)/(2n(n−1))`, `ε_n=1/(16n³)`, `a=c−ε_n`, `b=c+ε_n`. The exact degree elevation gives `g_n=f−ε_n`, and the lower-array increments are `ε_(n−1)−ε_n≥0`. At `k₀=3`, `λ=2`, `ρ=11/2`, `η=1/5`, the base `max_j b(2,j)=97/128<4/5`; the separate rational increment-tail bound is `1/64`, so `ψ≤49/64`. Independent uniform thresholding is an exact f-coin. Here the selected `L` has infinite mean, so the example also shows bounded estimator values do not imply finite expected p-tosses.

## A finite odds tree

For N004 leaf biases `(1/5,2/3,3/7,4/5)` in the specified balanced tree, the internal biases are `(1/3,3/4,3/5)` and the root is `3/5`, agreeing with the product of leaf odds. With leaf expected primitive costs `(1,2,3,4)`, the exact recursive expected cost is `219/4`, provided the leaves have finite means and each repeated call is fresh.

The package includes exact-rational scripts for these finite examples. Their outputs are consistency checks; the cited theorem proofs establish the general interfaces.
