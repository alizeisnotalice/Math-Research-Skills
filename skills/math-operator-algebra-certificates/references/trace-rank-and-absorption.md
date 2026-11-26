# Trace, rank, and finite partition interfaces from OpenAI operator-algebra sources

These references provide reusable finite tests inside their stated operator-algebra hypotheses.  They do not make a finite test a substitute for the ambient amenability, nuclearity, or central-sequence assumptions.

## Averaging and finite phase recovery

**Source.** *Bounded recovery for modular spectral averages*, OpenAI (23 September 2026), physical pp. 5 and 7–10, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Bounded-recovery-for-modular-spectral-averages-September-23-2026/Bounded-recovery-for-modular-spectral-averages-September-23-2026.pdf), SHA-256 `7a0b0017ec76bdb23651398ca264127b0a6ad8159dd9f1e123e95f412eb33348`.

For the source's standard-form setting, its recovery construction has a usable order: modular averaging, finite phase randomization, polar cutoff, Fourier filtering, then compact phase selection.  Preserve the stated boundedness and standard-form identities at each transition; the output is a bounded recovered object satisfying the theorem's selected spectral-average constraints.

**Scoped reference.** *Expected amenable subalgebras preserving core commutants*, OpenAI (23 September 2026), physical pp. 4–5, 12, and 17, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026/Expected-amenable-subalgebras-preserving-core-commutants-September-23-2026.pdf), SHA-256 `af9a34e4fa4d0b23d115634d27d413f1013261dbe02b82802c3127c3b0efdb82`.  Its word-coefficient and fixed-core steps depend on the relative-bicentralizer shift and weak-Dixmier inputs identified by the source.  Use it as a dependency map for that amenable-core route, not as a free-standing finite algorithm.

## Positive cuts, ranks, and trace tests

**Source.** *Cuntz comparison and Jiang–Su absorption*, OpenAI (23 September 2026), physical pp. 7–8 and 11–12, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Cuntz-comparison-and-Jiang-Su-absorption-September-23-2026/paper.pdf), SHA-256 `5cbeda4528e0e671dcdb5cc55de6e32acb6bcd7e9bf219b905e2b3c206542e15`.

The reusable local route is: take a positive cut, construct its polar witness, verify the hereditary-algebra and rectangular-corner placements, then transfer trace data and perform the source's spectral rounding.  The certificate must list the cut level, both corners, and the trace inequalities used; a symbolic Cuntz comparison without these placements is incomplete.

**Scoped reference.** *Equivariant Jiang–Su Stability for Amenable Actions in the Unital Stably Finite Case*, OpenAI (5 October 2026), physical pp. 3–5 and 15, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Equivariant-Jiang-Su-Stability-for-Amenable-Actions-in-the-Unital-Stably-Finite-Case-October-5-2026/paper.pdf), SHA-256 `99c6295ef166983a4d8f5213c49a0fc83a761d6e11996fd327bda41eed7971c4`.  Within its amenable-action, unital stably finite and equivariant-uniform-property-Gamma hypotheses, coordinate estimates are turned into invariant central projections before the stated absorption theorem is applied.  Do not use the projection conclusion without those hypotheses and the cited absorption input.

**Source.** *Nuclear dimension and Jiang–Su stability without elementary subquotients*, OpenAI (23 September 2026), physical pp. 10–11, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Nuclear-dimension-and-Jiang-Su-stability-without-elementary-subquotients-September-23-2026/paper.pdf), SHA-256 `0a4fd7d8c4ac282e6be24e35ec777e3c853a5c47c62940a1cb6bac3f460e9715`.

Its finite trace interface begins from \([P]\le K[b]\) and finite \(d_\tau(b)\), yielding a trace bound on \(\operatorname{her}(P)\).  Record \(K\), the positive element, each chosen trace, and whether the requisite relative-commutant equivalence was supplied rather than inferred.

**Source.** *Tracial projection methods and uniform property Gamma*, OpenAI (23 September 2026), physical pp. 8–13, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Tracial-projection-methods-and-uniform-property-Gamma-September-23-2026/paper.pdf), SHA-256 `11c90e4d0861aa3f2aa91b50ba569111f1c35537bc19cac12b8c15e7fb6a565e`.

For real-rank-zero inputs, the source combines scalar compression, a small full-support projection, and projection-column splitting to build finite trace-test partitions.  The reusable output is a finite partition with its trace errors and support bounds explicitly tabulated; the quoted completion and uniform-Gamma equivalences remain external hypotheses.
