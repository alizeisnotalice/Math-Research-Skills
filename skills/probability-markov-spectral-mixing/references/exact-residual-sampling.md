# Exact uniform sampling by a rare residual correction

Use this construction only when the target is the uniform law on an explicitly finite state space and all of the following inputs have been certified.  It turns a certified approximate sampler into an exact one; it does not supply a mixing bound, a state-space count, or an efficient enumerator.

## Pinned source and scope

This is distilled from Section 8, especially pp.19–21, of the following preprint.  Page 18 supplies the particular switch-chain gap-to-TV estimate used there; pp.19–20 specify the rational tabulation and correction; p.21 limits the conclusion to expected polynomial bit cost.

- *Polynomial mixing of the switch chain for every graphical degree sequence* (OpenAI preprint, September 25, 2026), [official pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Polynomial-Mixing-of-the-Switch-Chain-for-Every-Graphical-Degree-Sequence-September-25-2026/main.pdf), SHA-256 `e70eab92c1315e6706eea3613e9826871e009d1ef8de31f82d5750d026240af3`.

The source applies the recipe to one specified lazy switch kernel after proving its own gap and size estimates.  This reference records only the residual-mixture mechanism.  In particular, it makes **no** assertion that an arbitrary switch chain has a suitable spectral gap or polynomial mixing time.

## Required certificate and exact representation

Let `Omega` have `M >= 1` elements, let `u(x)=1/M`, and fix a start state `x0`.  Supply integers `D >= 1`, `t >= 0`, and `q >= 1`, an exact kernel `P`, and `A=qP` such that:

1. `A[x,y]` is a nonnegative integer for every pair, and every row of `A` sums to `q`.  Thus one exact `P` step from `x` is obtained by drawing `U` uniformly from `{0,...,q-1}` and selecting the cumulative row interval containing `U`.
2. The correction branch can enumerate `Omega`, compute `M`, and propagate the integer row vector `a^(0)=1_{x0}`, `a^(s+1)=a^(s) A` through `s=t`.  Hence `p(x)=P^t(x0,x)=a^(t)(x)/q^t` exactly.
3. A proof certificate, not a floating-point estimate, gives

   `||p-u||_TV <= 2^(-2D)` and `M*2^(-D) <= 1`.

   An explicit upper bound `Mbar >= M` may replace `M` in both prerequisites.  If the first inequality is obtained from a reversible lazy/nonnegative-spectrum gap bound, retain the complete derivation, including the clock and the size bound; for example, the source uses `||P^t(x0,.)-u||_TV <= (sqrt(M)/2) exp(-gamma*t)`.  Do not label a numerical mixing experiment as this certificate.

The TV certificate implies for every `x` that `p(x) <= 1/M + delta^2`, where `delta=2^(-D)`.  Together with `M*delta <= 1`, this gives `(1-delta)p(x) <= 1/M`.  Consequently the residual below is nonnegative.

## Exact sampler

Set `delta=2^(-D)`.  Draw `D` fair bits.

- Unless all are zero (probability `1-delta`), simulate exactly `t` transitions of `P` from `x0` and output the result.  This branch has law `p`.
- If all are zero (probability `delta`), enumerate and propagate as above, then form the integer weights

  `w(x) = 2^D q^t - M(2^D-1)a^(t)(x)`.

  They are nonnegative and sum to `M q^t`.  Draw uniformly from `{0,...,M q^t-1}` and choose the cumulative interval with weights `w(x)`.  This branch has law

  `r(x) = w(x)/(M q^t) = [1/M-(1-delta)p(x)]/delta`.

Use independent fresh bits after the branch decision.  The output is therefore exactly

`(1-delta)p(x)+delta*r(x)=1/M`.

Uniform integer draws can use rejection from `ceil(log2 K)` fair bits for a range of size `K`; they terminate almost surely.  The correction branch may be exponentially expensive.  An expected-polynomial claim additionally needs a demonstrated bound on `delta` times its enumeration/tabulation cost, as in the pinned source; exactness alone does not provide that complexity guarantee.

## Exact finite replay

The following checked two-state instance exercises every integer formula.  Take `Omega={0,1}`, `x0=0`, `P=[[3/4,1/4],[1/4,3/4]]`, `q=4`, `A=[[3,1],[1,3]]`, `t=3`, and `D=2`.  Then `M=2`, `delta=1/4`, `M*delta=1/2`, and `||P^3(0,.)-u||_TV=1/16=delta^2`.

```python
from fractions import Fraction

M, q, t, D = 2, 4, 3, 2
A = ((3, 1), (1, 3))
a = [1, 0]
for _ in range(t):
    a = [sum(a[i] * A[i][j] for i in range(M)) for j in range(M)]
qt = q ** t
p = [Fraction(v, qt) for v in a]
w = [(2**D)*qt - M*(2**D - 1)*v for v in a]
r = [Fraction(v, M*qt) for v in w]
delta = Fraction(1, 2**D)
out = [(1-delta)*p[i] + delta*r[i] for i in range(M)]
assert (a, w, out) == ([36, 28], [40, 88], [Fraction(1, 2)] * 2)
```

Thus the ordinary law is `(9/16, 7/16)`, the residual law is `(5/16, 11/16)`, and their `(3/4,1/4)` mixture is exactly uniform.  This finite replay validates the arithmetic of the wrapper only; it is not evidence for any family-level mixing assertion.
