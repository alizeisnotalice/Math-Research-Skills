# Scalar-codomain no-gap guard for occupation relaxations

Source: M. Korda and M. Rios-Zertuche, *The gap between a variational problem
and its occupation measure relaxation*, ESAIM: COCV 32 (2026), article 18,
doi:10.1051/cocv/2026018; local arXiv:2205.14132v4.  The scalar-codomain
no-gap result and its hypotheses are in physical pp. 19--31; the integral
constraint gap is demonstrated on pp. 49--50.

## Guard

Invoke the no-gap/superposition conclusion only after checking the paper's
scalar-valued setting and its stated occupation/regularity conditions.  Those
conditions are a source-level dependency: this reference does not synthesize
a superposition measure or certify them from discretized trajectories.

Do not extend the conclusion to added integral constraints.  The source's
example with `F(y)=y(1-y)` and `H(y)=1-10y` has classical feasible value `1`,
whereas a convex mixture of the two zero-cost constant curves satisfies the
occupation constraint with value `0.1`.  Thus a relaxed feasible measure need
not represent an admissible classical curve in that setting.
