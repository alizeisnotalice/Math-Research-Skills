# Negative examples: three invalid substitutions

### Total count does not encode all block moments

Two laws can have the same complete law of `S_1+S_2` yet different `E[S_1S_2]`. The exact size-2-block construction is in the package-local exact check（本机附件：`evidence/project/expansions/20261115/readers/L07/math/l07_initial_checks.py`）. Do not reduce a block-vector moment problem to a single total-count distribution without a theorem that the event and feasible class are fully exchangeable over all coordinates.

### Two-level majority does not solve the iterated question

BGP Theorem 16 concerns two-level majority-of-majorities. Its §5 Question 4 asks about iterated majority of threes and is unanswered there. A recursive message map, mixed-moment propagation and error accumulation need separate proof.

### G14 Fourier methods are a separate handoff

For three-bit parity, each coordinate has forced-flip influence 1 but each singleton Walsh coefficient is 0. Conversely, a nonzero singleton coefficient witnesses dependence on that coordinate but does not certify a condition on all coordinates. Check output coding: the exact Fourier formula for influence has a factor 4 for a `{0,1}`-valued function and no factor for a `{-1,1}`-valued function.


## Revision9 missing-condition cases

### Weighted allocation denominator

For `c=(1,-1)` and atom `B={1,2}`, `c(B)=0`; the atom allocation is undefined, so the weighted-summary theorem does not apply. For `N>=4`, weighted row sums also do not identify every individual pair intersection.

### Missing cross-block moment

With two singleton events of marginal `1/2` but no `S_(1,1)`, identical events give union `1/2`, while disjoint events give union `1`. The separate block marginals cannot certify the union.

### Missing known-mode bridge

For `n=4`, `k=2`, `S_1=2`, `S_2=8/5`, imposing only nonnegative split differences but omitting `Σ_{i<=k}v_i>=Σ_{i>k}v_i` enlarges the feasible set: the original-p known-mode maximum is `19/50`, while the unbridged split relaxation reaches `7/15`. The counterexample and exact certificate are recorded in the R07 bridge check（本机附件：`evidence/project/expansions/20261115/readers/L07/revision9_1/math/R07_shape_bridge_check.out.json`）. Use the original-p shape LP unless every transformed constraint has been verified.

### Block-label lift

A multivariate count LP bounds only the supplied mixed-moment class. It does not automatically lift to an arbitrary labelled event law with heterogeneous marginals. Prove that averaging preserves every labelled constraint and objective before calling the reduction exact.


## Revision11 missing-condition cases

- A count LP matching only total-count moments cannot certify labeled cross-block k-wise independence; retain every mixed factorial constraint before claiming a lift.
- A pointwise bound valid at every original count site is valid with zero shape multipliers. The incorrect move is to use transformed/relaxed columns and claim sharpness for the full known-mode LP after dropping its bridge, or to use shape multipliers with the wrong sign.
- Generic labeled partial-intersection union optimization is NP-hard in worst case even when inputs specify only sets of size at most two; finite formulation alone does not imply an efficient algorithm.
- R07 confirmed the Adler–Karp–Ross physical-p.7 table values `0.1896/0.7871` are inconsistent with the displayed product law; isolate those table entries while retaining the accepted exact Theorem-5 formula.
- The unused PSS heterogeneous-Bernoulli mode shortcut fails for `n=2`, parameters `(16/25,1/100)`: its value is 0 although the exact count law has unique mode 1.
- Uniform PGF closeness does not imply total-variation closeness: `δ_k` and `δ_(k+1)` have TV distance 1 but PGF sup norm `k^k/(k+1)^(k+1)→0`; coefficient bounds need summable/tail control.


## Revision12 missing cross-block moment

The two laws in the positive example have the same entire total-count distribution but different cross-block moments. A total-count LP cannot substitute for the mixed moment vector when the target constraints include cross-block labeled intersections.


## Qiu scale and normalization boundary

Do not mix the main-text scaled variables `v_ij=u_ij/i` with Appendix-1 unscaled `u_ij=P(N=i,X_j=1)`. Their moment rows and tail objectives differ; retain `p0+Σ_{i≥1,j}v_ij=1` under the scaled convention. Fixed-layer homogeneous projection cuts are invariant under this positive rescaling, but the full LP normalization is not optional.


## Revision15 missing inference steps

- Pairwise independence does not fix a three-factor product: the exact Bernoulli(1/100) example in the positive section has matching all first/second moments but a nonzero product gap. Use the small-total-variance theorem only with its stated range and variance, and preserve the source’s tail-probability form.
- Fixed marginals do not specify an independent joint law. In the three-Bernoulli example, independence gives event probability 1/2 while the exact worst-case value is 3/4.
- Do not use the compact Bernoulli or PERT formulations outside their source assumptions. For general finite supports or arbitrary combinatorial regions, the finite atom LP remains the safe model unless a separate separation/compactness proof is supplied.


## Revision15.1: missing complement dual constraints

For three Bernoulli(1/2) marginals and event `c_1+c_2+c_3≥2`, the event-only potential `−1+c_1+c_2+c_3` has expected value `1/2` but is negative at the atom `000`; it is not dual-feasible. The normalized atom dual must separately be at least 1 on the event and nonnegative on every complement atom. R07’s exact source-specific condition record preserves both constraints.

## Uncovered G13 routes

- Do not claim G13.05 tensor-moment/tree-message coverage from Gopalan–Yehudayoff. Its admitted use is a bounded-factor expectation approximation and symmetric-polynomial tail bound under explicit independence-order hypotheses; it does not define subtree messages, close cross-child moment states, or prove a recursive lift.
- Do not infer G13.06 multilevel stability from one-level or two-level estimates. A recursive theorem needs a proved one-step transition on its message state and a quantitative error recurrence with order, conditioning, and dependence costs.
- Do not use a generic finite count LP as a tree algorithm. If the constraints omit cross-child joint moments needed by the objective, the count LP is only a relaxation.
