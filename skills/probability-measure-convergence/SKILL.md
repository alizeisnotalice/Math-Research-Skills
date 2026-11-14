---
name: probability-measure-convergence
description: Analyze weak convergence, tightness, conditional laws, changing integrands, and martingale-problem limits. Use when a proof passes from stochastic models to limits of probability measures or needs a precise convergence mode.
---

# Probability measures and convergence

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill to identify which convergence theorem a probability argument actually supports. Start by naming the state space, sigma-field, topology, limit law, and test class. Keep weak convergence, setwise convergence, total variation, Wasserstein convergence, convergence in probability, and almost-sure convergence distinct.

## Workflow

1. **Specify the spaces and mode.** State whether laws live on a Polish space, another metric space, a path space with a named topology, or only a measurable space. Define the convergence being proved and the tests it controls. For conditional laws, state the conditioning sigma-field and the version/support convention.
2. **Separate compactness from identification.** Prove tightness or compact containment first, then identify subsequential limits with a determining class. Prokhorov applies to probability measures on Polish spaces. Finite-dimensional convergence alone does not give path-space convergence.
3. **Check test-function conditions.** Portmanteau handles a fixed nonnegative lower-semicontinuous function. For varying or signed integrands, use the exact envelope, convergence-in-measure, and tail assumptions below. Weak convergence does not control unbounded expectations by itself.
4. **For kernels, check versions and measurability.** Regular conditional probabilities are generally specified only marginal-a.e. Continuity can select a version on the support; it says nothing about off-support values. A jointly Borel parameterized kernel may need a measurable right-inverse or another selection hypothesis.
5. **Keep model interfaces explicit.** Tightness, invariance, uniqueness, compatibility, stationarity, exchange of limits, UI, and weak-to-TV upgrades are separate claims. Cite only the theorem whose hypotheses have been verified.

## Weak convergence and varying integrands

For probability measures on a metric space, weak convergence means convergence against every bounded continuous test. Portmanteau gives

\[
\int f\,d\mu\leq\liminf_n\int f\,d\mu_n
\]

for a fixed nonnegative lower-semicontinuous `f`. A continuity-set probability limit also requires `μ(∂A)=0`.

For varying nonnegative measurable `f_n`, Feinberg–Kasyanov–Zadoianchuk, Theorem 1.1 (B18-001, PDF pp. 2–3), gives the **joint lower envelope**

\[
\int \liminf_{n\to\infty,\,s'\to s} f_n(s')\,\mu(ds)
\leq \liminf_n\int f_n\,d\mu_n.
\]

Do not replace this by `∫ liminf_n f_n(s) μ(ds)` without an additional theorem. Their proof truncates, regularizes tail infima to l.s.c. functions, applies Portmanteau, and then takes a monotone limit. The source’s counterexample is `S=[0,1]`, `μ_n=δ_{1/n}⇒δ_0`, and `f_n=1_{ {0} }`: the pointwise-liminf integral is 1 while every right-hand integral is 0.

For signed functions, B18-001 Theorem 4.3 (PDF pp. 5–6) needs measurable lower bounds `g_n≤f_n` and a finite lower bound on the corresponding joint upper-envelope integral. Corollary 4.7 (p. 7) is a special case with one common bounded-above `g≤f_n` and the stated limit of `∫g dμ_n`; replacing the upper-semicontinuous regularization `ḡ` by `g` requires `g` upper semicontinuous. A common finite lower bound is one sufficient choice. Weak convergence alone is not a signed Fatou theorem.

Feinberg–Kasyanov–Liang, Theorem 2.2 (B18-003, PDF p. 4), provides the same weak lower-envelope inequality for real-valued integrands when either the negative parts are asymptotically uniformly integrable under `μ_n`, or the source’s exact lower-envelope condition holds. Their classical weak Fatou Theorem 4.1 (PDF pp. 9–10) additionally requires lower semiequicontinuity, convergence from below in `μ`-measure, and that same negative-tail or envelope condition. This is a sufficient criterion, not an equivalence. `a.u.i.` means the tail supremum vanishes after `limsup_n`; it can ignore finitely many initial terms and is not automatically uniform integrability of the whole sequence.

For B18-002, keep the two uniform-over-sets conclusions separate. **Theorem 1.1 (PDF p. 2)** assumes `dist(μ_n,μ)→0` in the paper’s bounded-measurable-test total-variation norm, `f∈L¹(μ)`, and each `f_n∈L¹(μ_n)`. Its one-sided inequality `liminf_n inf_A (∫_A f_n dμ_n − ∫_A f dμ) ≥ 0` holds iff both (i) `f_n` converges **from below in μ-measure** to `f`, meaning `μ{f_n≤f−ε}→0` for every `ε>0`, and (ii) the theorem’s negative-tail condition holds: `liminf_{K→∞} inf_n ∫ f_n 1_{f_n≤−K} dμ_n ≥0`. Full convergence in measure and absolute uniform integrability are not its conditions. **Corollary 1.8 (PDF pp. 4–5)**, under the same TV/L¹ premises, instead characterizes the absolute conclusion `sup_A |∫_A f_n dμ_n−∫_A f dμ|→0`: it holds iff `f_n→f` in `μ`-measure and the absolute tails are uniformly integrable, `lim_{K→∞}sup_n∫|f_n|1_{|f_n|≥K}dμ_n=0`. For example, on a one-point space with `μ_n=μ=δ_x`, `f_n(x)=1`, and `f(x)=0`, Theorem 1.1’s one-sided inequality and both of its conditions hold, but full convergence in measure and Corollary 1.8’s absolute conclusion fail. Corollary 1.6 is only for nonnegative `f_n`. Do not replace either TV premise by setwise convergence: the paper’s dyadic-density example has setwise convergence and exact integral equality on every measurable set, yet fails the required convergence-in-measure condition. Its signed Example 3.2 has a localized printed-sign discrepancy; use the source’s displayed value only as a literal and the separately checked derivation in the card.

## Conditional laws, disintegration, and conditional LDP

A regular conditional law needs an appropriate measurable-space existence theorem, commonly a standard Borel/Polish hypothesis. Check measurability, probability-valuedness, and the conditional-expectation identity separately. Values off the conditioning marginal’s support are not identified by the law.

For parameterized disintegration, Bogachev–Malofeev (B18-004) works with completely regular Souslin spaces. Theorem 3.4 (PDF pp. 8–10) constructs a measurable family under its stated assumptions; its conclusion is measurable for the sigma-algebra generated by the relevant Souslin sets, not automatically Borel. Fiber support is only asserted on the attainable set `Ω₁={(y,z): y∈f_z(X)}`. The proof uses a fixed Dirac extension off `Ω₁`, and the source’s final all-`y` sentence is locally inconsistent with that construction; do not add surjectivity or use that sentence to enlarge the theorem. Theorem 3.5 (p. 10) gives a jointly Borel upgrade only with its Borel right-inverse/selection conditions. Theorem 3.4 proves measurability, not weak or continuous parameter dependence.

For conditional large deviations, van Zuijlen (B18-005) Theorems 1.2–1.3 (PDF pp. 4–5) start from a **good joint LDP**, supported versions of regular conditional laws weakly continuous on the conditioning support, and exact local numerator/denominator ratio criteria. The all-support-sequence statement includes finite fiber-rate assumptions and the source’s open/closed test-set conventions. Do not infer a conditional LDP from joint weak convergence or a joint LDP alone. Preserve the distinction between its physical PDF pp. 31–32 in Example 9.1: the density/mgf is on p. 31 and the following prose rate is on p. 32. For that two-dimensional Gaussian example, the normalized model needs `0<|r|<1`; the source’s local `r≠0` wording does not make `|r|≥1` a probability model.

For Gaussian conditional continuity and operator formulas, use the exact Banach or Cameron–Martin norm assumptions from the source cards. A scalar covariance ratio does not imply an operator-norm bound; a Hilbert-topology isomorphism does not imply continuity of its inverse in a weaker ambient topology. The finite-rank and infinite-rank Gaussian disintegration theorems also have different proof status and assumptions.

## Tightness, paths, and representations

A family of laws on a Polish space is tight when one compact set captures mass uniformly to arbitrary accuracy. Prokhorov gives relative weak compactness, not identification of the limit or convergence of the entire sequence. For paths, name the topology (`J₁`, `M₁`, uniform, `S`, pseudo-path, or another exact topology) and use its criterion; these topologies are not interchangeable.

Aldous (W01-L16, 1987 Berkeley report version) Proposition 1.2 (PDF p. 3) uses finite-dimensional martingale convergence, fixed-time uniform integrability, and a **continuous** limit to obtain `J₁` convergence. Proposition 2.2 (PDF p. 7) is a different criterion for general processes and requires the stated two-sided signed stopping-time increment condition. For martingale applications, Lemma 2.3 (PDF p. 8) is a proof bridge: optional sampling and a uniform tail cutoff for stopped increments yield the positive stopping-time probability bound required by Proposition 2.2. Neither result permits finite-dimensional convergence alone to imply path convergence. Weak convergence of filtrations is a separate process-level assertion; retain its filtration inclusion, right-continuity, UI, and process-specific hypotheses.

Skorokhod representation is a recoupling under its stated Polish/separability hypotheses; almost-sure convergence on the new space is not convergence on the original probability space. Specialized `S`-topology and Meyer–Zheng pseudo-path results are weaker than `J₁`/`M₁`; they do not prove a requested stronger path limit.

## Martingale-problem and adapted-law limits

Criens–Pfaffelhuber–Schmidt (B8 canonical source, Theorem 2.28/Corollary 2.31 and Theorem 4.3; PDF pp. 13–15, 25–26) gives a **limit-identification** interface. First establish tightness and convergence of the joint process laws. Then verify determining tests, weak or weak-strong continuity as applicable, UI for unbounded terms, and vanishing approximate martingale identities. Uniqueness is a separate step. Weak convergence alone does not pass unbounded expectations or upgrade to TV.

Kurtz 2014 (B17-004) develops weak/strong solution and compatibility methods for Polish input/output models. Keep its sufficient decomposition criterion and compatibility assumptions exact. The 2007 paper (B17-003) is read as a predecessor dependency in the same rewrite family; its printed martingale-condition “iff” is specifically corrected by the 2014 version and is not an additional independent source or a theorem to reuse unqualified.

Kurtz 1998 (B17-022), Theorem 3.2 and Corollary 3.5 (PDF pp. 12–15), concerns filtered martingale problems for conditional distributions and a Markov-function quotient criterion. Its setup needs the specified observation filtration, generator/forward-to-martingale assumptions, and uniqueness conditions. The paper explicitly warns that martingale-problem uniqueness need not imply forward-equation uniqueness without extra hypotheses. Use it only after a target model has a suitable Polish-state augmentation and the required generator and well-posedness; it does not supply queue stability, stationary tightness, or limit exchange.

Backhoff–Bartl–Beiglböck–Eder (B17-012), Theorem 1.2 (PDF p. 5), gives a finite-horizon discrete-time topology equivalence involving adapted Wasserstein and convergence of bounded continuous adapted stopping values under the stated law/moment conditions. It is not a general weak-topology result, continuous-time theorem, unbounded-reward result, or infinite-horizon tail bound. Use the source’s `inf` cost convention and do not change it to a supremum reward without a separate sign conversion.

Feehan–Pop (B8 canonical source, Theorem 1.3 and assumptions 1.8/1.11/1.13; PDF pp. 3–6) is a specialized half-space-supported Itô-process Markovization/mimicking theorem. Under its initial, coefficient, moment, inward-drift, ellipticity, and regularity/factorization assumptions it constructs a weak strong-Markov diffusion with the same one-time marginals. Equality of one-time marginals does not identify the path law. It is not a general construction of regular conditional kernels.

## Checked examples and invalid transfers

- **Valid fixed-test transfer:** if `μ_n⇒μ` on a metric space and `f≥0` is l.s.c., then Portmanteau gives `∫f dμ≤liminf∫f dμ_n`.
- **Invalid varying-integrand shortcut:** with `μ_n=δ_{1/n}⇒δ_0` and `f_n=1_{ {0} }`, pointwise `liminf_n f_n(0)=1`, but `∫f_n dμ_n=0`. Use the joint spatial/index lower envelope or prove a theorem’s extra regularity.
- **Weak convergence does not pass arbitrary expectations:** `X_n=n·1_{U≤1/n}` for `U` uniform converges to zero in probability while `E X_n=1`. Verify UI or another exact expectation-passage hypothesis.
- **Setwise is not TV:** oscillating dyadic densities can converge setwise while retaining a fixed TV discrepancy. Do not use setwise convergence in B18-002’s TV theorem.
- **Equal marginals do not imply equal paths:** two processes may have the same law at every fixed time and different joint laws over multiple times; Feehan–Pop’s output is a one-time-marginal statement.
- **Joint weak convergence does not identify conditional kernels:** a conditional law is a versioned, support-sensitive object. Supply continuity/selection or local-ratio assumptions from the theorem being used.

## Evidence status

R04 approved W01 strict-v2 for a new version. The original staging note recorded this version as not yet published or installed; that historical review state is distinct from the current repository migration. The source set contains 31 distinct independent works (30 papers and one book) across 32 acquired source records. Kurtz 2007 (B17-003) is retained as a full-text-read predecessor dependency and receives zero separate work-family credit; it is not double-counted with the 2014 rewrite. The ten v1 course and teaching fragments remain background and do not count.
