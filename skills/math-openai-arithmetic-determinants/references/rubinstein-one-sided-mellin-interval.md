# One-sided Mellin zero exclusion on long intervals

For
\[
 G(x)=\sum_{n\geq 1}\Lambda(n)(x/n-1)_+-x\log x+(1+\gamma)x,
\]
put
\[
 F(s)=\int_1^\infty G(x)x^{-s-1}\,dx
      =-\frac{\zeta'(s)}{s(s-1)\zeta(s)}-\frac1{(s-1)^2}+\frac{1+\gamma}{s-1}
\]
initially for \(\operatorname{Re}s>1\).  The displayed subtraction cancels the pole at one, and a zero
\(\rho\) of \(\zeta\) in the critical strip produces a pole of \(F\), with residue
\(-m_\rho/[\rho(\rho-1)]\).

If a supplied analytic argument proves, for some \(0<\theta<1\),
\[
G(x)\leq x^\theta\quad\hbox{throughout }[Y,Y^{3/2}]
\]
for arbitrarily large \(Y\), then \(\zeta(s)\) has no zeros with
\(\operatorname{Re}s>\theta\).  This is a conditional transfer gate.  It requires the stated
normalization of \(G\), the Mellin identity with its pole accounting, and the upper bound on each
whole interval.  Bounds at isolated points or a numerical plot do not meet the gate.

The source's direct interval proof puts \(u=\log x\), takes Taylor coefficients of \(F\) at a fixed
real \(\sigma>2\), and chooses the coefficient order proportional to \(\log Y\).  The gamma-shaped
kernel then concentrates in \([\log Y,3\log Y/2]\).  An assumed pole to the right of \(\theta\) gives a
strictly larger Cauchy lower bound for a nearby Taylor coefficient, a contradiction.  This uses only
the supplied interval estimate and standard growth of \(G\).  The argument does not furnish that
estimate.

This does not certify the draft's claimed Riemann-hypothesis route.  Its main inequality \(M\) is
explicitly left as a chain of unproved hypotheses in the draft, and the cited Lean development was
not available for this review.

Source. M. O. Rubinstein et al., *The Alpöge--Claude proof of the Riemann hypothesis explained for
the Riemann zeta function*, working draft v2, 22 November 2026, SHA-256
`b49de5037af55c6df66843db710332a358c4eb1d2799581c673cd2ea17e8ea40`, physical pp. 5--7 and
30--31. The local source is an explanatory draft.  This reference adopts only the stated Mellin
transfer, whose proof is printed there.
