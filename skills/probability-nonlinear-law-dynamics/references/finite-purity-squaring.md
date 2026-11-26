# 归一化平方迭代与最大原子的尾质量

对有限概率向量 \((w_i)\)，令 \(s=\sum_i w_i^2\)、\(u=1-s\)、\(w_i'=w_i^2/s\)。由非负性直接得

\[
1-\sum_i(w_i')^2=\frac{2\sum_{i<j}(w_iw_j)^2}{s^2}
\le \frac{2(\sum_{i<j}w_iw_j)^2}{s^2}=\frac{u^2}{2(1-u)^2}.
\]

若最大原子为 \(1-x\)，其余原子的平方和至多 \(x^2\)，所以 \(2x(1-x)\le u\le 1-(1-x)^2\)。当 \(u<1/2\) 时，最大原子至少为 \(s>1/2\)，由小根分支得 \(x\le(1-\sqrt{1-2u})/2\)。程序返回根号内的精确有理数及等价的二次不等式。

相关原稿物理页 6 的 Lemma 3.1 印出了更强的式 (3.3)。取 \((13/14,1/14,0)\)，得到 \(u=13/98\)、\(x=1/14\)。原式要求 \(1-x\ge\sqrt{1-2u^2}\)，而 \(1-2u^2-(1-x)^2=985/9604>0\)。后续凡用该式的传播步骤需要另证。此处的有限概率结论由上面的非负代数独立给出。[固定原稿 PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-boundary-field-gap-for-the-spin-one-Heisenberg-chain-September-24-2026/paper.pdf)

```sh
python3 scripts/check_finite_purity_squaring.py 13/14 1/14 0
```
