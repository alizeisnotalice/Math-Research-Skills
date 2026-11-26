# 行列式依赖的来源索引

下列四篇原件支撑可调用的条件 DPP、完备性、抽样依赖或半平面性质。共享原件可按 SHA-256 在 `/Volumes/共享/Math_Research_Literature/01_Existing_Skill_Sources/` 定位。下方同时保留 31 条旧登记的题名与哈希，供查找历史原件和进一步复核。

## Active scoped sources

### EXSRC-849170808020180b — Bufetov, Qiu, Shamov, *Kernels of conditional determinantal measures and the Lyons–Peres completeness conjecture*

- **Original and identity:** J. Eur. Math. Soc. 23 (2021), 1477–1519, DOI
  `10.4171/JEMS/1038`; SHA-256
  `849170808020180ba92d664a7a9dff7b01a9b68555b31fef0639836ee166fd0e`.
  Current archive: `Papers/84/849170808020180ba92d664a7a9dff7b01a9b68555b31fef0639836ee166fd0e__849170808020180b.pdf`.
- **Checked locators:** Theorem 1.4 and Theorem 1.6, physical p.7 (printed
  1483); Lemma 1.9 and Lemma 1.10, physical p.10 (printed 1486); tail proof,
  physical pp.28–31 (printed 1504–1507).
- **Admitted use:** A self-adjoint locally trace-class positive contraction has a
  conditional DPP kernel under conditioning on a Borel-set configuration (Lemma
  1.9); its tail sigma-field is trivial along bounded exhaustions (Theorem 1.6).
  If the kernel is an orthogonal projection onto H, sampled kernel functions are
  a.s. complete in H (Theorem 1.4).
- **Conditions and boundary:** E is locally compact sigma-compact Polish with a
  sigma-finite Radon measure; K is self-adjoint, locally trace class, and has
  spectrum in [0,1].  Projection/completeness needs the additional orthogonal-
  projection/RKHS hypothesis.  Tail triviality is not arbitrary group-action
  ergodicity, and no BK statement follows.

### EXSRC-7904edb8619ad4b3 — Brändén, Jonasson, *Negative dependence in sampling*

- **Original and identity:** SHA-256
  `7904edb8619ad4b3d30aa38ddeaa2d4d47298fe3c645a92e18250b7128c1d2cd`.
  Current archive: `Papers/79/7904edb8619ad4b3d30aa38ddeaa2d4d47298fe3c645a92e18250b7128c1d2cd__7904edb8619ad4b3.pdf`.
- **Checked locator:** Theorem 1, physical p.9; Sampford/Pareto applications,
  physical p.12.
- **Admitted use:** If independent 0–1 families X and Y are strongly Rayleigh,
  then the law of Z=X+Y conditioned on `sum_i X_iY_i=0` is strongly Rayleigh.
  The paper applies this to specified sampling constructions and obtains CNA+;
  that is a negative-dependence interface, not BK.
- **Conditions and boundary:** The input laws must actually be strongly Rayleigh,
  the two families independent, and the disjointness conditioning event have
  positive probability.  Do not replace these by generic NA/CNA, and do not
  infer a random-witness BK inequality.

### EXSRC-77e019f8e1fee753 — Bufetov, Qiu, *Conditional measures of generalized Ginibre point processes*

- **Original and identity:** arXiv:1608.03736v2 (2017-04-27), 27 physical
  pages; SHA-256
  `77e019f8e1fee753ea47ae2183cf7ceee2843187335a6dd21a5e591d1a0f3846`.
  Current archive: `Papers/77/77e019f8e1fee753ea47ae2183cf7ceee2843187335a6dd21a5e591d1a0f3846__77e019f8e1fee753.pdf`.
- **Checked locator:** Theorem 1.5 and Corollary 1.6, physical p.4; derivation
  using rigidity and same-order Palm Radon–Nikodym derivatives, physical p.5.
- **Admitted use:** For the paper's generalized Fock projection DPP, conditioning
  on the exterior of a bounded B gives the fixed-number interior OPE of (1.12).
  When phi is radial and B contains 0, Corollary 1.6 gives the stated principal-
  value product weight.
- **Conditions and boundary:** This is not a theorem for arbitrary conditional
  DPPs.  Retain the paper's phi/Fock-kernel assumptions, number rigidity, bounded
  B, and (for the product formula) radial phi plus `0 in B`.  The generic
  self-adjoint conditional-kernel claim belongs instead to the preceding BQS row.

### EXSRC-7d0d3b07266ee12d — Choe, Oxley, Sokal, Wagner, *Homogeneous Multivariate Polynomials with the Half-Plane Property*

- **Original and identity:** arXiv:math/0202034v2 (2002-12-04), 111 physical
  pages; SHA-256
  `7d0d3b07266ee12d68093a490a47c3b86e6d304a76bd419dd8d0635ad3e66d6d`.
  Current archive: `Papers/7d/7d0d3b07266ee12d68093a490a47c3b86e6d304a76bd419dd8d0635ad3e66d6d__7d0d3b07266ee12d.pdf`.
- **Checked locators:** Theorem 1.1 (connected-graph spanning-tree polynomial),
  physical p.4; Theorem 7.1 (HPP support is a matroid basis family), p.46;
  determinant construction Theorem 8.1, p.50; permanent construction Theorem
  10.2, p.64.
- **Admitted use:** The right-half-plane HPP convention supports the exact
  spanning-tree/determinant and specified nonnegative-permanent constructions;
  Theorem 7.1 is a necessary matroid-support result.  It supports the skill's
  convention warning and its rejection of “every matroid basis polynomial is
  stable.”
- **Conditions and boundary:** The source uses the right half-plane, whereas
  real stability is normally upper-half-plane; the fixed-degree substitution
  must be written explicitly.  Theorem 7.1 is one-way.  No generic DPP,
  strong-Rayleigh, or BK result is supplied by HPP alone.

## Historical R10 rows retained for identity only

The following names and SHA-256 values are retained because they appeared in the
snapshot registry.  Their promised cards/PDF objects are absent from this snapshot, so
they are archival leads rather than active theorem support until a new card names a
claim, locator, version, and dependency.  The four active rows above are repeated here
only by reference, not re-counted.

| Historical title | SHA-256 / source id | Current status |
|---|---|---|
| Determinantal Probability Measures | `e84c37bdad09a9337d41266311b9d266d34d6e1fae5bfa81fcdb75e4ac1d9aba` / PR-978b45a13662 | identity only; resolve in original archive |
| Uniform Spanning Forests | `17da5f8f44c41ae071c306743155bab0ae56863cb2652bb010ae006963333693` / PR-d9e630a5f1fa | identity only; resolve in original archive |
| Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances | `5ac77ebeb5a5e81b043c13563717fdf6a203dfbb18a9ee9cd30bbded7bba39a0` / PR-aeefaf918ee6 | identity only; resolve in original archive |
| Negative Dependence and the Geometry of Polynomials | `bf0f91277a5874ffca7c63af3dbfb4a97dde8c977aa4c061cefbca8fddedb301` / EXSRC-bf0f91277a5874ff | identity only; resolve in original archive |
| Concentration of Lipschitz Functionals of Determinantal and Other Strong Rayleigh Measures | `66ba88e13a429a0a3d01f1a7a2b0a8c5fdfd52b816427d94d0b95d09b6791499` / EXSRC-66ba88e13a429a0a | identity only; resolve in original archive |
| Closure Properties and Negatively Associated Measures Violating the van den Berg–Kesten Inequality | `2be5bcbcbb47fb90f64a480b6854c21b0e6701798d915f243054dbd2eac20d3c` / EXSRC-2be5bcbcbb47fb90 | identity only; resolve in original archive |
| Perturbation analysis of the van den Berg Kesten inequality for determinantal probability measures | `289ce03696c5e3b9c86ec18341e1699d03fc84dc732401f5664430d74c0373bb` / EXSRC-289ce03696c5e3b9 | identity only; resolve in original archive |
| A BK Inequality for Randomly Drawn Subsets of Fixed Size | `61fc0dcb5a13eab3b8bb5a42f03f8b10423db8ed3aabf8f7b8d7b3965b6b7438` / EXSRC-61fc0dcb5a13eab3 | identity only; resolve in original archive |
| Negative Dependence and Srinivasan’s Sampling Process | `86f8f3d45fa1c1f645912427963d9efbea3eba9cd7be8f9d73b20a3a2a9c7a43` / EXSRC-86f8f3d45fa1c1f6 | identity only; resolve in original archive |
| The BK inequality for pivotal sampling a.k.a. the Srinivasan sampling process | `0491c5825f871316e76536fd2e2f7d9e9d5088c9e4da5c738ff72943ff7bb9d0` / EXSRC-0491c5825f871316 | identity only; resolve in original archive |
| The case of equality in BK | `c228ab1ca7320c726f268007289d15042d3846fee775eb19d55dc7abadc90417` / EXSRC-c228ab1ca7320c72 | identity only; resolve in original archive |
| Conditional Intensity and Gibbsianness of Determinantal Point Processes | `b4d42d4dd61c84ba47ab11601821143e214f9b8225a65fd37e1d5c4e71fed1d5` / EXSRC-b4d42d4dd61c84ba | identity only; resolve in original archive |
| BK-type inequalities and generalized random-cluster representations | `70fa02375213cfff442822976b05ebae8c5dff03824ee937d05a1617197247d2` / EXSRC-70fa02375213cfff | identity only; resolve in original archive |
| A BK inequality for random matchings | `1967fd100319577506a41e209183ac46f6c22fa3622145a0ebc32fc73a3f6e44` / EXSRC-1967fd1003195775 | identity only; resolve in original archive |
| On Tail Triviality of Negatively Dependent Stochastic Processes | `b13b89dbfd9bc4e2b455bd99b8b847a9b50c7782e6046df1c555cad69af6ab1a` / EXSRC-b13b89dbfd9bc4e2 | identity only; resolve in original archive |
| Invariant coupling of determinantal measures on sofic groups | `ac6d3767cb7a4c2d216de2a13b8579f2d133773e3d5b12f1610ab630fc792544` / EXSRC-ac6d3767cb7a4c2d | identity only; resolve in original archive |
| Discrete Approximations of Determinantal Point Processes on Continuous Spaces: Tree Representations and Tail Triviality | `af89bb36241dd940dbf58a10928d15c1e8c747a3a7b2d6b8343c4e1bf4087f25` / EXSRC-af89bb36241dd940 | identity only; resolve in original archive |
| Negatively Correlated Random Variables and Mason’s Conjecture for Independent Sets in Matroids | `da9df75e375888803df2a9d3f665e4cecde6e054e67cdd704fea3e15a35b90ae` / EXSRC-da9df75e37588880 | identity only; resolve in original archive |
| Modified log-Sobolev inequalities for strong-Rayleigh measures | `438ba4f0bae10a470e736eda350f6cf83c48acad043ee78bf72bbc3ba1ab55c8` / EXSRC-438ba4f0bae10a47 | identity only; resolve in original archive |
| The Cosine–Sine Decomposition and Conditional Negative Correlation Inequalities for Determinantal Processes | `115093ef8c30d8b287935bf1833e944056d150cc952908affb84bc03c801ba0d` / EXSRC-115093ef8c30d8b2 | identity only; resolve in original archive |
| A note related to the CS decomposition and the BK inequality for discrete determinantal processes | `9693d4a7a84a546a80915e5f80db4a07b298e2d02d5e4c5192a5203ed2779ea8` / EXSRC-9693d4a7a84a546a | identity only; resolve in original archive |
| Stationary Determinantal Processes: Phase Multiplicity, Bernoullicity, Entropy, and Domination | `1262abc6cd6d6f6d2ccbb4268dcfb9030388a182cadad28514dbe23ca06d47b2` / EXSRC-1262abc6cd6d6f6d | identity only; resolve in original archive |
| Rayleigh Matroids | `571337373f995b25d61344d6ce8f88d1d7cb393c8e14b373b9d40bfb3c0562ae` / EXSRC-571337373f995b25 | identity only; resolve in original archive |
| Conditional measures of determinantal point processes | `0623831a2058eb76b94d2804fc8e419668c622cc38d11c9582067e52a5e47c8a` / EXSRC-0623831a2058eb76 | identity only; resolve in original archive |
| Conditional negative association for competing urns | `6bf59d792cd35b3520601c6341ad3548d30c8a93c0f7e541ec93e5e4e83aa2e2` / EXSRC-6bf59d792cd35b35 | identity only; resolve in original archive |
| Balls and bins: A study in negative dependence | `1c7f24edb807198f51c1cfb6d0be77819672aaa7c6b4c9ea787ead830909e5ab` / EXSRC-1c7f24edb807198f | identity only; resolve in original archive |
| Rank-three matroids are Rayleigh | `ce6007baabe2ca5f271cb2233d4a0927ab40e5ce263a60fd8386fec837faf55c` / EXSRC-ce6007baabe2ca5f | identity only; resolve in original archive |

## Explicitly withheld historical claims

The absent zero-quota `RN_DURRETT.md` and `RN_AARONSON.md` attachments are likewise
not installed by this overlay.  The historical count “31 scoped uses” is provenance,
not a present validation.  In particular, do not reactivate the Dubhashi–Ranjan
Theorems 31/37 route: the current `SKILL.md` records the unweighted conditional-
averaging proof gap.  Neither this registry nor the retained identities resolves A025
or A141.
