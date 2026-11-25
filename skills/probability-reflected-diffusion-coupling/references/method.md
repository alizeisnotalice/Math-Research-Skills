# Proof interfaces for reflected-diffusion coupling

This reference states proof obligations and the bounded interfaces reviewed for L08. Source theorems may be broader; use a claim only with the hypotheses and scope summarized in the local source index.

## 1. Specify and solve one marginal

Record the state domain, covariance and drift, reflection field, regulator support, and corner rule. A facewise SRBM and a normal-cone reflected Brownian motion are different models unless the reflection data and Skorokhod map identify them.

- **Normal-cone reflection.** Saisho's conditions (A) and (B), including \(N_x=N_{x,r_0}\ne\varnothing\) for a common \(r_0>0\) and \(\langle l_x,n\rangle\ge1/\beta\), support a unique deterministic normal-reflection SP; bounded Lipschitz coefficients give the associated strong reflected SDE. Verify the actual normal sets at every corner. This is a one-marginal result, not a coupling theorem (EXSRC-2f6b5402637cac53).
- **GPS/ESP models.** Ramanan's GPS theorem uses its specified orthant and \(J+1\) reflection directions. An ESP need not be a finite-variation SP. The accepted continuous-input example distinguishes the conclusion on \([0,\tau_0)\) from an endpoint conclusion, which needs separate hypotheses (EXSRC-289aaf4d39cff403).
- **Polyhedral approximation.** Kang–Williams require their exact facewise reflection assumptions, local perturbation and support conditions, tightness hypotheses, and Brownian-driver plus martingale conditions in the generated limit filtration before a limit is identified as an SRBM. A fixed-triangle margin check supports that individual-marginal route only; it supplies no pair coupling or spectrum (EXSRC-61f38f6c62e9c593).
- **Sensitivity.** Keep the admitted examples narrow: Lipshutz–Ramanan (2018) is used for nearby-start synchronous sensitivity only in the two-dimensional normal orthant with \(R=I,b=0,\sigma=I\); Lipshutz–Ramanan (2019) is used for the normal half-line with \(b=0,\sigma=1\), constant data, and a pure feasible initial perturbation. On the half-line, distinguish the raw pointwise derivative from its right-continuous derivative-process regularization at first contact. Neither use licenses a general oblique corner derivative or meeting-tail claim (EXSRC-dbc465f6b783d606; EXSRC-6170b182ae853a60).
- **Smooth-domain controls.** Andres (2011) is used for its same-noise stability estimate, not the general derivative-identification chain. Burdzy (2009) is used for its uniform local-time localization lemma, not its signed shape-operator derivative theorem. Lundström–Önskog's moving-domain regularity claim remains on hold because its uniform full spatial Sobolev-norm wording has not been resolved ([source index](sources.md)).

## 2. Define the coupling class and verify both marginals

For a co-adapted coupling, write the joint filtration and show that each driver is Brownian in it. Predictable orthogonal transforms of Brownian motion preserve Brownian law by their bracket and Lévy's characterization. For an unrestricted coupling, establish each coordinate's correct path law without adding a common-filtration constraint.

Specify the joint construction through the first meeting time \(T\), then state the post-meeting rule. If the proof uses an auxiliary folded or reflected-domain coordinate, verify its transformed driver and boundary law separately.

- Loper's reviewed construction gives a co-adapted normal mirror coupling with both normal-reflected Brownian marginals on a bounded convex set, and continues together after meeting. Define F_d(s,k)=P_k(τ_{(-d,d)}>s) for standard one-dimensional Brownian motion. For t>0 it proves P(T>t)≤F_d(4t,d−|x−y|). Equivalently, a comparison written on [0,d], reflected at d and killed at 0, with start r uses argument k=d−r. The radial comparison is pre-meeting; this is not a triangle-sharp rate. The accepted use excludes the separate pipe lower/sharpness, Lemma 2(3) plus-sign, and MGF/end-point branches (EXSRC-e429ef47a4d66ae8).
- Atar–Burdzy (2002) convert a separating line barrier into a nodal-domain conclusion through mixed Dirichlet–Neumann exit survival. Their mirror-domain pair requires all stated (A1)–(A4) conditions; the configured obtuse-triangle example is not an arbitrary-triangle meeting-tail theorem (EXSRC-f641b0ca9637dc96).
- The accepted Atar–Burdzy (2004) use is a derived co-adapted mirror construction on the smooth unit disk using product-domain reflected-SDE cutoffs. Its proof checks both marginal laws and post-meeting continuation without the printed Lemma 1 estimate. It does not certify their general lip-domain spectral argument (EXSRC-4265613ad6a3f726; its disk repair was independently reviewed by R07).
- Cranston–Le Jan's two 1989 disk papers concern one specified synchronous normal-reflection construction. One proves noncoalescence despite exponential distance contraction; the other proves a simultaneous pair-boundary event using an auxiliary crease local time. The latter does not claim that the two original regulator measures overlap. These are accepted, source-specific wave08 uses. Disk noncoalescence does not rule out another coupling class; simultaneous product-boundary visits do not imply overlapping individual regulator measures or a tail estimate.

## 3. Separate tail bounds, TV bounds, and spectral constraints

Let \(T\) be the first meeting time and require the coupling to stay together after \(T\).

- **Tail upper bound to TV.** For a coalescing coupling, \(\|\mathcal L(X_t)-\mathcal L(Y_t)\|_{\rm TV}\le P(T>t)\). A source's survival estimate therefore yields a TV upper bound once its marginal and continuation hypotheses are checked.
- **Spectral obstruction to a tail lower bound.** If \(-\Delta f=\mu f\) with Neumann data and the Brownian generator is \(\Delta/2\), then \(P_tf=e^{-\mu t/2}f\). For any correct coalescing coupling and bounded \(f\),
  \[
  P(T>t)\ge \frac{e^{-\mu t/2}|f(x)-f(y)|}{2\lVert f\rVert_\infty}.
  \]
  This is a necessary lower bound. It does not supply a coupling with a matching upper bound. Check generator normalization and the source's eigenvalue indexing before comparing rates.
- **A killed-pair spectrum is a different object.** For the derived interval example in §4, the symmetric start constraint \(x+y=L\) reduces the pre-meeting pair to a one-dimensional process killed at its meeting point. Its mixed Neumann–Dirichlet spectrum gives the actual survival exponent for that configured pair. Do not replace this pair calculation with a single-particle Neumann eigenvalue.
- **G16.06: selected Markov joint process only.** A joint generator calculation requires a selected Markov coupling; it is not a restriction on an unrestricted coupling target. For standard Brownian marginal covariance I and instantaneous cross-covariance C(x,y), the formal covariance block is \(\begin{pmatrix}I&C\\C^T&I\end{pmatrix}\), which must be positive semidefinite (equivalently \(\|C\|_{op}\le1\)); the interior candidate generator is \(\tfrac12(\Delta_x+\Delta_y)+\sum_{ij}C_{ij}\partial_{x_i}\partial_{y_j}\). Then verify the actual product-domain reflection and corner rules, the killing set (often the diagonal), the resulting boundary conditions, and the spectral theorem for that possibly degenerate process. A single-particle Neumann gap or an L² decay statement alone does not prove a survival-tail upper bound; show the killed-pair expansion and a nonzero leading survival coefficient or another valid tail argument.
- **Nodal barriers are not meeting tails.** Atar–Burdzy (2002) use exit survival and mixed-boundary eigenvalues to constrain eigenfunction nodal sets; this is a spectral/geometric interface, not an upper estimate for \(P(T>t)\).

## 3A. One-particle Neumann Poincaré interface (G16.04)

For a bounded connected Lipschitz domain \(D\), define the first positive Neumann eigenvalue of \(-\Delta\) by
\[
\mu_1(D)=\inf\left\{\frac{\int_D|\nabla u|^2}{\int_Du^2}:u\in H^1(D),\ \int_Du=0,\ \int_Du^2>0\right\}.
\]
The reviewed \(p=2\) convex-domain result gives \(d^2\mu_1(D)\ge\pi^2\); the strict triangle result gives \(D^2\mu_1(D)>j_{1,1}^2\) for each nondegenerate planar triangle. Here \(d\) or \(D\) is the domain diameter, and both eigenvalues are for \(-\Delta\); divide by 2 to compare with the standard reflected-Brownian generator \(\tfrac12\Delta\). These one-particle lower bounds do not construct a pair coupling or a meeting-tail upper bound (EXSRC-61071ee2e4fdd736; EXSRC-88da49597197e0e5).

## 4. Derived positive case: symmetric starts on an interval

Let \(D=[0,L]\), \(0\le x<L/2\), and start at \((X_0,Y_0)=(x,L-x)\). Before meeting use \(X_t=x+B_t+L_t\), where \(L\) is the regulator at 0, and \(Y_t=L-X_t\); thus \(Y\) is reflected at \(L\) with driver \(-B\). If \(T\) is the first time \(X\) reaches \(L/2\), its stitched driver is \(Z_t=B_t-2B_{t\wedge T}\), Brownian by the predictable sign-change representation. Stop the mirror phase at \(T\), then continue both coordinates together using the increments of \(B\). Both drivers are Brownian in the common filtration and both marginals are normal-reflected Brownian motion.

The pre-meeting pair stays on the anti-diagonal. Its killed generator reduces to \(\tfrac12 d^2/dx^2\) on \([0,L/2]\), with \(f'(0)=0\) and \(f(L/2)=0\). The modes and rates are
\[
\phi_n(x)=\cos((2n+1)\pi x/L),\qquad \lambda_n=(2n+1)^2\pi^2/(2L^2).
\]
The survival expansion has coefficients \(4(-1)^n/(\pi(2n+1))\). Since its leading coefficient is positive for every fixed \(0\le x<L/2\), the large-time exponent is \(-\pi^2/(2L^2)\). For \(0<x<L/2\), set \(d=L\) and \(r=|x-(L-x)|=L-2x\) in the already reviewed Loper expression \(F_d(4t,d-r)\). Its killed-interval spectral series becomes exactly this mixed-boundary survival series, so the selected interval coupling attains Loper’s diameter comparison bound for these symmetric starts. The derived interval series also covers \(x=0\), while Loper’s accepted bound is used here only for interior starting points. The coupling, killed-pair boundary argument and conditions are proved in §4. A local SymPy calculation checked the displayed generator, boundary conditions, eigenvalues and coefficients; the mathematical proof is stated here. This is a derived method supplement accepted by R08 as a same-Loper-work G16.06 method replacement, with net new source-work increment 0. Its exact pair-domain and mixed-boundary calculation applies only to this symmetric-start interval construction. It does not cover starts \(x+y\ne L\), general intervals with another coupling rule, or triangles.

## 5. Keep reviewed limits visible

Do not turn a one-particle theorem into a pair construction, an asymptotic distance estimate into finite coalescence, or a Neumann lower bound into a coupling-tail upper bound. For a polygon corner, verify the actual normal cone or facewise Skorokhod rule; smooth-boundary local-time formulas do not settle it. In the unit disk, the accepted Cranston–Le Jan synchronous example has exponential distance contraction but T=∞ almost surely, so distance decay alone is not a meeting-tail estimate. The exact reviewed positive and negative examples are in [examples/positive.md](../examples/positive.md) and [examples/negative.md](../examples/negative.md).
