# Exact Bernoulli count laws and order comparisons

Supply the independent trial parameters as JSON integers or exact rational strings in ([0,1]). Include `comparison_probabilities` for a second law, which may have a different number of trials. The empty parameter list gives a count equal to zero. Parameters zero and one contribute deterministic trials.

```sh
python3 -B scripts/exact_bernoulli_sum.py examples/exact-bernoulli-sum-convex.json
```

For each law, entry (k) of `pmf` is (Pr(S=k)), and entry (k) of `survival_ge` is (Pr(Sge k)). The latter includes the zero entry at (k=n+1) for (n) trials. The pmf is computed by multiplying the Bernoulli factors ((1-p_i)+p_i z); the sum of the input parameters and the sum of (p_i(1-p_i)) give the mean and variance.

For `left_leq_right`, the script pads both laws on the common integer support and checks the following exact inequalities.

| Order | Finite criterion for (Xle Y) in the named order |
| --- | --- |
| Stochastic | (Pr(Xge k)lePr(Yge k)) at every integer threshold. |
| Convex | Equal means and (mathbb E(X-k)_+lemathbb E(Y-k)_+) at every integer threshold. These stop-loss functions are linear between consecutive integers. Equivalently, on the finite integer support each convex function is an affine part plus nonnegative multiples of integer-knot stop losses. |
| Likelihood ratio | (p_X(i)p_Y(j)ge p_X(j)p_Y(i)) for every (i<j), where (p_X,p_Y) are the pmfs. |
| Reversed hazard | (F_X(i)F_Y(j)ge F_X(j)F_Y(i)) for every (i<j), where (F_X,F_Y) are the cdfs. |

Cross products keep the last two checks valid at zeros. The reverse comparison swaps the two laws. In the example the left count is constant at one and the right count is (mathrm{Bin}(2,1/2)). The left count is smaller in convex order. The survival probabilities cross between thresholds 1 and 2.

For dependence, use the [fixed-count constraints](../SKILL.md) suited to the joint law. Marginal parameters alone do not specify the pmf of a dependent sum.
