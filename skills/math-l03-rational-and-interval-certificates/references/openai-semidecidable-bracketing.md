# Strict-witness bracketing

For a target real `alpha`, a uniformly computable increasing lower certificate sequence, and a strict semidecidable upper witness for every rational above `alpha`, dovetail the two searches to return rational brackets. The input must distinguish an actual strict upper witness from an unverified numerical estimate; this component does not make a random-SAT threshold computable until both certificate suppliers are provided.

Source: *Computing the Random 3-SAT Threshold*, SHA-256 `be7bde6cd4e513e134ffa36b94506ddd9fd0c13fd9f740d2ebac8494d249c530`, physical pp. 2--3, Lemma 2.1.

For finite replay, [the exact bracket checker](../scripts/strict_witness_bracket.py) takes the largest lower certificate and the smallest strict upper witness. It rejects an inconsistent combined ledger. In the accompanying [fixture](../examples/strict-witness-bracket.json), the interval is `[3/4, 4/5]`.

## 固定来源

- 物理页 2, 3。Lemma 2.1 SHA-256 `be7bde6cd4e513e134ffa36b94506ddd9fd0c13fd9f740d2ebac8494d249c530`。[Computing the Random 3-SAT Threshold](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Computing-the-Random-3-SAT-Threshold-September-27-2026/article.pdf)
