<!-- Card update: W15 read Chapter 2 completely; Chapter 9 remains a partial inspection. -->

# R. M. Gray, *Entropy and Information Theory*, corrected first-edition PDF

- **Identity/version:** Stanford author-hosted 324-page corrected first-edition PDF; title page dated June 26, 2023. Springer second-edition record: DOI `10.1007/978-1-4419-7970-4`. Local PDF `evidence/fulltexts/I15.pdf`, SHA-256 `77f5f22748a080c1521f8cd0daab03d7030eaa9a0f3f2cfbbf47867604daac5d`.
- **Reading status:** Complete selected Chapter 2 (all §§2.1–2.7), physical PDF pp. 39–68 / printed pp. 17–46. Also inspected Chapter 9 introduction and §§9.2–9.3 only, PDF pp. 190–194 / printed pp. 168–172. The whole book and Chapter 9 are not claimed as read.
- **Reader:** W15. The complete chapter was read from the local full-book PDF; searchable extraction was used page-by-page. The earlier Chapter 9 excerpt remains partial.

## Chapter 2 results and proof chain

- Entropy of finite-alphabet measurements/partitions and entropy rate are related to the induced process distribution; system entropy is the supremum over finite partitions (PDF pp. 39–42).
- The divergence inequality (Lemma 2.3.1 / Theorem 2.3.1), data processing under finite measurements (Lemma 2.3.3), entropy concavity under mixtures (Lemma 2.3.4), and variational divergence formula (Theorem 2.3.2, PDF p. 52) are derived from elementary logarithmic inequalities/Jensen and finite-alphabet manipulations (PDF pp. 42–53).
- For stationary finite-alphabet processes, block entropy is subadditive, so Lemma 2.4.1 gives the entropy-rate limit as an infimum of normalized block entropies (PDF p. 53). Corollary 2.4.1 gives upper semicontinuity on stationary measures; Lemma 2.4.2 gives affinity; Theorem 2.4.1 integrates component entropy rates under the explicit integrability assumption (PDF pp. 54–55).
- Conditional entropy, mutual information, and relative entropy have chain rules and data-processing statements for finite alphabets (PDF pp. 57–63). The chapter explicitly warns that a naive data-processing inequality for conditional mutual information after coarsening the conditioning variable does not follow.
- Relative-entropy-rate limits require extra conditions: Lemma 2.4.3 and Corollary 2.4.2 use a stationary finite-alphabet reference process with stationary `k`-step Markov transitions and finite-dimensional absolute continuity (PDF pp. 56–57). Theorem 2.6.1 shows `D̄(p || p^(k))→0` for stationary finite-alphabet sources and their `k`-step Markov approximations (PDF pp. 64–66).
- Lemma 2.7.1 (PDF pp. 67–68) gives one-sided almost-sure bounds for normalized relative-entropy densities under finite-block domination `M_n ≫ P_n`; the two-sided zero limit under `P` additionally requires `M ≫ P`. Its proof is Markov inequality plus Borel–Cantelli, not stationarity.

## Remaining partial Chapter 9 notes

The inspected Chapter 9 pages define a channel as a regular conditional input-to-output law and show that a stationary input coupled with a shift-compatible stationary channel produces a stationary hookup. For random output length, the physical shift must be specified; input-block shifts may be needed. These notes do not constitute a complete selected chapter.

## Transfer limit for B051

These finite-alphabet entropy and stationarity facts support the formulation of an information-rate variational problem. They do not justify interchanging the supremum over stationary inputs with a small-deletion limit or infinite series; that requires additional uniformity, compactness, and tail control. Keep the Markov-reference hypotheses on relative-entropy-rate formulas explicit.

## Coverage

The complete selected unit is recorded in `evidence/W16/reading_coverage.json#I15`; the full-book PDF has 324 pages, but only Chapter 2 is counted as a complete selected chapter.
