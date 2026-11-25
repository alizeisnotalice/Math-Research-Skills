---
name: probability-measure-convergence
description: Analyze weak convergence, tightness, conditional laws, changing integrands, and martingale-problem limits. Use when a proof passes from stochastic models to limits of probability measures or needs a precise convergence mode.
---

# Probability measures and convergence

Use this skill to identify which convergence theorem a probability argument actually supports. Start by naming the state space, sigma-field, topology, limit law, and test class. Keep weak convergence, setwise convergence, total variation, Wasserstein convergence, convergence in probability, and almost-sure convergence distinct.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

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

For conditional large deviations, use only van Zuijlen (B18-005) Theorem 1.2 / Theorem 6.9 sufficient directions `(A2)⇒(A1)` and `(B2)⇒(B1)`: a good joint LDP, chosen weakly continuous product regular conditional kernels on each conditioning support, finite fiber-rate normalization, and the exact uniform local-ratio premises. The lower numerator is `closure(U)` and the upper numerator is `interior(W)`; retain the source’s nested neighborhood/limit orders and support restrictions. Do not use a converse, Theorem 1.3, or infer a conditional LDP from joint weak convergence or a joint LDP alone. The approved scope does not rely on Example 9.1.

For Gaussian conditional continuity and operator formulas, use the exact Banach or Cameron–Martin norm assumptions from the source cards. A scalar covariance ratio does not imply an operator-norm bound; a Hilbert-topology isomorphism does not imply continuity of its inverse in a weaker ambient topology. The finite-rank and infinite-rank Gaussian disintegration theorems also have different proof status and assumptions.

## Tightness, paths, and representations

A family of laws on a Polish space is tight when one compact set captures mass uniformly to arbitrary accuracy. Prokhorov gives relative weak compactness, not identification of the limit or convergence of the entire sequence. For paths, name the topology (`J₁`, `M₁`, uniform, `S`, pseudo-path, or another exact topology) and use its criterion; these topologies are not interchangeable.

Aldous (W01-L16, 1987 Berkeley report version) Proposition 1.2 (PDF p. 3) uses finite-dimensional martingale convergence, fixed-time uniform integrability, and a **continuous** limit to obtain `J₁` convergence. Proposition 2.2 (PDF p. 7) is a different criterion for general processes and requires the stated two-sided signed stopping-time increment condition. For martingale applications, Lemma 2.3 (PDF p. 8) is a proof bridge: optional sampling and a uniform tail cutoff for stopped increments yield the positive stopping-time probability bound required by Proposition 2.2. In the Proposition 2.2 proof, keep the source's corrected roles: `g` is the small-oscillation reference, while `f` defines `T_σ` and its post-stop increments (Lemmas 4.1/4.10, PDF pp. 11–14). Neither result permits finite-dimensional convergence alone to imply path convergence.

For filtration convergence, W01-L17 admits only Theorem 1: on a common probability space with finite horizon and right-continuous `Fⁿ⊂F`, use the paper's weak-filtration mode, an adapted càdlàg decomposition `X=M+A` with `M` UI, `A` continuous, `A₀=0`, and `E sup|A|<∞`; then `E[X_t|Fⁿ_t]→X` in probability in `J₁`. A changing-terminal-variable condition from Remark 1(2) requires `L¹` convergence; convergence in probability alone does not suffice. Do not import Theorems 2–3, Hᵖ/UT/bracket, or BSDE conclusions.

Other path and law-space interfaces in the current source cohort have different topologies and hypotheses. W01-L18 gives tightness for random finite Borel measures on Polish `S` through rare modifications with relatively compact expected measures; the converse requires UI of total masses. W01-L19 gives `S`-compactness on real `D([0,1])` from sup and rational-level upcrossing bounds or bounded-variation approximations; it gives no `J₁` implication or fixed-evaluation continuity. W01-L20 gives pseudo-path graph-law tightness and quasimartingale closure under the source's uniform conditional-variation bound and terminal convention; pseudo-path topology is weaker than `J₁`/`M₁`. W01-L21 concerns compactness of randomized stopping times only under its bounded raw continuous-process tests and fixed marginal. W01-L22 transfers stable convergence of empirical-predictive error under `P≪Q`, a countably determined class, and UI of `||W_n||` under both laws. W01-L23 is only the truncated-uniform-cost criterion on `D[0,1]`: `W_u→0` iff a common new-space coupling has uniform distance tending to zero in probability; it is not an almost-sure or original-space representation. Use each source's exact card for definitions and remaining assumptions.

Weak convergence of filtrations, pseudo-path convergence, `S`-topology convergence, and `J₁`/`M₁` convergence are separate assertions; retain each source's topology and transfer conditions.

## Additional reviewed limits and couplings

For W01-L18, use only the random finite-measure tightness criterion for finite Borel measures on Polish `S`: approximate each random measure by an integrable modification with uniformly small probability of change and require relative compactness of the expected measures; the converse retains uniform integrability of total masses. W01-L19 is limited to real `D([0,1])`: sup and rational-level crossing/oscillation control or bounded-variation approximations yield `S`-compactness, not `J₁`/`M₁` convergence or fixed-time evaluation continuity. W01-L20 concerns real càdlàg paths on `R₊` with a limit at infinity under the source's `e^{-t}dt` graph-law pseudo-path topology; its quasimartingale closure needs the exact uniform conditional-variation bound and terminal convention. Neither is an arbitrary fdd or local-bracket theorem.

W01-L21 covers compactness of randomized stopping times on compactified time `[0,∞]` under a fixed marginal and the paper's bounded raw continuous-process tests; do not substitute arbitrary càdlàg tests or ordinary stopping times. W01-L22 is a stable change-of-measure transfer in the coordinate c.i.d. setup: retain a countably determined class, `P≪Q`, stable convergence under `Q`, and UI of `||W_n||` under both `P` and `Q`; the faster-rate and urn results are not included. W01-L23 is Lemma 12 only on `D[0,1]` with its Borel sigma-field and truncated uniform cost: vanishing transport cost is equivalent to a common **new-space** coupling with uniform distance tending to zero in probability. It gives neither almost-sure nor original-space coupling, nor a shortcut from `J₁` distance.

Skorokhod representation is a recoupling under its stated Polish/separability hypotheses; almost-sure convergence on the new space is not convergence on the original probability space. Specialized `S`-topology and Meyer–Zheng pseudo-path results are weaker than `J₁`/`M₁`; they do not prove a requested stronger path limit.

## Martingale-problem and adapted-law limits

For the Criens–Pfaffelhuber–Schmidt canonical source, the admitted interface is the **control-free limit identification route** in Corollary 2.31 and Proposition 2.32 (PDF p. 14). It assumes a Polish state/path setting, right-continuous adapted real test processes, an explicitly determining bounded test family, almost-sure continuity of the relevant canonical evaluations and products under the limit law, joint UI on compact time intervals, weak convergence of the path laws, and vanishing approximate martingale tests. Theorem 2.28 and Theorem 4.3 are not admitted as additional weak-strong or fixed-jump interfaces in this candidate. Tightness and uniqueness are separate; weak convergence alone does not pass unbounded expectations or upgrade to TV.

Kurtz 2014 (B17-004), Theorem 1.5, is admitted for Polish input/output models with fixed input law and the paper's class of admissible joint laws: weak existence plus pointwise uniqueness is equivalent to the existence of a strong solution together with joint uniqueness in law. The abstract theorem needs no convexity or compatibility assumption; compatibility is a separate sufficient premise for martingale preservation. The 2007 paper (B17-003) is a predecessor dependency in the same rewrite family; its printed martingale-condition “iff” is corrected by the 2014 version and is not an additional independent source or an unqualified theorem to reuse.

Kurtz 1998 (B17-022), Theorem 3.2 (PDF pp. 12–13), is admitted only as a filtered martingale lifting/conditional-law uniqueness route under its explicit augmented forward-equation-to-martingale representation premise. The sufficient interface normalizes the generator by adjoining `(1,0)∈A` with `A1=0` and requires that representation premise for the resulting normalized augmented operator, including its coordinate-cylinder tests. The observation filtration is the completed integral-history filtration; the proof uses countable Laplace coordinates and the physical p. 9 coordinate-ODE argument. Original MP uniqueness is used only for the final uniqueness conclusion. Do not infer the representation premise from bare MP uniqueness or extend this row to Corollary 3.5, quotient-Markov, queueing, stationarity, or limit-exchange claims.

For Backhoff–Bartl–Beiglböck–Eder (B17-012), use only Lemma 7.1 (PDF pp. 42–43): on a finite discrete horizon and Polish state space, adapted Wasserstein convergence in the stated order implies convergence of the `inf` values for bounded continuous adapted costs. Both causal directions and the source’s coordinate-filtration setup are part of the interface. This does not admit the paper’s full topology equivalence, continuous-time or infinite-horizon claims, unbounded rewards, or an ordinary weak-convergence shortcut. Do not change the `inf` cost convention to a supremum reward without a separate sign conversion.

For Feehan–Pop, the admitted result is only the independent, unshifted compactly supported `C²` one-time weak forward identity obtained by conditional projection of the given half-space-valued Itô process. It uses the source’s initial and coefficient assumptions, integrability of the drift and covariance, measurable conditional coefficients, and compactly supported `C²` test functions. The full mimicking, weak-existence, uniqueness, and strong-Markov conclusions are held: the finite-ε estimate in the source has a gap, and this identity does not depend on that estimate or on an imported PDE result. Equality of one-time marginals does not identify the path law.

## Reviewed continuation interfaces (2026-11-16)

R03 high-review matched all 31 distinct works in the existing source cohort for scoped uses. The exact theorem interfaces, assumptions, locators, and transfer limits for every admitted source are in the frozen scope register（本机附件：`references/scope_register.md`） and the machine-readable source admissions（本机附件：`evidence/scoped_uses.json`）. The registry governs any source-specific claim above. It does not approve every theorem or every claim in a cited work, and at this immutable candidate freeze, whole-entry scientific review, case review, and portable review remain pending; publication/install status is tracked separately by the root release receipt.

The W01-L12 continuation includes a separately derived graph/BL/countable-partition representation route under the source’s original separable-metric and Borel-map hypotheses. It uses a new common probability space and needs no completeness, Radon, or regular conditional distribution assumption. See its card and the independent R03 review in the evidence index; do not restore its older held Lusin proof.

## Checked examples and invalid transfers

- **Valid fixed-test transfer:** if `μ_n⇒μ` on a metric space and `f≥0` is l.s.c., then Portmanteau gives `∫f dμ≤liminf∫f dμ_n`.
- **Invalid varying-integrand shortcut:** with `μ_n=δ_{1/n}⇒δ_0` and `f_n=1_{ {0} }`, pointwise `liminf_n f_n(0)=1`, but `∫f_n dμ_n=0`. Use the joint spatial/index lower envelope or prove a theorem’s extra regularity.
- **Weak convergence does not pass arbitrary expectations:** `X_n=n·1_{U≤1/n}` for `U` uniform converges to zero in probability while `E X_n=1`. Verify UI or another exact expectation-passage hypothesis.
- **Setwise is not TV:** oscillating dyadic densities can converge setwise while retaining a fixed TV discrepancy. Do not use setwise convergence in B18-002’s TV theorem.
- **Equal marginals do not imply equal paths:** two processes may have the same law at every fixed time and different joint laws over multiple times; Feehan–Pop’s output is a one-time-marginal statement.
- **Joint weak convergence does not identify conditional kernels:** a conditional law is a versioned, support-sensitive object. Supply continuity/selection or local-ratio assumptions from the theorem being used.

## Evidence status

The 2026-11-16 reader candidate binds 31/31 distinct works in the existing measure-convergence cohort to scoped R03 high-review admissions. It remains a candidate: whole-entry scientific review, case review, portable review, publication, and installation are pending. No new complete read or global reading credit was added in this continuation. Kurtz 2007 (B17-003) remains a predecessor dependency with zero separate work-family credit and is not double-counted with the 2014 rewrite. The original 197-file manifest has no preimage and is not reconstructed. The already-installed `probability-variational-limits v5` was not changed.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
