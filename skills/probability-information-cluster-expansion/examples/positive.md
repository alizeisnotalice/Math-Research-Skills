# Positive example: keep the claim at the proved order

## B051 prompt

“Kanoria–Montanari give the coefficients through `d²`. Can we say the deletion-channel capacity series converges because the numerically evaluated coefficients stabilize?”

## Good response pattern

First state the proved result with the log base and remainder: `C(d)=1+d log₂(d)−A₁d+A₂d²+O(d^(3−ε))` for every fixed `ε>0`. This proves the stated asymptotic through `d²`. Section 6 asks for higher orders and convergence; it does not answer either. The finite Decimal cutoff check only verifies arithmetic for displayed coefficient sums. To claim an `A₃` term, prove a sharper remainder and identify the normalized residual; to claim convergence, prove a nonzero radius and equality to capacity, with uniform control of the input optimization and information-rate limit.

## A007 prompt

“Poisson arrivals have a uniform scaled waiting-time limit at large switch-over times. Does the same formula hold for general renewal arrivals?”

## Good response pattern

The source proves the Poisson benchmark but labels the general-renewal statement Conjecture 4.2 and asks for a rigorous proof. At polling epochs, general renewal arrivals retain age/residual-life information. Formulate the age-augmented state and prove the steady-state/fluid scaling and tightness before transferring a waiting-time law. Do not present the conjectured extension as established.

## Finite truncation prompt

“Can I truncate the positive sum in Drinea–Mitzenmacher Theorem 3 to certify a capacity lower bound?”

Check which paper and functional the proposed truncation concerns. I05 Eq. (16) uses `log[binom(r+z,k)−binom(r,k)]` and the nested sum `Σ_k Σ_(i,z,r,s) Σ_(t∈F(i,z,r,s)) Pr[T=t,K=k](…)`. Its Proposition 1 controls typical-output block-count deviations; it does not supply an entropy-tail correction. I14 Proposition 1 is a separate statement for truncating the I14 Drinea–Mitzenmacher functional and includes the retained-mass term `(1−ε)log(1−ε)`. Do not cite either proposition as a truncation rule for the other paper’s expression.


## Use cluster criteria only in their source models

A finite-event LLL claim may use Scott–Sokal C05 only after checking the exact dependency graph and conditional event-probability hypothesis; its sharp nonvanishing result is not a deletion-channel theorem. Abstract polymer criterion C12 and measurable pair-potential criterion C15 also require their source-specific activity, stability, and integrability assumptions. A channel application still needs a proved representation and uniform bounds.

For A007, W14-004/R13 may be cited only as an auxiliary counterexample to moment-only stability reasoning in a two-queue adaptive model. It does not imply a large-switch-over or general-renewal waiting-time limit.


For the Poisson-arrival A007 comparator, first verify Resing's per-customer independent iid replacement Property 1 (exhaustive/gated policies are examples). With positive switchovers, use the multitype branching process with immigration in every state (Theorem 3, report PDF p. 9); with zero switchovers use the distinct state-zero immigration representation (Theorem 4, pp. 11–12). A stationary PGF additionally needs the primitive subcritical offspring matrix, embedded-chain irreducibility/aperiodicity, and stated immigration log moment. This is not a general-renewal limit.
