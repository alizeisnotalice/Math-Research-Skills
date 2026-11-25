# 固定来源与核对边界

本技能的本地核对发生在 2026-11-25：对每份 PDF 重新计算 SHA-256，并以
`pdfinfo` 核对标题及页数；再读取下列页码的本地抽取文本。三项都在
`.local/literature-distillation/openai-inventory.jsonl` 标为 `catalogued` 且
`scholarly_review: pending`。`OpenAI/math` 固定到提交
`3344da59991ed94f9ba711217b29c1d760badfa6`；链接是固定提交而非浮动分支。

| 分类 | 本地 PDF 与校验 | 已读取、可供本技能使用的内容 | 明确未采纳 |
|---|---|---|---|
| A | *Finite Monoid Computations and a Uniform Generalized Star-Height Bound*, 44 页；SHA-256 `3bf9877aaa27427d668f5ae5b3e31396ed49079677956c6f2a9e83b872b4b405`；[固定 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026/Finite-Monoid-Computations-and-a-Uniform-Generalized-Star-Height-Bound-September-25-2026.pdf) | PDF p. 5 的 Lemma 2.2 给出 `D'⊆D⊆E` 的 split identity、量词和基例；同页 Lemma 2.3 给出仿射复合取线性部分的同词布尔恢复。 | 标题、摘要或其余章节的任何统一上界、构造完成性、表达式大小、算法或复杂度。 |
| B | *Generalized Star Height at Most Four*, 34 页；SHA-256 `01348808b4c54659991a80b928f143bac74c452ce3f4d9f8ed35581fdd0809f6`；[固定 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Generalized-Star-Height-at-Most-Four-September-25-2026/Generalized-Star-Height-at-Most-Four-September-25-2026.pdf) | PDF pp. 4–5 的 Lemmas 2.1–2.2：`E⊆Σ+` 前缀码、split 的精确表达式与 `R_{v,y+f}∩R_{0,f}` 的 affine recovery。 | 标题、摘要或其余章节的总体高度结论、局部 marker/timing 构造的完整正确性、效率或表达式大小。 |
| C | *Generalized Star Height at Most Three*, 38 页；SHA-256 `eeae440333d912abcc3b7b440c82ea5c7538f9bde75856e1f194d579c7d93fd9`；[固定 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Generalized-Star-Height-at-Most-Three-September-25-2026/article.pdf) | PDF pp. 6–7 的 Lemmas 2.1–2.3：同一 split identity、Boolean affine recovery 和齐次线性 lift。 | 标题、摘要或其余章节的总体高度结论、双 split/decoder 的完整证明、效率或表达式大小。 |

三者的 split/affine 页面相互印证，但这种文本核对不等同于对其整体论文证明的
同行评审或独立完成证明。本技能所作的唯一额外计算见
`../scripts/check_finite_instance.py`：它以一个有限玩具模型作精确枚举，不能升级为
一般结论。
