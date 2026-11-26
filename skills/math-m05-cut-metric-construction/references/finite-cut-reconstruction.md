# Finite cut reconstruction

**Source.** OpenAI, *Metric Markov Cotype Two of \(\ell_1\)*, 5 October 2026, Lemma 2.1, PDF pp. 3--4 (local SHA-256 `d1977f73e5a70137791d0739b58b049fa30e3ad9caa4dfeb8353142db37ab60f`; 9 pages). The pinned source is <https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026/l1-markov-cotype.pdf>.

## Statement used here

For finitely many real \(\ell_1\) vectors \(x_i\), define \(v,b_B,w_B,z_i,T\) exactly as in the skill. Then, after removing the zero-weight cuts,
\[
T(z_i)=x_i,
\qquad \|x_i-x_j\|_1=\sum_Bw_B|z_i(B)-z_j(B)|
=\sum_Bw_B(z_i(B)-z_j(B))^2,
\]
and \(T\) is 1-Lipschitz from weighted \(\ell_1\) to ambient \(\ell_1\).

## Independent finite proof

Fix a coordinate \(k\), list its distinct point values as \(\alpha_1<\cdots<\alpha_m\), and let \(B_r=\{i:x_i(k)\ge\alpha_{r+1}\}\). Directly from the min--max formula, at coordinate \(k\) only \(B_r\) has nonzero contribution at level \(r\), equal to \(\alpha_{r+1}-\alpha_r\). Summing the levels selected by \(i\) yields \(T(z_i)(k)=x_i(k)\).

For a pair \(i,j\), these nonzero cuts are nested. Hence all signed summands \((z_i(B)-z_j(B))b_B(k)\) have the same sign, so
\[
 |x_i(k)-x_j(k)|=\sum_B|z_i(B)-z_j(B)|b_B(k).
\]
Summing coordinates gives the weighted \(\ell_1\) identity. Since the differences of binary bits are in \(\{0,\pm1\}\), their absolute values equal their squares, proving the Hilbert-square identity. Finally,
\[
\|T(u)-T(u')\|_1\le\sum_B|u_B-u'_B|\,\|b_B\|_1
=\sum_Bw_B|u_B-u'_B|.
\]

The proof uses only a finite family of supplied \(\ell_1\) vectors. It neither supplies the geometric-killing martingale estimate nor proves Markov cotype or a Lipschitz extension theorem. The reconstructed image is in ambient \(\ell_1\), and need not lie in a prescribed subspace containing the input.
