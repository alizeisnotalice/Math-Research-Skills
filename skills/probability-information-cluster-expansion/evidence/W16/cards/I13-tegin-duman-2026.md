<!-- Reader: W15; full-text read of shared D01 arXiv v4 PDF; review pending. -->
# Busra Tegin and Tolga M. Duman (2026), “Capacity Approximations for Insertion Channels with Small Insertion Probabilities”

- Source: IEEE *Transactions on Information Theory* 72(3), 1437–1453 (2026), DOI [10.1109/TIT.2025.3644665](https://doi.org/10.1109/TIT.2025.3644665). Read copy: arXiv:2411.14771v4, last revised 18 Dec 2025, 46-page PDF, [arXiv record](https://arxiv.org/abs/2411.14771). The paper reports a preliminary ISIT 2025 version, DOI 10.1109/ISIT63088.2025.11195329; it is not the full reader copy. Shared PDF: `evidence/fulltexts/I13.pdf`, SHA-256 `c7478ee7f4cc70cad9e71f0f00bba783daa37455d0fc7d4317d00df9b3bf0fa1`.
- Reader: W15; PDF pp. 1–46 read. This is the existing D01 handoff, with no duplicate download.
- Model: two distinct binary i.i.d. insertion channels with insertion probability `α`: (i) simple insertion, which may append an independent fair bit after each input bit; (ii) Gallager insertion, which replaces an input bit with two independent fair bits.

## Capacity statements and proof structure

For each fixed `ε>0` and sufficiently small `α`, Theorem 3 (PDF p. 12) gives for the simple-insertion capacity

`C₁(α)=1+α log₂(α)+G₁α+O(α^(3/2−ε))`, with `G₁≈0.4901`.

Theorem 13 (PDF p. 32) gives for the Gallager model

`C₂(α)=1+α log₂(α)+G₂α+O(α^(3/2−ε))`, with `G₂≈−0.5865`.

The constants are specified by the convergent series in Eqs. (15) and (114). The achievability argument uses i.i.d. Bernoulli(1/2) input. For the converse the authors use the stationary-ergodic information-rate formulation, first truncate run lengths with a controlled loss, then bound the output and conditional entropies for high-entropy inputs. Section III decomposes `I(Xⁿ;Y)` into output entropy, insertion-pattern entropy, ambiguity entropy and output-run-length uncertainty. The Dobrushin capacity theorem and the stationary-ergodic characterization are quoted in Section II and their proofs are explicitly referred to earlier sources (PDF p. 9); the Gallager converse’s finite-run truncation proof is partly summarized by reference to the simple-insertion proof (PDF p. 43). Thus the full paper was read, but those cited proof details are not reproduced in this source.

## Full-text map

| Section | PDF pages | Coverage |
|---|---:|---|
| §I, Introduction | 2–6 | Context, two models, contributions and asymptotic statements. |
| §II, Preliminaries | 7–9 | Insertion models, information-rate/capacity characterization and run notation; cited foundational proofs are deferred. |
| §III, Rate decomposition | 10–12 | Run/output-segment variables and entropy-chain decomposition. |
| §IV, Simple insertion | 12–31 | Theorem 3, achievability, entropy terms, finite-run reduction and converse. |
| §V, Gallager insertion | 32–43 | Theorem 13 and parallel entropy, achievability and converse analysis; Lemma 21 proof is abbreviated by cross-reference. |
| §VI, Conclusions | 44 | Summary and future directions. |
| References | 45–46 | Bibliography. |

## Reader-copy artifact note and transfer limit

The rendered reader PDF page 36 contains the unrelated sentence “Your explanation is clear, but I’ll make a few adjustments for presentation and clarity:” embedded between the paper’s mathematical prose (after Eq. (128)). This is present in the PDF rendering, not just an OCR artifact. It appears to be extraneous text; the surrounding equations remain legible. Preserve this as a source-artifact limitation rather than silently treating it as part of the proof. The results concern insertion models and do not prove any higher-order expansion for the deletion-only channel or convergence of its capacity series.
