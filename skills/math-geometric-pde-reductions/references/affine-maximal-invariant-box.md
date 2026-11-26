# Certified ODE continuation route

Source: *A Smooth Nonquadratic Entire Affine Maximal Graph in Dimension Ten*
(OpenAI, 5 October 2026), Proposition 2.1 and equations (8), (16)--(17),
Lemmas 4.1--4.2, PDF pp. 2--7; local copy SHA-256
`f7851c8489621a2df0e520d7aebe9c4dca5e6d3e68c9086d914b479dc9983da9`.

## Exact transfer statement

Let a solution of the radial system on an interval of positive radii have
positive \(F,P,y,y'\), let
\[
A=r y/F,\qquad B=r y'/y,\qquad D=(-rP'/P)/B,
\]
and suppose these variables satisfy, with \(s=\log r\),
\[
\begin{aligned}
A_s&=A(1+B-A),\\
B_s&=B(9+A+\tfrac{12}{11}BD-9B),\\
D_s&=(11-D)A-8D+BD(1-D/11).
\end{aligned}
\]
If \((A,B,D)\) begins in
\(K=[0,9/2]\times[0,7/2]\times[0,33/7]\), it remains in \(K\) for every
later time for which that ODE solution exists.

## Independent check of the route

At \(q=(9/2,7/2,33/7)\), direct rational substitution makes all three
components zero.  On \(K\), the cross derivatives needed to control the
upper faces are
\[
\partial_BV_1=A,\quad \partial_AV_2=B,\quad
\partial_DV_2=\tfrac{12}{11}B^2,\quad
\partial_AV_3=11-D,\quad
\partial_BV_3=D(1-D/11),
\]
which are nonnegative because \(0\leq D\leq33/7<11\).  Thus on an upper
face, the associated component is at most its value at \(q\), hence is
nonpositive.  On lower faces \(A=0,B=0,D=0\), the respective normal
components are \(0,0,11A\), hence inward.

For completeness, project a nearby point coordinatewise onto the box.  The
face inequalities give \((z-\Pi z)\cdot V(\Pi z)\leq0\).  Local Lipschitz
continuity gives \(\frac d{ds}\operatorname{dist}(z,K)^2\leq
2L\operatorname{dist}(z,K)^2\); Gronwall proves forward invariance.
The accompanying checker evaluates every displayed rational sign exactly.

## Reconstruction boundary

The source obtains this ODE only after the radial reduction
\[
y^8y'=r^8FP^{-12/11},\qquad (y^8P')'=-11r^8P^{-1/11},\qquad F'=y.
\]
Its local construction at \(r=0\), positivity, and compact-subset
continuation are extra hypotheses/arguments.  This note certifies none of
them and makes no assertion for other dimensions, ansatzes, or arbitrary
affine-maximal solutions.
