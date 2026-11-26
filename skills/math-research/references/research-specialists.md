# 专题数学方法

按对象找到可调用的证明构件和精确检查器。先核对输入及来源的适用范围。领域键稳定，用于路由和机器索引，不替代单项技能的适用条件。

<a id="euler-gamma-pade"></a>

## 欧拉常数、Padé 与整数线性形式

γ 的无理性、特殊值逼近、精确递推或有限 Padé/行列式证书。

- [math-euler-constant-irrationality](../../math-euler-constant-irrationality/SKILL.md) · 研究欧拉–马歇罗尼常数 γ 的无理性。构造或审计 γ 的 Padé、多重正交、超几何、递推、整数线性形式、分母消去与 Sondow 型判据，也用于核对 E/G 函数、算术 Gevrey 与 Stokes 常数方法能否转移到 γ。
- [math-order-two-casoratian-audit](../../math-order-two-casoratian-audit/SKILL.md) · Audit supplied rational second-order recurrences by exact Casoratian and consecutive quotient identities. It certifies finite identities only.
- [math-prevost-hurwitz-pade-remainder](../../math-prevost-hurwitz-pade-remainder/SKILL.md) · Construct and audit Prévost's finite [n/m] exp(-t) Padé coefficients and its signed Euler-constant/Hurwitz-zeta remainder; preserve all auxiliary zeta and logarithm terms.
- [math-euler-series-continued-fraction](../../math-euler-series-continued-fraction/SKILL.md) · Convert a finite nondegenerate rational series segment to Euler generalized continued-fraction data exactly. Use for finite algebraic identity checks, not for convergence or irrationality claims.
- [math-sondow-log-fractional-certificate](../../math-sondow-log-fractional-certificate/SKILL.md) · 从 Sondow 的双积分与对数线性形式构造可严格计算的欧拉常数分母排除证书。用于生成 S_n 对数权重、认证分数部分阈值、估计余项或寻找使判据在无穷多个指标成立的方法。
- [math-gamma-continued-fraction-recurrence](../../math-gamma-continued-fraction-recurrence/SKILL.md) · 用精确递推生成并审查 Hessami Pilehrood 的欧拉常数有理逼近与非简单连分数。适用于有限系数、收敛子和分母高度核对，不用于无理性结论。
- [math-gamma-gregory-series-interval](../../math-gamma-gregory-series-interval/SKILL.md) · 用 Gregory 系数的 Fontana–Mascheroni 级数计算欧拉常数 γ 的严格有理区间，核对精确系数、剩余质量和给定有理候选。
- [math-gamma-meijer-cmf](../../math-gamma-meijer-cmf/SKILL.md) · 用 Kalisch 等的 Meijer G 保守矩阵场构造欧拉常数 γ 的 Apéry 型候选逼近。复跑已知三阶轨迹，核对对偶矩阵、CVM 换基、收敛判据和约分后的算术质量。
- [math-gamma-multiple-laguerre-approximants](../../math-gamma-multiple-laguerre-approximants/SKILL.md) · 用 Wolfs–Van Assche 的混合型多重 Laguerre 显式有限和生成欧拉常数有理逼近，并审计算术整化、约分、余项和渐近障碍。
- [math-openai-arithmetic-determinants](../../math-openai-arithmetic-determinants/SKILL.md) · 从 OpenAI 算术预印本提取 Taylor 接触消元、整数多项式行构造、行列式算术下界与解析上界比较。用于设计或审查 Catalan 常数、π 与欧拉常数研究中的行列式候选。
- [math-alternating-reciprocal-criteria](../../math-alternating-reciprocal-criteria/SKILL.md) · 用 Sondow 的交错倒数和—连分数判据，严格区分可证明的无理性、有限前缀核验，以及需要整条简单连分数假设的超越性结论。适用于 Pierce 展开或快速增长分母的交错倒数和；不用于仅凭数值近似宣称无理或超越。
- [math-integer-linear-form-rates](../../math-integer-linear-form-rates/SKILL.md) · 用已经证明的整数线性形式高度与双边余项界，生成给定分母的有理逼近下界或推导无理性指数上界。适用于核对 Apéry 型证据和同时逼近的非消失条件。
- [math-hankel-pade-certificates](../../math-hankel-pade-certificates/SKILL.md) · 对整数幂级数做精确 Hankel 行列式与 Padé 有限证书，核验正矩投影的有理下界，并审计 Mahler–Hankel 定理的独立准入门槛；不以有限计算断言超越性或无理度指数。
- [math-euler-maclaurin-quadrature-certificates](../../math-euler-maclaurin-quadrature-certificates/SKILL.md) · 为满足端点消失条件的多项式 Euler--Maclaurin 求积构造精确余项与可复核误差包围；不用于未经认证的一般浮点积分。
- [math-harmonic-sum-recurrences](../../math-harmonic-sum-recurrences/SKILL.md) · 用精确有理算术生成和核对广义超调和数的有限系数。适用于需要把嵌套调和定义化为有限递推、初等对称和或普通调和数的场景；不用于无限 Euler 和、zeta 值化简或无理性结论。
- [math-zeta-polynomial-expansion-coefficients](../../math-zeta-polynomial-expansion-coefficients/SKILL.md) · 精确生成指定 Riemann ζ 多项式展开系数中的 γ、ζ(2),…,ζ(m+1) 与有理余项；不数值求 ζ，也不认证无穷级数收敛。

<a id="transcendence-diophantine-g-functions"></a>

## 超越性、丢番图逼近与 G/Mahler 函数

代数独立、有效逼近、Mahler/G-函数或指数丢番图问题。

- [math-exponential-order-reduction](../../math-exponential-order-reduction/SKILL.md) · Compute and verify the finite extended-order reduction used for pairwise-coprime equations a^x+b^y=c^z before any logarithmic or gap-principle argument.
- [math-four-square-witness-certificates](../../math-four-square-witness-certificates/SKILL.md) · Produce or verify an exact finite four-square witness while explicitly separating that certificate from the incomplete descent in the source note.
- [math-exponential-logarithm-algebraic-independence](../../math-exponential-logarithm-algebraic-independence/SKILL.md) · 核对 Mahler 1931/32 指数与对数代数独立性及多项式非消失下界的精确适用条件。
- [math-rational-logarithm-independence-gate](../../math-rational-logarithm-independence-gate/SKILL.md) · Exactly test whether positive rational inputs have a nontrivial multiplicative power relation, before applying logarithmic-ratio or linear-form results. It does not prove an irrationality exponent or a lower bound.
- [math-algebraic-group-logarithm-distance](../../math-algebraic-group-logarithm-distance/SKILL.md) · 对给定代数点的对数与代数 Lie 子空间，按交换代数群或仿射代数群模型核对距离下界的各自前提。
- [math-baker-runge-height-gates](../../math-baker-runge-height-gates/SKILL.md) · 在已给出射影模型、除子和 S-整模型时，核对 Baker--Runge 型积分点高度界的交叠条件与例外集；不计算未给出的有效常数。
- [math-elliptic-quasielliptic-function-independence](../../math-elliptic-quasielliptic-function-independence/SKILL.md) · 对已给定椭圆格、指数参数和 Serre 函数参数，依据经认证的线性无关条件调用函数层面的代数独立性；不从数值特殊值或“几乎处处”结论推断特定点独立性。
- [math-exponential-algebraic-methods](../../math-exponential-algebraic-methods/SKILL.md) · 根据指数方程的模型选择复环面或阿贝尔簇上的存在定理，或明确承担 Schanuel、EAC 等前提后的指数多项式与幂映射结论。
- [math-fibonacci-valuation-reductions](../../math-fibonacci-valuation-reductions/SKILL.md) · 对给定 Fibonacci 指数的精确整除前提，检查 F_l 的精确幂整除并应用三分支的指数约化；不宣称解完原始指数丢番图方程。
- [math-finite-field-formal-series-congruences](../../math-finite-field-formal-series-congruences/SKILL.md) · Verify finite coefficient windows for elementary formal-series fixed points over a prime field, with explicit truncation boundaries.
- [math-g-function-restricted-approximation](../../math-g-function-restricted-approximation/SKILL.md) · 对已认证为有理系数非有理 G-函数的有理值，调用有效的固定基底分母逼近下界；也用于限制其 b 进制展开中的长重复数字块。
- [math-gfunction-representability-obstructions](../../math-gfunction-representability-obstructions/SKILL.md) · Apply a Picard--Vessiot obstruction to a proposed rational representation of a G-function by supplied solution families, singularity bounds and differential-Galois data.
- [math-lacunary-recurrence-transcendence](../../math-lacunary-recurrence-transcendence/SKILL.md) · Apply a Subspace-Theorem transcendence criterion to lacunary reciprocal series after certifying the conjugate-root representation, sublinear heights and all-index gap condition.
- [math-mahler-purity-filtration](../../math-mahler-purity-filtration/SKILL.md) · Apply the generalized-Mahler Hahn/Puiseux purity filtration to a supplied Mahler equation, while tracking exceptional arithmetic-growth layers and decomposition hypotheses.
- [math-mahler-system-admission](../../math-mahler-system-admission/SKILL.md) · Apply scoped basis, lifting and purity theorems for supplied Mahler equations or systems after certifying the coefficient field, transformation, regularity and orbit hypotheses.
- [math-mixed-littlewood-pseudoadic](../../math-mixed-littlewood-pseudoadic/SKILL.md) · 对满足有限素数支撑和增长条件的伪绝对值序列，调用已发表的混合 Littlewood 存在性定理；不把它当作给定 alpha 的有限逼近算法。
- [math-parameterized-norm-form-certificates](../../math-parameterized-norm-form-certificates/SKILL.md) · Verify the published solution families of the Bajpai--Bennett cubic norm-form equation and the Bennett--Ghadermazi extremal cubic Thue equation at supplied integer parameters.
- [math-primary-pseudopolynomial-certificates](../../math-primary-pseudopolynomial-certificates/SKILL.md) · 精确核对主伪多项式的有限 binomial 变换、素数乘积整除条件和已给出的全指标前提。
- [math-syracuse-exact-words](../../math-syracuse-exact-words/SKILL.md) · Verify a supplied finite valuation word for the accelerated positive odd 3x−1 Syracuse map, including its exact source and affine identity. Do not use it to infer predecessor density or a Collatz-type conjecture.
- [math-ax-schanuel-dimension-defect](../../math-ax-schanuel-dimension-defect/SKILL.md) · 对已明确的平坦联络、模 j、Hodge 周期映射或矩阵指数数据，选择相应 Ax--Schanuel 维数缺陷定理并核对不可省略的几何前提。
- [math-q-series-rational-approximants](../../math-q-series-rational-approximants/SKILL.md) · 对给定有理 q 和 z 生成 Tschakaloff 递推的精确多项式系数，核验有限整数化缩放及余项分离。
- [math-function-field-period-transcendence](../../math-function-field-period-transcendence/SKILL.md) · 在已给定的正特征 Drinfeld 模、t-motive 与解析平凡化数据下，定位周期、准周期、第三类周期和 Carlitz 张量周期的条件性超越/代数独立接口。

<a id="analytic-number-theory-special-functions"></a>

## 解析数论、L 函数、模形式与特殊函数

ζ/L 函数、模形式、MZV、特殊函数及其有限恒等式。

- [math-dirichlet-l-value-span-scope](../../math-dirichlet-l-value-span-scope/SKILL.md) · Apply the current preprint's asymptotic Dirichlet L-value span lower bound with the exact conductor, coefficient field, and opposite-parity restrictions.
- [math-hypergeometric-padic-prime-density](../../math-hypergeometric-padic-prime-density/SKILL.md) · Compute the eventual congruence classes and Dirichlet density of p-adically bounded primes for a supplied rational regular-singular hypergeometric series nF_{n-1}.
- [math-modified-dirichlet-character-omega-bound](../../math-modified-dirichlet-character-omega-bound/SKILL.md) · 对有限素数修改的原始 Dirichlet 特征，按解析、Baker 和差异度量门槛调用部分和的对数 Ω 下界。
- [math-modular-bootstrap-certification](../../math-modular-bootstrap-certification/SKILL.md) · Transfer a verified feasible spinless modular-bootstrap functional to a CFT gap bound under the source's precise admissibility and integrability hypotheses.
- [math-xi-theta-finite-certificates](../../math-xi-theta-finite-certificates/SKILL.md) · Audit finite Xi/theta positivity components from supplied moment envelopes and exact polynomial inequalities; do not infer a zero-free strip or RH.
- [math-cmzv-rational-pullback](../../math-cmzv-rational-pullback/SKILL.md) · Place specified iterated integrals or multiple polylogarithms in a cyclotomic MZV space through a verified rational-pullback criterion.
- [math-cyclotomic-euler-t-parity](../../math-cyclotomic-euler-t-parity/SKILL.md) · 对满足收敛条件的根单位 cyclotomic Euler T-sum，调用围道留数奇偶归约到较低阶和；不提供未展开余项的数值公式，也不采纳猜想的 multiple-t 奇偶性。
- [math-motivic-euler-sum-unramifiedness](../../math-motivic-euler-sum-unramifiedness/SKILL.md) · 对已精确匹配的 motivic Euler-sum 字族或已认证余作用账本，调用非分歧判据；不把 motivic 结论误写成数值 period 恒等式。
- [math-selberg-riesz-criteria](../../math-selberg-riesz-criteria/SKILL.md) · 对给定 Selberg 类 L-函数数据和经认证的系数渐近，调用 Riesz 型 Meijer-G 判据的 GRH 蕴含或反向判据。
- [math-nevanlinna-functional-transcendence](../../math-nevanlinna-functional-transcendence/SKILL.md) · 核对非恒定整函数的 Nevanlinna 特征分离、测度有限的异常集及源定理给出的函数域超越次数。
- [math-bessel-cross-product-recurrence](../../math-bessel-cross-product-recurrence/SKILL.md) · 在已给定的 Bessel/modified-Bessel 定义域内，使用离散 Riccati 恒等式与二阶交叉积递推；不把有限递推代数当作圆板谱重数或超越性证明。
- [math-modular-holonomic-telescoping](../../math-modular-holonomic-telescoping/SKILL.md) · 用显式极点数据、带权 q 展开和经证实的 valence 界检查亚纯模形式导出的 holonomic 递推。
- [math-dirichlet-l-derivative-sine-reduction](../../math-dirichlet-l-derivative-sine-reduction/SKILL.md) · 对给定偶周期有理数据，精确生成 Dirichlet 型级数在零点导数的形式对数权重。核对周期、对称性、零索引和分母。
- [math-mzv-newton-harmonic-relations](../../math-mzv-newton-harmonic-relations/SKILL.md) · Check finite Newton/binomial duality for positive multiple-harmonic indices exactly. Use to prepare finite inputs for Kawashima-type MZV relations, not to prove MZV independence or Euler-constant claims.
- [math-zeta-arithmetic-estimates](../../math-zeta-arithmetic-estimates/SKILL.md) · 根据指定的 ζ 函数采样、平滑核和参数区间接入等差级数矩比较与光滑数零点修正。适用于检查扭权、测量模型和误差来源。

<a id="differential-difference-dynamics"></a>

## 微分差分方程、递推与动力系统

有限递推、差分 Galois、可积系统、正交多项式或周期轨道。

- [math-finite-cyclic-difference-pv](../../math-finite-cyclic-difference-pv/SKILL.md) · Certify the finite cyclic Picard–Vessiot-ring construction for a caller-supplied finite-order diagonal representation; do not use it to solve general inverse difference-Galois problems.
- [math-double-elliptic-orbit-confinement](../../math-double-elliptic-orbit-confinement/SKILL.md) · Apply the source-scoped confinement theorem for finite translation orbits on a surface with two elliptic fibrations and non-torsion sections.
- [math-semiclassical-orthogonal-deformations](../../math-semiclassical-orthogonal-deformations/SKILL.md) · 对给定半经典正交权及移动奇点，核验递推系数的 Toda 变形方程和 Freud 权的 Painleve IV 化简。
- [math-differential-operator-minimization](../../math-differential-operator-minimization/SKILL.md) · Minimize a supplied rational-coefficient differential operator for a specified formal solution, after certifying the Ore factor, degree-bound and initial-series subroutines.
- [math-linear-difference-hypertranscendence](../../math-linear-difference-hypertranscendence/SKILL.md) · 对移位、q-差分或 Mahler 线性差分方程，在已给定的函数域与系数域中应用有理函数或超越函数二分，并核验参数化差分 Galois 前提。
- [math-hofstadter-nested-recurrences](../../math-hofstadter-nested-recurrences/SKILL.md) · 用精确整数递推计算广义 Hofstadter 函数 F_k 的有限前缀，并核对已给出的点态比较。
- [math-recurrence-finite-screening](../../math-recurrence-finite-screening/SKILL.md) · Exact bounded residual checks for k-Pell multiplicative dependence, decimal k-Lucas concatenations, and unit-constant two-sided recurrences. Never promotes a finite box to a global recurrence theorem.
- [math-lienard-half-arc-matching](../../math-lienard-half-arc-matching/SKILL.md) · 将已验证的 Lienard 半平面弧坐标匹配转化为周期轨道与孤立零点问题；不用于未经认证的数值积分或周期数上界。

<a id="analysis-geometry-pde"></a>

## 调和、几何与泛函分析及 PDE

极大算子、Fourier/谱、度量几何、热核、共形或几何 PDE。

- [math-strip-poisson-smoothing](../../math-strip-poisson-smoothing/SKILL.md) · Transfer a symmetric complex-center profile in a fixed strip to complete monotonicity using hyperbolic-secant Poisson smoothing.
- [math-conformal-dimension-perron-brackets](../../math-conformal-dimension-perron-brackets/SKILL.md) · 对给定扩张共形 Markov 分区、认证导数区间和有理比较向量，验证非负转移矩阵的谱半径界并判断指数与维数的方向。
- [math-subanalytic-preparation](../../math-subanalytic-preparation/SKILL.md) · 用明确给定的次解析族、泛参数域和纤维模型整理有理幂次展开与边界余项；记录常数和阈值的参数依赖。
- [math-asymptotic-midpoint-moduli](../../math-asymptotic-midpoint-moduli/SKILL.md) · 在已认证的树、段森林或 Daugavet-L1 结构上，调用渐近中点模量与可数分支 diamond 失真界；不把有限算术或抽象范数当作结构证书。
- [math-conformal-domain-estimates](../../math-conformal-domain-estimates/SKILL.md) · Manage gated conformal-domain coordinate-energy and univalent inverse-integral-means transfers. Use only with the specified normalization, boundary, and source-model hypotheses; not for arbitrary holomorphic maps or planar compactness.
- [math-tube-maximal-transfer](../../math-tube-maximal-transfer/SKILL.md) · Transfer a specified three-dimensional tube or curved extension packet estimate through its declared maximal, capacity, and level-set interfaces. Not a generic Kakeya, restriction, or incidence certificate.
- [math-centered-cube-endpoint-budget](../../math-centered-cube-endpoint-budget/SKILL.md) · Audit or extend centered axis-parallel cube Hardy–Littlewood weak-(1,1) bounds: all-scale source/receiver budgets, joint high-capacity remainders, and finite-dimensional square/cube certificates. Use for centered-cube-upper-bound, the Round 830 remainder, or cubical endpoint constants; not for Euclidean balls, Kakeya tubes, or strong rectangular maxima.
- [math-hbl-finite-presentation](../../math-hbl-finite-presentation/SKILL.md) · 对已给定的有理有限子空间图和边权，精确核验 HBL 有效表示并分解平衡边流；不搜索表示或计算一般 HBL 常数。
- [math-torus-packet-spectral-density](../../math-torus-packet-spectral-density/SKILL.md) · 对给定有理分段仿射扭转与有限角向 Fourier 包，精确计算模一推前的阶梯谱密度、色间正交门槛和可选 L1 密度差。
- [math-cat0-inductive-barycenters](../../math-cat0-inductive-barycenters/SKILL.md) · Transfer a finite centred distribution in a complete CAT(0) metric cone into an inductive-barycenter energy bound, with exact Euclidean finite-support replay. Use for certified cone geometry, not generic group-action or sampling claims.
- [math-geometric-pde-reductions](../../math-geometric-pde-reductions/SKILL.md) · 核对给定几何模型的高度方程、标量曲率归一化、Neumann 能量、径向 ODE 不变域、弱流代表元和单相极小子的维数归约。 包含固定顶点倾斜比较与给定加权幂零坐标的局部检查。
- [math-lattice-heat-asymptotics](../../math-lattice-heat-asymptotics/SKILL.md) · Prove and safely use the first large-time correction for the continuous-time nearest-neighbor lattice heat kernel. Use for the exact dispersion 2(1-cos k), tensor-product dimensions, and clearly separated physical scaling.

<a id="algebraic-arithmetic-geometry"></a>

## 代数几何、模空间、p-adic 与非阿基米德几何

除子、Hodge/period、特殊点、模曲线、p-adic 或非阿基米德资料。

- [math-ladic-level-triviality-gate](../../math-ladic-level-triviality-gate/SKILL.md) · Apply the Kadets--Litt level-to-triviality implication only after an arithmetic semisimple l-adic representation and a certified curve-dependent depth are supplied.
- [math-fermat-hodge-lattice-quotients](../../math-fermat-hodge-lattice-quotients/SKILL.md) · Reduce a certified Fermat middle-Hodge lattice quotient to an explicit group-ring quotient, while preserving the geometric and arithmetic premises needed for the reduction.
- [math-geometric-g-function-special-points](../../math-geometric-g-function-special-points/SKILL.md) · 对已给出的一参数代数族、退化、周期矩阵与特殊纤维数据，选择 G-函数局部关系、特殊点高度或模曲线非典型交的定理接口。
- [math-likely-intersections-density](../../math-likely-intersections-density/SKILL.md) · Apply the conditional likely-intersection density theorem for a verified definable complex quotient presentation and its Ax--Schanuel witnesses.
- [math-modular-unlikely-intersections](../../math-modular-unlikely-intersections/SKILL.md) · Route a specified modular-curve or abelian-family unlikely-intersection problem through the available degeneration, height, Galois-orbit and conditional Lang--Trotter theorems.
- [math-padic-abelian-intersection-bounds](../../math-padic-abelian-intersection-bounds/SKILL.md) · Apply the source-scoped Buium--Coleman reduction bounds for a smooth p-adic curve inside an abelian variety after an unramified model and jet-space data have been certified.
- [math-special-point-bound-gates](../../math-special-point-bound-gates/SKILL.md) · Apply Paulin's explicit special-point discriminant and root-of-unity order bounds to a supplied curve in P1 x Gm after checking its field, polynomial and geometric hypotheses.
- [math-holomorphic-local-to-global-transfer](../../math-holomorphic-local-to-global-transfer/SKILL.md) · Transfer specified holomorphic local data to descent, gluing, integrability, or universal-cover product conclusions only after the matching geometric gate has been established. Not for arbitrary local charts or holomorphic distributions.
- [math-ag-divisor-intersection-ledger](../../math-ag-divisor-intersection-ledger/SKILL.md) · 对已给定的精确除子、公共解消与交叉数表核验局部代数几何接口；不构造几何对象或采纳丰度/Iitaka 主定理。 支持点吹起中零循环的整系数推拉。
- [math-nonarchimedean-analytic-transfer](../../math-nonarchimedean-analytic-transfer/SKILL.md) · 在完备非阿基米德环境中，核对有理或形式的有限阶解析 jet 转移、近似根余项及稠密压缩逆塔上的 Roos 差分。
- [math-weil-deligne-purity-lfactor](../../math-weil-deligne-purity-lfactor/SKILL.md) · Certify the local L-factor half-plane and Frobenius determinant consequence of supplied pure weight-zero Frobenius-semisimple Weil–Deligne data. Use only after the Weil–Deligne representation, inertia invariants, and purity witnesses have been established externally.

<a id="algebra-representation-operator-cohomology"></a>

## 代数、表示论、算子代数与上同调

有限代数、群与表示、算子代数、链复形或转移证书。

- [math-mixed-determinant-border-certificates](../../math-mixed-determinant-border-certificates/SKILL.md) · Exactly check the finite rank-one bordering identity for a caller-supplied tuple of rational symmetric matrices in the mixed-determinant construction.
- [math-heisenberg-group-determinant-certificates](../../math-heisenberg-group-determinant-certificates/SKILL.md) · Exactly compute the finite group-determinant matrix of a supplied sparse element of the order-125 Heisenberg group, with a replay for one documented witness.
- [math-symmetric-polynomial-ratio-certificates](../../math-symmetric-polynomial-ratio-certificates/SKILL.md) · Evaluate finite complete-homogeneous and Schur Turan ratios exactly on rational inputs, preserving the stated partition and positivity domains.
- [math-nonnegative-matrix-path-certificates](../../math-nonnegative-matrix-path-certificates/SKILL.md) · Verify the odd-power path certificate for finite entrywise-nonnegative symmetric matrices, with exact finite arithmetic where the inputs are rational.
- [math-finite-nonassociative-algebra-audits](../../math-finite-nonassociative-algebra-audits/SKILL.md) · 核验指定有理轴代数乘法表、消去后的线性泛函，或素域上的仿射 medial rack 恒等式和见证。
- [math-algebraic-transfer-certificates](../../math-algebraic-transfer-certificates/SKILL.md) · 核对已给定的余留映射、整系数转移、链提升、格拼接或有限对称张量资料。适用于 Gersten 与 Milnor 障碍、升 HNN 扩张的同调输入和纤维函子条件。
- [math-cohomological-transfer](../../math-cohomological-transfer/SKILL.md) · 核验链复形权截断、Mayer–Vietoris 条件、图状神经上链延拓以及已给代数或谱数据上的局部化与张量消失。
- [math-f2-group-ring-cancellation](../../math-f2-group-ring-cancellation/SKILL.md) · Verify a finite characteristic-two group-ring cancellation certificate from two labelled components and a supplied exact group-label product oracle; it does not establish torsion-freeness or nonzero factors.
- [math-free-group-presentation-traces](../../math-free-group-presentation-traces/SKILL.md) · 核验有限 Andrews–Curtis 自由群表示轨迹，以及已给成员关系时的带并自由积正规形见证。
- [math-operator-algebra-certificates](../../math-operator-algebra-certificates/SKILL.md) · 核验算子代数中的幺正压缩修复、平移卷积核、谱相位迹、自伴谱编码及 C* 截断转运。按已给投影、严格谱隙、迹或比较见证选择。
- [math-projective-induction-cocycle-certificates](../../math-projective-induction-cocycle-certificates/SKILL.md) · 用有限 Cayley 表和有理相位精确核验图子群上的射影诱导校正、乘子、代表元变换和有限指标维数。

<a id="discrete-combinatorics-games"></a>

## 图论、组合、离散几何与博弈

有限图、计数、permanent、半群、概率组合或有限博弈证书。

- [math-lattice-box-manhattan-ordering](../../math-lattice-box-manhattan-ordering/SKILL.md) · Exhaustively optimize or validate a Manhattan-length ordering of all points in a small integer box.
- [math-rees-zero-complete-mappings](../../math-rees-zero-complete-mappings/SKILL.md) · Verify the explicit even-index complete mapping of a finite Rees 0-matrix semigroup over Z/2Z with identity diagonal.
- [math-average-degree-tree-embedding](../../math-average-degree-tree-embedding/SKILL.md) · 在有限简单无向图中，按平均度严格阈值核对给定树的嵌入，并返回可检查的顶点映射。
- [math-finite-permutation-terrace-certificates](../../math-finite-permutation-terrace-certificates/SKILL.md) · Verify a supplied ordering of all even permutations as a finite basic-terrace certificate; includes a reader for the public packed A7 witness format.
- [math-graph-spectral-moment-certificates](../../math-graph-spectral-moment-certificates/SKILL.md) · Compute adjacency trace moments and short-cycle counts of finite simple graphs, and exact integral circulant spectra and energy by Ramanujan sums.
- [math-permanent-inequality-contracts](../../math-permanent-inequality-contracts/SKILL.md) · Audit finite permanent inequalities for stochastic matrices and symmetrizable inverse M-matrices, retaining each source theorem's hypotheses and equality scope.
- [math-petal-join-domination-polynomial](../../math-petal-join-domination-polynomial/SKILL.md) · Exhaustively verify the finite domination-polynomial identity for a clique joined to repeated copies of a small petal graph.
- [math-regular-graph-low-induced-edge-count](../../math-regular-graph-low-induced-edge-count/SKILL.md) · Exhaustively count finite vertex subsets whose induced subgraph has at most a given number of edges, while checking regularity.
- [math-unfair-polynomial-trinomial-factors](../../math-unfair-polynomial-trinomial-factors/SKILL.md) · Apply the trinomial case of the unfair 0–1 polynomial theorem after checking its normalized finite-support and nonnegative-coefficient hypotheses.
- [math-two-generator-graded-semigroup-certificates](../../math-two-generator-graded-semigroup-certificates/SKILL.md) · 精确计算双生成分层数值半群的 Wilf 型有限不等式，或枚举给定数值半群分解为不可约超半群交集的长度。
- [math-one-special-parking-equality](../../math-one-special-parking-equality/SKILL.md) · Enumerate the invariant one-special-preference parking set for a finite positive length list and check the subset-sum equality criterion.
- [math-cycle-weighted-permanent](../../math-cycle-weighted-permanent/SKILL.md) · Compute finite Macdonald cycle-weighted permanents and their scalar normalizations exactly for rational q and t.
- [math-graded-character-order](../../math-graded-character-order/SKILL.md) · Certify finite graded multiplicity comparisons through cumulative coefficient differences and optimal ordered matching.
- [math-quantum-permanent-score](../../math-quantum-permanent-score/SKILL.md) · Check finite partition-score lower bounds from a supplied nonnegative orbital coefficient profile.
- [math-cycle-type-likelihood-bounds](../../math-cycle-type-likelihood-bounds/SKILL.md) · Compare two supplied finite cycle-type laws under an explicit iid observation model, with Hellinger affinity and Bayes-error bounds.
- [math-bimatrix-kite-mixing](../../math-bimatrix-kite-mixing/SKILL.md) · 核验双矩阵博弈的后悔值、s-kite 条件与精确最佳回应混合。适用于已有候选策略的局部改进与有限证书，不把尚未独立复核的全局近似 Nash 声明当作可用定理。
- [math-edge-deck-reconstruction-audit](../../math-edge-deck-reconstruction-audit/SKILL.md) · 审计有限简单图的无标号单边删除卡组，精确比较候选反例并核对边重构定理的图类和密度门槛。适用于小图枚举、边卡组断言和来源结论的适用范围检查。
- [math-finite-graph-family-witnesses](../../math-finite-graph-family-witnesses/SKILL.md) · 核验显式有限图族的三直径、装饰树独立多项式、后继色路径与 Mycielski 张量图的奇窗口着色见证。
- [math-honeycomb-finite-boundary-flux](../../math-honeycomb-finite-boundary-flux/SKILL.md) · 在有限、单连通蜂窝三角形域中认证零环权重的带相位边界通量恒等式及凸域正性界；不用于条带渐近、桥质量或一般自避游走。
- [math-clique-free-random-multiplier](../../math-clique-free-random-multiplier/SKILL.md) · Construct and exactly check the finite-support random multiplier from the clique-free neighborhood recursion for a supplied finite weighted K_r-free graph.
- [math-grid-piecewise-translation-embedding](../../math-grid-piecewise-translation-embedding/SKILL.md) · Certify a finite cellwise translation embedding between two strict-size subsets of a specified square cell grid. Use after a geometric argument has supplied an allowable common grid; it does not polygonize sets or prove a general equidecomposition theorem.
- [math-three-strip-token-bound](../../math-three-strip-token-bound/SKILL.md) · Certify the finite three-strip/token boundary bound for a sequence of equal-cardinality planar threshold cuts with matched exchanges; not a halving-line asymptotic solver.

<a id="complexity-tensor-transfer"></a>

## 复杂性、张量与离散证明迁移

通信复杂性、张量复杂性或已命名研究项目的有限迁移接口。

- [euclidean-tensor-geometry](../../euclidean-tensor-geometry/SKILL.md) · Apply or audit OpenAI family 379 Euclidean tensor prices, Strassen spectral invariants, and common-placement network bounds in arithmetic complexity and combinatorics. 中文触发：欧几里得张量几何、张量价格、渐近谱、跨割下界。Do not use for generic tensor numerics or classical maximal operators without a proved model bridge.
- [math-discrete-proof-transfer](../../math-discrete-proof-transfer/SKILL.md) · 为固定二叉 Derrida–Retaux/H3、连续 Cantelli、自由边界方格双峰 A022、非负因子 A30/A175、布尔 Fourier 谱维数 A28/A165 审核可迁移引理并制作可独立核验的证书。另用于周期图的有限连通分支与例外顶点预算。不要因同名 Fourier、稳定性或张量术语就迁移结论。
- [math-logrank-rectangle-rank-halving](../../math-logrank-rectangle-rank-halving/SKILL.md) · 从有限 Boolean 通信矩阵的单色矩形出发，精确核验互补块秩分裂，并把给定矩形或协议分割转为 rank-halving 递归证书。用于审计 Log-Rank 路线的有限接口，不搜索大矩形或认证高秩渐近定理。
