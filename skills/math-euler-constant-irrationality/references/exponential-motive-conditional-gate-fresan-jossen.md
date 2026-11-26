# Euler--Mascheroni 指数动机的条件结论门槛

对 Fresán--Jossen 所构造的指数动机 \(M(\gamma)\)，只在调用者已经给出指数动机范畴、Betti/de Rham 实现及比较同构的前提下使用本页。输入还须明确采用原文的指数周期猜想。它不是 \(\gamma\) 无理性的无条件方法。

## 已核对的局部构造

在 \(X=\operatorname{Spec}\mathbb Q[x,y]\) 上取 \(f=xy\)，令 \(Y\) 为 \(xy(x-1)(y-1)=0\) 的四条直线并在 \((1,1)\) 吹起。原文把吹起诱导映射的像定义为 \(M(\gamma)\)。其所列周期矩阵含有

\[
\begin{pmatrix}1&0&\gamma\\0&e^{-1}&E_1(1)\\0&0&2\pi i\end{pmatrix},
\]

其中第一行对应 \(\gamma_\square-\gamma_\triangle\)。Proposition 12.8.7 证明

\[
0\longrightarrow\mathbb Q(0)\longrightarrow M(\gamma)
 \longrightarrow\mathbb Q(-1)\longrightarrow0
\]

为非平凡扩张。此处的几何构造和非分裂性可作来源限定的结构事实，不能替代数值逼近、整系数线性形式或分母排除。

## 条件结论

若明确附加 Exponential Period Conjecture，Corollary 12.8.8 给出 \(\gamma\) 与 \(2\pi i\) 的代数独立性，Corollary 12.8.12 给出 \(\gamma\) 在通常 periods 所生成域上的超越性。缺少该猜想时，报告前述扩张和周期矩阵，停止于条件门槛。

## 来源范围

Javier Fresán and Peter Jossen, *Exponential motives*, authors' preprint, 2024，物理页 277--284，式 (12.8.0.1)、Definition 12.8.2、\S12.8.5、Proposition 12.8.7、Corollaries 12.8.8 与 12.8.12。本机 SHA-256 `7da885c162606b3c7a2b377d532e59097e51a6856c7f9ba75071d559d2e5ebf5`。局部构造还依赖该稿第 2--8 章建立的范畴与比较实现。
