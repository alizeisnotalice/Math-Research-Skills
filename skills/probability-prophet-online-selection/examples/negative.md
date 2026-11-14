# Negative example: a guarantee with the wrong denominator

Do not say “the unit-density online knapsack ratio is 0.432” by quoting Proposition 3 of M0060. That proposition is an upper bound `(1−e^(−2))/2≈0.4323` relative to the ex-ante/flow LP `UP(H)`. The proved algorithm in §5.2 guarantees 0.3557 against that same LP, and the gap remains. Nor can a ratio against an integer offline knapsack optimum be substituted for the LP ratio. State both the algorithmic lower bound and universal upper bound with the same denominator, then mark the optimum unresolved.

Likewise, do not apply the 1/2 result for dynamic matching to arbitrary heterogeneous departure rates simply because the paper reports simulations with no counterexample. Its proof covers homogeneous departures, the bipartite side-wise homogeneous case, and two types; the general extension is conjectural.

Do not apply M0036's adaptive IID `1/β*≈0.745` one-slot threshold theorem to independent non-identical random-order inputs: the paper's heterogeneous random-order theorem is instead nonadaptive and gives `1−1/e`. Nor does either one-slot theorem settle the multi-unit `k>1` `inf_n` versus `n→∞` question.
