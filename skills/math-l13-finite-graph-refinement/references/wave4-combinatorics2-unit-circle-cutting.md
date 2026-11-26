# Unit-circle cutting and balanced rectangle ledger

Source: *A power saving for planar unit distances*, SHA-256
`72bfa9153772b2124385cf4e53a5557320ab92e29fe4bdcb35a05a34481aede0`,
Lemma 2.2 and Propositions 2.3--2.4 (physical pp.5--8).

For a finite point set \(P\), \(l\) distinct unit circles, and \(R\ge1\), sample
\(s=\lceil CR\log(2+l)\rceil\) circles.  After deleting sampled-circle points,
the surviving points admit assignment to \(O(1+s^2)\) open cells, each crossed by
at most \(l/R\) original circles.  The required hypotheses are specifically the
two unit-circle pair bounds (two circles meet at at most two points; two points
have at most two unit-circle centres) and the stated open-boundary convention.

The downstream incidence interface is
\[
 I(P,Q)\le C\log^2(2+|P|+|Q|)
 (|P|^{2/3}|Q|^{2/3}+|P|+|Q|).
\]
Under the source's \(t^3\)-point, \(t^{4-o(1)}\)-ordered-unit-pair premise,
Proposition 2.4 then selects an induced rectangle with its displayed degree,
marginal, and subset-capture bounds (2.2)--(2.5).  This is a conditioned
finite-incidence preprocessing route, not a standalone power-saving proof.

## 固定来源

- 物理页 5, 6, 7, 8。Lemma 2.2 and Propositions 2.3--2.4 (physical pp.5--8) SHA-256 `72bfa9153772b2124385cf4e53a5557320ab92e29fe4bdcb35a05a34481aede0`。[A power saving for planar unit distances](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-power-saving-for-planar-unit-distances-September-23-2026/paper.pdf)
