# Evaluation-image criterion and a perturbed quotient lift

**Source.** OpenAI, *Relative independence of the separable quotient problem*, Proposition 2.2 and Lemma 9.1, PDF pp. 4--5, 32; SHA-256 `77cc28d21bfb07f729a6e0e4ae85ff22fd32e7e2a24831e79a15e6db4acf54ad`.

## Input contract

For the criterion, let `X` be an infinite-dimensional real or complex Banach space and `F` a closed infinite-dimensional subspace of `X*`.  For the perturbation lemma, require a Banach space `E`, closed `Y subset E*` whose evaluation `E -> Y*` is an isometric isomorphism, `W=E*/Y`, quotient `Q`, and a bounded `B:E* -> W` with `||B||<=1/10`, `B*(W*) subset J_E(E)`, and `B(E*) subset B(Y)`.

## Reuse

Apply Proposition 2.2 exactly as an equivalence: `X` has a separable infinite-dimensional Banach quotient iff some such `F` has norm-separable evaluation image `R_F(X)`; `F` may be selected separable.  Under the second contract, form `ker(Q-B)`: Lemma 9.1 identifies its dual with `E` by restriction and proves `B(ker(Q-B))=B(Y)` using the convergent small-perturbation lifting series.

Do not replace separability of the evaluation image with separability of `F`, and do not omit either the bidual-range or `B(E*) subset B(Y)` condition in the perturbation construction.

## 固定来源

- 物理页 4, 5, 32。Proposition 2.2; Lemma 9.1 SHA-256 `77cc28d21bfb07f729a6e0e4ae85ff22fd32e7e2a24831e79a15e6db4acf54ad`。[Relative independence of the separable quotient problem](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Relative-independence-of-the-separable-quotient-problem-September-23-2026/paper.pdf)
