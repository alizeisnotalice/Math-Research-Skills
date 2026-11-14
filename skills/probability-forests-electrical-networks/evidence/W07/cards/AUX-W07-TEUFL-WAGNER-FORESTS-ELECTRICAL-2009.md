# AUX-W07-TEUFL-WAGNER-FORESTS-ELECTRICAL-2009 — rooted forests and boundary electrical data

**Source and read copy.** Elmar Teufl and Stephan Wagner, “Spanning Forests, Electrical Networks, and a Determinant Identity,” *DMTCS Proceedings* vol. AK, FPSAC 2009, 847–858, DOI [10.46298/dmtcs.2699](https://doi.org/10.46298/dmtcs.2699). Read the complete 12-physical-page DMTCS PDF at `evidence/fulltexts/AUX-W07-TEUFL-WAGNER-FORESTS-ELECTRICAL-2009.pdf`, SHA-256 `fe7f2b09dd0cb9e6a7b17990ad244722017d729ad635d13c7d57641c99763172`. D05 checked acquisition identity only; W07 read the entire body and references. Rendered PDF pp. 2, 6, 7, and 10 to verify the conjecture coefficients, the Desnanot–Jacobi calculation, the electrical formula, and the tree-count recurrence.

## Rooted-forest determinant results (§§1–2; PDF pp. 1–6)

For a graph with Laplacian $L$, write $L(R)$ for the principal minor obtained by deleting rows and columns indexed by $R$. **Theorem 1 (PDF p. 1)** is the all-minors matrix-tree theorem in the unweighted formulation stated there: $r_G(R)=\det L(R)$ counts spanning forests whose roots are exactly $R$. **Theorem 2 (p. 2)** concerns a finite connected multigraph and a distinguished set $D$ of size $\theta$ on which the restricted automorphism action is the full symmetric or alternating group. For every $R\subseteq D$ with $|R|=k$,
\[
r_G(R)=k\rho^{k-1}\theta^{1-k}t(G),
\]
where $\rho$ is the resistance-scaling factor relative to $D$ and $t(G)$ is the spanning-tree count. The symmetry hypothesis and finite connected graph setting are essential to this stated formula.

**Conjecture 3 (PDF p. 2)** proposes, for a possibly weighted and possibly disconnected graph, an identity relating $r_G(R)t(G)^{|R|-2}$ to a sum over graphs on $R$ with $|R|-1$ edges whose components are paths, isolated vertices, or cycles (including a two-edge 2-cycle). The coefficient factors are $2^{1-\ell}$ for a path of positive length $\ell$, $-2^{1-\ell}$ for a cycle of length $\ell>2$, $1$ for an isolated vertex, and $-1/4$ for a 2-cycle. The general identity is explicitly left conjectural. The three-terminal case is proved: for arbitrary vertices $v,w,x$ in the unweighted graph statement,
\[
\begin{aligned}
r(\{v,w,x\})r(\{v\})={}&\tfrac12\bigl(r(\{v,w\})r(\{v,x\})+r(\{v,w\})r(\{w,x\})+r(\{v,x\})r(\{w,x\})\bigr)\\
&-\tfrac14\bigl(r(\{v,w\})^2+r(\{v,x\})^2+r(\{w,x\})^2\bigr).
\end{aligned}
\]
The combinatorial proof (pp. 3–5) takes two copies of $G$, identifies the three terminals, and extracts a coefficient of the spanning-tree polynomial; it partitions rooted-forest pairs into distinct-connection, cycle, and identical-copy cases, with the displayed coefficients canceling the latter two. The algebraic proof (pp. 5–6) uses zero row/column sums and symmetry of the Laplacian to derive a relation among minors, then applies Desnanot–Jacobi. Remark 2 (p. 6) reports verification of the general conjectural pattern for four and five boundary vertices by a more general identity; it does not prove Conjecture 3 for arbitrary $|R|$.

## Electrical networks and self-similar enumeration (§§3–4; PDF pp. 6–11)

Section 3 defines the weighted Laplacian for conductances $c(e)\ge0$, electrical equivalence with respect to a terminal set $D$, effective conductance, and effective resistance $\rho_{\rm eff}=c_{\rm eff}^{-1}$. In the unit-conductance connected-graph setting, equation (5) on PDF p. 6 gives
\[
R_{\rm eff}(u,v)=\frac{r_G(\{u,v\})}{t(G)}.
\]
For strongly symmetric terminal sets, Theorem 2 gives the analogous root-set counts. If two graphs are electrically equivalent relative to $D$, their normalized rooted-forest counts $r_G(R)/t(G)$ agree for $R\subseteq D$. **Conjecture 4 (p. 7)** asks whether all pairwise effective resistances on a complete graph determine its conductances uniquely; the authors derive the three-vertex formula but leave the general reconstruction question open.

Section 4 (PDF pp. 8–11) replaces self-similar subgraphs by electrically equivalent small terminal networks to enumerate spanning trees. For the modified Sierpiński sequence $T_n$, it derives
\[
t(T_{n+1})=\frac{196}{27}\left(\frac{15}{7}\right)^{3n}t(T_n)^6
\]
and an explicit iterated formula. A second sequence $U_n$ has a two-conductance recursion and asymptotic tree-count form; no simple closed form for its conductances is claimed. The arguments depend on calculating the effective boundary network at each replacement step.

## Full reading coverage and scope

All physical pages 1–12 were read, including references. `evidence/W07/reading_coverage.json` records §1/all-minors statement and conjecture (pp. 1–3), §2 two proofs (pp. 3–6), §3 electrical definitions and resistance link (pp. 6–7), §4 Sierpiński and modified self-similar enumeration (pp. 8–11), and references (pp. 11–12).

For A141 this is **auxiliary determinant/electrical context**: it supplies rooted-forest minor counts and a three-terminal identity, but it does not address configuration-dependent disjoint witnesses or prove a BK inequality for weighted UST. Keep Theorem 1’s unweighted statement, Theorem 2’s symmetry assumptions, the unit-conductance scope of equation (5), and the explicitly conjectural status of Conjectures 3–4 separate.
