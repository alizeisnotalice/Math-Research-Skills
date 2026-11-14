# LIN2017HARMONIC — harmonic measure for biased walk on a supercritical GW tree

**Source:** Shen Lin, “Harmonic measure for biased random walk in a supercritical Galton–Watson tree,” arXiv:1707.01811v4 (14 January 2019; manuscript date 27 March 2022). Read the full 18-page PDF, SHA-256 `85e80f14cbe4572a84b8c272590185ef5c8d4e2dc4e4001b9751992c876501af`.

## Model and bias convention

The offspring law ((p_k)_{k\ge1}) is nondegenerate, leafless ((p_0=0)), and has finite mean (m>1). For a vertex (x\ne\varnothing) with ν(x) children, the λ-biased walk moves to its parent with probability λ/(ν(x)+λ) and to each child with probability (1/(ν(x)+λ)). Thus λ=1 is simple random walk, λ=0 is forward-only, and transience holds exactly when (0\le\lambda<m). The harmonic ray is the loop-erasure of the transient walk; the boundary metric is (d(\xi,\eta)=\exp(-|\xi\wedge\eta|)).

## Dimension theorem

Theorem 1 (PDF pp. 2–3): for (0<\lambda<m), the almost-sure Hausdorff dimension (d_\lambda) of the λ-harmonic measure satisfies

\[
d_\lambda>\mathbb E_{GW}[\log\nu],\qquad
\lim_{\lambda\downarrow0}d_\lambda=\mathbb E_{GW}[\log\nu],\qquad
\lim_{\lambda\uparrow m}d_\lambda=\log m.
\]

The reference λ=0 is the visibility measure. The strict comparison is a dimension statement on this fixed visual boundary metric; it is not equivalence or singularity of harmonic measures on different trees or metrics.

## Proof dependency chain

The proof introduces the escape probability β(T) and effective conductance (C(T)=\lambda\beta(T)/(1-\beta(T))), then constructs the stationary law for the environment seen from the biased walk (Sections 2–3, PDF pp. 4–9). Section 4 (pp. 9–11) constructs a harmonic-flow-stationary law with explicit Radon–Nikodym density relative to GW. The entropy/dimension formula (Eq. (8), pp. 11–12) expresses (d_\lambda) under that stationary law. FKG gives the strict lower bound against λ=0; dominated convergence in the conductance/escape-probability representation yields both endpoint limits (Section 5, pp. 12–14). Section 6 (pp. 14–17) proves Theorem 2’s path-degree comparisons using the stationary laws, FKG, and strong laws.

Theorem 2 (PDF pp. 3–4) also states that the harmonic ray’s average offspring lies strictly above (m) and strictly below (m^{-1}\sum_k k^2p_k); the latter bound is only informative when the second moment is finite. The walk-path average offspring is below (m) for (0<\lambda<1), equals (m) at λ=0 or 1, and exceeds (m) for (1<\lambda<m). For (0<\lambda\le1), the harmonic-ray average exceeds the walk-path average. The paper explicitly notes that the walk-path statistic is not monotone in λ, and leaves monotonicity of (d_\lambda) and the harmonic-ray statistic as open questions.

## Reading coverage

Complete PDF read: model, conventions, main theorems, §1 (PDF pp. 1–4); escape probability/effective conductance, §2 (pp. 4–5); walk-environment stationary law, §3 (pp. 5–9); harmonic stationary measure, §4 (pp. 9–11); dimension formula and endpoint limits, §5 (pp. 11–14); path offspring averages, §6 (pp. 14–17); references (p. 18). Physical PDF pages are used.

## Scope boundary

Theorem 1 is not a monotonicity theorem. A numerical or path-degree comparison does not prove monotonicity of harmonic-measure dimension. Keep the toward-root convention and leafless finite-mean assumptions explicit when comparing it with other biased-walk papers.
