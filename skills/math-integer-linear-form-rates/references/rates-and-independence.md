# 指数率、有限下界与独立性

Zudilin *An essay on irrationality measures of π and other logarithms*，本机 EXT-0154 为 [arXiv:math/0404523v2](https://arxiv.org/abs/math/0404523v2)，SHA-256 `48f58b01e77eebd9b6cc6f2b0b86e9d5c9b7d588861020316fb6975bd1b8ba0d`。PDF 物理页 2，Proposition 1 引用 Lemma 3.1，给出整数线性形式双边指数率与无理性指数的关系。这里独立推导实数、普通整数系数的版本。

## 给定分母

对正整数 \(b\)，取满足 \(bUs^n\le1/2\) 的最小 \(n\ge n_0\)。给定任意整数 \(a\)，令 \(\Delta=q_n a-bp_n\)。由
\[
\Delta=b\ell_n-q_n(b\xi-a)
\]
得到两种情况：

1. \(\Delta\ne0\) 时 \(|\Delta|\ge1\)，故 \(|\xi-a/b|\ge1/(2bQA^n)\)。
2. \(\Delta=0\) 时 \(\xi-a/b=\ell_n/q_n\)，故 \(|\xi-a/b|\ge Lr^n/(QA^n)\)。

取两条下界的较小值即可覆盖所有 \(a\)。第二种情况需要余项的正下界，快速趋零的上界无法提供这一项。

## 无理性指数

若
\[
\limsup_{n\to\infty} \frac{\log|q_n|}{n}\le C_1,\qquad
\lim_{n\to\infty}\frac{\log|\ell_n|}{n}=-C_0,\quad C_0,C_1>0,
\]
则 \(\mu(\xi)\le1+C_1/C_0\)。取 \(\varepsilon\in(0,C_0)\)，可在充分大的同一首指标取 \(A=e^{C_1+\varepsilon}\)、\(r=e^{-C_0-\varepsilon}\)、\(s=e^{-C_0+\varepsilon}\)，三个比例常数取一。所选 \(n\le \log(2b)/(C_0-\varepsilon)+O(1)\)。两种行列式情况分别给幂指数 \(1+(C_1+\varepsilon)/(C_0-\varepsilon)\) 和 \((C_1+C_0+2\varepsilon)/(C_0-\varepsilon)\)。令 \(\varepsilon\downarrow0\)。若目标原先未证明无理，证得一列非零整系数余项趋零已足够，因为有理目标的既约分母乘上余项会给出趋零非零整数。指标若有空缺，须另外控制可取 \(n\) 相对 \(\log b\) 的增长。

## 共享分母的独立性

设 \(\ell_{i,n}=q_n\xi_i-p_{i,n}\) 对 \(i=1,2\) 均趋零，三个系数均为整数，且最终 \(q_n\ne0\)。若对每个固定的非零整数对 \((b_1,b_2)\)，组合 \(b_1\ell_{1,n}+b_2\ell_{2,n}\) 在无穷多个指标非零，则 \(1,\xi_1,\xi_2\) 有理线性无关。假设 \(b_0+b_1\xi_1+b_2\xi_2=0\)，该组合就是整数 \(-b_0q_n-b_1p_{1,n}-b_2p_{2,n}\)，与非零且趋零矛盾。若最终二者非零且 \(\ell_{1,n}/\ell_{2,n}\to0\)，上述组合非消失立即成立。若 \(\xi_1=\xi_2\) 且两条余项相同，各自非零趋零仍不能排除组合 \((1,-1)\)。

Postelmans–Van Assche 的 [arXiv:math/0604312v1](https://arxiv.org/abs/math/0604312v1) 物理页 3–4 的 Lemma 1.2 锁定共享分母与相对余项条件。该文具体的 \(q\)-zeta 构造还依赖各自的整性和精确渐近。本页采用上面的独立推导及其明确非消失条件。

## 精确回放

以 \(p_n+q_n\sqrt2=(1+\sqrt2)^n\)、\(n\ge1\) 为例。另一嵌入给出 \(|q_n\sqrt2-p_n|=(\sqrt2-1)^n\)。平方比较得到 \(2/5<\sqrt2-1<5/12\)，而 \(q_n\le(5/2)^n\)。因此用以下经证明的输入运行：

```sh
python3 scripts/linear_form_bound.py 5 --first-index 1 \
  --height-base 5/2 --height-scale 1 --lower-base 2/5 --lower-scale 1 \
  --upper-base 5/12 --upper-scale 1
```

把 `--upper-base` 改成 1 会拒绝输入。不能用这个例子为别的常数认证速率。
