# Affine-minimum plateau for mass-action systems

Source: OpenAI, *Uniform Permanence in Weakly Reversible Mass-Action Systems*, SHA-256 \`69edba6a8946a5517aae4b2add648ff9782069abe6409f7ecd31a82428853f07\`, physical pp. 3-4 and 8-9, Lemma 2.1, Corollary 2.2 and Proposition 3.1. Pinned snapshot: https://github.com/openai/math/tree/3344da59991ed94f9ba711217b29c1d760badfa6

At scale \(h\), write \(X_h(p)=(h^{p_1},\ldots,h^{p_m})\) and form a finite affine minimum
\[
F_h(x)=\min_{\lambda\in\Lambda}(r_\lambda\cdot x+b_\lambda(h)).
\]
Lemma 2.1 selects finite slopes \(r_\lambda\) independent of \(h\), with offsets \(o(h^a)\), so every active label approximates its exponent vector to prescribed tolerance.  Corollary 2.2 makes this uniform over \(p\) after the finite family is fixed.

For a fixed positive stoichiometric class and sufficiently small \(h\), Proposition 3.1 defines \(M_h=F_h(c)\), \(K_h=\{F_h=M_h\}\), and states that \(K_h\) is nonempty, compact, convex, and lies in \(\operatorname{int}[h^{1/2},h^{-1/2}]^d\).  The construction is class- and rate-specific.

## 固定来源

- 物理页 3, 4, 8, 9。Lemma 2.1, Corollary 2.2, Proposition 3.1 SHA-256 `69edba6a8946a5517aae4b2add648ff9782069abe6409f7ecd31a82428853f07`。[Uniform Permanence in Weakly Reversible Mass-Action Systems](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Uniform-Permanence-in-Weakly-Reversible-Mass-Action-Systems-October-5-2026/permanence.pdf)
