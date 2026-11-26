# Exact finite audit for a Hermitian sign series

**Primary source.** OpenAI, *Polynomial-Time Unitary Synthesis from a Boolean Oracle*, Lemma 3.1, physical PDF p. 6, pinned manuscript commit `3344da59991ed94f9ba711217b29c1d760badfa6`, SHA-256 `198849e472386b7a14e8cd7ff52e8ec305c1b6ebc596ec846bcd947bb04b101c`.

The source assumes finite-dimensional Hermitian matrices \(L_i\), independent Rademacher signs \(\varepsilon_i\), and \(v=\|\sum_iL_i^2\|\), and proves, for integral \(a\ge1\),
\[
 \mathbb E\|\sum_i\varepsilon_iL_i\| \le2h^{1/(2a)}\sqrt{(2a-1)v}.
\]

The reusable proof step is the Gaussian trace-moment recurrence. For \(X=\sum_i g_iL_i\), Gaussian integration by parts followed by spectral weighted AM--GM yields
\[
 \mathbb E\operatorname{Tr}X^{2a}\le(2a-1)v\,\mathbb E\operatorname{Tr}X^{2a-2}\le h(2a-1)!!v^a.
\]
The order relation \(\sum_iL_i^2\preceq vI\) is essential. The source then writes \(g_i=\varepsilon_i|g_i|\) and uses conditional Jensen to transfer the **norm** estimate to signs; this does not identify an arbitrary sign trace moment with the Gaussian one.

`scripts/check_matrix_sign_moment.py` is deliberately narrow. For rational Hermitian matrices with entries in \(\mathbb Q(i)\), it verifies every principal minor of \(vI-\sum_iL_i^2\), exhaustively computes the supplied finite Rademacher trace moment, and reports the Gaussian upper bound separately. It is an exact certificate for that input only. It does not prove the general lemma, estimate a non-Hermitian series, or replace a rectangular dilation.
