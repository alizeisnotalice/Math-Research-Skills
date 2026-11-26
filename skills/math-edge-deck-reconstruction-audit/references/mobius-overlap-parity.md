# Möbius overlap parity for a deck-equal pair

## Pinned source and locus

Google Cogentic, *Unconditional Edge Reconstruction of Simple Graphs of
Linear Density*, fixed Google Research commit `4a7bc8ab0bc7`; local source
`10_Google_Cogentic_2026-11-25/PDF/06_edge_reconstruction.pdf`, 47 physical
pages, SHA-256
`170b2fc1f241cc8325e0b5573d444e061b1b7bb8fb3083a3ac88cabd0ce4f196`.

This add-on uses only physical pp. 8--9, Lemma 2.2(1): its double-counting
identity for spanning subgraphs, followed by Boolean-lattice Möbius inversion.
It does not use the paper's later density, spanning-tree, or multiscale claims.

## Finite adapter

For non-isomorphic labelled representatives \(G,H\) on the same vertex set
with equal unlabelled single-edge decks, put

\[
a_Z(S)=\#\{\sigma\in\operatorname{Sym}(V):
 E(G)\cap\sigma^{-1}(E(Z))=S\},\quad S\subseteq E(G).
\]

The cited argument gives

\[
a_G(S)-a_H(S)=(-1)^{m-|S|}|\operatorname{Aut}(G)|.
\]

For \(E_0\subseteq E(G)\), summing \(a_G(S)\) over \(S\supseteq E_0\)
also produces the directly enumerable permutation set
\(\Sigma_G(E_0)\). Consequently the source lower bound is
\(|\Sigma_G(E_0)|\ge2^{m-|E_0|-1}|\operatorname{Aut}(G)|\) when
\(|E_0|<m\), and the exact \(|\operatorname{Aut}(G)|\) bound at \(E_0=E(G)\).

The script exhaustively enumerates these quantities for \(n\le7,m\le10\).
It first checks deck equality and non-isomorphism, so it is a replay of the
conditional finite lemma rather than a reconstruction solver.

[固定版论文](https://github.com/google-research/google-research/blob/4a7bc8ab0bc770e71a259b7966c500496b99010a/cogentic_research_papers/edge_reconstruction/paper.pdf)。

从技能根目录运行

```sh
python3 -B scripts/edge_deck_mobius_overlap.py examples/matching.json examples/star-isolate.json
```
