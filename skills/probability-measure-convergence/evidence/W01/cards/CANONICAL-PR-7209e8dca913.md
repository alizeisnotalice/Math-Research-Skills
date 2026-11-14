# Canonical usage card — Feehan & Pop, degenerate martingale problem and mimicking

## Reuse boundary and identity

This is a W01-specific use card for canonical source `PR-7209e8dca913`, accepted full read W02-S031. It is **not** a new L04 full-text read. The paper is by Paul M. N. Feehan and Camelia Pop, “On the martingale problem for degenerate-parabolic partial differential operators with unbounded coefficients and a mimicking theorem for Itô processes,” arXiv:1211.4636v3 (27 physical PDF pages). W02 read pp. 1–27 and the R04 approval snapshot at `evidence/PR-7209e8dca913-approval-snapshot.json` records R01's accepted source decision. The copied snapshot binds the approved archive-member hashes for the PDF, W02 card, sources ledger and coverage, as well as the reviewed-original ZIP and release-manifest-bound installed-review hashes. The original ZIP does not contain `review.json`; the snapshot records that the frozen installed review hash matches its published release manifest. L04 rendered the source's p. 5 for the square-root factorization. Current global/index files are diagnostic only.

## Specialized half-space martingale problem

The state space is the closed half-space `H̄ = R^(d−1) × [0,∞)`. The source generator (Definition 1.1, PDF p. 3) is

`A_t v(x) = (1/2) x_d Σ_{i,j} a_ij(t,x) ∂_ij v(x) + Σ_i b_i(t,x) ∂_i v(x)`.

On canonical `C_loc([0,∞); H̄)`, for every `v ∈ C_0²(H̄)`, the process `v(X_t) − v(X_s) − ∫_s^t A_u v(X_u) du` must be a continuous martingale in the augmented right-continuous canonical filtration, with the process fixed at its initial point through time s. **Theorem 1.3 (PDF p. 3)** gives uniqueness in law for each `(s,x)` under Assumption 2.2.

**Assumption 2.2 (PDF p. 12)** is specialized: constants δ,K,ν>0 and α∈(0,1); the zeroth-order coefficient is bounded above; the normal drift satisfies `b_d(t,x′,0) ≥ ν`; near the boundary (`x_d < 2`), a is uniformly elliptic and the listed coefficients have the stated boundedness and cycloidal Hölder regularity; away from the boundary, `x_d a` is uniformly elliptic and `x_d a,b,c` have the stated parabolic Hölder regularity. The source derives the stated linear-growth control. Theorem 2.5 (PDF p. 13), used in the PDE proof, is recalled from the authors' companion paper rather than proved here.

**Theorem 1.11 (PDF pp. 5–6)** is a separate weak-existence/uniqueness/strong-Markov result for the associated SDE under Assumption 1.8. Its exact factorization is `σ(t,x)=√(x_d) ζ(t,x)` and `a(t,x)=ζ(t,x)ζ(t,x)*`, with `(a,b)` satisfying Assumption 2.2. The square root and this SDE theorem should not be conflated with Theorem 1.3.

## Conditional-coefficient mimicking

**Theorem 1.13 (PDF p. 6; proof pp. 24–25)** starts with an `R^d`-valued Itô process X, adapted coefficients β and ξ, and

`E ∫_0^t (|β_s| + |ξ_s ξ_s*|) ds < ∞` for every t ≥ 0,

with deterministic `X_0=x_0∈H̄` and `X_t∈H̄` a.s. Define deterministic Lebesgue-measurable conditional coefficient functions

`b(t,x)=E[β_t | X_t=x]`,  `x_d a(t,x)=E[ξ_t ξ_t* | X_t=x]`.

If `(a,b)` satisfy Assumption 2.2 and the selected diffusion coefficient σ satisfies (1.8)–(1.9), the unique weak solution of the associated SDE with the same initial point has the same **one-time marginal distributions** as X. The proof uses a conditional-expectation Itô identity, the imported backward-PDE result, and an ε-shift in the boundary coordinate before letting ε decrease to zero.

The theorem does not construct a general regular conditional probability kernel and does not identify the path law. Equality of one-time marginals is strictly weaker than equality of finite-dimensional or path distributions.

## W01 use and unproved interface

This is a concrete but highly specialized conditional Markovization template: under the half-space coefficient assumptions, the constructed diffusion is well-posed and matches the input Itô process in each one-time marginal. It does not match or identify the joint/path law. Its half-space geometry, inward normal drift, weighted ellipticity, Hölder assumptions, and imported PDE theorem are essential. No formal120 problem is mapped to this source: A011 is a general stationary queue total-variation question and A127 is a two-leaf CTCS covariance question; neither currently supplies this PDE model. Keep the card as an auxiliary method source only; do not infer general disintegration, tightness, weak-limit identification, or path-law equality.

## Provenance and status

- Canonical source: `PR-7209e8dca913`; W02-S031 read all PDF pp. 1–27. The copied R04 approval snapshot binds the R01 accepted decision and the exact original PDF/card/source/coverage hashes; snapshot and archive hashes are listed in `canonical_proofmanifest.json`.
- L04 inspected/rendered original PDF pp. 1, 3, 5, 6, 12, 24; complete canonical coverage remains W02's evidence.
- W01 state: `reuses_canonical`; no new full-text read or download; quota credit 0; R04 accepted the usage mathematics and reused full-read evidence; final immutable-anchor confirmation and mother integration remain pending.
