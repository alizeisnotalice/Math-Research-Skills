# Negative example: do not transfer a UST correlation theorem to an MST

On the finite graph obtained from (K_4) by replacing two opposite edges by triples of parallel edges, assign iid continuous labels and take the minimal spanning tree. For two distinguished nonincident parallel edges (e_1,e_2), Lyons–Peres–Schramm’s exact calculation gives

\[
\mathbb P(e_1\in T)=\mathbb P(e_2\in T)=\frac{331}{1260},\qquad
\mathbb P(e_1,e_2\in T)=\frac{109}{1575}.
\]

The joint-to-product ratio is (109872/109561>1): the edge indicators are positively correlated. The exact independent check enumerates all (10!=3{,}628{,}800) strict label orders; output is saved at `workers/W07/examples/verify_finite_examples.json`.

The graph carries the **minimal** spanning-tree measure, not the uniform spanning-tree measure. This example therefore does not refute A141. It shows why UST determinantal negative association cannot be transferred to MSTs.

For A141, another invalid shortcut is to cite negative association for increasing events on two disjoint fixed edge sets and conclude the BK inequality. BK asks for a union over pairs of disjoint, configuration-dependent witnesses. The fixed-coordinate negative-association statement does not control that union.
