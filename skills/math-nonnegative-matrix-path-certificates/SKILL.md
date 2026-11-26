---
name: math-nonnegative-matrix-path-certificates
description: Verify the odd-power path certificate for finite entrywise-nonnegative symmetric matrices, with exact finite arithmetic where the inputs are rational.
---

# Nonnegative matrix path certificates

Use this tool for the finite path inequality, not for arbitrary matrices.  Supply
same-order real symmetric matrices \(C_1,\ldots,C_t\) with entrywise
nonnegative entries, entrywise-nonnegative endpoint vectors \(u,v\), and an
odd exponent \(k=2r+1\).  Its certificate target is

\[
 (u^T C_1\cdots C_t v)^k
 \le (u^Tu)^r(v^Tv)^r\,u^TC_1^k\cdots C_t^k v. \tag{P}
\]

For rational finite inputs, calculate the two sides in exact rational
arithmetic and retain \(C_i,u,v,k\) plus both values.  The supplied replay
performs these eligibility checks before evaluating (P).

## Proof route and scope

For strictly positive data, regard the left product as a Gibbs partition
function on a \(t\)-edge path.  Glue a long-path Markov law by alternately
using each edge marginal and its reversal.  Oddness makes every block finish
at the next vertex; symmetry makes the reversed edge have the same energy.
The log gap is the sum of the long-path KL divergence and the two endpoint
KL divergences.  It is nonnegative.  Entrywise nonnegative data follow only
by the stated \(\varepsilon\)-positive perturbation and limit.

Do not apply this route when an entry is negative, a factor is nonsymmetric,
or \(k\) is even.  In particular, the analogous many-factor norm/spectral
claim can fail for even exponents.  The paper's all-exponent *two-factor*
spectral conclusion uses a separate even-exponent argument; it is not a
license to use (P) at even \(k\).

The finite calculation is an instance certificate, not a proof of a
parameterized inequality or a spectral-radius limit.  For the latter, keep
the separate norm/spectral argument and its Gelfand-limit hypotheses.

Run `scripts/check_odd_path_certificate.py` for an exact positive instance,
a zero boundary instance, and the documented even-parity rejection witness.
The source statement, proof dependencies, and physical locators are in
[the source note](references/sra-spectral-blakley-roy-v1-wave7.md).
