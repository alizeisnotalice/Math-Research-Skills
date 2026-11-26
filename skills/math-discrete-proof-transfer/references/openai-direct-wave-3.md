# Periodic hitting sets from finite routing tables

## Dyadic scale version

Source: *The dyadic case of the Erdos similarity conjecture*, family 084, SHA-256 `7e7f6e576f6378978887e6f1043b550d7ea927fb31f29a3a65a7abf2ef29bbed`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-dyadic-case-of-the-Erdos-similarity-conjecture-September-25-2026/paper.pdf), physical pp. 4, 11--12, and 14; Lemma 2.1 and Lemma 5.1.

1. Input \(p\in(0,1)\), a finite ordered routing tree, separated index windows, nested periodic grid keys, and terminal tables independent of the center exposure.
2. On a fixed exposure atom, identify the first default node before revealing the remaining terminal entries. For any fixed normalized scale, the distinct terminal addresses give the product Bernoulli calculation.
3. List every grid-boundary scale in \([1,2]\), add endpoints and one midpoint in each complementary interval. Each local predicate is then constant on an open representative interval. Union-bound only after these representatives are fixed on the exposure atom; repair the residual center set by an open periodic neighborhood and the dyadic tail.
4. Output an open periodic \(H\) of density at most \(6p\) that hits each \(x+t2^{-n}\), for some \(n\ge1\), at every center and \(t\in[1,2]\).

## Geometric scale version

Source: *The geometric case of the Erdos similarity conjecture*, family 084, SHA-256 `a689fb6bbb9d545ae2aee377b0d19555d4c7ad14fb7e5ee0c2d69e6d7d17301e`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-geometric-case-of-the-Erdos-similarity-conjecture-October-5-2026/geometric-erdos-similarity.pdf), physical pp. 3--4 and 10--12; Proposition 2.1 and Lemma 5.1.

Use the same routing contract for a fixed \(q\in(0,1)\), but use nested dyadic grid resolutions comparable to \(q^{-b/(1-q)}\). At a local edge block of length \(r\), enumerate only its child-subtree boundary crossings; the source bound is \(D_{M,q}(r)=4+2(M-1)r(1+2c q^{-2r})\). Choose the branching parameter so the conditional terminal failure beats this representative count. Repair the remaining closed periodic center set using that \(tq^n\to0\).

The exact helper `../scripts/scale_representatives.py` audits the finite boundary/midpoint list for rational data. Boundary: it checks grid constancy cells, not routing-table independence, density selection, or the global similarity theorem.
