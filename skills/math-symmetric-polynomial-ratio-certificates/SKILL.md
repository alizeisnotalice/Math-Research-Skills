---
name: math-symmetric-polynomial-ratio-certificates
description: Evaluate finite complete-homogeneous and Schur Turan ratios exactly on rational inputs, preserving the stated partition and positivity domains.
---

# Finite symmetric-polynomial ratio certificates

Use this skill to calculate a specified complete-homogeneous ratio or compare two specified Schur Turan-ratio values with exact rational arithmetic.

## Complete-homogeneous ratios

For a nonempty rational vector \(x\geq0\), integers \(\ell\geq0\) and \(r\geq1\), the helper returns

\[
\frac{h_{\ell+r}(x)}{h_\ell(x)}=G_{\ell,r}(x)^r.
\]

It reports the \(r\)-th power and never chooses an unverified rational root. Read [the source scope](references/wave9-mcleod-finite-ratio.md) before treating the value as an instance of a global inequality.

## Schur Turan ratios

For a partition \(\lambda\) padded to \(n\) parts, \(1\leq i<n\), and two rational values \(1<x_0<x_1\), calculate the two \(T_{\lambda,i}\) values by Jacobi--Trudi determinants. The helper requires \(\lambda_1>\lambda_n\), which is the source theorem's nonconstant case. Read [the source scope](references/wave9-schur-turan-finite-ratio.md) for the restrictions and excluded Macdonald conjecture.

```sh
python3 scripts/symmetric_ratio_certificates.py examples/wave9-mcleod-power.json
python3 scripts/symmetric_ratio_certificates.py examples/wave9-turan-pair.json
```

Each output is a finite rational computation. It does not prove convexity, subadditivity, or interval-wide monotonicity.

Use JSON integers for degrees, indices and partition parts. Supply each evaluation point as an integer or an exact rational string.

## 文献复核采用的构件

- [Jack and restricted Macdonald majorization contract](references/sra-jack-majorization.md)
