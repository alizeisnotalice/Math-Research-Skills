# BAFGH2012LEAVES — biased walks on Galton–Watson trees with leaves

**Source:** Gérard Ben Arous, Alexander Fribergh, Nina Gantert, and Alan Hammond, “Biased Random Walks on Galton–Watson Trees with Leaves,” *The Annals of Probability* 40(1) (2012), 280–338, DOI 10.1214/10-AOP620; arXiv:0711.3686v4 (17 November 2010). All 49 physical PDF pages were read (SHA-256 `28d6baaf27bffde3e7ed8bfce67f2dd28a207ac821d348b913aeb3611ed0b96b`). The model, limit law, trap reduction, and final limit proof were checked on rendered physical pp. 2–3, 12, and 41.

## Model and results

Let the supercritical Galton–Watson offspring law have (p_0>0), finite second moment, extinction probability (q), and generating function (f). The walk is biased **away from the root**: at a vertex with (k) children, it moves to the parent with probability (1/(1+\beta k)) and to each child with probability (\beta/(1+\beta k)). The reversible conductance of an edge from level (|x|-1) to (|x|) is proportional to (\beta^{|x|-1}). Put
\[
\beta_c=1/f'(q),\qquad \gamma=-\frac{\log f'(q)}{\log\beta}\in(0,1).
\]
Under (\beta>\beta_c), Theorem 1.1 gives tightness of the normalized hitting times (\Delta_n/n^{1/\gamma}) and heights (|X_n|/n^\gamma), and the almost-sure logarithmic exponent (\log|X_n|/\log n\to\gamma). Theorem 1.2 proves failure of full-sequence distributional convergence for sufficiently large β (the authors conjecture this throughout the sub-ballistic regime). Theorem 1.3 gives infinitely divisible subsequential limits along (n_\lambda(k)=\lfloor\lambda f'(q)^{-k}\rfloor). Theorem 1.4 describes the Lévy spectral function, moment range, absolute continuity, and the trap-excursion variable (Z_\infty); in particular the limiting law has moments of order α exactly for α<γ.

## Proof dependencies

The environment is split into the infinite backbone and independent finite traps. Under the subcritical trap law \(Q\), the height tail is \(Q(H\ge n)\sim\alpha f'(q)^n\), and \(E_Q Z_i=f'(q)^i\) for the generation size \(Z_i\). This does **not** give a finite mean for the Q-trap's raw root-relative conductance mass: conductance weights at generation i have scale \(\beta^i\), while \(E_Q Z_i=f'(q)^i\), so the expected generation sum is \(\sum_i(\beta f'(q))^i=\infty\) when \(\beta f'(q)>1\). This divergence is a direct calculation from the trap law and conductance levels; it is not the bottom-relative return-time variable below. The finite quantity used by the limit theorem is instead the bottom-relative return-time variable \[S_\infty=2\sum_{i\ge0}\beta^{-i}(1+\Lambda_i),\] where \(\Lambda_i\) is the invariant weight of the subtraps attached to the \(i\)-th ancestor of the trap bottom \(\delta\), in the normalization of (3.5). Lemma 3.1 identifies this as a mean return time to \(\delta\) in the bottom-normalized infinite-tree network. Lemma 3.5 bounds \(E_Q\Lambda_i\le C(\beta f'(q))^i\), so Proposition 3.1 gives \(E_QS_\infty<\infty\): after multiplication by \(\beta^{-i}\), the remaining sum is geometric in \(f'(q)^i\), with \(f'(q)<1\). These are different quantities; the raw trap mass is not asserted integrable. On the backbone, super-regeneration creates iid blocks and a positive asymptotic fraction ρ of steps. The paper shows that hitting time is asymptotically concentrated in deep traps, proves that separated deep-trap gaps become independent, and reduces each long delay to excursions from the trap bottom. The limiting trap delay is encoded by
\[
Z_\infty=\frac{S_\infty}{1-\beta^{-1}}\sum_{i=1}^{\mathrm{Bin}(W_\infty,p_\infty)}e_i,
\qquad p_\infty=1-\beta^{-1},
\]
with the independent variables and the laws of (S_\infty,W_\infty,e_i) specified in the paper. Section 10 applies triangular-array/iid-sum limit theory to the trap delays; Section 11 transfers that limit to the walk and proves Theorems 1.1–1.4. The geometric trap-height lattice produces log-periodic subsequences and explains why the limit is generally not a full-sequence stable law.

## Scope boundary

This is the leaves-induced sub-ballistic regime. It does not contradict the leafless λ=m CLT or the positive-speed leafless regime: offspring assumptions and the direction/parameter convention differ. The source proves walk-height and hitting-time asymptotics, not harmonic-measure dimension or its monotonicity.

## Complete-paper coverage

| Physical PDF pages | Content read and proof mechanism |
|---|---|
| 1–4 | Model, conductance convention, critical bias, exponent γ, Theorems 1.1–1.4, proof roadmap. |
| 5–7 | Backbone construction, embedded walk, and super-regeneration blocks. |
| 8–11 | Finite-trap law, height tail, and trap-measure estimates. |
| 12–14 | Proof overview and deep-trap occupation; the hitting time is essentially spent in large traps. |
| 15–19 | Number of visits to a large trap and estimates for its excursion counts. |
| 20–22 | Asymptotic independence of time spent in different deep traps. |
| 23–26 | Time spent at trap bottoms and reduction to excursions from the bottom. |
| 27–35 | Laplace/characteristic analysis of deep-trap delay and limiting excursion variable. |
| 36–40 | I.i.d.-sum triangular-array limits, Lévy spectral function, centering/variance estimates. |
| 41–48 | Proofs of Theorems 1.1–1.4, including non-convergence and moment/density properties. |
| 49 | References. |

The rendered p. 2 verifies the transition probabilities, conductances, and γ; p. 3 gives the exact subsequential limit; physical pp. 10–12 verify the raw/bottom-normalized conductance distinction, the definition of \(S_\infty\), and the proof of its finite expectation; p. 12 checks the deep-trap reduction; p. 41 checks the triangular-array result.
