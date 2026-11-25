# 有限域扩张与一元乘法迹

## 特征二的平方扩张

从 \(\mathbb F_2\) 开始。对每个已构造的有限域 \(K\)，\(x\mapsto x^2+x\) 是加法同态，核为 \(\{0,1\}\)，像恰占一半。穷举 \(a\) 和候选原像，选 \(a\) 不在像中，则 \(X^2+X+a\) 无根且不可约。以二次商 \(K[X]/(X^2+X+a)\) 扩域，域大小平方。重复直到 \(|K|>\Delta\)，最终大小至多 \(\max(2,\Delta^2)\)。以二元组表示元素，保留每层的 \(a\)，并以 \(X^2=X+a\) 约化乘法。穷举中只需计数器和递归算术，适合控制空间；运行时间还需要独立评估。

本机从 \(X^2+X+1\) 得到 \(\mathbb F_4\)，枚举自映射像为 \(\{0,1\}\)，取生成元为下一常数，验证所得 16 元表示中每个非零元素都恰有一个逆元。

## 复原一元乘法迹

设 \(f\) 为特征零域上的首一 \(n\) 次多项式，\(v\) 为任意多项式。以 \(1,x,\ldots,x^{n-1}\) 作商代数基。令 \(M_v\) 为乘 \(v\) 后模 \(f\) 的矩阵，则
\[
\operatorname{tr}M_v=[x^{n-1}]\big((vf')\bmod f\big).
\]
当根 \(\lambda_i\) 互异，在分裂域内按根求值给乘法迹 \(\sum_i v(\lambda_i)\)。对 \(vf'\) 的余式作 Lagrange 插值，第 \(i\) 项是 \(v(\lambda_i)f(x)/(x-\lambda_i)\)，最高系数为 \(v(\lambda_i)\)。首一除法下两侧都是 \(f,v\) 系数的多项式，因此在互异根的稠密开集恒等后也覆盖重根。须明确模数首一和商基。多变量正规序列不能直接照搬一元证明。

本机 SymPy 分别对 \(x^2-2,(x-1)^3,x^5-x-1\) 的乘法矩阵和余式最高系数得到 \(6,9,25\) 的相等结果。

- OpenAI 预印本 PDF 3 页，Lemma 2 的特征二塔；单带机器的整体模拟未用。SHA-256 873c9e2790a66c536fc6d38ab9005c177e2c64d0303b25f214a19a552398daff。[Simulating One-Tape Time in Two-Fifths-Power Space](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Simulating-One-Tape-Time-in-Two-Fifths-Power-Space-September-25-2026/article.pdf)
- OpenAI 预印本 PDF 12 页，Proposition 3.2 的迹与余式接口；本页独立证明一元特例。SHA-256 151fe6144a42154d5dd0ebb4f2e9b63641da74177ca7a53d50c829e8784a7c41。[Existential–universal real sentences in the counting hierarchy](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Existential-universal-real-sentences-in-the-counting-hierarchy-October-4-2026/etr-counting-hierarchy.pdf)
