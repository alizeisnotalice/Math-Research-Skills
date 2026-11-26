# Complete-homogeneous ratio finite evaluation

For (x=(x_1,ldots,x_n)), define (h_k(x)) by

\[
\sum_{k\geq0}h_k(x)t^k=\prod_{j=1}^n(1-x_jt)^{-1}.
\]

For (ellgeq0), (rgeq1), the source writes

\[
G_{ell,r}(x)^r=\frac{h_{ell+r}(x)}{h_ell(x)}.
\]

The supplied evaluator accepts a nonempty nonnegative rational vector and reports this exact (r)-th power. It deliberately does not select a rational root. The extraction comes from physical pp. 1–6 of *A Proof of McLeod's 1959 Conjecture on Complete Homogeneous Symmetric Ratios*, v1.

```sh
python3 scripts/symmetric_ratio_certificates.py examples/wave9-mcleod-power.json
```

The output is a finite evaluation. Convexity and subadditivity on (mathbb R_+^n) require the source theorem or an independent proof.
