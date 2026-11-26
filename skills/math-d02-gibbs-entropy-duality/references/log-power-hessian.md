# 有限 log-power-mean：梯度、Hessian 与嵌套条件协方差

使用 D02 核验有限 Gibbs 倾斜和对数配分递推的导数。

## 来源与蒸馏范围

来源为 *The low-temperature Sherrington–Kirkpatrick fluctuation scale*，OpenAI Math 固定提交 `3344da59991ed94f9ba711217b29c1d760badfa6`，本地 SHA `e0e2e5e34169e701ff4bbd43736a3b9ea0dcee3c40606d78a36e844c86a3a4d9`。物理 pp. 6–7 的有限层级定义和 Lemma 2.1 给出本接口。

对有限倾斜算子

\[
 T_mF=m^{-1}\log\mathbb E[e^{mF}],\qquad m>0,
\]

若子节点导数为 \(g_i=\nabla F_i\)、\(H_i=\nabla^2F_i\)，倾斜子概率为 \(p_i\)，则

\[
 \nabla T_mF=\sum_i p_i g_i,\qquad
 \nabla^2T_mF=\sum_i p_iH_i+m\sum_ip_i(g_i-\bar g)(g_i-\bar g)^\top.
\]

有限树从叶到根反复应用该式，正是嵌套条件协方差传播。脚本要求每个内部节点提供正有理 `mass`、非负且和为一的有理 `tilted_probabilities`、以及声称的 gradient/Hessian；递推必须完全相等。零概率子节点允许，表示有限倾斜分布中的零质量分支。

## 近零与对称性

脚本另取输入的正有理 `near_zero_mass` \(\varepsilon\)，报告

\[
 \bar H+\varepsilon\operatorname{Cov}_p(g),
 \qquad
 \frac{H_m-\bar H}{m}=\operatorname{Cov}_p(g).
\]

后一个等式以精确有理数检验；前一个 Hessian 必须严格对称。替换质量时固定输入的倾斜权重与子节点导数。若研究实际 \(m\downarrow0\) 的渐近变化，还需计算随 \(m\) 变化的倾斜权重。

## 示例与限制

示例先以质量 \(1/1000\) 合并梯度 \((1,0)\) 和 \((-1,0)\)，再以质量 2 将该节点与梯度 \((0,2)\) 的节点按 \((2/3,1/3)\) 合并。根梯度为 \((0,2/3)\)，根 Hessian 为

\[
 \begin{pmatrix}167/500&0\\0&16/9\end{pmatrix}.
\]

```sh
python3 scripts/log_power_hessian_certificate.py \
  examples/nested-rational-log-power-hessian.json
```

该脚本不构造高斯增量、spin Gibbs 核或 Parisi 参数，也不推出 cavity 比较、低温尺度或任何渐近结论；它只认证调用方已经提供的有限倾斜导数数据。
