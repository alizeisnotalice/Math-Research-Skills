# Positive cases with checked scopes

## One marginal: a fixed triangle approximation check

For a fixed nondegenerate convex triangle with constant inward unit normals on its three faces, the Kang–Williams positive-combination geometry can be verified face by face. A side has margin \(1\). At a vertex of interior angle \(\alpha\), equal weights on its two inward normals give margin \(\sin^2(\alpha/2)>0\). Taking the minimum over the finitely many faces and vertices gives a positive margin. Under the remaining paper hypotheses, this supports its individual facewise SRBM approximation route. It is not a two-particle construction (EXSRC-61f38f6c62e9c593).

For normal-cone reflection, Saisho's individual-marginal theorem applies when its exact common-radius Condition (A) and uniform inward-direction Condition (B) hold. Check the chosen normal set at each corner; existence of a normal vector by itself does not verify (A) or (B) (EXSRC-2f6b5402637cac53).

## Coupling with a proved tail upper bound

On a bounded open convex domain \(\Omega\) of diameter \(d\), use Loper's co-adapted normal mirror coupling for standard reflected Brownian motion with generator \(\tfrac12\Delta\). Both coordinates have the correct normal-reflected marginals, the mirror transform is Brownian in the joint filtration, and the paths remain together after the first meeting \(T\). For \(t>0\),
\[
P(T>t)≤F_d(4t,d−|x−y|).
\]
Here F_d(s,k)=P_k(τ_{(-d,d)}>s) is standard one-dimensional Brownian survival in (-d,d) from k.
This yields a TV upper bound. It is diameter-based and does not establish a sharp rate for a selected triangle (EXSRC-e429ef47a4d66ae8).

## Derived method supplement: symmetric interval starts

For \(D=[0,L]\) and starts \((x,L-x)\), \(0\le x<L/2\), reflect \(X\) at 0 and set \(Y=L-X\) until \(X\) reaches \(L/2\). Then use the common driver after meeting. The pre-meeting pair generator is \(\tfrac12d^2/dx^2\) on \([0,L/2]\) with Neumann condition at 0 and Dirichlet condition at \(L/2\). Its modes are \(\cos((2n+1)\pi x/L)\); the leading survival coefficient is \(4\cos(\pi x/L)/\pi>0\), so the actual survival exponent is \(-\pi^2/(2L^2)\). For interior starts, this expansion equals Loper’s reviewed \(F_L(4t,2x)\) diameter comparison term by term. The assumptions and derivation are in the [interval derivation in §4](../references/method.md#4-derived-positive-case-symmetric-starts-on-an-interval); a local SymPy calculation checked the displayed identities but is not the proof. This R08-accepted method supplement is a same-Loper-work replacement with net new source-work increment 0; it does not cover \(x+y\ne L\) or a triangle. It analyzes one selected Markov pair process and does not make A020 Markov or co-adapted.

## Spectral and nodal conclusions

For a bounded connected Lipschitz domain, the first positive Neumann eigenvalue of \(-\Delta\) has variational form \(\mu_1(D)=\inf_{u\in H^1(D),\,\int_Du=0,\,\|u\|_{L^2(D)}>0}\int_D|\nabla u|^2/\int_Du^2\). Esposito–Nitsch–Trombetti gives \(d^2\mu_1(D)\ge\pi^2\) for bounded convex domains at \(p=2\); Laugesen–Siudeja gives \(D^2\mu_1(D)>j_{1,1}^2\) for each nondegenerate planar triangle. Both are one-particle lower bounds for \(-\Delta\); divide the eigenvalue by two for generator \(\tfrac12\Delta\). Neither constructs a coupling or a meeting-tail upper bound (EXSRC-61071ee2e4fdd736; EXSRC-88da49597197e0e5).

Atar–Burdzy's nodal-line result is useful when the exact planar regularity and all mirrored-domain conditions (A1)–(A4) hold. The barrier plus mixed-boundary exit comparison constrains a nodal set; the configured obtuse-triangle example is source-specific. This is not a general acute-triangle coupling or a meeting-tail bound (EXSRC-f641b0ca9637dc96).

## Sensitivity and stability in explicit models

- **Normal half-line sensitivity.** For \(G=[0,\infty)\), \(d=n=1\), \(b=0\), \(\sigma=1\), constant data and a pure feasible initial perturbation \(y\ge0\), the path is
  \[
  Z_t^x=x+W_t+(-x-\min_{s\le t}W_s)^+.
  \]
  The raw directional derivative is \(y\), \(0\), or \(\max(y,0)\) according as \(x+\min_{s\le t}W_s\) is positive, negative, or zero. For \(x>0\), the right-continuous derivative-process regularization is \(y\,1_{\{t<\tau_x\}}\), with \(\tau_x=\inf\{t:x+W_t=0\}\); at \(t=\tau_x\), the raw derivative may equal \(y\) while that regularization is \(0\). At \(x=0\), its projected initial direction is \(L_0[y]=0\), even though the raw derivative at \(t=0\) is \(y\). This is one marginal's sensitivity, not a tail theorem (EXSRC-6170b182ae853a60).
- **Normal orthant sensitivity.** In two dimensions with \(R=I,b=0,\sigma=I\), use coordinatewise Skorokhod formulas and the same Brownian motion for an interior start \(x\) and an admissible nearby start \(x+\varepsilon y\). This checks only the reviewed pure-initial-perturbation synchronous sensitivity case; it does not certify the full printed general derivative claim (EXSRC-dbc465f6b783d606).
- **Smooth-domain stability.** Andres (2011) gives a same-noise path stability estimate under its bounded connected \(C^3\) setup with additive standard Brownian noise and normal reflection. Burdzy (2009) gives a uniform local-time localization bound under its smooth-boundary hypotheses. These are stability/localization interfaces; the general derivative-identification branches are not used ([source index](../references/sources.md)).
- **Critical orthant uniqueness.** Bass–Burdzy's same-driver uniqueness requires completely-S and \(\rho(|I-R|)\le1\), with both solutions adapted to the filtration where their common Brownian driver is Brownian. The accepted deterministic quadrant nonuniqueness example has its own exact oblique parameters and does not define a reflected-Brownian pair (EXSRC-597b2e8559291403, EXSRC-bfe4d4555e712da5).

## Disk benchmarks

For the unit disk, the accepted Burdzy–Chen–Jones use is the qualitative almost-sure distance-contraction theorem plus the derived inequality
\[
\limsup_{t\to\infty}t^{-1}\log |X_t-Y_t|\le -1/R^2
\]
for a disk of radius \(R\), under their synchronous smooth normal-reflection setup. The exact \(\Lambda(D)\) exponent proof is excluded; this gives no finite meeting-time tail (PR-aeba2162c0a9).

The accepted wave08 uses add three bounded benchmarks: Atar (2001) supplies a configured rectangle synchronous-order/spectral example; Atar–Burdzy (2004) supplies a derived co-adapted mirror construction on the smooth unit disk after the R07-reviewed product-domain repair; and the two Cranston–Le Jan (1989) articles give, respectively, a specified synchronous disk coupling with no finite meeting and a simultaneous product-boundary event. None gives a triangle-tail upper bound. The two disk results do not assert overlap of the original individual regulators (EXSRC-cd55a9e0f1e0c2d0, EXSRC-4265613ad6a3f726, EXSRC-62f2ce007b957ddb, EXSRC-ef5251d44e6ca12e).
