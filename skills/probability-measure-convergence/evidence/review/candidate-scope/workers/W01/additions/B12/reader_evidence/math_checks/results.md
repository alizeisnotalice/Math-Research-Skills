# Local mathematics checks

Executed with the project's local `.runtime` Python and SymPy; machine-readable output is `conditional_kernel_checks.json`.

1. For B18-005 Example 9.1, symbolic expansion gives
   `1/2*(x^2 - 2*r*x*y + y^2) - 1/2*(x-r*y)^2 - 1/2*(1-r^2)*y^2 = 0`.
   The displayed scaled log-mgf `lambda*r*y + lambda^2/2` on physical p. 31 has Legendre transform `1/2*(x-r*y)^2`. The prose sentence on physical p. 32 (printed p. 1089) prints `(x-r*y)^2`; the difference is `(x-r*y)^2/2`. This is a source-text discrepancy flagged in the card, not an author-text correction or proof of the LDP.
2. Exact two-atom conditional-kernel example: for each n put mass 1/2 at `(X,Y)=(0,1/n)` and 1/2 at `(1,-1/n)`. The joint laws converge weakly to the equal mixture at `(0,0)` and `(1,0)`. At `y_n=1/n`, the conditional law of X is `delta_0`, whereas at the limit conditioning value `Y=0` it is the equal mixture. The bounded continuous test `phi(X)=X` separates the two conditional laws by exactly 1/2. Thus joint weak convergence alone cannot entail convergence of the selected conditional laws. This example does not satisfy or refute the full LDP hypotheses of Theorems 1.2/1.3; it only demonstrates why extra kernel/version hypotheses matter.

These calculations check the algebra and the finite example; they are not proofs of parameterized disintegration, conditional LDP criteria or any general theorem.

The normalizer check forms `[[1,-r],[-r,1]]`; SymPy returns determinant `1-r^2` and eigenvalues `1+r`, `1-r`. The two-dimensional Gaussian integral is finite exactly when `|r|<1`. Together with the source's `r≠0`, the model as stated is valid for `0<|r|<1`; this algebraic integrability check is not an LDP proof.
