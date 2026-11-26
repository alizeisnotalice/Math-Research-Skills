# Block-polar subspace repair

**Pinned source.** OpenAI, *Strong Ulam Stability Characterizes Amenability*,
Lemma 3.3, physical PDF p. 9 (pinned preprint PDF SHA-256
`b28d280b0c673c6904f2459168a8a5dba32ff7363158f7dc101abb1ed3cb3911`,
19 pages), [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Strong-Ulam-Stability-Characterizes-Amenability-October-5-2026/strong-ulam-stability.pdf).

## Transfer statement

Let `U` be a unitary on a real or complex Hilbert space and `P` an orthogonal
projection.  If

\[
\|U-I\|\le t<1/2\quad\hbox{and}\quad\|(U-I)P\|\le e\le1/2,
\]

then the block-polar construction below produces a unitary \(\widehat U\) that is the identity on \(PE\) and preserves its orthogonal complement. The bounds are
\[
\|\widehat U-U\|\leq3e,\qquad \|\widehat U-I\|\leq t+3e.
\]

## Independent proof of the reusable step

Write the blocks with rows and columns `PE,(I-P)E`.  Since
`(U* - I)P=-U*(U-I)P`, both the first block column of `U-I` and the first
block row have norm at most `e`; hence `||b||,||c||≤e`.  Consequently

\[
 \left\|U-\begin{pmatrix}I&0\\0&d\end{pmatrix}\right\|\le2e.
\]

The `d` block obeys `||d-I||≤t<1`, so it is invertible.  From the lower-right
block of `U*U=I`,

\[
d^*d=I-b^*b.
\]

Thus its polar factor `v=d(d*d)^(-1/2)` is unitary and

\[
 \|v-d\|=\|I-(d^*d)^{1/2}\|
 \le 1-\sqrt{1-e^2}\le e^2.
\]

It follows that `||Uhat-U||≤2e+e²≤3e`; the second estimate is the triangle
inequality.  This proof needs no finite-dimensional compactness and therefore
also applies to arbitrary Hilbert spaces.

## Boundary

The `t<1/2` and `e≤1/2` assumptions here reproduce the cited lemma.  A
particular instance may admit a repair outside them, but that is not certified
by this entry.  Numerical singular values alone do not certify the hypotheses;
use an exact calculation or a separately justified operator-norm bound.

```sh
python3 scripts/replay_rotation.py --case valid
python3 scripts/replay_rotation.py --case rejected
```
