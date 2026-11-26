# OpenAI SK tail and rooted-tree constructions (Wave 4 geometry-a-1)

These are stated-data routines for finite-step spin-glass and rooted Gaussian constructions.  They do not certify a thermodynamic limit outside the hypotheses explicitly supplied by the source.

## Differentiated tail closure and polynomial coercivity

**Source.** *Full support of the zero-temperature Sherrington–Kirkpatrick order parameter*, OpenAI (27 September 2026), physical pp. 9–10 and 16–17, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Full-support-of-the-zero-temperature-Sherrington-Kirkpatrick-order-parameter-September-27-2026/main.pdf), SHA-256 `86256ac3e995c880c1f9075b3e2410d6cb5ca37e4f00ef6303c7605e87e1d3d8`.

For the source's smooth finite-step data, write its density as \(f=e^\ell g\), score \(s=-\partial_x\log g\), and on each forward heat step use \(g_t=\tfrac12g_{xx}\).  At a jump \(c_+-c_-=\delta\ge0\), the stated update is \(g_+=g_-e^{-\delta\Phi}\).  Lemma 3.1 closes the class \(\ell(t,x)=c x+C(t)+O(e^{-\kappa x})\) on \(x\to+\infty\), including a fixed finite number of derivatives.  Its Gaussian transport estimate applies to \(Y_x=\lambda x+b+\sqrt VZ\) with bounded parameters and transfers exponentially decaying derivatives under expectation.

For the coercivity stage, retain the actual finite-step derivative/integrability assumptions and the source's rational polynomial identity (Lemma 4.1 and Proposition 4.2); its reusable output is a nonnegative remainder certificate.  Record the step data, derivative order, tail constants, and every polynomial term instead of reporting coercivity from sampled values.

## Fixed-word tree transfer and finite descendant formula

**Source.** *QAOA attains the SK ground-state energy in the thermodynamic-first limit*, OpenAI (25 September 2026), physical pp. 6 and 26, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026/QAOA-attains-the-SK-ground-state-energy-in-the-thermodynamic-first-limit-September-25-2026.pdf), SHA-256 `4d07ebe181b03157398deef72b23eff8046183f67855d30f9e48e222550a44ba`.

For a fixed ordinary QAOA word \(W\) with fixed real coefficients and angles, the imported transfer has the normalization
\[
 v_W=\lim_{D\to\infty}\frac{\sqrt D}{2}\langle W_D\Omega\mid Z_iZ_j\mid W_D\Omega\rangle,
\]
where the edge lies in the finite light cone of the \((D+1)\)-regular tree and \(C_D=D^{-1/2}\sum_{\{i,j\}\in E}Z_iZ_j\).  This is only a fixed-word statement.

Lemma 3.1 gives a separate finite construction: supplied finite positive \(c_j\) and the scalar data in its equations (3.3)–(3.6), recursively form \(Z_{j+1}=G(g_j)\).  The resulting real odd descendant formula \(F_N\), of height at most \(N+1\), has the required joint Gaussian law, is bounded by one, and has stated rooted energy \(\mathbb E(F_N)=\sum_{j=0}^N A_jB_{j+1}\).  Reuse only after checking positivity/finite-ness of every \(c_j\) and the supplied scalar recursion.
