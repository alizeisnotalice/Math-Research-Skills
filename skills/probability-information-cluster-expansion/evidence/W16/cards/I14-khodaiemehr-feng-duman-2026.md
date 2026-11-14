<!-- Reader: W15; full arXiv v2 PDF read from the shared D01 handoff, without re-downloading it. -->
# Hassan Khodaiemehr, Chen Feng, and Tolga M. Duman (2026), “Improved Lower Bounds on the Capacity of the Binary Deletion Channel via a Learning Approach to Run-Length Inputs”

- Source: arXiv:2609.24908v2, PDF dated 26 September 2026 (v1 posted 21 September 2026), [arXiv record](https://arxiv.org/abs/2609.24908). Shared PDF: `evidence/fulltexts/I14.pdf` (22 pages; SHA-256 `c5b63f59eaf9527d7be0e7bdf52b71238b39589200aa60d25a5e2c7eb18c638d`).
- Reader: W15; full PDF pp. 1–22. The file remains in D01’s handoff directory; this worker did not duplicate the download.
- Scope: constructive capacity lower bounds for the binary i.i.d. deletion channel; the two optimization searches do not prove global optimality.

## Results and conditions

Theorem 1 (PDF p. 5, equations (13)–(14)) gives the Drinea–Mitzenmacher functional as a lower bound when the run-length law P is geometric or has finite support:
`C(d) ≥ −h(d) + ((1−d)/E[K]) (H(q) + Λ(P))`.
Here q is the output-run-length law and Λ is the expected log-count of survival patterns compatible with an output run and its input group. The common prefactor `(1−d)/E[K]` multiplies both entropy and Λ terms. Lemma 3 (PDF p. 5, equations (17)–(19)) reduces these quantities to P and its renewal weights. Proposition 1 (PDF p. 6, equations (22)–(23)) handles finite truncations using the retained mass `1−ε=Σ_{k∈K} q̃_k` and the correction `(1−ε)log(1−ε)` inside the entropy bound; it uses concavity of `−x log x` to compare the full entropy with truncated mass. Thus finite truncations give a valid lower bound when this correction and the accompanying truncated Λ term are included; dropping entropy tail terms without that correction is not justified by nonnegative termwise truncation alone.

For finite-support P, the paper extends the Venkataramanan–Tatikonda–Ramchandran (VTR) construction beyond Markov/geometric run laws by using the residual length of the current input run as a hidden Markov state. Lemma 8 (PDF pp. 10–12, equations (35)–(36)) gives a chain penalty Φ accounting for output runs formed from multiple input runs. Proposition 3 (PDF p. 12, equation (38)) proves `Φ(P,d) ≥ (1+D)Φ_VTR(P,d)` for every finite-support P, with a further nonnegative contribution from chains of length at least two. Theorem 2 (PDF p. 12, equation (40)) gives the free-law VTR lower bound for every finite-support P, `0<d<1`, and integer κ≥1; all terms except Φ are finite sums, and any finite partial sum of Φ preserves validity.

Section V separates proposal from certification: nonconvex search proposes candidate laws and makes no global-optimality claim (PDF pp. 12–14). Proposition 4 (PDF p. 15) verifies an interval-arithmetic evaluation of a finite expression at a specified exact rational law, yielding a rigorous lower endpoint for capacity. The displayed run-length clusters at high deletion probability are empirical search observations, not a structural theorem (PDF pp. 18–21). The paper lists unrestricted maximizer existence and tail form as unknown (PDF p. 21).

## Transfer limit

This paper improves constructive lower bounds; it does not prove exact capacity, an all-orders small-deletion expansion, or convergence of the Kanoria–Montanari series. Interval certification validates a chosen candidate’s bound, not the optimizer or the search procedure.
