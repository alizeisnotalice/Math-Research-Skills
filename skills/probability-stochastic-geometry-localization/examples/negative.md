# Negative examples: claims that need a missing bridge

## Symmetry does not prove Haar optimality

If translating a center law leaves the expected cover time unchanged, its orbit average is Haar. To infer that Haar has no larger objective, prove that the expected cover-time functional is convex under mixtures of center laws or provide another comparison. Invariance alone only says all translates have the same value; it gives no inequality for their mixture. A fixed-radius counterexample also does not refute a growing-ball claim.

For the logical gap in the symmetry-only inference, let the compact group be `C2` and write a probability law as `(p,1-p)`. The abstract functional `F(p)=p(1-p)` is invariant under the group action `p↔1-p`, but `F(1/2)=1/4` while `F(0)=0`; Haar is not a minimizer. The exact SymPy check is in `abstract_symmetry_counterexample.py`（本机附件：`evidence/calculations/abstract_symmetry_counterexample.py`） with `output`（本机附件：`evidence/calculations/abstract_symmetry_counterexample.out.txt`）. This is only a counterexample for an abstract invariant objective, not for the actual growing-ball cover-time functional.

For the actual growing-ball model, Aldous (2022, printed p. 765) leaves the compact-group Haar question open. The same page gives a strict discrete-versus-continuous uniform comparison only for the **fixed-radius** circle model and says it is unknown whether that has a growth-model analogue. Therefore this source neither proves nor refutes Haar optimality for growing balls. Its bounds on `χ(S)` use covering numbers and do not identify the minimizing seed law.

## A124 concentration needs the `c*/E C` gate

Aldous's variance theorem is conditional on the ratio of the worst single-point mean hitting time to the whole-space mean cover time. The paper does not show this ratio is small in general. For `S_n=[0,n]`, with seed masses `θ_n({0})=1-1/n` and `θ_n({n})=1/n`, it gives
\[
n^{-1}C_n\Rightarrow\min\{1,(1+\xi)/2\},\qquad \xi\sim\operatorname{Exp}(1),
\]
a non-degenerate limit (Aldous 2022, printed p. 761). Do not report weak concentration merely because each space is compact or because the bound is stated.

## Finite receiver coverage is not complete spatial cover

For iid transmitters `X_1,…,X_n` and a finite receiver sample `Y_1,…,Y_m`, Higgs–Penrose–Yang's threshold asks that each sampled receiver be k-covered. The paper states this is only a lower bound on the radius covering every point of the region. Its Chen–Stein and count-bracketing de-Poissonization control that finite-sample threshold under `m/n→τ` and the stated Euclidean assumptions. They do not establish fixed-size transfer for continuum J-M cover time or a network span. Name the exact target functional before importing a coupling bound.

## Restricted J-M boundary effects cannot be dropped

For restricted J-M arrivals the centers lie inside `A`. The planar limit has both `|A|` and `|∂A|` terms; the unrestricted process has a different limit. Replacing one by the other erases a leading boundary contribution. The smooth `d≥3` theorem also assumes `A=\bar A°` and `∂A∈C²`. See Penrose–Higgs (2026), Theorems 2.1–2.3, and the source card（本机附件：`evidence/referenced/17474a78d25fb496-EXSRC-9c442ea403eae4f3-PenroseHiggs2026.md`）.

## Mecke does not de-Poissonize a network span

The Mecke formula converts an expectation over a Poisson process into an insertion integral. It does not bound how much the entire network span changes when the Poisson count differs from k, and it does not control routes that leave the window. Without functional sensitivity, a boundary-tail estimate, and uniform integrability, a Poisson length-intensity limit is not the fixed-k result.

## SIRSN scaling does not imply stabilization

Scale/translation invariance and finite edge intensity are structural properties of a network law. They do not furnish a finite-radius dependence cutoff or a tail bound for the effect of distant input. Do not cite generic Euclidean MST or coverage stabilization without proving that its radius and add-one estimates hold for this SIRSN route observable.

## Finite marginals do not bound the endpoint maximum

From `E len r(0,U)<∞` one cannot conclude `E sup_i len r(0,U_i)<∞`. The endpoints are sampled against one shared route network. A countable supremum requires a separate maximal or tail argument; a Poisson union-length bound or a typical close-pair average is a different statistic.


## Do not identify discrete cover criteria with growing-ball concentration

An iid coupon holdout condition is not the same as an age-dependent Poisson growing-ball process: the latter's ball radius depends on the arrival age, so the final covered set is not automatically a sequence of iid random subsets. Likewise, a finite-state monotone hitting potential is not available until a Markov state and a decreasing potential are proved. A fixed-radius disk theorem, a Boolean occupied-volume bound, or a Poisson-to-binomial continuum threshold cannot be pasted onto a continuous-time cover observable without a model-specific coupling and error estimate.


## G22.02: the deterministic-proxy hypothesis is not automatic

For the same `F=η([0,1])`, `V+=F` is unbounded. Therefore no finite deterministic `c` can make `V+≤c` almost surely, and the deterministic-proxy Corollary 3.3(ii) does not apply. The self-bounding Corollary 3.6 does apply. This is a missing-premise example, not a counterexample to either theorem.

Do not use this source to upgrade source12's imported `[1]` upper-tail or `[19]` median-tail branches. Source12 remains admitted only for deterministic local deletion-cost under its own `K1–K3` conditions. Also keep v1 Corollary 5.4/5.5 numbering separate from the unmapped 44-page EJP version.
