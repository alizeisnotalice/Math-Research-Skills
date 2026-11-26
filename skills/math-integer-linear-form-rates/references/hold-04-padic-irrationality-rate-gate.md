# p-adic linear-form rate gate

Let \(\xi\in\mathbb Q_p\).  Suppose caller-supplied integer sequences
\(a_n,b_n\) and real \(\alpha>\beta>0\) satisfy
\[
 |a_n+b_n\xi|_p\leq e^{-\alpha n+o(n)},\qquad
 \max(|a_n|,|b_n|)\leq e^{\beta n+o(n)},
\]
and \(a_nb_{n+1}-a_{n+1}b_n\ne0\) for every \(n\).  Then \(\xi\) is
irrational and its p-adic irrationality measure obeys
\[
 \mu(\xi)\leq \frac{\alpha}{\alpha-\beta}.
\]

This is an admission criterion, not a sequence generator.  Check integrality,
the asymptotic valuation and height inequalities, and every adjacent
determinant separately; finitely many numerical p-adic tests cannot replace
the all-\(n\) hypotheses.

Source: Li Lai, Johannes Sprang and Wadim Zudilin, *A note on the
irrationality of \(\zeta_2(5)\)*, arXiv:2505.05005v2, physical p.3, Lemma
2.3 (attributed there to Bel); local SHA-256
`cefad9f37082129c10f6dbe91602248ee7eb6287ab7b753eee813474fa3dc640`.
The source's own recurrence and p-adic remainder proof are not included.
