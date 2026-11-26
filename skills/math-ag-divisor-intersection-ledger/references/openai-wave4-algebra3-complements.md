# OpenAI: local complement and Cartier-section reductions

## Bounded klt complements for Fano contractions

**Source.** *Bounded klt complements for Fano contractions*, SHA-256
`d50937326c7cb11549cc75d8daf5cd57656f85cf52f52a7cf551c22104482c67`;
physical pp. 3, 4, 6.

**Input/model.** Fix an algebraically closed characteristic-zero field, a
dimension `d`, positive rational `epsilon`, and a projective surjective normal
integral contraction `f:X→Z` with `f_*O_X=O_Z`, `K_X` Q-Cartier, `X`
`epsilon`-lc, and `-K_X` relatively ample.  A local threshold is written

\[
 \operatorname{lct}(X;\mathfrak a)=
 \inf_{E(\mathfrak a)>0}\frac{A_X(E)}{E(\mathfrak a)}.
\]

**Extracted transfer.** The stated target is a number `N(d,epsilon)` and,
for each closed `z`, an effective Q-divisor `B` and neighbourhood `U` such
that `(X,B)` is klt over `U` and `N(K_X+B)|_{f^{-1}(U)}` is integral Cartier
and linearly trivial.  Its cited reduction isolates the birational local
threshold input: for birational `f`, Fano type over `Z`, Q-Cartier `K_X`,
relatively nef `-K_X`, and `epsilon`-lc `X`, seek
`lct(X;m_zO_X) >= c(d,epsilon)`.  The operational bookkeeping is therefore:
record the exact contraction, point ideal, valuation convention, and whether
the output required is local linear triviality rather than numerical
triviality; do not replace the threshold with a generic-fibre or discriminant
coefficient threshold.

**Output/boundary.** Scoped reference. This records the stated local-to-
complement reduction only.  Constructing the threshold constant uses the
source's normalized-volume, MMP/Mori-dream-space, canonical-bundle, and trace
inputs (physical p. 4), so this entry supplies neither an `N` nor a finite
certificate of klt/Fano-type hypotheses.

## Uniform Cartier sections for Fano type contractions

**Source.** *Uniform Cartier sections for Fano type contractions*, SHA-256
`8d97ba60373419ba60890f3a130a854481596ac206dc2902f299ac542e4f761b`;
physical pp. 2--3, 102--103.

**Input/model.** For an `epsilon`-lc rational pair `(X,B)` of dimension `d`
and a positive-dimensional-base Fano-type contraction `f:X→Z` with
`-(K_X+B)` nef over `Z`, the extracted conclusion asks for a neighbourhood
`U` of a chosen closed `z`, an effective Cartier divisor `D` on `U` through
`z`, and `tau(d,epsilon)>0` such that

\[
 (f^{-1}(U),B|_{f^{-1}(U)}+\tau f^*D)\quad\hbox{is log canonical}.
\]

**Steps.** The paper reduces this to bounded birational klt complements in
the finitely many base dimensions (p. 102).  When changing real to rational
data, retain the finite boundary support and write the local Cartier
representations using the same coefficient variables on a finite open cover.
They impose a finite rational affine system; a real solution yields rational
solutions (and rational points are dense in its real solution space).  Then
descend finite-type data to an algebraically closed `k0` admitting an embedding
in C, retaining normality, geometric integrality, `f_*O_X=O_Z`, projectivity,
relative ampleness/nefness, a common log resolution, and its discrepancy and
ideal-order coefficients (pp. 102--103).  The supplied exact script checks
only the finite rational affine-system substep.

**Output/boundary.** Scoped reference. It does not construct Cartier
representations, prove that a pair is Fano type or epsilon-lc, establish field
descent, or produce `tau`, `D`, a complement index, or a log-canonical
threshold.

## 固定来源

- 物理页 3, 4, 6。Theorem 1.1; Proposition 2.1 SHA-256 `d50937326c7cb11549cc75d8daf5cd57656f85cf52f52a7cf551c22104482c67`。[Bounded klt complements for Fano contractions](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Bounded-klt-complements-for-Fano-contractions-September-25-2026/Bounded-klt-complements-for-Fano-contractions-September-25-2026.pdf)
- 物理页 2, 3, 102, 103。Theorems 1--2; H.4 SHA-256 `8d97ba60373419ba60890f3a130a854481596ac206dc2902f299ac542e4f761b`。[Uniform Cartier sections for Fano type contractions](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026/Uniform-Cartier-sections-for-Fano-type-contractions-September-25-2026.pdf)
