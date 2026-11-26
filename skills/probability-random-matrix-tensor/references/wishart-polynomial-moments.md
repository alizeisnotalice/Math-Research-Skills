# Wishart 主子式的整数阶矩

输入正定有理协方差 \(\Sigma\)、自由度 \(\alpha\) 和若干给定主子式及非负整数幂，计算
\(\mathbb E\prod_s \det(W_{I_s,I_s})^{r_s}\)。使用中心 Wishart 约定 \(\mathbb E W=\alpha\Sigma\)。任意非负整数 \(\alpha\) 用高斯样本构造，允许 \(\alpha<p\) 的奇异律。非整数自由度要求 \(\alpha>p-1\)，其中 \(p\) 是协方差维数。

## 独立的降阶递推

先对整数 \(\alpha=n\) 写 \(W_{ij}=\sum_{\ell=1}^n X_{\ell i}X_{\ell j}\)，其中各行独立且为 \(N(0,\Sigma)\)。对第一因子中的 \(X_{\ell i}\) 做高斯分部积分。导数落到 \(X_{\ell j}\) 时给出 \(n\Sigma_{ij}\) 项。落到其余任一 \(W_{ab}\) 时给出 \(\Sigma_{ia}W_{jb}+\Sigma_{ib}W_{ja}\)。于是
\[
\mathbb E[W_{ij}P(W)]=\alpha\Sigma_{ij}\mathbb E P(W)+
\sum_s \mathbb E[(\Sigma_{ia_s}W_{jb_s}+\Sigma_{ib_s}W_{ja_s})
 \prod_{t\ne s}W_{a_t b_t}],
\qquad P(W)=\prod_s W_{a_s b_s}.
\]
各项的总次数下降一阶，空积为 1。

对全秩的中心 Wishart，生成函数是 \(\mathbb E e^{\operatorname{tr}(TW)}=\det(I-2\Sigma T)^{-\alpha/2}\)，在 \(T=0\) 的邻域成立。它可从密度中的指数项变换得到。将 \(\Sigma^{-1}\) 换成 \(\Sigma^{-1}-2T\) 后，通过正定矩阵合同变换比较两个归一化常数。对称矩阵上的合同变换 \(X\mapsto A X A^{\mathsf T}\) 的 Jacobian 为 \(|\det A|^{p+1}\)，在对角坐标中可直接求得。展开 \(\exp[-(\alpha/2)\log\det(I-2\Sigma T)]\) 可见每个有限阶矩都是 \(\alpha\) 的多项式。递推等式在所有充分大的整数自由度成立，故在整个全秩实参数范围成立。非对角项若从生成函数提取系数，要使用 \(T_{ij}=t_{ij}/2\)。

脚本展开给定主子式多项式，按降阶式精确计算有理矩。块可以重叠。零次幂视作 1。若整数自由度小于任一正幂主块的维数，该因子因样本秩不足而恒为零。运行成本随主块大小和总次数增长，适合小规模精确值和回归基准。非整数幂及一般下正交事件依赖另行论证。

~~~sh
python3 scripts/wishart_minor_moments.py examples/wishart-correlated-minors.json
~~~

示例的 \(\Sigma_{12}=1/2\)、\(\alpha=5/2\)，得到 \(\alpha^2+2\alpha\Sigma_{12}^2=15/2\)。

来源为 Gaunt–Ouimet 的 *On Wilks’ problem: Exact recursive formulas via Stein’s method for the joint moments of disjoint principal minors of Wishart random matrices*，本机 SHA-256 3064eb3b3db5eb0558e3df7579a72e51b14018874eb6b19f0caa8b1feeaffcad。物理页 4–5 的式 (3.1) 与 Theorem 3.1 使用 Wishart Stein 恒等式。这里直接导出有限多项式递推，独立于其引用的 Bailly 等的 Stein 刻画。[arXiv 固定稿](https://arxiv.org/abs/2607.03984v1)
