# 欧拉常数相关本机文献逐篇核对

本页收录从三组本机索引按题名相关性筛出、按 SHA-256 去重的 58 份非 OpenAI PDF。按主要方法归类。表内的页码是本机文件的物理页，期刊页码按正式题录使用。范围栏保留候选构造、源文献声称及本轮的依赖门槛。已形成工具的来源另附调用入口。

先读 [方法和来源选择](methods.md)。检查线性形式是否真的隔离 \(\gamma\)，再比较公分母、高度、非消失和趋零。直接使用正式出版定理时，按本页版本引用。对预印本候选，先核验实际论证及所用依赖。

## 计算区间、误差与历史

### 01 · A bound for the error term in the Brent-McMillan algorithm

- 版本与身份。local arXiv:1312.0039v1, 10 pp; published Richard P. Brent and Fredrik Johansson, Mathematics of Computation 84(295) (2015), 2351-2359, doi:10.1090/S0025-5718-2015-02931-7 (author erratum records the x&gt;=1 condition for (2.7)). SHA-256 为 `0f91cf7757be471d4e7d34f1248f1ae8ffedb4791919d44bf7661ede24985ce0`。
- 本机原文定位。\['local PDF p.7, Theorem 1, (30)-(32); p.8, Corollary 2', 'published Math. Comp. 84 (2015), 2351-2359, Theorem 4.1/Corollary 4.3'\]
- 核对范围。For integer n&gt;=1 and an admissible truncation N, gives the certified numerical bound \|gamma_tilde-gamma\|&lt;24 exp(-8n); Corollary 2 permits N&gt;=4.970625759544 n for n&gt;=138. This is a computation/error theorem, not an irrationality criterion.
- 依赖与状态。Bessel-function identity for gamma / finite Taylor sums and optimal asymptotic truncation / Theorem 1 excludes rounding and log(n)-evaluation error published-scoped-numeric-only
- 调用入口。[Brent–McMillan 区间](brent-mcmillan-enclosure.md)

### 04 · An asymptotic expansion for the error term in the Brent-McMillan algorithm for Euler's constant

- 版本与身份。local arXiv:1809.04342v2 (16 Feb 2019), 9 pp; published R. B. Paris, Journal of Mathematics Research 11(3) (2019), 60-66, doi:10.5539/jmr.v11n3p60. SHA-256 为 `ac75af081586e59595491e6da33b8ca5064783fd38c3ebd7c89044566a4ae75f`。
- 本机原文定位。\['local PDF p.6, Theorem 1 (3.7); p.7, Theorem 2 (4.2)', 'published J. Math. Research 11(3) (2019), 60-66, Theorems 1-2'\]
- 核对范围。Derives asymptotic expansions as x-&gt;+infinity for the optimally truncated Bessel-product remainder and the resulting Brent-McMillan error. It refines numerical error analysis only; it neither states nor implies irrationality of gamma.
- 依赖与状态。terminant-function asymptotics/hyperasymptotics / optimal truncation N=x or 2x / asymptotic expansion for I_0(2x)^{-2} published-scoped-numeric-only

### 09 · Approximation Of Logarithm, Factorial And Euler Mascheroni Constant Using Odd Harmonic Series

- 版本与身份。local undated 13-pp PDF, author metadata Narinder Kumar Wadhawan and Priyanka Wadhawan; textual identity with arXiv:2511.21102 was verified, but the exact local arXiv revision is not encoded in the PDF. No formal publication located. SHA-256 为 `5da7f8809978b87008046d30dd458e8c0e784b21ae0bcefe1e64d70920b7ffe1`。
- 本机原文定位。\['local PDF pp.11-13, (2.28)-(2.33) and conclusion', 'arXiv:2511.21102 (submitted 26 Nov 2025)'\]
- 核对范围。The local text uses heuristic ≃ substitutions to propose logarithm/factorial/gamma approximations. Its own p.12 reports gamma approximately 0.5736309333 with about 0.6% error, while p.13 subsequently asserts 0.577215664901; it supplies no controlled remainder resolving that conflict. It is not usable as a proof or as an irrationality input.
- 依赖与状态。heuristic replacement of finite sums by integrals / truncated expansion with omitted higher powers / empirical fitted corrections; no rigorous error bound hold-unverified-heuristic

### 10 · Approximations to Euler's constant

- 版本与身份。local arXiv:0708.2771v1 (21 Aug 2007), 11 pp; formal article Kh. Hessami Pilehrood and T. Hessami Pilehrood, Mathematical Inequalities & Applications 13(4) (2010), 761-773. Published statement and local theorem were both checked. SHA-256 为 `46d219d527ee9f5cc82f332c80dab55d296bf62e3fd9b115f5a4c41e0d8f62d3`。
- 本机原文定位。\['local arXiv PDF pp.3-5, Theorem 1 and Corollaries 2-6', 'published Mathematical Inequalities & Applications 13(4) (2010), 761-773, Theorems 1-2'\]
- 核对范围。Under explicit integer parameter inequalities, Theorem 1 gives an exact double-integral remainder representation for a transformed linear combination of harmonic/logarithmic approximants to gamma; Theorem 2 gives an explicit geometric error bound. These are convergence-acceleration results, not an irrationality proof.
- 依赖与状态。hypergeometric/binomial transformation / adjoint differential operators and Fubini / positive integral kernel and maximization lemma for the bounds published-scoped-numeric-only

### 11 · Collection of formulae for the Euler constant γ

- 版本与身份。Gourdon–Sebah web manuscript, local 2008-11-11 revision; no peer-reviewed primary version identified. SHA-256 为 `5f854a49dbfd21e88afb962af3141cd33a048cf83c773cebeab925944bf145cf`。
- 本机原文定位。local PDF pp. 1–10 (dated 11 Nov 2008), especially p. 1 integral identities; formula catalogue, not theorem/proof text
- 核对范围。Unrefereed collection of integral, series, product, and continued-fraction formulae for γ; individual identities are not independently proved in this document.
- 依赖与状态。The document attributes individual formulae to its bibliography, but gives no derivations sufficient to audit them here. / Any formula selected for a tool must be rechecked against its cited primary source or independently proved. blocker: bibliography/lead only; do not ingest catalogue formulas as certified skill rules.

### 15 · Euler's constant: Euler's work and modern developments

- 版本与身份。Published primary: Jeffrey C. Lagarias, Bull. Amer. Math. Soc. 50 (2013), no. 4, 527–628, doi:10.1090/S0273-0979-2013-01423-X; local copy is arXiv v6 (2013-10-25). SHA-256 为 `f1b94683051164c14cd2f3151cb97599578e7dc4dc64ddb69d0de2198b2c5e81`。
- 本机原文定位。local arXiv:1303.1856v6 pp. 1–3 (Introduction; Conjectures 1.0.1–1.0.2), table of contents pp. 1–2; the γ Diophantine-approximation survey is §3.15
- 核对范围。Historical and modern survey. It records, rather than resolves, the irrationality conjecture and the stronger non-period/transcendence conjecture; its value here is source routing and status control.
- 依赖与状态。Broadly dependent on the cited literature; it is not a self-contained proof source for the surveyed results. / No numerical or proof claim from a survey subsection should be promoted without checking the cited primary paper. held: status/bibliography anchor only; no standalone tool rule extracted.

### 20 · Fast convergences towards Euler-Mascheroni constant

- 版本与身份。Published primary: Cristinel Mortici, Comput. Appl. Math. 29 (2010), no. 3, 479–491, doi:10.1590/S1807-03022010000300009. SHA-256 为 `877790629d7d786016face917e2ec69476d032f74eeed6a066256982ec0b3985`。
- 本机原文定位。published local PDF pp. 480–485: Lemma 1 (p. 481), Theorem 2 (pp. 482–483), Theorem 3 (pp. 484–485)
- 核对范围。Gives parameterized logarithmic corrections to H_n−log n. In particular, the stated quadratic correction μ_n has lim_{n→∞} n^5(μ_n−γ)=3959/806400; it is an asymptotic acceleration result, not a finite-n certified bound.
- 依赖与状态。Lemma 1 converts a limit for successive differences into an error asymptotic. / The coefficient expansions used in Theorems 2–3 are symbolic power-series computations; their conclusions certify rates/limits, not interval-enclosed errors for a specified finite n. candidate: numerical acceleration recipe only; a rigorous digit certificate still needs an independent explicit remainder bound or interval check.

### 27 · On Euler's Constant

- 版本与身份。Local title page: Michel Waldschmidt, “On Euler’s Constant”, 2 Mar 2023, 77 slides; no formal publication/citable theorem article verified. SHA-256 为 `9923178a710a579e853d37f47bafbdc8bc295371cd030ddfdd281c34a01cc7ba`。
- 本机原文定位。08:G50; local slides 1, 37–38; https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/EulerConstant.pdf
- 核对范围。Actual local item is a 77-slide lecture note dated 2 Mar 2023. Its “Irrationality of Euler’s constant” slide labels irrationality a conjecture and reports only computational continued-fraction data plus a lower bound on a hypothetical denominator.
- 依赖与状态。numerical continued-fraction computation/OEIS data / cited surveys and known transcendence results held — status/reference source only; numerical observations and a conditional denominator lower bound are not a proof mechanism.

### 35 · Precise error estimate of the Brent–McMillan algorithm for the computation of Euler's constant

- 版本与身份。Jean-Pierre Demailly, Moscow Journal of Combinatorics and Number Theory 7(4) (2017), 271–306; local copy is HAL hal-01377144v2, submitted 2016-10-08, hash-verified (663,032 bytes). SHA-256 为 `54e02390d45d08dd2962a57349c37bea8cee67d959dfe43c94f1618620c783d6`。
- 本机原文定位。local HAL cover leaf (hal-01377144v2); article p. 1, abstract and (0.1)–(0.3)
- 核对范围。A rigorous error analysis for a numerical algorithm computing γ via I_0, K_0 and an optimally truncated divergent expansion. It supplies no irrationality criterion and no Diophantine-height bound; its role is numerical evaluation only.
- 依赖与状态。Bessel identities for I_α and K_0 and Γ′(n+1)=(H_n−γ)n! (article p. 1) / Hankel integral for 1/Γ and the paper's asymptotic/error analysis / formal statement/version check only formal-version-citation-checked; numerical-error tool only

### 36 · Ramanujan and Euler's constant

- 版本与身份。Richard P. Brent, CARMA Workshop presentation, 2010-07-08; local slide deck hash-verified (875,255 bytes); no journal article citation is present on the PDF. SHA-256 为 `ca538695d44f536b6309d5289177e8e834ae1942a201bbc537c8b601cbe2e74a`。
- 本机原文定位。local PDF slide 2 (Motivation; γ=−Γ′(1) and open-status statement); slides 62–64 (Conclusion)
- 核对范围。This is a 2010 workshop presentation surveying computation and Ramanujan-related formulas. It explicitly states that irrationality/transcendence of γ was not known; it is not a primary proof source or a new irrationality criterion.
- 依赖与状态。presentation-level review of continued fractions and computation rather than a self-contained theorem/proof dependency presentation-audited; background only, no proof component selected

### 47 · Some new algorithms for high-precision computation of Euler's constant

- 版本与身份。Formal citation and DOI checked; local file is a later author-hosted one-page abstract, not the 1980 full text. SHA-256 为 `e4290e83059ffd586850d06c1b474b93d7dc22bf2362abe946e04bc6593da7dc`。
- 本机原文定位。Local author-hosted PDF p.1 only (explicitly an abstract/comments page). Formal article: Math. Comp. 34 (1980), 305-312, DOI 10.1090/S0025-5718-1980-0551307-4.
- 核对范围。The available local source reports algorithms for high-precision computation and conditional continued-fraction denominator lower bounds if gamma or exp(gamma) is rational. It is numerical/computational evidence and does not establish irrationality; the full formal article was not present in the audited local PDF.
- 依赖与状态。Only the abstract-level Bessel-function algorithm and computed regular continued fractions are locally verified. Any exact algorithmic theorem, error bound, or reproduction step must be checked against the 1980 primary article before use. held-version-only

### 51 · The Euler constant: γ

- 版本与身份。Local 8-page web essay, not a refereed research-paper version; PDF metadata title gamma.dvi and date 2004-04-14. No formal-paper citation claimed. SHA-256 为 `ea06221f4c4c4076a28d845aedb0713f26ddac681276d5361bd51f87d9896e3e`。
- 本机原文定位。04:P03a; local PDF pp. 1–8 (Gourdon–Sebah, dated 2004-04-14)
- 核对范围。Expository/computational note only: defines γ, records bounds and algorithms. Its formula (7) labels the Brent–McMillan O(e^{-8n}) remainder as empirical, and it explicitly says irrationality/transcendence of γ is unknown; it supplies no irrationality criterion.
- 依赖与状态。Euler–Maclaurin expansion, exponential-integral and Bessel-function algorithms; formula (7) is attributed to Brent–McMillan but explicitly not proved in this note. held — retain solely as historical computation/background, not as a proof or a source of a certified γ irrationality tool.


## 积分、级数、分数部分与判据

### 02 · A family of criteria for irrationality of Euler's constant

- 版本与身份。local arXiv:math/0507231v1, 15 pp; no formal publication was located in the checked primary/index sources. SHA-256 为 `2751e941f6c44c0c6a7823e97a10a9614253f5d6ad0d9763ddfe33a1dceb400c`。
- 本机原文定位。\['local arXiv PDF p.5, Theorems 1-2; p.6, Theorem 3; p.12, proof', 'arXiv:math/0507231v1 (12 Jul 2005)'\]
- 核对范围。For 0&lt;=m&lt;=n, gamma=A_{n,m}-L_{n,m}+J_{n,m}; Theorem 2 makes rationality equivalent to the stated fractional-part identity, and Theorem 3 says that {d_n(-1)^m L_{n,m}}&gt;=0.707^n infinitely often for one fixed m implies irrationality. The observed n&lt;=1000 data/density language is explicitly only numerical suggestion.
- 依赖与状态。Padé approximation to log(u)/(1-u) / positivity/total monotonicity of the integral remainder J_{n,m} / Rosser-Schoenfeld LCM bound d_n&lt;=exp(1.039n) preprint-scoped-conditional

### 03 · A Hypergeometric Approach, Via Linear Forms Involving Logarithms, to Irrationality Criteria for Euler's Constant

- 版本与身份。local arXiv:math/0211075v4 (29 Apr 2009), 7 pp; formal version verified as Jonathan Sondow, with appendix by Sergey Zlobin, Math. Slovaca 59(3) (2009), 307-314. SHA-256 为 `a709a732b9101326b55fa927d265ccbb8232960ae74fa22fbd6626bcf51b1517`。
- 本机原文定位。\['local PDF p.2, Theorem 1; pp.3-5, Lemmas 1-3 and proof', 'published Math. Slovaca 59(3) (2009), 307-314, Theorem 1, doi:10.2478/s12175-009-0127-2'\]
- 核对范围。For its defined positive integer S_n and hypergeometric integral I_n, the fractional-part equality {log S_n}=d_{2n}I_n for some n (equivalently eventually all n) is equivalent to rationality of gamma. Hence failure of that equality at one n is an irrationality criterion; no local numerical convergence alone supplies it.
- 依赖与状态。Thomae transformation and the hypergeometric-to-series identity / partial-fraction linear forms in 1,gamma,logarithms / double-integral equality / Sondow's 2003 Beukers-integral criterion published-scoped-conditional

### 06 · An Infinite Product for e^gamma via Hypergeometric Formulas for Euler's Constant, gamma

- 版本与身份。local undated 5-pp manuscript matching Jonathan Sondow's arXiv:math/0306008 e-print; no formal journal publication located in the checked author/arXiv records. Local proofs (pp.2-4) were read. SHA-256 为 `fdd39a1c718c1fa5f3a2f7999951afc495c815d4a1cf972df61f6d70ddf0e4a9`。
- 本机原文定位。\['local PDF p.1, product (2); pp.2-4, four proofs', 'arXiv:math/0306008 (31 May 2003)'\]
- 核对范围。Establishes the displayed binomial-coefficient infinite product for e^gamma and hypergeometric/integral representations. It provides representations and numerical evaluation routes, not an irrationality statement for gamma or e^gamma.
- 依赖与状态。Thomae hypergeometric transformation / digamma integral / beta integral / double-integral representation of gamma preprint-scoped-representation-only

### 07 · An irrationality measure for Liouville numbers and conditional measures for Euler's constant

- 版本与身份。local arXiv:math.NT/0307308 (23 Jul 2003), 12 pp; no formal journal publication located in the checked author/arXiv records. Local conditional proof chain checked at pp.7-11. SHA-256 为 `a91aebbac1ee54ae0acb6d24b44d68f5b4d658d86e0ea88eba6a6c0e416c0ab8`。
- 本机原文定位。\['local PDF p.8, Theorem 1; p.9, Theorem 3; pp.10-11, conditional exponent results', 'arXiv:math.NT/0307308 (23 Jul 2003)'\]
- 核对范围。Theorem 1 conditionally concludes that gamma is irrational and has irrationality base beta(gamma)&lt;=2e if lim_n log(log S_n)/n=0; later results impose other explicit hypotheses and, in places, additionally assume gamma irrational. The paper offers numerical evidence for hypotheses, not their proof.
- 依赖与状态。Sondow's Beukers-integral criterion d_{2n}I_n={log S_n} / Stirling and prime-number-theorem asymptotics / conditional approximation lemmas for irrationality bases/exponents preprint-scoped-conditional

### 12 · Criteria for Irrationality of Euler's Constant

- 版本与身份。Published primary: Jonathan Sondow, Proc. Amer. Math. Soc. 131 (2003), no. 11, 3335–3344, doi:10.1090/S0002-9939-03-07081-3; local copy is arXiv v2 (2002-10-04). SHA-256 为 `45e9d7788c6f71643ea2f39f7572cff5f5eced8f1947d144b5329b3d4ddfcd0f`。
- 本机原文定位。local arXiv:math.NT/0209070v2 pp. 1–3 (definitions and statement), pp. 4–10 (Theorems 1, 4, 5; Lemma 3), pp. 12–14 (combinatorial appendix)
- 核对范围。For the explicitly defined Beukers-type integral I_n and integer S_n, proves {log S_n}=d_{2n} I_n for one n iff for all sufficiently large n iff γ is rational; Corollary 6 gives the stated infinitely-often fractional-part sufficient condition for irrationality.
- 依赖与状态。Beukers/Apéry integrals are motivation, not a transferred irrationality theorem. / The local proof evaluates I_n (Theorem 1), uses d_{2n}A_n∈Z and 0&lt;d_{2n}I_n&lt;1 (Lemma 3), then proves the equivalence (Theorems 4–5); the appendix proves the needed combinatorial identity. candidate: exact finite-n criterion/linear-form audit component; it is conditional and does not prove γ irrational without verifying its fractional-part premise.

### 13 · Double Integrals for Euler's Constant and ln(4/Pi) and an Analog of Hadjicostas's Formula

- 版本与身份。Published primary: Jonathan Sondow, Amer. Math. Monthly 112 (2005), no. 1, 61–65, doi:10.2307/30037385 (also doi:10.1080/00029890.2005.11920168); local copy is a 2004 manuscript. SHA-256 为 `377b57366d0d7706de81b7dff50d514ea8aaa7e6ab3903fdf90386489712a04f`。
- 本机原文定位。local manuscript p. 1, equations (2)–(3) (double integrals for γ and log(4/π)); pp. 4–5, Theorem 1 and proof of the analytic-continuation identity
- 核对范围。Proves γ=∫_\[0,1\]^2 (1−x)/((1−xy)(−log(xy))) dxdy, alongside the alternating analogue for log(4/π); its final theorem concerns a ζ* integral identity, not an irrationality result for γ.
- 依赖与状态。Termwise integration/geometric expansion and the standard Γ(s)ζ*(s) integral in local pp. 4–5. / The article explicitly describes Beukers integrals only as analogy; no transfer of Apéry irrationality is established. candidate: validated integral-representation component; not an irrationality certificate.

### 14 · Euler's constant, q-logarithms, and formulas of Ramanujan and Gosper

- 版本与身份。Published primary: Jonathan Sondow and Wadim Zudilin, Ramanujan J. 12 (2006), no. 2, 225–244, doi:10.1007/s11139-006-0075-1; local file is arXiv v1 (2003-04-02), described by the authors as an extended preprint. SHA-256 为 `80b8fdd56e422cb559f4e0dda4fb38e81eaa512f976ec7285a0918252fa04342`。
- 本机原文定位。local arXiv:math/0304021v1 pp. 1–2 (q-log definition and prior linear form), pp. 4–8 (Lemmas 1–7), p. 9 (Theorem 2 rationality criterion); published pagination may differ
- 核对范围。For its explicitly defined I_{n,m}, L_{n,m} and range 2^(n−1)≤m≤2^(n+1), proves the stated fractional-part equality d_{2n}L_{n,m} mod 1 = d_{2n}I_{n,m}; develops q=2/3 formulae and asymptotics. It does not assert an unconditional irrationality proof for γ.
- 依赖与状态。The local proof derives the representation through Lemmas 1–7, then invokes the prime-number-theorem growth of d_N to ensure 0&lt;d_{2n}I_{n,m}&lt;1 (p. 9). / It explicitly builds on Sondow's earlier criteria; its q&gt;3 damping obstruction is Lemma 14 (local pp. 22–23). candidate: q-log/finite-linear-form criterion component, with range and asymptotic hypotheses retained; no unconditional conclusion.

### 21 · Generalizations of Guillera-Sondow's double integral formulas

- 版本与身份。Local PDF header: arXiv:math/0606287v3 \[math.NT\], 19 Aug 2006; author’s page labels it a preprint (no journal version verified). SHA-256 为 `3a46cdd2f9c24953f866d0127385d40a7ef46b016de791945bac7f60c78d6e30`。
- 本机原文定位。07:EXT-0016; local pp. 1–3, Theorems 1–4; https://arxiv.org/abs/math/0606287
- 核对范围。Actual local statement: Zlobin proves m-fold integral identities (Theorems 3–4) expressing them through the Lerch transcendent; gamma and log(4/pi) occur only as special representations. This is an analytic-representation source, not an irrationality theorem.
- 依赖与状态。Lerch transcendent Phi and its shift/differentiation identities (local (1)–(2)) / Guillera–Sondow double-integral formulas cited as the m=2 antecedent held — retain only for verified integral/Lerch identities; no integer coefficients, denominator clearing, or nonzero shrinking linear form is supplied.
- 调用入口。[高维正积分](../../math-sondow-log-fractional-certificate/references/double-integral-extensions.md)

### 22 · Integrals Over Polytopes, Multiple Zeta Values and Polylogarithms, and Euler's Constant

- 版本与身份。Local PDF header: arXiv:0705.0732v2, 24 Sep 2007. Primary published record verified: DOI 10.1134/S0001434608090290 (Pleiades/Mathematical Notes abstract). SHA-256 为 `2616bacbf889626c530c62fed01ed3551537d1ea13d4a5e8592c182beff11c5f`。
- 本机原文定位。04:P10; local pp. 1, 5–6, 11–12; https://arxiv.org/abs/0705.0732; https://doi.org/10.1134/S0001434608090290
- 核对范围。Actual local Theorem 1 expresses triangle integrals as integer linear combinations of MZVs and polynomials in zeta values; Proposition 2 gives gamma as an integral involving generalized binomial coefficients. The gamma material is representational, while the MZV application includes explicitly conditional algebraic-independence reasoning.
- 依赖与状态。multiple-zeta identities proved from the triangle integral (local Lemma 1/Theorem 1) / Sondow 2003 criterion/integral formulas are cited for the separate gamma approximation discussion / the conditional part depends on algebraic independence of pi,zeta(3),zeta(5),... held — usable as a cited integral/MZV source only; it provides no gamma integer-form irrationality certificate and its conditional claims must retain their hypothesis.

### 25 · New Vacca-Type Rational Series for Euler's Constant and Its "Alternating" Analog ln(4/Pi)

- 版本与身份。Local PDF header: arXiv:math/0508042v1, 1 Aug 2005. Published version verified from the author bibliography: Additive Number Theory, Springer (2010), pp. 331–340. SHA-256 为 `1ba9c7fa19cc537329d52f52a10b80ba703df50079af41f09f0343812a54c3ab`。
- 本机原文定位。07:EXT-0019; local pp. 1–4, Theorems 1–2; https://arxiv.org/abs/math/0508042
- 核对范围。Actual local Theorem 1 proves binary-digit rational series for gamma and log(4/pi); Theorem 2 gives a base-q/additive acceleration. These are convergent representations, not a rationality contradiction.
- 依赖与状态。Vacca’s series and binary digit-count identities / Addison’s series/general base-q Vacca construction candidate — use the exact series identities; held for irrationality because convergence of rational partial sums gives neither the requisite denominator control nor a nonzero integer linear form.
- 调用入口。[Vacca 有理级数](finite-rational-series.md)

### 30 · On irrationality of Euler’s constant and related asymptotic formulas

- 版本与身份。Local PDF header: arXiv:2312.00295v1 \[math.GM\], 3 Aug 2023; no published version verified. SHA-256 为 `2c44fd61e6c7e03bfceee962d7f465143d6d23ffb356b6c5d755672bae80a075`。
- 本机原文定位。04:附录; local pp. 1, 5–9; https://arxiv.org/abs/2312.00295
- 核对范围。The local preprint claims gamma irrationality from Sondow’s criterion, but its proof is not valid. Lemma 3 is concluded from computer checks only through n=200; Lemma 4 is explicitly conditional on a conjectured formula in another answer and uses “numerics suggest”; the final step substitutes d_{2n}~e^{2n} inside a fractional-part expression and then asserts a limit 0. None establishes Sondow’s required fractional-part condition or an integer-form contradiction.
- 依赖与状态。Sondow 2003, Criteria for irrationality of Euler’s constant (the criterion invoked) / Sondow 2005 double-integral identity / unproved all-n identities/asymptotics and a non-rigorous fractional-part limit held — do not route as an irrationality proof. The claimed conclusion must remain disputed/withheld unless replaced by a valid all-n integer-form, nonvanishing, and decay argument.

### 44 · Rebuttal of Kowalenko's paper as concerns the irrationality of Euler's constant

- 版本与身份。Primary record checked: local file is arXiv:1202.3093v4. SHA-256 为 `6b0edd98b5d2337dfe5683e50626c61c189c75d51fb440b1cf68b9431bd2244e`。
- 本机原文定位。Local arXiv PDF pp.1-3: abstract; sections 2-3. arXiv:1202.3093v4 (2012-04-05).
- 核对范围。A claim audit/counterargument: it identifies the invalid inference in Kowalenko's asserted proof and concludes that irrationality of gamma remains open. It also records that the alleged rational series representation was known; it supplies no positive irrationality certificate.
- 依赖与状态。The rebuttal depends only on explicit counterexamples to the claimed digit/randomness and positive-series arguments. It must be used as a negative guardrail, not as a source of a proof or an approximation method. guardrail-rebuttal

### 56 · Vacca-type series for values of the generalized-Euler-constant function and its derivative

- 版本与身份。Local source is arXiv:0808.0410v1 (2008-08-04); primary version verified: Kh. Hessami Pilehrood and T. Hessami Pilehrood, Journal of Integer Sequences 13 (2010), Article 10.7.3 (received 2009-10-19; revised 2010-06-27). SHA-256 为 `998c9e2d85231a69dc229337a837cd4ab0bf2d69237f9548792d00c2508c344f`。
- 本机原文定位。07:EXT-0018 / 08:G25; local PDF pp. 4–10, Theorems 1–5; pp. 12–15, Corollaries 9–15
- 核对范围。Gives base-B Vacca/Ramanujan/Addison series and analytic continuation for γ_{a,b}(z) and derivatives; specializes to exact series for log(4/π), log Somos constants, log Glaisher–Kinkelin A, G/π and ζ'(2)/π². These are representation/acceleration identities, not integer-form irrationality criteria for γ.
- 依赖与状态。Proofs expand Catalan-type integrals through a base-B generating-function identity, use uniform convergence for termwise integration, and invoke Lerch-transcendent analytic continuation and prior Sondow–Hadjicostas γ_{a,b} identities. candidate — base-B digit-series identity/acceleration component only; no conversion of convergence into an irrationality conclusion.


## Padé、多重正交与算术高度

### 05 · An Infinite Family of Apéry-like Recurrences for Euler's Constant

- 版本与身份。local arXiv:2610.13919v1, 32 pp; no formal publication located. The local component proof chain was checked at the cited pages. SHA-256 为 `e3ef0106c717f6a66e441fa468240b684a21c648cfcf2f9a8ca9f368c801d17b`。
- 本机原文定位。\['local PDF p.9, Theorems 1-3; pp.10-13, Proposition 1 and proof of Theorem 2; pp.15-19, Lemma 9 and proof of Theorem 3', 'arXiv:2610.13919v1 (9 Oct 2026)'\]
- 核对范围。Claims that, for r=3, specified trajectories t in T_3^* and a generic dual vector, a normalized dual-CMF limit equals gamma; the algebraic identity gives p_r^T S_r(0)/q_r^T S_r(0)=gamma. It is an approximation/limit construction only, and the paper itself says its empirical convergence is insufficient for an irrationality proof.
- 依赖与状态。Meijer-G residue identity (Proposition 1) used for Theorem 2 / CMF state-vector construction / Lemma 2 dual-convergence criterion / Lemma 9 strong recessivity based on its stated asymptotic basis preprint-scoped-approximation-only

### 08 · Application of Padé Approximation to Euler’s constant and Stirling’s formula

- 版本与身份。local HAL hal-02017852v3 (submitted 9 Aug 2019), 18 pp; published Marc Prévost and Tanguy Rivoal, The Ramanujan Journal 54(1) (2021), 177-195, doi:10.1007/s11139-019-00201-9. SHA-256 为 `947724ac14cd2e703f46d5d920a26458c799a4685d191c91a1a58850d847ff93`。
- 本机原文定位。\['local HAL PDF p.3, Theorem 1 (4)-(5); p.4, discussion excluding an irrationality deduction', 'published Ramanujan Journal 54(1) (2021), 177-195, Theorem 1'\]
- 核对范围。Gives an effective Padé error bound for the digamma expansion and resulting fast convergent approximations to gamma; local p.4 explicitly says these approximations cannot prove irrationality because of log(n) and denominator growth.
- 依赖与状态。Stieltjes-integral representations for digamma/log-Gamma / near-diagonal Padé approximants / orthogonal-polynomial error identity and comparison published-scoped-numeric-only
- 调用入口。[正矩 Padé](../../math-gamma-multiple-laguerre-approximants/references/legendre-pade-moments.md)

### 24 · Legendre modified moments for Euler's constant

- 版本与身份。Local author manuscript dated 25 Jun 2007. Primary publication verified: Marc Prévost, Journal of Computational and Applied Mathematics 219(2) (1 Oct 2008), 484–492, DOI 10.1016/j.cam.2007.09.015. SHA-256 为 `daf112a9a9a8f9e6f25e9e9cb04fce8f2356c10644654b90ce411ca8c864af56`。
- 本机原文定位。04:P11c; 07:EXT-0533; local pp. 1–2, 8–10; https://doi.org/10.1016/j.cam.2007.09.015
- 核对范围。Actual local Theorem 1 gives gamma=A_{n,m}-L_{n,m}+J_{n,m}, with explicit logarithmic and rational terms; Theorem 4 proves signed J_{n,m} is totally monotone and O(4^{-n}). The arithmetic section states only sufficient irrationality criteria, not irrationality of gamma.
- 依赖与状态。shifted Legendre polynomial orthogonality/Rodrigues formula / Markov–Stieltjes integral representation of the weight / Fubini and integrations by parts; arithmetic corollaries require fractional-part conditions not established in the paper candidate — retain the exact identity and certified O(4^{-n}) remainder, but hold every irrationality inference until a valid integrality/LCM and nonvanishing argument is supplied.
- 调用入口。[Legendre 修正矩](../../math-gamma-multiple-laguerre-approximants/references/legendre-pade-moments.md)

### 26 · On a continued fraction expansion for Euler's constant

- 版本与身份。Local PDF header: arXiv:1010.1420v3 \[math.NT\], 29 Dec 2013. Published journal record verified: Journal of Number Theory 133(2) (2013), DOI 10.1016/j.jnt.2012.08.016. SHA-256 为 `0fc9404ea3f673bc2215cbce0858ba8a18a9f8f0c00c73d0465c642953aea0dc`。
- 本机原文定位。04:P20; 07:EXT-0011; 08:G06; local p. 1 and recurrence/continued-fraction sections; https://arxiv.org/abs/1010.1420; https://doi.org/10.1016/j.jnt.2012.08.016
- 核对范围。Actual local abstract constructs rational approximations/linear forms in 1 and gamma and a non-simple continued fraction converging sub-exponentially. Its Apéry discussion explicitly lists the integer-form conditions that prove irrationality for zeta(3), but it does not establish analogous sufficient integrality and decay for gamma.
- 依赖与状态。Aptekarev et al. rational approximants / Meijer G-functions, hypergeometric series and creative telescoping / continued-fraction conversion of the inhomogeneous recurrence candidate — retain recurrence/continued-fraction construction; hold all irrationality use absent a separately checked integer-form, denominator and nonvanishing proof.

### 31 · On linear forms containing the Euler constant

- 版本与身份。arXiv:0902.1768v2 \[math.NT\], 2009-02-28; local file hash-verified (94,905 bytes); no journal version was identified in this audit. SHA-256 为 `84f09b5f2122f9fe01ce1fd9e75fe6c7bdbcbb322c8b24912b485fc45ddffa16`。
- 本机原文定位。local PDF pp. 2–4, equations (2), (3), (8)–(11)
- 核对范围。Validated finite factorial-normalized determinant identity and recurrence. Printed (9) and (10)–(11) imply a leading constant one quarter of (3). Under the same recurrence, Tulyakov’s published small branch is of order 16^(-n)/n, so the printed nonzero limit of 16^n g_n is also incompatible with its cited source. Adopt finite algebra only.
- 依赖与状态。Tulyakov DOI 10.4213/mzm5260 for sequence integrality / Aptekarev–Tulyakov DOI 10.1090/S0077-1554-09-00175-7 for factorial lattice determinants / Tulyakov DOI 10.4213/spm16, eqs. (3)–(4), contradicts printed small-branch scale; actual g branch normalization remains to be established finite determinant replay only; printed asymptotic estimates excluded
- 调用入口。[精确混合行列式与渐近审计](mixed-log-height-audit.md)

### 32 · On Rational Approximations to Euler's Constant and to γ + log(q)

- 版本与身份。Carsten Elsner, International Journal of Mathematics and Mathematical Sciences (2009), Article ID 626489, 22 pp., DOI:10.1155/2009/626489; local file hash-verified (597,502 bytes). SHA-256 为 `c76817e3c589125a192bf291806fc55631a826eb2a972161defb3db59b12e679`。
- 本机原文定位。local journal PDF p. 1 abstract; p. 6, Theorem 2.4, especially (2.7)–(2.8); its printed title writes q=a/b
- 核对范围。For positive integers a,b,d,m with d≥42, Theorem 2.4 constructs transformed rationals approximating γ+log(a/b), with an exponential-in-m error estimate. This is an approximation/denominator construction, not an irrationality proof for γ or γ+log(a/b); the a/b normalization and d≥42 restriction are essential.
- 依赖与状态。Euler summation formula with Bernoulli-polynomial remainder (PDF p. 7, (3.4)–(3.9)) / denominator bookkeeping using lcm values and von Staudt's theorem (PDF p. 12, (4.9)–(4.13)) / formal statement/version check only; no downstream proof dependency accepted without a separate audit formal-version-citation-checked; approximation method only
- 调用入口。[混合对数高度](mixed-log-height-audit.md)

### 38 · Rational approximation of Euler's constant using multiple orthogonal polynomials

- 版本与身份。Walter Van Assche and Thomas Wolfs, Combinatorics and Number Theory 14(2) (2025), 141–162, DOI:10.2140/cnt.2025.14.141; local source is arXiv:2404.09799v3, 2025-04-15, hash-verified (264,508 bytes). SHA-256 为 `d56423c36c73e318ae6850d1c8a36a309766db668041d9c3161500c54adf9459`。
- 本机原文定位。local arXiv PDF p. 3, Theorem 1.2 and its height/error discussion; p. 4, Theorem 1.3; p. 6, Propositions 2.2–2.3
- 核对范围。Theorem 1.2 constructs rational functions approximating γ+log x (x&gt;0); at x=1 it gives integral P_n,Q_n but records r(n)=4 n^(1/4)/log n·(1+o(1))→0, hence is explicitly far from proving γ irrational. The dual theorem concerns e^xE_1(x), and at x=1 δ=eE_1(1). Integer normalizations n!lcm(1,…,n)F_{n;1}^{(I)} and n!F_{n;2}^{(I)} must be kept with the claimed error.
- 依赖与状态。mixed type multiple orthogonal polynomials associated with the exponential integral / Proposition 2.2's explicit γ+log x linear form and Proposition 2.3's integrality (PDF p. 6) / formal statement/version check only; no irrationality conclusion admitted formal-version-citation-checked; conditional approximation/height construction only

### 39 · Rational approximation to Euler's constant at a geometric rate of convergence

- 版本与身份。José A. Adell and Alberto Lekuona, Mathematics of Computation 89(325) (2020), 2553–2561, DOI:10.1090/MCOM/3528; local source has pre-publication placeholder front matter, hash-verified (287,905 bytes). SHA-256 为 `02e459a234ae8fbd961e4240142cc70886803e7d40f064e9fade148f81656d25`。
- 本机原文定位。local PDF p. 2, equations (1.4)–(1.6) and explicit no-irrationality notice; p. 7, Corollary 3.4 and (3.11)–(3.13)
- 核对范围。For λ=2N it gives an explicit rational expression for γ with error at most 3e^(−λ)/λ after truncating a Poisson/harmonic expectation and a log series. The authors expressly state that the convergence is not sufficient to prove irrationality; there is no controlled common denominator/height comparison supporting such an inference.
- 依赖与状态。Poisson expectation f(λ)=E H(N_λ)−log λ and its exponential error (PDF p. 2) / finite log expansion log(1+a) used with a=1 (PDF p. 7, (3.10)–(3.13)) / formal statement/version check only formal-version-citation-checked; numerical rational approximation only
- 调用入口。[几何逼近与有效高度](mixed-log-height-audit.md)

### 40 · Rational approximations for the quotient of gamma values

- 版本与身份。Kh. Hessami Pilehrood and T. Hessami Pilehrood, Indagationes Mathematicae (N.S.) 20(4) (2009), 583–601, DOI:10.1016/S0019-3577(09)80027-X; local source is arXiv:1010.0429v2, 2010-12-09, hash-verified (189,901 bytes). SHA-256 为 `66e1b1a2fee570a7e4f7d40543f1f630fc2dba2e40e451a18de3a272202eb437`。
- 本机原文定位。local arXiv PDF p. 5, Theorem 1 and (14)–(15); p. 8, Lemma 1/(16)–(17); p. 14, Theorem 2 and Corollary 4
- 核对范围。For rational a_1,a_2,b with a_1−a_2∉Z, a_i&gt;−1,b&gt;0, Theorem 1 approximates Γ(a_2+1)/(Γ(a_1+1)b^(a_2−a_1)). The exact integer scaling includes μ_{n}^{a_2−a_1}μ_{2n}^{a_2} and n!, and the paper explicitly says its linear forms do not prove irrationality of the quotient. Euler γ occurs only as a limit/differentiation case giving explicit Aptekarev numerators, not as a proof of γ irrationality.
- 依赖与状态。multiple Jacobi–Laguerre polynomial integral R_n (PDF p. 8, (16)–(17)) / asymptotics and arithmetic scaling in Theorem 1 (PDF p. 5) / coalescing-parameter derivative leading to the digamma/γ formula in Theorem 2 and Corollary 4 (PDF p. 14) / formal statement/version check only formal-version-citation-checked; retain the parameterized Gamma-quotient normalization, no γ-only irrationality component

### 41 · Rational approximations for values of derivatives of the Gamma function

- 版本与身份。Formal primary version checked against AMS metadata; the local 37-page PDF is the published paper text dated 2009-01-13. SHA-256 为 `4244ef49d4eccbb0ec9d91338b6e904ae7bd602e60909617102f9b846301acf3`。
- 本机原文定位。Local PDF pp.1-5: abstract; Theorems 1 and 2; p.8, Proposition 1. Formal article: Trans. Amer. Math. Soc. 361 (2009), no.11, 6115-6149, DOI 10.1090/S0002-9947-09-04905-8.
- 核对范围。For x&gt;0, Theorem 1 constructs factorial-height rational-function approximants to log(x)+gamma with a subexponential error and nonvanishing infinitely often; x=1 gives gamma. Theorem 2 supplies simultaneous rational approximations to gamma and zeta(2)-gamma^2. These approximation statements do not make an integral linear form tend to zero, and Conjecture 1 (the stronger n! denominator) remains a conjecture.
- 依赖与状态。Selected construction uses simultaneous Pade approximants to Euler functions, recurrence/asymptotic analysis, and the stated denominator bounds. For gamma, retain the paper's explicit obstruction: its Aptekarev-type linear forms are not small enough after clearing denominators; do not promote convergence or nonvanishing to irrationality. candidate-with-obstruction
- 调用入口。[Gamma 多 Laguerre 矩](../../math-gamma-multiple-laguerre-approximants/references/legendre-pade-moments.md)

### 42 · Rational approximations for values of the digamma function and a denominators conjecture

- 版本与身份。Primary record checked: local file is arXiv:1004.0578v1. No formal-journal version was established in this audit. SHA-256 为 `225d48f305e7709c3b0a80c216f50ac8bdf18500c160aecfea213e57a112714b`。
- 本机原文定位。Local arXiv PDF pp.1,3-7,19: abstract; Theorem 1; Corollaries 1-6; bibliography. arXiv:1004.0578v1 (2010-04-05).
- 核对范围。For a,b in Q with a&gt;-1 and b&gt;0, Theorem 1 gives Jacobi-Laguerre rational approximants to log(b)-psi(a+1), including gamma at (a,b)=(0,1), and exact numerator/denominator formulas. Corollary 2 specializes to rational digamma arguments; Corollaries 5-6 establish the stated denominator divisibilities for the Rivoal-related sequences. The gamma specialization is an approximation result, not an irrationality proof.
- 依赖与状态。The selected proof chain is the generalized Jacobi-Laguerre polynomial identity, hypergeometric numerator/denominator formulas, and Lemmas 3-5 asymptotics; the Rivoal denominator comparison is Theorem 2/Corollaries 5-6. Neither the displayed exponential ratio error nor the denominator statements alone supply a vanishing integer linear form in gamma. candidate-with-obstruction


## 相邻常数、digamma、有限类似物与 Gamma 商

### 16 · Euler–Lehmer constants and a conjecture of Erdös

- 版本与身份。Published primary: M. Ram Murty and N. Saradha, J. Number Theory 130 (2010), no. 12, 2671–2682, doi:10.1016/j.jnt.2010.07.004. SHA-256 为 `a9f7ba855ad19139141722f01042002374f6c82335439358e13dd69e1c80d9e0`。
- 本机原文定位。published local PDF pp. 2671–2673 (definition and Theorems 1–4), pp. 2675–2677 (Lemmas 8–12), pp. 2678–2679 (§3 proof of Theorem 1)
- 核对范围。For Euler–Lehmer constants γ(a,q), proves that at most one number in the infinite list γ(a,q), 1≤a&lt;q, q≥2, is algebraic; conditionally describes the γ(2,4)=γ/4 exception if γ is algebraic. This is a result on generalized constants, not irrationality of γ.
- 依赖与状态。Gauss/digamma formulas in Lemma 8 and Baker's linear-forms theorem, stated as Lemma 9 and used through Lemma 10. / Theorem 1's proof is local §3 but its transcendence step depends essentially on Baker's theorem; the paper also imports earlier results as Lemmas 11–12. held: rigorous contextual result for Euler–Lehmer constants; no direct γ-irrationality tool component.

### 18 · Expansions of generalized Euler's constants into the series of polynomials in π^{-2} and into the formal enveloping series with rational coefficients only

- 版本与身份。Published primary: Iaroslav V. Blagouchine, J. Number Theory 158 (2016), 365–396, doi:10.1016/j.jnt.2015.06.012; local arXiv v4 (2016-12-16) says it copies the journal content with minor corrections. SHA-256 为 `2eba6bd7e4fb5ce422d6dee568e7add1a2197c172340c5ab57f080e8614380f1`。
- 本机原文定位。local arXiv:1501.00740v4 pp. 7–8, equations (19)–(20) (convergent Stieltjes-constant series); pp. 16–17, equations (45)–(47) (formal/semi-convergent enveloping expansion and finite-N remainder parameter)
- 核对范围。Provides a convergent π^{-2}/Stirling-number series for γ_m, including γ=γ_0, and separately a finite-order alternating enveloping expansion. The latter is explicitly not an equality to an infinite convergent rational series.
- 依赖与状态。The derivation of (19) uses Jensen–Franel's integral/formal series manipulations; the convergence bound is developed in local pp. 9–12. / The rational-coefficient expansion follows by a formal interchange of non-absolutely-convergent sums (p. 16), then is retained only as finite-N formula (46)–(47) with 0&lt;θ&lt;1 (p. 17). candidate: numerical/asymptotic expansion component, provided the convergent and finite-order enveloping regimes are kept separate.

### 28 · On finite analogues of Dobiński's formula and of Euler's constant via Gregory polynomials

- 版本与身份。Local PDF header: arXiv:2604.01578v1 \[math.NT\], 2 Apr 2026. Author publication list reports it accepted in International Journal of Number Theory; no final paginated version verified. SHA-256 为 `b8766f9be74d0a25c80b04e382449902c83a2c7f60641d746cb4974fd97fc6a4`。
- 本机原文定位。04:P27; 08:G54; local pp. 1–2, Theorem 1.1; https://arxiv.org/abs/2604.01578
- 核对范围。Actual local Theorem 1.1 is an identity in the quotient ring A for a finite analogue e_A; the paper extends finite analogues of gamma via Gregory polynomials. It explicitly notes that nonzero/irrationality-type questions in A remain unknown, and it does not concern the real Euler constant’s irrationality.
- 依赖与状态。finite multiple zeta values in A / Kaneko–Matsusaka–Seki finite gamma analogues / Gregory-polynomial identities and Fermat-quotient finite logarithms candidate — retain only finite-ring identities with their ambient ring; no transfer to real gamma or irrationality is licensed.
- 调用入口。[Gregory 有限类似物](finite-rational-series.md)

### 29 · On finite analogues of Euler's constant

- 版本与身份。Local PDF header: arXiv:2401.09935v2 \[math.NT\], 23 Jan 2025. Primary published citation verified: International Mathematics Research Notices IMRN 2025(2), Paper rnae281, DOI 10.1093/imrn/rnae281. SHA-256 为 `7e0ee4d2ba3ade1cda070a8e85c403da74928a3fbbad964a3c24f8394ba43679`。
- 本机原文定位。08:G53; local pp. 1–2; https://arxiv.org/abs/2401.09935; https://doi.org/10.1093/imrn/rnae281
- 核对范围。Actual local abstract defines several finite analogues in A and proves relations among them modulo the Q-span of 1 and finite logarithms. The introduction expressly says it is unknown whether real gamma is irrational and states that the article instead studies finite analogues.
- 依赖与状态。finite multiple zeta values and the Kaneko–Zagier correspondence conjecture / Fermat quotients/finite logarithm / Gregory coefficients and finite regularization of zeta(1) candidate — finite-analogue results are admissible with their conjectural dependencies explicit; no real-gamma irrationality consequence.

### 33 · On the Arithmetic Nature of the Values of the Gamma Function, Euler's Constant, and Gompertz's Constant

- 版本与身份。Tanguy Rivoal, Michigan Mathematical Journal 61(2) (2012), 239–254, DOI:10.1307/mmj/1339011525; local prepublication dated 2011-03-05, hash-verified (234,498 bytes). SHA-256 为 `0bac95bf781ec79692bbcb52e2045b5bc3007b978344ea38d9b5503326812418`。
- 本机原文定位。local PDF p. 1 abstract; p. 2, Theorems 1–2 and inequalities (1.1)–(1.2)
- 核对范围。For rational z&gt;0, Theorem 1 gives a simultaneous lower bound for approximation to (γ+log z,G_0(z)); in particular at least one member is irrational. Theorem 2 gives the corresponding disjunctive transcendence statement for algebraic z. At z=1 this concerns the pair (γ,δ=G_0(1)); it does not prove γ irrational/transcendental by itself. The height is H=max(\|p\|,\|q\|,\|r\|) and the exponent is H^(−3−ε), so this joint normalization must be retained.
- 依赖与状态。Hermite–Padé approximants to 1, exp, and G_α, as identified immediately after Theorem 1 / Nesterenko linear-independence criterion for the quantitative statement / Shidlovskii E-function results for the qualitative joint statement / formal statement/version check only; no γ-only inference adopted formal-version-citation-checked; preserve only its disjunctive γ–G_0(z) scope

### 34 · On the Uniqueness of Ein(1) among Linear Combinations of the Euler-Mascheroni and Euler-Gompertz Constants

- 版本与身份。arXiv:2510.00315v1 \[math.NT\], 2025-09-30; local file hash-verified (269,533 bytes); no journal version identified. SHA-256 为 `809143ef6fea26a2c917ea6a7a5a1679f97c62737d9fa5f263f3f20e7db4116c`。
- 本机原文定位。local PDF p. 1, abstract and equations (1)–(3); p. 2, equations (4)–(9) and the stated imported arithmetic claims; p. 5 proof of the divergent-series uniqueness calculation
- 核对范围。The paper studies the analytic/Borel-summation uniqueness of α=1/e in γ+αδ and records γ+δ/e=Ein(1). It explicitly says neither γ nor δ is known irrational. Its statements about transcendence/disjunctive transcendence are imported from other work; they cannot be promoted to a γ-only result. The exact coefficient is 1/e and δ=−e Ei(−1), not an arbitrary rational coefficient.
- 依赖与状态。Hardy's exponential-integral identity (PDF p. 1, (1)–(3)) / claimed prior Powers (2025) E-function/Siegel–Shidlovskii work for the arithmetic assertions (PDF p. 2, (iii)–(v)) / absolute convergence of the rearranged double series in the uniqueness calculation (PDF p. 5) preprint-audited-with-external-dependency; keep only the α=1/e analytic identity/uniqueness component, with arithmetic claims held pending audit of the cited predecessor

### 37 · Rational approximants for the Euler-Gompertz constant

- 版本与身份。arXiv:1104.4721v2 \[math.NT\], header dated 2011-11-10, while the manuscript title page says 2018-11-07; local file hash-verified (138,820 bytes); no journal version identified. SHA-256 为 `9083e2e8585a244814b0ca9787dd6ddc302ff69888e28a417025f26d9984401e`。
- 本机原文定位。local PDF p. 1, Main Theorem and Corollaries 1.2–1.3; pp. 13–14, proofs of those corollaries
- 核对范围。It constructs explicit integral/binomial sequences a_m/b_m→−δ for the Euler–Gompertz constant δ, not γ. Corollary 1.2 follows by differentiating the stated uniform limit and using the identity for ∫x^k e^(−x)/(x+1)dx. No denominator-versus-error estimate sufficient for irrationality is asserted or obtained, and its conjectural digamma formula is not a theorem.
- 依赖与状态。uniformity in the proof of Theorem 1.1 before differentiation (PDF pp. 3, 13) / the integral identity in Lemma 3.1 used in Corollary 1.2 (PDF p. 13) / growth/nonvanishing required for irrationality is absent; Conjecture 1.4 remains unselected preprint-audited; δ-approximation component only, metadata-date conflict retained and no irrationality dependency accepted

### 43 · Rational function approximations of the special function e^x E_1(x) and applications to irrationality of Euler-Gompertz constant delta

- 版本与身份。Primary record checked: local file is arXiv:2210.06768v2. No formal publication version was established in this audit. SHA-256 为 `e94116441dbfd20784c10d5ebb74087d1e6fbac16050e0736072b0cab012c7d6`。
- 本机原文定位。Local arXiv PDF pp.1-2,6-7,15-16: abstract; Theorem 4.1; Theorems 7.1-7.2. arXiv:2210.06768v2 (2024-09-22).
- 核对范围。The paper proves convergence and bracketing of a continued fraction for F(x)=e^x E_1(x), and develops rational approximations to the Euler-Gompertz constant delta=F(1). Its proposed irrationality route is conditional on proving delta B_i-A_i is nonzero for every i. It concerns delta, not Euler's constant gamma.
- 依赖与状态。For the only irrationality implication, Theorem 7.2 additionally requires the unproved nonvanishing of every constructed delta B_i-A_i; Theorems 4.1 and 7.1 merely give denominator growth/convergence. Do not transfer delta statements to gamma or suppress this nonvanishing condition. held-adjacent-conditional

### 46 · Series and Product Representations of Gamma, Pseudogamma and Inverse Gamma Functions

- 版本与身份。Formal primary version checked at Maple Transactions: published 2025-02-23 (the local PDF also carries arXiv:2301.09699v4, 2025-03-13). SHA-256 为 `d8ba69ea1fed0411461239e7902cf52941e3427245a3890d8ea4b9c63d5a51b3`。
- 本机原文定位。Local PDF pp.1-2,3-5,9: abstract; Theorems 2.1-2.2 and 2.6; Corollary 2.7; Conjecture 3.1. Formal article: Maple Transactions 5(1) (2025), Article 16090, DOI 10.5206/mt.v5i1.16090.
- 核对范围。The formally proved Newton-series identities include 1/Gamma(x+1) for x&gt;0 (Theorem 2.1) and the Gamma Newton series for real x&gt;=1 (Theorem 2.6); Corollary 2.7 gives a rational-term series for Euler's constant. The inverse-Gamma Newton series is explicitly Conjecture 3.1. None of the identities is an irrationality proof for gamma.
- 依赖与状态。Use only the stated convergence domains and the Laguerre/Newton interpolation bounds. Do not invoke the inverse-Gamma proposal as a theorem, and do not infer arithmetic information about the sum of the rational gamma series without a separately proved denominator/error certificate. candidate-computational-identity

### 50 · The Digamma function, Euler-Lehmer constants and their p-adic counterparts

- 版本与身份。Primary record checked: local file is arXiv:1308.6451v1. No formal-journal version was established in this audit. SHA-256 为 `0ed3930e598ff000ddd1411453973c6f9dfef851b90db4a94f3bba63ecf4c177`。
- 本机原文定位。Local arXiv PDF pp.1-4: abstract; Theorems 1.1-1.8 and definitions. arXiv:1308.6451v1 (2013-08-29).
- 核对范围。Theorem 1.2 says at most one member of the indicated infinite archimedean set {gamma} union {psi(r/n)} is algebraic; this does not decide whether gamma itself is algebraic. Theorems 1.3-1.8 concern p-adic Euler-Lehmer constants and p-adic digamma values in C_p, including distinctness and 'at most one algebraic' assertions, so they are not archimedean gamma irrationality results.
- 依赖与状态。Keep the domains separate: the classical digamma identity is archimedean, whereas the p-adic function uses log_p, a fixed embedding into C_p, and its own Euler-Lehmer constants. Selected results rely on the cited Murty-Saradha inputs; no cross-domain transfer is justified. guardrail-archimedean-padic

### 52 · The generalized-Euler-constant function γ(z) and a generalization of Somos's quadratic recurrence constant

- 版本与身份。Local PDF identifies arXiv:math/0610499v1 (2006-10-16); primary published version: J. Sondow and P. Hadjicostas, Journal of Mathematical Analysis and Applications 332(1) (2007), 292–314, DOI 10.1016/j.jmaa.2006.10.064. SHA-256 为 `bfb366f2eb7595081072b9a8c43804794e162bc92faa75d9ad2af1e67a8b340d`。
- 本机原文定位。07:EXT-0286 / 08:G19; local PDF pp. 1–5, Theorem 1; pp. 18–25, Theorems 13 and 16
- 核对范围。Defines γ(z)=Σ_{n≥1}z^{n−1}(1/n−log((n+1)/n)) for \|z\|≤1, with γ(1)=γ and γ(−1)=log(4/π). Theorem 1 gives polylogarithm series; Theorem 13/root-of-unity formulas and Theorem 16 derivative formulas are exact identities. They do not establish irrationality of γ or of the displayed special values.
- 依赖与状态。Proofs use absolutely convergent rearrangements and analytic continuation via the Lerch transcendent; root-of-unity evaluations use the Weierstrass product for Γ, and derivative evaluations use the Kinkelin–Bendersky hyperfactorial/Barnes G machinery. candidate — exact generalized-Euler-constant/roots-of-unity identity toolkit only; preserve the γ(z), base, and Γ/Barnes scope and do not promote it to an irrationality result.

### 53 · Transcendence of generalized Euler-Kronecker constants

- 版本与身份。Local source is arXiv:2402.13138 (8 pp); primary version verified as N. Kandhil and R. Lunia, Bulletin of the Australian Mathematical Society 109(3) (2024), 464–470, DOI 10.1017/S0004972723000631 (online 2023-07-10). SHA-256 为 `ab88b3f19e96e87f0ae83c2266fbf137dd2b838076cf43ec3c122fcbaba41e86`。
- 本机原文定位。08:G55; local PDF pp. 1–7, especially Theorem 1.2 and Lemmas 2.3, 3.2–3.3
- 核对范围。For a fixed number field K and prime-ideal subsets Ω_i satisfying the stated summability and finite asymmetric-difference hypotheses, Theorem 1.2 proves that at most one γ_K(Ω_i)/δ_K(Ω_i) is algebraic. The K=Q specialization is a family statement; it neither proves γ irrational nor applies to arbitrary generalized-Euler data without its hypotheses.
- 依赖与状态。The local proof chain is explicit: ideal-counting/partial summation gives Lemma 2.2; finite/infinite Ω formulae give Lemma 3.2/Corollary 3.3; subtracting two alleged algebraic values reduces to logarithms of rationals and invokes Lindemann's theorem plus unique factorisation. candidate — narrowly use the Euler–Kronecker family separation theorem with all Ω/K hypotheses recorded; no direct Euler-constant irrationality claim.

### 54 · Transcendental values of the digamma function

- 版本与身份。Primary version verified: M. Ram Murty and N. Saradha, Journal of Number Theory 125(2) (2007), 298–318, DOI 10.1016/j.jnt.2006.09.017; local PDF is the publisher-formatted article. SHA-256 为 `648488550f5b1d82037741593d1287bbfac0d3fb4e1cb85193b6e22b753d46eb`。
- 本机原文定位。04:P28 / 08:G28; local PDF pp. 1–5, Theorems 1, 3, 4, 8–10
- 核对范围。For q&gt;1, Theorem 1 proves ψ(a/q)+γ transcendental (1≤a&lt;q); Theorem 3 says at most one among γ and ψ(a/q) for reduced residues is algebraic; Theorem 8 gives the analogous at-most-one assertion for Euler–Lehmer γ(a,q). It does not decide γ itself.
- 依赖与状态。Gauss's rational-argument digamma formula and the Hurwitz zeta functional equation reduce the values to logarithms; Baker linear forms in logarithms and cyclotomic linear-independence/non-vanishing inputs supply the transcendence statements. candidate — classical rational-argument digamma/Euler–Lehmer tool with q&gt;1 and reduced-residue conditions; retain the at-most-one qualifier for γ.

### 55 · Transcendental values of the p-adic digamma function

- 版本与身份。Primary version verified: M. Ram Murty and N. Saradha, Acta Arithmetica 133.4 (2008), 349–362, DOI 10.4064/aa133-4-4; local PDF is the journal article. SHA-256 为 `9a1456601d7d6e300be7f937a3f5f73c1b5b0208814a4f9696fdb8302a76da69`。
- 本机原文定位。04:P32; local PDF pp. 1–4, Theorems 1–2; pp. 10–12, their proofs
- 核对范围。For Diamond's p-adic constants, Theorem 1 (prime q) gives at most one algebraic member of {γ_p,γ_p(r,q)}. Theorem 2 gives transcendence of ψ_p(r/p)+γ_p when q=p, and of p^N/(p^N−1)H'_N(r/q)+γ_p when q≠p with p^N≡1 mod q. It is not a theorem about classical γ or Morita's Γ_p without the stated identification.
- 依赖与状态。Uses Diamond's p-adic log-gamma/digamma setup, p-adic Hurwitz zeta/L-functions and Okada non-vanishing, cyclotomic-unit multiplicative independence, and Kaufman's p-adic linear-forms-in-logarithms result. candidate — p-adic-only module; keep prime/modulus, Diamond-function, and logarithm-normalization hypotheses explicit.

### 57 · Continued Fractions and Irrationality Measures for Chowla–Selberg Gamma Quotients

- 版本与身份。Local PDF metadata: arXiv:2510.00215v5, dated 2026-09-29. Author publication list describes an Algebra & Number Theory version as ‘to appear’; no journal VoR treated as verified here. SHA-256 为 `c2746cbbdb3c30b9c44741fe728573b42ad56ad16cba150020421ebb944928fc`。
- 本机原文定位。08:P39-02; local PDF pp. 1–3, 16–19, 20–25; actual PDF heading and arXiv metadata
- 核对范围。This is not the bundled P39 title. It defines CS(D) and proves explicit irrationality-measure bounds for 20 listed Chowla–Selberg gamma quotients/algebraic multiples; e.g. Theorem 6.2 gives μ(CS(−3))&lt;5.548, μ(CS(−7))&lt;5.282, and qualifying bounds for other CS(D). It does not concern Euler's γ, arbitrary Γ values, or p-adic quotients.
- 依赖与状态。Preprint proof chain inspected: hypergeometric/CM evaluations and continued fractions (Sections 4–6) supply rational approximants; Lemma 1.2 turns decay plus denominators into measures; Theorem 7.3 gives denominator control and Proposition 7.7 uses prime-distribution asymptotics. Theorem 6.2 depends on this whole chain, not just numerical CF recognition. candidate — preprint theorem may be used only for the named CS(D) quotients and its stated irrationality-measure bounds after retaining its complete denominator/CM hypotheses; title corrected from the mixed P39 bundle.

### 58 · Variations on a theme of Apéry

- 版本与身份。Local PDF metadata: arXiv:2501.10090v3, dated 2025-11-03. No primary journal version was verified; handle as a preprint. SHA-256 为 `e0901974899d5586080816194e8bccfa7b473aa4497eab44e3ab7e710bc93808`。
- 本机原文定位。08:P39-01; local PDF pp. 1–4 (especially Theorem 2.1 and its warning), pp. 5–16
- 核对范围。This is the other P39 PDF, not a Chowla–Selberg irrationality-measure paper. It produces elegant rapidly convergent continued fractions, including a CF for (Γ(1/4)/Γ(3/4))^4 in Theorem 2.1 and period/quasiperiod quotients. The authors explicitly state that it gives no new irrationality results; for the displayed γ quotient the common denominators are too large for such a conclusion.
- 依赖与状态。Actual preprint derivations use Apéry acceleration/continued-fraction transformations, Ramanujan gamma-quotient CFs, Euler–Beukers integrals with creative telescoping, and Chowla–Selberg/modular period evaluations; the relevant obstruction is the denominator growth explained on local PDF p. 4. held — retain as a continued-fraction discovery/recurrence source, but prohibit use as an irrationality proof or as evidence about Euler's γ; title corrected from the mixed P39 bundle.


## 算术 Gevrey、特殊函数与指数动机

### 17 · Euler’s constant and exponential motives

- 版本与身份。Javier Fresán lecture slides (Pisa/Regulation V, dated 2024-06-03 in the hosted copy); non-refereed talk material, no formal publication verified. SHA-256 为 `27c9bff0c49ce226b1fa34fdaa532453b18f6ed57c0dbb8501b4cc372ddd8b0b`。
- 本机原文定位。local scanned 8-page lecture slides, pp. 1–8; no numbered proposition/proof recoverable from this scan
- 核对范围。Expository lecture connecting γ to an exponential-motive extension and period conjectures; the slide deck is not a formal-paper proof source.
- 依赖与状态。The slides state they are based on joint work with Peter Jossen; the substantive construction/proofs are in the separate local Exponential motives preprint (SHA 7da885c162606b3c7a2b377d532e59097e51a6856c7f9ba75071d559d2e5ebf5), §12.8. / No standalone proof pages or independently auditable theorem are present in this scanned talk file. blocker: use only as a pointer to the Fresán–Jossen preprint; do not distill it as a proof-bearing skill source.

### 19 · Exponential Motives（及专论 Euler's constant and exponential motives）

- 版本与身份。Javier Fresán and Peter Jossen, Exponential motives, authors' 2024 preprint (local PDF created 2024-04-11); no peer-reviewed publication version verified. SHA-256 为 `7da885c162606b3c7a2b377d532e59097e51a6856c7f9ba75071d559d2e5ebf5`。
- 本机原文定位。local 2024 preprint pp. 277–284 (§12.8): integral (12.8.0.1), Definition 12.8.2, period matrix §12.8.5, Proposition 12.8.7, Corollaries 12.8.8, 12.8.12
- 核对范围。Constructs an exponential motive M(γ), a nontrivial extension 0→Q(0)→M(γ)→Q(−1)→0, whose displayed period matrix contains γ. The algebraic-independence/transcendence conclusions in Corollaries 12.8.8/12.8.12 are conditional on the exponential period conjecture.
- 依赖与状态。The construction depends on the preceding development of the exponential-motive category and comparison isomorphism (Chs. 2–8), plus rapid-decay/de Rham computations in §12.8. / The γ integral identity is attributed to Belkale–Brosnan in §12.8; Proposition 12.8.7 has a local proof, whereas corollaries explicitly assume Conjecture 8.2.6. held: rigorous conditional motivic framework, not an unconditional irrationality/transcendence method; preserve the period-conjecture premise.

### 23 · Is Euler's constant a value of an arithmetic special function?

- 版本与身份。Local cover: HAL hal-01619235v2, submitted 20 Dec 2017. Author bibliography classifies it as “survol (2017), 10 pages”/unpublished note; no journal publication verified. SHA-256 为 `acd3276a65159df6792b07f048900a0bdaa9a7ac9fcef270d909cdba9e0808bd`。
- 本机原文定位。07:EXT-0606; local pp. 1–4, 10–11; https://hal.science/hal-01619235v2; https://rivoal.perso.math.cnrs.fr/articles/cteuler.pdf
- 核对范围。Actual local abstract and discussion explicitly say that no representation proves gamma is an E-, G-, or M-function value at an algebraic point; the note argues this is plausibly impossible and supplies representation/series context. It is a 10-page survey note, not a proof of irrationality or transcendence.
- 依赖与状态。Siegel–Shidlovsky, Chudnovsky and Nishioka results are discussed but not applicable to gamma / known Vacca-type identities and cited E/G/M-function arithmetic theory held — route only as a status/obstruction source; do not infer arithmetic properties of gamma from its representations.

### 45 · Relations between values of arithmetic Gevrey series, and applications to values of the Gamma function

- 版本与身份。Primary record checked: local file is arXiv:2301.13518v1. No formal-journal version was established in this audit. SHA-256 为 `0f08c970d28d4fcfc7b26b64c0f55ccc6d6f05241ecaaaaab3c8693fc7a16140`。
- 本机原文定位。Local arXiv PDF pp.1-4: abstract; Theorems 1-3 and Corollary 1. arXiv:2301.13518v1 (2023-01-31).
- 核对范围。Unconditionally, Theorem 1 relates the value rings G, E, D for arithmetic Gevrey orders 0,-1,1. The statements on Gamma derivatives at nonintegral algebraic points, Gompertz delta, and Euler gamma not lying in E are conditional: Theorem 2 assumes E cap D=Q, while Theorem 3/Corollary 1 assume Conjecture 2. This paper does not prove irrationality of Euler's constant gamma.
- 依赖与状态。Preserve three distinct Gevrey regimes: E-functions (order -1), analytic continuations of G-functions (0), and divergent E-functions/renormalized values D (1), with a specified non-anti-Stokes summation direction. Selected arithmetic conclusions require exactly the stated conjecture(s), so no conditional consequence may enter an unconditional gamma skill. conditional-framework

### 48 · Séries Gevrey de type arithmétique, II. Transcendance sans transcendance

- 版本与身份。Formal primary version checked: Ann. of Math. 151 (2000), 741-756; local file is arXiv:math/0003239v1. SHA-256 为 `676b0f33a59c84107bf0607fcfc22b1b7b019f346880207cf19de5ede75a6fe8`。
- 本机原文定位。Local arXiv PDF pp.1-4: introduction; Theorem 2.1.1 and Lemma 2.1.2. Formal article: Annals of Mathematics 151 (2000), 741-756; arXiv:math/0003239v1.
- 核对范围。Part II studies values of holonomic arithmetic Gevrey series of nonzero order. Theorem 2.1.1 applies to an order s&lt;0 series with algebraic/denominator growth and a minimal annihilator, under vanishing at an algebraic point at every infinite place; it yields a local solution basis. Its Lindemann-Weierstrass and E-function consequences are structural results, not a result on Euler's constant gamma.
- 依赖与状态。Its proofs explicitly build on Part I's singularity/purity theorems and distinguish arithmetic Gevrey orders below zero from positive-order divergent series, including p-adic summability phenomena. Do not identify formal p-adic equalities such as sum n n!=-1 with an archimedean gamma statement. foundational-framework

### 49 · Séries Gevrey de type arithmétique, I. Théorèmes de pureté et de dualité

- 版本与身份。Formal primary version checked: Ann. of Math. 151 (2000), 705-740; local file is arXiv:math/0003238v1. SHA-256 为 `6f2b59f64f44cf46904d9013a505ab57160695975ca96b797560f606854a9ef4`。
- 本机原文定位。Local arXiv PDF pp.1-4: introduction, purity and duality theorems. Formal article: Annals of Mathematics 151 (2000), 705-740; arXiv:math/0003238v1.
- 核对范围。Part I defines arithmetic and Nilsson-Gevrey series and proves purity/duality for a minimal polynomial-coefficient differential operator. For s not equal to 0 it controls nontrivial singularities and exchanges order s at 0 with -s at infinity; for s=0 it is the G-function/Fuchsian regime. These are conditional-on-hypotheses structural tools, not a gamma irrationality theorem.
- 依赖与状态。Application requires a verified holonomic arithmetic (Nilsson-)Gevrey representation, minimal annihilator, correct sign/order s, and the specified sector/Stokes qualification in the duality statement. The use of p-adic analysis for the s=0/G-operator portion cannot be silently replaced by an archimedean statement. foundational-framework
