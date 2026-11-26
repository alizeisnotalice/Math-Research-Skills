---
name: math-l21-local-to-global-lattice-certificates
description: 用有限商模的主分解拼接指定局部整格，并核对乘子阶、最大阶饱和与局部单位陪集。适用于数域中的 order-ideal 或局部格计数。
---

# L21 · 局部到整体的格子证书

适用于一个数域的最大阶 `R`、其满秩子阶 `O`、分数 `R`-理想 `I` 已经给定，且要由局部形状恢复整体的满 \(\mathbb Z\)-格子。它处理的是 \(\mathbb Z\)-格子和 `O`-理想。不能把它们替换为 `R`-子模，也不能由一个任意有限商子群直接断言可逆性。

## 可认证的局部拼接

设 \(q=[R:O]\)，于是 \(qR\subset O\)。对每个有理素数 \(p\)，写
\[
 I_p=I\otimes\mathbb Z_p,\qquad R_p=R\otimes\mathbb Z_p,
 \qquad O_p=O\otimes\mathbb Z_p.
\]
先固定每个 \(p\) 上的生成元 \(I_p=\xi_pR_p\)。只接受局部数据
\[
 L_p=\xi_p t_pO_p,\qquad t_p\in R_p^\times.
\]
当 \(p\nmid q\) 时它自动等于 \(I_p\)。对有限的 \(p\mid q\)，将 \(L_p/qI_p\) 视为 \(I_p/qI_p\) 的子模。有限阿贝尔群的 primary decomposition 给出
\[
 I/qI\simeq\bigoplus_{p\mid q} I_p/qI_p.
\]
取给定局部子模的直和并逆像，便得到唯一的满 \(\mathbb Z\)-格子 \(L\subset I\)，且其完成正是指定的 \(L_p\)。这个拼接证书需要列出每个 \(p\mid q\) 的局部格和它在有限商中的像。它不能以“模 \(q\) 看起来相容”替代主分解。

在上述单位形状下，逐个局部检查给出
\[
 [I:L]=\prod_{p\mid q}[R_p:O_p]=q,
 \qquad RL=I.
\]
第二式来自 \(1\in O_p\)，故 \(R_pL_p=I_p\)，再比较全部完成。它是一个独立门槛。即使 \(L\) 的加法指数正确，若 \(RL\ne I\)，它也不能进入本入口的理想类参数化。

## 可逆性、陪集和均匀性

一个满分数 `O`-理想 \(J\) 可逆，当且仅当每个 \(J_p\) 都有 \(J_p=\eta_pO_p\)，其中 \(\eta_p\in K_p^\times\)。正向方向可以在半局部环的每个极大理想选生成元，再用 CRT 合成一个生成元并由 Nakayama 引理提升。反向方向则将
\[
 J^{-1}=\{a\in K:aJ\subset O\}
\]
完成化，得到 \((J^{-1})_p=\eta_p^{-1}O_p\)，因而 \(JJ^{-1}=O\)。

对固定 \(I_p\)，不同局部格由有限齐性空间
\[
 R_p^\times/O_p^\times
\]
参数化。稳定子确为 \(O_p^\times\)，因为 \(tO_p=O_p\) 蕴含 \(t,t^{-1}\in O_p\)。所以归一化 Haar 测度的推前是这个有限陪集空间的均匀分布。全局独立局部选择的计数为
\[
 \prod_{p\mid q}[R_p^\times:O_p^\times].
\]
这里的均匀性是给定 Haar 输入后得到的结论，不能在局部选择并非单位陪集时照搬。

## 反例门槛

以 \(R=\mathbb Z[i]\)、\(O=\mathbb Z+2\mathbb Zi\)、\(I=R\)、\(q=2\) 为例。两个单位平移得到
\[
 O=\mathbb Z\langle1,2i\rangle,
 \qquad iO=\mathbb Z\langle i,-2\rangle,
\]
它们均指数 2 且 `R`-饱和。反之
\[
 L_{\rm bad}=\mathbb Z\langle1+i,2i\rangle
\]
也有加法指数 2，却满足 \(RL_{\rm bad}=(1+i)R\ne R\)。它的模 2 线不能替代单位陪集的局部数据。运行 [精确例](scripts/check_z_i_order.py) 可复核这些指数和饱和性。

来源为 OpenAI 预印本 *Equidistribution of primitive quartic torus packets for arbitrary orders*，PDF pp. 6–7，Lemma 2.1。其全文的等分布、局部密度、Fourier 分析及筛法结论都需要额外工作，未由此技能认证。已固定的本机 PDF SHA-256 是 `95c2a937da74097afe5d155a412fa89a2c4560a8231f10c4230244a8c6bed0f5`。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Equidistribution-of-Primitive-Quartic-Torus-Packets-for-Arbitrary-Orders-October-5-2026/quartic-torus-packets.pdf)

**Integral-plane covolume certificate.** For a full-rank row lattice \(\Lambda\subset\mathbb Z^3\) of index \(I\), primitive \(y\), and \(g=\gcd(y\cdot b_1,y\cdot b_2,y\cdot b_3)\), the exact checker verifies \(\det(\Lambda\cap y^\perp)=I|y|/g\) using a unimodular kernel basis. It is a finite certificate only; see `references/integral-plane-covolume.md` and `scripts/check_plane_covolume.py`.
