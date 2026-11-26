# 边卡组与 Edge–Kelly 计数

固定版本为 Google Research 仓库 `4a7bc8ab0bc7` 的 *Unconditional Edge Reconstruction of Simple Graphs of Linear Density*。用户下载件为 `10_Google_Cogentic_2026-11-25/PDF/06_edge_reconstruction.pdf`，47 页，SHA-256 为 `170b2fc1f241cc8325e0b5573d444e061b1b7bb8fb3083a3ac88cabd0ce4f196`。本轮采用 PDF 物理页 1–2 的卡组定义和经典小图例子，以及物理页 8 的 Lemma 2.2(1) 的 Edge–Kelly 双计数。[固定发布记录](https://github.com/google-research/google-research/commit/4a7bc8ab0bc7)

## 运行有限核验

图输入为 JSON 对象，`n` 给出顶点数，边端点取 \(0,\ldots,n-1\)。例如四环输入如下。

```json
{"n": 4, "edges": [[0, 1], [1, 2], [2, 3], [3, 0]]}
```

在该技能目录运行：

```sh
python3 scripts/edge_deck_audit.py examples/positive-cycle.json --compare examples/positive-cycle-relabelled.json
python3 scripts/edge_deck_audit.py examples/boundary-matching.json --compare examples/boundary-star-isolate.json
python3 scripts/edge_deck_audit.py examples/positive-cycle.json --pattern examples/single-edge.json
```

第一例的 `isomorphic`、`same_unlabelled_edge_deck` 均为真。第二例分别为假、真。\(2K_2\) 与 \(K_{1,2}\sqcup K_1\) 删去任一边后均得到 \(K_2\sqcup 2K_1\)。程序比较同一顶点数的图，枚举全体顶点置换，在 \(n\le8\) 上给出无标号规范编码。卡组保留重数。比较 \(n>8\)、含重边或含环时拒绝输入。

给定宿主 \(G\) 和图案 \(F\)，记 \(m=|E(G)|\)、\(e=|E(F)|\)，并以 \(\mathrm{inj}(F,G)\) 表示保持边的单射数量。每个嵌入在 \(m-e\) 张删边卡中存活，故当 \(e<m\) 时，
\[
\mathrm{inj}(F,G)=\frac{\sum_{x\in E(G)}\mathrm{inj}(F,G-x)}{m-e}.
\]
对无标号相同的卡按重数累计。脚本直接计算分子并核对整除。单边嵌入四环共有 8 个有序端点选择。若把四环自身作为图案，脚本因 \(e=m\) 而拒绝使用公式。需要非诱导子图副本数时，可再除以 \(|\operatorname{Aut}(F)|\)。

## 原稿中的整体范围

Theorem 1.1 声称有限简单无向图在 \(n\ge4,\ m\ge1000n\) 时可边重构。物理页 46 的结论还依赖 Propositions 6.5、7.3、8.4 的多尺度论证。其整体证明及 Lean 工程在本轮未独立核验。[六篇原稿索引](../../math-research/references/google-cogentic-2026-11-25.md)
