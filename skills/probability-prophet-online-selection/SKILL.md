---
name: probability-prophet-online-selection
description: Analyze prophet inequalities, optimal thresholds, online resource allocation, and stochastic matching while preserving the arrival model and benchmark.
---

# Prophet inequalities and online selection

Use this skill when an online policy selects random rewards or allocates limited resources, especially when the claim compares it with an offline prophet, a fluid/ex-ante LP, or an omniscient dynamic benchmark.

Before transferring a theorem, write down (1) independence and distribution knowledge, (2) arrival order and who controls it, (3) capacity and whether decisions are irrevocable, (4) policy class, and (5) the exact denominator. These determine whether a quoted constant applies.

For the assigned A001/A002/A005 and online-allocation problems, the current evidence and unresolved interfaces are in [method.md](references/method.md), with source-by-source acquisition and reading status in [sources.md](references/sources.md). R07 independently approved 30 complete paper reads and one fully acquired book with complete selected Chapters 1 and 3, totaling 31 eligible reading sources. This is a complete-read baseline, not an assertion that all 31 uses have high mathematical review. See the final R07 review（本机附件：`evidence/project/reviews/R07/review.json`） for its exact version binding. Reader-ledger pending labels are retained as historical declarations; publication metadata is certified only where explicitly recorded. Partial and unread sources are excluded from the completed-source quota. The [W13 source ledger](references/sources.md) links the full assigned M0034–M0090 inventory and 19 supplements; `baseline.md`（本机附件：`references/baseline.md`） binds the exact R07 scope and hashes. The first eight original W13 sources are mapped in the revision 21 high-use scope（本机附件：`evidence/project/expansions/20261115/readers/L02/revision21/coverage.json`）; the next eight scoped key-proof overlays are in the batch02 scope（本机附件：`evidence/project/expansions/20261115/readers/L02/continuation_20261116/prophet_batch02/scope.md`）, and the selected S010–S018 uses are in the batch03 scope（本机附件：`evidence/project/expansions/20261115/readers/L02/continuation_20261116/prophet_batch03/scope.md`）, and six further scoped uses plus one held relevance case are in the batch04 scope（本机附件：`evidence/project/expansions/20261115/readers/L02/continuation_20261116/prophet_batch04/scope.md`）. After batch04, R02 reports at most 30 high-reviewed uses among the 31 historical baseline entries; S003 remains held and the count does not upgrade all 31. The active corrected statements and positive/missing-condition cases（本机附件：`examples/l02_continuation_20261116_cases.md`） are in [`method.md`](references/method.md). The method-by-method partial coverage map for G06.01–G06.05, including the narrow M0062-only G06.05 structural result, is in the G06 coverage table（本机附件：`evidence/project/expansions/20261115/readers/L02/continuation_20261116/prophet_whole_entry_metadata_v2/G06_method_coverage.md`）.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

## Non-negotiable distinctions

- Do not interchange IID, independent non-identical, random permutation, adversarial fixed order, and freely selected order. State whether policies are adaptive or static.
- Name the comparator: expected offline top-k prophet, online dynamic optimum, ex-ante/flow LP, or omniscient long-run reward-rate. Approximation ratios across different denominators are not directly comparable.
- In threshold arguments define strict exceedance counts explicitly. If distributions have atoms, state the tie convention or random tie-breaking probability.
- Keep a limit for one fixed distribution separate from an infimum over distributions that may vary with n. Do not infer termwise monotonicity from an equality of limit and infimum.
- A conjecture, open problem, finite numerical search, or first-page bibliographic inspection is not a theorem. For computational evidence, run the exact finite model where possible, save code/output, and label it numerical or finite-instance evidence.
- For matching and OCRS, specify the resource feasibility family, batch/arrival process, correlation assumption, and adversary model. Dynamic matching with departures, one-shot online matching, and static resource allocation use different state spaces and benchmarks.

When using an exact result, record the theorem/proposition number, PDF and printed page if both exist, all quantifiers and hypotheses, and the precise inequality. See the positive and negative examples for the A002 calibration and model-transfer checks.

## L02 revision: Bernoulli tails and source-specific limits

For a random-order threshold claim, define `B_i(t)=1{V_i>t}`, `D(t)=Σ_i B_i(t)`, the strict/weak convention, and the acceptance capacity. Keep `E D(t)`, `P(D(t)≥k)`, expected utilization, and the ex-ante/flow-LP benchmark as separate quantities. The exact Poisson-binomial PGF is `Π_i(1-p_i+p_i z)`; an exact coefficient calculation is finite evidence, not a stockout-calibrated prophet theorem. See `examples/l02_order_and_tail_cases.md`（本机附件：`examples/l02_order_and_tail_cases.md`）.

For M0067's balanced capacity-k Bernoulli reduction, use atomless marginals or Remark1 randomized ties with adjusted indicators. Lemma4 fixes `δ=φ*_k`, not arbitrary `φ`; the fixed-δ Lemma5 subproblem is separate. Lemma6/Poisson retains balanced-optimum assumptions including `φ*_k≥1/2`. Replace the source Lemma7 proof with R09's compactness/subsequence/unique-Poisson-root repair; do not claim quantitative constants from that repair. Price calibration is order-oblivious, but allocation and welfare may depend on the fixed arrival order. See the corrected M0067 card（本机附件：`evidence/project/expansions/20261115/readers/L02/revision6/cards/PR-92095869f9f6.md`）.

The constrained-order result M0058 applies to independent nonnegative values, one acceptance, and a preselected finite permutation family. Theorem 3.4's exact `φ⁻¹` threshold ratio requires `n≥3`; its statement is distinct from Theorem 3.1's lower bound. Random tie handling is in Section 2, physical pp.5–6. Physical pp.15–16 are Appendix B permutation/auxiliary estimates. It provides no `k>1` stockout calibration and no Palm or dynamic-programming certificate.

For M0072, copies are resource/market augmentation while capacity remains one. Proposition 1 is physical pp.7–8. Theorem 1's expected-reward lower bound imports [7, Theorem 2.2] at physical p.15. Proposition 4 uses the source constant `1/(60ε)`. State its Θ complexity forms in the `ε↓0` regime. Preserve R10's targeted-revision hold.

M0055 Lemma 3.8 is `E_T[F(1_T/2)] ≥ F(x)/16`, not a bound on raw `E[f(T)]`; the source-reported Theorem 5.2 `O(1)` has no repaired constant here. Do not infer `1/6400`.

These M0055/M0058/M0072 cards are prior-reading reuse in the separate L02 revision packet. They provide no new Bernoulli-extremal source quota. The new G05 draft has its own coverage and source ledger; do not merge its pending source count with this skill's reviewed baseline.

See `references/l02_revision1.md`（本机附件：`references/l02_revision1.md`） for the original corrected locator record and `references/l02_revision6.md`（本机附件：`references/l02_revision6.md`） for G05 provenance and explicit cross-tool count boundaries.


## L02 Bernoulli tools for threshold demand (no Prophet quota merge)

When a threshold policy creates a random demand count, define its independent effective indicators with the exact tie rule and use the L02 G05 crosswalk（本机附件：`references/l02_revision16_g05.md`） to select a count-law tool. Exact Poisson-binomial recursion is the default. Dümbgen–Wellner can give a **relative** matched-mean Poisson event bound only with independent Bernoulli probabilities `<1`; deterministic probability-one indicators must be shifted out and the event/comparator recalculated. Komisarski–Rajba 2018 supplies a parameter-majorization convex-order/stop-loss comparison, not monotone stockout tails. Boland–Singh–Cukic needs an independent comparator pair; Pinelis is only the restricted iid `F^3_+` moment interface. Positive and failure cases are in the L02 examples（本机附件：`examples/l02_revision16_stockout_cases.md`）.

A G05 count or tail bound is a risk input, not a prophet policy theorem. It does not by itself prove an online/offline reward ratio or close the k>1 stockout-calibration conjecture. Preserve the acceptance capacity, arrival model, tie handling, information constraints, and benchmark denominator when composing with a separate prophet guarantee. None of these four G05 works is added to the separate R07 Prophet/G06 31-unit baseline.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。
