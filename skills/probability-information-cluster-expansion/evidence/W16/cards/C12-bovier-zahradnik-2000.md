<!-- Card created by W15 after reading and visually inspecting all 11 PDF pages; review pending. -->

# Anton Bovier and Miloš Zahradník, “A Simple Inductive Approach to the Problem of Convergence of Cluster Expansions of Polymer Models”

- **Identity/version:** Journal of Statistical Physics 100(3–4) (2000), 765–778, DOI `10.1023/A:1018631710626`; WIAS report 536. Publisher/report metadata and local title page checked. Shared reader PDF: `evidence/fulltexts/C12.pdf`, SHA-256 `1cbfec10c35765ca4b913e4984d64f17920a11dd44f982d4e9c28d961618034e`, 11 pages. W15 rendered and read every page.

## Model and theorem

The source treats an abstract hard-core polymer gas with activities `w_P`, a symmetric incompatibility relation, and connected multi-indices/clusters. Its cluster coefficient vanishes for decomposable multi-indices. Theorem 1 (PDF p. 3) assumes `0<δ<1`, sets `L(δ)=sup_{x∈(0,δ)}[-log(1−x)/x]=−log(1−δ)/δ`, and requires, for every polymer `P` and `Q`,

`|w_P| e^{a(P)} ≤ δ`,  and  `Σ_{P∼Q}|w_P|e^{a(P)} ≤ a(Q)/L(δ)`.

Then for every `Q`, the absolute sum over clusters containing `Q` is at most `L(δ)|w_Q|e^{a(Q)}`, and the sum over clusters incompatible with `Q` is at most `a(Q)`. The theorem is a sufficient convergence criterion under these polymer/activity bounds.

## Proof route and scope

The proof (PDF pp. 5–6) is inductive in a finite polymer domain: split the partition function into terms compatible and incompatible with a selected polymer, write the ratio as a logarithm, use the activity condition and the inductive cluster bound, and pass through the connected-graph expansion. Later pages treat partial polymers and finite-order extensions (Theorem 2, PDF pp. 7–8). The argument supplies a relatively short proof of a Dobrushin-type criterion; the paper describes its criterion as weaker than the classical Kotecký–Preiss version in some formulations, so do not replace C01 with a claim that it reproduces the original theorem.

This is auxiliary method evidence for B051 only. No deletion-channel polymer objects, incompatibility relation, or uniform activity estimates are provided here.

## Full-text coverage

See `evidence/W16/reading_coverage.json#C12` for physical pp. 1–11, including model and definitions, theorem hypotheses, induction proof, partial-polymer extension, discussion, and references.
