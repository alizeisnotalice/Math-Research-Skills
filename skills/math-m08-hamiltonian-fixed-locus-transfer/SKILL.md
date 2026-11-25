---
name: math-m08-hamiltonian-fixed-locus-transfer
description: 用有限阶或 involution Hamiltonian 映射上的不变小扰动，将干净固定子流形的固定点问题转为其上的临界点问题，并核验短周期排除与非退化块。
---

# M08 · Hamiltonian 有限阶固定子流形迁移

给定闭辛流形上的有限阶 Hamiltonian 映射，若要以固定子流形上的函数控制小扰动后的固定点，先验证下列数据。这个技能只给出局部固定点迁移。它不产生 Arnold 下界、稳定 Morse 数结论或任何来源论文的反例。

## 有限阶的固定点—临界点对应

令 \((M,\omega)\) 闭，\(A\in\operatorname{Ham}(M,\omega)\) 且 \(A^m=\mathrm{id}\)。设
\[
 F=\operatorname{Fix}(A)
\]
为闭嵌入子流形，并在每个 \(q\in F\) 满足 clean 固定集条件
\[
 T_qF=\ker(dA_q-I).
\]
对给定的 \(f\in C^\infty(F)\)，先任取延拓 \(\widetilde f\)，再作有限平均
\[
 K=\frac1m\sum_{j=0}^{m-1}\widetilde f\circ A^j.
\]
则 \(K\circ A=K\)、\(K|_F=f\)。平均微分
\[
 P_q=\frac1m\sum_{j=0}^{m-1}(dA_q)^j
\]
是投向 \(T_qF\) 的投影，所以
\[
 \operatorname{Crit}(K)\cap F=\operatorname{Crit}(f).
\]

令 \(B_s\) 是 \(K\) 的 Hamiltonian 流。闭性给出一个 \(\delta>0\)，使任意 \(0<t<\delta\) 时 \(B_t\) 的固定点恰是 \(X_K\) 的零点。这个短周期门槛必须在紧流形或已给全局统一局部 Lipschitz 和停留时间的同等设置下证明。因 \(A\) 与 \(B_s\) 交换，若 \(0<\varepsilon<\delta/m\)，则
\[
 (A\circ B_\varepsilon)^m=B_{m\varepsilon},\qquad
 \operatorname{Fix}(A\circ B_\varepsilon)=\operatorname{Crit}(f).
\]
证明固定点等式时，不能只从 \(A\circ B_\varepsilon(q)=q\) 推出 \(A(q)=q\)。先以幂等式得到 \(dK_q=0\)，再得 \(B_\varepsilon(q)=q\)，最后得到 \(A(q)=q\)。

## involution 的非退化检验

若 \(g^2=\mathrm{id}\)，在 \(x\in F=\operatorname{Fix}(g)\) 有
\[
 T_xM=E_+\oplus E_-,\quad E_+=\ker(dg-I)=T_xF,\quad E_-=\ker(dg+I).
\]
辛不变性使两个子空间辛正交且各自非退化。若每个连通分支上的 \(h\) 是 Morse 函数，取不变延拓 \(f\)。在 \(x\in\operatorname{Crit}(h)\) 处，线性化 \(L=dX_f(x)\) 保持这两个块。切向块由
\[
 \omega(L_+u,v)=\operatorname{Hess}_x h(u,v)
\]
可逆。对 \(\Phi_\varepsilon=\psi_\varepsilon\circ g\)，小正 \(\varepsilon\) 时
\[
 \frac{e^{\varepsilon L_+}-I}{\varepsilon}\longrightarrow L_+,
 \qquad -e^{\varepsilon L_-}-I\longrightarrow-2I,
\]
故 \(d\Phi_\varepsilon-I\) 可逆。若临界点集有限，取所有局部门槛的最小值。这一段要求 involution、Morse Hessian 和辛切向分裂。有限阶 \(m>2\) 的固定点对应本身不自动给出此非退化结论。

## 检查清单

- 核验 \(M\) 闭、映射本身为 Hamiltonian、阶数与 clean 固定集条件。
- 指明函数定义在每个固定分支上，延拓后再平均。仅有不变函数而没有给定的分支限制不足以得到想要的临界集。
- 对所选 \(\varepsilon\) 同时检查短周期门槛和所有临界点的块行列式。
- 若需要把复合映射表为一周期 Hamiltonian 时间一映射，拼接两个有端点平坦的 Hamiltonian 路径。一个映射是 Hamiltonian 并不自动给出所需固定点轨迹的收缩性质。

运行 [线性化复算](scripts/check_linearized_involution.py) 检查二维切向 Morse 块和二维法向反射块。该例只复核局部块行列式，不替代流形上的短周期论证。

## 固定来源和范围

- OpenAI, *Three fixed points on the symplectic quadric threefold*, PDF pp. 3–5, Proposition 2.1 和 Lemma 2.2，SHA-256 `bebf04613245ab3cd52f29724c9fe43e2943c07dfabd96fb21fd5394f175c474`。原文的 quadric 与三临界点构造不在本技能的默认结论内。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-degenerate-counterexample-to-the-critical-number-Arnold-bound-September-23-2026/paper.pdf)
- OpenAI, *Hamiltonian Fixed Points Below the Stable Morse Number*, PDF pp. 6–7, Proposition 3.2，SHA-256 `b482e3ec793c52e06a1a3f6cd92f13518a806511e2974cd4f9005eea116f5f0f`。只采用 involution 的分裂和非退化证明。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Hamiltonian-Fixed-Points-Below-the-Stable-Morse-Number-October-5-2026/paper.pdf)
- OpenAI, *Sharpness of the Cyclic Integral Floer Bound Below the Stable Morse Number*, PDF pp. 6–7, Lemma 3.1 和 Proposition 3.2，SHA-256 `b9fec0a6b56d3a8dd7ffe7ce53bfd6304e3a6560f98d0ee7f73812862b9a1c02`。它独立给出同一 involution 局部机制。循环 Floer 主张未被采用。[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Sharpness-of-the-Cyclic-Integral-Floer-Bound-Below-the-Stable-Morse-Number-October-5-2026/sharp-cyclic-integral-floer-bound-below-stable-morse-number.pdf)
