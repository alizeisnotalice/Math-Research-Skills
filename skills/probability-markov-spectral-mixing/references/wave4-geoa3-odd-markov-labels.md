# Odd labels on a finite reversible marked chain

**Source.** OpenAI, *Nontrivial Markov Type Forces Superreflexivity*, Lemma 2.3 and Theorem 1.1 proof, PDF pp. 3--5; SHA-256 `5df09ebb518ff529acd50e9325765d8f7301a2fa83891056681af7960be29709`.

## Input contract

Supply a finite marked chain whose edge probabilities satisfy detailed balance with a stationary distribution, an odd label `g(e*)=-g(e)` in a normed space `V`, and a Markov type-`p` bound with constant `K`.  The finite span of the labels may instead be finitely representable in such a space, with the same limiting constant.

## Reuse

Lift the edge walk to a sufficiently large finite lattice cube, reject boundary exits, and apply Markov type to the potential whose increments are the odd labels.  Letting the cube grow gives
`E ||sum_(i=1)^n g(E_i)||^p <= K^p n E ||g(E_1)||^p`.
The source combines this with its explicitly constructed finite chain with linear displacement to contradict non-superreflexivity when `p>1`.

This is not a spectral-gap or mixing estimate.  It requires a finite reversible marked chain and odd labels; it does not cover arbitrary nonstationary Markov chains or labels that are not antisymmetric on reversed edges.

## 固定来源

- 物理页 3, 4, 5。Proposition 2.2; Lemma 2.3; proof of Theorem 1.1 SHA-256 `5df09ebb518ff529acd50e9325765d8f7301a2fa83891056681af7960be29709`。[Nontrivial Markov Type Forces Superreflexivity](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026/paper.pdf)
