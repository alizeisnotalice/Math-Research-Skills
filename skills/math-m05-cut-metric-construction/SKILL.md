---
name: math-m05-cut-metric-construction
description: 在有限树分解上拼接一致二元 cut law，或审查嵌套 cut 坐标图，核对边缘、零质量、重参数化与局部 L1 度量公式。
---

# M05 · 有限 cut-metric 构造

用于有限顶点集上的二元标签测度，需要把树分解的局部 law 拼成一个全局 cut 测度，或需要用高度与横向场构造嵌套标签集时。先说明目标只是一个有限 \(L_1\) 伪度量、边控制还是额外的分离下界。局部拼接本身不提供全局失真界或远距离分离。

## 树分解上的二元 law 拼接

设 \(T\) 是有限树，\(B_t\subseteq V\) 满足覆盖、每条图边同袋出现、以及每个顶点的出现袋构成连通子树。令 \(\Omega_R=\{0,1\}^R\)。输入每袋上的有限非负测度 \(\mu_t\)，先核对以下数据。

1. 所有 \(\mu_t\) 有同一总质量 \(m\)。对每条树边 \(ts\)，令 \(S=B_t\cap B_s\)，并逐个标签 \(a\in\Omega_S\) 核对 \((\mu_t)|_S(a)=(\mu_s)|_S(a)\)。
2. 空分离集采用 \(\Omega_\varnothing=\{\varnothing\}\)，其限制测度的唯一原子质量为 \(m\)。因此空分离集不是跳过一致性检查的理由。
3. 若 \(m=0\)，每袋 law 都是零测度。直接取 \(\rho=0\) 与 \(D=0\)，不写条件分布或分母公式。

当 \(m>0\) 时，可任选根袋，以 \(\mu_{\rm root}/m\) 抽样；对子袋，固定交集标签并按 \(\mu_s\) 的条件 law 抽取余下标签。运行交集性质保证子袋中此前已赋值的顶点恰为该交集。零质量交集标签从未被抽到，条件 law 不定义也无妨。

由归纳检查每袋边缘仍为 \(\mu_t/m\)。将概率 law 乘回 \(m\) 得 \(\rho_\mu\)。对所有分离集标签质量为正的完整标签 \(\omega\)，还可用
\[
 \rho_\mu(\omega)=
 \frac{\prod_{t\in V(T)}\mu_t(\omega|_{B_t})}
      {\prod_{ts\in E(T)}\mu_{B_t\cap B_s}(\omega|_{B_t\cap B_s})}.
\]
任一分母为零时，该完整标签的质量定义为零，不能约掉零因子。该无根表达式也用于复核换根不变性。若所有袋 law 在全局标签取反下对称，则 \(\rho_\mu\) 也对称。

全局 cut 伪度量为
\[
 D_\mu(u,v)=\rho_\mu\{\omega:\omega(u)\ne\omega(v)\}
 =\lVert \omega\mapsto\omega(u)-\omega(v)\rVert_{L_1(\Omega_V,\rho_\mu)}.
\]
若图边 \(uv\) 位于某袋且该袋的分离质量有已核上界，才可用三角不等式沿图路径传递该上界。分离下界需要额外机制，例如已独立核验的共同子测度、流或随机分割论证。

需要完整的拼接证明、零质量处理或精确有限检查时，读[树分解拼接](references/tree-gluing.md)，并运行 `python3 scripts/check_gluing.py`。

## 嵌套 cut 坐标图

在一个共同标签空间 \(\mathbb R\times\{-1,1\}\) 上，以测度 \(\tfrac12\,dz\) 乘均匀符号，定义
\[
 A_v=\{(z,\sigma):z<h(v)+\sigma\kappa P(v)\}.
\]
只在两个点使用同一组 \((z,\sigma)\) 时，才可得
\[
 \mu(A_v\mathbin\triangle A_w)
 =\frac{|\Delta h+\kappa\Delta P|+|\Delta h-\kappa\Delta P|}{2}
 =\max\{|\Delta h|,\kappa|\Delta P|\}.
\]
沿高度坐标，要求 \(P\) 通过所有识别或 switch，且 \(\kappa\operatorname{Lip}_{\rm vert}(P)<1\)。这使两条边界 \(h\pm\kappa P\) 严格递增，标签集在每列嵌套，且其对称差等于竖直长度。

若 \(P=\psi(h)\) 并且 \(\kappa\operatorname{Lip}(\psi)<1\)，可令 \(\phi_\sigma(H)=H+\sigma\kappa\psi(H)\)。每个 \(\phi_\sigma\) 是递增双射，变换 \(z'=\phi_\sigma^{-1}(z)\) 后可把同一批集合重写为零横向场的图。复核时还应检查推前测度仍是所需的 Lebesgue 边缘。该重参数化只保留同一点的集合，不能自动让不同旧图共享标签变量。

需要边界识别、重参数化或局部公式的证明时，读[嵌套坐标图](references/nested-charts.md)。

## 证据边界

两个接口均从 2026-09-23 的 OpenAI 预印本逐页核对。它们给出局部、有限构造。本文档不把相关论文的全局 \(L_1\) 嵌入、统一失真常数、随机图表持久性或流切割结论作为已随接口导入的结论。版本、SHA-256 与页码见[来源记录](references/sources.md)。
