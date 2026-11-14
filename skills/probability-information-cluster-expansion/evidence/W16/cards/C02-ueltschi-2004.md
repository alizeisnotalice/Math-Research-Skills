<!-- Card revision: W15; source originally fully read in the earlier W16 batch. -->
# Daniel Ueltschi (2004), “Cluster Expansions and Correlation Functions”

- Source: *Moscow Mathematical Journal* 4(2), 511–522 (2004), DOI [10.17323/1609-4514-2004-4-2-511-522](https://doi.org/10.17323/1609-4514-2004-4-2-511-522); arXiv:math-ph/0304003v3. Local PDF: `evidence/fulltexts/C02.pdf` (11 pages; SHA-256 `2cc3e036af5b2a46afe95acf0b5863fe5c7d31554debb10a2a5cade4122bdbfc`).
- Reading: full paper, PDF pp. 1–11. This revision corrects the source ID from the prior misnamed `C03` card.
- Scope: cluster convergence for a specified measure-space partition function and associated correlation functions; comparison method only for B051.

## Theorem and proof locations

Let Ω be the paper’s measure space, μ a complex measure with finite total variation, and ζ a measurable symmetric interaction. Theorem 1 (PDF p. 2) assumes, for all A,A′∈Ω:

1. `|1+ζ(A,A′)| ≤ 1`;
2. there is a measurable `a:Ω→[0,∞)` with `∫Ω |ζ(A,A′)| exp(a(A′)) d|μ|(A′) ≤ a(A)` for every A;
3. the separate global condition `∫Ω exp(a(A)) d|μ|(A) < ∞`.

Then the partition function is nonzero, its logarithm has the connected-cluster expansion, and the sum/integrals converge absolutely. The rooted bound (4) controls the absolute cluster sum by `exp(a(A₁))`. The proof on PDF pp. 2–3 removes edges incident to a pinned root, decomposes the remaining graph into connected components, and uses the weighted-integrability inequality to close the induction.

Theorem 3 (PDF p. 5) adds a nonnegative weight `b:Ω→[0,∞)` and a nonnegative symmetric weight `c:Ω×Ω→[0,∞)`, defining `dμ_b=exp(b)dμ` and `ζ_c=ζ exp(c)`. Its hypotheses include `|1+ζ_c(A,A′)|≤1` pointwise and `∫Ω |ζ_c(A,A′)| exp(a(A′)) d|μ_b|(A′)≤a(A)` for every A. The theorem gives weighted correlation estimates; the proof and pinned-cluster bounds are on PDF pp. 5–7. Keep the measure/weight integrability assumptions as stated in each theorem rather than transferring Theorem 1’s condition without checking.

## Transfer limit

The deletion-channel capacity has not been represented by this partition function. Theorem 1 or 3 therefore supplies no capacity-series convergence claim without an explicit model map, verified weights, and bounds uniform in block length and run tails.
