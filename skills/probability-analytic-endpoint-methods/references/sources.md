# W25 source guide: 30 mother-approved papers

R01’s mother-source binding approved the exact 30 works below (686 physical pages, all full-text read). This is an independent source-binding decision, not a blanket proof audit. The AEP-020 corrigendum adds two read physical pages to that same work and is not a separate source. Final skill-scope review/release remains pending.

Every entry links to a portable card containing theorem numbers, physical and printed page anchors, proof dependencies, coverage, and preserved limitations. Local PDF paths and SHA-256 values are in evidence/W25/sources.json; full page/section coverage is in evidence/W25/reading_coverage.json.

## CZ-03 — On the dimensional weak-type (1,1) bound for Riesz transforms

Daniel Spector, Cody B. Stockdale (2020). DOI: [10.48550/arXiv.2004.03382](https://doi.org/10.48550/arXiv.2004.03382). Full-text version: arXiv v2 (R03 freeze); the seed’s v1 date was superseded by explicit version binding; 17 physical pages.

Theorem 4.1 reduces a scalar weak-(1,1) problem to a regular term and finite positive atoms under the paper’s odd homogeneous mean-zero kernel and angular continuity assumptions. Its printed p. 11 good-part and finite-sum estimates omit the squared angular/L2 factor; for a general kernel, use the reduction only with an independently certified L2 norm or completed norm argument. For a fixed Riesz coordinate, the angular mass is 2/π and the finite-atom term is O(log n), not dimension-free.
Card: [evidence/W25/cards/CZ-03.md](../evidence/W25/cards/CZ-03.md).

## CZ-04 — A dimension-free weak-type (1,1) bound for the vector Riesz transform on R^n

Yuyuan Ouyang, Daniel Spector, Cody B. Stockdale (2026). DOI: [10.48550/arXiv.2608.18068](https://doi.org/10.48550/arXiv.2608.18068). Full-text version: arXiv v1; 12 physical pages.

The fractional obstacle decomposition applies to real f in L1∩L2, λ>0 and 0<α<2; at α=1 the source obtains a vector Euclidean weak-(1,1) upper bound 2. Its proof uses positive/negative parts and certifies the real case. The constant is not claimed optimal and is not a sharp vector strong-Lp constant.
Card: [evidence/W25/cards/CZ-04.md](../evidence/W25/cards/CZ-04.md).

## CZ-05 — On the sharp weak-type inequality for Riesz transforms

Rodrigo Bañuelos, Mähdi Hormozi, Alexander Volberg (2026). DOI: [10.48550/arXiv.2611.11788](https://doi.org/10.48550/arXiv.2611.11788). Full-text version: arXiv v1; 37 physical pages.

The v1 preprint claims the sharp real-input scalar-coordinate Euclidean weak-(1,1) constant K_D. The product extension has a horizontal derivative only and requires a nonzero standard σ-finite transverse space, a nonnegative self-adjoint generator, and a symmetric sub-Markov semigroup. Treat the asserted theorem/sharpness as source claims pending independent proof review; it gives no sharp vector constant.
Card: [evidence/W25/cards/CZ-05.md](../evidence/W25/cards/CZ-05.md).

## AEP-006 — A theorem on weak type estimates for Riesz transforms and martingale transforms

Nicolas Th. Varopoulos (1981). DOI: [10.5802/aif.826](https://doi.org/10.5802/aif.826). Full-text version: published journal version; Numdam PDF has 9 physical pages including archive cover; 9 physical pages.

For a finite bounded Radon measure μ=f dx+ν, the main Riesz-vector tail is a liminf as λ→∞ bounded below by k_n||ν||, with positive dimension-dependent k_n unspecified. The separate all-threshold comparison assumes positive singular ν and uses Σ_j|R_jν|, not the Euclidean vector norm. Martingale UI criteria require the source’s bounded relatively-orthonormal finite-increment system, L1-bounded martingale and no-common-real-eigenvector condition; maximal-transform criterion is only sufficient and needs Σ_j P_jM_j=I.
Card: [evidence/W25/cards/AEP-006.md](../evidence/W25/cards/AEP-006.md).

## AEP-007 — Sharp weak type estimates for Riesz transforms

Adam Osękowski (2014). DOI: [10.1007/s00605-014-0613-7](https://doi.org/10.1007/s00605-014-0613-7). Full-text version: published open-access journal version; 23 physical pages.

For real scalar input and one Euclidean Riesz coordinate, Theorem 1.1 gives sharp positive-part weak-Lp constant C_p^+ and full absolute-value upper bound 2C_p^+, only for 1<p<∞ and the paper’s sup_r r^(1/p)f**(r) Lorentz quantity. The martingale proof needs Jensen on random X0; do not use its printed pointwise equality. The lower-endpoint line on printed p. 317 (physical p. 13) has m↓0, not m→∞. No p=1 operator constant or sharp vector estimate; sphere sharpness is only asserted in dimension 2.
Card: [evidence/W25/cards/AEP-007.md](../evidence/W25/cards/AEP-007.md).

## AEP-009 — A different approach to endpoint weak-type estimates for Calderón-Zygmund operators

Cody B. Stockdale (2020). DOI: [10.1016/j.jmaa.2020.124016](https://doi.org/10.1016/j.jmaa.2020.124016). Full-text version: arXiv:1812.11392v4 (27 April 2020), complete 12-page author preprint; same work as JMAA 487 (2020), Article 124016, not publisher layout.; 12 physical pages.

Theorem 1 is scalar-output Euclidean weak-(1,1) under standard kernel size and two-variable Hölder smoothness, L2 boundedness, and off-support integral representation; the constant depends on T and dimension and is not sharp. Keep Theorem 2’s weighted Ap statement separate: its p. 5 arbitrary-set affine-dilation step is not implied by doubling and remains quarantined pending an independent weighted estimate.
Card: [evidence/W25/cards/AEP-009.md](../evidence/W25/cards/AEP-009.md).

## AEP-016 — Sharp martingale inequalities and applications to Riesz transforms on manifolds, Lie groups and Gauss space

Rodrigo Bañuelos, Adam Osękowski (2015). DOI: [10.1016/j.jfa.2015.06.015](https://doi.org/10.1016/j.jfa.2015.06.015). Full-text version: Complete author-hosted manuscript on Purdue author site, dated 20 June 2015, 48 physical pages; journal version is JFA 269(6), 1652–1713, and has different pagination.; 48 physical pages.

The matrix differential-subordination estimates need the source’s adapted continuous symmetric nonpositive matrix drift; geometry-specific applications retain their manifold/group/sphere/Gauss hypotheses. For vector log formulas with a 1/(K−1) remainder use K>1 although Theorems 3.3/3.7/3.9 print K>2/π; scalar directional L(K) retains K>2/π. The p<2 event route depends on the separately attributed global-minimum supplement accepted by R01, not the printed Lemma 2.7 proof. No p=1 operator theorem.
Card: [evidence/W25/cards/AEP-016.md](../evidence/W25/cards/AEP-016.md).

## AEP-017 — Multiplier theorems via martingale transforms

Rodrigo Bañuelos, Fabrice Baudoin, Li Chen, Yannick Sire (2021). DOI: [10.1016/j.jfa.2021.109188](https://doi.org/10.1016/j.jfa.2021.109188). Full-text version: arXiv:2003.02077v2 (9 July 2021), complete 28-page preprint; same work as JFA 281 (2021), Article 109188, not publisher layout. PDF front matter gives author Yannick Sire.; 28 physical pages.

Use its stopped-extension/Green-kernel/spectral-calculus/conditional-expectation representation only under the diffusion, vertical-process, potential, geometric and bundle assumptions in the card. The resulting operator estimates are strong-Lp for 1<p<∞, not weak-(1,1). Generic linear-C Theorem 4.11 and all-index second-order diagonal use remain quarantined; first-order and distinct-index/separately certified matrix-norm scopes stay separate.
Card: [evidence/W25/cards/AEP-017.md](../evidence/W25/cards/AEP-017.md).

## AEP-018 — Bellman function and linear dimension-free estimates in a theorem of Bakry

Andrea Carbonaro, Oliver Dragičević (2013). DOI: [10.1016/j.jfa.2013.05.031](https://doi.org/10.1016/j.jfa.2013.05.031). Full-text version: arXiv:1105.6330v3 (15 June 2013), complete 16-page author preprint; same work as JFA 265(7) (2013), 1085–1104, but not publisher-layout bytes.; 16 physical pages.

The Bellman/Bochner method gives bilinear constant 3(p*−1) and nonsharp dimension-free vector Riesz upper bound 12(p*−1) on the specified weighted complete manifold with Ricφ≥−a²g and source closure/domain conditions. The proof is real-valued; use the stated complex-data qualification. This is strong-Lp only and does not identify C207’s best vector constant.
Card: [evidence/W25/cards/AEP-018.md](../evidence/W25/cards/AEP-018.md).

## AEP-019 — Transformation de Riesz pour les semi-groupes symétriques. Première partie : étude de la dimension 1

Dominique Bakry (1985). [Source record](https://www.numdam.org/item/SPS_1985__19__130_0/). Full-text version: Official Numdam scan of the complete published standalone contribution, printed pp. 130–144; 16 physical pages including archive/title leaf. Not the entire LNM volume.; 16 physical pages.

This is a complete standalone one-dimensional Jacobi contribution, not the whole LNM volume. The semigroup comparison uses α,β≥0 and the source’s mean-zero polynomial/core setup; the H1→L1 conclusion uses its source Hardy space. It is not Lebesgue weak-(1,1), a Euclidean vector Riesz theorem, or a multidimensional duality argument.
Card: [evidence/W25/cards/AEP-019.md](../evidence/W25/cards/AEP-019.md).

## AEP-020 — Transformation de Riesz pour les semi-groupes symétriques. Seconde partie : étude sous la condition Γ2 ≥ 0

Dominique Bakry (1985). [Source record](https://www.numdam.org/item/SPS_1985__19__145_0/). Full-text version: Official Numdam scan of the complete published standalone contribution, printed pp. 145–174; 31 physical pages including archive/title leaf. Not the entire LNM volume. Official Numdam 1986 correction at volume 20, printed p. 614 was read as a same-work supplement; it corrects one matrix entry in the proof of Proposition 1, with no change to theorem hypotheses/statements/constants. The correction and R01 independent Hessian expansion establish the corrected entry with leading factor 2; see the mirrored supplement and coverage.; 31 physical pages.

The corrected source gives the diffusion-only C≤c_p√Γ direction and, for a general symmetric semigroup, √Γ≤c_p C only for p>2 on the source good core. The all-p equivalence needs the additional §4.3 common-h/commutation structure. The official correction replaces the Proposition 1 proof entry by (f,f)(f,g), retaining leading 2; R01’s M34=2Γ(f,f)Γ(f,g) residual-zero computation is local algebra only. The 2-page correction is same-work support, not a 31st source.
Card: [evidence/W25/cards/AEP-020.md](../evidence/W25/cards/AEP-020.md).

## AEP-021 — Martingales and sharp bounds for Fourier multipliers

Rodrigo Bañuelos, Adam Osękowski (2012). DOI: [10.5186/aasfm.2012.3710](https://doi.org/10.5186/aasfm.2012.3710). Full-text version: Complete arXiv:1111.7212v1 author preprint, submitted 30 Nov 2011; same work as Ann. Acad. Sci. Fenn. Math. 37(1) (2012), 251–263; not publisher-layout PDF.; 11 physical pages.

Use the sharp p>1 martingale differential-subordination and second-order Riesz-combination results only in the source’s smooth homogeneous model. The product-cone condition is part of its theorem; the proof does not authorize arbitrary axis-value representative extensions. It gives no weak-(1,1) theorem or first-order vector best constant.
Card: [evidence/W25/cards/AEP-021.md](../evidence/W25/cards/AEP-021.md).

## AEP-023 — Riesz transform on manifolds and heat kernel regularity

Pascal Auscher, Thierry Coulhon, Xuan Thinh Duong, Steve Hofmann (2004). DOI: [10.1016/j.ansens.2004.10.003](https://doi.org/10.1016/j.ansens.2004.10.003). Full-text version: arXiv:math/0411374v1, submitted 17 Nov 2004; published citation Ann. Sci. Éc. Norm. Supér. 37(6) (2004), 911–957.; 47 physical pages.

The manifold good-λ criterion needs its estimates for every f, every base point and every ball, plus the separate condition Tf∈Lp whenever f∈Lp. Its Riesz application additionally needs uniform truncation bounds and an L2 limit; the strong-type range is 2<p<p0. It is not a scalar Euclidean weak-(1,1) result.
Card: [evidence/W25/cards/AEP-023.md](../evidence/W25/cards/AEP-023.md).

## AEP-024 — Maximal inequalities and Riesz transform estimates on Lp spaces for Schrödinger operators with nonnegative potentials

Pascal Auscher, Besma Ben Ali (2007). DOI: [10.5802/aif.2320](https://doi.org/10.5802/aif.2320). Full-text version: Published official Numdam journal PDF, AIF 57(6) (2007), printed pages 1975–2013; includes one archive cover page.; 40 physical pages.

The distribution estimate maps f∈C0∞ to H^(1/2)f and controls it by ||∇f||1+||V^(1/2)f||1 for nonnegative V∈A∞. It is not an arbitrary-L1 input estimate or a Riesz-transform weak-(1,1) theorem. The author is Besma Ben Ali.
Card: [evidence/W25/cards/AEP-024.md](../evidence/W25/cards/AEP-024.md).

## AEP-041 — A simple proof of the A2 conjecture

Andrei K. Lerner (2013). DOI: [10.1093/imrn/rns145](https://doi.org/10.1093/imrn/rns145). Full-text version: Author-hosted copy of published IMRN 2013(14), 3159–3170; advance-access date 2 Jun 2012.; 12 physical pages.

The local-oscillation sparse route assumes the classical Euclidean CZ/L2 setting and the weak-(1,1) input used in Proposition 2.3. The paper prints ε<|y|<ν for K(x,y); this origin-centered notation is quarantined, and reuse requires the separately justified centered truncation ε<|x−y|<ν. The c(n)m complexity bound is for m≥1; m=0 is the direct sparse-average term. Output is weighted strong-L2, not a new endpoint theorem.
Card: [evidence/W25/cards/AEP-041.md](../evidence/W25/cards/AEP-041.md).

## AEP-044 — An elementary proof of the A2 bound

Michael T. Lacey (2017). DOI: [10.1007/s11856-017-1442-x](https://doi.org/10.1007/s11856-017-1442-x). Full-text version: Complete arXiv:1501.05818v7 author preprint, dated 12 Oct 2015, 12 physical pages; same work as Israel J. Math. 217(1) (2017), 181–195; not publisher-layout PDF.; 12 physical pages.

The martingale/Dini-CZO sparse route needs its explicit weak-L1 truncation input and Dini/kernel hypotheses. Keep the theorem’s literal minimum exponent: the separate R08 legal witness at p=3 contradicts that source-local displayed claim; it does not refute the paper wholesale or certify a maximum-exponent repair.
Card: [evidence/W25/cards/AEP-044.md](../evidence/W25/cards/AEP-044.md).

## AEP-045 — Sharp inequalities for the Haar system and martingale transforms

Adam Osękowski (2016). [Source record](https://www.math.uni.wroc.pl/~pms/publicationsArticle.php?nr=36.1&nrA=11&ppB=147&ppE=164). Full-text version: Official journal-hosted complete PDF, Probability and Mathematical Statistics 36(1) (2016), pp. 147–164, 18 physical pages.; 18 physical pages.

The source proves real scalar Haar/martingale positive-contraction estimates with fixed initial coefficient 1 and a one-sided event. Preserve that event and normalization. No Riesz representation, vector estimate, or direct C207 best-constant conclusion follows.
Card: [evidence/W25/cards/AEP-045.md](../evidence/W25/cards/AEP-045.md).

## AEP-EXT-003 — Endpoint multiplier theorems of Marcinkiewicz type

Terence Tao, James Wright (2001). DOI: [10.4171/RMI/303](https://doi.org/10.4171/RMI/303). Full-text version: Published Revista Matemática Iberoamericana 17(3) (2001), 521–558; official EMS Press PDF, 38 physical pages.; 38 physical pages.

The multiplier and interval-overlap results are one-dimensional. Proposition 5.1 requires supp(m_I)⊂I, ξ_I∈I, and common order-zero seminorm and pointwise-domination constants; its local Orlicz mapping takes input supported on compact K and restricts output to that same K with C_K. No Euclidean scalar-Riesz reduction or dimension-free conclusion is supplied.
Card: [evidence/W25/cards/AEP-EXT-003.md](../evidence/W25/cards/AEP-EXT-003.md).

## AEP-EXT-005 — A proof of the weak (1,1) inequality for singular integrals with non doubling measures based on a Calderón-Zygmund decomposition

Xavier Tolsa (2001). DOI: [10.5565/PUBLMAT_45101_07](https://doi.org/10.5565/PUBLMAT_45101_07). Full-text version: Complete author preprint arXiv:math/0002221v1 (submitted 25 Feb 2000), 10 physical pages; published counterpart Publicacions Matemàtiques 45(1) (2001), 163–174, DOI 10.5565/PUBLMAT_45101_07. Acquired version is the preprint, not publisher layout.; 10 physical pages.

The non-doubling weak-(1,1) decomposition assumes polynomial growth, the stated kernel regularity and uniformly L2-bounded truncations. Keep β>α^n for large-cube existence and β>α^d for small a.e. doubling cubes distinct. An unbounded Ω is not covered by a global finite-family cover; use the source’s localized limit or a countable annular finite-overlap repair. Constants are not claimed dimension-free.
Card: [evidence/W25/cards/AEP-EXT-005.md](../evidence/W25/cards/AEP-EXT-005.md).

## AEP-EXT-015 — Borderline Weak Type Estimates for Singular Integrals and Square Functions

Carlos Domingo-Salazar, Michael Lacey, Guillermo Rey (2016). DOI: [10.1112/blms/bdv090](https://doi.org/10.1112/blms/bdv090). Full-text version: Complete author preprint arXiv:1505.01804v2 [math.CA], dated 26 May 2015, 13 physical pages; published Bull. Lond. Math. Soc. 48(1) (2016), 63–73. The acquired file is v2, not publisher layout.; 13 physical pages.

The normalized Dini maximal-truncation Theorem 1.6 needs its Young-function summability condition. The intrinsic-square Theorem 1.11 includes p=1,w∈A1, but its p<2 proof is imported. Preserve the p. 4 cone/dilation, p. 5 Dini-monotonicity, and p. 6 reverse-Hölder exponent defects; any conventional definition or reciprocal-order reverse-Hölder step is an external conditional input, not a source correction.
Card: [evidence/W25/cards/AEP-EXT-015.md](../evidence/W25/cards/AEP-EXT-015.md).

## AEP-EXT-009 — A Weak-Type Inequality for Orthogonal Submartingales and Subharmonic Functions

Adam Osękowski (2011). DOI: [10.4064/ba59-3-7](https://doi.org/10.4064/ba59-3-7). Full-text version: Published journal version, Bulletin of the Polish Academy of Sciences: Mathematics 59(3) (2011), article printed pages 261–274; official IMPAN-hosted PDF.; 14 physical pages.

For a submartingale X with X0=0 and an orthogonal, strongly differentially subordinate semimartingale Y, Theorem 1.2 gives P(Y*≥1)≤c sup_t E|X_t|. Its smooth-function Theorem 4.1 has separate C2, subharmonicity, orthogonality, gradient/Laplacian domination and harmonic-measure assumptions. The printed (3.2) sign and sharpness exit domain are defective; the int(J−1) exit and two-budget selector are separately attributed reader derivations. The source itself leaves smooth-function sharpness open; neither result proves C208.
Card: [evidence/W25/cards/AEP-EXT-009.md](../evidence/W25/cards/AEP-EXT-009.md).

## AEP-EXT-010 — Maximal Weak-Type Inequality for Orthogonal Harmonic Functions and Martingales

Adam Osękowski (2013). DOI: [10.4064/ba61-3-3](https://doi.org/10.4064/ba61-3-3). Full-text version: Published journal version, Bulletin of the Polish Academy of Sciences: Mathematics 61(3–4) (2013), article printed pages 209–218; official IMPAN-hosted PDF.; 10 physical pages.

The maximal martingale theorem requires continuous real martingales starting at zero with orthogonality and differential subordination; the harmonic formulation keeps its open connected domain, base point, gradient constraints and harmonic measure. Distinguish the maximal path event from the nonmaximal harmonic-measure norm. The source prints a closed strip despite its open-domain hypothesis; a separately attributed open-strip example uses boundary limits. This is not a Euclidean Riesz theorem.
Card: [evidence/W25/cards/AEP-EXT-010.md](../evidence/W25/cards/AEP-EXT-010.md).

## AEP-EXT-001 — The Hilbert transform and rearrangement of functions

R. O’Neil, G. Weiss (1963). DOI: [10.4064/sm-23-2-189-198](https://doi.org/10.4064/sm-23-2-189-198). Full-text version: Official full text, printed pages 189–198; 6 physical PDF pages.; 6 physical pages.

Use the rearrangement formulas in their stated one-dimensional Hilbert/conjugate or odd homogeneous-kernel classes. Theorem 3 has full ||Ω|| after combining sign pieces although its indicator lemma has ||Ω||/2; Theorem 4 uses sin(s/4). Theorem 2’s displayed Ap already incorporates the printed rearrangement step; do not multiply by an additional p′ Hardy factor. Strong-Lp or distribution results do not themselves establish a general scalar weak-(1,1) Riesz theorem.
Card: [evidence/W25/cards/AEP-EXT-001.md](../evidence/W25/cards/AEP-EXT-001.md).

## AEP-EXT-014 — Calderón-Zygmund Decomposition, Hardy Spaces Associated with Operators and Weak Type Estimates

The Anh Bui, Xuan Thinh Duong (2025). DOI: [10.1007/s11118-024-10158-0](https://doi.org/10.1007/s11118-024-10158-0). Full-text version: Official full text, printed pages 1–18; 18 physical PDF pages.; 18 physical pages.

In the self-adjoint Gaussian setting, Theorem 1.6 assumes sublinear T bounded on L2 and H_L^p→Lp for one 0<p<1; the operator Hardy-space hypotheses include the stated doubling/heat-kernel and atom parameters M>n/2(1/p−1/2). The self-adjoint route is source-supported. The non-self-adjoint Proposition 3.8 formula is false even for a positive scalar operator; Theorem 3.4’s proof route stays unverified until downstream molecule estimates are independently repaired. Do not transfer either to C207/C208 without matching all inputs.
Card: [evidence/W25/cards/AEP-EXT-014.md](../evidence/W25/cards/AEP-EXT-014.md).

## AEP-EXT-002 — Notes on Fourier Analysis (XXIX); subtitle: An Extrapolation Theorem

Shigeki Yano (1951). DOI: [10.2969/jmsj/00320296](https://doi.org/10.2969/jmsj/00320296). Full-text version: Official J-STAGE published scan, J. Math. Soc. Japan 3(2) (1951), printed pp.296–305; 10 physical pages; public PDF carries encryption flag and parses without supplied password.; 10 physical pages.

Yano’s theorem concerns real integrable functions on a finite interval, a finite-measure formulation, countable subadditivity/sign symmetry, and Lp operator growth of order (p−1)^−k for 1<p<2. It gives an L log^k L→L1-type result with an additive finite-measure term, not a weak distribution estimate. The printed Young-comparison footnote does not bound its weighted remainder; the card separately completes that step and handles the two lowest dyadic levels.
Card: [evidence/W25/cards/AEP-EXT-002.md](../evidence/W25/cards/AEP-EXT-002.md).

## AEP-EXT-006 — Weak Factorizations of the Hardy space H^1(R^n) in terms of Multilinear Riesz Transforms

Ji Li, Brett D. Wick (2016 (arXiv v2; 19 Mar 2016)). DOI: [10.4153/CMB-2017-033-9](https://doi.org/10.4153/CMB-2017-033-9). Full-text version: Complete author preprint arXiv:1603.02699v2 dated 2016-03-19, 12 physical pages; published counterpart Canadian Mathematical Bulletin 60(3) (2017), 571–585, DOI 10.4153/CMB-2017-033-9.; 12 physical pages.

The H1 weak factorization uses the paper’s multilinear Riesz-transform atom model and its Hölder/size assumptions. Each atom configuration needs the verified partial-adjoint denominator lower bound before division; retain the exact factorization and convergence hypotheses. It is not a direct weak-(1,1) estimate for a scalar Riesz coordinate and supplies no dimension-free C208 reduction.
Card: [evidence/W25/cards/AEP-EXT-006.md](../evidence/W25/cards/AEP-EXT-006.md).

## AEP-EXT-011 — Weak-type inequalities for Fourier multipliers with applications to the Beurling-Ahlfors transform

Adam Osękowski (2014). DOI: [10.2969/jmsj/06630745](https://doi.org/10.2969/jmsj/06630745). Full-text version: Official J-STAGE published journal free-access PDF, J. Math. Soc. Japan 66(3) (2014), 745–764; 20 physical pages.; 20 physical pages.

The martingale method applies to its exact Lévy-symbol multiplier class and 1<p<∞; Theorem 3.4’s vector weak-(p,p) output is restricted to the structured C^N-valued coefficient functions in the unit ball. The printed Theorem 1.2 appears to put the abstract weak norm where the distribution coefficient belongs: Eq. (3.6) gives a different exponent (e.g. p=3/2). Preserve this source discrepancy rather than silently correcting it. No p=1 weak endpoint or sharp C207 vector strong-Lp constant follows.
Card: [evidence/W25/cards/AEP-EXT-011.md](../evidence/W25/cards/AEP-EXT-011.md).

## AEP-EXT-004 — A variant of Yano’s extrapolation theorem on Hardy spaces

Odysseas Bakas (2019). DOI: [10.1007/s00013-019-01366-x](https://doi.org/10.1007/s00013-019-01366-x). Full-text version: Published Archiv der Mathematik 113 (2019), 537–549; Springer open-access PDF, 13 physical pages.; 13 physical pages.

Theorem 1 defines T on measurable functions over the one-dimensional torus, with modulus subadditivity |T(f+g)|≤|Tf|+|Tg| and complex homogeneity |T(αf)|=|α||Tf|. The L^p growth hypothesis holds for every g∈H^p for each 1<p≤2; the proof uses H∞ pieces G_λf that need not be analytic trigonometric polynomials. The conclusion is the stated L log^r L→L1 estimate only for analytic trigonometric polynomial inputs. Extending it to the full Hardy–Orlicz space additionally requires the pointwise difference condition |T(f)−T(g)|≤|T(f−g)| and density/unique extension. It is an eligible auxiliary endpoint method, not a Euclidean Riesz weak-(1,1) reduction.
Card: [evidence/W25/cards/AEP-EXT-004.md](../evidence/W25/cards/AEP-EXT-004.md).

## AEP-026 — The foundational inequalities of D. L. Burkholder and some of their ramifications

Rodrigo Bañuelos (2010). DOI: [10.1215/ijm/1336049979](https://doi.org/10.1215/ijm/1336049979). Full-text version: Complete author preprint arXiv:1012.4850v2 (first-page header 3 Aug 2011; physical PDF also prints an internal manuscript date 25 Oct 2018); journal issue Illinois Journal of Mathematics 54(3) is dated 2010, pp. 789–868; DOI record registered 2012. This is the complete preprint pagination, not publisher layout.; 99 physical pages.

This is a survey: distinguish its martingale statements/proof outlines from cited primary proofs. Sharp martingale inequalities are martingale inputs; the separate Brownian stochastic-integral representation followed by conditional-expectation projection gives strong-Lp Riesz-coordinate estimates. Projection need not preserve weak type, so martingale weak-L1 does not yield a Riesz weak-(1,1) bound. Problem 7 at physical p. 37/printed p. 35 asks for the optimal C_p in \(\lambda^p\,\operatorname{Leb}\{x\in\mathbb R^n:|R_j f(x)|>\lambda\}\le C_p\|f\|_p^p\) for the scalar Euclidean coordinate R_j, 1≤p<∞; its p=1 discussion says a dimension-independent constant is unknown and cites a C log(n) upper estimate. Remark 3.4.2 and Problem 8 at physical p. 38/printed p. 36 ask for weak-(1,1) of the Gaussian vector transform \(R_g f=\nabla(-L)^{-1/2}f\) on \(\mathbb R^n\) with Gaussian measure. These are distinct questions and neither concerns C207’s vector strong-Lp best constant. Reuse the Bellman outline only after independently verifying a smooth/localized U≥|Y|^p−c^p|X|^p, E U(X_0,Y_0)≤0, nonpositive Itô drift on the allowed directions, and valid localization/expectation/limit steps; the survey defers full proof details to [23,24].
Card: [evidence/W25/cards/AEP-026.md](../evidence/W25/cards/AEP-026.md).

## AEP-040 — The sharp weighted bound for general Calderón-Zygmund operators

Tuomas P. Hytönen (2012). DOI: [10.4007/annals.2012.175.3.9](https://doi.org/10.4007/annals.2012.175.3.9). Full-text version: Published Annals of Mathematics version, 175(3) (2012), 1473–1506; 34 physical pages.; 34 physical pages.

The sharp A2 theorem is weighted strong-L2 for standard Calderón–Zygmund operators with the source’s kernel data and A2 weight; its constant C(T) carries dimension/regularity dependence. Proposition 5.1 gives weak-(1,1) only for each bounded dyadic shift, with O(u) dependence. Do not describe the paper as proving weak-L1 for T or summing to a dimension-free scalar Riesz bound; its weak-L2 reduction is explicitly unused.
Card: [evidence/W25/cards/AEP-040.md](../evidence/W25/cards/AEP-040.md).

## Inventory boundaries

The 30 source records are research papers or standalone journal/proceedings contributions; none is counted as a whole textbook. Three published contributions (AEP-019, AEP-020 and AEP-045) have no DOI recorded; unique PDF SHA-256 and distinct titles preserve their identities. AEP-020’s official correction is linked as same-work support.

The W25 pool contains 56 candidate rows: these 30 approved works plus 26 metadata-only/not-acquired rows in evidence/W25/candidate_pool_exclusions.json. AEP-EXT-007, AEP-EXT-012 and AEP-EXT-013 are separately preserved full-text background readings with zero quota credit; they are not part of the 30. W25-L15-B13 is outside this binding. Do not add it to the count without a new independent review.

R01’s exact final mother decision, per-source decision objects, 694-file source binding, and candidate transformation ledger are under scope/source_approvals/ and scope/. Source-specific proof gaps and conditional repairs remain exactly as stated in the cards.
