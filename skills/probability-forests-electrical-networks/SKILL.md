---
name: probability-forests-electrical-networks
description: Analyze uniform and minimal spanning forests, electrical networks, mass transport, unimodular random networks, and related finite spanning-tree inequalities.
---

# Probability on forests and electrical networks

本次修订的来源范围、原文链接与审核状态，见 [来源与审核状态](references/sources.md)。

Use this skill for uniform spanning trees/forests (UST, FSF, WSF), minimal spanning forests (FMSF, WMSF), electrical networks, MTP/unimodularity, and invariant random structures on graphs.

Start by naming the exact random object and its construction. Weighted finite UST, free/wired exhaustion limits, and free/wired minimal forests are different measures; state which boundary condition, edge weights/labels, and limiting procedure are in force. Record local finiteness, connectedness, transitivity or quasi-transitivity, unimodularity, conductance bounds, transience, and (\theta(p_c)=0) when a theorem uses them.

For a theorem application, check the assumptions against [the method guide](references/method.md), then locate its theorem card and exact PDF page in [the source guide](references/sources.md). Preserve theorem numbers, versions, and errata. Treat an open problem as open unless a cited source proves the same statement under matching assumptions.

For BLPS, keep the finite single-edge identity (Theorem 4.1) distinct from the unnumbered multi-edge Transfer Current Theorem (eqs. (4.4)–(4.5)). In the infinite resistance-energy flow space, the free current is \(P_{\Diamond^\perp}\chi^e\), and the wired current is \(P_{\star}\chi^e\); do not describe both as projections onto cycle-flow spaces.

Use Python exact arithmetic or MATLAB for finite examples and checks when useful. Save the input and output. A computation can verify a finite instance or catch an algebra error; it is not a proof of an infinite-network theorem. See the stored transfer-current example and the MST counterexample in `examples/`.

For A141, projection-determinantal formulas, rooted-forest determinants, and effective-resistance identities are exact finite-law context; they do not prove BK for configuration-dependent disjoint witnesses. For B064, the independent-thinned-WUSF result gives a connected-augmentation special case on \(\mathbb Z^d\), \(d\ge3\), while the arbitrary-Cayley-graph problem remains open; see the source cards before transferring either result.

This W07 skill covers the forest/electrical/MTP portion of the formal 120-question set. Tree-biased walks, harmonic measure, and SIRSN random spatial geometry belong to W20; do not duplicate them here.

The 30-use forest cohort in calibration r5 and batch2 revision2 has passed R10 source-use review. The Schramm 2011 Selected Works chapter is L10’s one new full read. Supplemental HD planar use is accepted without extra quota credit; the corrected AL mass-transport/root-law use card v4 (Definition 2.1, PDF pp. 10–11) is accepted for this scoped use. PTN2026 remains partial and supplies no active positive theorem; its Chapter 11 caveat stays in a non-counted appendix. Final package decisions are recorded by the independent package reviews.

For finite checks use Python 3 with SymPy 1.14.0. Run the local check runner（本机附件：`scripts/run_finite_checks.py`） with `--output-dir` in the current research project or its data-volume temporary directory.

## Source-use boundary

Use the current, versioned source-use cards for any theorem-specific application. For a formally published result, verify the edition and the cited statement. For a claim supported only by a preprint, check the actual claim, relevant proof steps, assumptions and version before relying on it. Unavailable evidence and out-of-scope extensions remain research leads. Review and installation states in historical records refer to their own versions.

全文、附件与历史证据的定位见 [本机证据访问说明](../math-research/references/evidence.md)。

要同时保留割上界与生成树打包时，读 [原文构件](references/packing-preserving-sparsification.md)。

For a finite connected weighted spanning tree law, `scripts/check_finite_tree_response.py` exactly audits the covariance-row identity `sum_f |Cov(1_e,1_f)| = 2p_e(1-p_e) <= 1/2` from rational conductances.  The accompanying causal Brownian-sampler contract applies only after separately checking a countable coordinate set, jointly Borel drift, one uniform finite-tilt sup-norm response constant, and the relevant equivariant exhaustion; it is not a finitary-FIID claim.
