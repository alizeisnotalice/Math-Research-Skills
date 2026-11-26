---
name: probability-generating-function-boundaries
description: Audit two-dimensional queue-length PGF equations and complex boundary reductions while preserving event epochs, empty-boundary terms, analytic hypotheses, and probability admissibility.
---

# Probability Generating Functions and Complex Boundary Methods

Use this skill when a stationary law on a two-dimensional integer lattice is represented by a bivariate probability generating function (PGF), and analysis uses a functional equation, kernel, analytic continuation, a Riemann–Hilbert (RH) problem, Wiener–Hopf factorization, or a Fredholm equation. Its main application is auditing method choice and transfer limits for two-queue polling, especially the mixed gated/1-limited interface A006. It does not solve A006 or establish the current literature status of that problem.


## Source-use boundary

Use the documented theorem only within the model and interface in its source-use card. For formally published work, verify the citation and the cited statement against the publication. Verify the active claim and relevant proof steps for a preprint-only result. Historical review notes retain the scope of their original versions. Keep source-card gaps, unavailable evidence, and open transfers as research leads.

The optional attachments named here are available in the original local installation or the central literature archive. See [evidence and local attachments](../math-research/references/evidence.md).

## Start with the object and observation epoch

Before manipulating a transform, record:

1. **State:** queue lengths, server position, phase, and any supplementary state.
2. **Epoch:** the exact event at which the state is observed: arrival to a queue, visit beginning, visit completion, service event, or arbitrary stationary time.
3. **Transform:** a PGF on an integer lattice, an LST of a nonnegative real workload, a stationary-mass expansion, or another transform.
4. **Model:** transitions or generator, arrival/service/switchover assumptions, discipline, route, and parameters.
5. **Stationarity:** whether a joint stationary law is assumed or proved, and which stability conditions support it.
6. **Unknowns:** every interior PGF, phase PGF, axis trace, empty-state mass, and event-frequency weight.
7. **Analytic domain:** where each function and kernel is analytic, including boundary continuity, branch choices, and moment assumptions.

Do not convert between observation epochs without a separately proved arrival-epoch or Palm identity. Do not call a stationary-mass product expansion a PGF: signed geometric weights are not atom probabilities.

## Use the selector

Follow the first route whose input conditions are established. Stop at a failed gate and report the missing hypothesis.

| Observed structure | Route | Required gate |
|---|---|---|
| A discrete embedded chain or CTMC with a countable-state stationary law | Derive the phase- and epoch-specific PGF equation | Enumerate interior, axes, origin, and all phases directly from transitions or the generator. |
| A polynomial kernel and explicit boundary functions | Kernel trace or cancellation | State the common domain, root branch, multiplicity, and boundary numerator that must vanish. |
| A parameterized kernel curve relates boundary traces | Analytic continuation and identity | Prove the curve lies in the common domain and traces continue there; specify connectedness and an adequate uniqueness set. |
| A trace relation on an oriented contour gives a jump | RH or shifted RH | Give contour, orientation, domains, jump/shift, index, endpoint conditions, singularities, and normalization. |
| A one-variable factorization is proposed after reduction | Wiener–Hopf | Locate zeros and poles in each half-domain; prove nonvanishing, index, and factor normalization. |
| An integral equation is proposed | Fredholm route | Name the function space and operator; establish a compactness/index alternative or a contraction on the stated norm. |
| A source expands stationary masses as geometric products | Compensation method | Keep it as a mass-series method; prove feasible cancellation roots, axis residual closure, convergence, and normalization in its own model. |
| A meromorphic transform is reconstructed by residues | Partial fractions / state extraction | Prove continuation, pole list and residues, and decay sufficient to eliminate the entire remainder and justify coefficient extraction. |

### Step 1: derive the equation at the named epoch

For a vector $(N_1,N_2)\in\mathbb Z_+^2$, its PGF is
$$
F(z_1,z_2)=\mathbb E[z_1^{N_1}z_2^{N_2}]
=\sum_{m,n\ge 0}p_{m,n}z_1^m z_2^n,
\qquad p_{m,n}\ge 0,\quad \sum_{m,n}p_{m,n}=F(1,1)=1.
$$
Absolute summability gives analyticity in the open unit bidisc and continuity on its closure. Derivatives at $z_i=1$ need the corresponding finite-moment assumptions.

Build the recurrence from the source transition rule or generator. Keep terms for an empty queue and the origin. For a phase process, preserve a vector of phase-specific PGFs. For polling, label each $F_i$ and $G_i$ by visit-start and visit-end epoch; a service-event sub-PGF is a different object.

For A006, the canonical historical interface in Boon–Boxma–Winands, Eqs. (3)–(4), has a 1-limited update
$$
G_2(z_1,z_2)=\beta_2(z_1,z_2)
\frac{F_2(z_1,z_2)-F_2(z_1,0)}{z_2}+F_2(z_1,0),
$$
with the analytic limit understood at $z_2=0$, and its gated visit retains the term
$$
\sigma_1(z_1,0)F_1(h_1(z_1,0),0).
$$
Dropping either axis term changes the equation. This preserves the source's server-arrival and departure epochs; it does not solve the resulting G/1-L system. See the exact source index（本机附件：`references/source-index.md`） and [the method notes](references/method.md).

### Step 2: distinguish PGF admissibility from LST complete monotonicity

If $F$ is a PGF, then
$$
L(s_1,s_2)=F(e^{-s_1},e^{-s_2})
$$
is the LST of an integer-valued nonnegative vector. For every pair of nonnegative integers $k_1,k_2$,
$$
(-1)^{k_1+k_2}
\frac{\partial^{k_1+k_2} L}
{\partial s_1^{k_1}\partial s_2^{k_2}}(s_1,s_2)\ge 0,
\qquad s_1,s_2>0.
$$
A normalized completely monotone function on the strictly positive quadrant, continuous with value one at the origin, is a Laplace transform of a probability measure on $\mathbb R_+^2$; this does not impose support on $\mathbb Z_+^2$. Derivatives at $s_i=0$ may be infinite when moments diverge. For example, $L(s)=e^{-s/2}$ is completely monotone but its representing mass is at $1/2$; the pullback $z^{1/2}$ is not an ordinary PGF analytic at zero.

To certify a candidate as a PGF, check its Taylor coefficients are nonnegative, its support uses the required integer lattice, and its total mass is one. Analyticity, boundedness on the unit disc, nonnegative values on $[0,1]$, or $F(1)=1$ alone is insufficient. The exact witness
$$
H(z)=\left(\frac{z-\tfrac12}{1-\tfrac z2}\right)^2
$$
is analytic and bounded by one in the unit disc, nonnegative on $[0,1]$, and has $H(1)=1$, yet its coefficient of $z$ is $-3/4$. A separate probability law $p_n=1/[n(n+1)]$, $n\ge 1$, has total mass one but infinite first moment; its PGF is continuous at $z=1$ while the derivative there diverges. Reproducible exact calculations are in math-evidence.md（本机附件：`references/math-evidence.md`）.

### Step 3: use the kernel only with its domain and multiplicities

Write the equation as
$$
K(z_1,z_2)F(z_1,z_2)=A(z_1,z_2),
$$
leaving every boundary function in $A$. List the common domain of $F,K,A$.

- In one variable, if $K$ has a zero of order $m$, removability of $A/K$ requires $A$ to vanish to at least order $m$.
- In several variables, establish local holomorphic divisibility along each relevant component of $\{K=0\}$. Pointwise vanishing at one or many isolated points does not prove divisibility.
- At a repeated root, match the cancellation order; do not use a simple-root derivative formula.
- Divide by a denominator only where it is nonzero. Keep an undivided identity at degenerate points and take a limit only after justifying it.
- A bivariate zero set such as the diagonal can be thin and still have interior accumulation points; the one-variable identity theorem does not imply a multivariate identity from that set alone. Use a parameterized one-variable identity on a connected domain, an open subset, an iterated-variable argument, or a theorem with the exact uniqueness-set hypothesis.

Vieta identities and root selection can identify a candidate branch or boundary cancellation. They do not by themselves show that a zero is a pole, that it is not canceled, that it dominates, or that the resulting transform is probabilistic.

### Step 4: formulate the complex boundary problem

For an RH reduction, record the oriented contour, both analytic regions, boundary traces, jump coefficient or shift, inhomogeneous term, index, singular points, endpoint regularity, and normalization constraints. Preserve source notation such as $G$ versus a pole-cleared $\widehat G$; check the displayed solution by substitution into the actual jump. A formal boundary relation is not a solvability theorem. A nonzero index needs its own compatibility and factorization conditions. If the problem has a shift, keep that shift.

For Wiener–Hopf, specify the scalar or matrix kernel, domains of zeros and poles, nonvanishing condition, index, and normalization of the factors.

For a Fredholm equation, state the function space and operator, then prove the relevant compactness/index alternative or contraction. Existence and uniqueness for the integral equation do not automatically imply the original PGF equation or probability admissibility.

For partial fractions, state the complex growth assumptions used to remove the entire remainder. Decay on a real sequence or a half-line does not imply a uniform bound on large complex contours.

### Step 5: reconstruct, substitute, and test the law

After solving a boundary relation, substitute into the original FE, retaining all axes, origin, phases, and embedded-event transformations. Then verify:

- the analytic domain required of a PGF;
- $F(1,1)=1$;
- coefficientwise nonnegativity and integer support;
- the model's original balance equations;
- finite moments only where derivatives at $1$ are used.

A truncation or numerical solve can diagnose residuals and signs over a checked range; it is not an all-coefficient proof. State its precision and truncation if used.

## Polling epoch and branching gates

Keep visit-start, visit-end, service-start, service-end, and arbitrary-time laws distinct. In Borst (1996), $F_i,G_i$ are mass-one visit PGFs, while pooled event sub-PGFs $L_i,M_i$ retain server position and each have total mass $\lambda_i/\lambda$, where $\lambda=\sum_j\lambda_j$. Conditional type-$i$ event laws require rescaling by $\lambda/\lambda_i$ when $\lambda_i>0$. Retain the division-free service identity
$$
z_iM_i=L_i\beta_i\!\left(\sum_j\lambda_j(1-z_j)\right);
$$
only divide by $z_i$ where $z_i\ne 0$.

Use a branching-cycle composition only after verifying Resing's Property 1: during the same visit, each customer present at arrival is independently replaced by an identically distributed descendant population. At a 1-limited visit with two customers present, one is served and one is retained, so the two replacements are not iid; the property fails. Do not transfer the infinite branching-product formula to mixed gated/1-limited polling without another proof.

## Method-specific positive cases and missing gates

- **Exact polling FE, not a solution:** the A006 source terms above preserve the empty-boundary traces. They define the problem to analyze.
- **RH example under source-specific hypotheses:** Boxma–Groenendijk's alternating one-customer polling report gives an index-zero RH construction for its stated contour case, with separate on-contour and outside-contour cases. This does not solve A006.
- **Coupled-processor PGFs:** accepted examples provide their own generator-derived FE, kernel branches, necessary trace equations, or resultants. Their epochs, transition laws, and contours are model-specific.
- **Compensation comparison:** Adan, AWZ, Adan–Boxma–Resing, and related records use stationary masses or method surveys. They do not become PGF coefficient theorems. Negative compensation weights are not negative PGF atom probabilities.
- **Continuous workload transforms:** the fluid polling LST and coupled-processor workload LST are not discrete queue-length PGFs. Their heavy-traffic or Wiener–Hopf identities do not supply integer support or lattice coefficients.
- **Source-literal holds:** the Dimitriou manuscript versions, Groenendijk's stationary displays, and other reviewed local formula discrepancies remain version-specific holds in their exact cards. Do not silently replace a printed formula with an independently derived one; label any repair as derived and restrict it to its checked model and scope.

The exact accepted use for each of the 30 distinct works—and the two zero-increment support rows—is indexed in source-index.md（本机附件：`references/source-index.md`）. That index preserves original artifact versions, method scope, conditions, transfer limits, frozen reader-evidence paths, and immutable R05 use snapshots.

## G09 coverage and unresolved work

This entry distinguishes six method interfaces:

- **G09.01, PGF FE and kernel:** concrete model-specific examples and audited necessary identities are admitted.
- **G09.02, analytic continuation and identity:** several model-specific continuation/branch arguments are admitted. There is no general continuation rule for an arbitrary candidate or for A006.
- **G09.03, RH boundary problems:** selected source-specific indexed examples are admitted with their exact contours and conditions. There is no transfer theorem or A006 solution.
- **G09.04, Wiener–Hopf:** uncovered as an independently verified PGF solution route. The survey's coupled-processor workload-LST reference is a locator, not a read primary proof.
- **G09.05, Fredholm:** uncovered as a general, independently verified route. Surveys citing a Fredholm argument do not supply that proof or its function-space hypotheses.
- **G09.06, admissibility:** the PGF/LST distinction and exact counterexamples are established. A generic theorem converting a complex analytic solution into a probability law is not.

Other unresolved steps include full bidisc continuation, general nonzero-index RH solvability, external map and Fredholm proofs, partial-fraction/state reconstruction requiring global complex growth, infinite compensation-series convergence outside each source's stated region, and coefficientwise nonnegativity after reconstruction. These are explicit gaps, not assumed defaults.

## Historical review status

The frozen R05 formal cohort selected for this G09 entry has 32 scoped rows: 30 eligible uses across 30 distinct work families and 2 zero-increment support rows. This is the source-level cohort status in source-index.md（本机附件：`references/source-index.md`）, not a cross-lane global transaction. Root's exact-cohort capture and whole-entry R05 review remain separate steps. This draft is not portable, published, or installed.

## Supporting references

- [Method and source notes](references/method.md)
- Exact mathematical evidence（本机附件：`references/math-evidence.md`）
- Frozen 30-source index and 2 support-zero rows（本机附件：`references/source-index.md`）
