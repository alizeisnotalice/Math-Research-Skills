# Penrose deformation and mass interfaces

All entries below are **Scoped reference.**  They retain source-specific
geometric constructions and hypotheses; none is a generic Penrose solver or
a verification of dominant energy, asymptotics, trapping, or outer minimization.

*A Charged Reduction of the Spacetime Penrose Inequality in Spatial
Dimensions at Least Four* (OpenAI, 5 Oct 2026), SHA-256
`3e5e445d305051a15f2f9925df4f38372f1fc0892ba516501d6e37795f1ba837`,
physical pp. 5--7, 31, 35--37, 42, Definitions 2.1--2.3, Theorem 2.5,
Lemmas 5.1/5.2/5.4 and the charged-curvature band estimate.  For `q>(n-2)/2`,
retain its exact AF falloffs `g-delta=O_2(rho^-q)`,
`K=O_1(rho^(-1-q))`, `E=O_1(rho^-k)`, its full-cut flux
`integral_Gamma i_E dV_g=omega_k Q`, and, after the neutral input, the
outer-branch bound `m >= (X_A+Q^2/X_A)/2` when `X_A>|Q|`.  The coupled solve
uses the stated trace equation for an arbitrary bounded `C^(1,alpha)` trial
scalar and preserves the electric curvature inequality
`R_gb/2 >= c_n^2 |i_E dV_g|^2_gb` on its original low-height region.
It applies only after its asymptotically flat initial-data, outermost/MOTS,
charge, dimension, and decay assumptions are supplied.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Charged-Reduction-of-the-Spacetime-Penrose-Inequality-in-Spatial-Dimensions-at-Least-Four-October-5-2026/paper.pdf).

*A local Penrose inequality for conformal perturbations of
Schwarzschild--anti-de Sitter data* (OpenAI, 5 Oct 2026), SHA-256
`624b287b6675a96256bf93ce5eefca9e08e04d6655f6808fd8529e6001b75012`,
physical pp. 6--8, 10, 12, 15, Theorem 2.1 and Lemmas 3.1/3.3,
Proposition 4.1.  With the specified TT seed and actual small solution
branch, its deficit is `D_q(eps)=m_AH(eps)-sqrt(A_eps/(16 pi))(1+A_eps/(4
pi))`; the stated local inequality is strict for sufficiently small positive
nonradial seeds.  The finite-angular inverse solves `L u=F` mode-by-mode and
the mass is represented by the exact Green formula (3.13).
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-local-Penrose-inequality-for-conformal-perturbations-of-Schwarzschild-anti-de-Sitter-data-October-5-2026/paper.pdf).

*Area-controlled end replacement and the Bondi Penrose inequality in the
CKS class* (OpenAI, 27 Sep 2026), SHA-256
`dbf670183435f2189936378a40363c6fa2f4ce746937ea430c465709ade4cb43`,
physical pp. 6--8, 10, 12, 14, Lemmas 2.1, 3.1, 4.1.  First Lorentz-balance
a strictly timelike Bondi charge so `f_*=M/4` has zero first spherical
harmonic; then the trace-free tensor equation `div_sigma T=d_S2 f` is
solvable.  The round-leaf collar uses
`c_R(r)=integral_R^r w(rho)rho^(-3/2)d rho`, with the stated interpolation
of `gamma,s,v,F,L,eta,tau`, to retain a DEC margin.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Area-controlled-end-replacement-and-the-Bondi-Penrose-inequality-in-the-CKS-class-September-27-2026/paper.pdf).

*Boundary graph deformations for the spacetime Penrose inequality* (OpenAI,
27 Sep 2026), SHA-256
`4205f51d8f1b130b487c27fa7243ad9f64747dfbfc1c7081ecb22f4030281379`,
physical pp. 7--8, 10, 12, 14--15, Definitions 2.1--2.2 and Theorem 2.3.
For prepared three-dimensional data with weighted strict DEC margin and
strictly future trapped boundary, the output metric obeys `R_g_hat>=0`,
`H_boundary(g_hat)<0`, `g_hat>=exp(-4 eps)g`, and every full enclosing cut
has area at least `exp(-4 eps) A_*`.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Boundary-graph-deformations-for-the-spacetime-Penrose-inequality-September-27-2026/paper.pdf).

*Conformal flow and the Riemannian Penrose inequality with minimizing
frontiers* (OpenAI, 27 Sep 2026), SHA-256
`d49778ad5b338b573424e49f07cc0f73af92d5bff4c9ffa16ae34d3ccf20853c`,
physical pp. 6--7, 9, 12, 15, Section 2, Proposition 3.3 and Lemma 4.3.
Use full intrinsic enclosing perimeter (including obstacle contact); its
discrete conformal flow is `h_j=u_j^(4/d)g_0`, outermost minimizing
enclosure `K_j`, harmonic velocity `v_j`, and update `u_(j+1)=u_j+eps v_j`.
The cited uniform density and area monotonicity are restricted to that
construction.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Conformal-flow-and-the-Riemannian-Penrose-inequality-with-minimizing-frontiers-September-27-2026/paper.pdf).

*Equality and rigidity in the spacetime Penrose inequality* (OpenAI,
27 Sep 2026), SHA-256
`4f1aab59ba484eb8a903daed582b30ffe17bbd42392e233213a30abb3aadc710`,
physical pp. 7, 9, 12, 15, Definitions 2.1--2.2 and the weak-support
enclosure construction.  Its usable interface fixes the full enclosing-area
infimum, retains all components/pockets, and converts a source-qualified
weak expansion support to a smooth enclosing boundary at a strictly larger
threshold.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Equality-and-rigidity-in-the-spacetime-Penrose-inequality-September-27-2026/paper.pdf).

*The Kerr--Newman Penrose Inequality for Axisymmetric Electrovacuum
Exteriors* (OpenAI, 5 Oct 2026), SHA-256
`ff3098c8faf29685970c83683b711fa03522f2ae7ac50f80f06d884da6cd71b3`,
physical pp. 6--7, 9, 12, 15, Theorem 2.2 and Propositions 3.5/3.8.  Under
the exact axisymmetric electrovacuum exterior assumptions, retain the mass
lower bound `m^2 >= A/(16 pi)+Q^2/2+pi(Q^4+4J^2)/A`; the axial potentials
are normalized by axis values `(-Q,0,-2J)` and `(Q,0,2J)` and reduce the
invariant field equations to `Ric_gamma=2 Phi^*G`, `Box_gamma Phi=0`.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Kerr-Newman-Penrose-Inequality-for-Axisymmetric-Electrovacuum-Exteriors-October-5-2026/paper.pdf).

*The Penrose inequality for maximal asymptotically hyperbolic initial data*
(OpenAI, 5 Oct 2026), SHA-256
`641d4aa3892adbca1c14c7bca0f165edc6b508e88f6b18880e3494a5495c39c2`,
physical pp. 4--5, 7, 10, 12, 15, Lemmas 3.2--3.5.  In the maximal AH
system the source derives `div Q=-(x-1)Sigma-P` and
`x^2(R_h+6)=x(D+|pi-K|^2)+(3/2)x|dx|^2+6(x-1)^2+2PN`, with
`D=16pi(mu-J.v)>=0`; its constant-height boundary identity controls the
directed mean curvature used in gluing.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-Penrose-inequality-for-maximal-asymptotically-hyperbolic-initial-data-October-5-2026/paper.pdf).

*The nonmaximal anti-de Sitter Penrose Inequality and original-data
rigidity* (OpenAI, 5 Oct 2026), SHA-256
`9e2b9ba2768918dcc5b8abd44ad47e4662fe0b62662c9b049e014ffc09861065`,
physical pp. 7--9, 11, 13, 15, Definitions 2.1--2.3 and Lemmas 2.4/3.2--3.5.
For an AH exterior with `3/2<tau<3`, use
`U_b(V,e)=V(div_b e-d tr_b e)+(tr_b e)dV-e(nabla_b V,.)` and its four fluxes
only after weighted DEC/integrability is verified.  A future-timelike flux
can be Lorentz-balanced to `(m_AH,0,0,0)`; the staged helper checks this
finite four-vector operation, not flux convergence or the geometric theorem.
[Pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/The-nonmaximal-anti-de-Sitter-Penrose-Inequality-and-original-data-rigidity-October-5-2026/paper.pdf).
