# Subdivided attachment comparison in strict higher categories

**Source.** OpenAI, *Thomason Model Structures in Every Strict Higher Dimension*, Proposition 6.1, Lemma 6.2, and Corollaries 6.4--6.5, PDF pp. 21--24; SHA-256 `4297861df49692b89cdcaa4a6471ce95b9b88b71e1ebf5b730412d898bf88181`.

## Input contract

Let `A subset B` be small posets, with `A` a sieve.  Its upward closure `Z` must admit a right-adjoint retraction `Z -> A`.  Given an attaching functor `UA -> X` in strict `n`-categories, form
`VB(X)=X pushout_(UA) UB` and `PB(X)=Nn(X) pushout_(Nn UA) Nn UB`.

## Reuse

Use the canonical comparison `PB(X) -> Nn VB(X)` only under that exact sieve/retraction contract.  Proposition 6.1 says it is a simplicial weak equivalence and that `Nn UA -> Nn UB` is monic.  For a boundary or horn inclusion, obtain `A,B` from the twice-subdivided face-chain construction in Lemma 6.2: `A` consists of nonempty chains lying in the indicated face poset, and the retraction is intersection with that face poset.  Then Corollary 6.4 applies to horn attachments and Corollary 6.5 transfers a supplied `Wn`-equivalence through a boundary or horn attachment.

Do not use this interface for arbitrary subposet attachments: the sieve and right-adjoint-retraction hypotheses are essential, and the source treats arbitrary attaching functors only after those poset hypotheses are supplied.

## 固定来源

- 物理页 21, 22, 23, 24。Proposition 6.1; Lemma 6.2; Corollaries 6.4--6.5 SHA-256 `4297861df49692b89cdcaa4a6471ce95b9b88b71e1ebf5b730412d898bf88181`。[Thomason Model Structures in Every Strict Higher Dimension](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Thomason-Model-Structures-in-Every-Strict-Higher-Dimension-September-25-2026/paper.pdf)
