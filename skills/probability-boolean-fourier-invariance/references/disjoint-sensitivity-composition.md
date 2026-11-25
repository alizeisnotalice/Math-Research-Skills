# Disjoint Boolean composition: sensitivity and zero-input block sensitivity

Use this component when a total outer Boolean function is evaluated on disjoint copies of a total inner Boolean function. It is a local composition rule, not a Fourier or spectral-sensitivity transfer theorem.

## Statement

Let \(f:\{0,1\}^a\to\{0,1\}\) and \(g:\{0,1\}^b\to\{0,1\}\) be total.  On coordinates \([a]\times[b]\), define

\[
(f\circ g)(x_1,\ldots,x_a)=f(g(x_1),\ldots,g(x_a)),
\qquad x_i\in\{0,1\}^b.
\]

For an input \(x\), let \(s(h,x)\) be the number of individual coordinates whose flip changes \(h\), and let \(\operatorname{bs}(h,x)\) be the maximum number of pairwise disjoint nonempty coordinate blocks whose flips change \(h\).  Write \(s(h)=\max_x s(h,x)\).

Then

\[
s(f\circ g)\le s(f)s(g).
\]

If \(g(0^b)=0\), then \((f\circ g)(0^{ab})=f(0^a)\) and

\[
\operatorname{bs}(f\circ g,0^{ab})
 \ge \operatorname{bs}(f,0^a)\operatorname{bs}(g,0^b).
\]

The second inequality is deliberately local: it concerns blocks sensitive **at the all-zero input**.  Do not replace either factor by global block sensitivity without separately proving that its witnessing blocks occur at zero.  Do not infer a statement about spectral sensitivity, an exponent \(\alpha\), or a separation rate from this component alone.

## Proof check

Put \(y_i=g(x_i)\).  A bit in child \(i\) is sensitive for \(f\circ g\) exactly when it is sensitive for \(g\) at \(x_i\) and flipping \(y_i\) changes \(f\) at \(y\).  Hence

\[
s(f\circ g,x)=\sum_{i:f(y^{\{i\}})\ne f(y)}s(g,x_i)
\le s(f,y)s(g)\le s(f)s(g).
\]

For the zero-input statement, take pairwise disjoint sensitive blocks \(C_1,\ldots,C_p\subseteq[a]\) for \(f\) at \(0^a\), and \(D_1,\ldots,D_q\subseteq[b]\) for \(g\) at \(0^b\).  The blocks \(E_{ij}=C_i\times D_j\) are nonempty and pairwise disjoint.  Flipping \(E_{ij}\) makes precisely the children in \(C_i\) change from inner value zero to one, so it changes the outer value because \(C_i\) is sensitive for \(f\) at zero.  Thus there are \(pq\) disjoint sensitive blocks at zero; maximize over the two families.

## Pinned source and finite replay

- **Pinned source:** OpenAI, *A superquadratic separation between sensitivity and block sensitivity* (25 September 2026), SHA-256 `a589970798bc590e5a27cb35cfa3092a355a4048cfa383bc369177289a00a1f8`, PDF p. 9, Lemma 4.2.  Local extracted page: `/Volumes/data/CodexTemp/Math-Research-Skills/openai-corpus.gruR7ANo/pages/a589970798bc590e5a27cb35cfa3092a355a4048cfa383bc369177289a00a1f8.json` (array index 8).
- **Exact finite replay:** for \(f=\mathrm{OR}_2\) and \(g=\mathrm{OR}_2\), exhaustive enumeration gives \(s(f)=s(g)=2\), \(s(f\circ g)=4\), and \(\operatorname{bs}(f,00)=\operatorname{bs}(g,00)=2\), \(\operatorname{bs}(f\circ g,0000)=4\).  The composition is \(\mathrm{OR}_4\), so both inequalities are equalities.  This is a finite check of the stated hypotheses and conclusion, not evidence for any stronger asymptotic claim.
