<!-- Card revision: W15; Theorem 2.1 assumption and page checked against the source. -->
# K. Sigman (2009), “Regenerative Processes”

- Source: Columbia University lecture notes (2009), 10 PDF pages. Local PDF: `evidence/fulltexts/R02.pdf` (SHA-256 `7b00b35038ab55915c1fc221d9af9cf588f2836b3f51d7b0f1367c3014fd6ffe`).
- Reading: full text, all 10 PDF pages; the existing card author attribution is retained.
- Relevance: regeneration and renewal-reward conditions for A007.

## Result and exact condition

The notes define regeneration on PDF pp. 1–2 by independence of the post-regeneration future from the pre-regeneration past and i.i.d. successive cycles. Theorem 2.1 (PDF p. 2) assumes positive recurrence and a measurable function f satisfying the exact cycle-integrability condition `E[∫₀^{X₁}|f(X(s))|ds] < ∞`. With cycle reward `R₁=∫₀^{X₁}f(X(s))ds`, it gives both the almost-sure time average and expected time average as `E[R₁]/E[X₁]`. The absolute-integral condition is essential; signed net-reward integrability alone is not a substitute.

The delayed-process results have their own initial-delay integrability conditions; do not transfer Theorem 2.1 to delayed cycles without checking them. The stationary/equilibrium version uses a length-biased initial cycle.

## Migration gap

Polling instants do not automatically regenerate a system with general renewal arrivals: arrival ages/residual times can remain dependent on the past at those epochs. One must exhibit a genuine regeneration state/epoch or use a Markov-renewal/age-augmented argument instead.
