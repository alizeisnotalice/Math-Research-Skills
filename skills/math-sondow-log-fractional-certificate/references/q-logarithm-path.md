# q-对数及几何指数尾的有理区间

当线性形式已归约到 Sondow--Zudilin 的 q-对数或到几何指数倒数和时，使用此页生成严格的有限区间。它并不构造 γ 的整数线性形式，也不单独执行无理性判据。

## 来源和范围

Jonathan Sondow、Wadim Zudilin，*Euler's constant, q-logarithms, and formulas of Ramanujan and Gosper*，本机原件为 arXiv:math/0304021v1，2003-04-02，`P09_Euler_s_constant_q_logarithms_and_formulas_of_Ramanujan_and_Gosper.pdf`，SHA-256 为 `80b8fdd56e422cb559f4e0dda4fb38e81eaa512f976ec7285a0918252fa04342`。正式版为 *The Ramanujan Journal* 12 (2006), 225–244，DOI [10.1007/s11139-006-0075-1](https://doi.org/10.1007/s11139-006-0075-1)。本机公式的逐页依据仍是上述预印本。

原件物理页 2 的式 (1) 定义

\[
 \ln_q(1+z)=\sum_{\mu\ge1}\frac{(-1)^{\mu-1}z^\mu}{q^\mu-1},\qquad |z|<q,quad |q|>1.
\]

本工具限制为整数 \(q\ge2\)、有理 \(0\le z<q\)。相邻两项的绝对值之比小于 \(z/q<1\)，故相邻的有限部分和给出严格的有理上下界。原件物理页 4 的 Lemma 1 还给出，对整数 \(n\ge0\)、\(0<k<q^{n+1}\)，

\[
 \sum_{\nu=n+1}^\infty\frac1{q^\nu+k}
 =\frac1k\ln_q\!\left(1+\frac{k}{q^n}\right).
\]

当 \(k=0\) 时，尾和以 \(1/[q^n(q-1)]\) 精确计算。脚本 [q_log_bounds.py](../scripts/q_log_bounds.py) 对两种对象都用 `Fraction` 输出端点，并拒绝超出已证明收敛和 Lemma 1 参数范围的输入。

```sh
python3 scripts/q_log_bounds.py q-log --q 2 --z 1/2 --terms 20
python3 scripts/q_log_bounds.py geometric-tail --q 2 --n 3 --k 1 --terms 20
```

第一个调用认证 \(\ln_2(3/2)\) 的区间。第二个调用认证 \(\sum_{\nu=4}^{\infty}(2^\nu+1)^{-1}\) 的区间。请求 `--z 2` 或 `--k 16`（当 \(q=2,n=3\)）会因违反适用条件而拒绝。

## 和 \(\gamma\) 判据的接口

原件物理页 8–9 的 Theorem 2 对二进制积分要求充分大的 \(n\) 及 \(2^{n-1}\le m\le2^{n+1}\)。Theorem 3 的分数部分下界只有在无穷多个指标成立时才推出 \(\gamma\) 无理。单个经认证的 q-对数区间最多用于该指标的有限分母排除。

原件物理页 15–17 的三进制路线要求 \(m=6k<3^n+1\)，并引入额外的整系数递推。物理页 21–22 明确指出 \(q>2\) 的广义积分余项无法满足所需的小量清分母条件，且 \(q>3\) 时 \((1-x)^m\) 不能消除所有其他广义 Euler 常数。这个脚本仍可计算 q-对数和尾项，不能据此启动任何 \(q>3\) 的无理性结论。
