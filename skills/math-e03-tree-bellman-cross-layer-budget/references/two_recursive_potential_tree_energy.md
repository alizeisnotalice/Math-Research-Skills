# 两个递归势的有限树能量证书

## 原文与采用范围

来源为 OpenAI, *Midpoint convexity from two recursive potentials*, 2026-09-27
preprint；本机 `manuscript.pdf` 的 SHA-256 为
`649d9f5632eb0ab801cd8aeea8293633e37ec2b58b37ec280527b2e1794f9b2a`，
共 23 页。核读 PDF 第 3–8 页，特别是第 6 页 Lemma 3.1 的完整证明；固定版本的
[官方 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Midpoint-convexity-from-two-recursive-potentials-September-27-2026/manuscript.pdf)。本次未找到已发表版本；因此只把这个已核预印本的有限引理作为来源。

令有限根树根为 `o`，`J` 为一批叶。给定四个非负场
`P,Q,P',Q'`，每个内部结点 `s` 与每个场 `A` 须满足

```
A_s^2 >= sum_{c in ch(s)} A_c^2.
```

还须逐点满足 `P'-P=Q'-Q=d>=0`，每一个内部点的 `P` 或 `Q`（至少一个）
必须在上式取等，且每个 `b in J` 有 `P_b=Q_b=0`。则 Lemma 3.1 给出

```
sum_{b in J} d_b^2 <= [d_o(2P_o+d_o)(2Q_o+d_o)]^(2/3).       (E)
```

原文证明不是普通的树求和：若 `P` 在一个结点取等，令
`U=d(2P+d)`、`V=(2Q+d)^2`。`P'` 的超可加性结合 `P` 的取等给出
`U_s>=sum U_c`，而 `Q',Q` 的二范数三角不等式给出
`V_s>=sum V_c`；再以 Hölder 对 `U_c^(2/3)V_c^(1/3)` 求和。
若 `Q` 取等则互换二场。这正是“某一个取等”不能删除的原因。

此条与现有 `math-e03-tree-bellman-cross-layer-budget` 不重复：E03 的接口是到达质量下
的单势平均预算与终端势望远镜；(E) 没有转移概率或节点质量，而需要两个递归势、
平方聚合和局部 tightness。也不能从 (E) 自动得出论文的递归范数、完备化、
中点模或 AUC-renorming 结论（这些使用 PDF 第 3–8 页余下的专门构造）。

## 可复现实证书

`scripts/audit_two_recursive_potentials.py` 接收有限有理树；逐项精确检查树结构、
四个平方超可加不等式、共同缺陷、每点 tightness 和选定叶零边界。为避免将无理
`2/3` 次幂浮点化，它以完全等价的有理不等式

```
(sum_{b in J} d_b^2)^3 <= [d_o(2P_o+d_o)(2Q_o+d_o)]^2
```

验证 (E)。

正例使用根缺陷 1 与两个边界缺陷 `3/5,4/5`；由 `3^2+4^2=5^2`，两边均严格等于 1。
`positive_depth_two.json` 还保留了一个内部结点，以实际回放一次两层的局部传播。
负例令根的 `P=Q=1` 而子场为零，故二个 `P,Q` 不等式均严格，程序必须拒绝它；
即使其它代数关系看似良好，也不可调用 Lemma 3.1。
