# AUX-W07-ENDS-2023 — ends of USTs on recurrent unimodular graphs

**Source and read copy.** Diederik van Engelenburg and Tom Hutchcroft, “The Number of Ends in the Uniform Spanning Tree for Recurrent Unimodular Random Graphs,” arXiv:2301.03875v1 (10 Jan. 2023). Read all 27 physical pages of the complete v1 PDF at evidence/fulltexts/AUX-W07-ENDS-2023.pdf, SHA-256 164f99cca2c378d9f668fd064d47c5ffced82c8a6e47a7accd31382cea17bbce, including the appendix and references. D05 verified acquisition identity only; W07 read the body. Render-checked physical pp. 3, 8, 12, 14, 18, 21, and 22, including the principal theorem, potential-kernel identity, affine-isomorphism/Doob-transform statements, Wilson lemma, unimodular spine argument, and appendix references.

## Main result and model boundary

Theorem 1 (PDF p. 3) states: if \((G,o)\) is a recurrent unimodular random rooted **graph** and \(T\) is its uniform spanning tree, then \(T\) has the same number of ends as \(G\) almost surely. The model is an unweighted graph, not a general conductance network. The paper explicitly warns that unimodularity is essential and that the statement can fail for weighted networks: very small conductances can alter graph end structure while having little effect on the UST. Thus do not silently extend this theorem to weighted URNs.

Theorem 15 (PDF p. 18) is the one-ended special case in harmonic-measure language: for a recurrent unimodular random rooted graph, the UST is one-ended almost surely iff the harmonic measure from infinity is uniquely defined. Theorem 14 on the same page is the cited earlier version requiring \(\mathbb E\deg(o)<\infty\); the paper removes this finite expected degree assumption, with its Appendix A proof. Proposition 12 (PDF p. 16) says any countable collection of distinct extremal harmonic measures yields at least as many distinct UST ends; retain this one-sided statement rather than inferring equality of the two counts from it alone.

## Potential kernels, Doob transforms, and proof chain

Section 2 defines the set \(\mathcal H\) of harmonic measures from infinity as consistent limits of exit distributions from finite sets (PDF pp. 4–5). For \(h\in\mathcal H\), the potential kernel is \(a^h(x,y)=h_{x,y}R_{\mathrm{eff}}(x\leftrightarrow y)\). Lemma 4 (PDF p. 8) gives the exact identity
\[
\Delta a^h(\cdot,y)=-\mathbf 1(\cdot=y),
\]
so the kernel is harmonic away from \(y\) and subharmonic at \(y\). The proof approximates extremal \(h\) by vertices escaping to infinity, writes the approximants with Green functions, and applies the strong Markov property, symmetry of effective resistance, and time reversal. Theorem 7 (PDF p. 12) identifies \(h\mapsto a^h(\cdot,o)\) as an affine isomorphism from \(\mathcal H\) to the paper's potential-kernel space, preserving extreme points. Theorem 8 (same page) says the Doob transform associated to an extremal \(h\) has no nontrivial invariant events (the paper's Liouville property).

For the forward structural implication, extremal harmonic measures give transient Doob-transformed walks. Lemma 10, “Wilson meets Doob” (PDF p. 14), shows that Wilson's algorithm rooted at any extremal \(h\) still samples the UST, independently of the chosen extremal measure and vertex enumeration. Proposition 12 (PDF p. 16) then turns distinct extremal measures into distinct UST ends using path-ratio separation. In particular, multiple extremal measures force at least as many UST ends.

For the converse, Section 3 uses unimodularity. Proposition 13 says a unimodular random rooted graph is two-ended iff it has linear volume growth (PDF p. 17). If the UST is two-ended, orient its unique bi-infinite spine at a uniformly chosen end and condition the root onto that spine; Lemma 16 (PDF p. 18) makes the resulting law stationary under shifts along the spine. The potential-kernel difference along the two ends is an additive resistance cocycle (Lemma 18, PDF p. 19). Lemma 19 and Proposition 20 combine stationarity with an ergodic argument to force effective resistance to grow linearly along the spine (Proposition 17, PDF p. 21). Since \(R_{\mathrm{eff}}\le d_G\), spine graph-distance grows linearly; mass transport bounds the mean size of cells assigned to nearest spine points, so the graph has linear volume growth and hence two ends. This completes the recurrent-unimodular implication.

Appendix A (PDF pp. 24–27) proves the one-ended/unique-harmonic-measure equivalence without the finite expected degree hypothesis. Its steps use a rerooting-invariant event for large harmonic mass, ergodicity and hyperfinite approximations with MTP/Fatou, repeated visits by the extremal Doob walk, intersection of independent transformed walks, and Wilson rooted at infinity to rule out positive probability of a two-ended UST when the harmonic measure is unique.

## W07 use boundary

This is an unweighted UST theorem in the recurrent unimodular regime. It is useful as a precise uniform-tree comparison for end questions, but it is not a theorem about minimal spanning forests or weighted random networks. Do not use it to infer FMSF/WMSF ends, or to bypass the separate hypotheses of transient-network WUSF results.

## Full reading coverage

All 27 physical pages were read. evidence/W07/reading_coverage.json records: introduction and theorem (pp. 1–3); harmonic measures from infinity (pp. 4–5); potential kernels and Doob transforms (pp. 6–10); affine isomorphism and extremal-transform Liouville theorem (pp. 10–13); Wilson rooted at an extremal harmonic measure (pp. 13–15); unimodularity and the spine setup (pp. 16–18); resistance growth and completion of the main proof (pp. 18–22); acknowledgements/references (pp. 22–23); Appendix A, including the no-finite-expected-degree result (pp. 24–27). Review status is pending.
