# Positive example: a proved sufficient regime for a signed landscape

**Input.** The graph edges are independently present with probability \(p\). Conditional on an edge, the signed entry is \(z_i z_j\) with probability \((1+\delta)/2\) and \(-z_i z_j\) with probability \((1-\delta)/2\), for a fixed planted sign vector \(z\). The coupling matrix is symmetric, the objective and rank-\(r\) sphere relaxation match PGEL-001, and \(\eta\in(0,1)\) is fixed independently of \(n\).

**Source result.** PGEL-001, Theorem 3.2 (physical PDF pp. 8–9), proves that if
\[
\frac{np}{\log n}\left(1-\sqrt{1-(1-\eta)\delta^2}\right)\ge1,
\]
then with probability tending to one every second-order critical point of the rank-\(r\) relaxation, for every \(r\ge2\), has \(YY^\top=zz^\top\). At rank two this gives the stated phase synchronization conclusion. The probability is over the graph/sign draw; the conclusion concerns every second-order critical point, not only almost every initial phase.

**Use.** This is a valid sufficient-regime statement when the model, objective normalization, independent edge law, and rank match the source. State the displayed inequality and fixed-\(\eta\) quantifier. The random signed proof reuses a cited concentration argument; the card records that dependency.

**Boundary.** For the C118 complete-graph threshold, this sufficient condition is about twice the proposed small-bias scale, up to the fixed slack. It does not prove the threshold or its necessity. See [the missing-interface example](conditions-missing.md) and [the PGEL-001 card](../sources/cards/PGEL-001.md).
