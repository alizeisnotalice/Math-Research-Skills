# Mahler 右因子与 Riccati 余项

令 \(\sigma f(x)=f(x^b)\)，\(b\ge2\)，并令
\(L=\ell_r\sigma^r+\cdots+\ell_0\)，其中 \(\ell_0\ell_r\ne0\)。候选 \(u\) 满足
\[
\ell_r u\,\sigma(u)\cdots\sigma^{r-1}(u)+\cdots+\ell_2u\sigma(u)+\ell_1u+\ell_0=0
\]
时，右 Euclidean 除法的余项为零，因此 \(\sigma-u\) 是 \(L\) 的一阶右因子。脚本逐项组成这个有理函数恒等式。

来源为 Frédéric Chyzak、Thomas Dreyfus、Philippe Dumas、Marc Mezzarobba，*First-order factors of linear Mahler operators*，本机 arXiv:2403.11545v3，SHA-256 `a20b664157d4b928a677385877afc9f6764931fb6b573b0652e1ccd42871c815`。物理页 10 的 Lemma 2.1 给出右因子与 Riccati 方程的充要关系和右除法证明。该论文后续的完整因子搜索还依赖差分域、广义级数与算法构造，本入口不采用那些部分。
