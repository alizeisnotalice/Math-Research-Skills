# Method and assumption checks

## Pin down the Fourier model

On the uniform cube \(\{-1,1\}^n\), use \(\chi_S(x)=\prod_{i\in S}x_i\), \(\hat f(S)=\mathbb E[f\chi_S]\), and Parseval \(\sum_S\hat f(S)^2=\mathbb E[f^2]\). Record whether the function is \(\{0,1\}\)- or \(\{-1,1\}\)-valued; changing encoding scales coefficients/influences. On a biased cube, name the orthonormal biased basis before using any Fourier identity.

For Boolean \(f:\{-1,1\}^n\to\{-1,1\}\):

- Coordinate influence: \(\mathrm{Inf}_i(f)=\Pr[f(x)\ne f(x^{\oplus i})]=\sum_{S\ni i}\hat f(S)^2\).
- Total influence / average sensitivity: \(\mathrm{Inf}(f)=\sum_i\mathrm{Inf}_i(f)=\sum_S |S|\hat f(S)^2\).
- Fourier degree: \(\max\{|S|:\hat f(S)\ne0\}\).
- Fourier L0 support: \(\#\{S:\hat f(S)\ne0\}\); Fourier L1 spectral norm: \(\sum_S|\hat f(S)|\); Fourier dimension: dimension of the linear span of the support sets over \(\mathbb F_2\).
- Dependence on coordinate (i) means some nonzero coefficient has (i\in S). It does not require \(\hat f(\{i\})\ne0\). Conversely, a nonzero singleton coefficient certifies dependence on that coordinate, but says nothing by itself about other variables.

For 0/1-valued Boolean comparands, squared L² distance equals normalized Hamming disagreement; unsquared L² distance is its square root. State which quantity a stability or approximation theorem controls.

These quantities are not interchangeable. Parity on all (n) bits depends on every bit and has Fourier L0 support 1, but all singleton coefficients vanish. This invalidates an inference from “depends on every variable” to “quadratic support” only when the singleton-coefficient premise is absent; it is not a counterexample to A165. A nonzero singleton coefficient does certify dependence on that coordinate, while “depends on every coordinate” only requires some supported set containing each coordinate. A single supported parity can therefore certify all-coordinate dependence without any singleton term. Fourier dimension is the \(\mathbb F_2\)-span dimension of the support, not its cardinality: the five-bit parity has support \(\{[5]\}\) and Fourier dimension 1, although its real degree and number of dependent variables are both 5. Keep the same distinction among Fourier ℓ₀, spectral ℓ₁, and coefficient ℓ_q bounds when applying sparsity theorems.

When comparing Boolean-function complexity measures, keep exact real multilinear degree, uniform approximate degree, and deterministic decision-tree complexity separate. Nisan–Szegedy Theorem 1.3 states (deg(f)≤D(f)≤16 deg(f)^8); Theorem 1.5, with uniform approximation error 1/3, states (approxdeg(f)≤deg(f)≤D(f)≤c approxdeg(f)^8). Both upper bounds are non-strict. None of these conclusions is a Fourier-support bound.

## Influence and noise

The uniform-cube noise operator satisfies \(T_\rho f=\sum_S\rho^{|S|}\hat f(S)\chi_S\), and \(\mathrm{Stab}_\rho(f)=\mathbb E[fT_\rho f]=\sum_S\rho^{|S|}\hat f(S)^2\). Under independent bit-flip noise with flip probability \(\delta\), \(\rho=1-2\delta\). Noise sensitivity is \(\Pr[f(x)\ne f(y)]\) for that coupling; for Boolean \(\pm1\)-valued (f), it equals \(\tfrac12(1-\mathrm{Stab}_\rho(f))\). State the coupling and normalization before using this relation. In particular, the coordinate influence is the forced-flip probability \(\Pr[f(x)\ne f(x^{\oplus i})]\). If a uniform bit is independently resampled with probability \(\epsilon\), its effective flip probability is \(\epsilon/2\); do not identify influence with the resampling-event probability.

BKS Theorem 1.9 (physical PDF p. 9) concerns a sequence of events \(A_m\subseteq\Omega^{n_m}\), with event indicators \(g_m=\chi_{A_m}\). Noise sensitivity is equivalent to, for each fixed \(k\),
\[
\sum_{S\subseteq[n_m]:\,1\le |S|\le k}\widehat g_m(S)^2\longrightarrow0.
\]
The constant term \(S=\varnothing\) is excluded; keep the sequence, event-indicator normalization, and fixed-noise asymptotic definition. The companion uniform-stability criterion concerns the high-degree tail \(|S|\ge k\). Vanishing \(\sum_i\mathrm{Inf}_i^2\) is a separate sufficient criterion, with a monotone converse under the paper's assumptions. Do not turn a qualitative limit into a finite quantitative bound without its rate and hypotheses.

## Invariance transfer

MOO's invariance principle compares multilinear polynomials over independent ensembles when the relevant low moments match, the ensembles satisfy the stated hypercontractivity conditions, the polynomial has bounded degree and normalized variance, and every coordinate influence is small. The smooth-test-function error depends on degree, influence, derivative bounds, and ensemble parameters. Distributional/threshold conclusions require an additional smoothing argument and anti-concentration near the threshold. For unbounded degree, check the smoothed theorem and low-degree-influence hypotheses rather than invoking the bounded-degree theorem directly.

When using Majority Is Stablest, preserve balancedness, the product/noise model, \(\rho\), and \(\max_i\mathrm{Inf}_i(f)\le\tau\). A small maximum Fourier coefficient \(\max_S|\hat f(S)|\) is a different condition; no implication is automatic because coordinate influence sums all squared coefficients containing that coordinate.

## Bounded independence and PTFs

State the reference product distribution and what k-wise independence means in the domain. DKN's degree-2 theorem is for Boolean-cube inputs. Kane's theorem is for k-wise independent standard Gaussian coordinates, compared with a fully independent Gaussian vector. The sufficient Kane bound is not known here to be optimal. If replacing polynomial values by signs, control \(\Pr(|p(X)|\le t)\) by an applicable anti-concentration theorem; closeness of polynomial moments alone does not settle threshold probability.

Do not merge finite independence with MOO invariance: invariance compares product ensembles under low influences/moment conditions; k-wise independence constrains the joint law while preserving only low-order marginals. A reduction between them needs a stated lemma.


For exact theorem use, preserve nearby quantitative qualifications: BKS Theorem 1.6 has \(II(f)\le C\Lambda(f)^2(1-\log\Lambda(f))\log n\); DKN Theorem 1.1 is \(\widetilde{\Omega}(\epsilon^{-9})\)-wise independence, with polylog factors suppressed; HKM Theorem 8.2 is \(\mathrm{AS}(f)\le3n^{1-2^{-d}}\). In MOO, Theorem 3.18 under Hypothesis 1 has \(\epsilon=(2B/r!)d\eta^{-rd}\tau^{r/2-1}\), while Theorem 3.19 defines separate Hypothesis-dependent error parameters without the test-derivative factor \(B\). Theorem 3.20 assumes Hypothesis 1, 3, or 4 and \(\mathbb E[Q^2]\le1\); it excludes Hypothesis 2. See the source cards for exact model assumptions and pages.
