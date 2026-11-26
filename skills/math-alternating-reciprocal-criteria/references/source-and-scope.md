# Source, derivation, and scope

## Audited original

Jonathan Sondow, *Irrationality and Transcendence of Alternating Series Via Continued Fractions*, arXiv:2009.14644v1, 30 September 2020, 17 pages.  Local original:

`/Volumes/data/Math_Research_Literature/07_Irrationality_Transcendence_Compendium/PDF/EXT-0322_Irrationality_and_Transcendence_of_Alternating_Series_Via_Continued_Fractions.pdf`

SHA-256: `1957eb2c360d661f72e18c96eca452f8bf9105290aaab10ff20ece293d578bad`.

The metadata and author/title are on PDF page 1.  The following locators refer to PDF pages, not the printed article’s section numbering.

* PDF pp. 2–3: Lemma 1 and Proposition 1.  For strictly increasing positive integers \(B_n\), it gives the type-I continued fraction and concludes irrationality when \(B_{n+1}\ge B_n(B_n+1)\) for every \(n\ge0\).
* PDF p. 3: the sharp boundary example: \(B_{n+1}+1=B_n(B_n+1)\) telescopes to the rational value \(1/(B_0+1)\).
* PDF pp. 4–5: Theorem 1.  For type II it separates (ii), the strict-growth irrationality criterion, from (iii), the global simple-continued-fraction hypothesis giving \(\mu\ge2.5\) and, using Thue--Siegel--Roth, transcendence.
* PDF p. 8: the converse formulation: being equivalent to a simple continued fraction means the designated partial sums are all convergents; this is a global statement.

## Independent finite identity check

Put \(a_1=B_0, b_1=1\), and, for \(j\ge2\),
\[
 a_j=B_{j-1}-B_{j-2},\qquad b_j=B_{j-2}^2.
\]
For the finite generalized continued fraction, define the standard continuants by
\[
 P_{-1}=1,\ P_0=0,\quad Q_{-1}=0,\ Q_0=1,\qquad
 X_j=a_jX_{j-1}+b_jX_{j-2}.
\]
Its value is \(P_{N+1}/Q_{N+1}\).  Substitution of the displayed \(a_j,b_j\), followed by induction on \(N\), gives
\[
 \frac{P_{N+1}}{Q_{N+1}}
 =\sum_{k=0}^N\frac{(-1)^k}{B_k}.
\]
The supplied script evaluates both sides independently with `fractions.Fraction`; the test is an exact finite identity, not a proof of Euler’s infinite equivalence or an irrationality proof.

For type II, set \(B_n=\prod_{j=0}^nA_j\).  Then
\(B_n-B_{n-1}=(A_n-1)A_0\cdots A_{n-1}\), and cancellation in the finite type-I fraction yields the stated type-II fraction.  This is the direct algebra behind Theorem 1(i).

## Inference ledger

| Evidence available | Permitted conclusion |
|---|---|
| Exact finite prefix and all checked adjacent inequalities | Exact equality of the finite sum and finite generalized continued fraction; no conclusion about the infinite sum’s arithmetic nature. |
| A proof that type-I hypotheses and \(B_{n+1}\ge B_n(B_n+1)\) hold for all indices | Irrationality, by Proposition 1. |
| A proof that type-II hypotheses and \(A_{n+1}>A_n\) hold for all indices | Irrationality, by Theorem 1(ii). |
| Additionally, a proof that the entire type-II equivalence is simple | \(\mu(\alpha)\ge2.5\), hence transcendence via Thue--Siegel--Roth, by Theorem 1(iii). |
| Decimal agreement, a long finite simple continued fraction, or merely a fast-growing denominator | None of the preceding infinite conclusions. |

The value \(\mu\ge2.5\) is not an automatic consequence of the type-I criterion, nor of every type-II Pierce expansion.  It is a conclusion under the extra global simplicity hypothesis in Theorem 1(iii).
