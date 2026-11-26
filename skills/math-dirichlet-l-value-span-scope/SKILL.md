---
name: math-dirichlet-l-value-span-scope
description: Apply the current preprint's asymptotic Dirichlet L-value span lower bound with the exact conductor, coefficient field, and opposite-parity restrictions.
---

# Dirichlet L-value span lower-bound scope

For a Dirichlet character \(\chi\) of conductor \(N\), set \(K=\mathbb Q(\exp(2\pi i/\varphi(N)))\) and retain only integers \(i\) whose parity is opposite to that of \(\chi\). The source proves, for sufficiently large \(s\),
\[
\dim_K\operatorname{Span}_K\{L(\chi,i):2\leq i\leq s,\ i\equiv1-\varepsilon_\chi\pmod2\}
\ge {C_N\sqrt N\over[K:\mathbb Q]}\sqrt{s\over\log s},
\]
with the casewise explicit \(C_N\) in [the source record](references/mistiaen-dirichlet-l-span.md).

This is an asymptotic span statement with a non-explicit sufficiently-large threshold. It is not a numerical independence test, a same-parity result, a bound over \(\mathbb Q\) without field comparison, or an irrationality proof for a selected L-value.
