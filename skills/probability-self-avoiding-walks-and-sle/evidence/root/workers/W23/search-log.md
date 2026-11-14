# W23 SAW/SLE reading and source-check log

Batch date: 2026-11-14. This is the reader-side record; the D01 log records candidate discovery and lawful acquisition.

## Search, identity, and dedup

- Used the 45-item candidate inventory at `downloads/D01/saw_pool/sources.json` and the five-item handoff at `downloads/D01/saw_pool/handoff.json`. D01's primary-record search/acquisition record is `downloads/D01/saw_pool/search-log.md`; the complete candidate preflight is in `preflight.json`.
- Checked primary arXiv records for the three read papers: [1007.0575](https://arxiv.org/abs/1007.0575), [1809.00760](https://arxiv.org/abs/1809.00760), and [1203.6051](https://arxiv.org/abs/1203.6051). Publisher metadata cross-checks are [Duminil-Copin–Smirnov](https://doi.org/10.4007/annals.2012.175.3.14), [Duminil-Copin–Ganguly–Hammond–Manolescu](https://doi.org/10.1214/19-AOP1400), and [Lacoin](https://doi.org/10.1007/s00440-013-0520-1). These confirm title/authors/version/publication identity; full mathematical statements were read in the PDFs.
- Queried `catalogue/canonical_read_index.json` (567 entries) and worker source ledgers for the three papers' DOI/arXiv/title/hash. No accepted complete read was found for these exact works. The earlier `discovery-isolated/feasibility-L11` SAW-02/03 records are metadata-only and were not inherited as reading evidence.
- The global dedup list explicitly excludes Grimmett's *Selected Problems in Probability* as the same work already read under W05/MIR-05; it is not counted again. Two general SLE papers are reused from accepted canonical W08 full reads only for continuum background; R03 accepted the W23 usage evidence, while source-row metadata corrections have been resubmitted.
- No additional downloads were performed. The acquired but unread P02 (73 pp) and P15 (27 pp) remain assigned to a future reading batch; the 40 metadata-only candidates are not reported as reads.

## Full-text reading and checks

| Local ID | PDF and complete physical pages read | SHA-256 | Focused visual checks |
|---|---|---|---|
| W23S001 | `downloads/D01/saw_pool/papers/honeycomb.pdf`, pp.1–11 | `11335571f5118514b5f761ad3d750e11b5537b1390aa3444742339b86e65bb8a` | pp.2, 6; full radical and boundary/bridge identity |
| W23S002 | `downloads/D01/saw_pool/papers/polygon_insertion.pdf`, pp.1–56 | `a9fa6fda92abda1a20eca0f378b1565e37e8afa69f58a2a57acc0482b270d8f3` | pp.2–4, 14, 21–22, 28–29, 37, 39–40, 54–55; theorem ranges, polygon mechanisms, joins and formulas |
| W23S003 | `downloads/D01/saw_pool/papers/lacoin_planar.pdf`, pp.1–25 | `1a681dbf7831f0f5ecf8d555083fbf60367592e550d11cd4a384566182bbcb69` | pp.1, 3, 12–15, 17–18, 20; limsup/full-limit distinction and change-of-measure estimates |

Physical page means the PDF page index; the article's printed page number was separately checked on rendered pages where relevant. Every physical page, including figures, appendix where present, and references, was read sequentially. Section-by-section proof-mechanism coverage is in `workers/W23/reading_coverage.json`.

## Actual local calculation

`workers/W23/math/check_claim_constants.m` was rerun using the connected local MATLAB service after R03 flagged a model-mixed numerical example; result is `workers/W23/math/check_claim_constants_results.txt`. The revised script checks only honeycomb identities/fugacity and the source-derived polygon-insertion threshold arithmetic. It does not substitute the honeycomb connective constant for the unknown square-lattice μ2 or evaluate Lacoin's gap at an arbitrary block size. The separate `math/lacoin_strict_gap_interface.m` requires a sourced certified upper bound for the Z² connective constant and proof-admissible C2 before it can compute a conditional numeric output; neither is supplied in this batch. Floating-point checks are not proof evidence.

## Batch status

At the initial calibration checkpoint, three unique papers had complete reads and two canonical SLE usages were accepted by R03, for a potential count of 5/30 and a gap of 25. The initial five-source calibration subsequently passed R03; see the continuation record below for the added full texts and current pending-review state.

## R03 correction check, 2026-11-14

- Rendered honeycomb PDF p.4 and corrected the paired path winding offsets to `W_common - 4π/3` and `W_common + 4π/3`; their difference is `8π/3`.
- Rephrased the square-lattice polygon-insertion conclusion as **upper asymptotic density one**, derived from the infinitely many intervals `[j,j^(4/3)]`; no natural-density existence is asserted.
- Removed the Lacoin calculation that combined the honeycomb μ with a square-lattice theorem and an arbitrary `N0=10^4`. The revised actual MATLAB output now contains only honeycomb checks and separate threshold arithmetic. The Z² interface is conditional on properly sourced inputs and was not numerically run.
- Corrected Beffara's arXiv record to [math/0211322](https://arxiv.org/abs/math/0211322), version v3, and Rohde–Schramm's journal pagination to [Annals pp. 883–924](https://annals.math.princeton.edu/2005/161-2/p07); the canonical local PDF remains the 51-page arXiv v4 version.
- These edits do not alter R03's review files or the three accepted full-reading records/two accepted continuum-only usage decisions. Source/skill stage awaits rereview.

## Continuation full-text batch, 2026-11-14

- Read the existing D01 handoff rows SAW-P02 and SAW-P15 from `downloads/D01/saw_pool/sources.json`; did not download or edit the D01 acquisition files. Identity/version and SHA-256 were checked against that handoff and the actual local PDF first/last pages. Cross-searched `catalogue/canonical_read_index.json`, `catalogue/master_sources.json`, and local worker ledgers by title, DOI, arXiv ID and hash. P02 has a D01 discovery/acquisition row only; P15 also has a metadata-only SAW-04 discovery row. Neither was previously accepted as a complete read.
- P02 local PDF: `downloads/D01/saw_pool/papers/lecture_notes.pdf`, arXiv:1206.2092v1, 73 physical pages, SHA-256 `48c4c9d89ff352a28de9e3e43dc92b7e2bca4e7a758cacac3503aaa58e6727a6`; read pages 1–73 sequentially, including all appendices/tutorial solutions, acknowledgements and references. Section summaries and proof mechanisms: `workers/W23/reading_coverage.json#sources.W23S006`; theorem/proof/model card: `workers/W23/cards/W23S006.md`.
- P15 local PDF: `downloads/D01/saw_pool/papers/subballistic.pdf`, arXiv:1205.0401v1, 27 physical pages, SHA-256 `305f1a61d23c0bd2241530e054874f74bea0a95b08010fc9087e6ad7f1f7c8d6`; read pages 1–27 sequentially, including all references and end matter. Section summaries and proof mechanisms: `workers/W23/reading_coverage.json#sources.W23S007`; theorem/proof/model card: `workers/W23/cards/W23S007.md`.
- Rendered P02 pp.13, 17, 20, 26, 50 and P15 pp.1, 10, 13, 24. These checks verified the Hammersley–Welsh threshold and dimension range, bridge-to-polygon inequality, high-dimensional strict-SAW theorem statements, the continuous-time weak-SAW model, Theorem 1.1 quantifiers and bridge comparison, zigzag-unfolding figure, and stickbreak counting geometry. The rendered images are in `workers/W23/text/`.
- Ran `workers/W23/math/check_p02_exact_identities.m` through the connected local MATLAB MCP and saved the actual output. It verifies numerical consistency of the honeycomb radical/fugacity identities, phase cancellation and the numeric Hammersley–Welsh threshold only; it is not proof evidence. The exact proof statements and their assumptions come from the complete PDFs.
- This continuation adds two unique full-text sources to the three prior complete reads; with two R03-accepted canonical SLE usages, the potential W23 count is now 7/30, leaving 23 further relevant unique sources. The initial five-source calibration passed R03; the new two source rows/cards and canonical skill update are pending independent review. The 40 other D01 pool entries remain metadata-only candidates.
- Skill migration: copied the draft slug to `skills/probability-self-avoiding-walks-and-sle/` byte-for-byte before canonical edits. `workers/W23/skill-migration-manifest.json` preserves the initial tree hashes; the draft remains untouched and only the canonical path is maintained after migration.


## R03 batch-2 correction, 2026-11-14

- Re-rendered and visually inspected P02 physical p.12 (Theorem 2.4), p.13 (Theorem 2.6), and p.48 (Theorem 6.11 Eq. (6.43)). The original partition entropy is `log P_D(A)~pi*sqrt(A/3)`; Theorem 2.6 retains `B>pi*sqrt(2/3)` because the last-minimum split contributes two partition factors. Eq. (6.43) has the full differential-form integral on the RHS, under finite-`Lambda` and positive-Hermitian-part assumptions.
- Re-rendered and visually inspected P15 physical p.18. Corollary 2.4 assumes infinite irreducible-bridge mean and derives exponential decay for renewal-rich bridges (including the bridge-conditioning `exp(C sqrt(n))` cost), contradicting Theorem 2.3 under ballisticity; the direction is not finite mean to exponential tail.
- Kept P15 Theorem 1.1's literal source wording while documenting the exact `n=1,v=1/2` boundary case. Executed the finite enumeration in local MATLAB; code and captured output are `workers/W23/math/check_p15_finite_n_counterexample.m` and `_results.txt`. This verifies only the finite counterexample; the skill applies the result asymptotically or with a finite prefactor.
- Updated only W23 cards, coverage, source rows/status/response/log, and the canonical W23 skill. R03 review files, first-five cards, D01 acquisition records, and L08 helper were not edited. All review statuses remain pending.


## R03-passed L08_B2 evidence mirrored into the mother ledger, 2026-11-14

- Verified `reviews/R03/w23_L08_B2_review.json` decisions and `w23_L08_B2_stage_hashes.json`. All three sources passed helper-stage review with accepted full-text evidence; source PDF hashes match D01 and the reviewer records. Stable mapping is SAW-P07 helper W23S006 → mother W23S008, SAW-P09 helper W23S007 → mother W23S009, and SAW-P10 helper W23S008 → mother W23S010.
- Copied the complete helper cards and source/coverage/mapping evidence into the mother IDs. Card changes are limited to the stable ID, L08 reader/mother-pending attribution, evidence paths, and P07's copied tree-count script path. The mathematical card text was preserved; no local-PDF hashes changed.
- Copied the inspected render pages and extracted full-text files byte-for-byte into `workers/W23/text/`, plus the finite tree-enumeration script/result into `workers/W23/math/`. File hashes and the allowed-diff manifest are in `workers/W23/mirror_manifest_L08_B2.json`.
- Updated C107 auxiliary source mapping and canonical method/source references. These graph-SAW results add scalar growth tools only; the lattice-SLE and C108 interfaces remain unproved. The mother source rows remain `review_status: pending` until R03 checks the stable-ID/hash binding.
- No new source search/download or paper read occurred in this mirror step. The helper directory, its R03 review, the first seven mother proof cards, and prior batch-2 corrections remain unchanged.


## R03-passed L06_B4 three-source mirror, 2026-11-14

- The already acquired D01 stock PDFs SAW-P11, SAW-P13, and SAW-P14 were read in full by L06: 25, 27, and 14 physical pages. Their exact local PDF SHA-256 values are `0db12154d0cf548abf542dd67fa8d2d7dd714f3b1e1dd874e878fd17d9c20dc0`, `faf14f9216dc2588d7b7eb8c5e0d6ef1968c10c57358a0d23078bec6f6139cc9`, and `554b3d961903e16ce3bd14cbba9d8b816ac447299f889203daa6e5cf52e44cb`; every physical page, theorem/proof tail, end matter, and references is in `workers/W23/reading_coverage.json`. No new downloads occurred.
- R03 accepted all three helper-stage identity/full-read records. Stable pool-based mother IDs are P11→W23S011, P13→W23S012, P14→W23S013; the helper IDs remain provenance fields, not mother IDs. Mother hash binding is pending R03.
- Re-ran `workers/W23/math/check_finite_saw_and_bridge_roots.m` with local MATLAB MCP. The script now writes the actual result using explicit `fopen`/`fprintf` and `jsonencode`: `workers/W23/math/finite_math_check.txt` and `.json`. Observed reciprocals are 6.649927048190 and 3.103803402736; the finite 3-regular tree counts are 1,3,6,…,1536 through n=10. The old zero-byte diary was retained unchanged as `workers/W23/math/finite_math_check.empty_diary_diagnostic.txt`; it is not evidence of output. These checks are finite consistency only.
- The cards, source rows, coverage, mapping, render pages, extracted text, runtime artifacts, and canonical method/source references were mirrored under the stable IDs. Full card/math content is retained; only stable IDs, reader/helper provenance, evidence paths, and the actual-output capture note were added. The sync hashes and allowed diff are recorded in `workers/W23/mirror_manifest_L06_B4.json`.
- All 13 source entries remain pending review at the mother level. The potential evidence count is 11 unique complete reads plus 2 accepted canonical usages, 13/30; 17 eligible unique sources remain to the minimum target. C107 still lacks lattice curve tightness/DMP/SLE identification, and C108 still lacks quenched full-limit existence/root independence.

## L08_B5 mother mirror (2026-11-14)

R03 passed helper-stage identity, metadata, full-text and complete-coverage review for SAW-P16, SAW-P18 and SAW-P24 (55 physical pages total). Stable IDs are W23S014, W23S015 and W23S016. The source PDFs are the unchanged D01 files; helper text extracts, all inspected renders and all four math evidence files were byte-copied into the W23 mother evidence folders. Bibliographic/version cautions and theorem scope flags remain in the cards. Mother source/card/coverage hash binding remains pending R03; no skill or review file was changed. See `workers/W23/mirror_manifest_L08_B5.json`.

## L06_B6 helper-stage-passed mother mirror (pending binding)

R03 passed the B6 helper stage for SAW-P31/P41/P45. Stable IDs were assigned by pool ID and exact local PDF SHA-256: P31→W23S017, P41→W23S018, P45→W23S019. The 16 previously accepted mother sources are unchanged. The three new mother rows and complete coverage are staged pending R03 mother-binding review and are not included in quota counts yet. P41’s two-page erratum is bound as same-work correction evidence with zero separate quota credit. See mirror_manifest_L06_B6.json for per-file hash/diff audit.


## 2026-11-14 — L10_B7 mother mirror (pending R03 binding)

- Mirrored SAW-P46/P47/P49 as W23S020–W23S022 after all three passed the R03 helper-stage review; all 73 helper-stage hash entries were rechecked.
- The D01 aliases P08/P12/P20 are the same works, not extra source credits. The prior 19-source count includes the R03-passed L06_B6 binding; these three new mother bindings remain pending, so accepted quota stays 19.
- Copied complete text extracts, all 53 rendered pages, and the actual MATLAB script/output byte-identically. C107 gains auxiliary graph methods only; its planar curve-limit/SLE interface remains unproved.
