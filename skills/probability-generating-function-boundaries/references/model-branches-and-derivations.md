# Model branches and derivations

This is the detailed companion to the PGF-boundaries skill.  It preserves the
source-specific model branches and exclusions; none is a transfer theorem for a
different polling, queueing, or workload model.

## 1. Derive the FE at the named epoch

For \((N_1,N_2)\in\mathbb Z_+^2\),

$$
F(z_1,z_2)=\mathbb E[z_1^{N_1}z_2^{N_2}]
=\sum_{m,n\geq0}p_{m,n}z_1^m z_2^n,
\qquad p_{m,n}\geq0,\quad F(1,1)=1.
$$

Absolute summability gives analyticity in the open unit bidisc and continuity
on its closure. Derivatives at \(z_i=1\) need the corresponding finite-moment
assumptions. Build the recurrence from the actual transition rule or generator;
keep empty-queue and origin terms. For a phase process preserve the vector of
phase PGFs. In polling, label \(F_i,G_i\) by visit-start and visit-end epoch;
a service-event sub-PGF is a different object.

For A006, the historical Boon--Boxma--Winands interface, Eqs. (3)--(4), has
the 1-limited update

$$
G_2(z_1,z_2)=\beta_2(z_1,z_2)
\frac{F_2(z_1,z_2)-F_2(z_1,0)}{z_2}+F_2(z_1,0),
$$

with its analytic limit at \(z_2=0\), while the gated visit retains

$$
\sigma_1(z_1,0)F_1(h_1(z_1,0),0).
$$

Dropping either axis term changes the equation. These preserve the source's
server-arrival/departure epochs and do not solve the resulting G/1-L system.
See the exact source index in `source-index.md` and [method notes](method.md).

## 2. PGF admissibility is stronger than LST complete monotonicity

If \(F\) is a PGF, then \(L(s_1,s_2)=F(e^{-s_1},e^{-s_2})\) is the LST of an
integer-valued nonnegative vector, so for nonnegative integers \(k_1,k_2\),

$$
(-1)^{k_1+k_2}\partial_{s_1}^{k_1}\partial_{s_2}^{k_2}L(s_1,s_2)\geq0.
$$

A normalized completely monotone function on the positive quadrant represents
a probability law on \(\mathbb R_+^2\), not necessarily the lattice.  For
example \(e^{-s/2}\) is completely monotone but pulls back to \(z^{1/2}\),
not an ordinary PGF. Infinite moments remain possible at the origin.

For a PGF check coefficient nonnegativity, lattice support, and total mass.
Analyticity/boundedness in the unit disc, nonnegative real values on
\([0,1]\), or \(F(1)=1\) do not suffice. The exact witness

$$
H(z)=\left(\frac{z-\tfrac12}{1-\tfrac z2}\right)^2
$$

is analytic and bounded by one in the disc, nonnegative on \([0,1]\), and
equals one at \(1\), but has \(z\)-coefficient \(-3/4\). The law
\(p_n=1/[n(n+1)]\), \(n\ge1\), has total mass one but infinite first
moment. Exact reproducible calculations are in `math-evidence.md`.

## 3. Kernel cancellation and continuation

Write \(K(z_1,z_2)F(z_1,z_2)=A(z_1,z_2)\), retaining every boundary function
in \(A\), and list a common analytic domain for \(F,K,A\).

- A one-variable zero of order \(m\) requires \(A\) to vanish to order at
  least \(m\). In several variables establish local holomorphic divisibility
  along each relevant component of \(\{K=0\}\), not just pointwise vanishing.
- Match repeated-root cancellation orders. Divide only where the denominator is
  nonzero; retain an undivided identity at degenerate points and justify any
  limit.
- A thin bivariate zero set can still have interior accumulation. A
  one-variable identity theorem does not prove a multivariate identity from it;
  use a connected parameterized identity, an open set, an iterated-variable
  argument, or the exact applicable uniqueness theorem.
- Vieta/root selection can produce a candidate branch or cancellation but does
  not prove a pole, absence of cancellation, dominance, or probability
  admissibility.

For a kernel-curve route, first prove the curve is in the common domain and the
boundary traces continue there, then identify the connected uniqueness set.

## 4. Complex boundary branches

For an RH reduction record the oriented contour, both analytic regions,
boundary traces, jump coefficient or shift, inhomogeneous term, index,
singular points, endpoint regularity, and normalization. Preserve source
notation such as \(G\) versus pole-cleared \(\widehat G\), and check a
displayed solution by substitution into the actual jump. A nonzero index needs
its own compatibility/factorization conditions; retain an actual shift.

For Wiener--Hopf, name the scalar or matrix kernel, zero/pole domains,
nonvanishing condition, index, and factor normalization. For Fredholm, name
the function space and operator and prove the compactness/index alternative or
contraction in the stated norm. Existence/uniqueness of an auxiliary integral
equation does not automatically imply the original PGF FE or a probability law.

For partial fractions/state extraction, prove continuation, the complete pole
and residue list, and enough global complex growth to eliminate an entire
remainder. Real-axis or sequence decay is not a large-contour bound.

## 5. Reconstruction and probability checks

Substitute any boundary solution back into the original FE, retaining axes,
origin, phases, and embedded-event transformations. Verify the required PGF
domain, \(F(1,1)=1\), coefficientwise nonnegativity, integer support, and the
original balance equations. Invoke finite moments only when derivatives at one
are used. A numerical truncation can diagnose residuals/signs over its checked
range but is not an all-coefficient proof; record precision and truncation.

## Polling epoch and branching gates

Keep visit-start, visit-end, service-start, service-end, and arbitrary-time
laws distinct. In Borst (1996), \(F_i,G_i\) are mass-one visit PGFs, while
pooled event sub-PGFs \(L_i,M_i\) retain server position and each have total
mass \(\lambda_i/\lambda\), with \(\lambda=\sum_j\lambda_j\). A conditional
type-\(i\) event law needs rescaling by \(\lambda/\lambda_i\) if
\(\lambda_i>0\). Keep the division-free identity

$$
z_iM_i=L_i\beta_i\!\left(\sum_j\lambda_j(1-z_j)\right)
$$

and divide by \(z_i\) only where nonzero.

Use a branching-cycle composition only after verifying Resing's Property 1:
each customer present at arrival is independently replaced during that visit by
an identically distributed descendant population. A 1-limited visit with two
customers serves one and retains one, so the replacements are not iid; do not
transfer the infinite branching-product formula to mixed gated/1-limited
polling without another proof.

## Positive cases and explicit exclusions

- **Exact A006 FE, not a solution.** The two A006 source terms above preserve
  the empty-boundary traces and define the problem to analyse.
- **RH only under source hypotheses.** Boxma--Groenendijk gives an index-zero
  RH construction for its stated alternating one-customer contour cases; it
  does not solve A006.
- **Coupled-processor PGFs.** Accepted examples supply their own
  generator-derived FE, branches, trace equations, or resultants. Epochs,
  transition laws, and contours are model-specific.
- **Compensation.** Adan, AWZ, Adan--Boxma--Resing and related records may use
  stationary masses or surveys; they do not become PGF coefficient theorems.
  Negative compensation weights are not negative PGF atom probabilities.
- **Continuous workloads.** Fluid-polling and coupled-processor workload LSTs
  are not lattice queue-length PGFs. Heavy-traffic/Wiener--Hopf identities do
  not supply integer support or lattice coefficients.
- **Source-literal holds.** Dimitriou manuscript versions, Groenendijk
  stationary displays, and other reviewed formula discrepancies remain holds
  in their exact cards. Never silently repair a printed formula; label a repair
  as derived and restrict it to its checked model.

The frozen source record contains 30 eligible work families and two
zero-increment support rows. It is intentionally a source map, not a proof of
the unresolved steps: full bidisc continuation, general nonzero-index RH,
external map/Fredholm proofs, global-growth residue reconstruction,
compensation convergence outside source regions, and coefficientwise positivity
after reconstruction.

## Links retained from the compact entry

- [Method and source notes](method.md)
- `math-evidence.md`
- `source-index.md`
- [OpenAI rooted planar-map corner substitution](wave4-pa2-rooted-corner-substitution.md)
