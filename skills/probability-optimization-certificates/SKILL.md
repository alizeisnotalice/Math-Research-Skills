---
name: probability-optimization-certificates
description: Build and audit finite-dimensional optimization bounds and proof certificates used inside probability arguments, including duality, interval validation, and exact LP/MIP checks.
metadata:
  short-description: Certified optimization bounds for probability proofs
---

# Probability optimization certificates

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill when a probability or online-selection argument relies on a finite LP, convex program, SDP, or integer program as a rigorous bound or computational certificate.

First write the primal and dual with their sign conventions, variable domains, and objective orientation. Verify weak duality directly from feasibility. Keep strong duality, attainment, minimax exchange, and convergence as separate claims; state the qualification or compactness assumptions for each one.

Treat a solver status or decimal solution as a candidate. For finite rational models, check primal and dual feasibility and the objective gap with exact rational arithmetic where practical. For floating-point computations, use a rigorous residual or interval enclosure with outward rounding and check every denominator, eigenvalue, and sign condition that enters the bound. Record numerical exploration separately from exact or interval-verified evidence.

For integer models, validate integrality, every rounded cut, and full branch coverage in the certificate. For SDP or other conic programs, distinguish a relaxation bound from exactness and state strict-feasibility or facial-reduction assumptions; weak duality alone does not imply zero gap or attainment.

For polynomial nonnegativity, SOS is an SDP certificate; DSOS and SDSOS are cheaper LP/SOCP inner certificates and may be conservative. In branch-and-bound, a quasi-lower bound may be valid only on boxes containing a global minimizer, so pruning must use the algorithm's minimizer-retention proof. Formalized exact LP/polyhedral theorems and numerical validation of a particular solver output are different kinds of evidence.

Read [references/method.md](references/method.md) for the certificate workflow and failure boundaries. Use [references/sources.md](references/sources.md) to locate this stage’s source inventory, reading cards, and read statuses. The 30-source set (29 complete papers and one complete acquired book with Chapter 5 fully read) has passed R08 independent review. Reader-side `review_status: pending` fields remain in the ledger; unread inventory entries are candidates, not theorem evidence. The cards record precisely which source pages were read.

For A001/A002/A005, use finite certificates only for their finite subproblems. A separate argument must establish the analytic interface: topology/compactness for minimax, arrival and atomicity conventions for online policies, and every passage to a distributional or (n\to\infty) limit. See the worker mapping in `evidence/W19/mapping.json`.

For generalized-moment ratios, retain positive event-probability assumptions and distinguish value equality from attainment; the mean–variance bound in S010 also requires positive variance for its infinite branch. For Farkas/image tests, distinguish closure from exact membership, and for moment-cone representation verify compactness before using a dual-cone equivalence. For conic error bounds, verify the cone class, face chain, PPS condition, and norm bounds stated by the cited theorem. The W19 cards for S003/S010/S011/S012 and S014/S015 record these scope boundaries.
