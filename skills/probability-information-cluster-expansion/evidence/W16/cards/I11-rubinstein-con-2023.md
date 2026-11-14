<!-- Reader: W15; full-text read of the shared D01 arXiv v1 PDF; review pending. -->
# Ittai Rubinstein and Roni Con (2023), “Improved Upper and Lower Bounds on the Capacity of the Binary Deletion Channel”

- Source identity: arXiv:2305.07156v1, submitted 11 May 2023; 25-page PDF. The arXiv record and title page identify Rubinstein and Con. A distinct six-page ISIT 2023 proceedings version is pp. 927–932, DOI [10.1109/ISIT54713.2023.10206626](https://doi.org/10.1109/ISIT54713.2023.10206626). Read copy: `evidence/fulltexts/I11.pdf`, SHA-256 `8da4378d15073ae7fb3d5d3a3945265ef7c3e50dad7fba27dcecf5fcdaa6a230`.
- Reader: W15; PDF pp. 1–25 read, including references. This is the existing D01 handoff; W15 did not download or copy it.
- Model: binary i.i.d. deletion channel with deletion probability `d`, capacity measured per input bit.

## Results and proof path

Theorem 1.1 (PDF p. 4) proves `C(BDC_d) ≤ 0.3745(1−d)` for every `d≥0.68`. The converse route starts with fixed-length deletion capacity `C_n(d)` and auxiliary channels `W_{n,k}` whose output is a uniformly chosen length-`k` subsequence of an `n`-bit input. Conditioning on the output length gives

`C_n(d) ≤ Σ_{k=1}^n binom(n,k)d^(n−k)(1−d)^k C_{n,k}`.

The auxiliary channels are finite DMCs, so Blahut–Arimoto bounds their capacities. Section 3 (PDF pp. 9–14) reduces memory use with caching/loop-nest changes, sparsity and symmetry. The high-deletion result also uses a monotonicity comparison for `C(BDC_d)/(1−d)`; the displayed bound is supported by the paper’s finite-channel computations, not a symbolic formula for capacity at all `d`.

Theorem 1.2 (PDF p. 5) proves `C(BDC_d)>0.1221(1−d)` for `0<d<1`. Section 4 starts from the rigorous Drinea–Mitzenmacher run-length code lower bound. The authors use a BAA-type procedure to optimize a heuristic score for run distributions; their score omits order-`D²` deleted-run interactions and difficult entropy terms (PDF pp. 18–20). In practice, an outer basin-hopping search chooses parameters (PDF pp. 17–18). They then insert a selected distribution into the rigorous Drinea–Mitzenmacher bound, which makes the resulting lower bound valid even though the heuristic is not the true code rate and the outer search is not a global-optimality certificate. Lemma 4.1 (PDF pp. 21–23) concerns approximation of the stated heuristic optimization under its model/parameter conditions; it does not certify global optimization of the actual deletion-channel rate.

## Full-text map

| Section | PDF pages | Coverage |
|---|---:|---|
| §1, Introduction and results | 3–5 | Defines the BDC, reviews bounds, states Theorems 1.1–1.2, and gives organization. |
| §2, Upper Bound Theory | 6–9 | DMC capacity/BAA, fixed-length deletion capacities and auxiliary fixed-subsequence channels. |
| §3, Memory-Efficient BAA | 9–14 | Caching, loop nesting, sparse transitions and numerical upper-bound results. |
| §4.1, DM framework | 14–16 | Run-length construction and its rigorous lower-bound interface. |
| §4.2–4.3, heuristic and analysis | 17–20 | Proposed run-law score; states the deleted-run and entropy effects omitted by the heuristic. |
| §4.4, reduction to convex optimization | 21–23 | BAA-type constrained score optimization and approximation lemma; discusses outer-parameter search practice. |
| References | 24–25 | Bibliography. |

## Transfer limit

This is a deletion-channel bound, not a higher-order small-`d` expansion. It contains no RKHS, adaptive arm allocation, Bernoulli reward-KL regret program, or proof of an all-orders capacity series. Treat it as a current finite-computation comparator only.
