# Method and assumption checks

## Pin down the Fourier model

On the uniform cube \(\{-1,1\}^n\), use \(\chi_S(x)=\prod_{i\in S}x_i\), \(\hat f(S)=\mathbb E[f\chi_S]\), and Parseval \(\sum_S\hat f(S)^2=\mathbb E[f^2]\). Record whether the function is \(\{0,1\}\)- or \(\{-1,1\}\)-valued; changing encoding scales coefficients/influences. On a biased cube, name the orthonormal biased basis before using any Fourier identity.

For Boolean \(f:\{-1,1\}^n\to\{-1,1\}\):

- Coordinate influence is the forced-flip probability \(\mathrm{Inf}_i(f)=\Pr[f(x)\ne f(x^{\oplus i})]=\sum_{S\ni i}\hat f(S)^2\).
- For \(f:\{-1,1\}^n\to\{0,1\}\) with the same normalized Walsh basis, \(\mathrm{Inf}_i(f)=4\sum_{S\ni i}\hat f(S)^2\). The forced-flip probability is unchanged by recoding the output, while every nonconstant coefficient doubles under \(f\mapsto2f-1\).
- Total influence / average sensitivity is \(\sum_i\mathrm{Inf}_i(f)\); with \({-1,1}\)-valued output it equals \(\sum_S |S|\hat f(S)^2\). For \({0,1}\)-valued output, \(\mathrm{Inf}(f)=4\sum_S |S|\hat f(S)^2\), equivalently \(\sum_S |S|\hat f(S)^2=\mathrm{Inf}(f)/4\).
- Fourier degree: \(\max\{|S|:\hat f(S)\ne0\}\).
- Fourier L0 support: \(\#\{S:\hat f(S)\ne0\}\); Fourier L1 spectral norm: \(\sum_S|\hat f(S)|\); Fourier dimension: dimension of the linear span of the support sets over \(\mathbb F_2\).
- Dependence on coordinate (i) means some nonzero coefficient has (i\in S). It does not require \(\hat f(\{i\})\ne0\). Conversely, a nonzero singleton coefficient certifies dependence on that coordinate, but says nothing by itself about other variables.

For 0/1-valued Boolean comparands, squared L² distance equals normalized Hamming disagreement; unsquared L² distance is its square root. State which quantity a stability or approximation theorem controls.

These quantities are not interchangeable. Parity on all (n) bits depends on every bit and has Fourier L0 support 1, but all singleton coefficients vanish. This invalidates an inference from “depends on every variable” to “quadratic support” only when the singleton-coefficient premise is absent; it is not a counterexample to A165. A nonzero singleton coefficient does certify dependence on that coordinate, while “depends on every coordinate” only requires some supported set containing each coordinate. A single supported parity can therefore certify all-coordinate dependence without any singleton term. Fourier dimension is the \(\mathbb F_2\)-span dimension of the support, not its cardinality: the five-bit parity has support \(\{[5]\}\) and Fourier dimension 1, although its real degree and number of dependent variables are both 5. Keep the same distinction among Fourier ℓ₀, spectral ℓ₁, and coefficient ℓ_q bounds when applying sparsity theorems.

When comparing Boolean-function complexity measures, keep exact real multilinear degree, uniform approximate degree, and deterministic decision-tree complexity separate. Nisan–Szegedy Theorem 1.3 states (deg(f)≤D(f)≤16 deg(f)^8); Theorem 1.5, with uniform approximation error 1/3, states (approxdeg(f)≤deg(f)≤D(f)≤c approxdeg(f)^8). Both upper bounds are non-strict. None of these conclusions is a Fourier-support bound.


## Boolean-square convolution identities (G14.01; keep the output coding)

For a Boolean function \(f:\{-1,1\}^n\to\{0,1\}\) with normalized Walsh coefficients, the pointwise identity \(f^2=f\) gives
\[
 \sum_{\alpha\subseteq[n]}\hat f(\alpha)\hat f(\alpha\triangle\gamma)=\hat f(\gamma),\qquad \gamma\subseteq[n].
\]
Indeed, expand both factors in Walsh characters, use \(\chi_\alpha\chi_\beta=\chi_{\alpha\triangle\beta}\), and compare the coefficient of \(\chi_\gamma\). For sign-valued \(F:\{-1,1\}^n\to\{-1,1\}\), the different identity \(F^2=1\) instead gives
\[
 \sum_{\alpha\subseteq[n]}\hat F(\alpha)\hat F(\alpha\triangle\gamma)=\mathbf1_{\{\gamma=\varnothing\}}.
\]
This is a derived coding identity. Do not import the sign-coded right-hand side into the \(0/1\) equation. The admitted M0142 argument concerns the sign-coded support-consistency condition; its pair multiplicity condition is necessary but not sufficient.

## Influence and noise

The uniform-cube noise operator satisfies \(T_\rho f=\sum_S\rho^{|S|}\hat f(S)\chi_S\), and \(\mathrm{Stab}_\rho(f)=\mathbb E[fT_\rho f]=\sum_S\rho^{|S|}\hat f(S)^2\). Under independent bit-flip noise with flip probability \(\delta\), \(\rho=1-2\delta\). Noise sensitivity is \(\Pr[f(x)\ne f(y)]\) for that coupling; for Boolean \(\pm1\)-valued (f), it equals \(\tfrac12(1-\mathrm{Stab}_\rho(f))\). State the coupling and normalization before using this relation. In particular, the coordinate influence is the forced-flip probability \(\Pr[f(x)\ne f(x^{\oplus i})]\). If a uniform bit is independently resampled with probability \(\epsilon\), its effective flip probability is \(\epsilon/2\); do not identify influence with the resampling-event probability.

BKS Theorem 1.9 (physical PDF p. 9) concerns a sequence of events \(A_m\subseteq\Omega^{n_m}\), with event indicators \(g_m=\chi_{A_m}\). Noise sensitivity is equivalent to, for each fixed \(k\),
\[
\sum_{S\subseteq[n_m]:\,1\le |S|\le k}\widehat g_m(S)^2\longrightarrow0.
\]
The constant term \(S=\varnothing\) is excluded; keep the sequence, event-indicator normalization, and fixed-noise asymptotic definition. The companion uniform-stability criterion concerns the high-degree tail \(|S|\ge k\). Vanishing \(\sum_i\mathrm{Inf}_i^2\) is a separate sufficient criterion, with a monotone converse under the paper's assumptions. Do not turn a qualitative limit into a finite quantitative bound without its rate and hypotheses.

## Invariance transfer

MOO's invariance principle compares multilinear polynomials over independent ensembles when the relevant low moments match, the ensembles satisfy the stated hypercontractivity conditions, the polynomial has bounded degree and normalized variance, and every coordinate influence is small. The smooth-test-function error depends on degree, influence, derivative bounds, and ensemble parameters. Distributional/threshold conclusions require an additional smoothing argument and anti-concentration near the threshold. For unbounded degree, check the smoothed theorem and low-degree-influence hypotheses rather than invoking the bounded-degree theorem directly.

When using Majority Is Stablest, preserve balancedness, the product/noise model, \(\rho\), and \(\max_i\mathrm{Inf}_i(f)\le\tau\). A small maximum Fourier coefficient \(\max_S|\hat f(S)|\) is a different condition; no implication is automatic because coordinate influence sums all squared coefficients containing that coordinate. A nonzero singleton coefficient certifies dependence on that coordinate, but influence may come only from higher levels; dependence on every coordinate does not require any singleton coefficient. A165 specifically requires \(\hat f(\{i\})\ne0\) for every \(i\), which is stronger than all-coordinate dependence.

## Bounded independence and PTFs

State the reference product distribution and what k-wise independence means in the domain. DKN's reviewed degree-2 branch is for Boolean-cube inputs. The current Kane scope is the positive-kernel smoothed Taylor interface: retain the even block orders, the derived sufficient condition \(k\ge D\sum_i m_i\), and expected remainder. For real polynomial h and f=sgn_+(h), the reviewed sign-expectation bound is 2ER+2b_X+2b_Y+4η, so the corresponding event-probability bound is ER+b_X+b_Y+2η under the explicit zero-boundary/kernel-tail gate. Moment matching alone does not settle threshold probability. This does not approve Kane's full headline exponent, Proposition 8, or a Boolean-cube counterpart.

Do not merge finite independence with MOO invariance: invariance compares product ensembles under low influences/moment conditions; k-wise independence constrains the joint law while preserving only low-order marginals. A reduction between them needs a stated lemma.


For exact theorem use, preserve nearby quantitative qualifications: BKS Theorem 1.6 has \(II(f)\le C\Lambda(f)^2(1-\log\Lambda(f))\log n\); DKN Theorem 1.1 is \(\widetilde{\Omega}(\epsilon^{-9})\)-wise independence, with polylog factors suppressed; HKM Theorem 8.2 is \(\mathrm{AS}(f)\le3n^{1-2^{-d}}\). In MOO, Theorem 3.18 under Hypothesis 1 has \(\epsilon=(2B/r!)d\eta^{-rd}\tau^{r/2-1}\), while Theorem 3.19 defines separate Hypothesis-dependent error parameters without the test-derivative factor \(B\). Theorem 3.20 assumes Hypothesis 1, 3, or 4 and \(\mathbb E[Q^2]\le1\); it excludes Hypothesis 2. See the source cards for exact model assumptions and pages.

## Self-duality, permutation symmetry, and the admitted representation boundary

The exact safe interface in G14.06 is a derived projection calculation. It is not a claim that the cited sources prove a full irreducible representation theorem. Let \(H=L^2(\{-1,1\}^n)\), and let a finite \(G\le S_n\) act by \(U_g f(x)=f(g^{-1}x)\). Coordinate permutations are unitary. The average
\[
 R_G=\frac1{|G|}\sum_{g\in G}U_g
\]
is self-adjoint because \(U_g^*=U_{g^{-1}}\), and idempotent because each group element occurs \(|G|\) times in the double sum. Its range is exactly \(\mathrm{Fix}(G)\), so it is the orthogonal projector onto invariant functions and
\[
 H=\mathrm{Fix}(G)\oplus\mathrm{Fix}(G)^\perp.
\]
Since \(U_g\chi_S=\chi_{gS}\), Fourier coefficients of \(R_G f\) are the averages of \(\hat f\) over the \(G\)-orbits of subsets. For \(G=S_n\), these orbits are the cardinality layers, and the invariant subspace is spanned by the layer sums.

Let \(Cf(x)=f(-x)\). Then \(C\) is a self-adjoint involution, commutes with \(R_G\), and satisfies \(C\chi_S=(-1)^{|S|}\chi_S\). Thus \(E=(I+C)/2\) and \(O=(I-C)/2\) are the even- and odd-level orthogonal projectors. The four commuting projections \(R_GE,R_GO,(I-R_G)E,(I-R_G)O\) are pairwise orthogonal and sum to \(I\). For sign-valued self-dual \(f(-x)=-f(x)\), \(Ef=0\), so all even Fourier coefficients vanish. For \(0/1\)-valued self-dual \(f(-x)=1-f(x)\), the constant coefficient is \(1/2\) and all nonempty even coefficients vanish after applying the sign-coded identity to \(2f-1\). These facts do not force nonzero singleton coefficients, and \(R_G\) need not preserve Boolean-valuedness. This derived interface supplies invariant-subspace projections, not the full \(S_n\) irreducible decomposition. Its independent derivation and exact finite check are bundled as the derived projection audit（本机附件：`evidence/reviews/R07/whole_entry_precheck/derived_projection_audit.md`）, script（本机附件：`evidence/reviews/R07/whole_entry_precheck/projection_checks.py`）, and output（本机附件：`evidence/reviews/R07/whole_entry_precheck/projection_checks.out.json`）; this carries no source/read credit.
