# 来源与核验定位

本 Skill 使用以下两份本机 OpenAI 预印本。二者均来自固定归档提交 `3344da59991ed94f9ba711217b29c1d760badfa6`，并以本机 SHA-256 识别。预印本状态意味着后续使用仍应核对实际需要的版本与证明步骤。

| 接口 | 文献与定位 | 本机 SHA-256 |
| --- | --- | --- |
| 树分解二元 law 拼接 | *L1 Embeddings of Graphs of Bounded Treewidth*, 2026-09-23, PDF p. 7, Lemma 2.2 与式 (2.3) | `13276d0ab77859c506912444eab88bd09e3a47fba8a8d1b4c0511740bfe80dbb` |
| 嵌套 cut 坐标图 | *Planar Graph Metrics Embed into L1 with Constant Distortion*, 2026-09-23, PDF p. 13, Lemma 3.1 与式 (5) | `11b3a102e7333bf836a1317d774647394e580a5078027d1b9153a0b7fbc9e0e5` |

固定在线来源分别为 [treewidth PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf) 和 [planar PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf)。本机副本相对 `Math_Research_Literature` 的路径分别为 `current/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf` 与 `current/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf`。

本轮直接核对的范围是上述两条局部引理、其证明和公式。树分解论文的远距离不确定性传输另依赖 Chlamtáč–Krauthgamer–Raghavendra 的对称 Markov flow 定理。平面论文的全局常失真结论另依赖其随机插值、图表持久性和跨尺度组合。它们均未作为本 Skill 的已核接口。
