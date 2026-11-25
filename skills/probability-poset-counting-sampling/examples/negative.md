# Negative example: do not transfer across models

A path-permutation peak formula counts index peaks, where a_i exceeds its two sequence neighbors. In a square grid the peak predicate compares all in-square graph neighbors; the path formula does not apply.

A theorem about two peaks on a regular tree, or about peaks/craters on a cycle, uses a different graph geometry and often different boundary conditions. It cannot be cited as a theorem for a free-boundary square. Likewise, an Eden growth-cluster boundary theorem is not a random-bijection labeling theorem.

For a fixed poset P, its linear extensions are exactly the total orders satisfying a conjunction of pairwise comparisons. “Exactly two graph peaks” imposes a combination of alternatives (“some neighbor is larger” at each nonpeak); it is not one fixed poset's linear-extension set unless a separate, non-overcounting construction is proved.

Finally, distinguish:
- exact #LE from an FPRAS estimate of #LE;
- an exact stationary sample from a rapidly-mixed approximate sample;
- exact branch weighting from choosing uniformly among currently available vertices;
- finite n counts from an asymptotic concentration proof.

The W09 finite square calculation through n=4 is a useful recurrence and boundary check. It is not evidence for an asymptotic theorem by itself.

## Do not turn necessary peak checks into a complete guard

For M0002, the source definition excludes degree-0/1 vertices from being peaks, while the direct recurrence counts every strict maximum over its neighbor set (including leaves and isolates). On the two-vertex path, each labeling has one direct local maximum but the M0002 source peak set is empty; the exact enumerated examples are in R05 model-boundary cases（本机附件：`evidence/reviewer_records/poset_stage_v5_review/model_boundary_cases.json`）. The source-side necessary checks are that every required peak has degree at least two and no two required peaks are adjacent. These checks reject leaf-required and adjacent-required inputs, but they are not sufficient to establish the source's `G`-admissibility premise: on a cycle, `S=empty` passes both checks although every bijective labeling has a peak. The accepted interface requires known `G`-admissibility, branch-local state copies, and collection of all recursion leaves. An arbitrary-`S` call is outside the accepted scope; this is not a whole-paper source-error claim.

## Other source-specific transfer failures

- M0013's colored-graph refinement and stabilizer pruning are valid for the stated canonical-search tree, but symmetry pruning alone does not preserve the number of labeled extensions. Supply orbit multiplicities or a separate bijective recurrence before using it as a counting quotient.
- M0017's explicit `Q_(i,j,m)` family and disjoint/ordinal-sum count constructions do not prove its headline minimum-size optimization. M0019's interval reduction requires a width-two poset with connected incomparability graph and proves only the accepted entropy-preserving reduction with `e(Q)≤e(P)`; it does not yield every special case or an exact sampler.
- W09-X003 is a modular/Turing reduction, not a parsimonious map. W09-X004's counted edge sets use the combined cover–incomparability graph; replacing it with the cover graph can merge distinct extensions.
- W09-X006's offline sets `S,T` must be fixed independently of observed test outcomes, and PASS uses the threshold `((1−epsilon)/2)|S||T|`. The accepted row does not certify the full `epsilon^4` upper-entropy theorem or the stronger printed mixture coefficient.
- W09-X010's CFTP correctness uses fair bits and a supplied legal extension. Recursive replay reuses that call's original block and independent calls use independent blocks. Do not turn the row into the source's excluded expected-runtime/extinction-rate theorem or a graph-peak sampler.
- W09-X013 needs the supplied valid arc-DAG and legal order. Its accepted safe state/slot bound is `O(n^(alpha+2))` when the supplied activity width `alpha` is fixed; the row neither certifies the optimized exponent nor an algorithm that finds minimum activity.

These are scope limits of accepted uses. They are not whole-paper source-error determinations.
