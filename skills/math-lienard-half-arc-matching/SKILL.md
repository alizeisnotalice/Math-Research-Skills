---
name: math-lienard-half-arc-matching
description: 将已验证的 Lienard 半平面弧坐标匹配转化为周期轨道与孤立零点问题；不用于未经认证的数值积分或周期数上界。
---

# Lienard half-arc matching

Use this method for the smooth classical Lienard system
\[
 \dot x=y-F(x),\qquad \dot y=-x,
\]
only after the two half-arc midpoint functions have genuinely been constructed on a common open transverse-width interval. It reduces a geometric periodic-orbit question to the scalar matching function; it is not a numerical procedure for constructing those functions.

## Required input

State `F in C^infty(R)` and `F(0)=0`. On each half-plane put
\[
 u=x^2/2,\qquad \phi_\pm(u)=F(\pm\sqrt{2u}).
\]
For a peak-to-axis arc of `u_y=phi_±(u)-y`, verify the source construction's transverse endpoint hypotheses: its height-zero endpoints are `a_±(r)<0<b_±(r)` on an open width interval `I_±`, and its midpoint
\[
 M_\pm(0,r)=(a_\pm(r)+b_\pm(r))/2
\]
is smooth with `|∂_r M_±|<1`. Work only on `I=I_+ intersection I_-`; an empty intersection certifies no nonconstant periodic orbit through this route.

## Matching conclusion

Form `Delta(r)=M_+(0,r)-M_-(0,r)`. On `I`, zeros of `Delta` are in bijection with images of nonconstant periodic solutions. A zero is isolated if and only if its corresponding periodic orbit is isolated. In particular, a multiple isolated zero remains a limit cycle, while a zero interval and its endpoints inside `I` do not.

Read [the proof and scope record](references/half-arc-matching.md) before transferring this conclusion. The record gives the reconstruction, the local-return argument, source locator, and a zero-profile calculation. To establish a number of cycles, certify the zeros of `Delta` separately (for example by a validated scalar procedure); neither this skill nor the cited proposition supplies a numerical integrator, a zero count, or the quintic paper's at-most-two theorem.
