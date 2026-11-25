# Negative cases: do not enlarge an admitted interface

## Dependence and anti-concentration mismatch

**Unsafe claim:** “The summands are exchangeable, so the independent matrix Bernstein bound applies; that upper-tail estimate also bounds the probability of a short interval.”

**Why this fails:** P001 assumes independent summands and controls an upper tail. Exchangeability does not supply independence, and a one-sided tail does not bound `P(|Y−t|≤ε)`.

**Repair:** Verify the dependence assumptions of the selected source. For interval probabilities, use a separately admitted anti-concentration interface, such as P012 only for a separable centered Gaussian process with unit marginal variances and finite supremum.

## Copula refinement without its source conditions

**Unsafe claim:** “The common marginal law and a convex-looking model let me use P019's improved convex-diagonal estimate.”

**Why this fails:** The current P019 admission is only the arbitrary-copula pointwise interval extrema for a common CDF. It excludes the convex-diagonal refinement and nonidentical marginals.

**Repair:** Use only the common-CDF bounds in the scope register, or establish a separately reviewed source interface before invoking another refinement.

## Using P020's held upper-bound chain

**Unsafe claim:** “P020's Gaussian order-statistic theorem supplies the desired upper concentration bound.”

**Why this fails:** The admitted P020 result is only the independently completed finite-variance concentration-function lower bound. The negative-`s` sum-closure step in the upper-bound proof remains an unresolved proof concern in this review. This package does not declare the stated upper theorem false.

**Repair:** Use P020 only for its lower bound, or provide a separate proof of the upper statement and its hypotheses.

## Promoting the P022 squared-norm bound to norm comparison

**Unsafe claim:** “The two largest covariance eigenvalues give the full Gaussian Hilbert-norm comparison scale.”

**Why this fails:** P022's admitted result is an explicit density bound for a shifted squared norm when `λ₁≥λ₂>0`; it does not establish full spectral comparison, and rank one is outside the finite density bound.

**Repair:** Apply only `sup_x f_{||G+h||²}(x)≤1/(2√(λ₁λ₂))` with its trace-class and rank-at-least-two hypotheses. Preserve that the conclusion concerns the squared norm and short bands derived from its density.

## Coupling without an anti-concentration step

**Unsafe claim:** “P018 makes two finite-vector statistics close, therefore their distribution functions are close uniformly.”

**Why this fails:** A coupling controls distance on its coupling space. CDF error also depends on how much mass the comparison statistic places in short intervals. P018's admitted scope is finite-vector Theorem 4.1/Corollary 4.1, not a full empirical-process, bootstrap, or anti-concentration theorem.

**Repair:** Add a separately justified interval-modulus bound for the comparison statistic and keep the coupling error and anti-concentration term distinct.

## Confusing the P027 tilt lemma with a Cramér theorem

**Unsafe claim:** “P027 proves a uniform martingale Cramér expansion, including the smoothing step, for either sign of `λ`.”

**Why this fails:** The admitted P027 use is Lemma 4.4's tilted-moment/bracket concentration under `0≤λ`, the stated `λε, λδ→0` regime, and `y≥4λδ`; the supplement-based smoothing step is not admitted. P028 remains held because its central proof supplement was unavailable.

**Repair:** Use only P027's exact Lemma 4.4 interface with nonnegative tilt and the source's parameter range. Do not use P028 or promote this lemma to a Cramér/MDP result.

## P029/P030 asymptotics as finite-threshold bounds

**Unsafe claim:** “The local Gaussian block limit or fixed-neighborhood localization gives the complete Pickands/manifold asymptotic or a nonasymptotic bound at a fixed threshold.”

**Why this fails:** P029 contributes only the fixed-`T` local block Lemma 4 with its stated constant and the separately completed `w`-dependent domination. P030 contributes only fixed-neighborhood localization under a uniform strict variance gap. Neither admission includes the full double-sum or manifold-stratum conclusion.

**Repair:** Keep each local statement at its admitted scope and asymptotic regime; do not infer a full high-excursion theorem or finite-threshold inequality.

## The P008 proof branch and the 1/8 route

**Unsafe claim:** “The published P008 `1/4` modified-log-Sobolev MGF chain follows from the printed ordered-sum bound.”

**Why this fails:** At `n=3` with the identity permutation and `R={I₃}`, the printed Eq. (4.3) squared-decrement bound fails (`24>18`). R14's corrected `4(n−1)S` bound supports the same route with a `1/8` range, not `1/4`. This does not affect the separately admitted independent first-positive-increment proof of Theorem 3.3.

**Repair:** Use P008 only for Theorem 3.3's nonnegative single-permutation statistic and retain its exact finite-array assumptions. Keep the 1/8 repair as a separate proof note; do not restore Lemma 4.2's full MGF or the unchanged downstream 1/4 constants.

## P003 printed constant versus the checked entropy route

**Unsafe claim:** “The displayed entropy argument proves P003's printed `32e` constant.”

**Why this fails:** The checked p. 9 argument gives the `64e` constant. The difference is recorded as a proof/statement mismatch; the source's theorem is not declared false.

**Repair:** Use the independently derived `64e` route under the stated product-law and coordinate-replacement conditions. Do not use the printed `32e` line as though the displayed proof established it. The separate Theorem 4.6 metric-scale issue remains held.

## Using P005's mis-scaled display for a sum

P005 defines `\bar M_n²=M_n²/n` and proves the sum inequality in Eq. (23). Its later Eq. (28) prints `exp(−n(t/\bar M_n)²/2)` for `S_n≥t`. For two independent Rademacher signs and `t=2`, the event has probability `1/4` while that right side is `e^(−4)`.

**Repair:** Retain Eq. (23), or rewrite its exponent using `M_n²=n\bar M_n²`. The later display may not be substituted as a sum-tail inequality.

## Hoeffding under dependence and finite-list selection

**Unsafe claim:** “Hoeffding's independent-coordinate proof applies to exchangeable inputs,” or “validation of finitely many C168 candidates proves the global measurable-partition optimum.”

**Why this fails:** Independence is the tensorization condition. The C168 validation bound covers only candidates fixed before an independent validation sample; it supplies neither a covering of all measurable partitions nor a discretization error.

**Repair:** Establish independence before using the exact bounded Hoeffding bound. For C168, freeze the finite candidate list before validation and report the simultaneous finite-list error only.

## Replacing Freedman's predictable variance

**Unsafe claim:** “Freedman's one-sided crossing bound remains valid after replacing `V_n=Σ E[X_i²|F_{i−1}]` by realized `ΣX_i²` or unconditional variance.”

**Why this fails:** The admitted theorem uses a predictable conditional-variance budget and a deterministic one-sided increment cap `X_i≤c`. Lower tails also require a reflected increment cap.

**Repair:** Verify the exact filtration, conditional means, cap, and predictable `V_n` event before applying the bound. Prove any alternative variance substitution separately.
