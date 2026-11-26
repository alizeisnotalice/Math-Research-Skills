# Dominant-root recurrence linear-form reduction

This reference records a shared, checked **preprint proof interface** from four
local manuscripts.  It is not a verification of the cited Matveev,
Laurent--Mignotte--Nesterenko, Bugeaud--Mignotte--Siksek, or
Dujella--Pethő results.

* `b43f4e...ee62`, *On the Diophantine equation \(F_n-F_m=2^a\)*,
  arXiv:1712.10138v1, physical pp.1--4: Binet bounds yield
  \(|1-2^a\alpha^{-n}\sqrt5|<4\alpha^{m-n}\); the proof checks the
  displayed three-factor linear form is nonzero before applying Matveev.
* `2b3a67...54c2`, *\(F_n-F_m=7^a,13^a\)*, arXiv:2302.07262v1,
  physical pp.1--5: the same Fibonacci dominant-root split is paired with the
  stated prime base and continued-fraction reduction.  Its theorem tables are
  specialized to \(p=7,13\).
* `069a35...d77f`, *k-Fibonacci exponential equation*, arXiv:2205.13168v1,
  physical pp.1--6: under \(3\le k\le\min(m,\log x)\), the source proves
  \((m-2)x+2<n<mx+2\) and
  \(|g\alpha^{n-1}(F^{(k)}_{m+1})^{-x}-1|<2^{2.3-x}\), with a separately
  checked nonzero form and stated height bounds.
* `d09665...2a04`, *\(L_n+L_m=3^a\)*, arXiv:2202.13182v1, physical
  pp.1--3,6: the Lucas estimate \(0.94\alpha^n<L_n<1.15\alpha^n\)
  produces \(0<a\log3-n\log\alpha<3\alpha^{m-n}\), after positivity and
  multiplicative independence have been supplied.

Use this route only after deriving the dominant-root approximation, a strict
upper error, nonvanishing of the actual logarithmic form, the number field and
heights, and a finite continued-fraction certificate satisfying the cited
reduction lemma.  A coarse Matveev bound and a numerical convergent alone do
not classify solutions; the final finite search remains an explicit separate
obligation.
