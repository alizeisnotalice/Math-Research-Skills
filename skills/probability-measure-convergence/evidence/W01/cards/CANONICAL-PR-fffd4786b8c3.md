# Canonical usage card — Ying & Degenne, Doob convergence in mathlib

## Reuse boundary and identity

This is a W01-specific use card for canonical source `PR-fffd4786b8c3`, accepted full read W02-S002. It is **not** a new L04 full-text read. The article is by **Kexing Ying and Rémy Degenne**, “A Formalization of Doob’s Martingale Convergence Theorems in mathlib,” arXiv:2212.05578v1 (14 physical PDF pages; DOI 10.1145/3573105.3575675). The local PDF filename contains a legacy author error (`Baanen_etal...`); the actual PDF front matter and accepted W02 source row give the authors above. The copied R04 approval snapshot at `evidence/PR-fffd4786b8c3-approval-snapshot.json` binds the exact accepted W02 source decision and the approved archive-member hashes for the PDF, W02 card, sources ledger and coverage. Its reviewed-original ZIP hash and release-manifest-bound installed-review hash are recorded there. The original ZIP does not contain `review.json`; the snapshot records that the frozen installed review hash matches its published release manifest. Current global/index files are diagnostic only.

L04 reopened/rendered the relevant original pages listed in `reading_coverage.json`. W02 read pp. 1–14 and R01 accepted that evidence. The paper describes a Lean formalization merged at its publication time; **L04 did not run Lean or check a current mathlib checkout**.

## Reusable statements and proof chain

**Conditional expectation (Definition 2.1, PDF pp. 4–5).** Let `(Ω, A, μ)` be a measure space, `B ⊆ A`, and `E` a Banach space. For Bochner-integrable `f ∈ L¹(μ; E)`, if the restriction of μ to B is sigma-finite, the conditional expectation is a B-strongly measurable integrable function, unique up to μ-a.e. equality, whose integral agrees with that of f on every B-measurable set. The paper constructs it first by an L² projection and extends to L¹ (pp. 4–5). The library function is total and defaults to zero outside the hypotheses; establish the measure, integrability, and measurability assumptions before using its identities. This is an L¹ conditional expectation, **not** a regular conditional probability kernel or state-space disintegration.

**Discrete Doob a.e. convergence (Theorem 3.1, PDF p. 8; proof pp. 10–11).** On the paper's finite-measure space, an adapted real submartingale `(f_n, F_n)` with `sup_n ∫|f_n| dμ ≤ R < ∞` converges μ-a.e. to an integrable, `F_∞`-measurable limit, where `F_∞ = σ(∪_n F_n)`. This is discrete time and the finite-measure setting is part of the formalized statement.

**UI and L¹ convergence (Theorem 3.6, PDF pp. 11–12).** For a discrete-time martingale in the stated finite-measure setting, probabilistic uniform integrability, L¹ convergence to an integrable `F_∞`-measurable limit f, and the identities `f_n = E[f | F_n]` a.e. for every n are equivalent. The proof route is: UI gives a uniform L¹ bound; upcrossing plus Theorem 3.1 gives a.e. convergence; a.e. convergence gives convergence in measure; Vitali gives L¹ convergence. For the conditional-expectation characterization, contraction yields

`||f_n − E[f | F_n]||₁ = ||E[f_m − f | F_n]||₁ ≤ ||f_m − f||₁` for m ≥ n.

The converse first identifies the limit on each `F_n` and then uses the π-system/Dynkin argument to reach `F_∞` (pp. 11–12).

## W01 use and unproved interface

This is a concrete reusable discrete-time UI ⇒ L¹ convergence and conditional-expectation interface. For Formal120 A127 (the critical Beta-splitting tree pair-covariance limit), it is only auxiliary: first construct the relevant discrete-time martingale on a suitable probability space and prove its UI; the paper supplies neither the tree-specific martingale nor the required joint second-moment UI. For A011, this result does not produce the queue process, a martingale, tightness, or a total-variation estimate. It does not turn convergence in probability into UI, extend to continuous time or infinite-measure spaces, or construct a regular conditional kernel.

## Provenance and status

- Canonical source: `PR-fffd4786b8c3`; W02-S002 read all PDF pp. 1–14. The copied R04 approval snapshot binds the R01 accepted decision and the exact original PDF/card/source/coverage hashes; snapshot and archive hashes are listed in `canonical_proofmanifest.json`.
- L04 usage spot-checks: rendered original PDF pp. 1, 4, 8, 11, 12; hashes and canonical approval references are in `canonical_proofmanifest.json`.
- W01 state: `reuses_canonical`; no new full-text read or download; quota credit 0; R04 accepted the usage mathematics and reused full-read evidence; final immutable-anchor confirmation and mother integration remain pending.
