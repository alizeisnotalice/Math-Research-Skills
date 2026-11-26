---
name: probability-permutation-subset-sums
description: Analyze invariant k-subsets of random permutations through cycle counts, Poisson limits, and random subset-sum reachability while keeping fixed-k limits separate from adjacent-k monotonicity.
---

# Permutation cycles and random subset sums

Use this skill when a uniform random permutation preserves a subset of a prescribed size, or when a multiset of random cycle lengths generates a random subset-sum set.

For a permutation with cycle counts `C_j`, an invariant set is a union of whole cycles. Thus a size-`k` invariant set exists exactly when there are integers `a_j` with `0≤a_j≤C_j` and `Σ_j j a_j=k`. This is a Boolean reachability event. Do not replace it by the expected number of representations.

There is also an exact finite-`n` model: for independent `Z_j~Poisson(1/j)`, `j=1,…,n`, the cycle-count vector of a uniform permutation in `S_n` has the law of `(Z_1,…,Z_n)` conditioned on `Σ_{j=1}^n jZ_j=n`. In particular `P(Σ jZ_j=n)=e^{-H_n}`. The unconditioned Poisson vector is the fixed-coordinate limit, not the finite-`n` cycle law; see Arratia–Barbour–Tavaré (1997), equations (2)–(5), physical p. 3, and the L14 use card（本机附件：`evidence/source_cards/EXSRC-8d97b493a6e9793f.md`）.

For each fixed `k`, the first `k` cycle counts of a uniform permutation of `[n]` converge jointly as `n→∞` to independent `Z_j~Poisson(1/j)`. Therefore the limiting probability is the probability that `k` is reachable from the Poisson multiset. This is a fixed-`k` limit; a growing `k` requires a separate uniform coupling or approximation error.

The current accepted source base supports four scoped method families: G27.01 (fixed-coordinate cycle laws and event transfer), G27.02 (conditional or model-specific reachable-set comparisons), G27.03 (labelled-cycle EGF and exact class enumeration), and G27.04 (Mellin/Fourier evaluation of the periodic kernel). The exact per-work hypotheses and exclusions are in the 30-row scope index（本机附件：`evidence/authority/G27_current30_scoped_allowlist.json`）. Method-use counts are 23, 8, 2, and 1 respectively; they overlap, so the total remains 30 distinct works. G27.05–.07 are analysis routes and proof guards, with no accepted source-use credit in this entry.

Kammoun–Maïda give a condition-sensitive universality result for products of independent permutations in the detailed two-factor case: at least one factor is conjugation-invariant and both factors satisfy H3 fixed-point-moment decay and H4 normalized 2-cycle decay. After the independently completed proof with its local corrections, fixed-coordinate cycle counts converge to independent `Pois(1/j)`, so each fixed-`k` reachability event transfers by finite-dimensional lattice-TV convergence. This does not assert finite-`n` equality or a growing-`k` rate; the `m>2` proof is only sketched. R14 accepted this scoped G27.01 use; see the L14 use card（本机附件：`evidence/source_cards/EXSRC-38d57015a9b427b0.md`）.

Ercolani–Ueltschi’s Corollary 2.2 gives fixed-coordinate independent `Pois(θ_j/j)` limits for fixed finite nonnegative weights when `h_n>0` eventually and `h_(n−1)/h_n→1`. R14 supplied a self-contained PGF/tightness/lattice-TV proof completion for this interface; the uniform specialization has `θ_j=1,h_n=1` and transfers the fixed-`k` bounded-multiplicity event. Theorem 5.1’s algebraic-weight saddle-point route is read but excluded from this method use. No growing-`k` rate or adjacent-target comparison follows. R14 accepted this scoped G27.01 use; see the L14 use card（本机附件：`evidence/source_cards/EXSRC-a4bbc39a9c64074c.md`）.

For the distinct conditional model of Ewens permutations given that every cycle has length at most a polynomial cutoff `α(n)`, Betz–Mühlbauer–Schäfer–Zeindler (Theorem 2.8) approximate the first `b=o(α(n))` cycle counts in total variation by independent Poisson counts with means `μ_j(n)=θ x_(n,α)^j/j`, where `n=θΣ_{j≤α(n)}x_(n,α)^j`. For fixed `k`, this transfers the bounded-multiplicity reachability event to independent `Poisson(θ/j)` counts. Keep this conditional model and its n-dependent Poisson approximation separate from the unconditioned uniform-permutation law; it gives no adjacent-target comparison. See the L14 use card（本机附件：`evidence/source_cards/EXSRC-2a23911f92ee017a.md`）.


## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).

## Accepted scoped multi-target extension (EFK Proposition 3.1 only)

Eberhard–Ford–Koukoulopoulos (2016), Proposition 3.1, gives a direct `m≥3` vector-reachability comparison between a finite-permutation target hit and `E|L_m(X_{k_1})|/k_1^(m−1)`, with its displayed upper factor and a two-sided comparison under `k_(m−1)≤c k_1`. R14 independently completed the proof after correcting the p. 12 dropped-probability factor, the p. 14 Markov coefficient and the bounded-`k` case; the completion uses EFG15b Proposition 2.1, already accepted as a separate work. The later Theorem 1.4 `δ_m` order proof is not certified here because it invokes additional Kou10 inputs. R14 accepted this scoped G27.02 use for one work; the R14-derived proof boundary is recorded in [method notes](references/method.md). It yields no adjacent-target sign.

## Work sequence

1. State whether the target is the finite-`n` probability or its fixed-`k` limit.
2. Express preservation as existence of a submultiset with total length `k`; keep multiplicities `0≤a_j≤C_j`.
3. For the Poisson limit, use independent `Poisson(1/j)` counts and sum over the failure event, or cap each count at `floor(k/j)` and place the excess mass in its saturated state. The literal set of failing count vectors may be countably infinite; saturation is a derived finite-state computation, not a claim that the original set is finite.
4. If using generating functions, distinguish the Boolean event `P(reachable)` from the expected number of representations.
5. For asymptotics, state the exact generating function or recurrence and all uniformity ranges. [Green–Sawhney, arXiv:2604.28116](https://arxiv.org/abs/2604.28116) proves in the preprint a smooth log-periodic asymptotic for `p(k)`, but its relative `o(1)` does not control the adjacent difference; see the use card and source notes.
6. To prove a one-sided comparison, provide an event inclusion under a measure-preserving injection or an explicit coupling. For a fixed target, adding a cycle only enlarges the reachable-sum set; comparing different targets still requires a separate event inclusion.

## Monotonicity boundary

The open assertion `p(k+1)≤p(k)` is a pointwise adjacent comparison. A relative equivalent `p(k)=g(k)(1+o(1))` does not imply the sign of `p(k+1)-p(k)`: the proposed main difference can be smaller than the uncontrolled remainder. A log-periodic factor also must be retained at the difference scale. Finite checks for `k≤K` are evidence only for those values.

Guerder gives an exact joint tail law for cycles typed by primitive words in standardized i.i.d. samples, then two different fixed-coordinate limits: geometric type counts for a non-Dirac fixed atom law, and independent `Pois(1/j)` ordinary cycle counts when the largest atom tends to zero. The printed fixed-law statement omits the non-Dirac boundary: a Dirac input standardizes to the identity, so `c_1=n` and `Geo_0(0)` is not a probability law. Only the latter transfers the fixed-`k` event to the uniform Poisson model; the exact finite-`n` identity is for typed cycles, not independent ordinary counts. No growing-`k` rate or adjacent-target comparison follows. R14 accepted this scoped G27.01 use; see the L14 use card（本机附件：`evidence/source_cards/EXSRC-c151b24b7be7bba9.md`）.

The seven method interfaces, current source status, and precise open-source gaps are in [method notes](references/method.md) and [source status](references/sources.md). The source-derived `p(1)=1-e^{-1}` check is in the [example](examples/positive.md); a common expected-count shortcut fails in the [counterexample](examples/negative.md).

**Evidence status:** R14 accepted 30 scoped G27 source-work uses. Root capture11 independently confirms 30 distinct G27 work families across the project; its source-use rows have accepted proof/conditions and specific-use flags, with no root-check errors. The exact source-by-source methods, hypotheses, transfer limits, cards, and admissions are in the 30-row scope index（本机附件：`evidence/authority/G27_current30_scoped_allowlist.json`）. The four accepted method-use counts are G27.01: 23, G27.02: 8, G27.03: 2, and G27.04: 1; they overlap and are not added to count works. Green’s problem collection is context only (zero method credit). Manstavičius–Petuchovas (2015) is a complete read with proof still pending and zero method credit. R14 reviewed the scientific and method scope of the frozen source snapshot.
