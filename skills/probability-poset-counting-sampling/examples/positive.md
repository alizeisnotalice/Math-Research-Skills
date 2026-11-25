# Positive example: exact finite free-square counts

For the free-boundary n×n grid, build only in-square nearest-neighbor edges and use the descending-order recurrence from [method.md](../references/method.md). On selection of v, it contributes one peak exactly when all its neighbors remain unselected.

The checked implementation is verify_counts.py（本机附件：`evidence/cases/verify_counts.py`）; the saved output is verification_results.json（本机附件：`evidence/cases/verification_results.json`）.

| n | Total labelings | Exactly 1 peak | Exactly 2 peaks | DP states |
|---:|---:|---:|---:|---:|
| 2 | 24 | 16 | 8 | 37 |
| 3 | 362,880 | 29,568 | 143,808 | 902 |
| 4 | 20,922,789,888,000 | 35,704,394,880 | 779,299,174,080 | 74,217 |

The DP agrees with an independent enumeration of all `(n²)!` labelings for n=2 and n=3. For n=3, among the 143,808 labelings with exactly two peaks, Manhattan distances 2, 3, and 4 occur 63,552, 64,512, and 15,744 times, respectively. One seeded exact branch-sampling trace is also saved; its existence demonstrates the finite sampler, not a distance limit.

These are exact finite calculations. They do not show that the normalized peak distance tends to zero as n grows.

## R05-scoped M0002 interface

For a finite simple graph and a prescribed set `S` already known to be `G`-admissible, the accepted `GraphPeakSetAlgorithm` interface tracks the allowance set `L` with `V_{<2}(G)⊆L⊆V`. Initialize `L=V_{<2}(G)` for an exact-set call, apply `L←(L∪N(v))∩(V\{v})` on each branch, use independent branch-local copies of `S`, `L`, and labels, and collect every recursion leaf. R05 accepted only this scoped use; it carries no polynomial-time or sampling guarantee. Exact review bindings and proof locators are listed in the M0002 scope row（本机附件：`references/accepted_scope_register.md`）.

## Additional source-audited interfaces (each with its own model)

These cases are accepted for the narrow interfaces below; the 30-row scope map（本机附件：`references/accepted_scope_register.md`） lists all other approved source uses and their limits.

- **Finite-poset encodings:** M0006 identifies Ehrhart counts of the order and chain polytopes with `Ω(P,m+1)` and their volumes with `e(P)/n!` for one fixed finite poset under the stated lattice convention. This can encode a conjunction of comparisons. A disjunctive graph-peak event first needs a disjoint decomposition or correct overlap weights.
- **Hardness and modular counting:** M0007's general `#LE` hardness is a polynomial Turing reduction using several prime-sized gadgets and modular/CRT reconstruction; it is not parsimonious and is not a hardness result for the free-square two-peak restriction. W09-X003's height-two construction is another modular/Turing reduction with prime `p>n` and CRT reconstruction after a sufficient prime product exceeds `n!`.
- **Symmetry-aware exact count:** W09-X004 counts fixed-poset extensions by acyclic reorientations of every incomparability edge in the combined cover–incomparability graph. For its bounded-treewidth MSO route, retain directed cover edges and every labeled incomparable pair; a cover graph alone is not the same counting object.
- **Narrow entropy reduction:** M0019 applies when the width-two poset has a connected incomparability graph and the source's canonical interval representation is used. The reduction preserves that graph's entropy and gives `e(Q)≤e(P)`; it does not establish every special case or a universal entropy-to-count inequality.
- **Exact sampler:** W09-X010 uses a supplied legal extension, fresh fair bits in each left-to-right adjacent-position sweep, an active-item bounding chain, and a fixed-block recursive CFTP construction. A recursion call replays its own block; expected-operation and extinction-rate claims are outside this row's accepted proof scope.
- **Direct active-map DP:** W09-X013 requires a supplied valid N-free arc-DAG representation and a supplied legal order. Its direct active-vertex last-position insertion recurrence is safe at `O(n^(α+2))` when the supplied activity width `α` is fixed; it does not prove the optimized exponent or compute a minimum-activity order.

The cases share the discipline “state exact object → prove the encoding/recurrence → count with multiplicity.” Their state spaces and guarantees are not interchangeable.


The exact direct-recurrence positive output is the reviewed R05 replay in verification_results.json（本机附件：`evidence/cases/verification_results.json`）. The older worker aggregate with one supplemental M0003 beta-identity entry is preserved separately and is not used as a generated-code equality target; see the R05 comparator correction（本机附件：`evidence/reviewer_records/poset_stage_v5_review/case_comparison_correction.json`）.
