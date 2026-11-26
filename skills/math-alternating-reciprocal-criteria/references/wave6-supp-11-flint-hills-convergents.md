# Generalized Flint Hills convergence through convergents

**Source.** Yuya Dan, *Critical convergence and Hausdorff measures for
generalized Flint Hills series*, manuscript dated 14 September 2026, physical
pages 3--8, raw PDF SHA-256
`ffb86a8c1bbf1756a51d3ecaccd3fc1f56c919f666f97adf223b8ab6f6c01141`.

**Status and scope.** Scoped reference. This is a preprint-derived
continued-fraction convergence test.  The adopted proof step was read on
physical pages 3--4: the author compares `sin(pi n x)` to the distance of
`n x` from an integer, partitions the sum into continued-fraction blocks, and
uses best-approximation separation.  It is not an irrationality criterion and
does not establish any statement about Euler's constant.

For irrational \(x\), write \(p_k/q_k\) for its simple-continuous-fraction
convergents and, for \(s>0\), \(t>1\), set
\[
 F_{s,t}(x)=\sum_{n\geq1}\frac{1}{n^s|\sin(\pi n x)|^t},\qquad
 G_{s,t}(x)=\sum_{n\geq1}\frac{1}{n^s\|n x\|^t}.
\]
The source first gives the pointwise comparison
\[
 \pi^{-t}G_{s,t}(x)\leq F_{s,t}(x)\leq2^{-t}G_{s,t}(x),
\]
then proves (Proposition 3.1) that a positive constant \(C=C(s,t)\) satisfies
\[
 \sum_{k\geq1}\frac{q_{k+1}^{t}}{q_k^s}
 \leq G_{s,t}(x)
 \leq C\sum_{k\geq1}\frac{q_{k+1}^{t}}{q_k^s}.
\]
Thus the two displayed series have exactly the same convergence status.  This
is a practical interface: calculate or rigorously bound the convergent
denominators, then test the positive series on the right.  Do not infer a
result from finitely many denominators.

At the critical exponent \(\tau=1+s/t\), pages 5--8 give an explicit
boundary-family diagnostic.  With \(\tau>2\), \(\beta=\tau-1\), and
\(s=t\beta\), choose continued-fraction digits by
\[
 a_1=2,\qquad
 a_{k+1}=\left\lfloor q_k^{\beta-1}(k+1)^{r/t}\right\rfloor .
\]
Proposition 5.1 states that the resulting \(x_r\) has irrationality exponent
\(\mu(x_r)=\tau\), while \(F_{s,t}(x_r)\) converges exactly when \(r>1\).
This separates a critical irrationality-exponent statement from a convergence
statement.  The user must verify the digit construction and its all-index
conditions for any adaptation.

**Dependencies actually used by the adopted preprint step.** The comparison
requires continued-fraction convergent theory, the elementary sine-versus-
distance bounds, and the block/separation estimates supplied in the source.
The Hausdorff-measure assertions are not adopted.
