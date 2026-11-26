# Fixed-order analytic-jet transfer

Source: *Stabilizer orbits and thick tensor ideals of dualizable K(n)-local spectra*,
OpenAI/math commit `3344da59991ed94f9ba711217b29c1d760badfa6`, PDF pp. 23--24,
Lemma 5.2; local PDF SHA-256
`5daea1486344421401eb3b52f6c818af8ab9e980eae34faf67a470221bc05ca3`.

## Contract

Let `F` be complete non-Archimedean, with maximum norm on `F^r`.  Let `theta=(theta_i)`
be analytic at zero with `theta(0)=0`, and let scalar analytic germs `a_j` define the
formal map
`U_i(X)=sum_{j>=1} a_j(X) theta_i(X)^j`.  Require its linear part `L=dU_0` to be
invertible.  For `delta_N -> 0`, require integral (`|a_{N,j}|<=1`) numerical coefficients
and, for every finite `M`, eventual equality `a_{N,j}=a_j(delta_N)` for `j<=M`.
The numerical series `U_{N,i}=sum_j a_{N,j} theta_i(delta_N)^j` is then defined for all
sufficiently large `N`.

If an analytic germ `P` vanishes at those `delta_N` and its unique *formal* expansion is
`P=sum_l B_l U^l`, then, for each fixed `m>=0`, there are `D,D_m` and a threshold (the
latter two may depend on `m`) such that

`||delta_N|| <= D ||U_N||` and
`|sum_{|l|<=m} B_l U_N^l| <= D_m ||U_N||^(m+1)`.

Do not use this when coefficient matching is only heuristic, tail coefficients are not
integral/bounded, the linear jet is singular, or a conclusion needs simultaneous control
for unbounded `m`.  It does not establish convergence of either full formal series and
does not verify external geometric/topological hypotheses that supplied the germs.

## Independent finite-order derivation

Fix `m`.  Since `theta(0)=0`, only finitely many summands affect any given total degree,
so `U` is a formal map and formal inversion is legal when `L` is invertible.  Define the
actual analytic finite sum `F_m,i=sum_{j=1}^m a_j theta_i^j`.  On a sufficiently small
closed polydisc, analyticity gives `||theta(delta)||<=c||delta||`.  Coefficient matching
through `m` and the ultrametric triangle inequality give

`||U_N-F_m(delta_N)|| <= ||theta(delta_N)||^(m+1) <= c^(m+1)||delta_N||^(m+1)`.

The ordinary finite Taylor bound for the analytic `F_m` gives
`U_N=J_mU(delta_N)+R_{m,N}` with the same-order remainder.  At `m=1`, this is
`U_N=L delta_N+O(||delta_N||^2)`.  For sufficiently small nonzero `delta_N`, the error is
strictly smaller than `||L delta_N||`; ultrametricity yields
`||U_N||=||L delta_N||` and hence the inverse estimate with `D=||L^{-1}||`.

Let `Q_m(Z)=sum_{|l|<=m}B_l Z^l` and `V_m=J_mU`.  Formal substitution shows that
`P-Q_m(V_m)` has no terms through degree `m`; its analytic Taylor bound is therefore
`O(||delta_N||^(m+1))`.  A finite polynomial is Lipschitz on a sufficiently small unit
polydisc (telescope each monomial).  Applying that bound to `U_N-V_m(delta_N)`, using
`P(delta_N)=0`, and then the inverse estimate proves the displayed inequality.  Every
operation is at fixed degree `m`; no full-series convergence is invoked.

## Exact small model

Over `Q_3`, take `theta_i(X)=X_i`, `a_j=1`, and `a_{N,j}=1` for `j<=N`, zero otherwise.
For `delta_N=(0,3^N)`, the first coordinate makes `P(X)=X_1` vanish; `U_N` is a finite
geometric sum and its second-coordinate discrepancy from the analytic sum is exactly
`3^(N(N+1))/(1-3^N)`, whose 3-adic valuation is `N(N+1)`.  Thus it is at least the
required fixed-order tail valuation `(m+1)N` whenever `N>=m`.  The accompanying program
checks this using integer exponents, not floating point.
