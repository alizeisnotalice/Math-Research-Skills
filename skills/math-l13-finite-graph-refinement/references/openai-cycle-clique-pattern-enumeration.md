# Canonical weighted path-forest enumeration

Source: OpenAI, *Cycle--clique Ramsey numbers*, SHA-256 \`366fc1d94b08e498183f475b170db56c72c7c898a24f3d3f1106e637ef42209b\`, physical pp. 27-37, Lemma 9.2 and Appendix A.1-A.3.

A pattern is a sorted list of positive edge-amount tuples; the empty tuple is a singleton.  Normalize each nonempty tuple by the lexicographically smaller of itself and its reversal.  Lemma 9.2 states that with \(t\) vertices and amount at most \(B\), these lists represent weighted linear-forest isomorphism classes exactly once.

The recursion chooses a first normalized tuple \(p\) with \(\ell(p)\le t-1\), \(\sigma(p)\le B\), then recurses with \(t-\ell(p)-1\) vertices, budget \(B-\sigma(p)\), and lower bound \(p\).  The exact script implements this bounded enumeration only.  Later forbidden-path and packing claims require additional source-specific graph hypotheses.

## 固定来源

- 物理页 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37。Lemma 9.2; Appendix A.1-A.3 SHA-256 `366fc1d94b08e498183f475b170db56c72c7c898a24f3d3f1106e637ef42209b`。[Cycle--clique Ramsey numbers](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Cycle-clique-Ramsey-numbers-September-25-2026/Cycle-clique-Ramsey-numbers-September-25-2026.pdf)
