# 奇割上的完美匹配律拼接

## 适用对象与结论

令 \(G=(V,E)\) 为有限无环无向多重图，\(|V|\) 为偶数；平行边保持不同标签。对真奇集 \(S\subsetneq V\)，令 \(C=\delta(S)\)，并令 \(G_1\) 保留 \(S\)、把 \(V\setminus S\) 收缩为一个新顶点，\(G_2\) 交换两侧。删去被收缩一侧的内部边；每条 \(C\) 中边在两个收缩图中保留其原标签。

记 \(P(H)=\operatorname{conv}\{\mathbf1_M:M\in\mathcal M(H)\}\)。若
\[
y_i\in P(G_i)\quad(i=1,2),\qquad (y_1)_e=(y_2)_e=:q_e\quad(e\in C),
\]
则存在 \(y\in P(G)\)，其两侧内部边坐标分别等于 \(y_1,y_2\) 的内部坐标，且 \(y_e=q_e\)（\(e\in C\)）。这是紧奇割 \(x(C)=1\) 的归纳分解所需的匹配律版本；即使不另行假定“紧”，上式的共同割边坐标已保证可执行此拼接。

## 可执行的共同随机性

从每个 \(y_i\) 任选一个均值为 \(y_i\) 的完美匹配随机变量 \(M_i\)。收缩顶点在每个完美匹配中恰被一条割边覆盖，因此
\[
\sum_{e\in C}q_e=1.
\]
先以 \(q_e\) 抽取带标签的割边 \(e\)。在条件 \(e\in M_i\) 下独立抽取两边的匹配；\(q_e=0\) 的条件分布无需定义。删去两个收缩顶点、把两份 \(e\) 换回原图中的同一条带标签边。所得边集覆盖 \(V\) 中每个顶点恰一次，故为 \(G\) 的完美匹配。

对任何内部边，条件期望再按 \(e\) 求全期望即还原该侧原边缘概率；割边边缘概率为 \(q_e\)。所以所得匹配律的均值正是上述 \(y\)。关键兼容条件是**逐条带标签割边**的同一分布，而非仅 \(y_1(C)=y_2(C)=1\)；后者不足以进行共同抽样。

## 精确有理数检验（已运行）

取两侧各三个顶点，割边为 \(c_{03},c_{14},c_{25}\)。在第一收缩图采用下列匹配律（括号内为概率）：

\[
\{c_{03},s_{12a}\}\,(1/8),\quad
\{c_{03},s_{12b}\}\,(3/8),\quad
\{c_{14},s_{02}\}\,(1/3),\quad
\{c_{25},s_{01}\}\,(1/6).
\]

在第二收缩图采用

\[
\{c_{03},t_{45a}\}\,(1/5),\quad
\{c_{03},t_{45b}\}\,(3/10),\quad
\{c_{14},t_{35}\}\,(1/3),\quad
\{c_{25},t_{34}\}\,(1/6).
\]

二者的割边律均为 \((1/2,1/3,1/6)\)。用精确 `Fraction` 实施上述条件独立耦合，六个全图匹配的概率和为 \(1\)，并逐边验证其边缘向量分别还原两侧输入律和共同割边律；没有浮点近似参与。复现核心为：对每对均含同一割边 \(e\) 的侧匹配赋概率 \(p_1(M_1)p_2(M_2)/q_e\)。

```python
from fractions import Fraction as Q
from collections import defaultdict

C = {"c03", "c14", "c25"}
L = [(frozenset(["c03", "s12a"]), Q(1, 8)),
     (frozenset(["c03", "s12b"]), Q(3, 8)),
     (frozenset(["c14", "s02"]),  Q(1, 3)),
     (frozenset(["c25", "s01"]),  Q(1, 6))]
R = [(frozenset(["c03", "t45a"]), Q(1, 5)),
     (frozenset(["c03", "t45b"]), Q(3, 10)),
     (frozenset(["c14", "t35"]),  Q(1, 3)),
     (frozenset(["c25", "t34"]),  Q(1, 6))]
def cut(M): return next(iter(M & C))
def marginal(law):
    ans = defaultdict(Q)
    for M, p in law:
        for e in M: ans[e] += p
    return dict(ans)
q = {e: marginal(L)[e] for e in C}
assert q == {e: marginal(R)[e] for e in C}
G = [(A | B, p * r / q[cut(A)]) for A, p in L for B, r in R
     if cut(A) == cut(B)]
assert len(G) == 6 and sum(p for _, p in G) == 1
for law in (L, R):
    for e, p in marginal(law).items(): assert marginal(G)[e] == p
```

## 已核对来源

本条是 **Lemma 2.1, “Gluing across an odd cut”**, 第 5--6 页的专用重述；已读取本机提取页，且其文献清单记录的 PDF SHA-256 为
`c0b726a089502900b6b0c6b26b3d024cc55c440ce5d4abc71584b2c9ffe2fae4`。

- OpenAI, *Entropy and Face Dimension of the Perfect-Matching Polytope* (2026-09-23), [固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Entropy-and-Face-Dimension-of-the-Perfect-Matching-Polytope-September-23-2026/main.pdf), Git commit `3344da59991ed94f9ba711217b29c1d760badfa6`, pp. 5--6, Lemma 2.1.

该来源允许平行边并要求标签保留；其图是假设为有限、无向、无环且顶点数为偶数。不要把本页当作任意图拼接、任意凸集合粘合，或只知割边总质量时的结论。
