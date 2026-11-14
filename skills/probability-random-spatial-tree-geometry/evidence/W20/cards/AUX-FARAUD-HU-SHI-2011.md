# AUX-FARAUD-HU-SHI-2011 — Critical stochastically biased walks and logarithmic-cubed displacement

**Authors/version:** Gabriel Faraud, Yueyun Hu, Zhan Shi; complete arXiv:1003.5505v5 author manuscript, 13 May 2011, physical PDF pp. 1–40. SHA-256 fdcb44ed6f217b7a2af1290089384ef46f83b5085461c079911cb9a7f8b37a8d. D05 identity/extent checked; W20 read the full text. Review pending.

## Model and theorem scope

The underlying tree is supercritical GW with random offspring N; each non-root vertex has an i.i.d. random vector of child-to-parent transition ratios A(x)=(A_i(x))_{i≤N(x)}, independent across vertices. Given the environment, the walk uses those ratios to choose children versus its parent. The environment is therefore random at each vertex and the walk is a RWRE; it is not the deterministic scalar λ-biased walk. Set ψ(t)=log E[Σ_{i=1}^N A_i^t]. The standing assumptions are ψ(0)>0, ψ(t)<∞ for every t in some interval (-δ,1+δ), and E[N^(1+δ)]<∞.

Let M_n=max_{0≤k≤n}|X_k|. The Lyons–Pemantle criterion quoted as Theorem A says recurrence if inf_{t∈[0,1]}ψ(t)≤0 and transience if that infimum is positive. This article studies the critical recurrent boundary inf ψ=0.

**Theorem 1.1 (physical p. 4).** If ψ(1)=ψ′(1)=0, then on non-extinction, M_n/(log n)^3→4/α almost surely, where α=(3π²/2)E[Σ_i A_i(log A_i)^2].

**Theorem 1.2 (physical p. 5; rendered).** If inf_{t∈[0,1]}ψ(t)=0 and ψ′(1)>0, let θ∈(0,1) solve ψ′(θ)=0. Then on non-extinction, M_n/(log n)^3→1/α_θ almost surely, with α_θ=(3π²/(2θ))E[Σ_i A_i^θ(log A_i)^2]. The different constants in the critical and noncritical branches are part of the statements. Neither is a harmonic-measure dimension result.

**Theorem 1.4 (statement on physical p. 7; proof through pp. 7–15).** For the associated branching-random-walk potential, if inf_{[0,1]}ψ=0 and ψ′(1)≥0 (equivalently, under ψ(t)=log E[Σe^(−tV)] and ψ(1)=0, E[Σ_{|x|=1}V(x)e^(−V(x))]≤0), the minimum of the ancestral maximum potential V̄(x)=max_{z on the root-to-x path}V(z) over |x|=n has order n^(1/3): n^(−1/3)min_{|x|=n}V̄(x)→(3π²σ²_θ/2)^(1/3) a.s. on non-extinction, where θ solves E[Σ_{|x|=1}V(x)e^(−θV(x))]=0 and σ²_θ=(1/θ)E[Σ_{|x|=1}V(x)^2e^(−θV(x))]. This is the potential estimate feeding the walk-displacement proof.

## Proof dependencies

The many-to-one identity (2.1) changes the branching-random-walk sum to a one-dimensional random walk S. A triangular Mogulskii small-deviation estimate gives the n^(1/3) exponent for S constrained to a corridor; the corresponding branching-random-walk minimum is proved by first/second-moment bounds, a Paley–Zygmund lower bound, and Borel–Cantelli. The one-dimensional potential representation bounds the probability ρ_n of hitting generation n before returning to the root in terms of the minimum along root-to-level-n paths; a deterministic escape-probability lemma then converts the exponential scale of ρ_n into the (log n)^3 scale of M_n.

For ψ′(1)>0, the proof tilts the potential by θ, obtains matching upper and lower scales for ρ_n using the reflected-walk corridor estimate of Proposition 3.1, then invokes the escape-probability lemma. In the critical case ψ′(1)=0, the upper bound uses a first-moment barrier estimate; the lower bound uses the size-biased branching random walk with an infinite distinguished spine, the conditional independence of side branches, a deterministic recursive lower bound on escape probabilities, and a uniform small-deviation estimate for the reflected walk. The entire proof is in Sections 2–6; Section 3 distinguishes δ=0 from δ>0, which changes the exponent constant.

## Applicability boundary

The theorem is about the maximum depth reached by one RWRE trajectory during its first n steps, on a critical recurrent environment regime. The random endpoint maximum A136 and the harmonic-measure dimension B076 are different variables and different questions. Do not identify M_n with a maximum over sampled routes, or the potential exponent with a boundary-measure dimension.

**Coverage:** physical pp. 1–40 read, including appendix and references. Rendered theorem check: p. 5 Theorem 1.2 and potential definition; section coverage is in evidence/W20/reading_coverage.json.
