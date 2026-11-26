# OpenAI · stationary reversible increments: a finite exact interface

## Scope and source check

This is a narrow finite-state component, not a claim about SK critical mixing.
The source is OpenAI, *Critical slowing down in the Sherrington–Kirkpatrick
model*, dated 2026-09-24, local PDF SHA-256
`20041aa4df40c551ba66fd9629f70a2efbc7778d8ea4e85c8bcfca9519826623`.
Its source PDF is [the official OpenAI repository copy](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Critical-slowing-down-in-the-Sherrington-Kirkpatrick-model-September-24-2026/paper.pdf).
It is treated here as the checked preprint version; no published edition was
identified in this review.

Read locators:

- PDF p. 6, Section 2/Lemma 2.1: for the random-scan heat-bath kernel
  `P=n^{-1}sum_i P_i`, the conditional expectations are orthogonal
  projections, `L=n(P-I)`, and
  `D_mu(f)=n <f,(I-P)f>_mu`.
- PDF p. 30, Lemma 6.1 and its proof: from stationarity and reversibility,
  `E_mu[(f(Y_k)-f(Y_0))^2]=2<f,(I-P^k)f>_mu`; the source then uses the
  heat-bath fact `spec(P) subset [0,1]` to conclude
  `E_mu[(f(Y_k)-f(Y_0))^2] <= 2k D_mu(f)/n`.

## Reusable finite theorem

Let `P` be a finite **row-stochastic, reversible** Markov kernel with
stationary probability `pi`, let `Y_0~pi`, and let `f` be real valued.  Put

```
E_P(f,f) = <f,(I-P)f>_pi
           = (1/2) sum_{i,j} pi_i P_ij (f_j-f_i)^2.
```

Then for every integer `k>=0`,

```
E_pi[(f(Y_k)-f(Y_0))^2] <= 2 k E_P(f,f).                (A)
```

The source proves (A) for its positive-semidefinite random-scan heat-bath
kernel.  The displayed finite statement is a directly checked extension to
an arbitrary finite reversible kernel, not an attribution that the source
states that extension: self-adjoint stochastic `P` has spectrum in `[-1,1]`,
and for each such eigenvalue `lambda`,
`1-lambda^k <= k(1-lambda)`.  For `lambda>=0`, use the geometric sum; for
`lambda<0`, its geometric sum is nonnegative and at most one.  Spectral
expansion of the exact stationary identity above proves (A).

For the source's heat-bath normalization, `E_P=D_mu/n`, so (A) is exactly
Lemma 6.1's discrete estimate `2k D_mu/n`.  Continuous-time clocks, the SK
model, random disorder, and any total-variation/mixing conclusion are outside
this finite interface.

## Exact audit and examples

`scripts/audit_stationary_increment.py` accepts rational JSON only, checks
row stochasticity and detailed balance exactly, computes `P^k` using rational
matrix arithmetic, and reports the two sides of (A).  It intentionally rejects
the directed three-cycle in `examples/negative_nonreversible.json`; a stationary
distribution without detailed balance is not enough for this certificate.

Reproduce the positive certificate:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 \
  scripts/audit_stationary_increment.py --input examples/positive_two_state.json
```

For `P=[[1/2,1/2],[1/2,1/2]]`, `pi=(1/2,1/2)`, `f=(0,1)`, and `k=3`,
the exact output is increment `1/2`, form `1/4`, and bound `3/2`.
