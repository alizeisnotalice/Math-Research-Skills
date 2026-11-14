# Canonical usage card — Criens, Pfaffelhuber & Schmidt, martingale-problem limits

## Reuse boundary and identity

This is a W01-specific use card for canonical source `PR-e1277389a5a9`, accepted full read W02-S003. It is **not** a new L04 full-text read. The article is David Criens, Peter Pfaffelhuber, and Thorsten Schmidt, “The Martingale Problem Method Revisited,” arXiv:2108.11930v1 (38 physical PDF pages). The local filename starts with `Becker_...`, which is not the author list. W02 read pp. 1–38. The copied R04 approval snapshot at `evidence/PR-e1277389a5a9-approval-snapshot.json` binds the accepted W02 source decision and approved archive-member hashes for the PDF, W02 card, sources ledger and coverage, along with the reviewed-original ZIP and release-manifest-bound installed-review hashes. The original ZIP does not contain `review.json`; the snapshot records that the installed review hash matches its published release manifest. Current global/index files are diagnostic only.

L04 reopened/rendered original pp. 1, 13–14, 25–26. In particular, PDF p. 26 was rendered to check the final proof step of Theorem 4.3. The canonical W02 record provides the complete read evidence.

## Abstract transfer theorem

**Theorem 2.28 (PDF pp. 13–14)** is a limit-identification theorem, not a tightness theorem and not a uniqueness theorem. Under Assumptions 2.21 and 2.27 and a dense time set D, the controlled joint laws `Q_n = P_n ∘ (L_n, X_n)⁻¹` must converge weak-strong to `Q = P ∘ (L, X)⁻¹`. The theorem also requires a determining bounded test family for the martingale-problem class; canonical versions of each test process; the stated `(Q_n,Q)`-continuity of test values and their products at dense times; uniform integrability of the approximating test values on bounded time intervals; and approximate martingale identities whose errors tend to zero for the determining tests. Then the limit law P solves the specified martingale problem.

Proof mechanism: weak-strong convergence and test continuity pass the expectation identities to the limit; the determining family gives the conditional martingale identity at dense times; uniform integrability, right-continuity, and Vitali extend it to arbitrary times. **Corollary 2.31 (PDF pp. 14–15)** removes the control variable but retains weak convergence, the determining family, canonical/continuous tests, UI, and approximate identities.

**Theorem 4.3 (PDF pp. 25–26)** handles fixed discontinuity times. Under J₁ convergence in `D(E)` and Assumptions 4.1–4.2, the limit law solves the stated martingale problem. Assumption 4.1 supplies high-probability jump control and compactness of the control-variable laws; Assumption 4.2 supplies dense-time approximate identities for generator, drift-integral, and compensator tests together with its expectation bounds. The proof extracts a weak-strong subsequence of `(L_n,X^n)`, uses jump control to obtain the needed test continuity on the relevant path sets, and applies Theorem 2.28. Weak path convergence alone is insufficient. Theorem 4.6 (PDF pp. 28–30) is a separate semimartingale-characteristics extension with its own stopped bounds and modified second characteristic; it is not used to remove Theorem 4.3's assumptions.

## W01 use and unproved interface

For A011, the theorem is at most an auxiliary route to identify a weak path-law limit **after** the queue model supplies a process representation, tightness, the relevant test domain, UI, continuity estimates, and approximate martingale identities. It does not upgrade weak convergence to the total-variation convergence asked there. For A127, it is only an auxiliary template if a process-level martingale-problem representation and all transfer hypotheses are independently established; it does not prove the CTCS pair covariance, cyclic-separation law, tightness, or joint second-moment UI. No target problem is solved by applying this theorem from weak convergence alone.

## Provenance and status

- Canonical source: `PR-e1277389a5a9`; W02-S003 read all PDF pp. 1–38. The copied R04 approval snapshot binds the R01 accepted decision and the exact original PDF/card/source/coverage hashes; snapshot and archive hashes are listed in `canonical_proofmanifest.json`.
- L04 usage spot-checks: rendered original PDF pp. 1, 13, 14, 25, 26; page images and hashes are listed in `canonical_proofmanifest.json`.
- W01 state: `reuses_canonical`; no new full-text read or download; quota credit 0; R04 accepted the usage mathematics and reused full-read evidence; final immutable-anchor confirmation and mother integration remain pending.
