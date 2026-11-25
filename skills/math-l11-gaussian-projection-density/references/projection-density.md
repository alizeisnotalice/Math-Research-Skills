# 从 ambient ball growth 到精确投影密度

这是默认入口的直接可用部分。令 \(\gamma_m\) 为 \(m\times d\) 独立标准 Gaussian 矩阵的分布，\(\lambda_m(dA,dy)=\gamma_m(dA)dy\)。对有限正 Borel 测度 \(\mu\)，\(\eta_\mu\) 是 \(\gamma_m(dA)\mu(ds)\) 经 \((A,s)\mapsto(A,As)\) 的像测度。

## 输入与精确结论

设 \(d,m\ge1\)、整数 \(p\ge2\)、\(\beta>m+p-2\)，且 \(\mu\) 支持于 \(B(z,R)\)，满足

\[
 \mu(B(x,r))\le H r^\beta\qquad(x\in\mathbb R^d,r>0).
\]

对 \(0\le j\le p-2\)，设

\[
 J_j=1+\frac{3^j2^\beta m}{\beta-j-m},\qquad
 B=(2\pi)^{-m(p-1)/(2p)}HR^{\beta-m(1-1/p)}
 \left(\prod_{j=0}^{p-2}J_j\right)^{1/p}.
\]

则 \(\eta_\mu=F\lambda_m\)，其中 \(F\) 可选为非负 jointly Borel 版本，且

\[
 \lVert F\rVert_{L^p(\lambda_m)}\le B.
\]

可令它在

\[
 E_{z,R}=\{(A,y):y\in Az+A B(0,R)\}
\]

外为零。这里是矩阵–标签空间的结论；它不是对每一个固定 \(A\) 的 pointwise density 断言。

## 可重放的证明接口

令 \(V=[s_2-s_1,\ldots,s_p-s_1]\)。依次按到先前 affine span 的距离积分，得到

\[
 \int\det(V^TV)^{-m/2}\,d\mu^{\otimes p}
 \le H^pR^{\beta p-m(p-1)}\prod_{j=0}^{p-2}J_j.
\]

对 \(\varphi_\delta=N(0,\delta^2I_m)\)，

\[
 \mathbb E_A\int\prod_{i=1}^{p}\varphi_\delta(y-As_i)dy
 =(2\pi)^{-m(p-1)/2}
 \det\!\left(V^TV+\delta^2(I+\mathbf1\mathbf1^T)\right)^{-m/2}.
\]

半正定加项不减行列式；先得平滑密度的统一 \(L^p\) 界，再以紧支撑测试函数、极限与 \(L^p\) 对偶导出 exact-image density。不能省去最后一步而把 \(F_\delta\) 的界直接称为 exact-label density。

共同支持的体积为

\[
 \lambda_m(E_{z,R})=v_mR^m\mathbb E\sqrt{\det(AA^T)}
 \le R^m(2\pi e d/m)^{m/2}.
\]

这一体积与 density 中的 \(R^{-m(1-1/p)}\) 在 Hölder block estimate 中恰好恢复局部质量的 \(r^a\) 次幂。

## 有限状态 block 接口

若未来成功函数 \(h_j:S^{d-1}\to[0,1]\) 在同一 scale \(R_0\) 满足

\[
 \int_{B(z,r)}h_jd\sigma\le(R_0r)^a,
\]

并且 block routing kernels \(g_j(A,As)\) Borel、\(0\le g_j\le1\)、\(\sum_jg_j\le1\)，那么在来源给定的 parameter regime 中，路由前成功质量的 scale 至多变为

\[
 R_0' =R_0\exp(Cd/a)N^{1/(aq)}.
\]

使用前必须给出 \(N\) 的真实有限上界：包括 state、停止时间和为下一 block 留存的其他离散标签。这个接口只控制一块；多块迭代及终端 success-to-information 转换另有额外前提，见 skill 主文件的条件性边界。
