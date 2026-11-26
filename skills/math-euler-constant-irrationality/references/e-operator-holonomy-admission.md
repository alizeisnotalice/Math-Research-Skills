# E-算子与算术和乐界的准入审计

给定候选逼近的两个生成函数、极限证明和所用定理版本，逐项核对 E-算子与算术和乐界的假设。结论限于已有证据覆盖的命题。

## 已核对的原始依据

1. S. Fischler and T. Rivoal, *Arithmetic theory of E-operators*,
   arXiv:1406.5995v1, 本机文件
   `07_Irrationality_Transcendence_Compendium/PDF/EXT-0040_Arithmetic_theory_of_E_operators.pdf`,
   SHA-256 `40ef2ae20cf57ceae3f4a3b849d0e83aaca6a0f9d917adfddaa840bc0635ec46`。
   定义 4 和定理 4 在物理页 5--6，扩展 E-逼近式 (1.8)--(1.9) 在页 6--7，
   \(\gamma\) 的递推例子 (6.4)–(6.6) 在页 27–28。定理 2–3 在页 3–4
   区分有限点连接常数和无穷远 Stokes 常数。[期刊版书目](https://doi.org/10.5802/jep.28)
2. F. Calegari, V. Dimitrov and Y. Tang, *Arithmetic holonomy bounds and
   effective Diophantine approximation*, arXiv:2510.04156v1, 本机文件
   `04_Attachment_References/PDF/P22-P35/P24b_Arithmetic_holonomy_bounds_and_effective_Diophantine_approximation.pdf`,
   SHA-256 `5f403f337fed8bfd776348a04aaaec7d57ca6f90c31dd871ed793bf24239c8f1`。
   Apéry-limit 框架和定理 2.1 位于物理页 3--4，命题 2.4 位于页 4--5，
   多赋值/有效版本定理 2.6 位于页 5--6。
3. S. Fischler and T. Rivoal, *Relations between values of arithmetic Gevrey
   series, and applications to values of the Gamma function*, arXiv:2301.13518v1,
   本机文件 `04_Attachment_References/PDF/P22-P35/P23_Relations_between_values_of_arithmetic_Gevrey_series_and_applications_to_values_of_the_Gamma_function.pdf`,
   SHA-256 `0f08c970d28d4fcfc7b26b64c0f55ccc6d6f05241ecaaaaab3c8693fc7a16140`。
   其定理 2 的 \(\gamma\) 结论须保留 Conjecture 1 的条件，不能作为无条件出口。

## 第一道门，E-算子类型

为候选 \(P_n/Q_n\to\eta\) 提交以下原件。

| 检查项 | 需提交的证据 | 结论标签 |
| --- | --- | --- |
| 极限 | 精确式或有明确误差界的证明 | `limit-established` |
| 生成函数 | \(\sum P_nz^n\) 与 \(\sum Q_nz^n\) 的明确表达 | `generator-recorded` |
| 普通 E 型 | 分子和分母的生成函数是否各自具备定义 4 的 \(A(z)E(B(z))\) 形状，其中 \(A,B\) 是代数幂级数，\(B(0)=0\)，\(E\) 是 E-函数 | 普通 E 型已证或待证 |
| 扩展型 | 出现的每个 \(\log(1-A_i(z))\)、代数函数和 E 函数是否满足式 (1.8) | `extended-E` 或 `outside-extended-E` |
| 无穷远数据 | 若使用 Stokes 常数，给出算子、扇形和 anti-Stokes 方向排除 | `Stokes-data-recorded` |
| 算术结论 | 分开列出无条件定理和每一个猜想前提 | `unconditional`、`conditional` 或 `not-established` |

普通 E 型不包括只因“满足一个多项式系数递推”而得到的序列。对数项出现时，
不能把扩展 E 型降格称为普通 E 型。connection constant 与 Stokes constant 也
不能互换。

### 已知的边界例子

令

\[
E(z)=\sum_{n\ge1}\frac{z^n}{n!n},\qquad
\sum_{n\ge0}P_nz^n=
 \frac{\log(1-z)}{1-z}-\frac{1}{1-z}E\!\left(-\frac{z}{1-z}\right).
\]

原文证明 \(P_n\to\gamma\)，且

\[
P_n=\sum_{k=1}^n(-1)^k\binom nk\frac{1-1/k!}{k},
\]

并满足

\[
(n+3)^2P_{n+3}-(3n^2+14n+17)P_{n+2}
+(n+2)(3n+5)P_{n+1}-(n+1)(n+2)P_n=0,
\]

其中 \(P_0=P_1=0\)、\(P_2=1/4\)。这个表达式给出扩展 E-逼近。\(\log(1-z)\) 是该构造中的一项。若另有表达式符合定义 4，须另给出等价证明。\(\gamma\) 是否存在普通 E-逼近在原文中是猜想，整系数线性形式所需的分母与误差比较也仍待建立。

[有限项脚本](../scripts/check_extended_e_approximation.py) 以 `Fraction` 逐项复核该和式
与递推，不把浮点近似作为验证证据。

## 第二道门，CDT 算术和乐界转移

在声称以 CDT 定理 2.1 排除 \(\eta\in\mathbb Q\) 前，逐项填写并保存以下记录。

| 门 | 必要材料 | 失败时的处理 |
| --- | --- | --- |
| Apéry 数据 | \(A\in\mathbb Z[[x]]\)、\(B\in\mathbb Q[[x]]\)，以及 \(B-\eta A\) 的较大收敛半径证明 | 仅保留逼近实验 |
| 解析数据 | \(\phi(0)=0\)、实际用于维数比较的每个 \(f_i\circ\phi\) 在开单位圆盘的亚纯延拓 | 不调用定理 2.1 |
| 分母数据 | 每个候选 \(f_i\) 的精确 LCM 型分母，列须“先零后常数” | 不以经验 lcm 代替证明 |
| 维数数据 | \(f_i\) 的 holonomic 性和 \(\mathbb Q(x)\)-线性独立证明 | 不以有限项秩替代 |
| 数值门槛 | 按定理计算 \(b\) 和 \(\tau(b)\)，证明严格不等式 \(\log|\phi'(0)|>\tau(b)\)，并控制式 (2.2) 的边界双积分 | 不能引用维数上界 |
| 反证接口 | 证明 \(\eta\in\mathbb Q\) 时所需函数确实进入被定理约束的空间，并构造超过上界的函数数目 | 没有无理性推论 |

若追求无理性测度，命题 2.4 还要求单独的 \(A_i,B_i\) 在半径 \(\rho\) 内收敛。
若使用多处或幂系统，则改用定理 2.6，并额外登记每个赋值处、\(\rho_u\)、
\(K(\eta,x)\)-线性独立性和全部分母 capping 数据。

上述扩展 E 例子的 CDT 审计停在构造阶段。该例仍需提供 \(\phi\)、LCM 分母矩阵、亚纯延拓及超出维数界的独立函数。

## 最小验收记录

每一次新候选构造至少归档：原始 PDF 路径和 SHA-256、页码/公式、上述每门的
通过或失败状态、可运行的精确有限项检查，以及“严格证明”“条件性推论”或
“数值证据”的标签。缺少一门时，输出只能保留在相应较弱层级。
