# Dyadic chord energy for stationary sequences

Let \((Y_t)_{t\in\mathbb Z}\) be a real stationary process with
\(\mathbb E Y_0^2<\infty\).  For \(h\geq0\), define
\[
 A_h=2^{-h}\sum_{t=0}^{2^h-1}Y_t,
 \qquad
 Z_h=2^{-h}\max_{0\leq u\leq2^h}
 \left|\sum_{t=0}^{u-1}Y_t-uA_h\right|.
\]
The empty sum is zero, so \(Z_0=0\).  The chord uses the mean of the
specific block.  It is not a chord of the unconditional mean.

Put
\[
 v_l=\mathbb E A_{l-1}^2-\mathbb E A_l^2\quad(l\geq1).
\]
Then \(v_l\geq0\), \(\sum_{l\geq1}v_l\leq\mathbb EY_0^2\), and
\[
 \lVert Z_h\rVert_2
 \leq \frac12\sum_{a=0}^{h-1}2^{-a/2}\sqrt{v_{h-a}}.
 \tag{1}
\]
Consequently
\[
 \sum_{h\geq1}\lVert Z_h\rVert_2^2
 \leq C\mathbb EY_0^2
 \tag{2}
\]
for an absolute constant \(C\).  Translation of the block to any
deterministic starting time has the same estimates.

## Proof record

For a length-\(2^l\) interval let \(U,V\) be the two half-block means
and \(W=(U+V)/2\) its mean.  The pointwise identity
\[
 \frac{(U-W)^2+(V-W)^2}{2}
 =\frac{U^2+V^2}{2}-W^2
\]
and stationarity give
\(v_l=\mathbb E(U-W)^2\).  Thus the \(v_l\) are nonnegative, and their
partial sums telescope to at most \(\mathbb EY_0^2\).  Independence of
the halves is never used.

Let \(F_a\) be the piecewise-linear cumulative-sum path using vertices
at multiples of \(2^{h-a}\).  It changes from the chord \(F_0\) to the
integer-time polygon \(F_h\).  On refining level \(a\), every one of the
\(2^a\) intervals receives its midpoint.  If \(U_j,W_j\) denote the
left-child and parent means on interval \(j\), its normalized midpoint
displacement is \(2^{-a-1}|U_j-W_j|\).  Bounding a maximum by the sum of
squares and then using stationarity yields
\[
 \left\lVert2^{-h}\lVert F_{a+1}-F_a\rVert_\infty\right\rVert_2
 \leq2^{-a-1}(2^av_{h-a})^{1/2}.
\]
The two triangle inequalities give (1).  Extend
\((\sqrt{v_l})_{l\ge1}\) by zero to nonpositive indices.  The right side
of (1) is its convolution with the \(\ell^1\) sequence
\((2^{-a/2-1})_{a\ge0}\), so the \(\ell^2\) convolution estimate gives
(2).

## Use boundary

This gives a finite-window error budget for a stationary scalar process.
It does not create a stationary law, a mixing estimate, a QR factorization,
or a Lyapunov splitting.  To apply it to a cocycle, first construct the
specific stationary scalar observable and separately verify every
deterministic estimate converting its chord deviations into the target
claim.  The estimate permits arbitrary dependence across time.

## Exact finite cyclic replay

The following computation uses rational values on a length-16 cycle.  A
uniform random starting position makes the cyclic sequence stationary.  It
checks the one-block variance identity and (1) at every available dyadic
scale.  It is a finite sanity check rather than a proof of (2) for general
processes.

```python
from fractions import Fraction
from decimal import Decimal, getcontext

y = [Fraction(n) for n in (2, -1, 3, 0, -2, 1, 4, -3, 2, 1, -1, 0, 3, -2, 1, 2)]
n = len(y)

def mean(start, h):
    return sum(y[(start + t) % n] for t in range(2**h)) / (2**h)

def e_square(values):
    return sum(value * value for value in values) / len(values)

def z(start, h):
    a = mean(start, h)
    return max(abs(sum(y[(start + t) % n] for t in range(u)) - u * a)
               for u in range(2**h + 1)) / (2**h)

getcontext().prec = 60
variances = {}
for h in range(1, 5):
    v = e_square([mean(s, h - 1) for s in range(n)]) - e_square([mean(s, h) for s in range(n)])
    left = e_square([mean(s, h - 1) - mean(s, h) for s in range(n)])
    assert v == left and v >= 0
    variances[h] = v
for h in range(1, 5):
    z_square = e_square([z(s, h) for s in range(n)])
    lhs = Decimal(z_square.numerator) / Decimal(z_square.denominator)
    rhs = sum(Decimal(1) / (Decimal(2) * (Decimal(2) ** (Decimal(a) / 2)))
              * (Decimal(variances[h - a].numerator) / Decimal(variances[h - a].denominator)).sqrt()
              for a in range(h))
    assert lhs.sqrt() <= rhs + Decimal("1e-50")
    print(h, variances[h], lhs, rhs)
```

The executed replay also evaluates the square-root form of (1) in high
precision real arithmetic after its variance identities have been checked
exactly.  It passed for \(h=1,2,3,4\).

Source. OpenAI preprint, *A zero-entropy system without a smooth positive
volume model*, PDF p. 5, Lemma 2.1.  Local PDF SHA-256:
`67d6dd8619de6c6fc11eb88edd3791b180a2c3c9bc6d5a6a68f272a5ab445687`.
The source's later smooth switching result has additional compact-manifold,
smooth-diffeomorphism, and invariant-measure hypotheses and is not included
here. [Fixed source PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-finite-entropy-system-without-a-smooth-positive-volume-model-September-25-2026/paper.pdf)
