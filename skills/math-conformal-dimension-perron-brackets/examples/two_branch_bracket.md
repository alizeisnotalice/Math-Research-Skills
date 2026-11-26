# One-state two-branch check

For a one-state graph with two inverse-derivative lower bounds `S=(1/4,1/4)` and upper bounds `U=(1/2,1/2)`, the Perron equations are

\[
2(1/4)^s=1,\qquad 2(1/2)^s=1.
\]

Their roots are `s=1/2` and `s=1`, respectively. Hence a system satisfying all of the reference assumptions would have the certified enclosure `1/2 <= delta <= 1`. This example checks the matrix-root orientation only; it does not construct a conformal dynamical system.

For a finite matrix whose powered entries are already exact rationals, run:

```
python3 scripts/perron_ratio_bounds.py
```

It exercises both strict spectral directions, the boundary case `rho=1`, and
rejection of a nonpositive test vector. It does not evaluate irrational powers.

对于已有的有理幂权矩阵，可指定自己的比较向量。

~~~sh
python3 scripts/perron_ratio_bounds.py --input examples/powered-weight-ratio.json
~~~

返回 \(9/8\le \rho(A)\le5/4\)。维数比较仍由输入的相应上下矩阵和原文分区条件决定。
