# Positive cases: exact concentration interfaces

Each case below is a use of one accepted source interface. The full conditions, theorem locators, and exclusions are in `references/scope_register.md` and the linked source card.

## Product entropy coefficient checked from the proof

For a finite product probability space and a nonempty set `A` of positive mass, the checked §4 entropy argument gives

`P(A) E exp(d_A²/14) ≤ 1`.

This is the coefficient proved by the audited entropy route. The article's opening `1/4` statement is a separate source claim whose original induction proof was not checked here; the `1/14` result does not refute that statement.

## Independent-coordinate Bernstein interface

For a product input law, measurable integrable `f`, and the source's centered coordinate-replacement differences, verify the finite `V,M` or `V_p,M` assumptions. Then apply only P003 Theorems 3.2–3.3 with the denominators recorded in the scope register. The displayed entropy proof supports the separately derived `64e` constant; do not silently use the printed `32e` line as if that proof established it.

## Common-marginal interval probability under arbitrary dependence

For `d` coordinates with common CDF `F`, set `u=F(x)` and `v=F(x+ε)`. P019 gives the source's pointwise lower and upper extrema for `P(x<max_i X_i≤x+ε)` over arbitrary copulas. This applies to the interval `(x,x+ε]`; it does not require or admit convexity of the copula diagonal, and it does not cover unequal marginals.

## Finite-vector Gaussian coupling

For `n≥3` independent centered `R^p` vectors with finite absolute third moments, form matching-covariance Gaussian vectors and retain P018 Theorem 4.1/Corollary 4.1's exact `β,δ,B₁,B₂,B₃` or `B₄` terms. The permitted statement is finite-vector coupling with the source's auxiliary-uniform/extension construction. It does not yield a whole empirical-process coupling, a VC rate, anti-concentration, or bootstrap validity.

## Finite-variance concentration-function lower bound

For a real random variable `W` with finite variance and `ε>0`, P020's admitted interface is the universal lower bound

`Q_closed(W,ε) ≥ ε / sqrt(12 Var(W)+ε²)`.

Its proof here is the independent uniform-smoothing and bounded-density argument. The source's Gaussian order-statistic and supremum upper-bound chain is held pending closure of a proof step; the theorem statements are not declared false.

## One-sided anytime martingale crossing

Let `(X_i,F_i)` be centered, square-integrable martingale differences with deterministic one-sided cap `X_i≤c`, `c>0`, and predictable conditional variance `V_n=Σ_{i≤n}E[X_i²|F_{i−1}]`. For `a,b>0`, Freedman (1975) gives

`P(∃n: S_n≥a, V_n≤b) ≤ exp[−(b/c²)h(ca/b)] ≤ exp[−a²/(2(b+ca))]`,

where `h(u)=(1+u)log(1+u)−u`. This does not replace predictable variance by realized squares or unconditional variance. A lower-tail statement needs a separately verified cap for the reflected increments.

## Equal-sample two-sample reflection tail

For two independent samples of the same size `n` from one common continuous law, use P035's exact equal-sample reflection formula. The separately derived envelope `2 exp(−k²/(n+1/2))` is available at the card's lattice thresholds. The source's `C=2` iff `n≥458` certification and its unequal-size tables are outside scope.

## Independent bounded Hoeffding

For independent centered variables with deterministic ranges `[a_i,b_i]`, the exact one-sided bound is `exp(−2t²/Σ_i(b_i−a_i)²)`. Independence is required for tensorization. The independent proof in the package is also used for the finite-candidate validation case; it does not authorize applying Hoeffding to dependent coordinates.
