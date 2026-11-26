# Homogeneous Mahler gap transfer

## Source and version

Dzmitry Badziahin, *On spectrum of irrationality exponents of Mahler numbers*,
local SHA-256 `87992e4a5f78c9c1d7b38e55477eb1d1fef3dfd2698fff9916e18395459d0c66`,
arXiv:1806.02946v1, 8 June 2018, 19 physical pages.  The local PDF was read
through p. 19.  The published version is *Journal de Théorie des Nombres de
Bordeaux* 31 (2019), 431--453, DOI
[10.5802/jtnb.1090](https://doi.org/10.5802/jtnb.1090).  This card uses the
local preprint's physical page locators and does not infer that its pagination
equals the published version.

## Exact finite algebra

Let \(f\in\mathbb Q((z^{-1}))\) satisfy the homogeneous equation

\[
f(z)=\frac{A(z)}{B(z)}f(z^d),\qquad d\ge2,
\]

with nonzero \(A,B\in\mathbb Q[z]\).  Suppose a pre-established convergent
\(p_u/q_u\) has \(u=\deg q_u\), and its next denominator degree is \(v>u\).
Set

\[
C=\gcd\bigl(A(z)p_u(z^d), B(z)q_u(z^d)\bigr),\qquad r_c=\deg C.
\]

If

\[
(d-1)(v-u)>\deg A+\deg B,
\]

then the source's Lemma 2 says the reduced image is a convergent and
its associated gap has endpoints

\[
u'=du+\deg B-r_c,\qquad v'=dv+r_c-\deg A.
\]

Its size is \(d(v-u)+2r_c-\deg A-\deg B\), which is strictly larger than
\(v-u\).  The formal residual identity behind this calculation is source
physical p. 4, equations (7)--(9).  The gap condition and convergent transfer
are source physical p. 8, Lemma 2.  This implementation recomputes the gcd,
reduction, degrees, endpoint formulas and strict numerical inequality over
\(\mathbb Q[z]\).

Run it with

```sh
python3 scripts/mahler_gap_step.py examples/mahler-gap-s2.json
python3 scripts/mahler_gap_step.py examples/mahler-gap-not-big.json
```

For \(A=z^2+2z+4\), \(B=1\), \(d=3\), and \(p/q=1/(z-2)\), the source
physical p. 16 identifies the initial gap \([1,3]\) when \(s=2\).  The exact
script gets \(C=1\) and \([u',v']=[3,7]\).  The second JSON proves only the
algebraic update and deliberately fails the big-gap hypothesis.

## Global gates retained outside the script

The source's Theorem 1 and Theorem 2 at physical pp. 2 and 4--7 require the
functional equation, a nonrational Laurent series, a valid evaluation point
\(b\) inside its convergence domain, and
\(A(b^{d^m})B(b^{d^m})\ne0\) for every \(m\ge0\).  They identify

\[
\mu(f(b))=1+\limsup_k d_{k+1}/d_k,
\]

under those global hypotheses.  A finite continued-fraction prefix, finite
nonvanishing audit, or the finite gap step above does not establish any of
them.

Primitive-gap reduction is source physical pp. 8--10, Lemmas 3--4.  The
eventual periodicity of the cancellation degrees \(r_{c,n}\), used to make a
limiting ratio rational, is source physical pp. 10--16, Proposition 2 and its
proof.  The finite-state/cyclotomic proof is not implemented here, so callers
must supply a separate complete periodicity proof before reporting an exact
irrationality exponent.  This route has no application to Euler's constant
without a separately proved homogeneous Mahler equation and every stated
global gate.
