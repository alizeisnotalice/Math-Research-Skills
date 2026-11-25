# Admitted source scopes

This is the operative source index for this candidate. Every entry below is one distinct work with a current reviewer-issued Brownian scoped-use row. The row does not certify every theorem in the work. Exact standard rows, original PDF identities, conditions, transfer limits, locators, reading evidence, and reviewer hashes are preserved in source_admissions.json（本机附件：`references/source_admissions.json`）. Packaged usage cards and independent review records are linked per source below; the current standard row’s accepted method, conditions, and limits control if an older card is broader.

## Version metadata supplement

The immutable batch04 admission row had null version fields for W08-R001 and W08-R007. The exact version metadata is supplied by the append-only R08 source version supplement（本机附件：`references/source_version_metadata_supplement.json`）; it does not alter accepted methods, conditions, reading coverage, or quota.

## Counting and book boundary

The R08-verified cohort contains 40 distinct works: the original 31, five distinct works already admitted in the earlier Brownian eight-row record, and four newly rebound Brownian works. Thirty-five current scoped uses are accepted (34 papers and one book); five works are currently held. Candidate05’s eight added rows all overlap the original 31 and add no new work. This continuation adds no global full-read credit.

M0224, Brownian Motion, is one book item. The whole 413-page book was acquired, but only four complete historical units totaling 107 physical pages were read and used: Chapter 4, pp. 106–127; Chapter 8, pp. 234–264; Chapter 9, pp. 265–299; Appendix Chapter 11, pp. 337–355. Do not infer whole-book or blanket chapter coverage.

## Current accepted scoped uses

### 1. PR-f7109db62ff7 — The Dimension of the Frontier of Planar Brownian Motion

- Work/version: paper; Electronic Communications in Probability1(1996)29–47, exact19p local PDF..
- Source PDF: workers/W08/papers/lawler_frontier.pdf (SHA-256 f57dea508d5181caa7da2c5f9f30c34ff23a3a067750fdaffe1222567decfe6d).
- Accepted method: Proposition3.8/Corollary3.9 sharp two-arm planar disconnection probability: q(nm) comparable to q(n)q(m), hence q(n) comparable to n^(-2alpha), with the lower bound uniform over all unit-circle starting pairs.
- Conditions: Independent planar BM paths, each stopped at its own radius-n exit; event leaves0 in the unbounded complementary component. All unit-circle starts permitted, no unit-separation constraint. Source alpha is half the radius exponent. Corrected opening-Theta wedge power pi/Theta and fixed-annulus gluing are supplied analytically.
- Transfer limits: The whole old-card a.s. frontier-dimension/minimum-point upgrade and later numeric alpha=1/3 are not qualified here. No nonintersection or Jordan-arc infimum conclusion.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch02/admissions.json /rows/1 (SHA-256 6adbae8b0466ff1d78abf030d8ef06dc862e31c6d781c5be4a8b9d321d7b02de); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-f7109db62ff7/usage_card.md`） (SHA-256 5f9aeb0f34a3c90ae754180a5d245b665cadf3063fbef4a4b7c46a4d3af68b65); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-f7109db62ff7/review_record.json`） (SHA-256 35c2db92b89e39e1ed8ac2d7b0cc434fa4af02f613c2dc1c80261d9b558b0aa0).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 2. PR-2a6cfc3818b2 — Conformal restriction: The chordal case

- Work/version: paper; arXiv:math/0209343v2, 25 Apr 2003; journal locator is JAMS 16 (2003), 917–955, DOI 10.1090/S0894-0347-03-00430-2. The local PDF is the v2 preprint..
- Source PDF: workers/W08/papers/lsw_conformal_restriction.pdf (SHA-256 54dbe827b62f581db81e7420cb527e176c94303af913c15d607ab03fe702442d).
- Accepted method: Complete Brownian-excursion h-transform restriction proof: X+iBES3 has avoidance probability Phi_A'(0); conditional conformal path law up to clock; independent integer-n filled unions have exponent n.
- Conditions: Source Q* bounded half-plane hull away from0, H\A simply connected; Phi fixes0,infinity and Phi(z)/z tends1. X and BES3 independent. Use source F_H^R filling. Local version math/0209343v2,25Apr2003.
- Transfer limits: SLE8/3, bubble/rho construction and Section9 identities/boundary4/3 are outside this admission. No full-trace equality or Brownian arc dimension.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch02/admissions.json /rows/3 (SHA-256 6adbae8b0466ff1d78abf030d8ef06dc862e31c6d781c5be4a8b9d321d7b02de); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-2a6cfc3818b2/usage_card.md`） (SHA-256 6517da6bd89706cd9f1130c3e11d77f6b0031e80661ef0c58ac118acafae4bf4); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-2a6cfc3818b2/review_record.json`） (SHA-256 de52db37e83c5558dc5c9001378b900c5cc8d82b75b111da9ca79d8f684ed1f9).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 3. PR-a55bd0ea17e1 — The dimension of the SLE curves

- Work/version: paper; arXiv:math/0211322v3,27Aug2008; electronic AOP36(4)(2008)1421–1452 reprint,33 physical pages, explicitly different pagination/typography from original..
- Source PDF: workers/W08/papers/beffara_sle_dimension.pdf (SHA-256 2b3b24b13b5770b05590588764be1805d862ad6a9e70cb010bfc3dc4ead33ffc).
- Accepted method: For each fixed kappa>0, chordal SLE trace in H has Hausdorff dimension min(2,1+kappa/8) almost surely, using the audited one-/two-point, fjord/reduction/summation and energy/germ chain.
- Conditions: Continuous transient chordal SLE trace driven by sqrt(kappa) standard BM, half-plane capacity2t. Fixed kappa; constants may depend on kappa and compact boxes. Correct Bessel dimension3-8/kappa, pre-swallowing boundary distance, and all absorbed-target conventions retained. Local electronic reprint math/0211322v3,27Aug2008.
- Transfer limits: No general kappa>4 boundary-duality theorem, radial whole-curve bridge, Brownian containment, or Jordan-arc-infimum result. No universal measure prefactor.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch02/admissions.json /rows/4 (SHA-256 6adbae8b0466ff1d78abf030d8ef06dc862e31c6d781c5be4a8b9d321d7b02de); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-a55bd0ea17e1/usage_card.md`） (SHA-256 49b81ce5b225697e5865118740ee57f015fc5478a88860d5dd753ee396ef2610); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-a55bd0ea17e1/review_record.json`） (SHA-256 30e72d5d4c2d4302e06bea7a16565a18c36ba7f326bcb1d8968ced7180d04fee).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 4. PR-2a7280a2bd33 — Non-intersection exponents for Brownian paths

- Work/version: paper; Probability Theory and Related Fields 84 (1990), 393–410; full 18-page journal-layout PDF.
- Source PDF: workers/W08/papers/M0193_seed.pdf (SHA-256 43233829fd61c948b480c2bf6ac32cb8749770ad74ce303fbcdebd1e38087c8e).
- Accepted method: Representative n=3,k=m=1 exit-ball nonintersection exponent exists and agrees for Brownian motion/random walk from0,e1; fixed-time exponent is half that radius exponent.
- Conditions: Two independent 3D paths or nearest-neighbor walks, distinct starts0/e1, source exit conventions. Brownian proof covarianceI/3 matches scaling; constant speed changes do not change exponent. Harnack, robust separation and many local conditioned intersection opportunities retained. Use the weaker good-radius limsup statement sufficient for the proof, not a circular literal Lemma3.7 liminf invocation.
- Transfer limits: Larger packets and n=2 have omitted/analogous source proofs and are not newly certified by this representative row. No sharp asymptotic constant, numerical exponent or dimension formula.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch02/admissions.json /rows/6 (SHA-256 6adbae8b0466ff1d78abf030d8ef06dc862e31c6d781c5be4a8b9d321d7b02de); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-2a7280a2bd33/usage_card.md`） (SHA-256 186957805393eef699310e78976dc77240768ceac258ba47d573534fda384572); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-2a7280a2bd33/review_record.json`） (SHA-256 f8f7510b8ed7e8e90552fe524644df3f18ea8f9d2720e89ccac7193c5f511b6f).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 5. PR-9c36cf792ab0 — Hausdorff Dimension of Cut Points for Brownian Motion

- Work/version: paper; Electronic Journal of Probability1(1996),paper2, exact20p local PDF..
- Source PDF: workers/W08/papers/lawler_cut_points.pdf (SHA-256 c23e1fbb0af2c968e8d6ee45acc75abf5801991aab6ed8fef35798a8e7eab583).
- Accepted method: For standard BM in d2/3, source cut-time set has dimension1-zeta and cut-point image dimension2(1-zeta) almost surely, with the explicit independently verified macro/protected-measure/germ repair and simultaneous Kaufman dependency.
- Conditions: Source radius nonintersection exponent2zeta with0<zeta<1, all sharp/separation/exit/two-cell inputs checked by R08; use actual epsilon/lambda separated neighborhoods, corrected spatial-R macro event, R=sqrt(N)/2,K4 anchored past protection, and planar C/n close-pair bound. Book dependency only already complete Ch9 physical289–292; no whole-book read.
- Transfer limits: No numerical zeta evaluation or planar arbitrary-Jordan-arc infimum. Strict d3 endpoint-path lower bound>1 additionally imports zeta3<1/2; no planar infinite-horizon cut-time claim.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch02/admissions.json /rows/7 (SHA-256 6adbae8b0466ff1d78abf030d8ef06dc862e31c6d781c5be4a8b9d321d7b02de); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-9c36cf792ab0/usage_card.md`） (SHA-256 32b668403ffc13c4987f04fa8b40cc00c4c59cc86f3503bec1440c86b919fbf1); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-9c36cf792ab0/review_record.json`） (SHA-256 93b5e93073f29db2dfbda2d8d066350b0948299f8ab4ecc8a676c06f0c39252b).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 6. PR-58f59904e178 — Asymptotic behaviour of disconnection and non-intersection exponents

- Work/version: paper; Probability Theory and Related Fields 108 (1997), 131–152; full 22-page journal-layout PDF.
- Source PDF: workers/W08/papers/M0196_seed.pdf (SHA-256 f1240f6b31a20cf9dd3a2b37c36336309e048cf198d3874bb51b875f27e6a8fe).
- Accepted method: Proposition1 large-packet disconnection radius exponents eta_n/n ->1/2 using the explicitly corrected outer connector and fixed-R finite-net proof.
- Conditions: Independent planar Brownian arms, supremum of arbitrary unit-circle starts, own first radius-R exits, non-disconnection of0. Use F_(R+1), strict sausage witnesses/positive clearance, and ordinary first-hit stopping times. First n->infinity at fixed R/epsilon/alpha, then epsilon->0, then R large. Time exponent eta_n/2.
- Transfer limits: Prop1 legacy disconnection asymptotic only. Proposition2 spider proof, exact finite-n exponents, frontier dimensions, Jordan-arc infima, derivative increments and conjectures excluded.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R14/continuation_20261116/admissions.json /rows/2 (SHA-256 4df8f9fb73827032abbce63b162eb3c69eb63eadb11d7772027781df1dc809f4); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-58f59904e178/usage_card.md`） (SHA-256 03f99c1091e723b1f55153bfa0d809f3b2eb4634ba9720a2779f2f1db411162d); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-58f59904e178/review_record.md`） (SHA-256 03f99c1091e723b1f55153bfa0d809f3b2eb4634ba9720a2779f2f1db411162d).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 7. PR-5ee8d055e2af — Values of Brownian intersection exponents, I: Half-plane exponents

- Work/version: paper; arXiv:math/9911084v2, 23 Oct 2000.
- Source PDF: workers/W08/papers/lsw_intersection_exponents_half_plane.pdf (SHA-256 2cd15441a5dfa07f005a5c6d213030989e69e61b5bcd8b414c6608e17f94e1ac).
- Accepted method: Stopped chordal-SLE6 locality plus the fully proved generalized-Cardy rectangle moment E[1_success exp(-lambda Lbar)]=exp[-u(lambda)L+O(lambda+1)], u=(6lambda+1+sqrt(24lambda+1))/6.
- Conditions: SLE6 rectangle width L,height pi, starts top-left, stops first bottom-or-right hit; Lbar=infinity on failure; lambda>=0. Locality only to specified internal-boundary hitting time, with increasing capacity clock.
- Transfer limits: Independent SLE interface only. Numeric Brownian exponent transfer, general cascade, radial comparison, percolation scaling and frontier/arc dimensions excluded pending separate exact dependencies.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch03/admissions.json /rows/2 (SHA-256 0a7670e05574a3630a43344c91cafda15298f02ee23c34eb79a2ce4acbae22a8); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-5ee8d055e2af/usage_card.md`） (SHA-256 9eae7a3a9395c2278f4821b65fb68b123b5c191afcb8c98c50a7789f7db767ce); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-5ee8d055e2af/review_record.json`） (SHA-256 e006dd20e2b38dc55834deba388493eeada62224833b65a5ae26533bf6eda614).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 8. PR-cd2918747063 — Values of Brownian intersection exponents, II: Plane exponents

- Work/version: paper; arXiv:math/0003156v3, 13 Dec 2000.
- Source PDF: workers/W08/papers/lsw_intersection_exponents_plane.pdf (SHA-256 059b0dd5507556b87ced0951c121557cf99a7a99a03e5d6a27795e1d27f087c5).
- Accepted method: Radial-SLE derivative and harmonic-measure moments, annulus first-hit moment E exp(-b L(r)) comparable r^nu, and the proved kappa6 stopped radial/chordal bridge.
- Conditions: kappa>0; derivative lemma b>0,t>=1,uniform initial angle. Harmonic-measure and annulus theorem b>=1. nu=(8b+kappa-4+sqrt((kappa-4)^2+16b kappa))/16. Bridge kappa6 only before first disconnection of0 and target1, with increasing time change.
- Transfer limits: No general full-curve equality. Exact Brownian numeric transfer and frontier/pioneer corollaries retain unclosed cascade/dimension dependencies; no SLE2 scaling-limit assertion.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch03/admissions.json /rows/3 (SHA-256 0a7670e05574a3630a43344c91cafda15298f02ee23c34eb79a2ce4acbae22a8); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-cd2918747063/usage_card.md`） (SHA-256 7192ff72afcc440a75074fb5d3b6eb1a323718e5c4cc5abc4c8fc4c527d69250); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-cd2918747063/review_record.json`） (SHA-256 05eba60084ca5d705eadd9d9c69bdfd825439600f1648b17ac4477d951668fcb).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 9. PR-f9e89b6cc4a1 — Analyticity of intersection exponents for planar Brownian motion

- Work/version: paper; arXiv:math/0005295v1, 31 May 2000 (local PDF title page); published Acta Mathematica 189 (2002), 179–201.
- Source PDF: workers/W08/papers/M0206_LSW_Analyticity_2002_arxiv.pdf (SHA-256 66c4b13bab4ecea29cf52615dbe0458a700c9f5ac44eb95e1e2bc919290c8e85).
- Accepted method: Proposition4.1 h-process coupling: under exact X_m hypotheses, traces outside e^(-m/2)U coincide with failure <=C exp(-v0 m), proved via strip harmonic density and separating crosscuts.
- Conditions: m>=1; gamma,gamma-prime in Gamma; both no-downcrossing Y_m, identical terminal segments gamma_m, identical accessible outer boundary arc. h-process starts at simple boundary prime end0, conditioned to exit accessible outer arc; constants uniform over X_m.
- Transfer limits: Admitted exponential domain-forgetting coupling only. It is not common-filtration/co-adapted Brownian coupling or meeting tail. Full exponent analyticity/spectral gap remains conditional on separate arbitrary-initial-domain sharp/separation inputs.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch03/admissions.json /rows/4 (SHA-256 0a7670e05574a3630a43344c91cafda15298f02ee23c34eb79a2ce4acbae22a8); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-f9e89b6cc4a1/usage_card.md`） (SHA-256 a22a15b1392f399757e66fde47bbd5104d0f6ac3245d034dd11c4c891eb81b65); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-f9e89b6cc4a1/review_record.json`） (SHA-256 1af41680dcf99a1ba330ee19d357af95d4b3fe67d6a317735d83de725f93d9c3).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 10. PR-d28f92a9f991 — Sharp Estimates for Brownian Non-intersection Probabilities

- Work/version: paper; arXiv:math/0101247v1, 30 Jan 2001.
- Source PDF: workers/W08/papers/lsw_sharp_nonintersection.pdf (SHA-256 197fd197c6d00a8e052da173121d4bd4a4dedf72fb0c202ffe60d58c437f83a0).
- Accepted method: Theorem1.1 sharp up-to-constant avoidance moments uniformly for0<lambda<=lambda0,r>=2, and Corollary1.2 nondisconnection limit atlambda0, with the explicit fixed-annulus nice-pasting/constant clarification in the R08 proof note.
- Conditions: Three independent planar Brownian arms start independently uniformly on unit circle, each stops on first radius exp(r). Z_r is conditional avoidance probability given arms1,2. Fixed finite lambda0; constants depend onlambda0 but notlambda,r.
- Transfer limits: No exact exponent values, frontier dimension or arbitrary-state h-process separation theorem is inferred. Original source numerical final section is not the admitted proof.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch03/admissions.json /rows/5 (SHA-256 0a7670e05574a3630a43344c91cafda15298f02ee23c34eb79a2ce4acbae22a8); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-d28f92a9f991/usage_card.md`） (SHA-256 86ee70c3431b6647a9a0c14b5c69a1241e5af7f37b4846e5365aad400d9d45a3); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-d28f92a9f991/review_record.json`） (SHA-256 b7adec7b7f4e15501a990e31df9a88dbe4f4fef410b7738c67087db697582add).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 11. PR-11816c91d974 — Values of Brownian intersection exponents III: Two-sided exponents

- Work/version: paper; arXiv:math/0005294v1, 31 May 2000.
- Source PDF: workers/W08/papers/lsw_intersection_exponents_two_sided.pdf (SHA-256 c941c48b5ecc98b8d1946ad55bfc87ef56ab16f9c6ec3bc57bab9f9de20a9611).
- Accepted method: Theorem3.1 two-sided chordal-SLE derivative moments, via the killed-Jacobi generator eigenfunction G=x^a1(1-x)^a2 and summable boundary-scale comparison.
- Conditions: kappa>0,w1,w2 strictlypositive,x in(0,1),s>=1; s=log(g_t(1)-g_t(0)), before first swallowing0 or1. G exp(-lambda s)<=h1<=C G exp(-lambda s), lambda and a_j exactly as in the bound PDF physical6 and proof note.
- Transfer limits: Independent derivative-moment interface only. Theorem4.1 geometric conversion is traced but not needed to enlarge this row. General Brownian numeric cascade/zero-weight/whole-plane/frontier claims excluded.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch03/admissions.json /rows/6 (SHA-256 0a7670e05574a3630a43344c91cafda15298f02ee23c34eb79a2ce4acbae22a8); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-11816c91d974/usage_card.md`） (SHA-256 ab41070c47f84e9e4e0c934807a389ddb137fd332aba4e609ba2a9dd57d1e8b2); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-11816c91d974/review_record.json`） (SHA-256 7d87a15a5d3a5f62adb24e52d8918b69700c1eb4061dcb8a2f76e5a15e336306).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 12. PR-290a8cdcb9cf — Brownian Motion

- Work/version: book; Cambridge University Press 2010 edition, complete 413-page PDF locally verified; only Chapters 4, 8, 9 and Appendix Chapter 11 were read in full..
- Source PDF: workers/W08/papers/moerters_peres_brownian_book.pdf (SHA-256 e850e30e824d33494e40c63faba0e23e364c8ccd80f58cee0d85732277071681).
- Accepted method: Direct mass-distribution/positive-alpha energy method and Brownian occupation-measure dimension proof, compact-target Martin-capacity hitting comparison in transient d>=3, and exact prior Kaufman simultaneous all-subsets proof reuse.
- Conditions: Finite positive Borel mass; energy alpha>0, Gaussian negative moments0<alpha<d,time integrabilityalpha<2. Martin safe subcase unkilled Brownian d>=3,start0,compact A avoiding0,M=G(x,y)/G(0,y),factor1/2 retained. Kaufman d>=2 on a single probability1 event for every time subset.
- Transfer limits: Only historical four complete units107p; no whole-book read/high certification. Appendix11 partial-proof overview, general Wiener/last-exit/intersection/Frostman routes and full SLE bridges are not blanket high qualified; no Jordan-arc infimum.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch03/admissions.json /rows/7 (SHA-256 0a7670e05574a3630a43344c91cafda15298f02ee23c34eb79a2ce4acbae22a8); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-290a8cdcb9cf/usage_card.md`） (SHA-256 678b4d6313e9a5d9886bb9db5ce41ef004b59afdd667ebdec128d0c4a3f34e45); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-290a8cdcb9cf/review_record.json`） (SHA-256 b51baf51966cddc4376ff158150f5b14ad566bd0d4febc9bcb93fe4cb3b1047a).
- Reading basis: complete_used_book_units; new global-read credit in this continuation is 0.

### 13. PR-15114922f01b — Labyrinth dimension of Brownian trace

- Work/version: paper; Exact undated 35-page University of Washington author manuscript, title LABYRINTH DIMENSION OF BROWNIAN TRACE; local bytes only, no journal-version equivalence asserted.
- Source PDF: workers/W08/papers/burdzy_labyrinth.pdf (SHA-256 7455ec6265b6f9e8b898c8268f8b8e7b1f5adc6d6ddb6a6d5e3911bfa84283ea).
- Accepted method: Conditional exact-gauge surgery: finite (P)-path reconnections and summable removal budgets produce nested compact path ranges with a dense protected ordered set; the limit admits an injective continuous parametrization and loses less than epsilon in phi-measure.
- Conditions: Planar Brownian (P)-paths as defined physical/printed11–13; use the explicit no-local-double-cut and exact trace/double-point gauge facts as named external hypotheses. phi=r²log(1/r)logloglog(1/r), phi2=r²(log(1/r)logloglog(1/r))² for sufficiently small r. Protected endpoints and the full Lemmas2.3–2.8 hypotheses retained.
- Transfer limits: Accepted conditional construction and measure-budget mechanism; external Taylor/Le Gall exact-gauge inputs and Burdzy–Lawler first-case no-double-cut input are not newly high-qualified here. No unconditional full Theorem1/1-prime requalification, no Jordan-arc infimum, frontier, all-arc dimension or reflected diffusion transfer.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch04_admissions.json /rows/0 (SHA-256 89460135e979ee042b782dcc5d87d4c5a1cf30b149432aeecd0b5a1f199e7a1d); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-15114922f01b/usage_card.md`） (SHA-256 9ab4e85a5586fdd65e9398bdcadf92cfa9a1558b2a6e5cb5441ad62e107483f0); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-15114922f01b/review_record.json`） (SHA-256 50262c21b13045f2165a7fb9b991af6971af4529982e8fb6457af7e1f349a335).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 14. PR-377ea198cb75 — Mirror couplings and Neumann eigenfunctions

- Work/version: paper; arXiv:math/0607400v1, 18 Jul 2006.
- Source PDF: workers/W08/papers/atar_burdzy_mirror.pdf (SHA-256 b364bdd3c41b1ef28f4ff704f6704316e886d7c1494524b500e8339bb2f3db22).
- Accepted method: For a bounded strictly convex planar C2 domain satisfying all five source Assumptions2.1–2.5, including every primed hinge/arc condition, use the mirror pair with correct inward-normal reflected marginals. The invariant mirror-state set and its specified initial side/order support the source second-Neumann-eigenvalue simplicity theorem. Proposition4.1 is only a sufficient coupling-separation criterion, supplied by the source mirror construction under that geometry.
- Conditions: All five original §2 assumptions and definitions retained exactly in frozen old card; the invariant-order claim additionally requires X0!=Y0, U0 in the constructed invariant set and the designated initial mirror side. Theorem2.1 is not claimed for all smooth convex domains. Brownian drivers for the selected mirror construction are predictable orthogonal transforms in the common filtration, with coalescent continuation.
- Transfer limits: No triangle-corner Skorokhod solver, arbitrary-start acute-triangle meeting tail, spectral-optimal coalescence rate, or impossibility for all couplings.
- Method IDs: G16.02, G16.05.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch01/admissions.json /rows/0 (SHA-256 ee64345c07f9fdf306dd0f06dd33d0ead0c11b479072b0bba03fa7a9fbead63e); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-377ea198cb75/usage_card.md`） (SHA-256 9b01d498b7965e0266e337c1ff3d0615e33186dbcbbd977d128055c66d648acc); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-377ea198cb75/review_record.json`） (SHA-256 e469c36ce86f08b17cf2b2769cd284cfdfc90badc273acfa96f8e4fcf71e99bf).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 15. PR-135a373bfff4 — Efficient Markovian couplings: examples and counterexamples

- Work/version: paper; Local 57-page author PDF, first-page date 4 Nov 2005; journal edition: Annals of Applied Probability 10(2) (2000), 362–409.
- Source PDF: workers/W08/papers/burdzy_kendall_efficient.pdf (SHA-256 12380a4a56f086a0b77e92ebd84455b77c85dd3af75b75567c57d39c57b84ccb).
- Accepted method: Use Lemma3.5 for a spectral rate ceiling with nonzero leading spectral difference, Definition3.6 for existence of suitable eigenfunction-separated starting pairs, and Theorem3.7 for mirror efficiency in obtuse triangles and mirror inefficiency only for strictly acute triangles with pairwise distinct angles.
- Conditions: Retain source spectral/operator time convention and nonzero eigenfunction difference. The single-product leading-density expansion uses its simple leading-mode assumption; with multiplicity one must use the full nonzero projector, or the bounded-eigenfunction coupling argument. Sticky continuation after meeting is required. The efficiency classification concerns the specified mirror scheme, not all couplings. Source physical40: each mirror subpair is Markov; their auxiliary four-process comparison is noncoadapted and non-Markov.
- Transfer limits: Do not silently repair physical21 printed pi and pi/100 scale, extend acute inefficiency to repeated angles, or rule out all Markov/coadapted/unrestricted couplings.
- Method IDs: G16.02, G16.03.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch01/admissions.json /rows/1 (SHA-256 ee64345c07f9fdf306dd0f06dd33d0ead0c11b479072b0bba03fa7a9fbead63e); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-135a373bfff4/usage_card.md`） (SHA-256 50e58dc34f83e7d36a214df4758f2f05839bb1fbb23590bd58c6b16893d12bd4); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-135a373bfff4/review_record.json`） (SHA-256 0dd83d6e84e67b275f53a84c84dabdbfb1123d2cd31b424708a251aab645c7fc).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 16. PR-79d79b3b00c8 — The dimension of the Brownian frontier is greater than 1

- Work/version: paper; arXiv:math/9508222v1, submitted 2 Aug 1995; the arXiv manuscript says published in modified form as JFA 143 (1997), 309–336, DOI 10.1006/jfan.1996.2928. Local PDF is v1, not journal layout..
- Source PDF: workers/W08/papers/bishop_jones_frontier_gt1.pdf (SHA-256 814295f91479e910c4fdb25803dfe47b9d5a1ecb937e131e57bacebfbe41ad71).
- Accepted method: Tree-filtration offspring/independent-thinning dimension interface (Lemmas3.3–3.4) and Brownian local surround-versus-exit endpoint estimate (Lemma6.2); quantitative constants remain existential.
- Conditions: Countable rooted random tree, tree-filtration with trunc_v(T) F_v-measurable and conditional offspring mean >=b>1, bounds m<=offspring<=M<infinity with0<=m<M and b<=M; boundary metric C theta^(-n),theta>1. For Lemma6.2, G=z+rG0,r in(0,1),eta in(0,1/10),x in core, J the fixed scaled separating rectifiable Jordan curve; Brownian standard strong Markov/Harnack inputs.
- Transfer limits: No new certification of the full Brownian frontier dimension theorem, exact epsilon, omitted Section7 flatness proof, general cascade or Jordan-arc infimum. Jones traveling-salesman theorem and full Gosper geometric verification are explicit dependencies if the full frontier chain is later requested.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch04_admissions.json /rows/2 (SHA-256 89460135e979ee042b782dcc5d87d4c5a1cf30b149432aeecd0b5a1f199e7a1d); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-79d79b3b00c8/usage_card.md`） (SHA-256 74643ab2fbc285f04fc20fd613ca5a55640cf751677e498a287aef157f5977fe); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-79d79b3b00c8/review_record.json`） (SHA-256 fb22a1ecaa549298d715f9e800fd0bee96e6039a0a7d8388f66b99e79baabfaf).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 17. PR-dc86eaebf6b4 — Basic properties of SLE

- Work/version: paper; arXiv:math/0106036v4, revised 20 Jan 2004; journal: Annals of Mathematics 161 (2005), 879–920.
- Source PDF: workers/W08/papers/rohde_schramm_basic_sle.pdf (SHA-256 c99b1f570d8f7f2ad3aec13cdd918d81050f8cdac50bc6296e1790c06bafb622).
- Accepted method: Chordal SLE boundary non-hitting scale-function proof (Lemma6.2) and rational-time domain-Markov separation proof of simple trace for0<=kappa<=4 (Theorem6.1).
- Conditions: Chordal upper-half-plane SLE driven by sqrt(kappa)B, hydrodynamic Loewner normalization dg=2/(g-xi)dt. For kappa>0 the real-point diffusion Y/sqrt(kappa) has Bessel dimension1+4/kappa; kappa0 is deterministic. Use source continuous-trace Theorem5.1 for kappa!=8 and domain-Markov Proposition2.1.
- Transfer limits: No radial whole-curve dimension transfer, exact trace or hull-boundary dimension, kappa8 continuity proof, Brownian frontier equality or Jordan-arc infimum. Theorem8.1 expected-cover exponent is not treated as Hausdorff equality.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch04_admissions.json /rows/3 (SHA-256 89460135e979ee042b782dcc5d87d4c5a1cf30b149432aeecd0b5a1f199e7a1d); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-dc86eaebf6b4/usage_card.md`） (SHA-256 5ccc8ad08e0a525095c3d784abe3e941eee0a9eb0ba17ad8d1f63751e551bba6); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-dc86eaebf6b4/review_record.json`） (SHA-256 02972547eb407ff3a38ec03c23ead1a4715726486b7400cea6fc755ed5863a30).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 18. PR-1018a43b4e34 — Loop-Erasure of Plane Brownian Motion

- Work/version: paper; arXiv:1001.3189v1 [math.PR], 19 Jan 2010; exact 10-page local preprint.
- Source PDF: workers/W08/papers/zhan_loop_erasure_bm.pdf (SHA-256 b79363ec0b16201d6c3002751a610e8655727ab180a51c099a30a248adc6ea47).
- Accepted method: Localized two-time commutation density: harmonic h-transform ratio and radial-SLE2 Poisson-kernel martingale yield a bounded stopped change of measure preserving both marginals on disjoint nested Jordan separators.
- Conditions: Unit disk, complex Brownian coordinates each variance t; positive normalized Poisson kernel Q0 for exit at1; radial SLE2 from1 toward0 independent initially. Separators sigma1,sigma2 are disjoint Jordan curves surrounding0, sigma2 surrounds sigma1. Stop before their corresponding first hits; constants depend on the fixed separator pair.
- Transfer limits: Only Lemmas4.1–4.2 and local measure following them. Global finite-family extension Proposition5.1 and weak-limit consistency invoke [11] and are not independently qualified here. No full loop-erasure theorem/uniqueness/algorithm upgrade or radial Hausdorff dimension inference.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch04_admissions.json /rows/4 (SHA-256 89460135e979ee042b782dcc5d87d4c5a1cf30b149432aeecd0b5a1f199e7a1d); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-1018a43b4e34/usage_card.md`） (SHA-256 4a0e400a585a47410fc4e8797e8c0079b7604cea13aa84fc2a71b32310cb4bfc); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-1018a43b4e34/review_record.json`） (SHA-256 2430b4bbe53f658261a017c4defa899b502214319079972586e944dc82bada7c).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 19. PR-6cd7f64e3473 — Shy couplings

- Work/version: paper; arXiv:math/0509458v1, submitted 20 Sep 2005; published PT&RF 137(3–4) (2007), 345–377..
- Source PDF: workers/W08/papers/shy_couplings.pdf (SHA-256 67f00f8a2c6ba0af54458a0adc1761aec3ebb157c809c93d348a8789a70d17e1).
- Accepted method: Strict-convexity/local-time obstruction to shy reflected couplings with sublinear displacement bracket (Theorem4.1(ii)), using a bounded-state martingale strong law and convex inward-normal signs.
- Conditions: Bounded strictly convex domain, normal reflected coordinates driven by Brownian motions in the common filtration as in(4.1)–(4.2); displacement quadratic variation A_t=<B-W>_t=o(t) almost surely. Retain source normalization L^X/t,L^Y/t ->surface(boundary)/(2volume(D)); for nonsmooth boundary use normal-a.e. and zero local time on surface-null exceptional sets.
- Transfer limits: No blanket Theorem4.3 pursuit theorem, arbitrary/non-coadapted coupling nonexistence, graph Theorem3.1, Example4.2 numerical rate, polygon result, finite meeting or spectral meeting-tail bound. Source default Markov(i)–(ii) is recorded but not equated to arbitrary coupling.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch04_admissions.json /rows/5 (SHA-256 89460135e979ee042b782dcc5d87d4c5a1cf30b149432aeecd0b5a1f199e7a1d); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-6cd7f64e3473/usage_card.md`） (SHA-256 ceb10173492cd10b466d8841b8de6172b14986fb508ee4c599e621b39c1d2bba); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-6cd7f64e3473/review_record.json`） (SHA-256 91c81d25b32bf705b983e3aded4ab1695df07a0480d2afa5c604d713f7883930).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 20. PR-834235cbb2c4 — Reflection couplings and contraction rates for diffusions

- Work/version: paper; arXiv:1305.1233v4, revised 19 Oct 2015; journal DOI 10.1007/s00440-015-0673-1.
- Source PDF: workers/W08/papers/eberle_reflection_contraction.pdf (SHA-256 93263a5a09dcf2409f2483c6196042296c2c14fd47d8643ba5e35209ef7be634).
- Accepted method: Use Eberle Theorem1/Corollary2 for a constant-invertible-noise diffusion on R^d under its curvature/cost hypotheses, plus the old-card Remark3 extension only for smooth bounded convex normal reflection with G=I. The product interface is accepted only as Theorem7 and the positive-rate Corollary8 subset via approximate componentwise coupling and scalar Kantorovich estimates.
- Conditions: Core: locally Lipschitz b, nonexplosive solution, fixed invertible sigma, SPD G, exact transformed direction e=sigma^-1(X-Y)/|sigma^-1(X-Y)| and source kappa/R0/R1 all-future-radius quantifiers; continuous kappa, positive liminf at infinity and integral_0^1 r*kappa^- finite. Reflected extension retains normal reflection, smooth bounded convex D, G=I and the restricted-kappa/diameter conventions. Product: finite n, identity component noise, locally Lipschitz nonexplosive b_i=b_i0+gamma_i, continuous kappa_i, positive liminf at infinity, r*kappa_i(r)->0 at0, weights0<w_i<=1 and source(49) with0<=epsilon_i<c_i. Cor8 requires nonnegative interaction Lipschitz lambda with2lambda/phi_i(R0_i)<c_i for every i. Finite corresponding initial costs.
- Transfer limits: No direct TV contraction, variable-sigma theorem, nonsmooth polygon/triangle reflection, general G reflected extension, exact discontinuous componentwise coupling, or spectral meeting-tail inference. No certification of every application in the cited sections, signed-alpha Cor9 rate or its preceding numeric sufficient smallness line.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch01/admissions.json /rows/2 (SHA-256 ee64345c07f9fdf306dd0f06dd33d0ead0c11b479072b0bba03fa7a9fbead63e); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-834235cbb2c4/usage_card.md`） (SHA-256 6f74b271fcbace7a21c2ef43bae90ba6e970fc0ca91b634dd7f0b3207176d702); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-834235cbb2c4/review_record.json`） (SHA-256 9242dc208344ce4a7486ca75caadc489dfee2b945319a151f2ac09880a5e5b9e).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 21. PR-49b1b6d0cdd1 — Brownian couplings, convexity, and shy-ness

- Work/version: paper; arXiv:0809.4682v3, revised 25 Nov 2009; published ECP 14 (2009), paper 7, pp. 66–80. Local PDF was visually read because OCR/text extraction was corrupted..
- Source PDF: workers/W08/papers/kendall_brownian_convex_shy.pdf (SHA-256 8e8ce284efa1542db9be62047ed73d6842e5049abe57cff14eac05975e3df28d).
- Accepted method: Potential supermartingale test (Lemmas4–5), predictable covariance representation (Lemma6), and small-pole quadratic potential proof of no co-adapted shy coupling for bounded convex domains without boundary segments (Theorem7).
- Conditions: Closure of bounded convex domain in R^n; no nondegenerate boundary line segment. Co-adapted standard Brownian noises represented by predictable J,K with J-transpose J+K-transpose K=I; normal reflection. Fixed epsilon>0, compact epsilon-separated pair set; pole outside closure; delta>0 chosen after epsilon,p,D.
- Transfer limits: Theorem8 general planar flat-boundary multiple-pole argument remains source-stated and unqualified by this row; no arbitrary/non-coadapted impossibility, sharp meeting time or Neumann spectral-tail inference. Lemma5 constants depend on epsilon and potential.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch04_admissions.json /rows/6 (SHA-256 89460135e979ee042b782dcc5d87d4c5a1cf30b149432aeecd0b5a1f199e7a1d); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-49b1b6d0cdd1/usage_card.md`） (SHA-256 f3f683a18ce97ab532dd19d87ec1d4a4b86d9e8cd20bd94a7b5ffac61f67791e); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-49b1b6d0cdd1/review_record.json`） (SHA-256 183f0a1bdc90137a3bab9bb8069801a48f7640638fc59dfe3c56cbaf0fd93d15).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 22. PR-574e5dc22806 — Coalescence of synchronous couplings

- Work/version: paper; UW repository PDF, full 31-page copy.
- Source PDF: workers/W08/papers/burdzy_chen_coalescence_sync.pdf (SHA-256 1ca885d3d928a3a5e934ddbd03532e7dd48dce7707c0eb97157a2f675fd4b966).
- Accepted method: Separated-wedge synchronous contraction interface in Lemma3.4: scale-invariant two-side forcing contracts distance by|cos theta|, while a reflected log-radius walk controls relative separation with probability q_m->1.
- Conditions: Wedge angle0<theta<2pi with theta not in{pi/2,pi,3pi/2}, so0<|cos theta|<1. Exact stopped synchronous wedge pieces and restart hypotheses(i)–(vi) physical23 retained; initial separation at inner radius <=2^(-m) times radius. Between restarted pieces require source(vi) nonincrease under ratio<=1/2.
- Transfer limits: Only the substantive wedge lemma in its displayed nonexceptional-angle case, no full arbitrary-polygon Theorem1.1(i), no lip-domain/eigenfunction Theorem1.1(ii), no unproved geometric special-angle cases, finite meeting or exact convergence rate. Whole-domain use needs every restart/recurrence/local-geometry hypothesis rechecked.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch04_admissions.json /rows/7 (SHA-256 89460135e979ee042b782dcc5d87d4c5a1cf30b149432aeecd0b5a1f199e7a1d); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-574e5dc22806/usage_card.md`） (SHA-256 f4869b3672ce2934adf9f1e3d1c5501ed1e37ef8954f11c4bafe4ea2b57acbb8); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-574e5dc22806/review_record.json`） (SHA-256 7e28298a89192a3fa96014e9111ad6039948f4f65fe4040efb89bb8f56b0fa22).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 23. PR-4ee08358cb44 — Neumann eigenfunctions and Brownian couplings

- Work/version: paper; UW repository PDF, 13-page review copy.
- Source PDF: workers/W08/papers/burdzy_neumann_brownian_couplings_review.pdf (SHA-256 279a5ac504f45622b8500bdac161671ae1369f5026a95a5c617615fa6bcf5796).
- Accepted method: Use the authored13p review for the Delta-Neumann heat convention and its second-mode expansion, and for transferring an already established coupling/order inequality to a second-eigenfunction order in the source named convex-symmetric/lip classes. Mirror/scaling and time-change discussions are retained as method synthesis, not new primary construction proofs.
- Conditions: Bounded connected domain and the source regularity/spectral/initial-data hypotheses; nonzero second-mode coefficient, with eigenfunction sign matched to the comparison. Coupling must actually preserve the declared ordered pairs. Delta-heat rate is mu2; standard Brownian generatorDelta/2 rate is mu2/2. Local UW13p copy has no printed version date; publication association does not assert byte identity.
- Transfer limits: No generic acute-triangle tail, universal coupling existence, primary SDE proof, or spectrum-alone meeting-time upper bound. Domain-class summaries in a review are not substituted for the primary geometric hypotheses of R002.
- Method IDs: G16.03, G16.02.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch01/admissions.json /rows/3 (SHA-256 ee64345c07f9fdf306dd0f06dd33d0ead0c11b479072b0bba03fa7a9fbead63e); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-4ee08358cb44/usage_card.md`） (SHA-256 4eb00dcddc0d18e382cbdd8a9cec9e29a166f425ddfe6b873a406e1d52ccd98a); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-4ee08358cb44/review_record.json`） (SHA-256 88b76bc41a8516ef5f911d9534a604eda9921b8761f74185db9d475a03008fd2).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 24. PR-433e9f5c54e5 — Conformal invariance of planar loop-erased random walks and uniform spanning trees

- Work/version: paper; arXiv:math/0112234v3, revised 10 Mar 2003; journal: Annals of Probability 32 (2004), 939–995.
- Source PDF: workers/W08/papers/lsw_conformal_lerw_ust.pdf (SHA-256 58038a74579c28d16e2d5265b2a0881b88f91c3dbdf27ad0ab0f1e802a71f7a4).
- Accepted method: Use Theorem1.1 for planar discrete LERW convergence in the unparameterized rho path metric to the conformal image of radial SLE2 in a proper simply connected D containing0. Retain separately Cor1.2 full wired/free UST scaling-limit existence and conformal invariance with C1 Jordan boundary, and Theorem1.3 mixed wired/free-arc Peano convergence to chordal SLE8.
- Conditions: Th1.1 requires proper simply connected D containing0, not smooth Jordan boundary; Cor1.2 has its own C1 smooth simple closed boundary and full-tree topology from Schramm11.3. Th1.3 uses its C1 Jordan domain, distinct endpoints and complementary wired/free boundary arcs with the specified lattice approximation. Driving-process convergence (Th3.7) is not sufficient alone: retain tightness/tameness and kernel continuity for Th3.9 path convergence.
- Transfer limits: No continuous Brownian-path loop-erasure construction, Brownian Jordan-arc infimum/dimension result, arbitrary network FSF/WSF result, or automatic extension from simply to finitely connected D.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/old_W08_high_batch01/admissions.json /rows/4 (SHA-256 ee64345c07f9fdf306dd0f06dd33d0ead0c11b479072b0bba03fa7a9fbead63e); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-433e9f5c54e5/usage_card.md`） (SHA-256 28f3f3372b3aa91d62e5d7c3c63f19872e8eec5a2088f1f17aa1f0f63bd46dd9); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-433e9f5c54e5/review_record.json`） (SHA-256 fb7f100a61e00e8a2a498e43453d04304c0e1ab05fd5c4762595f41ece9d0cc3).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 25. PR-ed6f76bd51c7 — The scaling limits of planar LERW in finitely connected domains

- Work/version: paper; arXiv:math/0610304v3, revised 21 Apr 2008; journal: Annals of Probability 36(2) (2008), 467–529.
- Source PDF: workers/W08/papers/zhan_lerw_finitely_connected.pdf (SHA-256 bfb386fc4a8b4f9b17e7b01eb6c8c2a819ed62998a4aa30e4dc65f94c633e5a8).
- Accepted method: Normalized generalized Poisson-kernel observable for interior-target continuous LERW in finitely connected domains is a local martingale (Theorem4.1), via explicit cancellation of the tip pole in Lemma4.1.
- Conditions: Finitely connected D, starting prime end w0, interior target z_e; conformal almost-H representation Omega bounded by real boundary plus disjoint analytic Jordan holes. Given maximal Loewner solution dxi=sqrt2 dB+2X_t dt, X_t=partial_x partial_y J_t/partial_y J_t atxi, J_t=Green(Omega\K_t,p;.) composed with inverse Loewner map. P_t is the generalized Poisson kernel at the tip normalized byP_t(z_e)=1. Stop before target, test point or geometric singularity; local martingale statement only.
- Transfer limits: No full discrete-to-continuous convergence Theorem4.2 audit, maximal-solution Theorem3.1 proof upgrade, other-target boundary/lattice assumptions, Brownian continuous loop-erasure existence/uniqueness, dimension equality, radial whole-curve dimension transfer, or Jordan-arc infimum. This row has a substantive local potential/martingale use and does not claim every old-card theorem high.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch05_speed_delta/admissions_v2.json /rows/0 (SHA-256 742ba02fcaaef1081045b8917dd28d1fd135227bedb4048396f7def04c4d1e43); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-ed6f76bd51c7/usage_card.md`） (SHA-256 edb6c5998e60aed779f029f5747d6719414800709a1736bfdc6ff4bf26d7bff2); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-ed6f76bd51c7/review_record.json`） (SHA-256 fa92ad6b710452fcd0fc9b24c83d299245566dc6a1ed96a516d7000a8ca6f608).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 26. PR-455d793d0df2 — Shy couplings, CAT(0) spaces, and the lion and man

- Work/version: paper; arXiv:1007.3199v4, 15 Mar 2013; published Annals of Probability 41(2) (2013), 744–784, DOI 10.1214/11-AOP723..
- Source PDF: workers/W08/papers/bramson_burdzy_kendall_shy_cat0.pdf (SHA-256 3b40baa61eb82ee9ec51834d4a7d20e57b731f2a36700b3a8dd4050429702b2f).
- Accepted method: Proposition17 deterministic greedy pursuit in a bounded CAT(0) domain: uniform finite epsilon/2-capture, with an explicit upper bound from intrinsic diameter and a total-curvature comparison.
- Conditions: D bounded in Euclidean space and CAT(0) in its intrinsic metric; uniform exterior-sphere radiusr and locally translated uniform interior-cone radiusdelta,anglealpha as Definitions6/8. LetDelta=diam_intr(D)<infinity. Man follows a measurable reflected control with speed at most1; lion has unit velocitychi along the unique intrinsic geodesic toward the man, until capture. Require the source geodesic regularity/first-variation framework (Propositions12,14,15). For0<epsilon<2Delta the explicit t_c=q_c² below applies; larger epsilon gives immediate capture.
- Transfer limits: Only deterministic Proposition17 with the actual intrinsic-metric diameter. Full stochastic Theorem1/2, Proposition18 drift limit, Proposition20 uniform probability and Lemma19 projected-Lipschitz route remain unqualified; no source-error verdict or repair of those parts. No non-coadapted impossibility, Euclidean-only diameter constant, finite exact meeting or sharp spectral tail follows.
- Method IDs: legacy Brownian module; no G16 ID assigned on this row.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch05_speed_delta/admissions_v2.json /rows/1 (SHA-256 742ba02fcaaef1081045b8917dd28d1fd135227bedb4048396f7def04c4d1e43); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-455d793d0df2/usage_card.md`） (SHA-256 f172e88eae9e77daf3d4bed451ff9ca2c07bf823e9c4b3ad999a404958a6a198); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-455d793d0df2/review_record.json`） (SHA-256 8ddac6f1004c8c3dca6e7323841043218a910a6844f84e9791fd37043c4294c0).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 27. EXSRC-2f6b5402637cac53 — Stochastic Differential Equations for Multi-dimensional Domain with Reflecting Boundary

- Work/version: paper; Springer journal full text, Probab.TheoryRelat.Fields74(1987):455–477, DOI10.1007/BF00699100,23physical pages..
- Source PDF: expansions/20261115/downloads/D03/papers/L08_Saisho_1987_Springer_journal_fulltext.pdf (SHA-256 2f6b5402637cac5312e823829187279437f323b417ae978245bfa8eb5770d07f).
- Accepted method: Use Theorem4.1 for the unique continuous normal Skorokhod solution for every continuous input started in closure(D), and Theorem5.1 for the unique strong individual reflected SDE after checking the exact normal-set geometry and bounded Lipschitz coefficients.
- Conditions: ConditionA: one r0>0 with N_x=N_(x,r0)!=empty for every boundary x. ConditionB: delta>0,beta>=1 and a unit l_x at each boundary point with l_x dot n>=1/beta for every normal at the specified nearby boundary points. Regulator is continuous, finite variation on compacts, normal-directed and boundary-supported. The SDE has the stated Brownian filtration/initial condition and bounded Lipschitz sigma,b. Bounded continuous coefficients alone support only the weaker weak-existence remark.
- Transfer limits: Normal single-particle well-posedness is not a joint coupling, arbitrary oblique reflection theorem, Neumann generator identification or spectral-tail theorem.
- Method IDs: G16.01.
- Authority: expansions/20261115/reviews/R08/admissions/L08_accepted7_batch06.json /rows/9 (SHA-256 5d279ec65b0c4b3316333e20c823940372895f06ee8568a054d084e2be7feda9); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/EXSRC-2f6b5402637cac53/usage_card.json`） (SHA-256 e0fedc847681717346e8f69235fa956999d303541b258a765f5cd18cde0c6585); independent review（本机附件：`references/evidence/use_scope_snapshots/EXSRC-2f6b5402637cac53/review_record.json`） (SHA-256 c10dd21ed0fcdadf7c21000d9c32238e3042f81aede76e7bea4a5cd08246844d).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 28. EXSRC-4265613ad6a3f726 — On Neumann eigenfunctions in lip domains

- Work/version: paper; Complete 30-physical-page author manuscript, title page dated December 17, 2001 and revised January 2004. Its corresponding published article is Journal of the American Mathematical Society 17(2) (2004), 243–265, DOI 10.1090/S0894-0347-04-00453-9. The local object is not the publisher PDF; no byte/text equivalence is claimed..
- Source PDF: expansions/20261115/downloads/D03/papers/L08_Atar_Burdzy_2004_Neumann_eigenfunctions_Lip_domains_UW.pdf (SHA-256 4265613ad6a3f726f3f7880deca3e2d41d83de8454811f4e3d0cec017c0aa83f).
- Accepted method: Derived unit-disk mirror pair, source Section2/Eq8 physical5-10 with R07 independently verified repair: bounded globally Lipschitz off-diagonal G_n on product normal-reflection domain, stopped consistency, global predictable orthogonal K, Z=integral KdW and Y=Gamma(y+Z). Both full coordinate path laws are standard normal-reflected Brownian motion in the same filtration; selected construction is W-strong/pathwise unique and stays together after a finite meeting if one occurs.
- Conditions: Exact30p UW revised author manuscript, no published-byte equivalence; full reader1-30 coverage/unique immutable grant and all delta hashes verified. Closed unit disk, fixed deterministic distinct starts. Full Saisho A with r0=1 and nearby-all-normal B with delta1/4,beta2sqrt2 on the4D product; bounded Lip cutoff G_n agrees with I-2vvT/|v|^2 for |v|>=1/n, nonzero v only in untruncated formula. Zero-column4x4 noise padding, unused-noise removal, global orthogonal K and correct Z_zeta+W_t-W_zeta patch are essential.
- Transfer limits: The printed universal adapted-driver Lemma1 fails the fixed interior linear-input t4<=Ct5/5 test and the local p10 display omits Z_zeta (Eq8 itself correct), both independently confirmed by R07. Only the derived disk route is admitted. Generic domain/corner/Picard/strong-Markov/lip-order/spectral proof, finite meeting or a meeting-tail upper bound are excluded. This selected coadapted construction imposes no restriction on unrestricted coupling classes.
- Method IDs: G16.02.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch06_four_rebind/admissions.json /rows/1 (SHA-256 8ff96a4a8c1cddbaad0c89f5ca899a10f31e4ca3b7eef9b073e7344f3601e56a); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/EXSRC-4265613ad6a3f726/usage_card.md`） (SHA-256 f0a5abf8a6d866bb8b7b356c4edb70fb1229ee0f6de92085c5415dbaff709c06); independent review（本机附件：`references/evidence/use_scope_snapshots/EXSRC-4265613ad6a3f726/review_record.json`） (SHA-256 7967057f52ee63b6fc4833e6cf19289257da37c28afba57369358d0a2a53da53).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 29. EXSRC-4c3fe3f31e76b954 — Pathwise uniqueness for reflecting Brownian motion in certain planar Lipschitz domains

- Work/version: paper; Complete arXiv:math/0510473v1 dated21October2005, local title Pathwise uniqueness for two dimensional reflecting Brownian motion in Lipschitz domains,5physical pages. Related ECP11(2006):178–181 journal title/DOI recorded; no local/journal text or byte equivalence asserted..
- Source PDF: expansions/20261115/downloads/D03/papers/L08_Bass_Burdzy_2006_author_preprint_arxiv_math0510473.pdf (SHA-256 4c3fe3f31e76b9540edf72bd30f8c37ee141479aadbde0b2dcfe008add73a95a).
- Accepted method: Use Theorem1 as a precise planar normal-reflection pathwise-uniqueness comparator when each boundary point admits a suitable local graph of Lipschitz constant<=1. The source selector/law proof also yields strong existence and allows candidate solutions with different filtrations.
- Conditions: Dimension2; normal reflection; same initial state and same Brownian path for the uniqueness comparison; a suitable constant<=1 local graph exists at every boundary point (not all arbitrary rotated charts). Each candidate is adapted with its driver Brownian in the declared filtration; boundary local time is continuous nondecreasing, boundary-supported and does not charge surface-null boundary sets.
- Transfer limits: The source compares same-start solutions and constructs no distinct-start two-particle coupling. It proves no Neumann spectral estimate or meeting/survival-tail upper bound. The wedge minimax calculation is a separate derived geometric argument, verified by local SymPy algebra and an explicit monotonicity proof.
- Method IDs: G16.01.
- Authority: expansions/20261115/reviews/R08/admissions/L08_accepted7_batch06.json /rows/13 (SHA-256 5d279ec65b0c4b3316333e20c823940372895f06ee8568a054d084e2be7feda9); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/EXSRC-4c3fe3f31e76b954/usage_card.json`） (SHA-256 b332ca29e66c033a277191f38ef8297c827dc1532337c2deef5887f0ee29d3e6); independent review（本机附件：`references/evidence/use_scope_snapshots/EXSRC-4c3fe3f31e76b954/review_record.json`） (SHA-256 c10dd21ed0fcdadf7c21000d9c32238e3042f81aede76e7bea4a5cd08246844d).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 30. EXSRC-61f38f6c62e9c593 — An Invariance Principle for Semimartingale Reflecting Brownian Motions in Domains with Piecewise Smooth Boundaries

- Work/version: paper; Exact40p arXiv0704.0405v1 electronic reprint. Ann Appl Prob17(2),741–779(2007), DOI10.1214/105051606000000899; first page explicitly distinguishes pagination/typography, no journal-byte equivalence..
- Source PDF: expansions/20261115/downloads/D03/papers/L08_Kang_Williams_2007_invariance.pdf (SHA-256 61f38f6c62e9c5931926c02b89f5df160082a1894572cbaaa689a4005dc20119).
- Accepted method: Fixed nondegenerate convex triangle represented by minimal halfplanes, constant inward unit face normals: singleton margin1 and vertex equal-weight margin sin²(alpha/2)>0 verify A5/Ass5.1. Th5.1 gives single-marginal weak existence with specified drift, strictly positive-definite covariance and starting law. Full Ass4.1 plus(vi)′,(vii) yield Th5.4 state-law convergence of qualified approximations. Th4.1 provides the localized state/regulator oscillation bound with its D-threshold.
- Conditions: A1–A5; unit globally Lipschitz fields; rho<min{rho0/4,R(a/4)/4},delta<rho/2; localized reflected equation, face-tube regulator support and small jumps; D(Pi(Osc+delta))<rho/2. Approximation state errors vanish and regulator-error TOTAL VARIATION vanishes, fields converge nearby uniformly, driver C-tight. Brownian driver law(vi)′ and centered-driver martingale in the LIMIT TRIPLE FILTRATION(vii) are separate. Uniqueness(viii) is only of W law. Extended SRBM is the whole triple satisfying all Definition2.1 conditions including(iii), not an ESP relaxation.
- Transfer limits: Near-domain paths alone, Brownian marginal law alone or vanishing regulator-error amplitude without vanishing total variation do not meet the theorem gates. Nonconstant fields are outside5.4. No two-start construction, transformed pair noise, Neumann generator/spectrum identification, coalescence or meeting-tail conclusion follows.
- Method IDs: G16.01.
- Authority: expansions/20261115/reviews/R08/admissions/L08_pending3_KW_method_id_correction.json /rows/0 (SHA-256 9c4eab22b213871a02419769d00ce6eba6cd742e58989b02f71d5ea52e200a88); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/EXSRC-61f38f6c62e9c593/usage_card.json`） (SHA-256 bd2ab529e6f8255dd817bc3d3277d0b07bd0208ebb87e08930f2036b963b23b0); independent review（本机附件：`references/evidence/use_scope_snapshots/EXSRC-61f38f6c62e9c593/review_record.json`） (SHA-256 860ff733b7dc726f8efbeec85b173b2a768ea06ed36bfc28871f3d58f59cf30b).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 31. EXSRC-62f2ce007b957ddb — On the noncoalescence of a two point Brownian motion reflecting on a circle

- Work/version: paper; Complete Numdam digitized archival copy of Annales de l’Institut Henri Poincaré, section B, 25(2) (1989), printed pages 99–107. The 10-physical-page local PDF has a Numdam title/copyright cover at physical p. 1 and the nine article pages at physical pp. 2–10. Original Gauthier-Villars copyright/terms notice is retained; no DOI identified..
- Source PDF: expansions/20261115/downloads/D03/papers/L08_Cranston_LeJan_1989_noncoalescence_circle_Numdam.pdf (SHA-256 62f2ce007b957ddbc247ae1dc03c4f57f8fedc32cc0d3c3971de1e96be7984e3).
- Accepted method: Theorem1 physical7/printed104: for any fixed unequal starts in the closed unit disk, two strong normal-reflection solutions driven by the SAME planar Brownian path never meet at any finite time almost surely. Yet z=|X1-X2|/2 <=z0 exp(-(phi1+phi2)/2) and (phi1+phi2)/t ->2, so limsup log z/t <=-1. This is a rigorous method-selection obstruction: spatial contraction does not imply synchronous finite coalescence.
- Conditions: Exact10p archival Numdam object: cover1/fullarticle2-10, immutable grant/file/internal digest and reader coverage all verified. Unit disk, normal reflection, continuous supported individual regulators, fixed unequal starts, common usual Brownian filtration. Rotating coordinates and logarithmic harmonic-function argument are stopped before first meeting; two full marginal laws correct.
- Transfer limits: For this specified synchronous pair P(T>t)=1 at every finite t. This does not refute mirror/maximal/unrestricted successful couplings, gives no polygon/triangle corner theorem, and does not transfer the unbounded exterior result. No post-meeting rule is reached; an exponential spatial-distance exponent is not a successful survival-tail upper bound.
- Method IDs: G16.02.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch06_four_rebind/admissions.json /rows/2 (SHA-256 8ff96a4a8c1cddbaad0c89f5ca899a10f31e4ca3b7eef9b073e7344f3601e56a); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/EXSRC-62f2ce007b957ddb/usage_card.md`） (SHA-256 0ef692006c4ea3fd4b81a163bda377a485485e600950f67868940ff5fbc88e84); independent review（本机附件：`references/evidence/use_scope_snapshots/EXSRC-62f2ce007b957ddb/review_record.json`） (SHA-256 735bd3578a8de8d43a69695ae96e46c13f4ff2ab7d38b25f8237c4c74b6b372a).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 32. EXSRC-9b3e5aee5d711232 — Mirror Coupling of Reflecting Brownian Motion and an Application to Chavel’s Conjecture

- Work/version: paper; Official EJP16(2011)paper18:504–530, DOI10.1214/EJP.v16-859,27physical pages..
- Source PDF: expansions/20261115/downloads/D03/papers/L08_Pascu_2011_mirror_coupling.pdf (SHA-256 9b3e5aee5d71123226f71f09072f0756fb819f9df68caeabbb1ec48f5154d73f).
- Accepted method: Theorem3.1 supplies a particular strong coadapted mirror pair under strict inner-closure nesting and convex inner domain, with orthogonal predictable second driver and correct reflected marginal laws; the conditional interposed-ball comparisons in Theorems5.3/5.4 give a separate Neumann heat-kernel interface.
- Conditions: For Theorem3.1, closure(D2) subset D1 with positive boundary separation, smooth bounded domains, convex D2, planar piecewise-C2 convex corners or C2 boundary for d>=3, and arbitrary initial points in the respective closures. G(z) is the orthogonal reflection off zero and G(0)=I; the construction selects a sticky solution but this coefficient also admits nonsticky solutions. Theorems5.3/5.4 retain their own printed D2 subset B subset D1 ball condition centered at x or y, with convex or appropriately star-shaped D2.
- Transfer limits: Theorem3.1 does not include the same-domain case, which is separately recalled in section2/Remark3.2. G(0)=I alone does not uniquely select stickiness. Heat-kernel comparison does not give a matching exponential coalescence-tail upper bound or optimize over unrestricted couplings.
- Method IDs: G16.02, G16.03, G16.05.
- Authority: expansions/20261115/reviews/R08/admissions/L08_accepted7_batch06.json /rows/11 (SHA-256 5d279ec65b0c4b3316333e20c823940372895f06ee8568a054d084e2be7feda9); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/EXSRC-9b3e5aee5d711232/usage_card.json`） (SHA-256 1ee641bbb9b9f6a3490235901001d25bb1c699f15e60601ccf750cddbaf6dd48); independent review（本机附件：`references/evidence/use_scope_snapshots/EXSRC-9b3e5aee5d711232/review_record.json`） (SHA-256 c10dd21ed0fcdadf7c21000d9c32238e3042f81aede76e7bea4a5cd08246844d).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 33. EXSRC-cd55a9e0f1e0c2d0 — Invariant Wedges for a Two-Point Reflecting Brownian Motion and the “Hot Spots” Problem

- Work/version: paper; Complete official Electronic Journal of Probability version, volume 6 (2001), paper 18, printed pages 1–19, DOI 10.1214/EJP.v6-91; published June 14, 2001. The acquired object is the EJP PDF served from the journal’s EMIS archive, not a separate preprint..
- Source PDF: expansions/20261115/downloads/D03/papers/L08_Atar_2001_invariant_wedges_two_point_reflected_BM_EJP6_18.pdf (SHA-256 cd55a9e0f1e0c2d044ac0f87ddc4a878029ac692d38508d417bfb7cebc49ea44).
- Accepted method: Exact rectangle D=(0,1)x(0,2), V=R_+^2: Conditions2.1-2.3 use primitive smooth-piece normals +/-e1,+/-e2 and normalized active nonzero normal cone at corners; Theorem2.2/Cor2.1 preserve coordinatewise order for same-W normal reflected Brownian paths. Explicit phi=-cos(pi*y/2) is the simple first positive Neumann mode, eigenvalue pi^2/4 for -Delta and decay pi^2/8 for Delta/2.
- Conditions: Exact official EJP19p; unique grant file and internal record digests separately verified, full reader1-19 coverage. Fixed bounded connected rectangle with normal reflection; correct two full marginal path laws and Brownian W in the common filtration. Proper closed convex full-dimensional wedge, W(D) empty, each primitive-face tangent projection invariant, strict dual gamma=(1,1). All active normal combinations normalized only when nonzero.
- Transfer limits: This row is the concrete rectangle/order/explicit-mode use. No arbitrary acute-triangle geometry, generic spectral simplicity, finite meeting or matching tail upper bound follows. Source abstract cone theorem actually requires closure(K-K)=E (original overbars confirmed); no generation gap is asserted, but generic Th3.1 operator route is not needed or included in this row. Projection failure n=(1,1)/sqrt2 sends e1 to(1/2,-1/2); strict positivity also fails for cones containing an opposite nonzero line.
- Method IDs: G16.02, G16.03.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch06_four_rebind/admissions.json /rows/0 (SHA-256 8ff96a4a8c1cddbaad0c89f5ca899a10f31e4ca3b7eef9b073e7344f3601e56a); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/EXSRC-cd55a9e0f1e0c2d0/usage_card.md`） (SHA-256 ade01b9d53f6fb01e9f74fe6687c2d54d06baf4e9ed086e140d72023707a81f1); independent review（本机附件：`references/evidence/use_scope_snapshots/EXSRC-cd55a9e0f1e0c2d0/review_record.json`） (SHA-256 0c8d45eb1c6a0e738c0465012e267591f7215b3964663d8b56742d576b667e1e).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 34. EXSRC-ef5251d44e6ca12e — Simultaneous boundary hitting for a two point reflecting Brownian motion

- Work/version: paper; Complete Numdam digitized archival copy of the Springer print chapter in Séminaire de Probabilités XXIII, Lecture Notes in Mathematics 1372 (1989), printed pages 234–238. Springer lists the digitized chapter online in 2006; the local object is the 1989 print chapter scan with its archive cover, not a later author preprint..
- Source PDF: expansions/20261115/downloads/D03/papers/L08_Cranston_LeJan_1989_simultaneous_boundary_hitting_Numdam.pdf (SHA-256 ef5251d44e6ca12e3f850749413a7a566f479ddc1e9f2e9d07b808540046eea9).
- Accepted method: Exact5-article-page theorem (physical2/printed234): fixed unequal-start unit-disk normal-reflection pair with the same planar Brownian input almost surely hits the product boundary ∂D×∂D. In the rotating pair coordinates, this is y=0 and x^2+z^2=1 (the auxiliary crease). This joint-boundary event coexists with the companion noncoalescence theorem.
- Conditions: Exact6p archival object cover1/fullnote2-6, independent unique grant and complete reader coverage verified. Disk rotation symmetry and normal reflection; same Brownian filtration yields two correct full marginal path laws. Explicit dependency on the separate exact10p noncoalescence admission. Correct weighted distance integral has1/2 and bound2z0; independently derived small-z harmonic Ito domination is fully derived in R08 proof.
- Transfer limits: Simultaneously located on the two boundaries does NOT mean the two original regulator measures charge simultaneously or overlap; auxiliary crease local time is distinct. The companion theorem supplies T=infinity, so there is no finite coupling-time tail. No arbitrary polygon vertex/triangle, different coupling class, or universal coadapted restriction follows.
- Method IDs: G16.02.
- Authority: expansions/20261115/reviews/R08/continuation_20261116/batch06_four_rebind/admissions.json /rows/3 (SHA-256 8ff96a4a8c1cddbaad0c89f5ca899a10f31e4ca3b7eef9b073e7344f3601e56a); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/EXSRC-ef5251d44e6ca12e/usage_card.md`） (SHA-256 5917cc51c8a9eced86fe1c0eef95b7a2f5a4fd9c4a5699d9e2c69211f5fac865); independent review（本机附件：`references/evidence/use_scope_snapshots/EXSRC-ef5251d44e6ca12e/review_record.json`） (SHA-256 74afcad19158c03d1b9e1517738f141fa4d89281de7093eaae090f821bb1cf7e).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

### 35. PR-dbf8c65c554f — Existence and Uniqueness of Semimartingale Reflecting Brownian Motions in Convex Polyhedrons

- Work/version: paper; Full40-page author-hosted1995 article associated with TheoryProbab.Appl.40(1):1–40, DOI10.1137/1140001. The separately hashed2005 two-page correction is compulsory companion support, not another work..
- Source PDF: workers/W14/data/dai_williams95_srbm.pdf (SHA-256 aaa759a14a0a6a584bbfb32aec84e3e0e46412b834e22917ae6d7e74af3fc742).
- Accepted method: For the exact convex-polyhedron SRBM model satisfying Assumption1.1, use Theorem1.3 to obtain existence and unique law of(state,regulator), Feller continuity and strong Markov property before designing a joint coupling.
- Conditions: Positive-definite covariance Gamma, specified drift theta, face-reflection vectors v_i, inward normals n_i and continuous adapted nondecreasing face regulators. For every maximal active-face set K require both S.a: v=sum a_i*v_i, all a_i>0, n_i dot v>0; and S.b: eta=sum c_i*n_i, all c_i>0, eta dot v_i>0. The corrected decomposition needs sufficiently small epsilon; corrected oscillation estimate needs input oscillation<=delta. For nonsimple polyhedra sufficiency is proved; necessity is not asserted.
- Transfer limits: Single reflected law only; no correlated two-particle noise construction, no automatically valid common filtration, no identification with the desired Neumann semigroup and no coupling-tail estimate.
- Method IDs: G16.01.
- Authority: expansions/20261115/reviews/R08/admissions/L08_accepted7_batch06.json /rows/5 (SHA-256 5d279ec65b0c4b3316333e20c823940372895f06ee8568a054d084e2be7feda9); decision accepted_for_scoped_use.
- Packaged scope evidence: usage card（本机附件：`references/evidence/use_scope_snapshots/PR-dbf8c65c554f/usage_card.json`） (SHA-256 a2c4a5625937914adadcd829f7da1ad55127fe4e48cee74809ed955e7578601e); independent review（本机附件：`references/evidence/use_scope_snapshots/PR-dbf8c65c554f/review_record.json`） (SHA-256 38071b4c02b5f83e92c74de36b15580afbdcda2728821c305468f4ec79ed2426).
- Reading basis: canonical_complete_read_reuse; new global-read credit in this continuation is 0.

## Current held works

The five current held works are M0171, M0175, M0192, M0201, and W08-R003 general Lambda. Exact dispositions are preserved in held_and_historical_dispositions.json（本机附件：`references/held_and_historical_dispositions.json`）. M0196 Proposition 1 is separately admitted by R14 and adopted by R08; the earlier held row is historical, not a sixth current hold. W08-R003 has a separate pre-existing disk-only scope recorded as historical bounded use; it adds no work to the current 35-row tally.

## Use rule

Use an admitted statement only with its listed hypotheses and conclusion. Where a proof dependency or transfer is not included in the scope, mark it as unresolved. No source entry grants transfer to a different path set, coupling class, stopping rule, exponent, dimension, geometry, or theorem.

## Relocated evidence closure

This candidate carries the exact bytes for the 35 admitted source PDFs, the required correctional-note companion, and the selected read, scope, proof, high-review, rebind, math, and STANDARD35/compiler evidence. The files are stored below `references/evidence/closure/`; `migration_closure_index.json`（本机附件：`references/evidence/migration_closure_index.json`） maps every original `(path, SHA-256)` to the package-local copies. Copy aliases preserve their verified preimage SHA and explicitly record when a current original path changed. Candidate08 remains immutable.
