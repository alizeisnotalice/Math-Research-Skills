# Disjoint probability-tree covering

Source: OpenAI, *The second Kahn-Kalai conjecture*, SHA-256 \`dd0c26b99de9e1d01d25f9b646a1fca1cd92fe34180ba7e5042ddcf91b61eb85\`, physical pp. 4-9, transition (2.2)-(2.3), Theorem 3.1 and Lemma 3.2.

At a transition choose a source \(c\), set \(Y=W\cup A_c\), choose target \(b\) with mass proportional to
\[
\nu_b\rho^{-|A_b|}\mathbf1_{\{A_b\subseteq Y\}},
\]
and retain \(T=A_b\setminus W\).  The two recorded invariants are \(T\subseteq A_c\cap A_b\) and \(A_b\subseteq W\cup T\).

The stated theorem assumes a finite disjoint probability tree, \(\sigma\)-spread levels, and positive capacities \(\ell_{i+1}\ge16\ell_i\).  With \(r=\min\{1,16e^{50}\sigma(1+\log_2\ell_k)\}\), it gives probability at least \(2/3\) that a product sample contains one path's label union.  The reduction lemma halves capacities while preserving recovery.  Do not drop disjointness, spread, growth, or finiteness.

## 固定来源

- 物理页 4, 5, 6, 7, 8, 9。Transition (2.2)-(2.3); Theorem 3.1; Lemma 3.2 SHA-256 `dd0c26b99de9e1d01d25f9b646a1fca1cd92fe34180ba7e5042ddcf91b61eb85`。[The second Kahn–Kalai conjecture](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-second-Kahn-Kalai-conjecture-September-24-2026/paper.pdf)
