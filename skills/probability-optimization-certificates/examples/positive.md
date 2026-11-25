# Exact optimization certificates: positive instances

## Rational LP duality

For `min 3x + 2y` subject to `x+y=1`, `x,y≥0`, the feasible primal point `(0,1)` has value `2`. The dual multiplier `π=2` satisfies `π≤3` and `π≤2`, also with value `2`. Exact feasibility and equal values certify optimality by weak duality.

## SOS lower bound on a declared compact interval

Minimize `f(x)=x²` over `1≤x≤2`.

The box generator g(x)=(2-x)(x-1) is nonnegative on this interval. The exact identity

x²-1=3(x-1)²+2g(x)

is an SOS quadratic-module certificate: both 3(x-1)² and constant2 are sums of squares over the reals. Hence f>=1 on the declared domain. The exact feasible point x=1 has f=1, so lower and upper certificates match and the optimum is1. This uses S024's accepted finite-certificate interface, not its unapproved extraction/termination algorithm. The identity is exact and can be checked without any SDP solver. If the box premise is removed, x=0 gives f=0 and g=-2; the same identity does not imply a global lower bound1. A nonnegative multiplier cannot rescue a negative generator outside its declared set.

The bundled exact checker is cases.py（本机附件：`evidence/R04/optimization_whole_entry_cases_v1/cases.py`）; its recorded output is cases.result.json（本机附件：`evidence/R04/optimization_whole_entry_cases_v1/cases.result.json`）. This verifies the finite identities shown, not hierarchy convergence or an unexecuted solver.

## Rump Krawczyk inclusion

The accepted M0349 interface is Theorem 13.3 (physical p. 89): for continuously differentiable `f`, `0∈X`, `x̃+X⊂D`, and `S=−Rf(x̃)+(I−RJ_f(x̃+X))X⊂int(X)`, the theorem supplies the stated root and uniqueness conclusion on the certified box. The minus sign is essential: for `f(x)=x`, center `1/4`, `R=1`, `X=[−1,1]`, the translated root enclosure `x̃+S` is `{0}` (the intermediate set is `S={−1/4}`); the incorrect plus sign returns `{1/2}`, which is not a root. The exact Fraction probe is linked in [the method guide](../references/method.md) and was run in the R04 high-review packet.
