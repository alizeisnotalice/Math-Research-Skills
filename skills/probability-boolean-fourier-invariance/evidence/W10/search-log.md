# W10 search and acquisition log

**Last updated:** 2026-11-14; L08 and D04 integration appended below.  
**Scope:** Boolean Fourier analysis, coordinate influences, noise sensitivity/stability, invariance, bounded independence, Boolean/Gaussian PTF links. Reader: W10.

## Registry coverage

- Preserved all 37 assigned seed375 records M0110–M0146 in `sources.json`; fields `seed_origin=seed375` identify them. They are not silently counted as read. Five seed entries (M0116, M0119, M0121, M0125, M0127) were retained but have no verified direct Boolean-Fourier interface in this pass and are excluded from the relevant-candidate count.
- Added 17 topical/boundary records, including primary sources for KKL, BKS, MOO invariance, Gaussian k-independent PTFs, and the influential-coalition conjectures. The source registry currently has 55 rows including one audit-only identity-conflict row; 49 active records carry at least one W10 topic tag.
- The principal local full texts are in `evidence/W10/papers/`. `papers/seed/Mxxxx.pdf` is not identity-verified from its filename alone. Only record a shared seed PDF after checking its title page.

## Searches and primary sources

Queries run through web search on 2026-11-13:

- `"The influence of variables on Boolean functions" Kahn Kalai Linial 1988 DOI` — FOCS/Dagstuhl record and the author-hosted PDF at <https://www.ma.huji.ac.il/~kalai/kkl.pdf> identify Kahn, Kalai, Linial; DOI 10.1109/SFCS.1988.21923.
- `"Influences in Product Spaces: KKL and BKKKL Revisited" Conjecture 2.6 Friedgut 2004` — Cambridge issue metadata; author-uploaded text at <https://www.researchgate.net/publication/2840412_Influences_in_product_spaces_KKL_and_BKKKL_revisited>. Read Conjectures 2.2, 2.6, nearby discussion, and Theorem 1.4. This resolved the ε mismatch in the Simons compilation: the original Conjecture 2.6 is a fixed-ε, O(log n)-coalition statement. Its displayed line omits monotonicity, while §1 restricts to monotone functions and says KKL shifting loses no generality for its purposes; preserve that context and do not silently extend it to arbitrary fixed assignments.
- `"A Brief Introduction to Fourier Analysis on the Boolean Cube" de Wolf DOI` — primary Theory of Computing page/PDF at <https://theoryofcomputing.org/articles/gs001/> and <https://theoryofcomputing.org/articles/gs001/gs001.pdf>; full 20-page text read in the browser. Local curl attempts failed TLS certificate validation; no TLS bypass was used.
- `"Noise stability of functions with low influences: Invariance and optimality" MOO 2010` — primary Annals PDF at <https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p05-p.pdf>; title/authors, definitions, and selected theorem/proof pages read. Local 50-page copy verified.
- Direct arXiv metadata/PDF checks: <https://arxiv.org/abs/1012.1614> (Kane, v3), <https://arxiv.org/abs/1201.3261> (Benjamini–Gurel-Gurevich–Peled), <https://arxiv.org/abs/1409.3033> (Bourgain–Kahn–Kalai), <https://arxiv.org/abs/2609.16401> (Chattopadhyay–Gurumukhani v2), and <https://arxiv.org/abs/2610.03086> (Friedgut v1). Local papers' first pages were checked before attaching them to records.

## Identity conflicts and failed acquisition

- A file previously named `KKL1988_influence_arxiv_reprint.pdf` was arXiv:math/9811157v2, the 46-page BKS noise-sensitivity paper, with a hash identical to `BKS1999_noise_sensitivity.pdf`. The mislabeled duplicate was removed. M0112 records this conflict; BKS1999 keeps the valid file. This wrong arXiv ID is not counted as a KKL copy.
- An old `booleansurvey.pdf` is arXiv:1208.0775v1, *Magneto-orbital helices and multiferroicity*. It remains an audit-only row, not a Fourier source. At that earlier stage, no correct local copy had been verified; this was superseded by the D02 copy and L08 full read recorded in the dated integration below.
- DOI gateway direct opens for the KKL conference record and Cambridge's Friedgut article endpoint were inaccessible in the browser. Metadata was cross-checked with FOCS/Dagstuhl, the Cambridge issue record, arXiv, and the author-hosted primary PDF/text. The local author PDF attempt for KKL failed TLS hostname validation; no TLS verification was disabled.
- `swift .../pdf_text.swift` could not initialize its Clang module cache in the default protected cache. The task's copied/local PDFs already have extracted text; no system installation or permission bypass was attempted.

## Reading and acquisition queue

Actual reading is recorded per source in `sources.json`; canonical cards are present for sources actually read. All 37 seed records remain present, including unread entries without local PDFs. Current reading queues and page-coverage counts are maintained in `evidence/W10/status.json`. Continue with the remaining partial-read queue and highest-value Fourier-sparsity/dimension papers; continue checking post-2014 resolution or counterexamples to A165 and B162 before calling either open/current.

## Coverage caveat

This is a staged batch for independent calibration, not a completed literature review. Current counts are in `evidence/W10/status.json`; the separate audit-only wrong-file row is excluded from active bibliographic counts. `review_status` remains `pending` throughout.

## 2026-11-14 reading and source corrections

- D02 files `evidence/fulltexts/M0113.pdf` (22 physical pages) and `M0114_NisanSzegedy_1994.pdf` (13 pages) were title-page checked, hashed, and read in full. M0113’s physical PDF page order is reversed relative to its printed 22-page author manuscript; its SIAM DOI record verifies the 1993 journal version and pages 1331–1348. The Princeton-hosted full manuscript was also opened for title/authors and theorem context. M0114’s local title page and DOI metadata match *Computational Complexity* 4 (1994), 301–313.
- Primary-record web checks: SIAM page `https://epubs.siam.org/doi/10.1137/0222080`; Annals page `https://annals.math.princeton.edu/2019/190-3/p06`; arXiv pages `https://arxiv.org/abs/1201.3261` and `https://arxiv.org/abs/1012.1614`; Numdam record `https://numdam.org/item/PMIHES_1999__90__5_0/`. These confirmed title/authors/publication metadata; theorem formulas and pages were checked against the local full texts.
- Huang Theorem 1.3 is recorded with monotone (h) and \(\Gamma(H)=\max\{\Delta(H),\Delta(Q_n-H)\}\); Lemma 2.3 is physical p. 4 and the proof continues p. 5. BGP’s equation (6) is the unstandardized \(\operatorname{Bin}(n,1/2)\) estimate \(\rho_m(n/2)\le2/\sqrt m\), used with \(m=k/2\); Theorem 16 is physical p. 7 and its proof p. 8. The XOR lower construction now preserves the parity-dependent positive-bias choice. BKS Theorem 1.9 explicitly excludes the constant level, \(1\le|S|\le k\). Kane’s general theorem and explicit physical-p. 8 bound are separated, with \(O(\epsilon)\) expectation error and full section coverage.
- Exact problem mappings A019 and A166 were added after checking `inputs/formal120.json`: A019 is iterated majority of threes (not arbitrary multi-level majority); A166 uses input nonzero support (m), not Fourier support. The conditional expectation identity is a route; the target lower bound remains unproved.


## 2026-11-14 handoff update — M0118 identity artifact

D02 supplied `evidence/fulltexts/M0118.pdf`. Its physical PDF p. 1 was visually checked for the title “A Brief Introduction to Fourier Analysis on the Boolean Cube” and author Ronald de Wolf; PDFInfo reports 18 pages and SHA-256 is `af3e5ab244e4c6c89fcf2ad4bdfa8945138ef400f3d53ff7eca1cfc0f5d81e85`. The artifact identity is now verified. The later L08 full read, hash/page-count check, and full physical-page map are recorded in the integration section below.


## 2026-11-14 L08 full-read integration and D04 identity import

- Integrated helper L08’s complete reads of M0118, KKL2014, and CG2026 into the mother ledger and canonical `evidence/W10/cards/`. The identity hashes and physical page counts match the files; the coverage maps span every physical page (M0118 1–18, KKL2014 1–21, CG2026 1–18). Helper provenance remains in each source row/card and the original `reader_batches/L08_batch1/` evidence remains intact. M0118 uses the correct CWI/ToC copy; the unrelated physics PDF remains rejected.
- D04 batch07’s eight new artifact hashes/sizes/page counts and two reused D02 paths were rechecked against the local files and imported as identity/acquisition evidence. No D04 article body was promoted to read. L08 batch2 owns M0123, DKN-HS, MZ-PTF, M0136, and M0124. M0111’s two-author 2011/CCC 2012 manuscript is stored as an alternate artifact; the registered three-author 2018 journal version remains unacquired and identity-pending. M0134 is the canonical seed record for the shared FKN2002 DOI/work; the topical FKN2002 row is marked alias to avoid duplicate-work counting.
- Registry counts and full/partial/not-read queues were refreshed in `evidence/W10/status.json`. The old M0118 acquisition-only status above is historical and superseded by this full-read record. All review statuses remain pending.

## L08 batch2 integration

Integrated the five complete reads M0123, DKN-HS, MZ-PTF, M0136, and M0124 into the W10 ledger, cards, full physical-page coverage, and source guide. Exact PDF hashes and page counts were rechecked; all remain independent-review pending. M0123 read-once is recorded as recursive branch-variable disjointness, and the Fourier-spectrum/sparsity entries retain their stated class limits.
