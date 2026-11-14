# Method: preserve model and information geometry

## 1. Freeze the statistical model

Record: action set (finite or continuous); conditional observation law; unknown parameter/function class; reward/mean map; filtration/adaptivity; regret or identification objective; horizon versus stopping rule; and uniformity/uniqueness assumptions. A Bernoulli observation can have very different parameters:

- direct mean: \(Y_t\mid x_t\sim\mathrm{Ber}(f(x_t))\), with \(f(x)\in[0,1]\) in an RKHS;
- logistic link: \(Y_t\mid x_t\sim\mathrm{Ber}(\sigma(g(x_t)))\), where \(g\) is the latent RKHS/linear score;
- additive noise: \(Y_t=f(x_t)+\epsilon_t\), with conditional subgaussian or Gaussian \(\epsilon_t\).

The source W15-001 is the direct-mean target. W15-013, -016, -017, -033, and the Bernoulli specialization of W15-034 are logistic-link analogues. W15-017 uses $Y\sim\mathrm{Ber}(\sigma(a^\top\theta))$, with finite-dimensional score and a logistic sensitivity constant; its confidence/regret bounds cannot be relabeled as direct-mean RKHS results. W15-006/-018/-019 use additive subgaussian/Gaussian observations.

## 2. Change of measure

For a common adaptive algorithm under environments \(\theta,\lambda\), derive the KL of the complete transcript. In finite arms with conditionally independent arm samples,
\[
D(P_\theta^T,P_\lambda^T)=\sum_{x\in\mathcal X}\mathbb E_\theta[N_x(T)]D(P_{\theta,x},P_{\lambda,x}).
\]
For any event \(A\), data processing lower-bounds this by \(d(P_\theta(A),P_\lambda(A))\); Bretagnolle–Huber gives a useful exponential error form. At a stopping time, verify integrability and the stopped-filtration version rather than silently reusing a fixed-horizon identity.

Then define alternatives that force a different best arm (or a wrong recommendation) and formulate the allocation LP/minimax problem. In a structured model, the alternatives must lie in the same RKHS-constrained family. Unstructured alternatives can only produce an unstructured baseline.

## 3. Confidence regions and allocation

For independent Bernoulli arms, invert the KL tail bound: a confidence endpoint solves \(N_x d(\hat p_x,q)\le\beta_t(\delta)\). For RKHS estimates with additive subgaussian noise, kernel self-normalized ellipsoids give simultaneous confidence bounds, but this alone does not exploit Bernoulli KL. Do not treat a per-arm KL endpoint as a correlated RKHS confidence region.

For fixed confidence, optimize proportions against the hardest alternative and track them; stopping must be calibrated for the requested error probability. For fixed budget, optimize error exponent at a fixed terminal time. Never infer universal fixed-budget optimality from a fixed-confidence theorem.

W15-020 is a separate fixed-confidence linear BAI comparison: its fixed-sequence OLS bound supports G/XY and within-phase allocations, while a fully adaptive OLS bound pays a $\sqrt d$ factor. Its finite-action, additive bounded i.i.d.-noise model assumes a unique best arm. Do not use the printed Lemma 2 lower bound for $H_{LB}$: physical pp.4, 11 have a gap-replacement direction error, and the proof uses $\lambda_{\max}(\Lambda_\lambda)\le L$ despite $\|x\|_2\le L$. The exact witness in `evidence/W15/linear_bai_lemma2_counterexample.py` yields $H_{LB}=1$ against printed RHS $100$. The direct safe consequence is $L^{-2}\max_y \|y\|_2^2/\Delta(y)^2\le H_{LB}$, retaining each direction gap; this is a sampling-design analogue, not Bernoulli KL or cumulative-regret guarantee. The counterexample does not address the separate static/adaptive allocation theorems.

For finite-dimensional logistic designs, W15-016 Theorem 1 is fixed-design: its width is (2.4\|x\|_{H_t(\theta^*)^{-1}}\sqrt{\log(2(2+t_{\rm eff})/\delta)}), on the stated variance-comparison event and with the theorem's burn-in/design assumptions. Keep the square root around the logarithm and do not apply this bound to reward-adaptive sampling; the paper explicitly warns that adaptivity breaks the fixed-design premise. W15-027 Theorem 22 is instead additive-subgaussian linear fixed-confidence BAI, with complexity (O(\sum_{i=2}^{d}(c_0/\Delta_i^2)(\log\delta^{-1}+\log|\mathcal X|+\log\log\Delta_i^{-1}))); there is no additional leading factor (d) outside the sum. It is a design/allocation analogue, not a Bernoulli-KL RKHS regret result. Both papers are now full-text read with their official supplements; the appendix proofs are recorded in separate-document page ranges in the W15 coverage ledger. Their additive-subgaussian/fixed-confidence model distinction from direct Bernoulli-KL RKHS regret remains unchanged.

For nonparametric fixed-budget best-arm identification, W15-010 studies the exponent of P(I_T ≠ a*) at a fixed T. Its successive-rejects upper bound is based on pairwise Chernoff rates Φ; for P[0,1] these can be rewritten as the paper's L information quantities. The Corollary 4 ordering is by an information lower bound f≤Φ (in the P[0,1] specialization, by Φ=L), not generically by mean rank. Ordering by descending means is only the separate Hoeffding gap-square specialization. Its lower bounds require distinct assumptions: Theorem 10 uses consistency, worst-arm balance, and pruning; Theorem 13 uses consistency, monotone allocation, and normality of the distribution model; Theorem 14 only assumes consistency but is weaker. Do not import these as a fixed-confidence stopping theorem or as an instance-dependent regret result. Preserve the endpoint caveat when replacing strict by non-strict KL constraints.

W15-008 is an RKHS lower-bound construction for additive Gaussian observations and continuous-domain minimax simple/cumulative regret. Its localized bumps and Fourier-RKHS norm argument can guide proof design, while its Gaussian KL and minimax rates do not transfer directly to Bernoulli observations with mean f(x).

W15-007 is an additional continuous Matérn-RKHS instance-dependent regret source under additive Gaussian/subgaussian observations. Its lower-bound construction requires the whole radius-$w$ ball to fit in the gap annulus (Remark 8, physical p.16); a packing of centers alone is insufficient. The printed bump amplitude $(c+1)\Delta$ at its center conflicts with the claimed $\sup|f-f_i|\le c\Delta$ and the $c^2\Delta^2/(2\sigma^2)$ Gaussian-KL step (pp.17–18). Treat that proof chain as unverified unless a feasible bump and its amplitude/KL are independently repaired and recalculated. The PDF also has nonmatching displayed exponent formulas in its upper-bound discussion; preserve their literal locations and do not declare a matching rate from the inconsistent expressions.

W15-017 is an adjacent logistic-link Bernoulli GLM source, not the direct-mean RKHS model. Its main Theorems 1–2 place the leading $\log(T/\delta)$ inside the square root (physical pp.4, 8), whereas Appendix D.1 restatement/proof and D.3 proof conclusion put it outside (pp.24–26, 30). Use the conservative outside-root factor when relying on the displayed proof and retain the discrepancy; TS-ECOLog is Appendix D.2, physical pp.26–28; the top of p.28 completes its proof, and D.3 begins later on that same page.

W15-011 treats the existence of a single fixed-budget algorithm family that matches a pointwise error-exponent oracle simultaneously on every instance. Its difficulty is H(μ)=T/log(1/p), the reciprocal of an error exponent. For static proportions, the oracle is an infimum over allocation vectors against structured alternatives; the Bernoulli two-arm result shows that a universal adaptive family cannot everywhere match this oracle. The finite-T result has a second-order log(2)/√T term and assumes the alternative's difficulty is at most √T. Keep this pointwise-uniformity question separate from fixed-confidence expected stopping time, regret, and instance-specific improvement.

## 4. OSSB candidate-transfer checklist for finite direct-Bernoulli RKHS

A possible structured parameter set is the finite evaluation image
\[
\Theta_F=\{(f(x))_{x\in\mathcal X}: f\in\mathcal H_k,\ \|f\|_{\mathcal H_k}\le B,\ f(x)\in[0,1]\}.
\]
It gives finite Bernoulli arm laws and a structured family. Before importing Combes–Magureanu–Proutière (W15-015), verify all items:

1. Unique best arm at the instance.
2. Direct observations \(\mathrm{Ber}(\theta(x))\) and reward \(\mu(x,\theta)=\theta(x)\).
3. The exact evaluation image is a known compact parameter set and represents every admissible B056 mean vector.
4. Bernoulli KL continuity on the finite-valued part of the parameter domain.
5. Uniqueness of the semi-infinite LP optimizer, or a theorem that handles multiple optimizers.
6. The OSSB estimate used to evaluate \(c(x,\widehat\theta)\) belongs to the structured domain or has a justified projection/extension.
7. The semi-infinite LP can be evaluated/solved by a specified oracle; the paper's general algorithm calls it repeatedly and notes it may be hard.
8. Keep the theorem's asymptotic \(\log T\) coefficient distinct from its finite-time bound with instance-dependent remainder constants.

Until all interfaces are proved, report OSSB as a candidate coverage result. Do not claim the B056 open problem is solved.

Source audit note for W15-015: Appendix B.2 (PDF p. 11) defines `Λ′(θ)={λ∈Θ:max_{x≠x*(θ)} μ(x,λ)>μ(x*(θ),λ)}`, a strict reward-crossing set, not a KL allocation threshold. Rendered PDF p. 12 explicitly identifies `inf_{λ∈Λ′(θ)}〈c*,D(θk,λ)〉` with `min_{λ∈overline{Λ′(θ)}}〈c*,D(θk,λ)〉`, notes `overline{Λ′(θ)}⊂Θ` and compactness, then applies Berge with minima over this closure. The earlier assertion that the source itself treated the strict set as compact was withdrawn: OCR had dropped the overlines. This visual correction removes that specific alleged proof gap; it does not prove the B056 transfer. Continue to check the model fit, empirical parameter domain, uniqueness assumptions, and computability of a repeated semi-infinite-LP oracle before importing OSSB.

## 5. Numerical evidence

A numerical allocation scan can verify algebra, KL values, or a discretized LP for a finite example. State the grid, model, and whether alternatives are discretized; such a scan is not a proof of the semi-infinite constraint or an algorithmic regret theorem. The saved MATLAB example uses the direct model \(f_\theta(x)=\theta^Tx\), Bernoulli parameter \(f_\theta(x)\), and a finite grid of alternatives. It is a consistency check only.


## 6. Fixed-budget oracle non-existence is an asymptotic boundary

W15-012 (Goldberger, 2026, §§2–4; Theorems 1–3) studies a finite number K of independent arms, unique best mean, and a consistent algorithm family with a fixed terminal budget. Its static oracle hardness is H_so=1/Gamma*_so, and its lower bound shows that for K≥3 no single algorithm family uniformly attains that pointwise fixed-allocation error exponent over all unconstrained mean vectors in a regular one-parameter NEF. The change-of-measure inequality uses KL(mu_k,lambda_k); the static-oracle exponent uses KL(lambda_k,mu_k), so preserve direction. The result is asymptotic in T and does not supply a confidence region, a finite-time regret theorem, or a computable sampling rule.

This can motivate searching for structured alternatives, but is not a direct theorem for B056. Bernoulli being an NEF only identifies the per-arm observation family. Theorem 3 allows the K means to vary freely in an open interval; a direct-mean Bernoulli RKHS model constrains the entire vector through its RKHS evaluation image. To transfer the lower bound, separately prove that its baseline and alternatives belong to the exact constrained image and meet the needed uniqueness/oracle conditions. To use it for a regret claim, also bridge asymptotic error exponents to the finite-time objective. See the explicit crosswalk in evidence/W15/cards/W15-012.md; current status is candidate/transfer unproved.


## 7. Gaussian fixed-confidence EBS: use within its exact model

W15-014 studies independent known unit-variance Gaussian arms with bounded means and a unique best arm. Its fixed-confidence design combines a time-uniform product confidence region, the conservative target \(\tilde\mu\in\arg\max_{\nu\in CR}w_{\min}(\nu)\), C-tracking, and a Gaussian GLR stopping rule. Section 3 gives an explicit scalar root for the optimal proportions and quantitative continuity bounds; those regularity estimates are essential to its finite-time proof. Theorem 5's tail and expectation guarantees hold on a coverage event of probability at least \(1-\gamma\), and the expectation is \(E[\tau\mathbf1_E]\); preserve this truncation and its small-\(\delta\) threshold. Theorem 6 is asymptotic fixed-confidence sample complexity.

This is a useful design pattern for conservative confidence-set allocation and optimizer regularity. It is not a direct-mean Bernoulli RKHS or fixed-budget regret theorem: its explicit optimizer assumes Gaussian quadratic KL, independent arm estimates, and no cross-arm RKHS constraint. Re-derive the confidence geometry, constrained allocation, computational oracle and finite-time regret statement for B056.

W15-014 Proposition 15 is printed for any simplex vector \(v\), but its Appendix C.6 proof invokes Lemma 18, which assumes relative allocation error \(\eta\in[0,1]\) (physical PDF p.20). A direct counterexample with \(\eta>1\) is recorded in `evidence/W15/proposition15_counterexample.py`; preserve the source's literal statement and flag this proof-scope limit. Theorem 5 itself assumes its parameter \(\eta\in(0,1]\), so this issue alone does not refute its stated application.



## 8. Adjacent linear, GLM, and kernel-regularity results

- **W15-021:** Gaussian linear best-arm identification is a fixed-confidence stopping-time problem. The finite-arm lower bound and lazy Track-and-Stop use covariance-design allocations and assume a unique best arm. Theorem 2 is an almost-sure asymptotic bound with the source-defined universal-constant relation \(\lesssim\), not an exact coefficient-one \(\le\); Appendix F proves it. Theorem 3 also retains \(\lesssim\) under its quantitative tracking condition. The sphere theorem statement (denominator 20) differs from the Appendix G.1 proof conclusion (denominator 40). This is a design/tracking proof pattern, not Bernoulli-KL cumulative regret or an RKHS-constrained alternative set.
- **W15-022:** Generalized-linear BAI uses a known increasing link with derivative lower/upper bounds, bounded feature vectors, and a finite-dimensional shared parameter. Physical p.7 defines \(\kappa=\sqrt{3+2\log(1+2L^2/\lambda_0)}\). Proposition 1 is fixed-time and uniform over feature pairs; only Theorem 1 applies a union bound with \(\delta_t=6\delta/(\pi^2t^2)\) to obtain all-times coverage. GapE solves a feature-space \(\ell_1\) representation LP and proves approximate-PAC stopping; logistic Bernoulli is a sigmoid-link example. Eq. (4) states the estimate as a score-equation solution without a projection; (c_\mu) is only lower-bounded on the true parameter ball. Before relying on the confidence proof, check finite well-definedness of the estimate and \(\dot\mu\ge c_\mu\) on the actual segment to it. The all-success logistic example in `examples/negative.md` diagnoses this proof interface, not a general theorem falsity. Do not treat the source as the direct mean \(Y\mid x\sim\mathrm{Ber}(f(x))\) with \(f\) constrained by an RKHS, or as an instance-dependent regret result.
- **W15-028:** Theorem 3/Theorem 9 lower-bound adaptation between smoother and rougher RKHS classes is for continuum \([0,1]^d\), specialized to \(d=1\), integer regularities \(m_1<m_2\), additive 1/4-sub-Gaussian noise, and jointly feasible radii. The full constraints are in Appendix A.2 and the bump/Pinsker proof is in Appendix B.1. Equation (55) writes an exact trajectory KL of \(2\mathbb E_0[N_{H_s}]\Delta^2\). A sub-Gaussian envelope alone does not determine an exact shifted-noise KL: for Bernoulli means \(p=0.1,q=0.2\), \(\mathrm{kl}(p,q)=0.0366900140\ne2(q-p)^2=0.02\). Use this result for regularity-adaptation and Sobolev/RKHS construction methods, while requiring a separate valid KL bound for direct Bernoulli feedback. This flags a step not justified by the stated envelope alone; it does not prove all lower-bound conclusions false. The card and saved calculation are `evidence/W15/cards/W15-028.md` and `evidence/W15/kernel_regularity_bernoulli_kl_check_results.txt`.

These three works are full-text read but awaiting independent review; the source cards preserve the theorem/proof locations and source-internal wording/constant discrepancies.
