# KKT-gated cuts for nonsmooth convex MINLP

Source: X. Wei and coauthors, *New Outer Approximation Algorithms for
Nonsmooth Convex MINLP Problems*, arXiv:2602.04122v1, Propositions 3.1--3.3
and Theorem 3.2 (physical pp. 6--14).  This is a preprint source statement.

For a fixed integer assignment, add a feasible-point or infeasible-point cut
only with the source's certified global subproblem solution and its KKT data:
the selected joint subgradients, multiplier signs, normal-cone inclusion, and
the stated rho relation.  The infeasible cut proof is conditional on precisely
these relations; collecting arbitrary slopes is insufficient.

Finite nonrepetition/termination also needs the finite integer set and the
global master assumptions in Theorem 3.2.  This reference supplies no
floating-point multiplier validator.
