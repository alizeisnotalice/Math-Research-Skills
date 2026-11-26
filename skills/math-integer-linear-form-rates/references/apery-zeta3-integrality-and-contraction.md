# Apéry zeta(3): closing an integral linear-form proof

Use this as a model for the **full** closure of an Apéry-type argument: a
recurrence or fast rational convergence alone is not enough.  This is a
zeta(3) reference, not a route to Euler's constant.

## Verified source, version, and loci

Wadim Zudilin, *An elementary proof of Apéry's theorem*, arXiv:math/0202159v1
(17 February 2002), physical PDF pp. 2--6: Lemma 1 and equations (1)--(4),
Lemmas 2--3 and (6)--(7), Lemma 4 and (10), and the final inequality (15).
Local source `EXT-0303_An_elementary_proof_of_Apery_s_theorem.pdf` has
SHA-256 `1911eb1caf7cb4160929f48bc3900c45ce1fa9265b794c7f330df133ab88e680`.

The work was published as “Apéry's theorem. Thirty years after,” *International
Journal of Mathematics and Computer Science* **4** (2009), no. 1, 9--19.
The checked formula and proof locators are deliberately those of the local
arXiv v1; publisher pagination has not been substituted.

## The reusable closure pattern

Let

\[
 R_n(t)=\left(\frac{(t-1)\cdots(t-n)}{t(t+1)\cdots(t+n)}\right)^2,
 \quad D_n=\operatorname{lcm}(1,\ldots,n),
 \quad F_n=-\sum_{t\ge1}R_n'(t).
\]

Lemma 1 gives

\[
 F_n=u_n\zeta(3)-v_n,\qquad u_n\in\mathbb Z,\quad D_n^3v_n\in\mathbb Z.
\]

The partial-fraction coefficient is
\(A_{2k}^{(n)}=\binom{n+k}{n}^2\binom nk^2\), hence
\(u_n=2\sum_{k=0}^nA_{2k}^{(n)}\).  The initial forms are
`F_0=2 zeta(3)` and `F_1=10 zeta(3)-12`.  Creative telescoping gives, for
both coefficient sequences,

\[
 (n+1)^3x_{n+1}-(2n+1)(17n^2+17n+5)x_n+n^3x_{n-1}=0.
\]

The crucial non-finite input is the source's positive integral bound

\[
 0<F_n<20(n+1)^4(\sqrt2-1)^{4n}.
\]

Together with `D_n<3^n`, it yields an integer that is positive and eventually
strictly below one under a hypothetical `zeta(3)=p/q`:

\[
 0<qD_n^3F_n<20q(n+1)^4\,[27(\sqrt2-1)^4]^n.
\]

The base is rigorously below one: `27(sqrt(2)-1)^4<1` is equivalent to
`458<324 sqrt(2)`, and squaring leaves the positive integer margin
`2*324^2-458^2=188`.

## What a new candidate must supply

1. An exact identity isolating the target in **one** linear form.
2. A proved common integer normalization, not merely integral-looking initial
   values.
3. A strictly positive/nonzero remainder and an asymptotic upper bound after
   the very same normalization.
4. A denominator-growth inequality strong enough that the normalized upper
   bound tends to zero.

Run the finite audit with

```sh
python3 scripts/apery_zeta3_certificate.py --through 8
```

It checks the binomial formula, recurrence-generated values, and each finite
`D_n^3 v_n` inclusion.  It does not prove Lemma 4's all-`n` integral estimate
or transfer this construction to another constant.
