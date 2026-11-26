# Bell-polynomial simultaneous gamma/zeta approximants

## Source, version, and scope

This component distils Theorem 1, Corollary 2, and Example 1 of Khodabakhsh
Hessami Pilehrood and Tatiana Hessami Pilehrood, *Rational approximations to
values of Bell polynomials at points involving Euler's constant and zeta
values*, **arXiv:1011.3833v1** (2010), PDF pp. 5--6.  The locally archived
original is

`07_Irrationality_Transcendence_Compendium/PDF/EXT-0058_Rational_approximations_to_values_of_Bell_polynomials_at_points_involving_Euler_s_con.pdf`

with SHA-256
`ad31e17bcbe489478aea5d302ab0a2bb6e8d6f442fb6a50b161ea72aafc331ca`.
The theorem's finite-sum formula is also justified on PDF pp. 8--9 through
Faà di Bruno's formula and the Bell-polynomial addition theorem.  Its
asymptotic proof is later in the same manuscript; this component does **not**
attempt to certify an asymptotic estimate from finite computation.

For an integer \(a\geq2\), \(1\leq\mu\leq a-1\), and \(n\geq0\), set

\[
 q_n=\sum_{k=0}^n {n\choose k}^{a}k!,\qquad
 r_m(k)=(m-1)!\left(aH_{n-k}^{(m)}+(-1)^m(a-1)H_k^{(m)}\right),
\]

and

\[
 p_{n,\mu}=\sum_{k=0}^n {n\choose k}^{a}k!\,
 Y_\mu(r_1(k),\ldots,r_\mu(k)).
\]

Here \(H_0^{(m)}=0\), and \(Y_\mu\) is the complete exponential Bell
polynomial.  The target is

\[
 \alpha_\mu=Y_\mu\!\left(\gamma,\,1!(2a-1)\zeta(2),\,
 2!\zeta(3),\ldots,
 (\mu-1)!\bigl(a+(-1)^\mu(a-1)\bigr)\zeta(\mu)\right).
\]

The theorem proves \(D_n^\mu p_{n,\mu}\in\mathbb Z\), with
\(D_n=\operatorname{lcm}(1,\ldots,n)\) and \(D_0=1\), and gives
sub-exponential simultaneous approximation to \(\alpha_\mu\).  It does not
prove irrationality of \(\gamma\), of any \(\zeta(m)\), or of a displayed
Bell-polynomial value.  Clearing the rational part alone does not create a
vanishing integer linear form.

## Exact executable component

`scripts/bell_gamma_zeta_approximants.py` uses only Python's standard-library
`Fraction` arithmetic.  It implements the Bell recurrence printed on PDF p. 4,
so every reported \(p_{n,\mu}\), \(q_n\), and \(D_n^\mu p_{n,\mu}\) is exact.
It deliberately represents \(\alpha_\mu\) symbolically rather than replacing
it with a decimal.

Example runs:

```sh
python3 scripts/bell_gamma_zeta_approximants.py \
  --a 2 --mu 1 --through 12 --crosscheck-a2 --negative-tests
python3 scripts/bell_gamma_zeta_approximants.py \
  --a 3 --mu 2 --through 8 --check-a3
```

The first check independently re-evaluates the \(a=2,\mu=1\) finite sum
\(\sum_k {n\choose k}^2k!(2H_{n-k}-H_k)\), hence cross-checks the installed
continued-fraction component's direct formula without importing it.  The
second retains Example 1's companion constant
\(\alpha_2=\gamma^2+5\zeta(2)\), checking the printed initial values
\(q_0,q_1,q_2=(1,2,11)\),
\(p_{0,1},p_{1,1},p_{2,1}=(0,1,13/2)\), and
\(p_{0,2},p_{1,2},p_{2,2}=(0,18,95)\).

## Dependencies and relationship to the previous component

The executable dependency set is Python standard library only; it requires no
network retrieval and no unversioned external preprint.  The source's actual
mathematical dependencies relevant here are E. T. Bell, *Exponential
polynomials*, Ann. of Math. 35 (1934), pp. 258--277 (its reference [2], for
the complete Bell-polynomial identities), and the authors' reference [8],
arXiv:1010.1420, for the \(a=2\) Euler-constant specialization.  The latter
is the source of the existing `math-gamma-continued-fraction-recurrence`
finite construction.  References [6], [7], [11], and [12] are cited by the
paper for adjacent constructions, algorithmic recurrences, or asymptotic
arguments, but are not dependencies of the exact finite evaluator here.

Use this component when a calculation needs the simultaneous family or one of
its Bell-polynomial companions.  Use the established continued-fraction
component when only the \(a=2,\mu=1\) sequence or its continued fraction is
needed.  Neither route supports an irrationality conclusion.
