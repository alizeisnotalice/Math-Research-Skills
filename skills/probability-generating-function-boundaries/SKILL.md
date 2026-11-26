---
name: probability-generating-function-boundaries
description: Audit two-dimensional queue-length PGF equations and complex boundary reductions while preserving event epochs, empty-boundary terms, analytic hypotheses, and probability admissibility.
---

# Probability Generating Functions and Complex Boundary Methods

Use this skill for a stationary law on a two-dimensional integer lattice whose
bivariate PGF is analysed through a functional equation (FE), kernel, analytic
continuation, Riemann--Hilbert (RH), Wiener--Hopf, Fredholm, compensation, or
residue reconstruction. Its main application is auditing method choice and
transfer limits for two-queue polling, especially the mixed gated/1-limited
interface A006. It does **not** solve A006 or establish its literature status.

Use a documented theorem only in the model and interface of its source card.
For a published source, verify the citation and cited statement; for a preprint,
verify the active claim and the proof steps actually used. Keep source-card gaps
and open transfers as research leads. See [evidence and local
attachments](../math-research/references/evidence.md).

## Exact trigger and intake

Before transforming anything, write down the state, observation epoch,
transform type, transition/generator model, stationarity hypothesis, every
unknown interior/axis/origin/phase transform, and the analytic domain.  Never
identify different observation epochs without a proved Palm or arrival-epoch
identity.  A stationary-mass expansion with signed geometric weights is not a
PGF.

For a candidate lattice PGF, require nonnegative Taylor coefficients, integer
support, and mass one. A normalized completely monotone LST need only represent
a measure on \(\mathbb R_+^2\), not on \(\mathbb Z_+^2\).

## Choose the first established branch

| Observed structure | Branch | Required gate |
| --- | --- | --- |
| Embedded chain or CTMC | Derive the phase- and epoch-specific FE | Enumerate interior, axes, origin, and phases from transitions/generator. |
| Polynomial kernel with boundary functions | Kernel trace/cancellation | Common domain, root branch, multiplicity, and vanishing boundary numerator. |
| Kernel curve joining traces | Continuation/identity | Curve lies in the common domain; traces continue on a connected uniqueness set. |
| Oriented-contour jump/shift | RH/shifted RH | Contour/orientation, two domains, jump or shift, index, endpoints, singularities, normalization. |
| One-variable factorization | Wiener--Hopf | Zero/pole domains, nonvanishing, index, factor normalization. |
| Integral equation | Fredholm | Function space plus compactness/index alternative or stated-norm contraction. |
| Geometric stationary-mass expansion | Compensation | Feasible roots, residual axis closure, convergence, and normalization in that model. |
| Meromorphic residue reconstruction | Partial fractions/state extraction | Continuation, complete pole/residue list, and global complex growth eliminating the entire remainder. |

If a gate fails, stop and state the missing hypothesis. Do not substitute a
nearby model's FE, contour, compensation series, or workload LST.

## Non-negotiable checks

1. Derive the equation at its named epoch and keep empty-axis, origin, and
   phase terms. In A006 the 1-limited and gated boundary terms are mandatory;
   see the detailed formulas below.
2. For \(K F=A\), retain all boundary functions in \(A\); cancellation must
   have the correct multiplicity and local holomorphic divisibility. A kernel
   zero or Vieta relation alone proves neither a pole nor probabilisticity.
3. For RH/Wiener--Hopf/Fredholm, specify the actual analytic spaces and
   normalization. A formal relation or a solution of an auxiliary integral
   equation is not automatically a PGF solution.
4. Substitute the reconstructed object into the original FE and check domain,
   \(F(1,1)=1\), coefficientwise nonnegativity, integer support, and the
   original balance equations. Numerical truncations are diagnostics only.

Detailed branch procedures, exact A006 formulas, positive examples, and all
source-specific exclusions are in [model branches and
derivations](references/model-branches-and-derivations.md). That reference is
part of this skill: use it whenever a branch is selected.

## Scope and unresolved work

The installed evidence admits source-specific G09.01--G09.03 FE/kernel,
continuation, and RH interfaces, plus the admissibility counterexamples of
G09.06. It does not provide a general Wiener--Hopf or Fredholm PGF solution
route, a generic conversion from analytic solution to probability law, or an
A006 solution. Full bidisc continuation, nonzero-index RH solvability,
global-growth residue reconstruction, compensation-series convergence outside
each source's stated region, and coefficientwise positivity after
reconstruction remain open gates.

## Supporting references

- [Method and source notes](references/method.md)
- Exact mathematical evidence: `references/math-evidence.md`
- Frozen source index: `references/source-index.md`
- [OpenAI rooted planar-map corner substitution](references/wave4-pa2-rooted-corner-substitution.md)
