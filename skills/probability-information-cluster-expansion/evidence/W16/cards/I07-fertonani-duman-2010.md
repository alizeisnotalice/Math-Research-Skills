<!-- Reader: W15; full-text read of the shared D01 PDF; review pending. -->
# Dario Fertonani and Tolga M. Duman (2010), “Novel Bounds on the Capacity of the Binary Deletion Channel”

- Source identity: IEEE Transactions on Information Theory 56(6), 2753–2765 (2010), DOI [10.1109/TIT.2010.2046210](https://doi.org/10.1109/TIT.2010.2046210); arXiv:0810.0785v1.
- Read copy: `evidence/fulltexts/I07.pdf`, 25 PDF pages, SHA-256 `2aba7dbe0a14fad0044462f599bb1f0419b571733e35dff9af0f29d571d85179`. The first page carries the arXiv:0810.0785v1 stamp (posted 4 October 2008); the same PDF also prints “Submitted to IEEE Transactions on Information Theory, November 1, 2018” and repeats the 2018 footer. These are the artifact’s conflicting version/date markings; this card does not reconcile them with the later journal record. W15 read PDF pp. 1–25, sections I–IX, including proofs and references.
- This is the binary i.i.d. deletion channel: each input bit is independently deleted with probability (d); capacity is per input bit. It is not a Bernoulli-reward bandit model.

## Full-text coverage and results

| Source section | PDF pages | What the source does |
|---|---:|---|
| I, Introduction | 1–3 | Defines the unknown capacity problem and previews four genie-aided upper bounds and two lower bounds. |
| II, Auxiliary channel | 3–8 | Defines a finite fixed-block auxiliary channel: one use has `L` input bits and `R` output bits, `D=L−R` deleted positions selected uniformly among the `binom(L,D)` patterns, independently across uses. It proves Lemmas 1–9 used by later bounds; this is not itself a run-length channel. |
| III, upper bound (C_1) | 9–12 | Reveals a process (Z) to the decoder, reducing the bound to auxiliary-channel mutual information evaluated by Blahut–Arimoto. |
| IV, upper bound (C_2) | 12–15 | Uses a second revealed process (W) to derive another computable upper bound. |
| V, upper bound (C_3) | 15–17 | Reveals a process (V) to both encoder and decoder and bounds the resulting channel. |
| VI, upper bound (C_4) | 17–19 | Gives the receiver-only (V) bound, with the auxiliary transition law depending on deletion probability. |
| VII, discussion | 19–22 | Compares bounds and states monotonicity/limit claims as conjectures where not proved. |
| VIII, lower bounds | 23–24 | Uses the auxiliary process (V) to obtain simple achievable-rate lower bounds. |
| IX, conclusion/references | 24–25 | Summarizes numerical comparison and cites prior work. |

The upper bounds follow by giving side information about the deletion process to one or both channel terminals; each genie can only increase capacity. Section II’s fixed-block channel is used in the later capacity bounds and evaluated numerically with Blahut–Arimoto. In the high-deletion discussion (PDF p. 22), this paper reports `C₂*/(1−d) → 0.49` as `d→1`; it compares this with the prior [7] bound `0.7918`. The latter is not this paper’s result. The numerical computation is not itself a symbolic proof of conjectured monotonicity, and the high-deletion result is not a small-`d` expansion.

## Transfer boundary

This source contributes channel-capacity bounds for an i.i.d. deletion channel. It has no RKHS, adaptive arm allocation, Bernoulli mean feedback, or instance-dependent bandit KL program, so it cannot establish B056’s structural regret claim. It also proves neither an all-orders small-(d) expansion nor convergence of the Kanoria–Montanari series.
