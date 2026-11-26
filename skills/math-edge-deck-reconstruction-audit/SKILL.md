---
name: math-edge-deck-reconstruction-audit
description: 审计有限简单图的无标号单边删除卡组，精确比较候选反例并核对边重构定理的图类和密度门槛。适用于小图枚举、边卡组断言和来源结论的适用范围检查。
---

# 有限图边卡组审计

先固定图是否有限、无向、简单，卡片是否为删一条边后的同顶点集生成子图，以及比较是否按无标号同构类的多重集进行。将 [边卡组脚本](scripts/edge_deck_audit.py) 用于 \(n\le8\) 的精确卡组比较。每张卡通过枚举顶点置换规范化，输出保留卡型及其重数。

检查候选图 \(G,H\) 或恢复给定小图的非诱导嵌入数时，可执行：

```sh
python3 scripts/edge_deck_audit.py G.json --compare H.json
python3 scripts/edge_deck_audit.py G.json --pattern F.json
```

只有 `same_unlabelled_edge_deck=true` 且 `isomorphic=false` 才是该有限输入范围内的边卡组碰撞。输入不同的顶点数、重边、环、越界端点和大于 8 个顶点的图会拒绝。拒绝不表示图可重构。

对一般理论先检查原文的量词。Google Cogentic 2026-11-25 公开稿所述线性密度范围是 \(n\ge4\) 与 \(|E|\ge1000n\)。该条件不覆盖稀疏小图。二边图 \(2K_2\) 与 \(K_{1,2}\sqcup K_1\) 是同卡组而不同构的边界例。

需要从边卡组进入来源的证明路线时，先读 [来源与有限界](references/edge-deck-reconstruction.md)。它区分 Edge–Kelly 的有限子图计数、孤立点剥离、原文的全局密度结论，以及尚未随公开稿提供的 Lean 形式化。
