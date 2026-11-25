# Brent–McMillan B3 的有理区间

用于消去浮点误差，复核 \(\gamma\) 的有限位值或候选逼近。输入整数 \(n\ge138\)，取 \(N=5n\)。约定 \(H_0=0\)，计算
\[
 \begin{aligned}
 I&=\sum_{k=0}^{N-1}\frac{n^{2k}}{(k!)^2},&
 S&=\sum_{k=0}^{N-1}H_k\frac{n^{2k}}{(k!)^2},\\
 T&=\frac1{4n}\sum_{k=0}^{2n-1}
        \frac{((2k)!)^3}{(k!)^4(16n)^{2k}},&
 Q&=\frac SI-\frac{T}{I^2}.
 \end{aligned}
\]
Taylor 两式使用 \(N\) 项，乘积项使用 \(2n\) 项。用相邻权重比复算，\(T\) 的和内权重从 \(1\) 开始，第 \(k\) 项除以前一项为 \((2k-1)^3/(32kn^2)\)。

Brent–Johansson 期刊版 Theorem 4.1 与 Corollary 4.3 给出
\[
 |Q-\log n-\gamma|<24 e^{-8n}.
\]
推论要求 \(n\ge138\)、\(N\ge\alpha n\)，其中 \(\alpha(\log\alpha-1)=3\)。取 \(N=5n\) 满足门槛，因为 \(\log 5>8/5\)。后一个严格不等式可用 \(z=2/3\) 的对数级数前六项直接证明。勘误将期刊式 (2.7) 的输入限定为 \(x\ge1\)，此处的 \(x=2n\) 满足该条件。

## 有理闭区间

由 \(e>8/3\)，取正有理数 \(E=24(3/8)^{8n}\)。令 \(n=2^j x\)，其中 \(1\le x<2\)。分别围住 \(\log 2\) 与 \(\log x\)。对 \(u\in[1,2]\) 令 \(z=(u-1)/(u+1)\)，前 \(m\) 项及尾界为
\[
 L_m(u)=2\sum_{k=0}^{m-1}\frac{z^{2k+1}}{2k+1},
 \qquad
 0\le\log u-L_m(u)\le\frac{2z^{2m+1}}{(2m+1)(1-z^2)}.
\]
当 \(z\le1/3\)，每个尾界至多 \((3/4)9^{-m}\)。取 \(m\) 使此量至多 \(E/(j+1)\)，调用 Sondow 证书中的同一有理对数函数，得 \(\ell\le\log n\le h\) 且 \(h-\ell\le E\)。于是
\[
  Q-h-E\le\gamma\le Q-\ell+E.
\]
精确 Fraction 计算 \(I,S,T\) 与两个端点。十进制输出对下端点向下取整、对上端点向上取整。仅当两个精确端点在所问格子的向下取整相同，才认证共同十进制前缀。用该区间比较 \(|q\gamma-p|\) 时，先按 \(q\) 符号乘区间，再减 \(p\)。

运行 [有理区间脚本](../scripts/brent_mcmillan_interval.py)。在 \(\gamma\) 无理性研究中，它提供有限输入的符号、误差和非消失核验。研究整数线性形式的无限子列依然需要统一算术论证。

## 从闭区间排除有限分母

用整数夹住整个区间。如果区间含有整数，最小既约分母为 1。否则用相邻整数作为初始端点 \(a/b<c/d\)，两端严格在区间之外且 \(bc-ad=1\)。任何夹在两端的既约 \(p/q\) 都满足
\[
 (p,q)=(cq-dp)(a,b)+(bp-aq)(c,d).
\]
两个乘数都是正整数，故 \(q\ge b+d\)。比较中项 \((a+c)/(b+d)\) 与目标闭区间。中项落在区间内即可返回，若落在区间外则替换对应一侧，保留行列式为 1。脚本用整式不等式一次跳过同向的多次更新。若有可行有理数在区间内，其分母总不小于当前的 \(b+d\)，而每个未结束步骤增加 \(b+d\)，因此搜索停止。

本机以有理数复跑 \(n=138\)、\(N=690\) 的区间，宽度小于 \(10^{-468}\)，并认证 400 位共同十进制前缀。对该区间执行最小分母搜索，所得最小分母超过 \(10^{234}\)。因此若 \(\gamma\) 有理，其分母超过这一门槛。另在 8,128 个小有理闭区间上通过逐分母穷举验收。

```sh
python3 scripts/brent_mcmillan_interval.py --n 138 --places 400 --exclude-denominators
```

## 版本与出处

- Richard P. Brent 与 Fredrik Johansson，*A bound for the error term in the Brent-McMillan algorithm*，*Mathematics of Computation* 84 (2015), 2351–2359。实际采用期刊版 Theorem 4.1 和 Corollary 4.3。对应本机 arXiv:1312.0039v1，PDF pp. 7–9，Theorem 1 与 Corollary 2，SHA-256 为 0f91cf7757be471d4e7d34f1248f1ae8ffedb4791919d44bf7661ede24985ce0。[期刊原文](https://maths-people.anu.edu.au/brent/pd/rpb256.pdf) [作者勘误](https://maths-people.anu.edu.au/brent/pub/pub256_errata.html)
- Jean-Pierre Demailly 的正式论文见 *Moscow Journal of Combinatorics and Number Theory* 7(4), 271–306 (2017)。本机 PDF 为 HAL-01377144v2，SHA-256 为 54e02390d45d08dd2962a57349c37bea8cee67d959dfe43c94f1618620c783d6。另有 R. B. Paris，*Journal of Mathematics Research* 11(3), 60–66 (2019)，本机 arXiv:1809.04342v2，SHA-256 为 ac75af081586e59595491e6da33b8ca5064783fd38c3ebd7c89044566a4ae75f。这两篇的更精细余项描述适合比较渐近项。当前区间的严格误差预算采用上列 Brent–Johansson 界。[Demailly 作者稿](https://www-fourier.univ-grenoble-alpes.fr/~demailly/source_files/gamma_brent_mcmillan/gamma_brent_mcmillan_HAL.pdf) [Paris 期刊版题录](https://doi.org/10.5539/jmr.v11n3p60)
