# FRIEDGUT2026 — Small influential coalitions in the continuous cube via the junta theorem

**Source.** Ehud Friedgut, arXiv:2610.03086v1, submitted 2026-10-02 (revised 2026-09-30), six physical pages. The local PDF title page and arXiv record match; SHA-256 is in sources.json. The paper states that this simplified proof was generated with AI assistance and lightly edited by the author.

## Model and theorem

Throughout, \(X\) is uniform on \([0,1]^n\), monotonicity is coordinatewise, and \(b_B\) means setting every coordinate in \(B\) to \(b\). Both the coalition and target are chosen before the remaining coordinates are sampled.

**Theorem 1 (physical p. 3).** There is an absolute constant \(C\) such that for \(n\ge2\), \(0<\epsilon<1/2\), every monotone \(f:[0,1]^n\to\{0,1\}\) has \(B\subseteq[n]\) and \(b\in\{0,1\}\) with
\[
|B|\le \frac{Cn}{\epsilon\log n},\qquad
\Pr[f(b_B,X_{-B})=b]\ge1-\epsilon.
\]
This is a continuous-cube one-sided coalition conclusion. It does not imply the discrete fixed-error \(O(\log n)\) conjecture.

## Lemma 1 and proof

For monotone \(h:[0,1]^n\to\{0,1\}\), define
\[
K(h)=\sum_{i=1}^n\mathbb E[h(1,X_{-i})-h(0,X_{-i})].
\]
This is the sum of the probabilities of nonconstant coordinate fibres, including changes that occur only at an endpoint.

**Lemma 1 (physical pp. 3–4).** There is an absolute \(c\) such that if \(K(h)\le L\), \(L>0\), then for every \(0<\eta<1\) there are \(S\subseteq[n]\) and \(b\in\{0,1\}\) with
\[
|S|\le \exp(cL/\eta),\qquad
\Pr[h(b_S,X_{-S})=b]\ge1-\eta.
\]

The proof discretizes each coordinate with \(M=2^m\) equally spaced values. Set \(D_M(x)=\lfloor Mx\rfloor/M\) for \(x<1\), \(D_M(1)=(M-1)/M\), and \(h_M(x)=h(D_M(x_1),\ldots,D_M(x_n))\). Monotonicity and a coordinate-by-coordinate telescoping sum give
\[
\Pr[h(X)\ne h_M(X)]\le n/M.
\]
Regard each grid coordinate as a block of \(m\) fair bits, so \(h_M\) is a Boolean function \(H_M\) on \(nm\) bits. With all other blocks fixed, \(H_M\) is a threshold in the binary ordering of the remaining block; its \(j\)-th bit has influence at most \(2^{-(j-1)}\). Summing block contributions gives
\[
I(H_M)\le
2\sum_i\mathbb E[h(1,D_M(X_{-i}))-h(0,D_M(X_{-i}))]
\le2K(h)+\frac{2n(n-1)}M.
\]
Choose \(M\) large enough that the discretization error is at most \(\eta/2\) and \(I(H_M)\le4L\). Friedgut’s Boolean junta theorem gives an \(\eta/2\)-approximant \(Q\) depending on at most \(\exp(8c_0L/\eta)\) of the grid bits. Let \(S\) be the original coordinates containing those bits. Averaging over \(X_S\) yields a fixed assignment \(a\) with \(\Pr[h(a,X_{-S})\ne Q(a)]\le\eta\). Put \(b=Q(a)\); moving each coordinate of \(a\) to endpoint \(b\) can only increase the probability of output \(b\), by monotonicity. This proves Lemma 1.

## Proof of Theorem 1

Fix \(0<\rho<1\). For \(0\le t\le\rho\), define the product marginal and its output mean by
\[
\nu_t=(1-\rho)\,\mathrm{Unif}[0,1]+(\rho-t)\delta_0+t\delta_1,\qquad
F(t)=\mathbb E_{\nu_t^{\otimes n}}f.
\]
Differentiating the product measure gives
\[
F'(t)=\sum_{i=1}^n
\mathbb E_{\nu_t^{\otimes(n-1)}}[f(1,X_{-i})-f(0,X_{-i})]
=:K_t.
\]
Since \(\int_0^\rho K_t\,dt=F(\rho)-F(0)\le1\), choose \(t\in(0,\rho)\) with \(K_t\le1/\rho\).

To apply Lemma 1 under \(\nu_t\), define the monotone endpoint-preserving transport
\[
T_t(u)=\operatorname{clip}_{[0,1]}\!\left(\frac{u-\rho+t}{1-\rho}\right),
\qquad h(u)=f(T_t(u_1),\ldots,T_t(u_n)).
\]
Then \(T_t\) sends Lebesgue measure to \(\nu_t\) and \(K(h)=K_t\). Lemma 1 with \(L=1/\rho\) and \(\eta=\epsilon/2\) gives \(S,b\) with
\[
|S|\le\exp(A/(\rho\epsilon)),\qquad
\Pr_{\nu_t^{\otimes([n]\setminus S)}}[f(b_S,X_{-S})\ne b]\le\epsilon/2.
\]
Replacing both endpoint atoms by the favorable endpoint \(b\) preserves this error bound by monotonicity. Sample the resulting marginal by independently putting each coordinate outside \(S\) into a random set \(R\) with probability \(\rho\), fixing it to \(b\), and sampling the others uniformly. If \(e(R)\) is the remaining failure probability, then \(\mathbb E_R e(R)\le\epsilon/2\). Markov’s inequality gives \(\Pr[|R|\le2\rho(n-|S|)]\ge1/2\); on this event the conditional average of \(e(R)\) is at most \(\epsilon\), so some fixed \(R\) satisfies both bounds. Thus \(B=S\cup R\) is fixed before the remaining coordinates are sampled and
\[
|B|\le\exp(A/(\rho\epsilon))+2\rho n,\qquad
\Pr[f(b_B,X_{-B})=b]\ge1-\epsilon.
\]
When \(\epsilon\log n>2A\), choose \(\rho=2A/(\epsilon\log n)\). Then the exponential term is \(\sqrt n\), and the right side is at most \((4A+1)n/(\epsilon\log n)\). When \(\epsilon\log n\le2A\), fixing all \(n\) coordinates suffices after increasing the absolute constant. This proves Theorem 1.

## Scope

The proof gives a one-sided coalition in the continuous cube with target \(b\) selected before the remaining inputs. Its exponential-in-\(L/\eta\) junta lemma and random endpoint-fixing step are essential. It does not yield a discrete \(O(\log n)\) coalition or remove the continuous product-space assumptions.

## Physical-page coverage

| Physical PDF pages | Section | Content read |
|---|---|---|
| 1–2 | Introduction | Title/abstract, history, theorem motivation, and proof context. |
| 3 | §2.1 | Exact model and Theorem 1 statement; §2.2 definition of \(K(h)\) and Lemma 1 statement/proof start. |
| 3–4 | §2.2 | Grid discretization, block-threshold influences, \(I(H_M)\) bound, junta approximation, endpoint assignment. |
| 4–5 | §2.3 | Mixture path \(\nu_t\), derivative identity, selection of \(t\), transport, and application of Lemma 1. |
| 5 | §2.3 | Random set \(R\), Markov step, pre-sampling quantifiers, \(\rho\) choice and size bound. |
| 5–6 | References | Bibliography and end matter. |

**Reading status:** full text, physical PDF pp. 1–6.
