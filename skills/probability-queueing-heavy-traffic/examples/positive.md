# Positive example: audit a B054 candidate transform

Given a proposed candidate for the $n\times n$ switch, first fix the paper's input: $n$, queue indexing, IID bounded arrivals independent across input-output pairs, $\lambda=(1-\epsilon)\nu$ with $\nu\in F$ and $\nu_{ij}>0$, stationary laws $\pi^\epsilon$, diagonal covariance, and a scheduling policy satisfying the paper's SSC definition. Then:

1. Check it is defined on the source's \(\Theta\), satisfies Eq. (7) with the boundary terms $M_k$, and obeys the exact heavy-traffic/SSC hypotheses.
2. State whether the target is the literal Eq. (8) class, an analytic class augmented by $L(0)=1$, or the probability-admissible class. Under literal Eq. (8), scaling $(L,M)\mapsto(cL,cM)$ already defeats uniqueness; flag this as a source-formulation issue.
3. For probability admissibility, separately check $L(0)=1$, support on the nonnegative SSC cone, positivity/complete-monotonicity on the real Laplace domain, and a valid boundary-measure origin for each $M_k$.
4. Treat Theorem 4's $2n$-exponential expression as a candidate solving Eq. (7) under symmetric variance; identifying it as the heavy-traffic law needs a consistent uniqueness premise. A MATLAB marginal simulation can check this candidate law numerically but cannot prove uniqueness.

This sequence keeps the queue-derived normalized transform, the literal analytic-class statement, and numerical consistency evidence distinct.
