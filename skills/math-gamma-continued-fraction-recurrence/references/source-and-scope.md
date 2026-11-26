# Source, finite identities, and arithmetic boundary

The locally downloaded source is Kh. Hessami Pilehrood and T. Hessami
Pilehrood, *On a continued fraction expansion for Euler's constant*,
arXiv:1010.1420v3, 29 December 2013.  It has 16 physical PDF pages.  The
journal version is *Journal of Number Theory* 133(2) (2013), DOI
[10.1016/j.jnt.2012.08.016](https://doi.org/10.1016/j.jnt.2012.08.016).
The formulas used here are checked against the local preprint, whose SHA-256
is `0fc9404ea3f673bc2215cbce0858ba8a18a9f8f0c00c73d0465c642953aea0dc`.

- Physical PDF pp. 8–9, equation (21) and Lemma 1, define \(p_n,q_n\) and
  prove their second-order homogeneous and inhomogeneous recurrences.
- Physical PDF pp. 10–12, Lemmas 2–3, Theorem 1, and Corollary 1, give the
  Meijer-G error analysis and the subexponential ratio asymptotic.
- Physical PDF pp. 13–15, Theorem A and Theorem 3, construct a non-simple
  continued fraction.  The script uses Theorem A directly, which works over
  rational partial elements and is independently checked by the convergent
  recurrence.

For example, the exact sums give

\[
(p_0,p_1,p_2,p_3,p_4,p_5)=
\left(0,1,4,\frac{59}{3},\frac{725}{6},\frac{13396}{15}\right),
\]
\[
(q_0,q_1,q_2,q_3,q_4,q_5)=(1,2,7,34,209,1546).
\]

Hence the first six rational approximants are
\(0,1/2,4/7,59/102,725/1254,6698/11595\).  These are exact finite facts.
The asymptotic statements in the source are author results.  Their use as a
numerical approximation statement has been checked only through the source
theorem, not reproved here.  Neither the recurrence nor the continued fraction
isolates a shrinking integer form in \(1,\gamma\), so neither supplies an
irrationality proof.
