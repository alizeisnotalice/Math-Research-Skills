# A. Kalai, M. Mitzenmacher, and M. Sudan (2010), “Tight Asymptotic Bounds for the Deletion Channel with Small Deletion Probabilities”

- Source: ISIT 2010; Microsoft Research author PDF, https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/2010-Tight_Asymptotic_Bounds.pdf. Local PDF: `evidence/fulltexts/I04.pdf` (5 pages; SHA-256 `873fc9782b76e2ef74e1ba60d996d1e1d57cc811f3674030857e9fcbf0904665`).
- Reading status: full text, all 5 pages.
- Relevance: entropy-scale converse for B051; strictly weaker order than the Kanoria–Montanari second-order theorem.

## Result

The abstract and conclusion establish `C(p) ≤ 1 − (1−o(1)) H₂(p)` as p→0. The companion elementary achievability bound `C(p) ≥ 1−H₂(p)` makes the leading loss asymptotic to binary entropy. The proof counts deletion patterns and “dirty” alignments to show that a successful high-rate decoder would also reveal too much of the deletion pattern. Theorem II.1 is stated for a code with success probability δ and finite blocklength n under an explicit lower bound on n; its asymptotic conclusion takes n→∞ before p→0.

## Limit

This identifies the leading entropy scale, but does not establish the d coefficient, the d² coefficient, any d³ coefficient, or convergence of a capacity series. The coding/counting proof is not an all-orders cluster expansion.
