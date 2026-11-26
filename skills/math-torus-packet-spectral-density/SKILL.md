---
name: math-torus-packet-spectral-density
description: 对给定有理分段仿射扭转与有限角向 Fourier 包，精确计算模一推前的阶梯谱密度、色间正交门槛和可选 L1 密度差。
---

# 有限环面包谱密度

Use this for a supplied twist
\[
 S(\theta,u,a)=(\theta+\phi(u),u,a)
\]
on one good arc, where the supplied lift \(\phi\) is strictly increasing and rational piecewise affine. Each packet has a nonzero integer angular frequency \(m\) and a coefficient whose squared mass, after integrating the spare coordinate, is a nonnegative rational constant on a rational subinterval.

Run [the exact checker](scripts/check_torus_packet_spectral_density.py) on the finite arc, lift pieces, and packet list. It checks continuity and strict monotonicity of the lift, support inclusion, and the required disjointness of packets with equal angular frequency. For every affine overlap it applies
\[
 (m\phi\bmod1)_*(q\,du),\qquad
 p(z)=\sum_{u:m\phi(u)\equiv z\pmod1}\frac{q}{|m\phi'(u)|},
\]
splits every wrap point exactly, and emits rational step intervals for each color and their total. An optional second finite list produces the exact \(L^1\) difference of its total density and the first list's total density.

The source also gives color orthogonality for a finite disjoint packet list and the general estimate \(\|p_F-p_G\|_1\le(\|F\|_2+\|G\|_2)\|F-G\|_2\). The checker can certify the left-hand density difference, but it does not infer the right-hand side from unrelated packet masses. It does not construct a smooth global torus diffeomorphism, a passage, stationary-phase approximation, simple spectrum, or a limiting spectral theorem.

Read [the source scope](references/torus-packet-source.md) before transferring a calculation beyond its explicit finite input.
