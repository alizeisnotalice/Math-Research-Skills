# 两篇原文提供的构造

来源为本机 Math_Research_Literature 的 02_Recent_Math_Papers/OpenAI/current，归档固定在 openai/math 提交 3344da59991ed94f9ba711217b29c1d760badfa6。核对的是原文具体构件。

## Family 005 的二次曲线与共轭配对

*Catalan’s constant is irrational*，本机 SHA-256 4023d0344abceb79dc46a16380dac3a662193f9d4f23e6c340b2162068b04c0e。物理页 2–4，特别是 §2 式 (2)–(6)。[固定版本原文](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf)

- 在二次扩张内取 f=√(1−t²)，分支 f(0)=1，w=t/(1+f)。共轭把 f 变为 −f，把 w 变为 w⁻¹。构造 Rᵣ=(1−t)^h t^(C−1) w^(r−g)，取 Pᵣ=(Rᵣ+Rᵣ*)/2 与 Dᵣ=t(Rᵣ*−Rᵣ)/(2f)。于是 tPᵣ−fDᵣ=tRᵣ，且 w=t/2+O(t³)；接触阶为 C+r−g。
- 令 d=|r−g|，将 Pᵣ、Dᵣ 用 T_d(1/t)、U_(d−1)(1/t) 表示，Dᵣ 带 sign(r−g)，d=0 时 Dᵣ=0。先用 t^d 缩放 Chebyshev 递推，构造全程整系数的多项式。论文的 M 与 Z 混合矩用此接触关系消去 ζ(2)，需保留它们各自的核、区域和系数。
- 后续读 §3–4 与 §7。原文分别使用素数估值、素数尺度的模非消失以及实位估计。脚本验收的是 §2 的行构造，后续矩计算、素数归约和实位界需按原文另核。

## Family 017 的加权对数插值

*The irrationality exponent of pi is 2*，本机 SHA-256 26eec5de7ac9dc49d28183fdea458e0858bc3323b5ba93c3d41bb105d8e3eab6。物理页 3–4，Theorem 2.1 与式 (2.1)–(2.2)。[固定版本原文](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf)

- 枚举满足 h w₀+Σαᵢwᵢ≤H 的单项式。以每个中心 j 的 Y=1+t、Xᵢ=cⱼᵢ+uᵢ+log(1+t) 生成按权截断的系数列。Taylor 目标的权为 (v₀,w₁/θ,…,wₘ/θ)，指数满足严格小于 H。截断 log 时至少保留所有 s v₀<H 的 t^s。
- 预先选 m、K、正有理 w₀、v₀、θ，检查 0<θ<1、Kθ^m<1、K(w₀/v₀)θ^m<1。其余权重依序选择且阈值独立于中心。对每个坐标 i，各中心的 cⱼᵢ 两两不同。原文的满秩结论在固定这些数据后的充分大 H 适用。
- 有理或高斯有理中心可精确消元，选非零子式并逐行清分母。把这个有限构件与定理的渐近满秩结论分开。原文解析小量还利用对数曲线与精确周期的关系、按横向指标分组并用相同 Taylor 次数导致的行列式消失。应用于 γ 需先给出能承担该机制的对象和证明。

本机有限测试采用 m=K=1、中心 c=2、w₀=v₀=1、θ=1/2、w₁=2、H=5。SymPy 的系数矩阵为 6×12，所选最大子式行列式为 −1/12。该例仅验证系数截断和消元实现。
