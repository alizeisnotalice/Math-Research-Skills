# Sharp asymmetric second-moment tail bounds

**Source and version check.** Ion, Klaassen, and van den Heuvel, *Sharp inequalities of Bienaymé–Chebyshev and Gauß type for possibly asymmetric intervals around the mean*, local arXiv:2208.08813v2 (physical pp. 1, 3, 5, 11–13), SHA-256 `fa7a746d63ff91496ea45cf1258842568f20a587ce5bb455ef3fd9b45a4009a6`.  The published version is *TEST* 32(2) (2023), 566–601, DOI [10.1007/s11749-022-00844-9](https://doi.org/10.1007/s11749-022-00844-9); the publisher-linked institutional record identifies it as the final published version.  The adopted calculation is checked directly in the local v2 proof of Theorem 2.2 (physical p. 5).

## Standardized general-distribution branch

For a random variable \(Z\) with \(\mathbb E Z=0\), \(\mathbb E Z^2=1\), and \(0<v\le u\), Theorem 2.2 gives the sharp piecewise upper bound for \(\Pr(Z\le-u\ \text{or}\ Z\ge v)\):
\[
B(u,v)=
\begin{cases}
1,&u\le 1/v,\\
\dfrac{4+(u-v)^2}{(u+v)^2},&1/v\le u\le v+2/v,\\
\dfrac1{1+v^2},&u\ge v+2/v.
\end{cases}
\]
At the middle branch, the proof applies Chebyshev to
\(2Z-(v-u)\) at threshold \(u+v\).  The source supplies extremal laws for the displayed ranges, so do not replace this bound by a generic concentration inequality or apply it without the normalization and the ordering \(0<v\le u\).

## Shape-constrained branches

The sharper unimodal result (Theorem 5.2) is conditional on unimodality and has a different one-sided piecewise formula; Theorems 5.3–5.4 impose further stated ranges on \((u,v)\).  The mode-equals-mean formulas in Theorems 6.1–6.3 require that additional hypothesis.  Treat distribution class, standardization, interval ordering, and threshold branch as required inputs; the included exact checker intentionally implements only Theorem 2.2's unrestricted class.
