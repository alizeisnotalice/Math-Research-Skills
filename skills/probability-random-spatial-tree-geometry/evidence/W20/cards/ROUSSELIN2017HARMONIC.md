# ROUSSELIN2017HARMONIC — invariant measures and dimension drop on GW trees

**Source:** Pierre Rousselin, “Invariant Measures, Hausdorff Dimension and Dimension Drop of Some Harmonic Measures on Galton–Watson Trees,” arXiv:1708.06965v2. Read the complete 37-page PDF (SHA-256 `2d1f6a9bb7230e9c6c23d40136dce22e001951af8176e3e53e6fb9a317f57b8e`).

## General flow-rule theorem

Section 2 (PDF pp. 5–10) defines a marked Galton–Watson flow rule. For a marked tree (T), a positive observation φ obeys a recursion

\[
\phi(T)=h\!\left(\Gamma_{\varnothing},\sum_{i=1}^{\nu_T(\varnothing)}\phi(T[i])\right),
\]

where (h:J\times J\to J) is measurable on the common interval (J\subset(0,\infty)) and satisfies the paper’s three identities: symmetry (h(u,v)=h(v,u)); associativity (h(h(u,v),w)=h(u,h(v,w))); and the position-of-summand identity

\[
\frac{h(u+a,v)}{(u+a)v}=\frac{h(u,a+v)}{u(a+v)}\quad (u,v\in J,\ a>0).
\]

With κ(u)=\(\mathbb E[h(u,\sum_{i=1}^{\nu_T(\varnothing)}\phi(T[i]))]\), using an independent marked GW tree inside the expectation, Theorem 3.2 (PDF p. 11) says that if (C=\mathbb E[\kappa(\phi(T))]<\infty), then (C^{-1}\kappa(\phi(T))\,GW(dT)) is invariant for the induced flow-rule Markov chain. The proof is a branching decomposition plus the algebraic identities; integrability is the normalizing condition, not automatic from the recursion.

## Biased harmonic measure

For a leafless, nondegenerate supercritical GW tree and a λ-biased walk in the transient regime λ<m, Section 4 (PDF pp. 14–19) specializes the flow to the escape probability β(T). Theorem 4.1 (PDF pp. 16–17) gives the harmonic-stationary density proportional to κ(β(T)) and the almost-sure dimension formula (Eq. (12)); the formula depends on the exact escape/conductance recursion. The paper’s finite-mean and integrability conditions are those used to normalize this density and apply the ergodic theorem. This is an explicit dimension formula, not a bias-monotonicity result.

## Recursive edge lengths and dimension drop

In §5 (PDF pp. 20–34), each vertex has an iid mark Γ>1 and the effective conductance variable is φ(T)=Γ∅β(T), satisfying the recursion with (h(u,v)=uv/(u+v-1)) on (J=(1,\infty)). Proposition 5.1 (PDF pp. 21–22) supplies sufficient tail/moment conditions for the needed κ(φ(T)) integrability: if (P(\Gamma\ge s)\le Cs^{-a}), then the paper’s three cases are (a>1); (a=1) and (\sum_kp_k k\log k<\infty); or (0<a<1) and (\sum_kp_k k^{2-a}<\infty).

Theorem 5.2 (PDF pp. 24–25) gives the natural genealogical metric dimension formula and strict dimension drop below log m unless both offspring and mark laws are degenerate, under (C<\infty). Theorem 5.8 (PDF pp. 32–33) treats the mark-dependent boundary metric (d_\Gamma): if (C<\infty) and (\sum_kp_k k\log k<\infty), the harmonic flow is exact-dimensional with the displayed deterministic formula; it has dimension zero in the stated (\mathbb E[-\log(1-\Gamma_{\varnothing}^{-1})]=\infty) case, and otherwise gives strict dimension drop below the Malthusian dimension α unless both laws are degenerate. These results concern dimension for a fixed random-tree metric, not monotonicity in λ.

## Reading coverage

Complete PDF read: introduction and marked-tree setup, §1 (PDF pp. 1–5); flow-rule recursion/algebra, §2 (pp. 5–10); invariant-measure theorem/proof, §3 (pp. 10–13); λ-biased harmonic measure, §4 (pp. 14–19); recursive-length trees and metric dimensions, §5 (pp. 20–35); bibliography (pp. 36–37). Physical PDF pages are cited.

## Scope boundary

The invariant-density mechanism is reusable only after checking the algebraic (h)-identities, the marked-GW recursion, and finite normalizing constant (C). Natural and mark-dependent metrics are distinct. Dimension-drop statements do not establish comparison or monotonicity across different biases; B076 remains unresolved by this source.
