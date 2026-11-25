# Weighted threshold anticommutator: local interface

Use this reference only for the finite, uniform Boolean-cube construction below.  It is useful when a real multilinear polynomial threshold function is already part of the problem and one needs to turn a same-sign edge count into a Hilbert--Schmidt calculation.  It is not a substitute for an independently verified global influence theorem.

## Pinned source and scope

- **Source:** OpenAI, *Average sensitivity of polynomial threshold functions*, 25 September 2026, preprint, 13 pages.
- **Pinned PDF:** [OpenAI math repository, commit `3344da59991ed94f9ba711217b29c1d760badfa6`](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026/main.pdf); SHA-256 `441f9f8a40930603ba88967f00514a974f13a8f8ab901f71206b2b7dc82e4884`.
- **Locally checked pages:** physical pp. 4--9 in the page array named by that SHA: the weighted grading (pp. 4--6), edge recovery (pp. 6--7), and parity/reflected coupling (pp. 8--9).  The source is a preprint.  Its headline total-influence theorem is deliberately not imported here.

All edges and pairs below are ordered.  Put \(\Omega=\{-1,1\}^n\), \(N=2^n\), and use the counting inner product.  The statements require a strictly positive weight \(w\colon\Omega\to(0,\infty)\); zero values must be dealt with before invoking the construction.

## Checked local identities

Let \(V_k=\operatorname{span}\{\chi_S:|S|\le k\}\), \(D=\operatorname{diag}(\sqrt w)\), \(K_k=DV_k\), and let \(E_k=K_k\cap K_{k-1}^{\perp}\) with orthogonal projections \(\Pi_k\).  Define

\[
 M=\sum_{k=0}^n\left(k-\frac n2\right)\Pi_k.
\]

The dimension bookkeeping gives \(\dim E_k=\binom nk\) and
\(\lVert M\rVert_{\mathrm{HS}}^2=nN/4\).  Coordinate multiplication has only equal- or adjacent-grade blocks:

\[
 \Pi_s Z_i\Pi_r=0\qquad\text{when }|s-r|>1.
\]

For a sign multiplier \(H=\operatorname{diag}(h)\), \(h\colon\Omega\to\{-1,1\}\), set
\[
 E_h=\{(x,y):\rho(x,y)=1,\ h(x)=h(y)\}.
\]
The source's local anticommutator lemma is

\[
 |E_h|\le 2\lVert MH+HM\rVert_{\mathrm{HS}}^2. \tag{A}
\]

Its proof uses only the preceding block locality, the fixed Hilbert--Schmidt energy, and the pointwise identity
\((MH+HM)_{xy}=(h(x)+h(y))M_{xy}\).  In particular, it counts same-sign **ordered** edges and has no probability conclusion by itself.

For a nonvanishing real multilinear \(p\) of degree at most \(d\), let \(f=\operatorname{sgn}p\), let \(\chi_{[n]}\) be full parity, and choose
\[
 w=|p|,\qquad h=\chi_{[n]}f,\qquad q=\chi_{[n]}p.
\]
Then full parity reverses on each cube edge, so same-sign edges of \(h\) are exactly the sensitive edges of \(f\).  Since \(q\) has Fourier support in degrees at least \(n-d\), character orthogonality gives the reusable zero-block fact

\[
 \Pi_sH\Pi_r=0\quad\text{if }r+s<n-d. \tag{B}
\]

Normalize the block Hilbert--Schmidt squares by
\[
 \Pr\{R=r,S=s\}=N^{-1}\lVert\Pi_sH\Pi_r\rVert_{\mathrm{HS}}^2.
\]
Each marginal is exactly \(\operatorname{Bin}(n,1/2)\), because \(H\) is unitary and \(\dim E_k=\binom nk\).  With \(U=S\) and \(V=n-R\), binomial symmetry gives equal marginals, while (B) gives the one-sided support condition \(V-U\le d\).  This is the coupling interface.  When a later argument needs a quantitative inequality for that coupling, prove or independently source it at that point; do not treat this reference as a verification of a global PTF bound.

## Exact finite replay actually run

The following exact rational replay was run with Python's standard-library `fractions.Fraction` (no floating point) for \(n=3\), \(p(x)=x_1+1/4\), \(f=x_1\), \(w=|p|\), and \(h=\chi_{[3]}f\).  To avoid radicals, write every projection as \(P_k=DB_kD\), where \(A_k\) is the \(\{\chi_S:|S|\le k\}\) evaluation matrix and

\[
 B_k=A_k(A_k^{\mathsf T}\operatorname{diag}(w)A_k)^{-1}A_k^{\mathsf T}.
\]

Thus all squared point-basis entries are the rational numbers \(w_xw_y(M_B)_{xy}^2\), and a zero block in (B) is tested as \(B_s\operatorname{diag}(wh)B_r=0\).  The actual outputs were:

```text
HS2(M)=6 = nN/4
|E_h|=8; A0=1/8; F=0; max_edge_sq=1/4
HS2(MH+HM)=8; 2 HS2(MH+HM)=16
all blocks r+s<n-d are zero: True
I(f)=|E_h|/N=1; inequality (A): True
```

This replay checks the normalization, ordered-edge convention, local edge inequality, and the spectral-support-to-coupling zero region in one nonconstant threshold example.  It is finite evidence for the implementation details, not a proof beyond this instance.
