# 一个困难坐标的共正最小值有限枚举

Oertel 与 Schürmann 在 *On Computing the Copositive Minimum and its Representatives* 的物理页 12–13，Lemma 5.1，将只有最后一个困难坐标的情形化为固定切片的凸二次规划。对于

\[
Q=\begin{pmatrix}A&q\\q^T&c\end{pmatrix},\qquad A\succ0,
\]

在 \(y\ge0\)、末坐标为 \(s\) 的切片极小值满足 \(f(s)=s^2f(1)\)。若 \(f(1)>0\)，任意整数 \(x\ge0\) 且 \(Q[x]\le\lambda\) 有 \(x_n\le\lfloor\sqrt{\lambda/f(1)}\rfloor\)。这里的 \(f(1)\) 是**非负约束**切片的值。固定 \(x_n=s\) 后，完成平方应当使用无约束 Schur 值

\[
\sigma=c-q^TA^{-1}q,
\]

而非一般情形下的 \(f(1)\)：

\[
Q[(y,s)]=(y+sA^{-1}q)^TA(y+sA^{-1}q)+s^2\sigma.
\]

因此可由 \(A\succeq\mu I\) 得到每个其余整数坐标的有限区间。若 \(y_\ast\ge0\) 是切片 \(s=1\) 的 KKT 最优点，则

\[
f(1)=\sigma+(y_\ast+A^{-1}q)^TA(y_\ast+A^{-1}q)\ge\sigma.
\]

只有无约束极小点 \(-A^{-1}q\) 本身非负时才有 \(f(1)=\sigma\)。边界 KKT 情形通常有严格不等式；故本工具仅用 \(f(1)\) 界定最后坐标，而在完成平方和其余坐标盒界中使用 \(\sigma\)。

`certify_one_difficult_coordinate.py` 要求有理矩阵、精确 KKT 最优点和正的有理谱下界 \(\mu\)。它用 Sylvester 主子式核验 \(A\succ0\) 及 \(A-\mu I\succ0\)，再逐点枚举并直接计算二次值。输入证书建立有限覆盖，不自动证明原矩阵共正、严格共正或属于 SPN。多困难坐标和浮点 QP 输出不适用。

```sh
python3 scripts/certify_one_difficult_coordinate.py examples/one-difficult-coordinate-positive.json
python3 scripts/certify_one_difficult_coordinate.py examples/one-difficult-coordinate-invalid-kkt.json
```
