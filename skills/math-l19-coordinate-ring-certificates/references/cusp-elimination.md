# Cusp 消元与坐标障碍

## 已重推的关系

来源为 *An explicit noncoordinate polynomial with affine three-space zero fibre*，PDF pp. 2–4，SHA-256 `a0f2145ec95a6083a4a9a54ef4d2c41fa9587cd435c6908c512ce90e6c64154b`。固定原文为 [OpenAI 归档版本](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-explicit-noncoordinate-polynomial-with-affine-three-space-zero-fibre-September-24-2026/paper.pdf)。它是预印本。

在任意交换环上，原文 Lemma 2.1 的证明完全给出。设
\[
 x^2+y^3=hs,\quad \alpha h+\beta y=1.
\]
替换 \(G=V+UW\) 后，以
\[
 a=y+U^2,\quad b=s-hG^2+2UyG,
\]
有
\[
 y^2a-hb=(hG-yU)^2+y^3-hs=0.
\]
取 \(r=\alpha(1+\beta y)\)、\(q=\beta^2\)，则
\(rh+qy^2=1\)，所以 \(W_0=ra+qb\) 满足 \(hW_0=a\) 和 \(y^2W_0=b\)。而
\[
 W-W_0=r(hW-a)+q(y^2W-b),
\]
故这两个关系生成的理想为 \((W-W_0)\)。最后 \(T=\alpha U+\beta G\) 给出所需多项式参数。

这条证明不需要 \(B\) 为整环或 \(h,y\) 中任一元素可逆。所需的是实际的单位理想见证 \(\alpha,\beta\)。例如在 \(\mathbb Z/6\mathbb Z\) 中，\(h=2,y=3,\alpha=2,\beta=1\) 满足该见证，脚本对此也作了检查。

同一来源的 pp. 2、4 还给出一个不同层次的环境计算。若
\[
 x=u^3+hv,\quad y=-u^2+hw,
\]
且
\[
 s=2u^3v+3u^4w+h(v^2-3u^2w^2)+h^2w^3,
\]
则恒等式 \(x^2+y^3=hs\) 可直接展开验证。令
\(p=-2s^2x+3sy^2-3s^3y\)、\(F=h-p-1\)，在
\((h,u,v,w)=(2,0,-1/2,1/2)\) 有 \(F=-1\) 且所有四个偏导为零。该临界点只给出所述环境多项式的坐标障碍。

## 审计记录，未提升为通用规则

* *A stable coordinate that is not a coordinate in four variables*，PDF pp. 2–3，SHA-256 `52d49d150cf01ef08c0eb878d1fde75b17125437a276a9616b4df7f1adeedcaa`，[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-stable-coordinate-that-is-not-a-coordinate-in-four-variables-October-5-2026/stable-coordinate-four-variables.pdf)。它的关联分次环、局部幂零导子与线丛提升组成专门的全局反证链。该链中稳定性和主结论不作为本技能的可调用结论。
* *An explicit failure of complex affine-space cancellation*，PDF pp. 2–4，SHA-256 `91a1a2f28c960cba25dd268e0f5515f0cff31463e4342098bbd89f857dd82023`，[固定原文](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/An-explicit-failure-of-complex-affine-space-cancellation-September-23-2026/paper.pdf)。其中从残余坐标到一稳定坐标使用 Dutta–Lahiri，从过滤导子到最终障碍还使用一系列几何和外部工具。这里只保留为来源追踪，不能引用来断言一般取消失败。
