# Method and problem map

## Six G07 interfaces

| Interface | Required proof object | Common invalid shortcut |
|---|---|---|
| G07.01 Epi/Gamma convergence | Correct topology and domains; liminf inequality; recovery sequence; equicoercivity/compactness for optimizer subsequences | “The objective converges pointwise, so minima converge.” |
| G07.02 UI / de la Vallée-Poussin | Uniform tail control for the changing family, with the correct signed part for a one-sided expectation bound | “Convergence in probability implies expectation convergence.” |
| G07.03 Tightness / Prokhorov | A named topology and tightness criterion; subsequences only unless uniqueness or full-sequence convergence is shown | “Tightness identifies the limiting law.” |
| G07.04 Minimax / qualification | Convex feasible sets, correct-side compactness, separate semicontinuity, and quasi-convexity/concavity; distinguish equality from attainment | “Probability laws are convex, so minimax applies.” |
| G07.05 Truncation / grid recovery | Both approximation directions, feasible recovery, and errors uniform over the parameter class | “A dense grid or truncation converges for each fixed model, hence uniformly.” |
| G07.06 Uniform errors / two limits | A joint or uniform error modulus covering the exact external-parameter range | “Take the pointwise limit twice in either order.” |

Direct source status: Rockafellar–Wets Proposition 7.2 and Theorems 7.31/7.33 are accepted for finite-dimensional deterministic sequential epi-convergence and minimizer/value transfer under compact capture or eventual level-boundedness; no stochastic integral convergence or infinite-dimensional compactness is supplied. Pennanen–Koivu Theorems 7–9 are accepted for stochastic expected-objective epi-convergence under weakly converging laws, with the exact liminf and recovery premises documented in the use card; this does not supply equicoercivity or a generic changing-domain Γ theorem. Keehan–Royset Lemma 3.1 and Theorems 3.3/4.2 are accepted for finite/infinite-horizon Bellman epi-consistency under explicit invariant-integrability, fixed compact-action, joint epi/pointwise, tail and equi-semicontinuity conditions; policy convergence and actual-control existence remain separate. Its §5.1 and Proposition 5.3 application branches remain excluded pending neutral review. R03 accepted the PGEL-045 use of PR-6410649e9c2b, Theorem 3.3, only for fixed real Dirichlet data on the Sierpinski gasket; its separate R06-derived Theorem 3.4 completion is restricted to the source's harmonic-spline/energy-orthogonality setting. This does not fill the general G07.01 source gap. G07.02 uses PR-be2810b8a348, PR-6f06351ec4ce, and Leskelä–Vihola have been accepted for their separate weak-law Fatou, TV-specific UI, and nonnegative-family stop-loss/UI scopes. The dVP proof is explicitly derived because Leskelä–Vihola Remark 4 cites an external source. Artstein–Wets Theorem 2.3 is accepted for fixed-law iid epi-SLLN under the source’s local common integrable-minorant premise, and Theorem 3.3 for one fixed finite-cost population `ε`-minimizer on compact `X`; no global-minimum comparison on noncompact `X` is claimed, and the held Theorem 4.3/Proposition 4.4 branch is excluded. Leclère Theorem 3 is accepted only for conditional-expectation relaxation of almost-sure equality constraints on a fixed probability space under Kudo convergence, actual strong-`L^p` continuity, and the source-space assumptions; Corollary 4 requires a given convergent subsequence of vanishing-error approximate minimizers. Sur–Birge is accepted only through the derived compact-domain positive-Harris specialization with a deterministic common Lipschitz bound and one `L¹(π)` reference section; its broad random-LSC and rate/CLT branches remain excluded. Shapiro (1991) is accepted as use #29 for Theorems 3.1–3.2 `C(S)` optimal-value delta method: the full supremum-norm process weak limit is a premise, not a pointwise-CLT consequence. Hess–Seri is accepted as use #30 for a derived recovery route that strengthens upper convergence to a countable target-epi-dense test set (or all fixed decisions) and requires supplied vanishing-error minimizers with relative compactness in Θ for optimizer transfer; the printed arbitrary-dense recovery and true-objective-value equalities remain held. The list records exact scopes; it does not certify all candidate routes.

## Problem routes

“Core” and “conditional” reflect the assignment map; an interface is not a claim that the whole archived problem is solved.

| Problem | Route and boundary |
|---|---|
| A001 | Core: finite-horizon IID prophet ratio. A finite minimax exchange does not establish the `k>1` all-horizon identity or uniformity over laws changing with `n`. |
| A002 | Conditional: static threshold prophet secretary. Preserve random order, ties, and stockout calibration; the target `k>1` calibration remains open. |
| A005 | Conditional: ex-ante LP benchmark for stochastic knapsack. Duality certifies the finite benchmark, not the online ratio gap. |
| A007 | Core: general-renewal polling. Prove renewal-age/residual tightness and uniform cycle bounds before exchanging stationarity and large switch-over limits. |
| A025 | Conditional boundary only: weak convergence or distinct marginals do not imply singularity; require a measurable separating event. |
| A030 | Core: directed Bernoulli flow. Need a joint finite-size / `p↑1` error estimate with boundary control; a continuum constant alone is not enough. |
| A122 | Core: nonlinear law-map fixed points. Compactness gives subsequences; also prove continuity and preservation/closedness of the target class. |
| A124 | Core: Poisson growing-ball cover time. Attainment and uniformity over all minimizing seed laws are part of the required interface. |
| A127 | Core: critical Beta tree pair heights. Need joint convergence and UI of products under the specified cyclic order; marginal CLTs do not determine the covariance. |
| A136 | Core: SIRSN route maxima. Finite mean route-by-route does not control the countable supremum; require an integrated tail estimate or a counterexample in the shared realization. |
| A137 | Conditional: binomial-to-Poisson SIRSN length. Need scaling, de-Poissonization, and UI of total length. |
| A185 | Conditional boundary only: grid-width and system-size limits require a joint estimate. |
| A190 | Conditional boundary only: replacing `n` by `Cn` does not preserve same-`n` asymptotics without regular growth. |
| A202 | Conditional: preserve the stated order of degree, scale, and parameter limits; verify all error bounds on the claimed range. |

## Theorem selection checklist

1. Write the exact target inequality/equality, including sign and quantifiers.
2. Check whether the source controls values, expectations, optimizer subsequences, optimizer laws, or only a finite optimization.
3. Match source topology, domain, probability law, moments, tail assumptions, and parameter quantifiers.
4. Prove missing hypotheses separately; label derived repairs and model-specific estimates as derived.
5. State which conclusion remains unavailable when only a one-sided theorem applies.
