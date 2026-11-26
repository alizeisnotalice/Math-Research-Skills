---
name: math-finite-graph-family-witnesses
description: Reproduce exact finite graph-family witnesses for triameter/peripherality and decorated-tree independence-polynomial sign separation.
---

# Finite graph-family witnesses

Use this skill for the two source-level finite tasks below.

```sh
python3 -B scripts/check_hko.py --example g1
python3 -B scripts/check_hko.py --example g2
python3 -B scripts/check_decorated.py --family 2
```

The HKO check computes distances, diameter, peripheral vertices, triameter triples, medianity, and (for the eight-vertex example) distance-heredity by all connected induced subgraphs. The decorated-tree check uses the printed transfer recurrence and exact rational evaluation at `-1/10` and `-1/6` for the `A^jB^(m-j)` finite family.

These are finite witness checks. They do not establish HKO minimality/uniqueness, the distance-hereditary structural theorem, arbitrary tree antichains in the independence-polynomial order, the root-interval lemma, or any claimed Lean artifact.

## 文献复核采用的构件

- [Source note: decorated-tree polynomial signs](references/decorated-tree-sign-witnesses.md)
- [Source note: HKO finite witnesses](references/hko-explicit-witnesses.md)
