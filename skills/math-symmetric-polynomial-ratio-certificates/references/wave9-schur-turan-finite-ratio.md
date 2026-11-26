# Schur Turán-ratio finite comparison

For a partition (lambda) padded to (n) parts, the source defines

\[
T_{lambda,i}(x)=\frac{s_lambda(1^{n-i},x^i)^2}
 {s_lambda(1^{n-i+1},x^{i-1})s_lambda(1^{n-i-1},x^{i+1})}.
\]

The evaluator computes the Schur values by Jacobi--Trudi determinants and compares two exact rational specializations (1<x_0<x_1). Its stated theorem applies for (1leq i<n) and (lambda_1>lambda_n). The source is physical pp. 1–4 of *Monotonicity of Turán-ratios of symmetric polynomials*, v1.

```sh
python3 scripts/symmetric_ratio_certificates.py examples/wave9-turan-pair.json
```

This checks a specified pair of values. It does not establish monotonicity on the full interval. The manuscript's final Macdonald claim is conjectural and excluded.
