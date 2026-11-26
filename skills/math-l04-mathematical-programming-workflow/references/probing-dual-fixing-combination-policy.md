# Combination guard for probing and dual fixing

Source: Y. Wang, E. D. Dolan, and coauthors, *Enhancing Presolve in Mixed
Integer Programming by Combining Probing and Dual Fixing*, arXiv:2607.10767v1,
Algorithm 1 and Theorem 1 (physical pp. 5--9).  This is a preprint source
statement.

For every proposed directed fixing, retain a certificate for the corresponding
auxiliary bound and for every propagation implication used to form it.  The
source proves its reachability condition only with these exact ingredients.

In particular, branch implications obtained for a variable with zero objective
coefficient may each preserve an optimum but need not remain jointly safe when
accumulated.  The interference example on pp. 5--6 requires an explicit
policy: discard those implications before combination, or revalidate their
joint effect.  Solver status and timing data are not such certificates.
