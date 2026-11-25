# 来源与复算范围

## Hessian 与二叉望远镜

- OpenAI, *An L³ Bound for the Dyadic Triangular Hilbert Form*, 固定版本 `openai/math@3344da59991ed94f9ba711217b29c1d760badfa6`，PDF pp. 3--4 的 Lemmas 2.1--2.2 与 Corollary 2.3，p. 8 的子节点条件平均和能量增量。SHA-256 `8e92ed5c9a2964956f01ed38b0dc88a849d6baaaf9cc593618e4f1103f2240a6`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-L3-bound-for-the-dyadic-triangular-Hilbert-form-October-5-2026/dyadic-triangular-hilbert.pdf)
- OpenAI, *The Maximal Triangular Hilbert Transform at the Symmetric Point*, 固定版本同上，PDF pp. 4--5 的 Lemmas 2.1--2.2，p. 18 的固定数组热流能量望远镜。SHA-256 `9dbcf9cb984bcf7b0809cc4221d119794ebca0e40027833ce9fe95b1e72c4247`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-maximal-triangular-Hilbert-transform-at-the-symmetric-point-September-24-2026/paper.pdf)

两文的具体 Hilbert-transform 结论使用额外的 mixed trace、条件随机化、Gaussian heat-flow 或多尺度分析。本技能仅复用其中给出且可在有限维重推的矩阵能量核。

## Trace Young

- OpenAI, *Equality Cases in the Sharp One-Dimensional Matrix Lieb--Thirring Inequality*, 固定版本同上，PDF p. 5, Lemma 2.2。SHA-256 `e88f3118d513e3133e672b809b58c6c7be43fcf09e802302ac0b569eeccd3298`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Equality-cases-in-the-sharp-one-dimensional-matrix-Lieb-Thirring-inequality-October-5-2026/sharp-one-dimensional-lieb-thirring-inequalities-matrix-potentials.pdf)

该条有限维不等式由在 \(Z\) 的特征基逐项作标量极大化，再对 \(t\mapsto t^p\) 严格凸性取迹得到。源论文的 Lieb--Thirring 等号分类含函数空间、作用泛函与谱步骤，不由本技能接受。

## 实际复算

`scripts/check_trace_energy.py` 用 Python 3 的 `decimal` 高精度执行一个二阶方向差分、一个非对角 Hermitian 方向的谱公式、一个二元树能量望远镜和两组 trace Young 检查。输出是这些有限维实例的数值一致性，不是源论文任一主定理的证明。
