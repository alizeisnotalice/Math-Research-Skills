# Prévost 的二进 Legendre–Padé 有理逼近

计算指定 \((n,m)\) 的 Padé 有理逼近、约分后分母和含 \(\gamma\) 的严格区间。适用 \(n\ge1,\ 0\le m\le n,\ b=n-m+1=2^p\)。取
\[
 c_k=(-1)^{n+k}\binom nk\binom{n+k}k,\qquad
 \widetilde L_{n,m}=pR_n(1)+\sum_{k=0}^{n}c_k R_n(k/b),
\]
其中 \(R_n\) 是原文给出的 \(\log(1+x)\) 的 \([n/n]\) Padé 式。输出有理近似 \(2H_n-\widetilde L_{n,m}\) 及其既约分母。

按[分数部分与余项工具](prevost-legendre-fractional-gate.md)的有理级数求 \(L_{n,m}\in[\ell,u]\)，用 Beta 界取得 \(J_{n,m}\in[j_-,j_+]\)。\(m\) 偶数时下端为 0，奇数时上端为 0。于是
\[
 \gamma\in [2H_n-u+j_-,\,2H_n-\ell+j_+].
\]
以同一端点包围 \(L_{n,m}-\widetilde L_{n,m}\) 和该 Padé 近似的误差。增大 --log-terms 只缩小对数部分。结果提供单个指标的误差和分母，统一的分母增长率与无穷指标证明仍需另外建立。

~~~sh
python3 -B scripts/prevost_pade_rational_interval.py 7 0 --log-terms 32
~~~

本机原稿为 Marc Prévost 2007 年 6 月 25 日手稿，SHA-256 为 daf112a9a9a8f9e6f25e9e9cb04fce8f2356c10644654b90ce411ca8c864af56。物理页 8–9 给出 \(J,L,2H_n\) 的关系，页 9–12 的式 (38)–(47) 与 Theorem 5 给出有理替换。这里用有理对数区间和 Beta 界计算误差。[期刊版](https://doi.org/10.1016/j.cam.2007.09.015)。
