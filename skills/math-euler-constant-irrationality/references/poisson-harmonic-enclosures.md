# Poisson 调和数与有理区间

需要用单个对数和简单的正余项构造 \(\gamma\) 有理区间时使用。输入为 \(N\ge1\)、调和项截断阶 \(m\) 和对数项数 \(j\ge1\)。输出为严格包住 \(\gamma\) 的有理区间。若还给定 \(p/q\)，同时返回 \(q\gamma-p\) 的区间和有限排除结果。

## 原文与变形

Adell–Lekuona，*Mathematics of Computation* 89(325) (2020), 2553–2561。原始下载文件 \(\texttt{G26-supp.pdf}\) 为期刊排版前的作者稿。SHA-256 为
`02e459a234ae8fbd961e4240142cc70886803e7d40f064e9fade148f81656d25`。
本地物理页 4，Lemma 2.1 (2.7)，把 \(\mathbb EH(N_\lambda)\) 写成全收敛级数。物理页 5，Theorem 3.1 (3.1)，给出带正余项的恒等式。物理页 7，Corollary 3.4，专门化到 \(\lambda=2^N\)。使用期刊版书目，保留本地版本定位。[正式论文](https://doi.org/10.1090/MCOM/3528)

令 \(\lambda=2^N\)，则
\[
\gamma=-\sum_{k\ge1}\frac{(-\lambda)^k}{k!\,k}
       -N\log 2-J_\lambda,\qquad
J_\lambda=e^{-\lambda}\int_0^\infty\frac{e^{-t}}{\lambda+t}\,dt.
\]
将原文正余项转为有理区间时，分别计算以下三项。

1. 在 \(m\ge\lambda-1\) 处截断交错级数。第 \(k\) 项到第 \(k+1\) 项的绝对值比为 \(\lambda k/(k+1)^2<1\)（\(k\ge m+1\)）。因此精确部分和与加上首个遗漏项后的第二个部分和给出两个端点，按符号排序。
2. 用 \(\log2=2\sum_{r\ge0}1/[(2r+1)3^{2r+1}]\)。保留前 \(j\) 项，几何尾界为 \(9/[4(2j+1)3^{2j+1}]\)。取端点时把 \(N\log2\) 的上界从左端扣掉。
3. \(0<J_\lambda<1/[\lambda\sum_{k=0}^m\lambda^k/k!]\)。下端扣除此上界，上端使用零。固定 \(\lambda\) 时，增大两种截断阶之后，此项的保守区间仍保留宽度。

## 本机回放

使用 [有理区间脚本](../scripts/poisson_harmonic_interval.py)。默认 \(N=4,m=64,j=9\)。两次回放可用：

```sh
python3 scripts/poisson_harmonic_interval.py --power 4 --candidate 1/2
python3 scripts/poisson_harmonic_interval.py --power 3 --candidate 57721566/100000000
```

- 正例 \(p/q=1/2\)。严格判定 \(2\gamma-1>0\)。
- 边界例 \(N=3\)，\(p/q=57721566/100000000\)。当前精度的清分母区间包含零，状态为未判定。可加大 \(N\) 或调用 [Brent–McMillan 区间](brent-mcmillan-enclosure.md)。

对近似值做高度审计时，比较的是同一个既约 \(p/q\) 的 \(q\gamma-p\)。当区间含零时无从认证符号。有限区间及有限分母排除的范围均由实际输入决定。研究无穷整数形式时，参照 [混合形式和高度](mixed-log-height-audit.md) 记录统一的非零性及清分母后的余项。
