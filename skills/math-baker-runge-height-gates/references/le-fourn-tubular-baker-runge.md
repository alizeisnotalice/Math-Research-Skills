# Baker--Runge divisor-intersection height gate

Source checked: Samuel Le Fourn, *Tubular approaches to Baker's method for curves and varieties*, arXiv:1812.06306v2 (2019), Theorem 1.1 and Corollary 1.2, physical pp. 1--3.  The local version is the preprint corresponding to the cited publication in *Algebra & Number Theory* 14 (2020), 763--785, DOI: 10.2140/ant.2020.14.763.

For a smooth projective variety \(X/K\), ample effective divisors \(D_1,\ldots,D_n\), \(D=\bigcup_iD_i\), the source defines \(m_B\) from finite divisor intersections and requires, at each resulting point \(P\), a rational function \(\phi_P\) supported away from \(P\).  With \(m_Y\) defined by intersections contained in \(Y\), its Theorem 1.1 applies only when

\[
(m_B-1)|M_L^\infty|+m_Y|S\setminus M_L^\infty|<n.
\]

It then bounds \(h_D(Q)\) for the stated S-integral points outside an effective strict closed set \(Z\) by \(C C_1(d,s)h_LR_S\log^*R_S\).  Corollary 1.2 gives the curve form under the per-pole \((H)_P\) condition and \(|S\setminus M_L^\infty|<n\).

This is a conditional theorem interface, not an implementation of its effectivity.  Page 3 makes the missing quantitative inputs explicit: a projective embedding and equations, divisor/function expressions, an effective Nullstellensatz, and logarithmic-form estimates.  Those must be supplied independently before a numerical bound is reported.
