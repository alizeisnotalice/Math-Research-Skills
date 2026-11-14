<!-- Card created by W15 after reading the complete shared PDF and rendering the LLL theorem page; review pending. -->

# Alexander D. Scott and Alan D. Sokal, “The Repulsive Lattice Gas, the Independent-Set Polynomial, and the Lovász Local Lemma”

- **Identity/version:** Journal of Statistical Physics 118 (2005), 1151–1261; arXiv:cond-mat/0309352v2. Publisher and arXiv metadata checked. Local reader copy: `evidence/fulltexts/C05.pdf`, SHA-256 `62116fa01808d58fc9b43d67629d1386b4ca9758be44aa679b9d28c44cda28ba`, 97 PDF pages. W15 read pp. 1–97.
- **Model:** Finite repulsive lattice gas with symmetric pair weights `W(x,y)∈[0,1]`; hard-core self-repulsion is the special case `W(x,x)=0`. The independent-set polynomial is the corresponding hard-core partition function.

## Core statements

- **Theorem 2.10, “fundamental theorem” (PDF pp. 17–18).** For a finite repulsive lattice gas and nonnegative vector `R`, the source equates: a connected zero-free path from `0` to `−R` in the negative orthant; positivity of `Z_W(w)` throughout `−R≤w≤0`; zero-freeness in the closed polydisc `|w|≤R`; convergence of the Taylor series for `log Z_W` at `−R`; and absolute convergence throughout that closed polydisc. It also gives `|Z_W(w)|≥Z_W(−R)>0` there. Under hard-core self-repulsion, additional equivalent tests include positivity at every coordinate-subset vertex, which connects the criterion to Shearer-type event measures.
- **Theorem 4.1, Shearer/LLL form (PDF p. 50; theorem page rendered).** Given events `(A_x)` and a graph `G` on the finite index set, suppose `P(A_x | ∩_{y∈Y} \bar A_y)≤p_x` for every `Y⊆X\Γ*(x)`. If `p∈R(G)`, then the probability of avoiding all events is at least `Z_G(−p)>0`, with a sharper conditional ratio bound. The bound is sharp: a strong-dependency-graph event family attains equality. If `p∉R(G)`, the theorem supplies zero-avoidance examples. The overbars on avoided events and the closed neighborhood in the conditioning condition are part of the source statement.
- **Theorem 4.2 (PDF pp. 51–54).** A soft-core extension requires an additional weak-dependence condition on the event interactions; it is not a generic weakening that can be dropped.

## Proof route and transfer boundary

The lattice-gas argument uses the alternating-sign property of Mayer coefficients, multivariate nonvanishing/positive-series arguments, and inclusion–exclusion. The LLL statement is proved through the hard-core partition-function/Shearer correspondence and conditional event bounds. Apply it only after a finite event family, dependency graph, and the source's conditional-probability hypotheses have been verified. It is useful as a precise LLL/independent-set criterion for B051 method context; it gives no polymer representation or convergent expansion for deletion-channel capacity.

## Full-text coverage

See `evidence/W16/reading_coverage.json#C05`: PDF pp. 1–97, all sections, proofs, appendices/discussion, and references. Theorem 4.1 was checked on the rendered physical p. 50 to preserve the avoidance-event bars.
