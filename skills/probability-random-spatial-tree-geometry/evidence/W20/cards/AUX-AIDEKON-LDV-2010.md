# AUX-AIDEKON-LDV-2010 — Hitting-time large deviations for transient GW-tree RWRE

**Author/citation:** Elie Aïdékon, *Annales de l’Institut Henri Poincaré, Probabilités et Statistiques* 46(1), 159–189 (2010), DOI 10.1214/09-AIHP204. **Read source:** complete Numdam/publisher article, physical PDF pp. 1–31, printed pp. 159–189. SHA-256 041931fd686d7666191c611f21114c509841552532218363d98e5b657c4018f2. W20 read all pages; review pending.

## Model and exact claims

The offspring law has q0=0, finite mean m>1, and minimum supported degree ν_min≥1. Independent positive environment variables A(x) mark non-root vertices; the child transition weight is A(child) and the parent weight is 1, so from x the parent probability is 1/(1+Σ_child A(child)), and child i probability is A(x_i)/(1+Σ_child A(child)). Assume ellipticity 0<i:=ess inf A≤s:=ess sup A<∞. Under the base annealed law Q^e the walk starts at the root e in the augmented tree, whose added parent is denoted by ē. Let `D(e)=inf{k≥1:X_{k−1}=e, X_k=ē}` be the first crossing from the root to that added parent. The conditioned law `S^e=Q^e(·|D(e)=∞)` forbids this crossing; it still allows the walk to leave and later return to the root. Let τ_n be the first hitting time of generation n. Define Λ=Leb{t∈R:E[A^t]≤1/q1}; if q1=0, the paper sets Λ=∞.

The statements use both transience, inf_{t∈[0,1]}E[A^t]>1/m, and positive speed, Λ>1. Let v be the speed.

- **Theorem 1.1 (printed pp. 160–161; physical pp. 2–3):** for 1≤b≤1/v, the annealed and quenched speed-up rate functions I_a≤I_q are continuous, convex and strictly decreasing, vanish at 1/v, and for a<b≤1/v the log probabilities of τ_n/n∈(a,b] divided by n converge to −I_a(b) and −I_q(b), respectively (quenched a.s.).
- **Theorem 1.2 (printed p. 161; physical p. 3):** for 1/v≤a<b, the slowdown log rates for τ_n/n∈[a,b) are −I_a(a) and −I_q(a). Both functions are continuous, convex and zero at 1/v. They are strictly increasing on [1/v,∞) if i>ν_min^(−1); if i≤ν_min^(−1), they are both zero on that interval.
- **Proposition 1.3 (physical p. 3; rendered):** with ψ(θ)=log E_Q[Σ_{i=1}^{ν(e)}ω(e,e_i)^θ], I_a(1)=−ψ(1) and I_q(1)=−inf_{θ∈(0,1]}ψ(θ)/θ. They agree iff ψ′(1)≤ψ(1); otherwise I_a(1)<I_q(1). Thus annealed and quenched rates need not match even in elliptic environments.
- **Theorem 1.4 (physical pp. 3–4):** in the low-minimum regime i<ν_min^(−1), if q1=0 or s<1, the conditioned slowdown probability has stretched-exponential bounds e^(−n^d1)<S^e(τ_n>an)<e^(−n^d2), 0<d2<d1<1. If q1>0 and s>1 (equivalently Λ<∞ here), then for a>1/v, log S^e(τ_n>an)/log n→1−Λ. The theorem explicitly excludes the critical i=ν_min^(−1) case.

## Proof architecture

The paper defines a regeneration time Γ1 at a first hit of a generation by a vertex with at least two children that is never crossed back over its parent. Under S^e, regeneration heights have exponential moments; consecutive time/height increments are iid and v=E_S|X_Γ1|/E_SΓ1. For i>ν_min^(−1), coupling the radial walk to a biased walk on Z gives an exponential moment for Γ1. In the low-minimum regimes, pipe-like stretches and one-dimensional gambler’s-ruin estimates give stretched tails. For Λ<∞, the proof uses 1D RWRE potential maxima, a trap decomposition with bounded-generation subtrees, and estimates for return probabilities to derive the polynomial regeneration tail exponent Λ.

The speed-up proof builds the branching set of vertices with favorable quenched hitting probabilities; its mean growth rate is asymptotically supermultiplicative, and a Seneta–Heyde argument gives the quenched rate. The slowdown proof uses a corresponding slow-hitting branching set; when i≤ν_min^(−1), an n-good tree event forces zero exponential rate. Proposition 3.3 transfers the conditioning that forbids crossing the added root-parent edge back to the original laws.

## W20 boundary

This article is a random-environment walk, not the deterministic scalar-biased walk whose boundary harmonic measure appears in B076. It supplies precise separation of annealed/quenched rate functions and trap regimes, but no harmonic-measure dimension or route-network maximum theorem. It can be used as a model comparator for C139 only; no Galton–Watson-to-Cayley-graph transfer is proved.

**Coverage:** complete physical PDF pp. 1–31 / printed pp. 159–189 read. Rendered checks: physical p. 3, Theorems 1.2 and Proposition 1.3; physical p. 4, regeneration definition and Proposition 2.1. Detailed coverage is in evidence/W20/reading_coverage.json.
