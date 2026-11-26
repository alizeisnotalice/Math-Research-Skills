# 加权弱型聚合证书

Tang--Wu 的 *Almost everywhere convergence of mock Fourier series for the middle-fourth Cantor measure*，arXiv:2607.27796v2，物理 PDF pp. 12--13 的 Lemma 5.1 给出下列有限及可数聚合步骤。

设 \((X,\nu)\) 为有限测度空间。每个 \(T_i\) 取非负扩展实值，且对所有 \(s>0\) 有

\[
 \nu\{T_i f>s\}\leq C_i\lVert f\rVert_1/s.
\]

若 \(a_i>0\) 且 \(\sum_i\sqrt{a_iC_i}<\infty\)，则

\[
 \nu\left\{\sum_i a_iT_i f>\alpha\right\}
 \leq \frac{\bigl(\sum_i\sqrt{a_iC_i}\bigr)^2}{\alpha}\lVert f\rVert_1.
\]

对有限表，给定正有理阈值 \(u_i\) 且 \(\sum_i a_i u_i\leq\alpha\)，事件包含于 \(\bigcup_i\{T_i f>u_i\}\)，所以直接得到常数 \(\sum_iC_i/u_i\)。源中的最优化取

\[
 u_i=\frac{\alpha\sqrt{C_i/a_i}}{\sum_j\sqrt{a_jC_j}},
\]

并由 Cauchy--Schwarz 得到显示的平方根常数。`check_weighted_weak_aggregation.py` 检查给定有限有理阈值的预算和并集界常数。它不检查任何算子的弱型假设。

可数情形还需要非负部分和的单调极限，以及 \(\sum_i\sqrt{a_iC_i}<\infty\)。这条引理本身不提供正交性、复值或符号抵消的极大不等式，也不单独导出几乎处处收敛。
