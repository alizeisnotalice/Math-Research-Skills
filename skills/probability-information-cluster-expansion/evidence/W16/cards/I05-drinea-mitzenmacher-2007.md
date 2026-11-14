<!-- Reader: W15; full paper read in this batch. -->
# Eleni Drinea and Michael Mitzenmacher (2007), “Improved Lower Bounds for the Capacity of i.i.d. Deletion and Duplication Channels”

- Source: *IEEE Transactions on Information Theory* 53(8), 2693–2714 (2007), DOI [10.1109/TIT.2007.901221](https://doi.org/10.1109/TIT.2007.901221). Author-hosted PDF: https://www.eecs.harvard.edu/~michaelm/postscripts/toit2007a.pdf. Local PDF: `evidence/fulltexts/I05.pdf` (22 pages; SHA-256 `e2084093d74b75305f7dc0889c1f4eff688d9dcbcb120d6cd4f15bc624883449`).
- Reading: W15 read PDF pp. 1–22, including the theorem and proof sections. This upgrades the former partial-read card.
- Scope: constructive achievable-rate lower bounds for the stated i.i.d. deletion/duplication channels; not a converse or exact-capacity theorem.

## Binary i.i.d. deletion theorem

The method partitions typical outputs into blocks and block types, then uses a “jigsaw” count of segmentations compatible with the received sequence. Theorem 2 (PDF p. 6 / journal p. 2698) states for independent bit deletions with probability d and binary input that

`C_del ≥ sup_{P∈ℙ} [ H(P)/(Σ_j jP_j) − ((1−d)/(Σ_k kP_k))(H(T,K)−H(P)) ]`,

where `Pr[T=t,K=k]` is specified in equation (6), and ℙ is the paper’s admissible run/type-law class in equation (8). Lemma 1, equations (14)–(15), expands `H(T,K)` using positive summands over the paper’s family `F(i,z,r,s)`.

Theorem 3 (PDF p. 7 / journal p. 2699) gives the explicit nested-series bound (16):

`C_del ≥ sup_{P∈ℙ} [ −H(d) + ((1−d)/(Σ_k kP_k)) ( H(P) + Σ_k Σ_{(i,z,r,s)} Σ_{t∈F(i,z,r,s)} Pr[T=t,K=k] log( binom(r+z,k) − binom(r,k) ) ) ]`,

with `Pr[T=t,K=k]` from (6), `P` from (8), and the displayed ranges from the source: first sum over `k`, then over tuples `(i,z,r,s)`, then over `t∈F(i,z,r,s)`. These indices range over possible run/block types without a finite cutoff in the theorem; the displayed object is a nested series. The logarithm contains the binomial-coefficient **difference** `binom(r+z,k)−binom(r,k)`, not a ratio. The inner `t`-sum is explicit in Eq. (16); suppressing it changes the formula.

Proposition 1 (PDF p. 7) is a typical-output concentration statement: with probability at least `1−N^{−Ω(log N)}`, it bounds deviations of block counts `B_k` and typed block counts `B_{t,k}` from their expectations by specified ranges. It is not an entropy-tail/truncation proposition. In particular, it does not provide the retained-mass correction `(1−ε)log(1−ε)` used for finite entropy truncation in I14 Proposition 1. Keep Eq. (16)'s infinite index ranges distinct from any finite numerical truncation; do not attribute the I14 truncation correction to I05.

For proof structure, Section III-A proves typicality of outputs (Theorem 1); Section III-B counts compatible type/block assignments, applies Stirling’s formula, prunes atypically likely codewords, and uses a union bound to derive Theorem 2 (PDF pp. 5–6). Section III-C revisits the count to allow typical fluctuations of block counts (Theorem 3 and Proposition 1, PDF pp. 7–8). Section IV applies the method to specific run laws; Section VII states an extension to i.i.d. deletion/duplication channels (Theorem 4, PDF pp. 15–16); appendices prove the lemmas (PDF pp. 19–22).

## Transfer limit

These are lower bounds for a particular run-structured random-code construction. They do not prove capacity optimality, the Kanoria–Montanari small-d expansion beyond its stated order, or convergence of that expansion.
