# Conditions-missing example: C118’s signed complete-graph threshold

C118 asks whether independent symmetric edge signs with mean parameter \(\delta\) give high-probability global synchronization of the complete-graph rank-two phase model at
\[
\delta\ge(1+\epsilon)\sqrt{\frac{\log n}{2n}}.
\]
The formal question is recorded in [`problem-boundaries.md`](../references/problem-boundaries.md). The obstruction is uniformity over the phase/configuration space: a concentration bound for one fixed phase vector does not by itself control all configurations or all second-order critical points.

PGEL-001 Theorem 3.2 is the closest direct model-family source. At \(p=1\), it proves a sufficient all-second-order-critical-point regime whose small-\(\delta\) scale is approximately \(\sqrt{2\log n/((1-\eta)n)}\), for fixed \(\eta\in(0,1)\). That is larger than C118’s proposed scale, by about \(2/\sqrt{1-\eta}\). It supplies a partial sufficient region and leaves the target threshold unresolved.

Do not fill the gap by importing positive-edge results, directed/signed deterministic results, a finite net without a valid approximation bound, or numerical evidence. A proof still needs a uniform phase-space argument at the target scale and a rigorous link from that argument to global synchronization. The available W24 sources do not supply this interface; C118 remains auxiliary/open in this package.
