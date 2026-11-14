# LPS2020IND — induced graphs of uniform spanning forests

**Source:** Russell Lyons, Yuval Peres, and Xin Sun, *Induced Graphs of Uniform Spanning Forests*, Annales de l’Institut Henri Poincaré, Probabilités et Statistiques 56(4) (2020), 2732–2744, DOI 10.1214/20-AIHP1056. Full reading of the 13-page published PDF, pp. 1–13. The formulas below were checked against the rendered PDF pp. 2–3 and 11–12; the exact PDF is `evidence/fulltexts/LPS2020IND.pdf`.

## The graph operation is part of every theorem

For a subgraph (Hsubseteq G), define its **induced-component graph**

\[
I_G(H):=\bigcup_{C\in\mathrm{Comp}(H)}G[V(C)].
\]

Thus (I_G(H)) has the same vertices and connected components as (H), but includes every ambient (G)-edge whose endpoints lie in the same (H)-component. The paper writes this operation with an overbar, (\bar H). It is not the original forest (H), and it can have many more edges. All recurrence, resistance, and resampling statements below concern this induced graph where indicated.

## Recurrence and resistance in the induced graph

- **Theorem 1.1 (PDF p. 2; proof pp. 7–8).** If (d\ge 8), almost surely every connected component of
  \[
  I_{\mathbb Z^d}(\mathrm{WSF}(\mathbb Z^d))
  \]
  is recurrent. This is not the already-known recurrence of the raw WSF tree: Morris's recurrence theorem for each raw WSF component is stated in the introduction as background. The proof works with the ambient edges added by (I_{\mathbb Z^d}). In the one-ended raw tree (T_o), cut the unique ray into bushes. The induced edges crossing a bush cut are precisely ambient lattice edges joining the corresponding bushes. Lemma 3.1 bounds expected numbers (N_{j,\ell}(n)) of such joining edges by marked-loop estimates; the return bound (p_t(o,o)\asymp t^{-d/2}) makes the required tail summable at (d\ge8). It yields disjoint cutsets (C_k) in (I_{\mathbb Z^d}(T_o)) with \(\sum_k |C_k|^{-1}=\infty\) almost surely. Nash–Williams then gives infinite effective resistance to infinity. Lemma 2.4 transfers the root-component conclusion to all components.
- **Theorem 1.3 (PDF p. 2; proof pp. 10–11).** For (v\in\mathbb Z^d), (d\ge9), with (T_v) the raw WSF component and \(\mathrm{Ray}_v(n)\) its unique raw-tree ray vertex,
  \[
  \liminf_{n\to\infty}\frac1n R_{\mathrm{eff}}^{\,I_{\mathbb Z^d}(T_v)}\bigl(v,\mathrm{Ray}_v(n)\bigr)>0\quad\text{a.s.}
  \]
  The resistance superscript is the induced graph. The proof uses a stationary two-sided LERW/WSF construction, which locally augments the target raw component by joining it to a second raw WSF component. Lemma 4.2 bounds the expected number of ambient lattice edges joining those two distinct raw WSF components by a sum controlled by \(\sum_t t(t+1)^2p_t(o,v)\), finite for (d\ge9). This controls the local discrepancy between the induced graph of the augmented component and the target induced component. Ergodicity along the stationary path gives positive density of cutset reciprocal-conductance contributions; Nash–Williams yields the linear liminf in the induced graph. The finite local modification is handled by Lemma 2.2, and Lemma 2.4 (tail component property) upgrades the positive-probability estimate to the root-component a.s. statement.

## Resampling identity on the induced-component graph

- **Definition (PDF p. 3; proof p. 11).** If (F_w(G)) or (F_f(G)) is first sampled, the paper next samples a spanning forest independently on each component of its induced-component graph. Its notation (\mathrm{FSF}(F_w(G))) is shorthand for (\mathrm{FSF}(I_G(F_w(G)))), not FSF on the raw tree edges.
- **Theorem 1.5 (PDF p. 3; proof pp. 11–12).** For every locally finite, infinite, connected graph (G),
  \[
  \mathrm{FSF}\!\left(I_G(F_w(G))\right)=\mathrm{WSF}(G),\qquad
  \mathrm{FSF}\!\left(I_G(F_f(G))\right)=\mathrm{FSF}(G).
  \]
  In finite volume, condition on the induced-component graph (K_{m,n}=I_{B_G(o,m)}(F_w^n\cap B_G(o,m))): every spanning forest that connects each component of (K_{m,n}) extends to a spanning tree of (B_G(o,n)) in the same number of ways. Thus the conditional law is the uniform spanning forest on (K_{m,n}). Couple restrictions as (n\to\infty), then exhaust the induced graph as (m\to\infty); the resulting FSF law is WSF on (G). The free identity is proved analogously. The induced graph operation must remain inside both resampling arguments.
- **Corollary 1.6 (PDF p. 3).** (\mathrm{WSF}(I_G(F_w(G)))=\mathrm{WSF}(G)) iff each component of (I_G(F_w(G))) has FSF equal to WSF.
- **Corollary 1.7 (PDF p. 3; proof p. 12).** If every component of the raw (F_w(G)) (respectively raw (F_f(G))) is one-ended, then
  \[
  \mathrm{WSF}(I_G(F_w(G)))=\mathrm{WSF}(G)
  \quad\text{(respectively }\mathrm{FSF}(I_G(F_f(G)))=\mathrm{FSF}(G)\text{).}
  \]
  For the wired assertion, Theorem 1.5 gives a coupling in which the resampled forest is a subforest of the original WSF. It has infinite components; a one-ended tree has no proper infinite spanning subtree, so the two forests agree.

## Counterexample boundary

The paper explicitly warns that neither \(\mathrm{WSF}(I_G(F_f(G)))=\mathrm{FSF}(G)\) nor \(\mathrm{WSF}(I_G(F_f(G)))=\mathrm{WSF}(G)\) holds for every graph (PDF pp. 3, 12). In the latter counterexample, (G) is two copies of \(\mathbb Z^5\) joined by a bridge. The induced component graph (I_G(F_f(G))) omits ambient edges carrying nonzero wired current; Thomson's principle then gives a strict change in wired edge-inclusion probability. Do not replace (I_G(F_f(G))) by the raw free forest in this argument.

For \(\mathbb Z^d\), Theorem 1.4 records the special identity \(\mathrm{WSF}(I_{\mathbb Z^d}(F_w(\mathbb Z^d)))=\mathrm{WSF}(\mathbb Z^d)\). It follows from Corollary 1.6 and the fact that on transitive amenable graphs FSF=WSF on each invariant random-subgraph component; this is a separate self-resampling statement, not a claim that the original raw WSF trees have changed edges.
