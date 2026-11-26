---
name: math-l19-coordinate-ring-certificates
description: 验证坐标环构造中的 cusp 关系、非单位除法消元和环境临界点证书。适用于需要从显式关系证明商环为多项式环的局部代数步骤。 包含线性多项式结式与专门化最大公因数的有限检查。
---

# 坐标环的显式消元证书

此技能处理一个可直接复核的局部代数模式。给定含单位元的交换环
\(B\)，元素 \(h,x,y,s\in B\) 满足
\[
 x^2+y^3=hs,\qquad (h,y)=B,
\]
令
\[
 S(h,U,V,W)=2U^3V+3U^4W+h(V^2-3U^2W^2)+h^2W^3.
\]
则
\[
 B[U,V,W]/(U^3+hV-x,\,-U^2+hW-y,\,S(h,U,V,W)-s)\simeq B[T].
\]

适用时必须实际提供 \(\alpha,\beta\in B\)，使
\(\alpha h+\beta y=1\)。这不是“\(h\) 或 \(y\) 可逆”的假设，也不能以在分式域中的除法代替。

1. 作可逆替换 \(G=V+UW\)。在 \(hW=y+U^2\) 下，三关系化为
   \[
   hG-yU=x,\quad hW=y+U^2,\quad y^2W=s-hG^2+2UyG.
   \]
2. 在 \(A=B[U,G]/(hG-yU-x)\) 中，令
   \(a=y+U^2\)、\(b=s-hG^2+2UyG\)。先验证
   \(y^2a-hb=0\)。令
   \(r=\alpha(1+\beta y)\)、\(q=\beta^2\)，则
   \(rh+qy^2=1\)，故 \(W_0=ra+qb\) 同时解两个线性关系。这证明 \(W\) 可消去，连同零因子情形。
3. 显式参数为 \(T=\alpha U+\beta G\)，其反向式为
   \[
   U=hT-\beta x,\qquad G=yT+\alpha x.
   \]
   逐个代回核验两个复合恒等。只有这些恒等式成立时，才可写出商环为 \(B[T]\)。

若用该消元识别某个特定纤维，再以环境梯度阻止给定多项式成为坐标，必须分开验证。一个临界点只否定该环境中的坐标多项式，因为坐标投影的梯度处处非零。它本身不证明商环同构、稳定坐标性质或取消猜想的结论。

参考 [cusp 消元与临界点验收](references/cusp-elimination.md)，其中固定了本机三篇 OpenAI 预印本的版本、页码和可采用范围。执行 [精确符号复放](scripts/check_cusp_certificates.py) 可复核此技能的恒等式、临界点及有零因子的单位理想系数例。

## OpenAI 原稿中的方法

- [Exact Jordan strata after determinant normalization](references/openai-arithmetic-2.md)

- [Stable coordinate in four variables](references/stable-coordinate-four-variables.md)

## 补充来源中的方法

- [Quartic rational Diophantine quadruple source model](references/c07-07-euler-surface.md)
- [Resultant gcd screen for a linear factor and polynomial](references/c07-07-resultant-gcd.md)
- [Effective unit-equation enumeration in a coordinate ring](references/evertse-gyory-unit-equation-enumeration.md)
