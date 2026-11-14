# Positive example: iid supercritical chemical distance

**Input.** Nearest-neighbour iid bond percolation on Z^d, fixed d≥2 and p>p_c. Let D(0,y) be the chemical distance when 0 and y are connected. Use the paper's l1 norm; conversion to Euclidean distance changes the constant by at most sqrt(d).

**Direct source statement.** Antal–Pisztora Theorem 1.1 (physical PDF p.3, printed p.1037, equation (1.3)) provides rho=rho(p,d)≥1 with

limsup as |y|_1→∞ of |y|_1^(-1) log P(0↔y, D(0,y)>rho|y|_1) < 0.

This is a **joint-event** estimate. Its proof uses good blocks, block domination, bad-cluster control and deterministic path repair. It is not stated as a conditional-probability theorem.

**Conditional corollary, with its extra argument.** For this iid supercritical lattice model, let theta=P(0 belongs to an infinite cluster)>0. FKG gives P(0 and y both belong to an infinite cluster)≥theta². Almost-sure uniqueness of the infinite cluster then gives P(0↔y)≥theta². Dividing the joint estimate by P(0↔y) changes its prefactor by at most theta^(-2), leaving its exponential limsup rate unchanged. This is a derived corollary using FKG and uniqueness, not a verbatim statement of Theorem 1.1.

**Evidence boundary.** For a different graph or dependent model, separately establish the block hypotheses and the connection-probability lower bound before transferring either conclusion. Finite-cluster computation does not prove the uniform large-distance estimate.
