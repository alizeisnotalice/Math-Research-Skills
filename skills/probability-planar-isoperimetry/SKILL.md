---
name: probability-planar-isoperimetry
description: Analyze isoperimetric profiles and curvature methods on planar graphs or tessellations when the boundary statistic, embedding, and theorem hypotheses can be matched.
---

# Planar graph isoperimetry and discrete curvature

This portable candidate has one active entry, this root `SKILL.md`; its evidence and references are adjacent package files. Use it only after specifying the graph, embedding, set family, and exact boundary statistic. A theorem about one statistic is not automatically a theorem about another. The reviewed source map below contains 30 narrowly admitted works; it does not settle the unrestricted outer-vertex profile A023, the conditional count A022, or the unrestricted infection interface A193.


## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).

## Name the boundary before using a theorem

For a finite vertex set S in a graph, distinguish at least:

- Crossing-edge cut: |E(S,V minus S)|.
- Outside-vertex boundary: |N(S) minus S|.
- Inside/occupied vertex boundary: vertices in S with a neighbour outside S.
- Tile-edge perimeter: tile-interface edges, with hole boundaries and multiplicity stated.
- Outside-cell site perimeter: distinct exterior cells sharing a side with the set.
- Occupied-cell/internal boundary: occupied cells adjacent to an exterior cell.
- Face boundary or contour length: specify primal or dual edges and how bridges, holes, and repeated traversals count.

Do not convert these by visual analogy. Prove any conversion with degree, multiplicity, component, and hole terms. An edge-isoperimetric estimate does not automatically give an outside-neighbour vertex estimate.

## Workflow

1. State the finite-set domain: arbitrary, connected, induced-connected, hole-free, edge-connected animal, or a named tessellation ball.
2. Give the plane embedding and local-finiteness assumptions. For a hyperbolic claim, fix the regular tessellation {p,q} and its parameter range.
3. Define the counted boundary, normalization, weights, and whether the denominator uses vertices, degree-volume, cells, or faces.
4. For an exact profile, prove a lower bound for every set in the domain and a matching upper witness at each claimed size. Balls supply a candidate upper bound on an infimum; they do not prove the lower bound.
5. Use Euler, curvature, duality, compression, recurrence, or Cheeger methods only with their exact hypotheses. Keep cited external inputs visible.
6. Check singletons, bridges, disconnected sets, holes, and terminal layers. Keep finite computation separate from proof.

## Six method interfaces

### G17.01 — Euler formula and discrete Gauss–Bonnet curvature

For a finite connected plane graph use V−E+F=2 with the unbounded face included, or V−E+F_b=1 with bounded faces only. Write face-degree incidences and internal/boundary vertex-degree sums separately. For holes or multiple components use the correct Euler characteristic. State whether curvature is ambient vertex curvature, induced-subgraph curvature, corner curvature, or boundary turn, and keep boundary corrections explicit.

### G17.02 — Planar duality and contour encoding

Name primal and dual edges and account for components, holes, bridges, orientation, and repeated contour traversals. A medial or dual circuit can encode a cut under precise hypotheses without giving a profile for all finite sets.

### G17.03 — Compression, shifting, and extremal-set structure

Prove cardinality preservation, nonincrease of the named boundary, and termination on the specified graph. Then prove that the target family is globally extremal on the claimed domain. A grid compression does not transfer automatically to another lattice or hyperbolic tessellation; an extremal-shape argument is not itself a compression theorem.

### G17.04 — Boundary recurrences for finite connected sets

Specify the layer or erosion operator, prove its exact increment or decrement under the stated hypotheses, and handle the starting and terminal cases. A recurrence for balls or convex lattice polygons is not an all-set recurrence.

### G17.05 — Cheeger inequalities and isoperimetric profiles

State the boundary denominator, measure, weights, and finite/infinite-set domain. For an exact constant prove both a universal lower bound and a matching sequence or exact finite profile. Keep edge Cheeger, degree-volume Cheeger, vertex boundary, and face profile distinct. A spectral conversion applies only after its measure, scaling, and generator hypotheses are checked.

### G17.06 — Geometric counting in hyperbolic tessellations

Fix {p,q}; distinguish vertex degree from face length, state the parameter range, and prove the count for that regular tessellation. Do not infer a result for arbitrary planar graphs or different face degrees. A tile-edge formula is not an outer-vertex profile.

## Accepted source interfaces

The following 30 works have accepted scoped-use rows in R09 union02. Each entry records only the admitted row. The exact union rows, source PDFs, reading records, independent reviews, use cards, and count freeze are locally mapped in the source index（本机附件：`references/source_index.json`）, method coverage（本机附件：`references/method_coverage.json`）, identity and count ledger（本机附件：`references/identity_count.json`）, book-unit record（本机附件：`references/book_usage.json`）, and origin-to-package map（本机附件：`evidence/origin_to_portable_map.json`）. Method memberships are G17.01: 12; G17.02: 12; G17.03: 4; G17.04: 9; G17.05: 25; G17.06: 10.

### PR-2c3e49004da9 — Self-avoiding walks and polygons on hyperbolic graphs

Christoforos Panagiotis (2024). DOI: 10.1002/jgt.23087. Methods: G17.01, G17.02, G17.04, G17.06. Exact local version: arXiv1908.00127v2,25Aug2022; exact35physical-page object.

**Admitted interface.** Panagiotis Theorem6, physical pp9--16: SAP boundary inner-chord/face-incident-inner-vertex inequality; Euler Lemma5.1, SAP-piece decomposition and auxiliary-forest overlap bound yielding the final minus-k.

**Conditions.** Finite connected plane S(d,k) region with outer self-avoiding polygon, simple bounded k-gonal faces, internal degree d, d,k>=3 and (d-2)(k-2)>4. (k-2)|ch(P)|+((d-2)(k-2)-3)|partial^V P|<=|P|-k; partial^V is inner face-incident boundary. F in Euler V-E+F=1 counts bounded faces.

**Transfer limits.** Only the explicit SAP/Euler/contour-incidence and finite decomposition subinterfaces; no discrete curvature/Gauss-Bonnet, general primal-dual theorem, all-finite-set outer PhiV, A022 conditional count or A193 arbitrary infection implication.

### EXSRC-324468617133ba10 — Isoperimetric Constants of (d,f)-Regular Planar Graphs

Yusuke Higuchi, Tomoyuki Shirai (2003). DOI: 10.4036/iis.2003.221. Methods: G17.02, G17.04, G17.05, G17.06. Exact local version: J-STAGE complete journal PDF 2003,8physicalpages.

**Admitted interface.** Higuchi--Shirai MainTheorem p2: exact normalized edge alpha and face alpha-star; face-ball recurrence upper bounds, independent all-finite-subgraph lower bound pp5--7 and regular primal/dual normalization.

**Conditions.** Assumption1.1 infinite connected simple standard (d,f)-regular Euclidean/Poincare tessellation; D=d-2,F=f-2. DF>4 gives alpha=(D/d)sqrt(1-4/(DF)),alpha-star=F sqrt(1-4/(DF)); DF4 standardEuclidean cases give0. Face-ball ratios approach the constants; finite attainment not asserted.

**Transfer limits.** alpha counts cut edges/degree-volume, alpha-star a source-defined face boundary/face count. Outer PhiV satisfies only alpha<=PhiV<=d*alpha; no exact A023PhiV, generic compression, curvature theorem, A022 or A193.

### EXSRC-a9452b71a206e994 — Explicit Isoperimetric Constants and Phase Transitions in the Random-Cluster Model

Olle Häggström, Johan Jonasson, Russell Lyons (2002). DOI: 10.1214/aop/1020107775. Methods: G17.01, G17.02, G17.05, G17.06. Exact local version: arXivmath/0008191v2,17Apr2001,28physicalpages; journal2002 metadata separate.

**Admitted interface.** HJL Theorems4.1/4.4 physicalpp17--20: beta(G)+delta(Gdual)=1 by Euler/filling and both orientations yield the exact edge-cut-per-vertex constant; Prop4.6 pp20--21 gives near-minimizing sequences only.

**Conditions.** Infinite proper plane regular graph degree d with locally finite regular plane dual degree f; standard tessellation/transitivity argument retained. iotaE=(d-2)sqrt(1-4/((d-2)(f-2))); beta=2/(d-iota),delta=2/(d+iota). All-finite vs large-connected infimum uses transitivity and cited external result[4], whose full proof is not newly read here.

**Transfer limits.** Euler branch only of G17.01; no Gauss-Bonnet, cardinality-preserving compression or ball minimizer theorem. iotaE/d<=PhiV<=iotaE leaves A023 open; no A022/A193. Printed random-cluster Th4.11 q>C application is quarantined: displayed proof establishes logq>C, not the printed weaker condition.

### PR-895a7396895c — Probability on Trees and Networks

Russell Lyons, Yuval Peres (2017). DOI: 10.1017/9781316672815. Methods: G17.01, G17.02, G17.05, G17.06. Exact local version: Author corrected/updated paperback PDF,19Aug2026,716physicalpages.

**Admitted interface.** PTN Chapter6 Theorems6.18/6.19 physicalpp217--219: exact edge-cut-per-vertex Cheeger constant and Euler primal/dual density proof; Th6.2 nonattainment p196 and p218Eq6.36 limiting-infimum consequence.

**Conditions.** Infinite proper plane regular graph degree d and regular dual degree q, both locally finite; section6.5 standard tessellation/transitivity hypotheses. PhiE(G;1,1)=(d-2)sqrt(1-4/((d-2)(q-2))); degree-volume version divides by d; zero in standardEuclidean product4 case.

**Transfer limits.** No exact outer PhiV: only PhiE/d<=PhiV<=PhiE. Euler use is not curvature/Gauss-Bonnet or compression/fixed-volume classification. Q6.20 displayed alpha_d is negative at d7 and is excluded; unproved cited special-case vertex and Oh degree-range results need primary audit. No A022/A193.

### PR-14b3349a4055 — Cheeger’s Inequalities for General Symmetric Forms and Existence Criteria for Spectral Gap

Mu-Fa Chen, Feng-Yu Wang (2000). DOI: 10.1214/aop/1019160118. Methods: G17.05. Exact local version: arXivmath/9804150v1,14Apr1998,21physicalpages; AnnProb2000 citation separate.

**Admitted interface.** Chen--Wang Theorem1.2 (1.11) physicalp3 and bounded specialization(1.12)p4 convert an already-proved Cheeger coefficient into a centered Poincare spectral-gap lower bound; proof pp6--8 and Lemma2.1 appendixpp19--21 checked.

**Conditions.** Probability pi, symmetric J, K0, form/domain hypotheses and scaling norm1.8. Finite connected simple d-regular graph d>=1 with uniform pi, J=pi*SRW P and r=s=M1 gives kprime=inf cut/(d|A|) for0<|A|<=N/2 and lambda1>=1-sqrt(1-kprime^2).

**Transfer limits.** Supporting known-profile-to-spectrum interface only, not a direct planar profile theorem. Same half-size family has PhiVhalf/d<=kprime<=PhiVhalf. No infinite-counting-measure A023 specialization, exact outer PhiV, extremizers, A022 or A193; lambda1 is Poincare gap, not absolute mixing gap.

### EXSRC-aba6f08d2edd69de — Duality Properties of Strong Isoperimetric Inequalities on a Planar Graph and Combinatorial Curvatures

Byung-Geun Oh (2013). DOI: not recorded in the accepted row. Methods: G17.01, G17.02, G17.05. Exact local version: Exact local arXiv1307.8033v1-stamped object30July2013,22physicalpages; internal typesetting date27Aug2018; no separately downloaded archive byte-equivalence asserted.

**Admitted interface.** Oh Theorem1(b) p2 proper-plane j-positivity duality via Euler/partition Lemmas8--12 pp8--15; Theorem3 p4 curvature-sign-to-inner-expansion criterion and pp15--16 explicit counterexample to omitting its vertex-curvature regularity guard.

**Conditions.** Connected simple graph embedded locally finitely in plane, simple dual, finite vertex/face degrees>=3, proper closed-disk faces. All subgraphs induced; simply connected means connected and G minus S one component. Upper averages over all such finite regions as relevant size tends to infinity. Negative upper edge/face curvature implies j>0; negative upper vertex curvature requires normality or bounded vertex degrees.

**Transfer limits.** j is inner-boundary/vertex-count, not pointwise outer boundary. Exact infimum relation j=h/(1+h) gives qualitative outer positivity from the criterion but no exact A023 constant. Woess[34] seed estimates remain an essential cited dependency; source transfer audited, external paper not newly fully read or credited. No self-contained Gauss-Bonnet identity, G17.06 tessellation-counting use, A022 or A193.

### EXSRC-9d893bd97537c651 — Sharp Isoperimetric Inequalities for Infinite Plane Graphs with Bounded Vertex and Face Degrees

Byung-Geun Oh (2020). DOI: 10.48550/arXiv.2009.04394. Methods: G17.01, G17.02, G17.04, G17.05, G17.06. Exact local version: Exact local 33-page PDF visibly stamped arXiv2009.04394v2,19Aug2024; internal typesetting date20Aug2024; D03 official-byte comparison inherited, not independently repeated by R09.

**Admitted interface.** Theorems5/7/8 pp11--15 distinct boundary-turn Gauss--Bonnet identities; Lemma9 pp16--19 and Theorem3 pp19--22 all-competitor inward-depth bounds; Theorem4 pp22--26 quasi-ball/hole-filling upper bounds. Theorem10 p28 is an exact outer-neighbor result only for triangulations; R09 separately expands its short proof.

**Conditions.** Connected simple locally finitely embedded infinite plane tessellation, each edge two distinct incident faces, normal intersections and finite polygon faces. p,q>=3,1/p+1/q<=1/2; Th3 minimum vertex/face degrees p,q; Th4 maximum degrees p,q. Phi(p,q)=(p-2)sqrt(1-4/((p-2)(q-2))). TypeI RHS chi(S); TypeII chi(D(S)open); TypeIII finite face graph, connected open interior, RHS2-m for induced-complement component count. Th10 triangular faces only, p>=6, respective min/max vertex-degree condition, outer j1=(p-6+sqrt((p-2)(p-6)))/2 on p-regular triangulations.

**Transfer limits.** Edge cut/vertex volume, degree-normalized edge ratio, face boundary walk and outside-neighbor vertices are distinct. Th3/4 are sharp across degree-constrained classes, not fixed-volume minimizers in every irregular graph. Th10 upper source proof leaves details to readers; independent completion recorded separately. No general q>3 outer profile, compression/G17.03, A022 or A193. Local-tessellation/infinigon extensions are separate and do not supply infinite-face quotients.

### EXSRC-ac3c8a6109a3185e — Site Percolation and Isoperimetric Inequalities for Plane Graphs

John Haslegrave, Christoforos Panagiotis (2021). DOI: 10.1002/rsa.20946. Methods: G17.01, G17.02, G17.04, G17.05, G17.06. Exact local version: Exact14-page WRAP-hosted Wiley-typeset journal PDF, DOI10.1002/rsa.20946,2020 online-first/2021 RSA58(1)150--163; legacy filename says AAM but version wording corrected; no arXivv2 equivalence asserted.

**Admitted interface.** Theorems4/5 p3, Lemmas15/16 pp9--10 and20/21 pp11--12, Corollaries17/22: Euler/disc completion and outerplanar overlap budget yield all-finite-set outer-neighbor lower bounds. Theorems18/23 pp10--13 give regular-ball recurrence sharpness by limiting ratios. Theorem6 pp4--6 separately gives a conditional site-interface criterion.

**Conditions.** Infinite connected simple locally finite plane graph without accumulation points. Every finite W: min vertexdegree d>=7 gives outer |partial W|>=alpha_d|W|, alpha_d=(d-6+sqrt((d-2)(d-6)))/2. Min vertexdegree d>=5 plus every facedegree>=4 gives alpha_(d+2). Regular triangulations/quadrangulations attain the infimum as ball-ratio limits. For interface pairs, C_infinity is ALL complementary components lying in occupied cluster Co unbounded face, even finite ones; B only neighbors in C_infinity. In triangulations M=d0(filled hull), not arbitrary holed Co. Th6 additionally needs uniform |M|<=a|B| and subexponential root-component volume f(|B|).

**Transfer limits.** Only known q3/q4 exact A023 subcases; general q>4 remains open. Euler/cut decomposition supplies G17.01, not generic curvature/GB. No finite-ball minimizer, compression/G17.03, A022 conditioned count or A193 arbitrary-infection interface. Face-degree>=4 excludes triangular faces, not all nonfacial3-cycles. Site threshold is not an implication from a Cheeger constant alone.

### EXSRC-74ab3d527c1bb1f1 — Curvature, Geometry and Spectral Properties of Planar Graphs

Matthias Keller (2011). DOI: 10.1007/s00454-011-9333-0. Methods: G17.01, G17.04, G17.05. Exact local version: arXiv1101.2970v1 visibly stamped15Jan2011; no publisher-byte equivalence asserted.

**Admitted interface.** Curvature with corner multiplicities and induced-subgraph Euler identity (Prop1 p7); Theorem1 pp8--15 curvature-to-local-tessellation copy/paste proof. Theorem4 pp19--20 ball adjacency/ordering via G1--G4 and explicit tessellation inputs; restricted derived |S_n|<=2|S_(n+1)| only. Theorem6(1),(3),(4) pp22--24 coarse crossing-edge Cheeger bounds from minimum vertex/face degrees and normalized/unnormalized curvature, with Ke/KP dependencies explicit.

**Conditions.** Connected topologically locally finite plane embedding. General corner definitions permit multiplicities; finite induced-region Euler use requires a nontrivial connected induced graph and includes its unbounded face, using recomputed induced curvature. Th1 alternatives: kappaC<=0; or simple G and kappaV<=0; or kappaF<=0 with regular extended edges/no terminals. Sphere geometry: global nonpositive corner curvature. Th6: simple G, global sup kappaV<=0, finite nonempty W subset U, cut edges join W to ALL V outside W. alpha_U=cut/ambient degree-volume; beta_U=cut/vertex count. p_U=inf_U degree, q_U=inf ambient face-degree touching U, unlike global suprema P,Q in C. alpha_U>=1-2q_U/[p_U(q_U-2)], beta_U>=p_U-2q_U/(q_U-2). alpha>=-2C sup_v(kappa(v)/degree(v)), beta>=-2C sup_v kappa(v), C=(1+2/(Q-2))(1+2/((P-2)(Q-2)-2)), with source infinity conventions and cited positive-RHS conditions; pointwise strict negativity yields beta>=alpha>0 using the uniform curvature gap.

**Transfer limits.** G17.04 is partial distance-sphere auxiliary support, not an arbitrary finite-connected-set boundary recurrence or optimizer theorem. Edge cuts, degree-volume, vertex-count and outer-neighbor statistics are distinct: no exact outer PhiV/A023, compression/G17.03, regular-family counting/G17.06, A022 or A193. Printed Th6(2) tail-INF statement is rejected as confirmed by independent R04; no silently corrected at-infinity interface is admitted. G5 quantitative vertex-curvature proof and dependent Th5 growth are excluded as unneeded source branches.

### EXSRC-80d8a7496b2b6067 — An isoperimetric inequality for planar triangulations

Omer Angel, Itai Benjamini, Nizan Horesh (2018). DOI: 10.1007/s00454-017-9942-3. Methods: G17.01, G17.04. Exact local version: ExactarXiv1604.05863v1stamp20Apr2016; separatetypesetting9Jul2018; no publisher-byte equivalence.

**Admitted interface.** Physicalpp2--4 bounded-face Euler/marked boundary-endpoint incidence and face-pairing proof of one-step disc boundary-walk decrement; strengthened internal minimumdelta>6 term. Endpoint singleton and5-wheel provide precise method-condition boundaries.

**Conditions.** Finite simple closed-disc triangulation; simple boundary cycle lengthn; Vtotalvertices,Eedges,Fboundedtriangles. Euler V-E+F1,3F2E-n,E3V-n-3. With nonempty interior, average INTERNAL degree sigma and boundary-marked internal-edge incidences m give m=2n-6-(sigma-6)(V-n), chords countedtwice. For nprime<=n-6 require every internal degree>=6 and nonempty stripped remainder. Bridges counttwice in nprime, isolated vertices0. Internal minimumdelta>6 gives nprime<=n-6-(delta-6)(V-n). Boundary vertices need no minimum6.

**Transfer limits.** Only bounded-face Euler/incidences and one-step disc boundary-WALK recurrence. No all-layer vertex bound; printed Th2/Cor3/Th4 endpoints remain refuted and excluded. No corrected universal volume/cut formula, Th5 hyperbolic comparison, Prop6 nonamenability, generic Gauss--Bonnet, compression, exact outerPhiV/A023,A022 orA193.

### EXSRC-2413a92d920b972a — Isoperimetric Constants of Infinite Plane Graphs

Serge Lawrencenko, Michael D. Plummer, Xiaoya Zha (2002). DOI: 10.1007/s00454-002-0694-2. Methods: G17.02, G17.04, G17.05, G17.06. Exact local version: Exact18-page Springer published PDF; printed313--330; no distinct-version equivalence asserted.

**Admitted interface.** Primal finite-face perimeter equals dual crossing-edge cut per dual vertex (physical3/printed315). Polygon reduction Lem4.2 (8/320), TypeI/II section-removal induction Th5.2 (11--13/323--325), one-ended lens structure Th6.3 (13--16/325--328), and nonregular local contraction comparisons Th7.1 (16--17/328--329) give the non-strict universal lower bound f(delta). Regular triangular lens recurrence pp6--8/318--320 gives class-infimum upper bound sqrt((delta-6)/(delta-2)).

**Conditions.** Simple proper locally finite one-ended plane cell2-complex, carrier homeomorphic to the plane. Finite competitors have positive area a(H)=finite-face count; l(partialH)=number of edges incident to at most one selected finite face, singular edges counted ONCE. h=inf l/a equals dual edge-cut/dual-vertex i(G*), not a degree-volume or primal outer-neighbor ratio. Lens topology requires minimumdegree>=6. Lower bound requires integerdelta>=7 and every ambient degree>=delta: f=(delta-6)(delta^2-8delta+15)/[(delta-4)(delta^2-8delta+13)]. Accepted h(G)>=f and h(delta)>=f are non-strict. Regular vertexdegree-delta triangular tessellation only: l1=delta,l2=delta(delta-4),ln=(delta-4)l(n-1)-l(n-2) for n>=3;a1=delta,a(n+1)-an=ln+l(n+1), ratio limit sqrt((delta-6)/(delta-2)). Global regular formula quoted from HJL/HS uses vertexdegree d, facedegree f, and 1/d+1/f<1/2.

**Transfer limits.** Each finite polygon ratio>f yields only infimum>=f absent a uniform gap. The regular lens family supplies an upper bound only; no sharp universal equality/class-infimum conjecture is proved. G17.04 supports this lens family and topology, not an arbitrary finite-set recurrence. No artificial l0=1 boundary length or Cassini atn1 is used. No primal outer PhiV/A023, cardinality-preserving compression/G17.03, generic curvature/G17.01, A022 or A193.

### EXSRC-5db9c997ea993a03 — Extremal {p,q}-Animals

Greg Malen, Érika Roldán, Rosemberg Toalá-Enríquez (2023). DOI: 10.1007/s00026-022-00631-1. Methods: G17.02, G17.04, G17.05, G17.06. Exact local version: Exact28-page arXiv2109.05331v1[math.CO],11Sep2021;2023bibliography/filename does not establish publisher equivalence.

**Admitted interface.** Fixed regular-tessellation tile-edge isoperimetry: maximize shared e2, then e1=pn-2e2 gives the exact spiral minimum P(n). Complete-layer degree matrices/ordered words (Prop3.3,Th1.3 pp3,9--16), spiral saturation formula (Th1.5 pp6,17--18), geometric spiral weak-dual path and integer lifting (Lem4.5/5.1 pp19--21), restricted-class dual descent plus total-edge hole filling (pp21--23) provide the scoped mechanism. The domain repair is separately R09-derived/R04-reviewed, not a claim that the broad printed lemma is correct.

**Conditions.** Fix integersp,q>=3 with(p-2)(q-2)>=4, regular p-gon tiles/qtiles at each ambient vertex. n>=1 is tile count; animal union has connected interior, holes allowed. e1 counts ALL selected/unselected tile interfaces including hole boundaries; in the full tile-dual graph it is a cut on n selected vertices of ambient degreep, normalized volume would bepn. The no-hole proof uses C(T): finite embedded subgraphs of the SAME regularT whose every bounded face is an actual ambient tile; componentwise weak dual lies in C(T*), full geometric interior degreeq. Use girth/forest and zero-face bases, two-dual face descent, and e2<=n-1 trivial case before g_n. Empty-spiral first-tile epsilon is not invoked. Filling a hole H adds TOTAL e(H) shared edges. Spiral values choose largestk with n(k)<=n<n(k+1), retain ordered deficit phase and r-1 saturation offset. q>3: P(n+1)-P(n) is p-2 orp-4 for n>=1; q3: p-4 orp-6 only forn>1. Euclidean t2 and hyperbolic t>2 layer formulas are separate.

**Transfer limits.** Exact finite-tile profile only in one fixed regular tessellation, not arbitrary planar graphs or primal fixed-vertex/outer-neighbor A023 profile. e1 includes hole boundaries, not exterior-only perimeter. Unrestricted Def2.1 weak-dual/Eq2.2/Lemma5.3 claims are refuted and excluded; the literal source statement is not silently corrected. Cor7.2 is excluded because q3 lies in its printed p>=4 range with zero denominator. All vertex/interior-vertex extrema across holes, uniqueness/exact extremizer classifications, Conj7.3 asymptotic assertion, general compression/G17.03, generic curvature/G17.01,A022 andA193 are excluded. Forq>=4 complete layers are not tile-dual graph-distance balls. No publisher/v1 text equivalence is asserted.

### EXSRC-355d181d08c8e9b8 — Isoperimetric numbers and spectral radius of some infinite planar graphs

Bojan Mohar (1992). DOI: not recorded in the accepted row. Methods: G17.01, G17.02, G17.05. Exact local version: Exact16-page DML-CZ scan; physical1 terms cover, physical2–16 printed411–425; personal-use copy retained, no redistribution approved.

**Admitted interface.** Sections3–4 reduce finite triangle regions and combine Euler/degree/boundary incidence, Eq4.8/4.9 physical9/printed418. Pure selected triangle regions give cubic dual crossing-edge cuts. Safe global Theorem6.1 (physical13/printed422) gives the coarse edge-Cheeger lower bound.

**Conditions.** Connected triangulated surface without boundary homeomorphic to a noncompact open subset of sphere/RP2/torus/Klein bottle, chi in{2,1,0}; every primal vertex belongs to at least integerk>=7 triangles. DualG cubic. i=inf finite nonemptyX |cutE X|/|X|, raw edges per dual vertex, normalized degree-volume divides by3. Direct r=|X|,q0=|cutE X| uses pure triangle-generated L; arbitrary nonpureL has dangling-edge terms. Universal i>=3(k-6)/(5k-18). Reduction gives q0prime<=max(q0,k),Iprime>=I, not equality.

**Transfer limits.** Literal unrestricted fixed-q0 finite Theorem4.1 is false and excluded. Max(q0,k) repair is R09-derived/R12-narrow-verified, not source text; requires reduced incidence/topology premises and chi>=0. End and cyclic refinements, spectral corollaries and all-k sharpness not admitted. No fixed-regular-tessellationG17.06, primal outer-PhiV/A023, cardinality-preserving compression, A022/A193.

### EXSRC-a340a109d73a2a50 — The Edge-Isoperimetric Problem for Regular Planar Tessellations

L. H. Harper (2001). DOI: not recorded in the accepted row. Methods: G17.03, G17.05. Exact local version: Exact17-page official published scan; printed47–63; literal title Tesselations; no other text version substituted.

**Admitted interface.** Euclidean triangularT={3,6}: Appendix stabilizing reflections preserve size and do not increase edge cut; lower-set weight sum and physical5–8/printed51–54 line-block exchange prove Theorem1 nested edge-optimal initial sets for every finite cardinality.

**Conditions.** Ordinary degree6 Euclidean triangular tessellation graphT, arbitrary finite vertex sets; boundaryTheta crossing edges, Theta=6|S|-2|I(S)|. Stabilizing reflection guard prohibits nonfixed crossing edges; generic chamber pointp. Infinite graph termination is for each fixed finiteS by strict distance potential within a finite lattice ball, not uniform finite-graphj0. TO lineblock lengths r-1,r,r,r,r,r+1 and weights0,1,2,3 give finite improving exchanges. Ball size1+3r(r+1) has only one stable optimizer; unrestricted uniqueness is not claimed.

**Transfer limits.** HoneycombH Theorem2 proof chain and arbitrary-S Lemma2 reverse stable iff statement held; no general optimizer duality or arbitrary planar compression. Hyperbolic extension is conjectural; VIP(T,H) left open by the paper. Crossing edges differ from outer vertices; no A023/A022/A193.

### EXSRC-63e8932d29899730 — An analogue of the Descartes-Euler formula for infinite graphs and Higuchi’s conjecture

Matt DeVos, Bojan Mohar (2007). DOI: 10.1090/S0002-9947-07-04125-6. Methods: G17.01. Exact local version: Exact18-page author-hosted manuscript with visible editorial notes; no equivalence to later2007 publisher text/pagination asserted.

**Admitted interface.** Physical3 regular-polygon metric/combinatorial curvature conversion kappa=2pi phi, and finite compact-front Theorem3.1 physical7–9: explicit boundary inner curvature plus interior defect equals2pi(s-t), by finite cell Euler and polygon angle sums.

**Conditions.** Finite compact polygonal regionQ with finite2cell decomposition, simple disjoint piecewise nice geodesic boundary cycles, closed completion Euler characteristic s in{0,1,2} as the source front definition permits, t boundarycomponents (planar regions have s=2). Face/boundary incidences counted with multiplicity; cellsF are insideQ, no exterior face. Sumface degrees=2E-lambda; added subdivision points have zero metric defect; total interior kappa plus boundaryiota=2pi(V-E+F)=2pi(s-t). For unit regular finite faces, phi(v)=1-deg(v)/2+sum_incidence1/deg(face), kappa=2pi phi.

**Transfer limits.** Boundary inner curvature cannot be omitted. This finite identity does not require or establish global tame/summable-negative-curvature classification. DraftglobalTheorem1.3, Cor1.4–1.5, discharging/3444Theorem1.7 not admitted. No edgeCheeger, outervertexPhiV/A023, compression, A022/A193.

### EXSRC-5635d16dd61d2073 — Isoperimetric Formulas for Hyperbolic Animals

Érika Roldán, Rosemberg Toalá-Enríquez (2025). DOI: 10.1007/s00373-025-02900-1. Methods: G17.05, G17.06. Exact local version: Exact23-page2025 Springer version of record; no equivalence to2206.14910v1 or distinct Malen published version asserted.

**Admitted interface.** Exact edge-perimeter formula Theorem1/Eq1.4–1.8 for n>n2, derived through Table2 boundary-degree words, Theorem9 characteristic Sturmian connection, Lemmas10–11 prefix floors, and geometric spiral edge identity3.10. Uniform2<epsilon<22 uses an explicitly separate R09-derived upper-bound repair; hence linear edge profile plusO(1).

**Conditions.** Integersp,q>=3, (p-2)(q-2)>4; one fixed regular{p,q} tessellation. Finite n-tile animals have connected interior; holes allowed, all boundary tile edges including holes counted once, equal full dual crossing-edge cut. n is tiles/dualvertices, dualdegreep, normalized volume ratio divides byp*n. Define t=(p-2)(q-2),alpha=(t-2+sqrt(t(t-4)))/2,beta=(alpha+1)/(p-2). Only n>n2=p(q-2)+1 admitted. k is integer with n_k<n<=n_(k+1); residue and phi use Eq1.5 cases, completed-layer indicator in Lemma11 must be retained. Pmin(n)=(p-2-2/beta)n+epsilon(n); exact epsilon is Eq1.6 and2<epsilon<22. All-animal extremality uses separately audited Malen mathematical edge result with R09 C(T) repair/R04 neutral, not asserted published/v1 text equivalence.

**Transfer limits.** PrintedEq1.9 initial endpoints are false and excluded; no all-n formula admitted. Refined errorEq1.10 not imported. Correctepsilon upper proof keeps source prior constant2 and improves phi2/beta<1.4 to obtain<20.6<22; this is derived, not source text. Characteristic Sturmian theorem is a cited input, no new read credit. No cardinality-preserving compressionG17.03, hole-vertex extrema/uniqueness, primal outerneighborPhiV/A023, A022/A193.

### EXSRC-191e72865e09b989 — Isoperimetric Inequalities on Hexagonal Grids

Berit Grußien (2012). DOI: not recorded in the accepted row. Methods: G17.03, G17.05. Exact local version: Exact12-page arXiv1201.0697v1 with3Jan2012stamp and title30Jan2020 conflict retained; no version equivalence or inferredjournalmetadata.

**Admitted interface.** Infinite Euclidean degree3 honeycomb Theorem1, physical3–7: cardinality-preserving row-gap translations yield three contiguous row families; extreme-neighbor incidence and a parallelogram count prove N(W)>=sqrt6*sqrt|W|. Crossing-edge E>=N supplies the same sharp constant; interior-set reduction gives the sharp nonlinear B inequality.

**Conditions.** Arbitrary finite W in the infinite Euclidean honeycomb vertex-edge graph. N=distinct outside-neighbor vertices, B=selected vertices with complement neighbor, E=crossing edges. All remain distinct. |N|²>=6|W|,|E|²>=6|W|, |B|>=sqrt6*sqrt(|W|+6/4)-3. Row-gap translations preservecardinality/N only; finite two-direction parallelogram shrinks during iteration. AreaQ and sum-of-squared row differences prove the universal bound. Sharpness uses actual tile clustersGr r>=1: V6r²,N=E6r; enlarged VGr unionN(VGr) has6r²+6r vertices andB6r. TheseGr are tile clusters, not primal metric balls.

**Transfer limits.** G17.03 only this lattice row-gap method, not arbitrary planar/hyperbolic compression or all optimizer classification. Sharp constants are not an exact minimum function for every cardinality. FiniteTheorem2, finiteRc formula and2/sqrt3conjecture excluded; printed Eq11 has a sqrt3factor defect. No tile-perimeter substitution, hyperbolic A023 outsidevertexprofile, A022/A193.

### EXSRC-6442b4e85c9dd144 — Planar lattice subsets with minimal vertex boundary

Radhika Gupta, Ivan Levcovitz, Alexander Margolis, Emily Stark (2021). DOI: 10.37236/10055. Methods: G17.03, G17.05. Exact local version: Exact32-page published EJC28(3)(2021)P3.57 DOI10.37236/10055; no arXiv byte/text equivalence asserted.

**Admitted interface.** Square-lattice l1 outside-neighbor vertex minimizers are characterized by Theorem6.4: boundary equality with the canonical diagonal enclosing box and missing cardinality at most the box excess. Theorem5.13 computes excess with exact parity/floor and corner/no-corner distinction. Proposition6.1 and Lemma6.10 give restricted saturation/component-gluing structural support.

**Conditions.** Finite nonempty subsets of Z2 with four nearest neighbors, distinct outside-neighbor vertex count. Canonical tight diagonal box bounds; zero-width canonical boxes have even other width. For standard B(alpha,beta), boundary=alpha+beta+4, size=floor((alpha*beta+alpha+beta+2)/2), excess=floor((floor(r)-k^2)/2). Positive-even no-corner Bhat has one fewer point and excess=(r-k^2-2)/2. The WW77 nested minimal comparison family is an external source input, not an additional newly read work. linfinity connectivity is auxiliary only; graph adjacency remains l1.

**Transfer limits.** Only this Euclidean square lattice and its distinct outside-neighbor vertex boundary. G17.03 is restricted structural improvement of saturated sets, not arbitrary plane compression. No hyperbolic A023, edge/face/tile conversion, A022/A193, neighborhood-preservation, or graph-of-minimal-sets admission. The cone formulation is excluded entirely from the admitted use; local derived corrections are explanatory audit evidence only.

### EXSRC-f93a4817eb949041 — An Isoperimetric Inequality and Pursuit-Evasion Games on Triangular Grid Graphs

Athipatana Iamphongsai, Teeradej Kittipassorn (2025). DOI: 10.1016/j.dam.2024.12.025. Methods: G17.03. Exact local version: Exact19page arXiv2312.12110v1 December2023 object; later2025DAM metadata not text/byte equated.

**Admitted interface.** Finite T_n outside-neighbor vertex profile via four cardinality-preserving neighborhood-monotone compressions and the two packing candidates. The exact all-n route is admitted through the explicit R09-derived guarded repair plus independent R06 neutral proof, not the source literal omitted guards/sums.

**Conditions.** n>=1; finite V={(x,y)>=0:x+y<=n}; edges six steps ±(1,0),±(0,1),±(1,-1); closed N restricted to V and boundary=N(A) minus A. Entire shifted unions clipped to legal column intervals. Initial counting only0<k<=T_n; proper final counting only n+1<=k<M; empty/full and n2,size2 separate. Dual partial-diagonal predecessor union>=a via proper-subset incident-edge injection. Exactlyk disjoint broken lines and nonstrict comparison. Empty wing handled separately; no triangular bracket at zero. Reuse the previously completed19p read; neutral has no separate credit.

**Transfer limits.** Only the exact finite triangular Euclidean graph and vertex boundary; no all-minimizer classification, games, infinite/hyperbolic transfer, A023, or edge/face/tile boundary substitution. Original literal unguarded Lemma6/extra sum are not accepted. Repair ownership is R09 with R06 independent audit.

### EXSRC-5f81aaba61be5f7b — Cheeger Constants, Growth and Spectrum of Locally Tessellating Planar Graphs

Matthias Keller, Norbert Peyerimhoff (2011). DOI: 10.1007/s00209-010-0699-0. Methods: G17.01, G17.05, G17.06. Exact local version: Exact arXiv0903.4793v3 physical18p with30July2009margin and10November2018title-date discrepancy retained; no2011journal text/byte equivalence.

**Admitted interface.** Exact induced-subgraph Euler/vertex-curvature identity and Theorem1 coarse crossing-edge Cheeger lower bounds with the guarded polygon incidence/reduction proof. G17.06 is limited to regular-tessellation vertex-sphere recurrence/counting under finite face length and no cut locus, with BP1/BP2 dependencies explicit; it is not a profile theorem.

**Conditions.** Infinite ambient locally tessellating plane graph under Definition2.1. Integer vertex/face caps p,q>=3 or infinity with1/p+1/q<=1/2; infinite caps remove the corresponding bound. Cpq=1 ifq infinity, q/(q-2) ifp infinity andqfinite, otherwise q(p-2)/((p-2)(q-2)-2). alpha>=2Cpq*inf(-kappa)>0 or alphatilde>=2Cpq*inf(-kappa/degree)>0, with crossing-edge/cardinality or full-degree-volume ratios. Proposition2.3 used only on connected polygons of>=2vertices with external degrees<=p-2. Theorem1 excludes singleton violators viaLemma2.4 before applying it. Euler face count includes the unbounded induced face and c(W) counts all nonambient induced faces. Sphere recurrence requires qfinite face-regular/no-cut-locus and cited BP1 identities; regular specialization p-2/p-4 coefficients, hyperbolic scope additionally(p-2)(q-2)>4. BP2 corner input is justified from vertex sign only because face regularity is fixed.

**Transfer limits.** No edge-to-outside-vertex conversion or sharp hyperbolic/A023 profile. Sphere/growth outputs are separate from edge-Cheeger statistics; no arbitrary-set boundary extremality follows from sphere recurrence. Printed singleton Proposition2.3, tree normalized ratio(p-2)/2, Proposition1.2/estimate7, spectral/Mahler branches and externally cited exact regular constants are excluded. Theorem4 tree-opening construction is not an independently admitted method.

### EXSRC-348d4438584cca84 — Polyiamonds and Polyhexes with Minimum Site-Perimeter and Achievement Games

Gábor Fülep, Nándor Sieben (2010). DOI: 10.37236/337. Methods: G17.01, G17.02, G17.05. Exact local version: Exact complete14physical-page EJC17(1)(2010)R65 VOR DOI10.37236/337.

**Admitted interface.** Exact maximum cell cardinality at fixed distinct outside-cell site-perimeter: sigmaT(p)=2floor(p²/12-p/2)+p forp>=3, sigmaH(p)=floor(p²/12-p/2)+1 forp6 orp>=8; all-connected-animal capacity bounds, attained fixed-perimeter families and one-sided inverse perimeter lower bounds. Restricted hexagonal-polyhex outer-dual/Euler identity suppliesG17.01/.02; no all-size inverse attainment is admitted.

**Conditions.** Finite nonempty edge-connected animals; holes permitted. Triangular cells are vertices of degree3 planar honeycomb adjacency; hexagonal cells are vertices of degree6 planar triangular adjacency; sharing one side defines neighbors. p counts all unoccupied side-neighbor cells including holes. Saturation/fixed-perimeter maximum argument and six integer-defect residues0,7,4,3,4,7. For hexagonal B only, p(B#)=p(B), s(B#)=2s(B)+p(B)-2 and sigmaT=2sigmaH+p-2 onp6 orp>=8. Lemma5.6 uses top cells in B intersection U, not the printed union/arbitraryU; Prop5.7 intended polyhex maximum is sigmaH, not printed sigmaT. Nonempty candidate shapes only; no hole Euler formula applied to arbitrary animals.

**Transfer limits.** Connected Euclidean cell models only. Fixed-perimeter capacity and inverse LOWER BOUND do not prove all-size piT/piH equality/attainment; Lemma4.3 chosen deletion can disconnect and inverse route is held. No arbitrary disconnected sets, general plane graphs, cardinality-preserving compression, edge-cut substitution, hyperbolic/A023/A022/A193 transfer or game claim. Duality is specific to convex hexagonal animals and not a general boundary conversion.

### EXSRC-b4ef8751c3dbb518 — Isoperimetrically Optimal Polygons in the Triangular Grid with Jordan-type Neighbourhood on the Boundary

Benedek Nagy, Krisztina Barczi (2013). DOI: 10.1080/00207160.2012.737914. Methods: G17.05. Exact local version: Exact23physical-page author-accepted manuscript posted15October2012, articleprinted1–22; journal2013 bibliographic link only, no VOR text or byte equivalence.

**Admitted interface.** Exact maximum number of triangular cells at each fixed distinct outside side-neighbor boundary P>=3, with corrected six-residue values6n²,6n²+2n−1,6n²+4n,6n²+6n+1,6n²+8n+2,6n²+10n+3. Source convex side identities plus reader-derived/R09-verified all-parameter optimization and explicit convex witnesses; safe all-animal upper bound uses already-admitted Fulep sigmaT for the identical statistic. One-sided inverse perimeter lower bounds only.

**Conditions.** Finite nonempty side-connected hole-free triangular-cell animals in the Euclidean triangular tiling. Cells are vertices of the degree3 planar honeycomb adjacency; outside TRIANGULAR cells sharing sides are counted distinctly. Six nonnegative integer sides satisfy closure and P=sumside; n>=1 for residue0/1/2 and n>=0 for3/4/5. Defect P²−6A=sum of three squares with coefficients1,3,3 and A=P mod2 yield minimal residues0,7,4,3,4,7. Printed case6 is corrected explicitly, not silently attributed to the source.

**Transfer limits.** Fixed-perimeter capacities do not assert all-size inverse attainment, classification of every extremizer or generic embedding-hexagon boundary monotonicity. No area-preserving compression, Section5 three-neighbor graph (containsK6), arbitrary disconnected transfer, edge-cut/inside-boundary substitution, hyperbolic A023, A022/A193. Source connected-hole-free restriction retained.

### EXSRC-3dbef813a4f3b8d7 — Tilings and isoperimetrical shapes I: Square lattice

Sylvain Gravier, Charles Payan (2001). DOI: not recorded in the accepted row. Methods: G17.05. Exact local version: Exact complete16physical-page DML-CZ digitized journal article40(1)(2001), printed63–77 on physical2–16; terms cover1; no alternate-version equivalence asserted.

**Admitted interface.** Exact occupied/internal four-neighbor square-cell boundary capacity max_{b(P)=n}|P|=M(n)=floor(n²/8+n/2+1) for every n>=1, and attained all-positive-area inverse min{n>=1:Delta<=M(n)}. Numeric sourceTheorems2/4 only, established through explicitly R09-derived/R10-neutral-verified Gupta-dependent erosion proof.

**Conditions.** Finite nonempty subsets of Z2 unit square cells; disconnected sets and holes permitted. b(P)=|P|−|I(P)|, where I(P) requires all four edge-neighbors occupied; missing cells in holes count in the complement. M(0)=0 empty convention only. Outside/internal statistics stay distinct: C(I(P)) subset P yields an outside budget, canonical-box capacity bounds the interior, balanced closed boxes attain capacity, and same-size outside minimizers plus remote singletons attain every inverse area. Gupta Lem2.1/boxsize/forwardTh6.4 are explicit admitted dependencies.

**Transfer limits.** No shape classification, uniqueness, source UD terminal iterate, Lem3 label formulas or Lem5 connectedness proof imported. No connected-only profile or king-graph planarity, exteriorTh5, Golomb/density claim, outside/edge/tile statistic substitution, general/hyperbolic/A023/A022/A193 transfer. Independent proof belongs toR09 and is confirmed byR10, not represented as the source literal proof.

### EXSRC-112bc4c1c06838cd — On isoperimetrically optimal polyforms

Daniel Vainsencher, Alfred M. Bruckstein (2008). DOI: 10.1016/j.tcs.2008.06.043. Methods: G17.05. Exact local version: Exact complete14physical-page Technion-hosted published typeset TCS406(2008)146–159 article, DOI10.1016/j.tcs.2008.06.043.

**Admitted interface.** Exact numeric X4 Pareto area–outside-boundary frontier: (0,0),(1,4),(F(p),p) for everyp>=6, F(p)=floor(p²/8−p/2+1), attained by explicit balanced diagonal boxes. Corrected legal Theorem7 B-domains and corrected Theorem42 indexed area A1=0, An=floor(((n+1)²+4)/8) n>=2; pn=n+3 n>=3. Reuses the already-admitted Gupta outside-budget capacity lemma; no complete all-shape classification or all-cardinality profile admission.

**Conditions.** Arbitrary finite subsets of nearest-neighbor Z2 square cells, disconnected/holes permitted. Perimeter counts distinct outside side-neighbor cells once. Pareto means both strong source quantifiers: boundarybudget≤p implies area≤A, and competitorarea≥A implies boundary≥p. Nonempty outside perimeter≥4; p5 infeasible; F4=F5=1 and strict feasible-frontier increase. Legal B ranges i0:m>=−1,i1:m>=0,i2/3:m>=−1, p=4(m+2)+i. Lemma39 coef corrected from1+i to2+i; Theorem42 literaln² replaced explicitly by(n+1)² and fixedi recurrence difference n−1.

**Transfer limits.** Only numeric Pareto envelope and explicit witnesses in the Euclidean X4 graph. Full Theorem4 shape/spine classification and universal expansion-optimality remain source-stated. No classification of all fixed-cardinality minimizers, exact all-cardinality boundaryprofile, compression, X8 kinggraph, hex proof deferred totechnicalreport, inside/edge/tile statistic substitution, arbitraryplanar/hyperbolic/A023/A022/A193 transfer.

### EXSRC-96e752f3c43fffee — A General Method to Determine Limiting Optimal Shapes for Edge-Isoperimetric Inequalities

Ellen Veomett, Emmanuel Tsukerman (2017). DOI: 10.37236/6403. Methods: G17.05. Exact local version: Complete official Electronic Journal of Combinatorics 24(1) (2017) P1.26 PDF; no byte-equivalence to related arXiv version asserted..

**Admitted interface.** For independently planar two-dimensional primitive-lattice graphs, exact finite edge cut is twice occupied direction-line runs. For compact full-dimensional convex bodies the correctly normalized anisotropic boundary of Z=Σ[-vi,vi] is minimized at homothetic copies of Z, and lattice-point/edge-cut ratios calibrate under large positive dilation. This identifies a continuous comparison shape, without identifying discrete optimal shapes.

**Conditions.** Distinct nonzero primitive integer generator directions modulo sign spanning R²; finite set for the run identity and actual gap-free fibers for its projection-only reduction. Plane application requires a separately valid plane realization. Convex sets must be compact bodies with nonempty interior. Orthogonal projections use squared-norm denominator; projected-lattice covolume is 1/||v|| and boundary weight its reciprocal ||v||. Minkowski coefficients used are nonnegative. Explicit independent R09 line-count, 2D squeeze and mixed-area equality arguments are bound.

**Transfer limits.** Only crossing edges and convex-body calibration. No outer-vertex profile, exact finite edge profile, discrete minimizer convergence or Def4-alone shape identification, generic compression, arbitrary plane graph or hyperbolic transfer, A023, A022 or A193 conclusion.

### EXSRC-0cee07fa92517c8a — Isoperimetry in integer lattices

Ben Barber, Joshua Erde (2018). DOI: 10.19086/da.3555. Methods: G17.05. Exact local version: Complete arXiv1707.04411v2, 19 April2018, 16 physical pages, typeset Discrete Analysis2018:7; no publisher byte-equivalence asserted..

**Admitted interface.** For a symmetric finite generator set U generating Z², with independently checked plane realization, the minimum n-vertex crossing-edge boundary is (1+o(1))2sqrt(area(Σ[0,u]))sqrt(n). Integer-dilate zonotope lattice sets give a matching upper family, and exposed-vertex removal/profile monotonicity supplies arbitrary cardinalities. The lower proof is the discrete random-push-out argument using the explicitly imported Ruzsa vertex-asymptotic theorem for a derived generator set.

**Conditions.** U is finite, excludes zero, is symmetric for undirected-edge interpretation, and generates all Z² as a group. Individual directions need not be primitive; occupied cosets of Zui are counted separately. Fixed U and δ>0 precede n≥n0(δ,U). Area is in integer-lattice coordinates. Ruzsa Theorem2 and Ehrhart Theorem11 are explicitly imported dependencies, not separately full-read original sources. Plane realization is an additional application guard.

**Transfer limits.** Asymptotic minimum edge-boundary value and near-optimal witness family only; no exact finite profile, all-minimizer convergence/stability/classification, nested optimal ordering, outer-vertex profile conversion, general planar/hyperbolic transfer, A023, A022 or A193 conclusion.

### EXSRC-32de53c3ce49f0e3 — Isoperimetry in two-dimensional percolation

Marek Biskup, Oren Louidor, Eviatar B. Procaccia, Ron Rosenthal (2015). DOI: 10.1002/cpa.21558. Methods: G17.02. Exact local version: Complete arXiv1211.0745v2,14January2015,40physicalpages; not equated to CPAM publisher pagination or bytes..

**Admitted interface.** For a finite nontrivial connected induced open subgraph on the square-lattice infinite cluster, the outer medial interface encodes a counterclockwise right-most circuit gamma with U subset fill(gamma) and auxiliary open right-boundary count b(gamma)<=ambient C_infty edgecut(U). Conversely an open nontrivial counterclockwise right-most circuit contained in C_infty gives connected U*=fill(gamma) intersect C_infty and ambient edgecut(U*)<=b(gamma). This is a contour/edge-cut encoding, independent of concentration and asymptotic profile estimates.

**Conditions.** Supercritical nearest-neighbor Bernoulli bond percolation on Z², p>1/2, on a realization with unique infinite open cluster. U finite, |U|>=2, connected as its induced OPEN cluster graph. Converse gamma finite nontrivial, open, counterclockwise outer interface, and gamma subset C_infty. Directed bridge traversals and auxiliary oriented multiplicity retained; the open-edge injections justify only the stated inequalities. Canonical outer trace is understood up to cyclic start.

**Transfer limits.** G17.02 only. No G17.05 profile, boundary norm asymptotics, stochastic shape theorem, quantitative circuit-to-curve error, Kesten concentration certificate, outer/inner vertex profile, generic compression, general planar or hyperbolic graph profile, A023/A022/A193 conclusion. The literal local bounds and proposed repairs remain held for separate neutral review.

### EXSRC-7670986d60d1e13b — Limit of the Wulff crystal when approaching criticality for isoperimetry in 2D percolation

Chang-Long Yao (2023). DOI: 10.1214/23-EJP1061. Methods: G17.05. Exact local version: Complete arXiv2303.04401v2,22November2023,20physicalpages,with EJP prepublication placeholders; no publisher-object byte equivalence..

**Admitted interface.** In supercritical triangular-lattice site percolation, use the source boundary/FPP norm equality beta_p=mu_p and its explicitly imported uniform near-critical FPP limit to compare continuum variational constants and defined dual norm bodies. Direct infimum comparison with Euclidean isoperimetry yields L(p)phi_p->2nu sqrt(pi), while halfspace/disk and area sandwiches yield the DEFINED unit-area dual body tending to the unit-area Euclidean disk. Neither argument needs a fixed-p profile theorem or identifies that dual body as a finite-p tangent-perimeter minimizer.

**Conditions.** Unit-edge Euclidean triangular lattice, Bernoulli sites with P_p(omega=1)=p>1/2 (open sites have FPP cost1). phi_p is only the infimum of beta_p-lengths of Jordan curves enclosing Euclidean area1; it is not here an admitted coefficient of a discrete profile. L(p) is the source fixed closed-crossing correlation-length convention. Proposition1.6 uses cited circuit/FPP and tilted-cylinder flow/percolation inputs; Theorem1.5 imports uniform L(p)mu_p(u)->nu from[30], not separately full-read here. Norm-to-infimum squeeze avoids minimizer existence; defined-body disk squeeze avoids the unrotated argmin assertion.

**Transfer limits.** Only G17.05 near-critical continuum norm/variational-constant and defined-dual-body comparison with named imported stochastic inputs. No source Theorems1.1/1.2 fixed-p profile constants or shapes, no unrotated W_hat argmin identification, no corrected all-p stochastic profile from a density/rotation substitution, no exact finite profile, deterministic planar/hyperbolic transfer, A023/A022/A193 conclusion, or joint n,p limiting theorem.

### EXSRC-24cbcb6f3e5ef02e — Tilings and isoperimetrical shapes. II. Hexagonal lattice

Sylvain Gravier (2001). DOI: not recorded in the accepted row. Methods: G17.04, G17.05. Exact local version: Complete DML-CZ digitized article with retained terms cover; article physical pp. 2–15, printed pp. 79–92..

**Admitted interface.** Exact convex lattice-hexagon occupied-boundary undress decrement6 with all six sides>=2; regular radius-q area3q²+3q+1 at occupied boundary6q yields a capacity lower witness.

**Conditions.** Finite unit honeycomb tiles identified with triangular centres; occupied/internal boundary. Convex lattice-aligned six-sided centre polygon with all six active side lengths>=2 for decrement; q>=1 for regular witnesses, q>=2 for applying decrement to regular patches. Singleton terminal boundary is1.

**Transfer limits.** No global maximal capacity equality, six-residue/classification/uniqueness, literal signed-word certificate, all-size inverse, G17.03 generic compression, arbitrary planar/hyperbolic/exterior-neighbour or A023 transfer.

### EXSRC-4694dcfa0be4fdc9 — Sharp N^{3/4} Law for the Minimizers of the Edge-Isoperimetric Problem on the Triangular Lattice

Elisa Davoli, Paolo Piovano, Ulisse Stefanelli (2017). DOI: 10.1007/s00332-016-9346-1. Methods: G17.05. Exact local version: Complete Springer Nature version of record, Journal of Nonlinear Science 27 (2017), 627–660..

**Admitted interface.** Connected triangular-lattice auxiliary isoperimetry via explicit bond/triangle incidence and Euler hole count: P>=p_n, A<=a_n, sqrt(A)<=k_n P; equality implies edge minimization, and is equivalent on the connected h=0 domain, given the named imported theta_n input.

**Conditions.** Finite connected n-site subset of standard unit-edge six-neighbour Euclidean triangular lattice. A counts contained unit triangles; P=H1(partial F)+2H1(G); h counts bounded nontriangular induced-graph faces. theta_n=2ceil(sqrt(12n-3)) is explicit Heitmann–Radin/Radin input quoted by source(12), not newly reproved. n>=2 for k_n; n2 bond direct; n1 cut6 with k1 unused. Reverse equality characterization guarded by h=0.

**Transfer limits.** No all-minimizer hole-free assertion, full tau-weight route, G17.03 compression, sharp N^3/4/Wulff/Hausdorff/shape theorem, all-n sharpness construction, arbitrary planar/hyperbolic/outside-vertex profile or A023 transfer.

# Positive and missing-condition examples

These examples illustrate source interfaces. Exact finite computations are evidence for the listed instances only.

## Positive cases

1. **Finite triangulation Euler/SAP route (Panagiotis).** For a finite connected S(d,k) plane region with a self-avoiding polygon boundary, simple bounded k-gons, internal degree d, and (d−2)(k−2)>4, use the source’s stated SAP inequality with its inner face-incident boundary. This is not an all-finite-set outer-neighbour theorem.
2. **Regular tessellation edge and face profiles (Higuchi–Shirai; Häggström–Jonasson–Lyons; Lyons–Peres).** The exact formulas require the named regular planar graph/dual or regular tessellation, the source’s degree and normalization conventions, and a matching sequence. Keep edge cut, degree-volume, vertex count, and face boundary denominators separate.
3. **Plane-graph outer-neighbour lower bounds (Haslegrave–Panagiotis; Oh 2020).** Apply only under proved degree and face-degree hypotheses. For example, the H–P lower bound with d≥7 is a direct all-finite-set outer-neighbour statement; the quadrilateral-face route requires d≥5 and all face degrees ≥4. It does not cover arbitrary face lengths.
4. **Compression (Iamphongsai–Kittipassorn).** The admitted method is the finite triangular-grid T_n outside-neighbour profile after the independently checked all-n compression proof. Its two candidate families apply on T_n only; it is not a hyperbolic compression.
5. **Honeycomb tile layer witness (Gravier, R09 batch24).** A regular radius-q honeycomb patch has area 3q²+3q+1 and occupied/internal boundary 6q. This is a lower witness for maximum area at that boundary count. For a convex lattice-aligned six-sided polygon with all active sides at least 2, inward underdress lowers the boundary by 6; the terminal singleton is excluded from this decrement.
6. **Triangular-lattice auxiliary Euler inequality (Davoli–Piovano–Stefanelli, R09 batch24).** For a finite connected set, retain h, the number of bounded nontriangular faces, in cut=2P+6−6h. With the explicitly imported θ_n=2 ceil(sqrt(12n−3)), the accepted incidence/Euler proof yields P≥p_n and A≤a_n, then sqrt(A)≤k_nP for n≥2. For n≥3 equality implies cut=θ_n; among connected h=0 sets, cut=θ_n implies equality. Handle n=2 directly and never use the coefficient at n=1.
7. **Percolation-specific interfaces.** Biskup et al. are admitted only for the outer medial contour encoding of a finite nontrivial connected induced open subgraph in the supercritical square-lattice infinite cluster. Yao is admitted only for the near-critical continuum norm/variational-constant and defined dual-body comparison with its imported stochastic inputs. Neither is a deterministic fixed-p outer-vertex profile.

## Missing-condition and boundary-convention cases

- **Occupied cells versus cut edges.** In the radius-one seven-cell honeycomb patch, occupied boundary has size 6 while the triangular-graph crossing-edge cut has size 18. Gravier’s statistic and an edge cut cannot be substituted. The local four-radius calculation is saved at the package's exact boundary-convention script（本机附件：`examples/calculations/boundary_conventions_example.py`）, saved output（本机附件：`examples/calculations/boundary_conventions_example.actual_output.json`）, and R09's independent finite-case output（本机附件：`examples/calculations/r09_actual_results.json`）.
- **Hole term.** In the six-cycle with its centre removed, n=6, E=6, A=0, P=12, cut=24, h=1. Dropping −6h from the Euler identity gives the wrong relation. This finite example clarifies the condition; it is not a source-error verdict.
- **Degenerate singleton.** For the DPS auxiliary coefficient, θ_1=6 and k_1 has zero denominator. Handle cut=6 and A=P=0 separately; use k_n only for n≥2.
- **Outer-boundary hypotheses.** A lower bound on |N(S) minus S| is not an edge-cut estimate without a proved conversion. State the set domain, degree and face-degree constraints, and matching upper sequence. An edge theorem alone does not identify A023.
- **Probability transfer.** A boundary estimate alone does not establish the A022 conditional peak-distance claim: separately compare distant-peak labelings with the full two-peak count. An infection rule does not inherit planarity from a degree bound: prove a plane embedding and map witnesses to the exact source boundary.
- **Held shape source.** D’Achille–Jacquier–Ruszel remains held for its broad all-N edge-minimizer classification and minimizer-limit use; it is not among the 30 eligible works.
- **Excluded path source.** Benjamini–Papasoglu’s winding-path/profile deduction remains outside the accepted 30 after a proof gap.
- **Nonplanar support-only source.** Veomett–Radcliffe king-lattice evidence is support-only and not an accepted planar source row.

## Scope exclusions and open transfers

- D’Achille–Jacquier–Ruszel (EXSRC-42b5f465d5ea00c5) remains held for all-N edge-minimizer classification and limit claims and is excluded from the 30 eligible works.
- Benjamini–Papasoglu’s winding-path/profile deduction remains excluded after a proof gap.
- Veomett–Radcliffe’s nonplanar king-lattice use is support-only and is not an eligible planar-source row.
- Claims beyond each source’s admitted row remain unreviewed unless a distinct accepted row covers them.

## Exact-profile, probability, and infection checks

For A023, define Phi_V as the infimum of |N(S) minus S|/|S| over finite nonempty sets in the specified graph. Prove a lower bound for every set and a matching upper sequence. State vertex degree and face length separately. An edge theorem transfers only after an explicit conversion. The accepted 30-source set does not settle the remaining general outer-vertex cases.

For A022, map the conditioned configurations to the counted sets and compare distant-peak labelings against the full two-peak count. An isoperimetric inequality alone does not prove the conditional limit.

For A193, first prove the particular rule graph has a compatible plane embedding, then show that the witness process is controlled by the exact boundary statistic. A degree constraint does not imply a face-degree condition.

This is a whole-entry candidate synchronized to R09 union02: 30 distinct locally eligible works plus one held source. It is not an installation or publication approval. Root identity deduplication and independent whole-entry/portable review remain required.
