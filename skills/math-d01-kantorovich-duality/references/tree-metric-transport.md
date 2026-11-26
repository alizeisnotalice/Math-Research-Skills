# 有限加权树上的精确输运证书

脚本 `scripts/tree_metric_transport_certificate.py` 只接收正边长、连通、无环的有限树，以及总质量均为 `1` 的有理数概率 `mu`、`nu`。它不接收一般图，也不搜索生成树。因此绝不把“某棵生成树”表述为原图的最优生成树。

令根为 \(r\)，非根顶点 \(x\) 的父顶点为 \(x^+\)，以 \(x\) 为根的子树为 \(T_x\)。记
\[
 \Xi_T(x)=\mu(T_x)-\nu(T_x),
\]

树度量的精确值为

\[
 W_{1,d_T}(\mu,\nu)=\sum_{x\ne r} w(x,x^+)\lvert\Xi_T(x)\rvert.
\]

脚本以 `Fraction` 计算该和；同时在子树内先配对可抵消的剩余供给和需求，输出一份完整耦合（含对角质量），逐行核对两个边缘。输出的势满足

\[
 u(r)=0,\qquad u(x)-u(x^+)=w(x,x^+)\operatorname{sgn}\Xi_T(x).
\]

程序逐条核对树边 Lipschitz 不等式。沿任意两点间的唯一路径求和即可得全局 Lipschitz 条件。其对偶值、耦合成本与切割和三者精确相等。这是对输入**树度量**的原始—对偶证书，而不是浮点近似。

运行示例：

```sh
python3 scripts/tree_metric_transport_certificate.py examples/tree-transport-positive.json
```

该例返回 \(W_1=11/4\)、势 \((u(r),u(a),u(b),u(c))=(0,2,-1,2)\)，并给出质量平衡的耦合。带三角形的 `tree-transport-cycle-rejected.json` 以退出码 2 被拒绝。

## 与 Bigot--Fredes 文献的边界

本机原件 SHA-256 为 `1916e2fb2533346280269931d57d1bca3945c09517b8abb63482dec0c6e189ea`，是 Bigot--Fredes, *Kantorovich Distance via Spanning Trees: Properties and Algorithms*, arXiv:2601.08396v1 (2026-01-13), 37 页。PDF pp. 8--9 的 Proposition 2.4--2.5 给出上述树公式、势和树边饱和；p. 10 Proposition 2.6 对**原图**还要求在全部生成树中最小化；pp. 17--18 Theorem 3.3 在弱非退化和最优树前提下再提升为原图势的结论。

arXiv 已有 v2（2026-11-23）；作者主页仍标为 preprint，未查得正式发表版本。因而本工具只复用可独立直接验证的树度量部分。若以后加入一般图模式，必须独立逐条核对原图每条边的 Lipschitz 不等式、给出该树达到图的下界/上界相等的见证，再使用原图最优性。 [所核原稿](https://arxiv.org/abs/2601.08396v1) · [修订记录](https://arxiv.org/abs/2601.08396v2)
