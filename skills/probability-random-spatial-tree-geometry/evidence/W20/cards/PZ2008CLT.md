# PZ2008CLT — a CLT for biased walks on Galton–Watson trees

**Source:** Yuval Peres and Ofer Zeitouni, “A Central Limit Theorem for Biased Random Walks on Galton–Watson Trees,” *Probability Theory and Related Fields* 140(3–4) (2008), 595–629, DOI 10.1007/s00440-007-0077-y; local text is arXiv:math/0606625v1 (24 June 2006). All 34 physical PDF pages were read (SHA-256 `c0124603b6bb062171f27c9c5cd74e6bbafe63a6ddbb8c77bf826b353a7b4d5c`). The bias convention and Theorems 1–2, corrector, and invariant-root law were checked on rendered physical pp. 2, 4–5, and 8.

## Model and theorem statements

The rooted Galton–Watson tree has offspring law ((p_k)_{k\ge1}) with **no leaves**, mean (m>1), and the paper's exponential-moment assumption. At a vertex with (d_v) children, the walk assigns weight λ to the parent and weight 1 to each child:
\[
P_T(X_{n+1}=v^*\mid X_n=v)=\frac{\lambda}{\lambda+d_v},\qquad
P_T(X_{n+1}=w\mid X_n=v)=\frac1{\lambda+d_v}
\]
for each child (w). Thus λ biases **toward the root**. Theorem 1 (λ=m) says that, for almost every GW tree, (|X_{\lfloor nt\rfloor}|/\sqrt{\sigma^2n}) converges in law to (|B_t|), a reflected/absolute standard Brownian motion, for a deterministic σ²>0. Theorem 2 is the corresponding quenched invariance principle for the horocycle coordinate (h(X_{\lfloor nt\rfloor})) under the **IGW marked-ray law**, with Brownian (not reflected) limit. Theorem 3 treats λ<m: under the same no-leaves and exponential-moment setting, there is a deterministic positive speed (v) and a quenched centered CLT for ((|X_{\lfloor nt\rfloor}|-vnt)/\sqrt{\sigma^2 n}). For λ>m the walk is positive recurrent, so these CLTs do not apply.

## Critical proof chain

On the auxiliary tree with an infinite marked ray, IGW size-biases offspring along the ray and designates one child as the continuation. The generation martingale is \(W_v=\lim_n Z_n(v)/m^n\). The martingale \(M_t\) has increments \(+W_{X_{t+1}}\) for an upward horocycle step and \(-W_{X_t}\) for a downward step. The root change from IGW to IGWR is not an unspecified size bias: the paper states the exact Radon–Nikodym derivative \[\frac{d\mathrm{IGWR}}{d\mathrm{IGW}}(\mathcal T,o,\mathrm{Ray})=\frac{m+d_o}{2d_o}.\] In the offspring-count coordinate of the displayed root laws, \(P_{\rm IGW}(d_o=k)=kp_k/m\) and \(P_{\rm IGWR}(d_o=k)=(m+k)p_k/(2m)\). The factor \(2d_o\) is essential: it makes the density normalized under IGW. Under IGWR the environment viewed from the particle is stationary and reversible (Lemma 2); the proof checks detailed balance on finite cylinder events using the critical transition probabilities \(1/(m+d_u)\) and \(m/(m+d_v)\). This gives the quadratic-variation limit for \(M_t\).

The additive horocycle coordinate is compared with the martingale by the corrector (Z=M/\eta-h(X)), where η is the second-moment normalization of the population martingale. Proposition 1 controls the corrector after smoothing over a time window; ergodicity gives the bracket limit, and the martingale invariance principle yields Theorem 2. A coupling from the ordinary GW-rooted tree to the marked-ray construction then yields Theorem 1. For λ<m, stationary regeneration blocks on the no-leaves tree give the annealed CLT, and the paper's path-decorrelation argument upgrades it to the quenched result.

## Transfer boundary

These are walk-position CLTs, not harmonic-measure dimension or dimension-monotonicity results. The critical theorem uses a marked-ray size-biased environment and the radial coordinate at λ=m; the transient theorem uses regeneration and exponential moments. Neither result transfers as stated to GW trees with leaves or to biased walks on Cayley graphs with dead ends. The bias parameter is the parent weight here, so it must be inverted/translated before comparison with away-root conventions.

## Complete-paper coverage

| Physical PDF pages | Content read and proof mechanism |
|---|---|
| 1–2 | Abstract, rooted GW model, transition convention, phase regimes, Theorem 1. |
| 2–4 | IGW marked-ray construction, horocycle coordinate, Theorem 2 and martingale roadmap. |
| 4–7 | Martingale construction, IGWR stationarity/reversibility, corrector statement, and proof roadmap. |
| 8–12 | Corrector estimates and smoothing-time bounds proving Proposition 1. |
| 13–18 | Auxiliary identities, offspring/population-martingale estimates, and bracket computation for (4). |
| 19–26 | Coupling from IGW to GW and proof of Theorem 1. |
| 27–32 | Regeneration-block proof for the transient λ<m case and Theorem 3. |
| 33–34 | Acknowledgments and references. |

Render checks at physical pp. 3, 6, and 8 verify the marked-ray offspring construction, exact root laws and density, and detailed-balance calculation. Physical pp. 2 and 4–5 verify the parent-weight convention, marked-ray horocycle theorem, and martingale/corrector.
