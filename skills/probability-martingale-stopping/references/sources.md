# Source register

Canonical records, local PDFs, hashes, reading pages, topic IDs and review state are in [evidence/W02/sources.json](../evidence/W02/sources.json). PDF identity and page/hash checks are in [pdf_validation.json](../evidence/W02/pdf_validation.json). Reading cards are in [evidence/W02/cards](../evidence/W02/cards).

## Complete paper and course-notes reads

**Strict v2 candidate (combined scope pending review):** 29 independently typed scholarly papers form the strict v1 base. The full 29-page Balázs document remains a completed course-notes read but is excluded from the scholarly quota. The R04-approved Aldous canonical use (`PR-bfe99a3417b7`) adds one candidate, giving 29+1=30 distinct source families with zero new full-text reads. Source-use approval does not approve the combined v2 scope or alter the installed release.

- W02-S001 Balázs, *Martingale Theory* course notes: the complete 29-page document was read, PDF pp. 1–29, including §§1–11 and references. It remains background (`course_notes`) and is excluded from the strict scholarly-source quota.
- W02-S002 Ying–Degenne (2023), *A Formalization of Doob’s Martingale Convergence Theorems in mathlib*: full 14-page paper read.
- W02-S003 Criens–Pfaffelhuber–Schmidt (2021), *The Martingale Problem Method Revisited*: full 38-page paper read; see control-aware martingale-problem and semimartingale-characteristic assumptions in the card.
- W02-S004 De Simoi–Liverani (2014), *The Martingale Approach after Varadhan and Dolgopyat*: full 28-page paper read; specialized expanding fast–slow averaging and fluctuation limits.
- W02-S005 Freedman (1975), *On Tail Probabilities for Martingales*: full 19-page paper read.
- W02-S006 Howard–Ramdas–McAuliffe–Sekhon, *Time-Uniform Chernoff Bounds via Nonnegative Supermartingales*: full 63-page local arXiv v8 read; v8 is distinct from the 2020 journal publication.
- W02-S007 Fan–Grama–Liu (2015), *Exponential Inequalities for Martingales with Applications*: full 22-page paper read; Theorem 2.1 is the conditional exponential-normalizer bound and Corollary 2.7 is the one-sided sub-Gaussian increment bound. Distinct from S010’s 15-page positive-tail-truncation and β-moment results.
- W02-S008 Fan–Grama–Liu (2012), *Hoeffding’s Inequality for Supermartingales*: full 20-page paper read.
- W02-S009 Fan–Grama–Liu (2012), *Large Deviation Exponential Inequalities for Supermartingales*: full 9-page paper read; two-sided exponential moments and positive-part/bracket truncation are separate hypotheses.
- W02-S010 Fan–Grama–Liu, *Martingale Inequalities of Type Dzhaparidze and van Zanten*: full 15-page arXiv v2 read; publication DOI is recorded separately from the local preprint.
- W02-S011 Fan–Grama–Liu, *Nonuniform Berry–Esseen Bounds for Martingales with Applications to Statistical Estimation*: full 21-page paper read; Corollary 2.2 p. 6 has $e^{-x^2/6}$ in the bracket-fluctuation term and uses the corrected threshold from (13) only in the first exponential.
- W02-S013 Fan, *A Generalization of Cramér Large Deviations for Martingales*: full 7-page version read; its absolute conditional-Cramér assumption yields both tail expansions and an MDP for all Borel sets in R; the short proof and lemma dependencies are recorded separately from S014.
- W02-S014 Fan–Grama–Liu, *Cramér Moderate Deviation Expansion for Martingales with One-Sided Sakhanenko’s Condition and Its Applications*: full 24-page paper read; the tilted-CLT lemma is deferred to the cited supplement, and the main tail conclusion is one-sided.
- W02-S016 Fan (2018), *Exact Rates of Convergence in Some Martingale Central Limit Theorems*: full 18-page v9 paper read; A1 conditional moments, A2 bracket control, stopped bracket corollary, and random-bracket repair are recorded.
- W02-S017 Hadjikyriakou–Prakasa Rao (2026), *Doob-type Optional Sampling Theorems for Demimartingales*: full 16-page arXiv v4 read.
- W02-S018 Sokol (2012), *Proving Existence Results in Martingale Theory Using a Subsequence Principle*: full 16-page paper read.
- W02-S019 Rémillard–Vaillancourt (2023/24), *Central Limit Theorems for Martingales-I: Continuous Limits*: full 18-page arXiv v3 read; see full Hypothesis 2.1 and A127 transfer boundary in its card.
- W02-S020 Černý–Ruf (2023), *Simplified Calculus for Semimartingales: Multiplicative Compensators and Changes of Measure*: full 30-page paper read.
- W02-S021 Delbaen (2024), *Martingales with Independent Increments*: full 11-page paper read; for fixed component index, increments are independent across time under the stated construction, but components are not asserted independent across indices; its best-independent-L2 lemma is imported from an earlier paper.
- W02-S022 Chen–Wang–Wang, *Martingale Solutions for the Three-Dimensional Stochastic Nonhomogeneous Incompressible Navier–Stokes Equations Driven by Lévy Processes*: full 32-page paper read; specialized PDE existence proof only. Lemma 2.4 p. 7 calls an angle-bracket process “quadratic variation” without defining the jump convention; the card separates the optional-bracket interpretation from predictable-bracket misuse.
- W02-S023 Herdegen–Herrmann (2015), *Single Jump Processes and Strict Local Martingales*: full 21-page paper read.
- W02-S024 Bañuelos–Osękowski (2016), *Stability in Burkholder’s Differentially Subordinate Martingales Inequalities and Applications to Fourier Multipliers*: full 42-page paper read; sharp Hilbert/orthogonal inequalities and scalar Riesz component bound are recorded. The scalar result is only auxiliary to C207’s vector norm.
- W02-S025 Cox–van Winden (2024), *Sharp Supremum and Hölder Bounds for Stochastic Integrals Indexed by a Parameter*: full 29-page paper read; includes countable stochastic-convolution and conditionally symmetric martingale maxima, metric chaining, and a one-dimensional SPDE application. Theorem 4.1 has printed factor 18D sqrt(p+log(1+aT))/sqrt(a); its proof has a separate intermediate log T estimate.
- W02-S026 Jacka–Norgilas (2018), *On the Compensator in the Doob–Meyer Decomposition of the Snell Envelope*: full 27-page v4 paper read; Theorem 3.3 retains the (S^1\cap H^1_{loc}) hypothesis and the density bound (dA=\mu dD^-), (0\le\mu\le1).
- W02-S027 Forré, *The Type-II Error of Test Supermartingales: e-Power versus the Chernoff–Stein Exponent*: full 47-page arXiv v1 paper read; its unique horizon minimizer is for the threshold $B_t$, while lattice-valued $G_t$ can tie in exact error at other horizons (Remark 5.7, p. 31).
- W02-S028 Bayraktar–Cox–Stoev (2017), *Martingale Optimal Transport with Stopping*: full 18-page paper read; finite-support reduction, stochastic Perron and viscosity/concave-envelope characterization.
- W02-S029 Belomestny–Schoenmakers (2021), *From Optimal Martingales to Randomized Dual Optimal Stopping*: full 27-page paper read; finite-grid weak/sure optimality classification and randomized dual perturbation.
- W02-S030 Dirksen (2014), *Itô Isomorphisms for (L^p)-Valued Poisson Stochastic Integrals*: full 51-page v3 paper read; Theorem 1.1 covers simple adapted integrands under future-increment independence, with mixed-norm regime changes; constants are equivalence constants.
- W02-S031 Feehan–Pop (2013), *On the Martingale Problem for Degenerate-Parabolic Partial Differential Operators with Unbounded Coefficients and a Mimicking Theorem for Itô Processes*: full 27-page paper read; specialized half-space diffusion source, auxiliary only to C112.
- W02-S033 Yaroslavtsev (2020), *Burkholder–Davis–Gundy Inequalities in UMD Banach Spaces*: full 43-page paper read; bracket, p-range, jump, and integral conditions are recorded in the card.

## Partial reads

None in the current batch.

W02-S032 is an unverified PDF candidate: local extraction is unreadable and author/year and full-document scope are unresolved. It has no card, is not read, and is excluded from accepted counts. Three source records remain not read (S012, S015, S032). There are 33 unique local PDFs after exact duplicate removal; 32 identities are presently accepted, but this is not a count of independently approved readings. R01 independently accepted 30 full-document sources: 29 research papers and one complete course-notes document. The final verdict and version binding are recorded in [R01 review](../evidence/review/review.json). Reader-ledger pending labels are retained as reader declarations; independent approval is recorded separately. The three unread records are excluded from the completed-source quota.

## Full-paper section coverage

Physical page ranges and a short description of actual mathematical content/proof mechanism for all 30 full-document reads are in [evidence/W02/reading_coverage.json](../evidence/W02/reading_coverage.json). Each coverage record is tied to the local PDF SHA-256. W02-S001 has full-document coverage for its front matter, §§1–11 and references; its card distinguishes stated results from proved results and records the discrete-time transfer limits.


## Canonical use for A007 (no new read)

- Aldous, [*Stopping Times and Tightness II*](https://digicoll.lib.berkeley.edu/record/86028?ln=en), `PR-bfe99a3417b7`: the reused artifact is the complete 16-page Berkeley Technical Report 124 (1987), not the later 1989 journal version. Its use card is in `evidence/W02/cards/`; complete canonical full-read card, coverage, exact PDF and immutable approvals are bundled under `evidence/canonical_reads/PR-bfe99a3417b7/` and `evidence/W02/source_approvals/`. Proposition 1.2 requires f.d.d. convergence to a continuous limit and fixed-time UI for real-valued martingales; Proposition 2.2 requires the two-sided all-stopping-times Γ condition for general processes. This supports only a conditional process-convergence step, not polling stability, renewal-age tightness, or a waiting-time limit. It is one quota candidate and no new read.
