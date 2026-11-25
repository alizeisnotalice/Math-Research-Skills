# Positive example: an induced harmonic-stationary tree law

Let the base system be simple random walk on an augmented supercritical Galton–Watson tree with nonconstant offspring, `p₀=0`, and `1<m<∞`. Its last-exit set `Exit` has positive measure. Inducing on that set gives the harmonic child-subtree transition rule, and conditioning the finite base measure on `Exit` normalizes an invariant probability for the induced chain. LPP95 Proposition 5.2 applies after verifying that each first-child harmonic weight is positive GW-a.s.; in this branching model, each descendant subtree is transient a.s., and countability gives simultaneous transience of all descendant subtrees. Theorem 8.1 then gives the induced HARM law, and the tower remark transfers ergodicity to the full path shift.

Keep the conclusions separate: Theorem 3.1 establishes stationarity and reversibility of the AGW rerooting chain; Theorem 8.1 plus the tower remark establish the later ergodic conclusion. The induced law is a normalized probability. Any scalar multiple remains stationary, so uniqueness is understood among normalized absolutely continuous stationary probabilities. See the exact page-bound card at `../references/cards/LPP1995ERGODIC.md` and the LPP95 use card in the L11 reader package.

## Other source-matched positive routes

### A generator/core route

Suppose a non-explosive PDMP on the source's smooth state manifold satisfies A2–A3 and the uniform smooth-compact approximation bound, including a finite displacement envelope on each bounded time interval, uniform over all initial states. If a finite measure has `∫λ dμ<∞` and annihilates the extended generator on every `C_c^1` function, DGM Theorem 21 and Corollary 22 provide a `C₀` Feller semigroup, a `C_c^1` strong-generator core, and invariance. The core bridge is the step that turns balance into invariance. It does not cover a different active boundary automatically; see the DGM card（本机附件：`references/cards/DGM2021PDMPINVARIANCE.md`）.

### An embedded Palm law

If a stationary PDMP probability already exists and its total interior-plus-boundary jump flux has finite positive mass `0<c<∞`, Löpker–Palmowski normalize the source's flux measure to obtain a stationary pre/post-jump probability. This is a valid embedded-law construction because both the stationary base and the finite normalizer are in hand. Reversal needs additional assumptions, and the argument does not create the continuous-time invariant law; see the time-reversal card（本机附件：`references/cards/LOEPKER2013TIMEREVERSALPDMP.md`）.

### A source-specific infinite-volume path

For the homogeneous two-sided space-time PPP model with `λ>0`, `d≥2`, and the paper's radius-one replacement/coalescence updates on locally finite configurations, exact bounded-window update/restriction commutation plus finite random influence yields Ferrari–Landim–Thorisson's stationary path construction. This is a positive G20.05 example only for that model; it does not prove the generic coordinate-prefix gate in the method contract. See the FLT card（本机附件：`references/cards/FERRARI_LANDIM_THORISSON2004_POISSON_TREES.md`）.

### A direct transform for one CIR model

For an already constructed conservative scalar CIR `dX=a(b−X)dt+σ√X dB`, `a,b,σ>0`, the bounded affine transition martingale identifies the invariant probability `Γ(2ab/σ², σ²/(2a))`. The separate calculation in R11's derivation（本机附件：`evidence/math/review_support/R11/continuation_v2/wave07_v2/CIR_safe_derivation.md`） proves the actual semigroup invariance; the source's general polynomial-characteristic converse is not used. This example does not propose an A17 law.
