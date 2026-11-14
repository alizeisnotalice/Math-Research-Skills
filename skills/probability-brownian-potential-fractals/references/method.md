# Brownian geometry, potential theory, and reflection coupling

This reference condenses the checked proof interfaces in the current W08 batch. Independent review is pending; unacquired sources remain explicitly identified in `evidence/W08/sources.json`.

## 1. Name the set and the quantifier

Before using a dimension theorem, write the set in the statement and the optimizing operator, if any.

| Object | Meaning | Checked result / warning |
|---|---|---|
| Brownian trace/range | \(B[0,1]\) or \(B[0,\infty)\) | Planar trace has Hausdorff dimension 2 (M0224, Thm. 4.29). |
| Frontier | Boundary of the unbounded complementary component / filled hull | Planar Brownian frontier has dimension 4/3 (M0175, with the detailed exponent route in M0205 and its cited analyticity paper M0206); this is not an arc theorem. |
| Chordal SLE\(_6\) trace | Loewner trace in \(\mathbb H\) from 0 to \(\infty\) | Beffara's formula gives dimension 7/4; do not confuse it with the 4/3 Brownian frontier (M0179, M0175). |
| Labyrinth dimension | Supremum of dimensions of Jordan arcs in a set | Planar Brownian trace has supremum 2 (W08-R001, Thm. 1). |
| B061 path infimum | Infimum of \(\dim_H J\) over all Jordan arcs \(J\subset B[0,1]\) with at least two points | The above frontier and supremum theorems do not determine this infimum. |
| Independent path intersection | Intersection of \(p\) independent Brownian ranges | M0224, Thm. 9.8 gives \(d-p(d-2)\) under \(d\ge2,p\ge2,p(d-2)<d\). |
| Loop-erasure | A simple curve extracted from a Brownian path by continuous loop-erasure | Zhan’s radial SLE2 result gives an admissible arc, but transferring its dimension requires the radial/chordal local-law bridge. |

For B061, a Jordan arc itself has dimension at least 1. Burdzy's percolation-dimension paper (M0171) concerns an infimum over connected sets in its own definition; it does not let us replace the B061 family of Jordan arcs by arbitrary connected subsets. Zhan constructs a simple loop-erasure contained in planar Brownian trace; Beffara gives the exact chordal SLE2 trace dimension 5/4. The available chain gives a candidate upper bound once the radial/chordal transfer and the stopping interval inclusion are justified. It does not prove the value 1. Burdzy's labyrinth theorem gives the opposite optimization (supremum) and equals 2. Keep these conclusions in separate rows of any argument. As another set distinction, chordal SLE6 trace dimension is exactly 7/4 by Beffara; Rohde–Schramm (W08-R006) only gives the trace upper bound 7/4 and separately the SLE6 hull-boundary upper bound 4/3. M0175's Brownian-frontier equality 4/3 is a third, different set.

M0205 (arXiv:math/0003156v3, PDF pp. 3–5) writes its exponent as \(\zeta(2,\lambda)\), whereas the companion M0206 (arXiv:math/0005295v1, PDF pp. 1–3) writes \(\xi(2,\lambda)\) for twice that time-decay exponent: under the common conditional-probability definition, \(\xi(2,\lambda)=2\zeta(2,\lambda)\). M0206 Theorem 1.1 proves \(\lambda\mapsto\xi(k,\lambda)\) real analytic on \((0,\infty)\) for each integer \(k\ge1\); its Corollary 1.2 extends the formula from \(\lambda\ge1\) to positive \(\lambda\), with continuity at zero supplied by its cited earlier result. For \(k=2\), this gives \(\eta_2=\lim_{\lambda\downarrow0}\xi(2,\lambda)=2/3\), and M0206 Corollary 1.3 combines this with the cited frontier-dimension identity to obtain 4/3. The analytic transfer closes M0205's stated gap, but the frontier remains a different set from B061's Jordan-arc infimum.

## 2. Brownian loop-erasure and SLE

### Zhan’s theorem (W08-R007)

For complex Brownian motion in a **strict** simply connected subdomain \(D\subsetneq\mathbb C\) containing 0, stopped at its first exit \(\tau_D\), the continuous loop-erasure exists almost surely. Theorem 2.1 identifies its time-reversal with radial SLE\(_2\) growing from a random prime end toward 0; the starting prime end has harmonic measure from 0. It gives existence, not uniqueness or a deterministic erasure algorithm. A disk exhaustion with radii tending to zero makes the stopped loop-erasure occur before deterministic time 1 eventually, because \(|B(1)|>0\) almost surely.

### Discrete LERW scaling references

Lawler–Schramm–Werner (W08-R013, Theorem 1.1) prove the planar discrete LERW scaling limit to radial SLE2 in simply connected domains, and Zhan (W08-R014) proves corresponding discrete-to-continuous LERW convergence in finitely connected domains with separate interior-endpoint, prime-end-endpoint and side-arc target assumptions. These results support the conformal toolkit. They are not the continuous loop-erasure theorem for Brownian motion; use W08-R007 for that construction and retain its own hypotheses.

### Dimension bridge

Beffara’s theorem (M0179) states for **chordal** SLE\(_\kappa\), \(\dim_H\gamma=\min(2,1+\kappa/8)\) a.s.; hence chordal SLE2 dimension is 5/4. Rohde–Schramm (W08-R006, PDF p. 7) says appropriately stated chordal results carry over to radial SLE via LSW01b Proposition 4.2. Mörters–Peres Appendix 11 (M0224, printed p. 338) states the beginnings of radial and conformally mapped chordal curves at the same \(\kappa\) are absolutely continuous up to a local stopping segment. Before using this to bound a *whole* loop-erased arc, state the exact stopping segment, conformal map and direction of absolute continuity, then justify passage from local segments to the complete trace. Do not claim equality in law of complete chordal and radial traces.

## 3. Hausdorff dimension and capacity

### General lower-bound routes

- A finite nonzero measure with \(\mu(V)\le C\operatorname{diam}(V)^\alpha\) on all sufficiently small closed \(V\) gives \(\dim_H E\ge\alpha\) (M0224, Thm. 4.19).
- Alternatively, finite Riesz energy \(I_\alpha(\mu)=\iint |x-y|^{-\alpha}d\mu(x)d\mu(y)\) gives \(\mathcal H^\alpha(E)=\infty\), hence \(\dim_H E\ge\alpha\) (M0224, Thm. 4.27). For Gaussian increments in \(\mathbb R^d\), check both time-integrability and the negative Gaussian moment condition \(\alpha<d\).
- For closed Euclidean sets, \(\dim_H A=\sup\{\alpha:\operatorname{Cap}_\alpha(A)>0\}\) (M0224, Thm. 4.32). Record closedness and the exact kernel.

### Hitting probability and potential kernels

For closed target \(A\) and transient Brownian motion as defined in M0224 (unkilled in \(d\ge3\), or killed at an independent exponential time or exit from a bounded domain in the stated cases), use the Martin kernel at the reference point 0,
\[
M(x,y)=G(x,y)/G(0,y).
\]
Theorem 8.24 gives exactly \(\tfrac12\operatorname{Cap}_M(A)\le \mathbb P_0(\tau_A<T)\le\operatorname{Cap}_M(A)\). The upper bound is the first-hit distribution’s finite Martin energy; the lower bound is a second-moment/Paley–Zygmund estimate. The radial potential is \(f(r)=\log(1/r)\) in the planar case and \(r^{2-d}\) for \(d\ge3\); it characterizes polarity but, because it is translation-invariant, it is not in general a uniform estimate of hitting probability from a fixed point for translated sets.

The equilibrium measure represents last exits, not first exits: for compact \(\Lambda\), \(\mathbb P_x(B(\gamma)\in A,0<\gamma<T)=\int_A G(x,y)d\nu(y)\) (M0224, Thm. 8.8). The last exit time is not generally a stopping time.

For \(d\ge3\), Wiener’s criterion (M0224, Thm. 8.37) is
\[
 x\text{ regular for closed }\Lambda\iff
 \sum_{k\ge1}2^{k(d-2)}\operatorname{Cap}_{d-2}\bigl(\Lambda\cap\{2^{-k-1}\le |y-x|<2^{-k}\}\bigr)=\infty.
\]
Use the annular shell and scale exactly; replacing the sum by a single capacity at one radius loses the criterion.

## 4. Reflection and synchronous couplings

### General reflection-coupling auxiliary result

Eberle (W08-R009, Theorem 1) treats Euclidean diffusions with constant invertible diffusion matrix, locally Lipschitz non-explosive drift, and a continuous radial curvature function κ satisfying lim inf at infinity positive and ∫₀¹rκ(r)⁻dr finite. In its base reflection coupling, the noise is reflected along \(e_t=\sigma^{-1}(X_t-Y_t)/|\sigma^{-1}(X_t-Y_t)|\) in driving-Brownian space, using \(I-2e_te_t^\top\); for general \(\sigma\), this is not reflection directly in the state-space direction \(X_t-Y_t\). The orthogonal stochastic integrand preserves the Brownian marginal. The smooth bounded convex-domain extension in Remark 3 explicitly uses \(G=I_d\) and restricts the curvature infimum to \(x,y\in D\). Its threshold is \(R_0=\inf\{R\ge0:\kappa(r)\ge0\text{ for every }r\ge R\}\), and \(R_1=\inf\{R\ge R_0:\kappa(r)R(R-R_0)\ge8\text{ for every }r\ge R\}\); here \(R\) is the candidate threshold and \(r\) ranges over all larger radii. If the defining set for either infimum is empty, the respective constant is set to \(\operatorname{diam}(D)\). This is a method reference, not a theorem for nonsmooth acute triangles or the spectral tail exponent in A020.

### Reflecting coupling / A020

Separate a specific coupling scheme from the universal question over all couplings. Burdzy–Kendall’s efficient-coupling theorem (W08-R004, Thm. 3.7) concerns **mirror/reflection coupling** in a triangle. For a generic acute triangle, distinct acute angles imply that mirror coupling is not efficient; equilateral and isosceles cases are unresolved there. This does not rule out arbitrary Markovian couplings, and a fortiori does not rule out arbitrary non-Markovian couplings. The paper explicitly raises that broader question.

The exact A020 prompt asks for two reflected Brownian motions in an acute triangle, with their correct Neumann-reflected marginals, and a coupling meeting the stated asymptotic tail rate involving the second Neumann eigenvalue \(\mu_2\). Check whether the proposed construction is mirror-coupled before applying W08-R004. Do not infer impossibility for all couplings from mirror-coupling inefficiency. Preserve the problem’s eigenvalue convention exactly: the source/statement uses \(\mu_2\), while Brownian-generator rates depend on whether the operator is \(\Delta\) or \(\tfrac12\Delta\); W08-R004’s printed 1D examples conflict with the usual squared-frequency eigenvalue normalization (see `evidence/W08/calculations/A020_generator_scale.md`). This convention issue does not resolve A020.

### Synchronous coupling / B062

Synchronous coupling uses the same driving Brownian noise for the two reflected processes; it is not mirror coupling. The B062 statement concerns a bounded smooth connected planar domain with holes and inward normal reflection. Keep those hypotheses attached: compare a bounded multiply-connected domain to the separate unbounded exterior-of-disks construction only after checking the problem’s exact domain class. A numerical simulation or pixelated path cannot certify positive-probability nonconvergence of the continuous reflected processes.

For every coupling, verify the two marginal laws, filtration/adaptedness requirements, reflection local-time directions, and stopping-time/event definitions before using a contraction or spectral estimate. In a reflected SDE, the inward normal reflection term is \(\int n(X_s)dL_s\) with a consistent normal convention; swapping inward/outward normals changes the process.

## 5. Brownian packet exponents: retain the normalization and path segment

- M0205 writes the full-plane time exponent as \(\zeta(2,\lambda)\); M0206 defines \(\xi(2,\lambda)\) with an extra factor 2 in \(-2\log\mathbb E[\Xi_t^\lambda]/\log t\). Thus \(\xi=2\zeta\), not identical numerical normalizations. M0206 Theorem 1.1 proves analyticity for each integer \(k\ge1\) on \((0,\infty)\), and its corollaries use continuity at \(0\) from the cited prior result; this closes the analytic-continuation step for the frontier formula but says nothing about B061's Jordan-arc infimum.
- In M0207's sharp nonintersection estimates, \(Y_r^j\) is the segment \(Y^j[T_0^j,T_r^j]\), from the first hit of the unit circle through the first hit of radius \(e^r\) (PDF pp. 2–3). Equivalently, the estimates use independent Brownian motions started uniformly on the unit circle and stopped on \(C_r\). Do not replace these by full paths \(Y^j[0,T_r^j]\) started at 0; those all share 0 and the cross-packet avoidance event would be impossible.
- For M0208, the threshold \(\widetilde\xi(1,1)=10/3\) is the half-plane/two-sided exponent. The full-plane value is \(\xi(1,1)=5/4\). Keep the tilde on the domain-specific threshold in the \(\eta\)-formula; neither number is a Jordan-arc dimension.

## 6. Frontier, conformal restriction, and shy-coupling boundaries

### Frontier is not a path infimum

Bishop–Jones–Pemantle–Peres (W08-R005, Theorems 1.1–1.2) prove a strict lower bound above one for the planar Brownian **frontier** using Gosper tiles, Whitney trees, a Jones beta-square estimate and a conditional surround-or-miss criterion. This supports only the frontier claim. It does not identify the Brownian range’s contained Jordan arcs, so it cannot bound B061’s infimum. Their final flatness assertion is stated with its proof omitted.

Keep three optimization/object distinctions explicit: M0171 uses an infimum over connected subsets in its percolation-dimension definition; B061 uses an infimum over Jordan arcs in the Brownian trace; W08-R001 uses a supremum over Jordan arcs (labyrinth dimension). No equivalence between those admissible families has been established here.

### Conformal restriction and SLE hulls

Lawler–Schramm–Werner (M0177) characterize chordal restriction samples by
\[
\mathbb P[K\cap A=\varnothing]=\Phi_A'(0)^\alpha
\]
for the specified simply connected test domains and normalized conformal map. Brownian excursion gives exponent 1; chordal SLE$_{8/3}$ gives exponent 5/8. Theorem 7.3 (M0177, PDF pp. 29–30) gives a finite-parameter construction for \(0<\kappa\le8/3\), with exponent \(\alpha_\kappa=(6-\kappa)/(2\kappa)\), by adding an independent Poisson cloud of Brownian bubbles of intensity \(\lambda_\kappa\mu\times dt\) to an independent chordal SLE\(_\kappa\), where \(\lambda_\kappa=(8-3\kappa)(6-\kappa)/(2\kappa)\). Although the printed theorem interval includes \(\kappa=0\), the displayed formulas divide by \(\kappa\); do not substitute zero or claim a finite \(\alpha_0\) (at most describe that endpoint formally as a limit). At \(\kappa=8/3\), the bubble intensity is zero and \(\alpha=5/8\). To obtain finite \(\alpha>5/8\), choose \(\kappa=6/(2\alpha+1)\); do not describe this as bubbles added to a fixed SLE\(_{8/3}\). For SLE$_6$, the paper compares **stopped filled hulls** with Brownian hulls at stated exit/hitting events. Do not upgrade these to equality of full traces.

For SLE$_6$, the trace dimension is 7/4 (M0179). The Brownian frontier is 4/3 (M0175); 4/3 also appears for hull boundaries in the restriction/bubble setting. These are different sets from the trace, and none evaluates the Brownian-trace Jordan-arc infimum.

### Shy couplings: retain geometry and coupling class

- Benjamini–Burdzy–Chen (W08-R008, §2 and Theorem 4.3) use a specific default Markov-coupling class: (i) \(X,Y,(X,Y)\) are Markov and the coordinates have the same transition probabilities; (ii) for every state \((x,y)\) and time \(s\), the conditional future law of \(X\) given \((X_s,Y_s)=(x,y)\) equals its law given \(X_s=x\). Theorem 4.3 rules out shy couplings within this class in bounded convex planar domains with \(C^1\) boundary and no line segments. It is not stated for arbitrary couplings, nor as a strengthening over all co-adapted couplings; keep the exact coupling definition and boundary hypotheses attached. Their Theorem 3.1 constructs a shy coupling on metric graphs with every vertex degree at least three and a positive lower bound on edge lengths. The graph theorem is not a reflected planar theorem.
- Kendall (W08-R010, Theorems 7–8) proves no co-adapted shy reflected-Brownian coupling for bounded convex domains whose boundary has no line segments in all dimensions, and for every bounded convex planar domain including flat segments. Both theorems are for **co-adapted** couplings; do not infer nonexistence for arbitrary couplings.
- Bramson–Burdzy–Kendall (W08-R015, Theorems 1–2) prove the CAT(0) result under uniform exterior-sphere and interior-cone conditions and the simply connected bounded planar consequence. Again the result is for co-adapted couplings; do not apply the planar theorem to domains with holes. Its mechanism is deterministic pursuit plus a Girsanov/vanishing-noise limit, not a sharp exponential rate.

These papers concern shy-ness or eventual epsilon-approach. They do not give A020’s requested sharp tail rate for an acute triangle. Keep graph, mirror, synchronous and arbitrary couplings separate, and check each theorem’s filtration class before using it.

## 7. Proof review checklist

1. Write the random set, time interval, ambient metric, and optimization quantifier.
2. Identify whether the result is almost sure, positive probability, expected dimension/covering count, or only an exponent bound.
3. For SLE, name radial/chordal, target, trace versus hull/frontier, parametrization, and local versus full curve.
4. For energy/capacity, give the kernel and exponent, measure support, integrability range, and whether the target is closed/compact.
5. For coupling, specify which coordinates share noise, what reflection rule is used, and whether the theorem covers that rule or all couplings.
6. Separate numerical generator/eigenvalue checks from a proof of the tail inequality.
7. Mark a proof gap explicitly whenever two source theorems require an unproved transfer step.
