---
name: probability-forests-electrical-networks
description: Analyze uniform and minimal spanning forests, electrical networks, mass transport, unimodular random networks, and related finite spanning-tree inequalities.
---

# Probability on forests and electrical networks

本次整理与历史阅读/审核状态的区别，以及可选本地附件的访问方式，见 [证据与迁移说明](../math-research/references/evidence.md)。

Use this skill for uniform spanning trees/forests (UST, FSF, WSF), minimal spanning forests (FMSF, WMSF), electrical networks, MTP/unimodularity, and invariant random structures on graphs.

Start by naming the exact random object and its construction. Weighted finite UST, free/wired exhaustion limits, and free/wired minimal forests are different measures; state which boundary condition, edge weights/labels, and limiting procedure are in force. Record local finiteness, connectedness, transitivity or quasi-transitivity, unimodularity, conductance bounds, transience, and (\theta(p_c)=0) when a theorem uses them.

For a theorem application, check the assumptions against [the method guide](references/method.md), then locate its theorem card and exact PDF page in [the source guide](references/sources.md). Preserve theorem numbers, versions, and errata. Treat an open problem as open unless a cited source proves the same statement under matching assumptions.

For BLPS, keep the finite single-edge identity (Theorem 4.1) distinct from the unnumbered multi-edge Transfer Current Theorem (eqs. (4.4)–(4.5)). In the infinite resistance-energy flow space, the free current is \(P_{\Diamond^\perp}\chi^e\), and the wired current is \(P_{\star}\chi^e\); do not describe both as projections onto cycle-flow spaces.

Use Python exact arithmetic or MATLAB for finite examples and checks when useful. Save the input and output. A computation can verify a finite instance or catch an algebra error; it is not a proof of an infinite-network theorem. See the stored transfer-current example and the MST counterexample in `examples/`.

For A141, projection-determinantal formulas, rooted-forest determinants, and effective-resistance identities are exact finite-law context; they do not prove BK for configuration-dependent disjoint witnesses. For B064, the independent-thinned-WUSF result gives a connected-augmentation special case on \(\mathbb Z^d\), \(d\ge3\), while the arbitrary-Cayley-graph problem remains open; see the source cards before transferring either result.

This W07 skill covers the forest/electrical/MTP portion of the formal 120-question set. Tree-biased walks, harmonic measure, and SIRSN random spatial geometry belong to W20; do not duplicate them here.

The corpus remains in progress: 41 candidates, 32 local PDFs, 30 full-text reads, 1 partial read, and 1 acquired unread (see `evidence/W07/status.json` and `evidence/W07/reading_coverage.json`). The four L13_final4 reads are integrated with complete article coverage; PTN and Doyle–Snell book units remain incomplete. All new source and mapping reviews remain pending.
