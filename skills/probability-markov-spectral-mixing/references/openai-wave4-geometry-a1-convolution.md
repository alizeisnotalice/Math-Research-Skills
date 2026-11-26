# Conditional convolution and affiliated transport reference (Wave 4 geometry-a-1)

**Source.** *Invariant-projection counterexamples for every irrational rotation*, OpenAI (27 September 2026), physical pp. 18–19 and 23, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Invariant-projection-counterexamples-for-every-irrational-rotation-September-27-2026/paper.pdf), SHA-256 `951244ce4ac9e346a2e4d302e600d6fc58939deabe495638c2bb9070d037bca0`.

Given \(K\ge1\), unit-ball vectors \(\xi(x),\gamma(y)\in\ell^2(\mathbb Z)\), finite positive endpoint functions, and \(A_v=\xi_v(x)F_v(x)\), \(B_w=F_{-w}(y)\gamma_{-w}(y)\), Lemma 5.1 assumes the zero convolutions \(\sum_vA_vB_{-n-v}=0\) for \(0\le n\le2K\), its displayed multiplier bounds, a positive-probability event \(E\) with central coordinate lower bounds, and two conditional exceptional-event bounds.  Its conclusion is
\[
 c\,\varepsilon(K,D,a)\le(2K+1)(\eta+2\sqrt\delta).
\]
The included finite checker evaluates the truncated convolution and this exact algebraic inequality when \(\sqrt\delta\) is supplied rationally; it does not verify the infinite-tail or conditional-probability hypotheses.

For transport, Lemma 6.1 states that if an injective positive self-adjoint \(H\) is affiliated with a finite tracial von Neumann algebra and \(HA\zeta=BH\zeta\) on \(\operatorname{Dom}H\), then an \(A\)-invariant projection \(p\) transports to the projection onto \(H(\operatorname{ran}p\cap\operatorname{Dom}H)\), which is \(B\)-invariant and has the same trace.  Its proof uses spectral cutoffs \(E_N=\mathbf1_{[1/N,N]}(H)\); retain the domain-intertwining condition.
