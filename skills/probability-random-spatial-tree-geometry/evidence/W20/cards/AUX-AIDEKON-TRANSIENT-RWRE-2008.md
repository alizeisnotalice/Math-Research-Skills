# AUX-AIDEKON-TRANSIENT-RWRE-2008 — Speed and displacement regimes for GW-tree RWRE

**Author/citation:** Elie Aïdékon, *Probability Theory and Related Fields* 142(3–4), 525–559 (2008), DOI 10.1007/s00440-007-0114-x. **Read source:** complete arXiv:0710.3377v1 author manuscript, 17 October 2007, physical PDF pp. 1–36. SHA-256 b1e775520efa1f221c3cf9c86e226a0b20d1d4551eae17619793564a09e65d7f. W20 read the entire text; review pending.

## Model and exact results

The GW tree has no leaves, q0=0, q1<1 and finite mean m>1. Each vertex is marked with an iid positive vector of child weights (A_i)_{i≤ν}; for one generic child value A, the transition probabilities are child i: A_i/(1+Σ_j A_j), parent: 1/(1+Σ_j A_j). The paper assumes ellipticity A and 1/A essentially bounded. Let Λ=Leb{t∈R:E[A^t]≤1/q1}; Λ=∞ when q1=0. The walk is transient under inf_{t∈[0,1]}E[A^t]>1/m.

- **Theorem 1.1 (physical p. 4; rendered):** under transience, Λ<1 implies zero speed and Λ>1 implies positive speed. The critical case Λ=1 is not decided by this criterion.
- **Corollary 1.2 (physical p. 4):** on a regular b-ary tree, transience implies positive speed.
- **Theorem 1.3 (physical p. 4; rendered):** under transience and Λ≤1, log|X_n|/log n→Λ almost surely. This is a polynomial-order statement and does not itself settle whether the critical Λ=1 walk has positive speed.
- **Theorem 1.5 (physical p. 5; rendered):** on a regular b-ary tree, if inf_{t∈[0,1]}E[A^t]>1/b and E[(Σ_{i=1}^b A_i)^(−1)]<∞, then the RWRE has positive speed. Combined with the random-environment representation of linearly edge-reinforced walk, it also proves positive speed of that reinforced walk on every b-ary tree, including the separate binary-tree argument.

## Proof dependencies

The recurrence/transience test is the multiplicative-cascade criterion. Define β(x)=P^x_ω(T_parent=∞); a regeneration time is the first hit of a level at a branching vertex never crossed back to its parent. For the regular-tree criterion, Lemma 2.1 bounds the expected number of distinct visited vertices per generation by 1/E_Qβ. Lemma 2.2 proves E(1/β)<∞ by selecting a child with maximal A along a ray and iterating the conductance recursion. Theorem 1.5 then bounds expected total occupation through level n by Cn; since τ_n≤Σ_{k≤n}N_k, Fatou’s lemma and τ_n/n→1/v yield v>0.

For the general GW speed criterion, the one-dimensional associated RWRE gives lower-tail estimates for long regeneration times. Long stretches with one child act as pipes; moments of the one-dimensional crossing time determine Λ. A truncated GW skeleton removes vertices with too many descendants at a selected depth; the remaining subtree is subcritical, enabling bounds on occupation counts and a lower bound for |X_n|. The upper bound uses a long single-child pipe. Section 6 proves the speed criterion, Section 7 treats the binary reinforced-walk case, and Section 8 computes the one-dimensional potential exponents.

## W20 boundary

The results concern a random environment on a supercritical GW tree, speed and displacement of a walk, and one reinforced-walk representation. They are not results about deterministic λ-biased harmonic measure on the tree boundary, nor about Cayley graphs. For C139, they are adjacent GW-tree comparators only; dead-end depth/tail estimates on the target group graph remain unproved.

**Coverage:** physical PDF pp. 1–36 read, including Sections 1–8 and all references. Rendered checks: physical p. 4 Theorems 1.1/1.3; physical p. 5 Theorem 1.5. Full page coverage is in evidence/W20/reading_coverage.json.
