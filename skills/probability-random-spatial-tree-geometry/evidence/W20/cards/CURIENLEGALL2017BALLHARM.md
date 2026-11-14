# CURIENLEGALL2017BALLHARM — harmonic measure of balls in random trees

**Source:** Nicolas Curien and Jean-François Le Gall, “The Harmonic Measure of Balls in Random Trees,” *The Annals of Probability* 45(1) (2017), 147–209, DOI 10.1214/15-AOP1050; arXiv:1304.7190v4. All 66 physical PDF pages were read (SHA-256 `d344a60969603d29698e64f5615e65699241c1e639e686d67479bf4284c2db8c`). Theorem 1, Theorem 3, and the conductance recursion were checked on rendered physical pp. 3, 6, and 7–8.

## Discrete and continuous models

For the discrete result, the offspring law is critical with mean 1 and finite variance (\sigma^2>0). The tree is conditioned to survive to generation (n), and simple random walk starts at the root; (\mu_n) is its first-hit distribution on generation (n). Theorem 1 states that there is a universal (\beta\in(0,1)), independent of the offspring law, such that for every δ>0,
\[
\mu_n\{v:n^{-\beta-\delta}\le\mu_n(v)\le n^{-\beta+\delta}\}\xrightarrow[n\to\infty]{\mathbb P}1.
\]
Thus, with high tree probability, most harmonic mass is supported by about (n^\beta) vertices rather than the order-(n) generation size. Corollary 2 gives the analogous statement for a size-conditioned GW tree when (n,N\to\infty), on the event generation (n) is nonempty; if (n=o(\sqrt N)), that event has probability tending to one.

The continuous model is the reduced critical GW tree limit (\Delta), equipped with Brownian motion stopped when it first reaches its height-one boundary. Theorem 3 gives, (\mathbb P)-almost surely and for (\mu)-almost every (x),
\[
\lim_{r\downarrow0}\frac{\log\mu(B_d(x,r))}{\log r}=\beta,
\]
so the harmonic measure has Hausdorff dimension β, whereas the boundary itself has dimension 1. The displayed numerical estimate β≈0.78 is an approximation, not a closed-form value. Proposition 4 characterizes β through the law of the random conductance (C), whose exact recursive distributional equation is visually confirmed on p. 7:
\[
C\overset d=\left(U+\frac{1-U}{C_1+C_2}\right)^{-1},
\]
where (U\sim\mathrm{Uniform}[0,1]) and (C_1,C_2) are iid copies of (C), independent of (U). Do not drop the reciprocal.

## Proof dependencies

The continuous proof prunes the tree to the subtree reaching level one and maps it logarithmically to a Yule tree. Under this map, Brownian motion becomes a time-changed Brownian motion with drift (1/2); the selected ray defines a measure on the Yule boundary. The law of the subtree above a level selected by the walk converges to a limiting law. A spine decomposition and conductance convergence yield an invariant, ergodic measure for shifts along the selected ray; Birkhoff's theorem applied to the log-mass cocycle proves exact dimension (Theorem 3).

For the discrete theorem, the proof first couples reduced discrete GW trees to (\Delta), then proves conductance and finite-level harmonic-measure convergence. Entropy/flow identities and cut-conductance estimates control the mass outside the (n^{-\beta\pm\delta}) window; dyadic scale summation closes the probability estimate. The fixed-size corollary uses conditioned-tree convergence and a separate survival/height comparison. The authors emphasize that Theorem 1 does not follow directly from Theorem 3; the discrete estimates are additional work.

## Model boundary for W20

This source concerns simple random walk on finite-radius balls of **critical** GW trees and the Brownian exit measure on their continuum reduced-tree limit. It is not the boundary harmonic measure for a transient biased walk on an infinite supercritical GW tree, and it is not a theorem about monotonicity in a bias parameter. It is a useful comparator for dimension mechanisms, not a direct substitute for the LPP/Lin/Rousselin setting.

## Complete-paper coverage

| Physical PDF pages | Content read and proof mechanism |
|---|---|
| 1–8 | Introduction, discrete and continuous models, Theorems 1–3, conductance recursion, Proposition 4. |
| 9–19 | Reduced-tree/Yule construction, Brownian motion, continuous conductance and harmonic-measure flow rule. |
| 20–37 | Spine decomposition, conductance limit, invariant measure and ergodic proof of the continuous exact-dimension theorem. |
| 38–47 | Discrete GW conventions; reduced-tree convergence; conductance and harmonic-measure convergence. |
| 48–55 | Main discrete theorem: flow/entropy lemmas, cut-conductance bounds, and dyadic-scale estimates. |
| 56–58 | Fixed-size GW tree corollary and conditioning estimates. |
| 59–62 | Alternative continuous proof and comparison with supercritical GW trees. |
| 63–65 | Appendix proof for the spine/conductance ingredients. |
| 66 | References. |

The visual checks show Theorem 1 on physical p. 3, Theorem 3 on p. 6, the continuous recursion introduction on p. 7, and the full reciprocal equation and β formula in Proposition 4 on p. 8.
