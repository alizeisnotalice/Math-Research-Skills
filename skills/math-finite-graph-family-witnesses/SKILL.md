---
name: math-finite-graph-family-witnesses
description: 核验显式有限图族的三直径、装饰树独立多项式、后继色路径与 Mycielski 张量图的奇窗口着色见证。
---

# Finite graph-family witnesses

Use these exact checks for a supplied graph, graph family, or colouring.

```sh
python3 -B scripts/check_hko.py --example g1
python3 -B scripts/check_hko.py --example g2
python3 -B scripts/check_decorated.py --family 2
```

The HKO check computes distances, diameter, peripheral vertices, triameter triples, medianity, and (for the eight-vertex example) distance-heredity by all connected induced subgraphs. The decorated-tree check uses the printed transfer recurrence and exact rational evaluation at `-1/10` and `-1/6` for the `A^jB^(m-j)` finite family.

These are finite witness checks. They do not establish HKO minimality/uniqueness, the distance-hereditary structural theorem, arbitrary tree antichains in the independence-polynomial order, the root-interval lemma, or any claimed Lean artifact.

## 文献复核采用的构件

- [Odd folded-window certificate for tensor products](references/odd-fold-window-certificate.md)
- [Successor-colour reachability on an edge deletion](references/successor-colour-paths.md)

- [Source note: decorated-tree polynomial signs](references/decorated-tree-sign-witnesses.md)
- [Source note: HKO finite witnesses](references/hko-explicit-witnesses.md)
