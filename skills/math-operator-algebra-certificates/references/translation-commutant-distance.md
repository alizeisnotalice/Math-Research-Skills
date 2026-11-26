# Finite translation-commutant distance bound

Source: *Unitarizability implies amenability for discrete groups*, Lemma 2.1, PDF pp. 5--6, pinned OpenAI PDF SHA-256 `deec58813ffe560edaa6ffa48b13569ed8017145c7165f4da8a50b8b9ba6e9e6`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Unitarizability-Implies-Amenability-for-Countable-Groups-September-23-2026/paper.pdf).

For a finite group (and verbatim for the countable case once the bounded row and column maps are given), put \(B=T-C\), \(h=K+\|B\|\), and \(Q(s)=C[0,s]\). Translation invariance gives \(C[x,y]=Q(x^{-1}y)\). The row map \(R=\operatorname{row}_0(C)\) has norm at most \(h\), since \(R=\operatorname{row}_0(T)-\operatorname{row}_0(B)\). Its codomain has dimension \(k\), so
\[
\sum_s\|Q(s)\|_{HS}^2=\|R\|_{HS}^2\le k h^2.
\]
Likewise \(L=\operatorname{col}_0(A-C)\) has norm at most \(h\), and its domain has dimension \(k\). Its blocks are \(W(x^{-1})-Q(x^{-1})\), hence
\[
\sum_s\|W(s)-Q(s)\|_{HS}^2\le k h^2.
\]
Minkowski in \(\ell_2(G;HS)\) yields \(\sqrt E\le2\sqrt{k}h\). Rearranging and taking the infimum over translation-commutant \(C\) proves the displayed lower bound.

The finite cyclic script proves only an instance with scalar rational data. Its PSD test certifies \(d^2I-(T-C)^*(T-C)\succeq0\), so its declared `d` is a rigorous upper bound on the operator norm. It cannot establish a best distance, boundedness on an infinite group, or the paper's later direct-sum conclusion.
