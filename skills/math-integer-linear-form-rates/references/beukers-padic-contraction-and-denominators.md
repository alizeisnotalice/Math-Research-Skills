# A p-adic contraction gate and rising-factorial denominator ledger

## Checked source and scope

F. Beukers, *Irrationality of some p-adic L-values*, Acta Mathematica
Sinica, English Series **24** (2008), 663--686,
doi:[10.1007/s10114-007-1029-2](https://doi.org/10.1007/s10114-007-1029-2).
The checked archival version is arXiv:math/0603277v2 (20 June 2006), local
SHA-256 `6858383b3473c93c4538c7de29cdb7a57e9ea8b23201a969cc604591bb5e51f1`.
The reusable statements are Proposition 2.1 and Lemma 2.2 (PDF physical
pp. 3--4).

This is an admission component for *p-adic* irrationality arguments.  It is
not a certificate for a real irrationality problem, and it does not by itself
establish irrationality of any p-adic L-value.

## Proposition 2.1: the contraction test

Let \(\alpha\in\mathbb Q_p\).  Suppose \(p_n,q_n\in\mathbb Z\) satisfy
\[
  \max\{|p_n|,|q_n|\}\,|p_n-\alpha q_n|_p\longrightarrow0,
\]
and \(p_n-\alpha q_n\ne0\) for infinitely many \(n\).  Then
\(\alpha\notin\mathbb Q\).

For an implementation or a proof ledger, record separately for every chosen
index:

1. an archimedean height bound \(H_n\ge\max(|p_n|,|q_n|)\);
2. a directed or exact bound on \(|p_n-\alpha q_n|_p\);
3. why the form is nonzero; and
4. a limit proof for \(H_n|p_n-\alpha q_n|_p\).

Do **not** infer the nonzero condition from numerical p-adic agreement.  If
\(\alpha=A/B\in\mathbb Q\), multiplication by \(B\) gives an integer whose
nonzero p-adic norm is bounded below by its reciprocal archimedean absolute
value; this is precisely the contradiction used in the proposition.

## Lemma 2.2: exact denominator preprocessor

For coprime integers \(b,F\), \(F>1\), write \(\beta=b/F\) and
\[
  \mu_n(F)=F^n\prod_{q\mid F}q^{\lfloor n/(q-1)\rfloor},
\]
where the product ranges over primes dividing \(F\).  Lemma 2.2 states that
the reduced denominator of
\[
  \frac{(\beta)_n}{n!}
  =\prod_{k=0}^{n-1}\frac{b+Fk}{F(k+1)}
\]
divides \(\mu_n(F)\).  The same lemma provides an additional lower
\(p\)-adic denominator estimate when \(p\mid F\); consult the source before
using that asymptotic estimate, rather than treating this finite divisor
check as a substitute for it.

`scripts/padic_rising_factorial_denominators.py` evaluates this finite
divisibility statement using exact rational arithmetic.  Its JSON output is
evidence for the supplied finite indices only; the lemma is the proof of the
general assertion.

## Route boundary

Use this route when a Pad\'e/continued-fraction construction has already
produced integer-scaled p-adic forms and the immediate open task is to keep a
transparent denominator/height ledger.  It is distinct from the existing
real Ap\'ery and gamma routes: it requires a specified prime and a p-adic
remainder estimate.
