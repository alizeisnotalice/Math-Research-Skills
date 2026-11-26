# Polynomial continued fractions: factorial-reduction admission

Apply this formula to a proposed gamma construction after identifying an integral polynomial continued fraction (PCF) and proving the listed hypotheses.

## Source and version

Nadav Ben David, Guy Nimri, Uri Mendlovic, Yahel Manor, Carlos De la Cruz
Mengual, and Ido Kaminer, *On the Connection Between Irrationality Measures
and Polynomial Continued Fractions*, arXiv:2111.04468v2, 22 March 2024,
Theorems 1--2 (physical PDF pp. 10--12; proof pp. 41--42).  The local source
is `EXT-0199_On_the_Connection_Between_Irrationality_Measures_and_Polynomial_Continued_Fractions.pdf`,
SHA-256 `23c503060f726d03cbab451fb5cbf9b6d00d9ad53987b2dfc889a2bab545492f`.

The record of publication is *Arnold Mathematical Journal* **10** (2024),
529--566, DOI [10.1007/s40598-024-00250-z](https://doi.org/10.1007/s40598-024-00250-z).
The checked local object is the stated arXiv v2, so use its physical pages and
formula numbering rather than assuming publisher pagination is identical.

## Exact object to audit

For `a(n), b(n) in Z[n]`, define the PCF convergents by

\[
u_n=a(n)u_{n-1}+b(n)u_{n-2},\qquad
(p_{-1},p_0)=(1,a(0)),\quad(q_{-1},q_0)=(0,1),
\]

and suppose that `p_n/q_n -> L`, with every `p_n,q_n` integral.  Let
`d=deg a`, require the balanced case `deg b=2d`, and let `A,B` be the
respective leading coefficients.  Put

\[
G_n=\gcd(p_n,q_n),\qquad
\alpha^2-A\alpha-B=0,
\]

where `alpha` is the root of larger absolute value.  The source's Theorem 2
also requires `A^2+4B>0` and a finite real limit.  Do not infer either from
a decimal recurrence experiment.

The missing arithmetic statement is *factorial reduction* with a proved
exponential factor `lambda`:

\[
 \log G_n=d\log(n!)+n\log\lambda+o(n).
\]

Under all of those hypotheses, the source gives the lower bound in its $1+\delta$ convention

\[
 \delta=
 \frac{\log|\alpha|-\log|B|+\log\lambda}
       {\log|\alpha|-\log\lambda}.
\]

Here `delta` is the paper's exponent attached to this particular convergent
sequence (its defining inequality is `|L-p_n/q_n|<|q_n|^(-1-delta)` for
infinitely many `n`); it is not an automatic equality for the usual
irrationality exponent.  A positive value can only be used after retaining
the source's condition `p_n/q_n != L` on the relevant infinite subsequence.

## Required audit order

1. Record `a,b`, degrees, `A,B`, the exact initial values, and a proof of
   convergence/limit identification.  A recurrence with rational, rather
   than integral, numerator data does not enter this theorem unchanged.
2. Prove the factorial-reduction asymptotic, including the value of
   `lambda`; a finite table of `gcd(p_n,q_n)` is diagnostic evidence only.
3. Check `A^2+4B>0`, `0 < lambda < |alpha|` for the displayed finite-log formula,
   and the sign needed for the proposed conclusion.
4. Only then combine the exponent with a separately proved non-equality and
   integrality statement.  The source's later PCF pattern rules are explicitly
   conjectural/experimental and are not admissible replacements for step 2.

For the installed Hessami Pilehrood gamma recurrence, the exact replay

```sh
python3 scripts/gamma_continued_fraction.py --through 8
```

checks its finite rational identities, but it does **not** exhibit an
integral PCF `a(n),b(n)` together with a factorial-reduction proof.  Thus this
reference does not upgrade that route to an irrationality argument.
