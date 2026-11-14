# gravner17 — Neighborhood growth dynamics on the Hamming plane

**Reading status:** `fulltext_read`; complete 55-page arXiv v1 / journal paper read, PDF pp. 1–55. The rectangle-to-plane equivalence and Theorem 1.2 were visually checked on PDF p. 4; Corollary 5.2 was checked on PDF p. 26. R03’s round-7 decision requested these corrections; this revised card is awaiting recheck.

**Reference:** Janko Gravner, David Sivakoff, and Erik Slivken, “Neighborhood Growth Dynamics on the Hamming Plane,” arXiv:1609.07202v1 (2016); *Electronic Journal of Combinatorics* 24(4) (2017), P4.29, DOI [10.37236/6400](https://doi.org/10.37236/6400). Local PDF SHA-256: `47db59ad443a71031066aa7b296bb7b2ca5fc66b33c9615e4e8babc4a97925c8`.

## Model and exact statements

The state space is the first quadrant of the two-dimensional Hamming graph. A finite zero-set (Z), a Young diagram of forbidden pairs, defines the update: an empty site is occupied when the pair consisting of the current counts on its entire horizontal and vertical lines lies outside (Z). For finite (Z), let (\gamma(Z)) be the smallest size of a finite seed that spans the plane. Theorem 1.1 proves

\[
|Z|/4\le\gamma(Z)\le|Z|,
\]

and Theorem 1.2 proves that a minimum seed can be found inside any rectangle (R_{a_0,b_0}\supseteq Z). The introduction on PDF p. 4 also states that, for every rectangle (R_{N,M}) containing (Z), if the initial occupied set is restricted to that rectangle, then it spans the whole plane (\mathbb Z_+^2) if and only if it internally spans (R_{N,M}). Thus the finite-to-infinite spanning interface is settled for this exact Hamming-plane rule and this finite-rectangle setup; it is not a blanket principle for other dynamics. Theorem 1.1 only gives the general lower bound (\gamma(Z)\ge |Z|/4); the authors explicitly say on p. 4 that they do not know whether the factor (1/4) can be improved.

For random initial subsets of (R_{N,M}) with density (p\downarrow0), take (\log N\sim-\alpha\log p) and (\log M\sim-\beta\log p). Define (I(\alpha,\beta,Z)=\lim_{p\to0}\log\mathbb P_p(\mathrm{Span})/\log p), when it exists. Theorem 1.3 proves existence and the variational formula

\[
I(\alpha,\beta,Z)=\inf_{A\text{ spans }Z}\rho(\alpha,\beta,A),\qquad
\rho(\alpha,\beta,A)=\max_{B\subseteq A}\bigl(|B|-\alpha|\pi_x(B)|-\beta|\pi_y(B)|\bigr),
\]

with the infimum attained by one finite family of spanning sets independent of α,β. Theorem 1.4 proves (\delta_n^2 I(\alpha,\beta,Z_n)\to I(\alpha,\beta,Z)), (\delta_n^2\gamma(Z_n)\to\gamma(Z)), and the analogous limit for the smallest thin spanning set when the rescaled square representations E-converge; finite-area limits give uniform convergence of (I) on ([0,1]^2). Corollary 5.2 (PDF p. 26) states that for fixed (\alpha,\beta\in[0,1]) and (\min\{a,b\}\to\infty),

\[
I(\alpha,\beta,R_{a,b})\sim\gamma(R_{a,b})(1-\max\{\alpha,\beta\}).
\]

Proposition 5.6 gives an explicit piecewise formula for the rate on the diagonal for threshold-bootstrap Young diagrams; for fixed (\alpha<1), its large-θ consequence is (I(\alpha,\alpha,T_\theta)=\frac{\theta^2}{4}(1-\alpha)+O(\theta)).

## Proof route and transfer boundary

The smallest-seed results reduce spanning sets to thin configurations and use Young-diagram decompositions. The rate proof combines pattern inclusion, a Janson-type overlap bound, and minimization of an energy-minus-projection-entropy functional. The continuum theorem uses E-convergence, compact truncation and matching discrete/continuous spanning comparisons; later sections prove corner bounds and use L-shaped examples to show that some proposed universal sharp bounds cannot hold.

This is a long-range Hamming-plane rule counting entire rows and columns, not nearest-neighbour bootstrap on ℚ². Its rectangle-to-plane criterion applies directly when the problem uses this rule and the initial set lies in a rectangle containing (Z). The paper does not prove the stronger general target (\gamma(Z)\ge |Z|/2): Theorem 1.1 gives only (|Z|/4), and the authors leave any improvement of that factor open.

**Section coverage:** [reading_coverage.json](../reading_coverage.json) (`/sources/gravner17`).
