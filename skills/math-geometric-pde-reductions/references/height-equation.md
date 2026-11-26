# Necessary height equation for a surface immersion

Source: *A Smooth Metric with No Local Isometric Immersion into Three-Space*,
OpenAI, 24 September 2026, Lemma 2.1, physical PDF page 4.  Local PDF SHA-256:
`6c2cf05d89a23473c52fecb2aea37bcbda7279db50004cf0b212b000430bd374`.

Let \(F:(M^2,g)\to\mathbb R^3\) be a smooth isometric immersion, let \(n\)
be a chosen unit normal, let \(e\in\mathbb R^3\) be unit and constant, and
put \(z=\langle F,e\rangle\), \(\nu=\langle n,e\rangle\).  The Gauss formula
gives
\[
  \nabla_g^2z=\nu II.
\]
Splitting \(e\) into tangential and normal parts gives
\( |dz|_g^2+\nu^2=1\).  Taking determinants and using the Gauss equation
\(\det II=K\det g\) yields
\[
  \det(\nabla_g^2z)=K\det(g)(1-|dz|_g^2).
\]
At a point where \(e=n\), \(dz=0\), \(\nu=1\), and
\(\nabla_g^2z=II\).  These are all necessary statements and are the only
ones certified by the residual checker.

The equation is not a reconstruction theorem.  Even algebraically, take the
Lorentz-signature tensor \(g=dx^2-dy^2\) and \(z=x\): \(K=0\),
\(\det\nabla_g^2z=0\), and the displayed residual is zero, but no Euclidean
isometric immersion can induce an indefinite metric.  Thus a zero residual
cannot even replace the positive-definiteness hypothesis, much less certify a
requested local or global immersion; it also omits the Gauss--Codazzi/
reconstruction and domain/boundary data.

命令读取 `x`、`y`、`pi`、精确整数字面量及有理小数，支持四则、幂和 `sin`、`cos`、`exp`、`sqrt`。有理函数用分子多项式判断残差恒等性。若符号化简无法确定非有理式的恒等性，返回 `undecided`。

运行[立体投影算例](../examples/sphere_stereographic.md)时，用 [Python 环境选择](../../python-math/SKILL.md)载入 SymPy。
