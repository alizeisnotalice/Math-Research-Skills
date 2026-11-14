# MORRIS2003 — recurrence of wired spanning-forest components

**Source and read copy.** Ben Morris, “The Components of the Wired Spanning Forest are Recurrent,” *Probability Theory and Related Fields* 125 (2003), 259–265, DOI 10.1007/s00440-002-0236-0. Complete 7-page searchable PDF read, SHA-256 `379a9298e0669f5569891a4a6924021c34d01efd8566b6b9688e22c7003dc1f3`.

## Network and spanning-forest setup (§1; PDF pp. 1–4)

The network is an infinite graph with nonnegative edge conductances $C(e)$; the edge resistance is $R(e)=1/C(e)$, and network random walk traverses an incident edge proportionally to conductance. Finite weighted spanning trees have probability proportional to the product of their edge conductances. The free and wired spanning forests are limits of finite weighted spanning-tree laws using free exhaustion and wired boundary identification. For flows, the paper distinguishes free unit flows (convex combinations of finite source-to-sink paths) from wired unit flows (satisfying Kirchhoff’s node law, allowing flow to escape through infinity); Thomson’s principle identifies the energy-minimizing flow and effective resistance.

For a finite network and edge $e=(s,t)$, Lemma 4 (PDF p. 4) prints $C_G(s\leftrightarrow t)=1/\mathbb P(e\in T)$. This is valid after globally scaling the network so the fixed edge $e$ has $C(e)=1$; such scaling leaves the weighted tree law unchanged but scales effective conductance. Hence the general form is
\[
C_G(s\leftrightarrow t)=\frac{C(e)}{\mathbb P(e\in T)},\qquad R_{\rm eff}(s\leftrightarrow t)=\frac{\mathbb P(e\in T)}{C(e)}.
\]
Thus the displayed unit-edge formula must not be used unchanged for arbitrary conductances. Proposition 5 gives the conditional spanning-tree law after including $e$ by contracting it, or after excluding $e$ by deleting it. Theorem 6 (PDF pp. 4–5) exposes edges one at a time in a random spanning tree conditioned to contain $e$; at each step contract an exposed tree edge or delete an exposed non-tree edge (ignoring edges parallel to $e$). Normalize the fixed edge $e$ to unit conductance by a global rescaling, which preserves the tree law; then the conditional effective conductance $C_{G_n}(s\leftrightarrow t)$ is a martingale. The proof is the two-case conditional expectation identity using Lemma 4 and Proposition 5.

## Infinite-network extension and recurrence (§1.2; PDF pp. 4–6)

Lemma 7 (PDF p. 4) gives the wired infinite-network identity $C_G^W(s\leftrightarrow t)=1/\mathbb P(e\in F)$ in the same fixed-edge normalization, for $F\sim\mathrm{WSF}$. In general, $C_G^W=C(e)/\mathbb P(e\in F)$ and $R_{\rm eff}^W=\mathbb P(e\in F)/C(e)$. Theorem 8 (PDF p. 5) extends Theorem 6 to WSF and FSF: conditioned on $e\in F$, the corresponding sequence of wired (or free) effective conductances is a martingale. The infinite proof uses the finite-set exposure identity and the weak-limit forest law.

**Theorem 9 (PDF pp. 5–6).** Almost surely, every WSF component is itself distributed as the wired spanning forest on that component. To prove this, fix $e=(s,t)$ and suppose with positive probability that $e$ lies in a WSF component and that deleting it leaves transient components on both sides. Contract the exposed forest edges in finite exhaustions. The resistance between the two sides tends to zero, so the wired effective conductance tends to infinity, contradicting almost-sure finite convergence of the nonnegative conductance martingale from Theorem 8. Thus no WSF edge has two transient sides; the componentwise WSF identity yields the stated recurrence conclusion in the corollary.

**Corollary 10 (PDF p. 6).** If $\sup_e C(e)<\infty$, then every connected component of the WSF is recurrent for network random walk, almost surely. The proof says it suffices to rule out a transient bounded-degree tree whose WSF equals the whole tree. For that tree, a finite-energy unit flow to infinity gives an edge with flow strictly between zero and one; the two sides then yield wired endpoint resistance below the edge resistance $1/C(e)$, so that edge has positive probability of being absent from the WSF. The short proof states this reduction without further detail; retain Corollary 10’s stated uniform edge-conductance bound and do not strengthen it. In particular, it applies to bounded-degree unit-conductance graphs, and it is not asserted for arbitrary unbounded-conductance networks.

## Reading coverage and boundary

Complete physical PDF pp. 1–7 were read: introduction and model/electrical preliminaries (§§1–1.2, pp. 1–4); finite and infinite conductance martingales, recurrence proof, and corollary (pp. 4–6); references (p. 7). Rendered pp. 2 and 4–6 to verify $R(e)=1/C(e)$, the weighted-tree law, Lemma 4’s normalization, Theorems 6/8/9, and Corollary 10.

These are WSF statements. They do not prove recurrence of minimal-forest components or establish the WMSF one-endedness input in B067. The paper’s conclusion is recurrence of each WSF component, not transience or a claim about FSF components.
