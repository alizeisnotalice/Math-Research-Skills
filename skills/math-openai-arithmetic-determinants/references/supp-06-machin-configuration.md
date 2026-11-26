# Exact Machin configuration gate

Source: *A closed-form law for the Salikhov--Zeilberger--Zudilin--Bai
family*, arXiv:2609.37459v2, SHA-256
`f502565f4fa50a4fd7b8a6a06c429209926adc246151130f8bd0769533b2d3ec`.
This is explicitly an unrefereed preprint.  The adopted step is labelled
`PROVED` by the source and was checked on physical pp.1--2; its finite
configuration list is checked exactly here, not accepted from the source's
numerical optimization claims.

Let \(w=u+vi\in\mathbb Z[i]\), \(v>0\), and \(P>0\).  For the source's
even, real contour integrand with zeros at \(0,\pm w,\pm\bar w\) and poles at
\(\pm P\), the logarithmic part is a linear form in \(1\) and \(\pi\) precisely
when
\[
 P^2-(u^2+v^2)=\pm2Pv.
\]
The proof computes the argument of \((P-\bar w)/(P+\bar w)\), then uses the
rational-tangent restriction at rational multiples of \(\pi\).  The sign fixes
the orientation; it does not by itself prove an irrationality-measure bound.

Run `python -B scripts/check_machin_configuration.py examples/machin_5_1_2.json`
for the Salikhov configuration, or `--limit 99` to reproduce the 16 primitive
positive-sign configurations with \(P<100\).  The checker is exact integer
arithmetic.  It does **not** verify contour deformation, saddle/min-max decay,
integrality/divisibility, or the preprint's `VERIFIED` finite searches and
`CONJECTURE` of global optimality.
