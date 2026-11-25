# 凸体平移覆盖的窗口周期化

令 \(K\subset\mathbb R^n\) 为满维凸体，\(V=|K|>0\)，取 \(r>0\) 使 \(K\subset Q_r=[-r,r]^n\)。令 \(X\) 为局部有限中心集，满足 \(K+X=\mathbb R^n\)。记 \(\theta_{\rm per}\) 为所有全秩格点阵 \(\Lambda\) 和有限余类代表集 \(T\) 给出的覆盖密度 \(V|T|/\det\Lambda\) 的下确界。

## 从任意覆盖得到周期覆盖

对每个 \(a\in\mathbb R^n\) 和 \(L>0\)，令 \(S=X\cap(a+Q_{L+r})\)。每个 \(y\in a+Q_L\) 都有 \(y=k+x\)，故某个覆盖中心 \(x=y-k\) 在 \(S\) 中。闭窗口保留边界覆点。周期中心 \(S+2L\mathbb Z^n\) 覆盖整个空间。保留每个余类的一个代表，则
\[
\theta_{\rm per}\le \frac{V|S\bmod 2L\mathbb Z^n|}{(2L)^n}
\le \frac{V\,\#(X\cap(a+Q_{L+r}))}{(2L)^n}.
\]
取 \(R=L+r\) 得到立方体中心强度下界
\[
\frac{V\#(X\cap(a+Q_R))}{|Q_R|}
\ge \theta_{\rm per}(1-r/R)^n,\qquad R>r.
\]

## 传到球窗口与重叠重数

固定 \(L\)，设 \(\beta=\sqrt n(L+r)\)。在 \(a\in z+B_{R-\beta}\) 上积分上面的计数下界。被计数的中心都属于 \(z+B_R\)，单一中心在积分中出现的权重至多 \(|Q_{L+r}|\)。于是
\[
\frac{V\#(X\cap(z+B_R))}{|B_R|}
\ge \theta_{\rm per}\left(\frac{L}{L+r}\right)^n(1-\beta/R)^n.
\]
先令 \(R\to\infty\)，再令 \(L\to\infty\)，得到立方体和球的上下极限均至少为 \(\theta_{\rm per}\)。

反向取周期覆盖，选格点阵的有界半开基本平行体 \(F\subset Q_d\cap B_d\)。对 \(W_R=Q_R\) 或 \(B_R\) 以及每个 \(t\in T\)，以落入 \(z+W_R\) 的 \(t+\Lambda\) 点为基址的基本格元，其并包含 \(z+W_{R-d}\) 并包含于 \(z+W_{R+d}\)，边界可按零测集处理。夹逼得各余类的极限中心强度均为 \(1/\det\Lambda\)，且对 \(z\) 一致。取所有周期覆盖的下确界，四种窗口和上下极限定义给出的**最优**密度都等于 \(\theta_{\rm per}\)。

若 \(K\subset W_s\)，则平均重叠重数的积分 \(\sum_{x\in X}|(K+x)\cap W_R|\) 由 \(V\#(X\cap W_{R-s})\) 与 \(V\#(X\cap W_{R+s})\) 夹住。除以 \(|W_R|\) 取上、下极限即可。已覆盖区域的体积是 \(|W_R|\)，覆盖密度还取决于重叠次数。

## 核验记录

对 \(K=[0,1]^n\)、\(X=\mathbb Z^n\) 用 Python Fraction 检查了 4 个中心偏移、6 个半整数窗口尺度与 \(n=1,2,3\) 共 72 个组合。模周期去重后，各坐标圆周间隙至多 1，足以证明这些有限测试实例确实覆盖，且去重只降低所列强度。一般结论由上述窗口证明给出。

已核对 OpenAI 预印本 *Translative covering densities of order n log n*（2026-09-23）PDF 28–29 页 Appendix A, Proposition A.1 及重叠重数说明。SHA-256 为 `2944d4b3135b4d794626b13db292b869dfc58b4668a29f194e8fbcb542290a3e`。此证明使用窗口截取、体积夹逼和 Tonelli，不依赖手稿主体的高维随机构造。[固定版本 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Translative-covering-densities-of-order-n-log-n-September-23-2026/paper.pdf)
