# Exact rational second-order-cone support cut

For the second-order cone \(\mathcal L_d=\{(u,t):\|u\|_2\le t\}\), a supplied unit vector \(q\) gives the valid support inequality \(q\mathbin\cdot u\le t\). The finite checker accepts rational `direction=q`, `point=u`, and nonnegative `height=t`, verifies \(\sum_iq_i^2=1\) exactly, and reports the cut violation. A positive violation proves that the supplied point is outside the cone, by Cauchy--Schwarz.

This is one conservative separation certificate. It does not compute a projection, choose a support direction, establish numerical floating-point soundness, solve a MISOCP, or imply convergence of an outer-approximation algorithm.

The source uses this support geometry in the polyhedral MISOCP outer approximation. Checked local version is arXiv:2608.10055v1, physical pp. 4--5, Proposition 2.1 and the residual/support discussion. The wider angular, volume and partial-integrality claims use further hypotheses and are outside this component.

Run `python3 scripts/certify_soc_support_cut.py examples/soc-support-cut-3-4.json`.
