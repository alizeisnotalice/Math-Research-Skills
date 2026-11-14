<!-- Reader: W15; full-text read of shared D01 arXiv v3 PDF; review pending. -->
# Mohammad Kazemi and Tolga M. Duman (2025), “Characterization of Deletion/Substitution Channel Capacity for Small Deletion and Substitution Probabilities”

- Source: arXiv:2503.02545v3, dated 27 July 2025. Read copy: `evidence/fulltexts/I12.pdf`, 6 PDF pages, SHA-256 `4a838a35bf788aa1be04b2b1fd1f0a1dd72af21396b9b3c25e3c6988d9973fbf`. W15 read pp. 1–6, all sections.
- Model: binary i.i.d. deletion/substitution channel. For fixed block length, the paper first conditions on exact numbers of deletions and substitutions; it then treats random i.i.d. counts. This is not a deletion-only all-orders theorem.

## Full-text coverage and results

| Source section | PDF pages | What the source does |
|---|---:|---|
| I, Introduction | 1–2 | States the small-error objective and relates it to the known deletion-only entropy-scale bounds. |
| II, System model | 2 | Defines deletions, substitutions, and the small-probability regime. |
| III, fixed deletion/substitution counts | 3–5 | Proves Lemmas 1–4 and Theorem 1 by bounding codebook size via confusable transmission/substitution patterns. |
| IV, i.i.d. channel | 5 | Transfers the fixed-count bound to random counts; states Theorems 2–3 and Corollary 3. |
| V, Conclusion | 5 | Summarizes the asymptotic scale and scope. |
| References | 6 | Bibliography. |

The final theorem states an upper bound of the form
\[
C\le 1-(1-o(1))\bigl(H(p_d)+H(p_s')\bigr),\qquad p_s'=p_s/(1-p_d),
\]
in the stated limit in which block length tends to infinity and then deletion/substitution probabilities tend to zero. Combined with the cited Gallager lower bound, this yields the paper’s first-order approximation. It does not specify a (d^2) coefficient or an all-orders remainder for the deletion-only problem. The proof uses combinatorial counting of confusable edit patterns followed by averaging over random edit counts; no uniform higher-order expansion is claimed.

## Transfer boundary

This is a neighboring synchronization-channel asymptotic, useful as a method comparison only. The substitution probability and its normalization (p_s'=p_s/(1-p_d)) are part of the theorem; setting (p_s=0) does not produce an unproved all-orders deletion-capacity expansion. It has no RKHS bandit or regret result.
