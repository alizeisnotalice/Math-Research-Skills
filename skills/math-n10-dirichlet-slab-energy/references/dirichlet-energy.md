# 加条带的代价与共同能量见证

## 交叠凸域

对有界非空开凸域 \(D\subset\mathbb R^m\) 和正定对角矩阵 \(Q\)，令 \(\lambda_Q(D)\) 为 \(-\operatorname{tr}(Q\nabla^2)\) 的 Dirichlet 最小本征值。等价地，它是 \(H^1_0(D)\) 中 \(\int\nabla f^\top Q\nabla f/\int f^2\) 的下确界。Brownian 运动的协方差率为 \(2Q\)。

再假设 \(D\) 关于原点对称，\(a,\delta>0\)，给定有限个行向量 \(v_i\)。对
\[
K=(2aD)\cap\bigcap_i\{x:|v_i x|<\delta\}
\]
得到
\[
\lambda_Q(K)\ \le\ a^{-2}\lambda_Q(D)+\frac{\pi^2}{\delta^2}\sum_i v_iQv_i^\top.
\]

从 0 出发，对 \([0,T]\) 上的路径施加闭约束 \(\overline{aD}\) 与每条半宽 \(\delta/2\) 的闭带。联合事件蕴含在开集 \(K\) 生存。有限时间网格的约束是中心对称凸集。由 Gaussian correlation，联合概率至少是各约束概率的乘积。用嵌套稠密网格和连续路径取极限，再以相应的较小开约束替换各因子。

有界开凸域内，从内点出发的生存概率指数率为 \(\lambda_Q\)。这个输入来自有杀死条件的热半群谱界和正的首本征函数。Rayleigh 商给出 \(\lambda_Q(aD)=a^{-2}\lambda_Q(D)\)。对每个非零 \(v_i\)，投影过程在 \((-\delta/2,\delta/2)\) 的生成元是 \(c_i\partial_x^2\)，\(c_i=v_iQv_i^\top\)。正首本征函数 \(\cos(\pi x/\delta)\) 对应 \(\pi^2 c_i/\delta^2\)。零行贡献零。由概率乘积取负对数并除以 \(T\) 得到所述方向。原始域中的半宽为 \(\delta\)，逐条估计所用的是其半宽 \(\delta/2\)。

这里使用 Royen 的正式发表结果（*Far East Journal of Theoretical Statistics* 48(2), 2014, 139–145），引用中心 Gaussian 测度对中心对称凸集的相关不等式。退化有限维 Gaussian 向量可表示为其线性支撑上的标准 Gaussian 的像。[作者预印本 v2](https://arxiv.org/abs/1408.1028v2)

## 一个函数同时控制全部坐标

若 \(\lambda_Q(K)\le b\operatorname{tr}Q\) 对所有正对角 \(Q\) 成立，则存在同一个非负 \(f\in H^1_0(K)\) 满足 \(\|f\|_2=1\) 以及 \(E_i(f)=\|\partial_i f\|_2^2\le b\) 对全部 \(i\) 成立。

令 \(A=\{u:\exists f\ge0,\ \|f\|_2=1,\ E_i(f)\le u_i\ \forall i\}\)。用 \(h=\sqrt{\alpha f^2+(1-\alpha)g^2}\) 保持归一化。Sobolev 链式法则与 Cauchy–Schwarz 给出 \(E_i(h)\le\alpha E_i(f)+(1-\alpha)E_i(g)\)。在固定有界 \(K\) 中，能量有界意味着可取弱 \(H^1_0\) 和强 \(L^2\) 子列。下半连续性证明 \(A\) 闭。若 \(b\mathbf1\notin A\)，分离超平面的系数 \(w\) 因 \(A\) 向上封闭而非负。测试 \(Q_\epsilon=\operatorname{diag}(w_i+\epsilon)\) 后令 \(\epsilon\downarrow0\)，则 \(\inf_{u\in A}w\cdot u\le b\sum_iw_i\)，与严格分离矛盾。取绝对值可使 Rayleigh 商的见证非负。

本机 SymPy 1.14.0 精确核对了条带本征方程、两个边界零值及平方积分 \(\delta/2\)。本模块核验了加条带和共同能量两个推理步骤。最终符号选择与滤波路径构造有另外的假设和证明。

OpenAI 预印本，PDF 5–6、8–11 页，Lemmas 2.3–2.5、3.1。SHA-256 d8924ac01b6d4dc0e70bd3fcb025132dc7fb66aa239dd7cb77d2310aa8f7b326。[The Euclidean Steinitz–Bergström theorem](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026/The-Euclidean-Steinitz-Bergstrom-theorem-September-24-2026.pdf)
