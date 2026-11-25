# 模素数余秩的局部行列式估值

这是一个可独立复用的局部算术构件：以清分母后的矩阵在
\(\mathbb F_p\) 上的左核维数，降低一个有理行列式所需的 \(p\)-分母。
它不包含 Catalan 常数的构造、解析衰减、素数求和、非消失或无理性测度。

## 适用的矩阵接口

令 \(A_0,L\in M_n(\mathbb Q)\)，\(p\) 为素数，\(s\in\mathbb Z_{\geq0}\)，并令
\(z\in\mathbb Z_{(p)}\)（即 \(z\) 的分母不被 \(p\) 整除）。以下是必须逐项
证明的输入：

1. \(M=p^sA_0\in M_n(\mathbb Z_{(p)})\)；
2. \(p^sL\in pM_n(\mathbb Z_{(p)})\)，从而
   \(p^s(A_0+zL)\) 模 \(p\) 的约化就是 \(\bar M\)；
3. 已有一个秩/左核证书给出整数 \(0\le e\le n\) 及
   \[\operatorname{rank}_{\mathbb F_p}\bar M\le n-e.\]

则
\[
 v_p\!\left(\det(A_0+zL)\right)\ge e-sn. \tag{1}
\]
这里允许左式为 \(+\infty\)；若后续需要非零行列式，必须另行证明，不能由
该估值不等式推出。

**证明。** 对 \(\bar M\) 取一个秩分解并提升到 \(\mathbb Z_{(p)}\)，得
\(M=UV+pE\)，其中 \(U\) 有 \(n-e\) 列。把
\(p^s(A_0+zL)\) 写为 \(UV+pE'\)，按列多线性展开其行列式：含有多于
\(n-e\) 个 \(UV\) 列的项为零，其余各项至少含 \(e\) 个因子 \(p\)。故其
行列式的估值至少为 \(e\)，再除去 \(p^{sn}\) 即得 (1)。这也是 Smith
标准形的直接推论。

## 如何给出可审计的余秩证书

不应只报告数值 ``rank``。令 \(V\) 是有限维 \(\mathbb F_p\)-空间，
\(\iota:V\hookrightarrow\mathbb F_p^n\) 是显式线性单射，\(\Phi:V\to W\) 是
显式线性约束。若逐列验证
\[
 \iota(\ker\Phi)^T\bar M=0,
\]
则
\[
 \operatorname{corank}\bar M\ge \dim V-\operatorname{rank}\Phi. \tag{2}
\]
这是 rank--nullity，而不是对原有 \(\mathbb Q\)-矩阵非奇异性的证明。

常见的“只控制一个列块”版本同样是局部的。若 \(C\) 是 \(c\) 个列的集合，
并且只证明 \(\iota(\ker\Phi)^T\bar M_C=0\)，再对其余 \(n-c\) 个列的值
附加线性条件，则
\[
 \operatorname{corank}\bar M\ge
 \dim V-\operatorname{rank}\Phi-(n-c). \tag{3}
\]
实际使用时应保存 \(\iota\)、\(\Phi\)、所控制的列集和每个约化条目；从
“许多对称行看起来相关”不能直接跳到 (2) 或 (3)。

## 有限复放（仅审计阈值）

在 Python 3.15.0 以精确有理算术复算
\[
 M=\operatorname{diag}(1,1,5,5),\qquad p=5.
\]
行消元得到 \(\operatorname{rank}_{\mathbb F_5}\bar M=2\)，所以余秩为 \(2\)；
同时 \(\det M=25\) 且 \(v_5(\det M)=2\)。这正好达到 (1) 的 \(e=2\)
下界。该四阶例只核对局部线性代数阈值，并未复算原文的 Chebyshev 行、数位
公式或任意 \(N,p\) 的核证书。

## 原文中的特例与边界

Sean Litsey 的 *An irrationality measure for Catalan’s constant*，
§3.1--§3.3（PDF pp. 11--13），取 \(s=2\)、
\(M=p^2A_{0,N}\)。在其已证 \(p^2A_{0,N}\) \(p\)-整、\(L_N\)
\(p\)-整以及 \(z\in\mathbb Z_{(p)}\) 的条件下，原文的 Proposition 3.3
正给出
\[
 v_p(\Delta_N(z))\ge\nu_N(p)-2n,
\quad \nu_N(p)=\operatorname{corank}(p^2A_{0,N}\bmod p).
\]
其 §4.2（PDF pp. 17--18）的 Theorem 4.1 是 (2) 的一个具体核证书模板：
借助额外的数位公式和差分恒等式证明 \(\iota(\ker\Phi)\) 落在左核。pp. 20--22
的 Theorems 4.6、4.8 使用的正是 (3) 这类列块补条件的计数。那些数位公式、
Chebyshev 恒等式和所有参数范围均是独立前提；本页没有验证它们。

原文随后把这类局部收益并入公共分母（pp. 14--15）并声称一个关于 Catalan
常数的全局结论。该链条还需要所有素数区间上的余秩下界、公共分母、非消失、
解析衰减及比较准则。本构件不采用文中任何数值指数（包括 270），也不向欧拉
常数 \(\gamma\) 转移：对 \(\gamma\) 应先明确给出 \(A_0,L,s\) 和上述三项接口。

本页只完成了上述局部引理与有限阈值审计。文献作者声称其完整证明有 Lean
形式化；本次过程没有下载、构建或核验该 Lean 工程，因此不把该声称视为本页的
验证结果。

## 来源版本

本机归档对应 Sean Litsey，*An irrationality measure for Catalan’s constant*，
Hexagon `2610.00187v7`（目录记录为 2026-10-11），本地 PDF SHA-256：
`b283e8c7f3b5ca61695e40c8a0ca7862765959d25502c3d0ea4d1645de1df97a`。
主公开版本为 [Hexagon 摘要页](https://hexagonmath.org/abs/2610.00187) 与
[PDF](https://hexagonmath.org/pdf/2610.00187)；作者仓库的
[paper 目录](https://github.com/slitsey/catalan-irrationality-measure/tree/main/paper)
是本地文献索引列出的源码入口。引用页码均指该已钉住本地 v7 PDF。
