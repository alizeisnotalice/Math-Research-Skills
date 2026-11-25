# Positive examples: route by the exact model

## A136: one binary hierarchy statement, no general SIRSN conclusion

Suppose the source model is Aldous's randomized binary hierarchy with \(1/2<\gamma<1\), and \(U_i\) are iid uniform disk points independent of one shared network. Route to the derived M0092 consequence only after checking those conditions: \(\mathbb E\sup_i\operatorname{len}r(0,U_i)\le\sqrt2K_\gamma\). The source's general OP34 remains open. The exact scope, derivation label, and transfer limit are on M0092（本机附件：`cards/M0092.md`）; the disk-radius and marginal checks are in batch01 results（本机附件：`evidence/python/batch01/independent_math_results.json`）.

For the general axiomatic question, record the single-route marginal and the iid endpoint maximum as different quantities. The exact uniform-disk radius calculation yields \(\mathbb E(1/|U|)=2\), while \(\max_{i\le n}1/|U_i|\) diverges in probability as \(n\to\infty\). This is only a missing-dependence illustration; the computation does not construct a compatible SIRSN counterexample.

## A027: keep stationarity, equality, ergodicity, and inducing separate

For the LPP1995 route, first verify the leafless GW assumptions, finite mean, simultaneous transience of all GW descendant subtrees, and the source's exact all-child flow positivity condition. Then use the local LPP1995 card（本机附件：`cards/LPP1995ERGODIC.md`） in order: AGW reroot-chain stationarity/reversibility; Proposition 5.1 equality-of-flow zero-one under \(\Theta+\Theta'>0\); Proposition 5.2 child-subtree chain ergodicity under strict \(\Theta>0\); Theorem 8.1 normalized induced HARM probability and tower argument. Do not infer ergodicity from equivalence alone.

## PZ08 critical marked ray: cylinder balance only

At parent weight \(\lambda=m\), no leaves, and the source exponential offspring-moment condition, use Lemma 2's finite-cylinder detailed balance for IGWR. The admitted card gives the root and strict-ray-ancestor laws. The separate disputed RN sentence is excluded by the R03 neutral review; the actual exact arithmetic is copied in PZ08 output（本机附件：`evidence/neutral/PZ08_R03_exact_results.json`） and the high-reviewed theorem interface is here（本机附件：`cards/PZ2008CLT.md`）.

## Other narrow positive calls

- For a Poisson close-pair question, M0100's tail is for the source's intensity-normalized typical unordered pair, with \(r\ge r_0\) and \(d\ge r\); it implies infinite mean for that law only. See M0100（本机附件：`cards/M0100.md`）.
- For positive speed in Aïdékon 2014, verify \(\lambda\in(\lambda_c,m)\), survival conditioning, finite mean, and artificial-parent reflection before using the marked-backbone ratio. The regular-tree exact speed examples are in batch03 results（本机附件：`evidence/python/batch03/independent_math_results.json`）; they check formula arithmetic, not the theorem.
- For the Aldous Shape Proposition 4 interface, retain the R09-repaired cutoff \(J=\max(2,\lfloor K^{1/4}\rfloor)\), not the printed non-vanishing choice. The R09 derivation review（本机附件：`evidence/neutral/Shape09_R09_review.json`）, R09 output（本机附件：`evidence/neutral/Shape09_R09_actual_parameter_results.json`）, and batch04 output（本机附件：`evidence/python/batch04/independent_math_results.json`） provide exact finite checks of \(J/\sqrt K\); the proof remains the source inequalities plus R09's local derivation, not those finite samples.
