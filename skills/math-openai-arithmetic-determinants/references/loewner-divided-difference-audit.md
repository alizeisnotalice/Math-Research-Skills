# Löwner 差商、原子 Gram 特例与非零性：适用范围审计

本页只抽取 Sean Litsey 的 Löwner 行列式构造中可单独复核的有限构件。它不是对原文全部不等式、指数、数值证书、Lean 工件或任何常数无理性的背书；尤其不把其 digamma/trigamma 构造转移成欧拉常数 \(\gamma\) 的构造。

## 1. 差商与 Hermite 表示的精确输入

令 \(T\) 为有限个**互异**点，且 \(F\) 在它们的邻域解析。原文定义 Löwner（差商）矩阵

\[
 L_F[t,t']=
 \begin{cases}
 \dfrac{F(t')-F(t)}{t'-t},&t\ne t',\\[4pt]
 F'(t),&t=t'.
 \end{cases}
\]

若一条正向简单闭曲线包围全部节点，且 \(F\) 在闭曲线及其内部的一个邻域全纯，则 Hermite 公式为

\[
 L_F=\frac1{2\pi i}\oint F(z)\,v(z)v(z)^{\mathsf T}\,dz,
 \qquad v_t(z)=\frac1{z-t}.
\]

这是解析恒等式，要求的是节点附近解析性和所述轮廓条件；它本身既不说明正定性，也不说明行列式非零。

原文第 3 节用于整数节点的进一步、且更专门的输入为一个 *frame*

\[
 F(z)=\sum_{s\in S}\bigl(w_s\psi(z+s)+w'_s\psi'(z+s)
              +w''_s\psi''(z+s)\bigr),
 \qquad \sum_{s\in S}w_s=0,
\]

其中 \(S\subset\mathbb Q\cap(0,1]\) 有限、所有系数有理且并非全零。令每个移位的极阶按原文定义，并令 \(d\) 是总极阶；平衡条件给出 \(F(z)=O(|z|^{-1})\)（右半平面）。设

\[
 \xi=F'(0),\quad
 \delta(z)=F(z+1)-F(z),\quad
 f_t=\sum_{k<t}\delta(k),\quad e_t=-\sum_{k<t}\delta'(k).
\]

对非负整数节点，原文的恒等式是

\[
 L_F=M+\xi I,
 \quad M[t,t']=\frac{f_{t'}-f_t}{t'-t}\ (t\ne t'),
 \quad M[t,t]=-e_t.
\]

这一步把可变常数放在公共节点的对角线上；有理性来自所给 frame 的有理移位和离散递推，不能脱离这些输入照搬。

## 2. 原文的测度不是正 Gram 测度

原文把 Hermite 轮廓向左移动后，得到

\[
 L_F[t,t']=\int v_t(z)v_{t'}(z)\,d\Omega(z).
\]

这里 \(\Omega\) 是**复测度**：穿过的 \(F\) 的极点带质量 \(-\operatorname{res}_yF\)，而轮廓 \(\Gamma\) 上还带密度 \((2\pi i)^{-1}E(z)\,dz\)。因此它可作为双线性积分表示，但一般不是正测度；矩阵也可以是矩形的 \(L_F[R,Q]\)。原文在这一处使用双族 Andréief 恒等式和绝对值上界，而没有由正半定性推出一般行列式非零。

下面的正 Gram 分解是可复用的**有限正原子特例**，不是对上述 \(\Omega\) 的额外断言。

## 3. 有限正原子核的 Gram 与严格非零条件

取实节点 \(t_1,\ldots,t_n\) 两两不同，实原子 \(z_1,\ldots,z_N\) 两两不同且均不等于任一 \(t_i\)，并取严格正权重 \(a_\ell>0\)。定义

\[
 K_{ij}=\sum_{\ell=1}^{N}
 \frac{a_\ell}{(z_\ell-t_i)(z_\ell-t_j)}.
\]

令 \(V_{i\ell}=(z_\ell-t_i)^{-1}\) 与 \(A_{i\ell}=\sqrt{a_\ell}V_{i\ell}\)，则

\[
 K=AA^{\mathsf T}=V\operatorname{diag}(a_1,\ldots,a_N)V^{\mathsf T}.
\]

故 \(K\succeq0\)。更精确地，Cauchy--Binet 给出

\[
 \det K=
 \sum_{J\subset\{1,\ldots,N\},\ |J|=n}
 \left(\prod_{\ell\in J}a_\ell\right)
 \det(V_{[:,J]})^2.
\]

在以上“节点互异、原子互异、原子避开节点、权重严格为正”的假设下，若 \(N\ge n\)，每个 \(n\)-原子子矩阵都是 Cauchy 矩阵，故其行列式非零；于是 \(\det K>0\)。若权重有符号/复数、原子落在节点、或行列数不匹配，则这个严格正性结论不可使用。

## 4. 已实际执行的精确有限复放

本机以 Python 3.15.0 的 `fractions.Fraction` 计算了上述特例，取

\[
 (t_1,t_2)=(0,1),\qquad
 (z_1,z_2,z_3)=(-1,-2,-4),\qquad
 (a_1,a_2,a_3)=(2,3,5).
\]

逐项有理运算得到

\[
 K=\begin{pmatrix}49/16&7/4\\7/4&31/30\end{pmatrix},
 \qquad \det K=\frac{49}{480}>0.
\]

Cauchy--Binet 三项（按原子对 \((-1,-2),(-1,-4),(-2,-4)\)）依次为

\[
 \frac1{24},\qquad\frac9{160},\qquad\frac1{240},
\]

其和恰为 \(49/480\)。这是对有限 Gram 恒等式和严格正性的精确复放；它不复放原文的复测度、轮廓估计、分母估计或任一全局指数。

## 5. 原文的非零性机制与不可替代条件

原文的实际非零性不是第 3 节的正定论证。对上述 frame、几何 \(G(r,m)\) 和每个有理 \(x_0\)，Theorem 5.6 的结论是：若

\[
 r\ge\max(1,d-2),
\]

则存在公共节点的删除集 \(I\)，满足 \(|I|\le\lfloor d/2\rfloor\)，使相应的方阵行列式 \(P_{r,I}(x_0)\ne0\)。证明路线是：

1. 将左右核识别为一对低次多项式 \((u,w)\) 的值与 Hermite 插值条件；
2. 用交叉积 \(w_1u_2-w_2u_1\) 的零点计数控制该空间；
3. 对 \(D=\prod_s(z+s)^{\nu_s}\)、\(A=D\delta\)，使用活跃极点 \(a=-s_0\) 处 \(A(a)\ne0\) 排除“短”解；
4. 由可见性选择至多 \(\lfloor d/2\rfloor\) 个公共节点删除，得到非奇异主限制。

因此，对一个新核只验证了有限 Gram 行列式为正，不能替代原文的插值、极点隔离、次数和删除选择证明；反过来，Theorem 5.6 也不宣称一般 \(L_F\) 是正定。

## 6. 与欧拉常数的边界

此文的核心常数是 \(\xi=F'(0)\)：例如 \(F_s\) 给出 \(-q^{-2}\Psi(s,1)\)，第二、三类 frame 给出 \(\zeta(3)\)、\(\pi^2\)、\(\pi^4\) 的组合。虽然 \(\psi(1)=-\gamma\)，这里的平衡 digamma 组合使用差分，且论文实际提取的是导数值或导数差；第 3 节的 \(\xi\) 中没有孤立的 \(\gamma\)。

更直接的障碍是：对每个正整数 \(m\)，

\[
 \psi(m)=H_{m-1}-\gamma.
\]

所以以整数节点取 \(\psi\) 的任何至少一阶**纯差商**都会消去共同的 \(-\gamma\)；重复节点的 Hermite 延拓只是导数，同样不会恢复该常数。故纯整数节点的 \(L_\psi\) 要研究 \(\gamma\)，必须额外加入一个锚定函数值或另有已证明的机制。这个消去结论仅适用于同一 \(\psi\) 在未分别缩放的整数节点上的共同常数项；不能擅自推广到各节点分别缩放、不同函数或不同归一化的情形。

因此不能从本页得到 \(\gamma\) 的有理线性形式、整数性、余项衰减或无理性。若要为 \(\gamma\) 设计类似路线，至少须另外给出：(i) 含 \(\gamma\) 的 \(L_F=M+\xi I\) 分解且 \(M\) 的算术可控；(ii) 对该 \(F\) 的全部极点/插值非零性假设；(iii) 同一归一化下的分母界和解析余项界。三项均不由 Litsey 的 trigamma 差分自动提供。

## 来源定位

Sean Litsey, *Irrationality measures from Löwner determinants*, `hexagon:2610.00401v3`，作者公开稿，73 页；公开 PDF 由 Hexagon Math 提供，未把它当作期刊正式发表版本。

- 固定 PDF：[hexagonmath.org/pdf/2610.00401](https://hexagonmath.org/pdf/2610.00401)
- 作者源码页：[slitsey/catalan-irrationality-measure, `paper-trigamma`](https://github.com/slitsey/catalan-irrationality-measure/tree/main/paper-trigamma)
- 本机语料固定 SHA-256：`c53187157e4e46ac2f75d33e55566fa727cfc218533916337c200ffad3f19c34`

页码定位：PDF 10 页 §2.1（差商与 Hermite），13--17 页 §3（frame、\(M+\xi I\)、几何），31--35 页 §5（Hermite 插值非零性），36 页 §6.1（复测度表示），36--38 页 §6.2--6.3（Andréief 与其用途）。
