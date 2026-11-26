# 有限原子终端律的后验树与停止见证

本参考只实现 Bayraktar–Cox–Stoev 的有限原子化框架中可独立核查的有限部分。原件为 *Martingale Optimal Transport with Stopping*，本机 SHA-256 为 `295b0c9d7dce14c293d5ca962790e2f8092d44e03aff33f4f72146581ba75aae`。正式版为 [SIAM Journal on Control and Optimization 56(1), 417–433](https://doi.org/10.1137/17M1114065)，对应 [arXiv:1701.06231](https://arxiv.org/abs/1701.06231)。物理页 3 令终端律为有限集合 \(X_N=\{x_0,\ldots,x_N\}\) 上的原子测度，并把条件律 \(\xi_t\) 作为取值于单纯形的测度值鞅。其均值满足
\[
 M_t=\int x\,\xi_t(dx).
\]
物理页 6 的 Theorem 3.1 进一步在连续 Brownian 控制、作者的 admissible-control 集及边界条件下，把有限维值函数识别为收益在权重单纯形上的凹包络。

`scripts/check_finite_posterior_tree.py` 检查一个有限后验树。固定支持点后，每个节点给出条件终端律的权重，边给出条件转移概率。脚本验证
\[
  \xi_v=\sum_{v\to w}q_{vw}\xi_w
\]
的每个坐标，因此节点均值是精确有理离散时间鞅。给定节点上的停留标记后，它检查该规则随当前树节点可测，计算给定策略的期望收益和 \(\mathbb E M_\tau-M_0\)，并求该**提交树内**的有限 Snell 递推值。 同时逐坐标核对停止后验的期望等于根节点后验。

运行：

```sh
python3 scripts/check_finite_posterior_tree.py --self-test
python3 scripts/check_finite_posterior_tree.py certificate.json
```

JSON 根必须是对象，并需要 `support` 与 `nodes`。每个节点含 `id`、`weights`、`reward`、布尔 `stop`，以及 `children` 的 `id/prob`。未停止叶节点被拒绝，所有边概率严格正。已停止的叶节点可保留非退化后验，因为该提交的策略已在该信息集停止。若要接回原文的终端原子律，可在停止后按这个后验再抽取一个条件终端原子。

输出中的 `tree_restricted_snell_value` 只在给定有限树和给定奖励表上优化。它没有构造连续 Brownian 鞅、没有检查文章的可采纳控制和粘性边界条件，也没有证明 Theorem 3.1 或任意终端律的全局最优运输值。
