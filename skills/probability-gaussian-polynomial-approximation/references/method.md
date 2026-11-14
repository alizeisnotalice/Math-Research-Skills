# Method: Gaussian sign approximation and nearby tools

## Problem normalization

Let $Z\sim N(0,I_n)$, let $p$ be a real polynomial of total degree at most $d$, and assume $\operatorname{Var}(p(Z))\ge1$. Define

\[
\delta(p)=\mathbb E[(|p(Z)|-1)^2].
\]

Since $p$ is not the zero polynomial, its Gaussian zero set has measure zero. With $f=\operatorname{sgn}p\in\{-1,1\}$, one has $\delta(p)=\|p-f\|_2^2$. Use the orthonormal Hermite basis for standard Gaussian measure; the sum of squares at level $k$ is the $L^2$ energy of total Hermite degree $k$. A different normalization changes coefficients and constants. When using Abu-Falahah–Torrea’s Hermite function map, compare the measure on physical PDF p. 1 with Lemma 3.1 on p. 5: the printed positive power of π does not give the claimed isometry; keep the source formula and the norm-derived correction separate pending source review (see [the M0250 entry in the source guide](sources.md#newly-integrated-l02-gaussian-b5-reads)).

## Deriving the known $d^{-1/2}$ lower bound

Kindler–O’Donnell, Theorem 2.9 (the general form; the introduction gives its constant-variance form as Theorem 1.3), gives a Gaussian Hermite tail lower bound of order $\operatorname{Var}(f)/\sqrt{k}$ for $\{-1,1\}$-valued $f$. The following is a deduction for B167, not a verbatim theorem in that paper.

Let $C g=g-\mathbb E[g]$ be the centering operator. It is a contraction in $L^2$. Thus

\[
\sqrt{\operatorname{Var}(p)}=\|Cp\|_2\le\|Cf\|_2+\|C(p-f)\|_2\le\sqrt{\operatorname{Var}(f)}+\sqrt{\delta}.
\]

If $\delta\le1/4$, then $\operatorname{Var}(f)\ge1/4$. Since $p$ has Hermite degree at most $d$, its squared approximation error to $f$ is at least the tail beyond degree $d$:

\[
\delta=\|p-f\|_2^2\ge W^{>d}[f]\ge c_0\frac{\operatorname{Var}(f)}{\sqrt d}\ge\frac{c_0}{4\sqrt d}.
\]

If $\delta>1/4$, then $\delta\ge c_1/\sqrt d$ for any $d\ge1$ after choosing $c_1\le1/4$. Combining the cases yields $\delta\ge c/\sqrt d$ for an absolute constant $c>0$. This provides no sharp value and no asymptotically optimal constant.

## Keep adjacent tools separate

- **Moment and tail estimates:** Latała’s Gaussian-chaos Theorem 1 compares moments for p>=2 at general order d; its Corollary 1 tail bound is stated for d>=2. The log-concave-tail M0229 result is a separate model: normalize inf{t:N_i(t)>=1}=1, set Nhat_i(t)=t^2 for |t|<=1 and N_i(|t|) otherwise, and use its vector/matrix supremum gauges. Neither source is a best $L^2$ sign-approximation result.
- **Small-ball and anti-concentration:** Carbery–Wright gives a degree-sensitive small-ball estimate. It can support smoothing or sign-stability arguments, but its $\epsilon^{1/d}$ form does not by itself give B167’s leading constant. On physical p. 12 (printed p. 244), Theorem 7 is $\|p^\#\|_q\le C\,\max(q,1)/\max(r,1)\,\|p^\#\|_r$ for $0<r\le q<\infty$ (ratio, not a power). Theorem 8 prints the sublevel factor $Cq$ for all $q>0$; the constant-polynomial test $p\equiv1,\alpha=1$ makes its left side 1, contradicting a uniform bound as $q\downarrow0$. Keep the source defect explicit and use only $q\ge1$ for B167 (e.g. $q=d$); do not silently replace $q$ by $\max(q,1)$. Tu–Boczar’s source Theorem 1.2 requires a nonzero degree-two nonnegative polynomial (equivalently positive expectation); keep this source statement distinct from the card’s explicitly derived degree-at-most-two extension.
- **Diffuse decomposition:** Kane approximates a Gaussian polynomial by one with a diffuse decomposition, with constants depending on fixed parameters including degree. Its diffuse-tuple condition is P(|q_i(X)-a_i|<=epsilon for every i)<=epsilon^m N, with N outside the exponent, and E|q_i(X)|^2<=1. This is structural PTF machinery, not a uniform sharp-constant theorem.
- **Noise sensitivity and surface area:** In Diakonikolas–Raghavendra–Servedio–Tan’s arXiv v1, keep the Gaussian-input and Boolean-cube PTF theorems separate. Their Theorem 1.5 prints an ε∈[0,1] range whose displayed upper bound fails at large noise; the proof only supports small noise. Do not extend it to a corrected all-ε estimate. Kane M0236 controls $\Pr[f(X)\ne f((1-\epsilon)X+\sqrt{2\epsilon-\epsilon^2}Y)]$ and Gaussian surface area for $f=\operatorname{sgn}p$. For its printed $d\,\arcsin(\sqrt{2\epsilon-\epsilon^2})/\pi$ upper bound, enforce $0\le\epsilon\le1$: the proof sets the principal angle $\theta=\arcsin(\sqrt{2\epsilon-\epsilon^2})$, for which $\cos\theta=|1-\epsilon|$, and identifies it with the coupling correlation $1-\epsilon$ only on this interval. The coupling itself remains well-defined through $\epsilon=2$, but the bound fails for $\epsilon>1$ (already for $f(x)=\operatorname{sgn}x$ at $\epsilon=3/2$). These boundary quantities differ from $\mathbb E[(|p|-1)^2]$.
- **Invariance:** MOO’s theorem compares low-influence multilinear polynomials on independent product inputs with Gaussian replacements. Check coordinate independence, the specific moment-matching and hypercontractivity hypothesis, degree, variance normalization, and every individual influence; the smooth-test/distributional variants have additional conditions. B167’s arbitrary real degree-≤d Gaussian polynomial need not be multilinear or low-influence, and its absolute-value loss is nonsmooth. The canonical-use card records this as a conditional route only, not a B167 theorem.

### Additional B7 sources: keep their input models intact

- **Gaussian convex-set and linear-series facts:** M0228 applies to centered Gaussian measures, equal-measure symmetric convex sets/strips, and separately a.s.-convergent Banach-valued Gaussian linear series. It does not yield a polynomial sign-distance estimate.
- **Independent-coordinate moment and small-ball results:** M0231 is for positive-coefficient decoupled chaos from independent positive variables with logarithmically concave tails. M0233 Theorem 2.5 is for \(A\xi\) with independent-coordinate subgaussian inputs; under the column-vector convention its Gram matrix is \(A^\mathsf{T}A\), while the source display’s \(AA^\mathsf{T}\) is isolated. M0234 is an additive \(L^p\) Gaussian approximation for linear sums of independent symmetric variance-one logarithmically-concave-tail variables, \(p\ge3\), with error \(p\|a\|_\infty\).
- **Decoupled-chaos norms:** M0238 uses independent symmetric inputs and normalized two-sided convex tail rates. It gives lower estimates at every order, upper estimates for \(d\le3\), and all-order upper estimates only for symmetric exponential inputs. M0242 is usable only under the HMO-supported \(N(t)=-\log\Pr(|X|\ge t)\) concave/log-convex-survival convention; its own p.2 has an opposite convexity statement. Do not transfer it to Gaussian/log-concave-survival inputs.
- **Other Gaussian auxiliaries:** M0240 gives centered polynomial moment/tail comparisons with degree-dependent constants and cannot be applied to \(|p|\) as a polynomial. M0241 is the Gaussian correlation inequality for closed symmetric convex events; retain the convexity needed by its proof. M0248 concerns finite Gaussian matrices with deterministic variance profile and Theorem 2 range \(1<p\le2\le q<\infty\); endpoints are separate identities. M0251 concerns finite Gaussian-vector CDFs/maxima and has no direct scalar-polynomial map.
- **Canonical chaos reuse:** M0247 Theorem 2.1 is an auxiliary comparison for finite Banach-valued coefficient arrays in independent Gaussian decoupled slots, moments \(p\ge1\), with order-dependent constants. It is canonical reuse, not a new W18 full read.
- None of these results supplies a reduction from B167's arbitrary real Gaussian polynomial and nonsmooth \(\mathbb E[(|p|-1)^2]\) objective to its stated input model. Treat each as conditional background until such a reduction is proved.

For C168, Gaussian/Hermite expansions may represent a kernel, but the exact bilinear extremal problem over sign partitions needs a separate derivation; no result here identifies its optimizer.
