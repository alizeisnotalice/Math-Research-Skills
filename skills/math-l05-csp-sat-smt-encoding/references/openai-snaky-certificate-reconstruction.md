# Bounded Maker-game certificate reconstruction

Source: OpenAI, *Snaky in 21 Maker moves*, SHA-256 \`e5ce107fdc4ec77fbbe2d3eab6babe6198e7160b0904462ae3fddfab0c88634c\`, physical pp. 3-7, Definition 2, Lemma 3 and Proposition 5.

The source gives a finite state representation and reconstructs its supplied Snaky strategy certificate in Proposition 5.  For any reimplementation, encode board coordinates, legal moves, player turn, terminal predicate, and the certificate successor relation.  Check each listed state has the stated turn and every nonterminal node has a legal successor, reporting the first failed state.

This is a bounded certificate workflow for the paper's board and rules, not a strategy claim for changed geometry, a different win condition, or another move limit.

## 固定来源

- 物理页 3, 4, 5, 6, 7。Definition 2; Lemma 3; Proposition 5 certificate reconstruction SHA-256 `e5ce107fdc4ec77fbbe2d3eab6babe6198e7160b0904462ae3fddfab0c88634c`。[Snaky in 21 Maker moves](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Snaky-in-21-Maker-moves-September-25-2026/article.pdf)
