# SOS outer containment for a global attractor

Source: M. Schlosser and M. Korda, *Converging Outer Approximations to Global
Attractors Using Semidefinite Programming*, Automatica 134 (2021) 109900,
doi:10.1016/j.automatica.2021.109900; local arXiv:2005.03346v3.  Theorem 2 is
on physical pp. 8--9; Theorems 5--6 are on pp. 15--16.

The source's exact dual feasibility inequalities imply `w >= 1` on the
attractor and hence an outer containment.  Its SOS hierarchy further requires
polynomial dynamics, compact basic-semialgebraic data with the stated
Archimedean condition, exact SOS feasibility, and the Putinar step.

The resulting source conclusion is `A subset X_k subset Y_k` and convergence
in volume under those hypotheses.  It is neither a Hausdorff-error estimate
nor an acceptance rule for a floating-point SDP Gram matrix.  Before emitting
containment, independently verify every polynomial/Liouville/positivity
identity and all Gram witnesses exactly.
