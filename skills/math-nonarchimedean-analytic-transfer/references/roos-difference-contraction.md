# Dense strict contractions solve the Roos difference equation

Source checked: OpenAI, *Failure of finite assembly for a chromatic overlap at the prime three*, Lemma 6.1, PDF p. 26; local SHA-256 `b1e58a49eb364dd8e29c4f4b78717cdceb6275f4d7f0f888b3759c0bc67167b7`, 72 pages. The pinned manuscript is [the PDF at openai/math commit 3344da59991ed94f9ba711217b29c1d760badfa6](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Failure-of-finite-assembly-for-a-chromatic-overlap-at-the-prime-three-September-25-2026/paper.pdf).

## Transfer statement

Let \((M_n,\|\cdot\|_n)_{n\ge0}\) be complete non-archimedean normed abelian groups and let \(f_n:M_{n+1}\to M_n\) be homomorphisms with dense image and \(\|f_nz\|_n\le c_n\|z\|_{n+1}\) for \(c_n<1\). Then
\[
D:\prod_{n\ge0}M_n\longrightarrow\prod_{n\ge0}M_n,
\qquad D(x)_n=x_n-f_n(x_{n+1}),
\]
is surjective. Therefore the usual two-term Roos complex has zero positive cohomology, so the positive derived inverse limits of this *countable chain* vanish.

The same conclusion for `Mapcts(T,M_n)` needs a profinite \(T\), its uniform/sup norm, completeness of the mapping spaces, and density after finite-clopen-partition approximation. This statement does not certify these conditions for a supplied geometric or spectral tower.

## Independent proof

Fix \(y=(y_n)\), choose any positive \(\epsilon_n\downarrow0\), and inductively make finite tuples satisfying the first \(n\) equations. Given \(x_0,\ldots,x_n\), density supplies \(x_{n+1}\) with
\[
d_n=y_n+f_n(x_{n+1})-x_n,\qquad\|d_n\|_n<\epsilon_n.
\]
Replace \(x_n\) by \(x_n+d_n\), and for \(i<n\) replace \(x_i\) by \(x_i+f_i\cdots f_{n-1}(d_n)\). The first \(n+1\) equations are then exact. For every fixed \(i\), later corrections have norm at most \(\epsilon_n\): this follows from the strict contractions (indeed the displayed composite is bounded by \(\|d_n\|\)). Thus the coordinate sequence is Cauchy, converges by completeness, and its limit solves every equation because each fixed coordinate equation was exact from a finite stage on. This proves surjectivity without assuming a simultaneous exact preimage at any finite stage.

For profinite \(T\), uniform continuity makes a continuous map uniformly close to one constant on a finite clopen partition. Approximate its finitely many values through the dense image of \(f_n\); the same construction applies to the complete mapping spaces.

## Exact small model and boundary

Let every \(M_n=\mathbb Q_3\) with the 3-adic norm and \(f_n(z)=3z\). These maps are surjective strict contractions. For the constant right side \(y_n=1\), the constant sequence \(x_n=-1/2\) exactly satisfies \(x_n-3x_{n+1}=1\). This is an exact calculation in the complete ambient group \(\mathbb Q_3\), not a claim that rational numbers alone are complete.

By contrast, the identity maps on \(\mathbb Q_3\) are not strict contractions, and the group \(\mathbb Q\) with the 3-adic norm is not complete. Neither case passes this interface merely because a particular right side might happen to have a solution.
