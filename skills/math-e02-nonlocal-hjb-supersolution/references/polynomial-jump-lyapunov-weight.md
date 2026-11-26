# Polynomial Lyapunov weight for finite-intensity jump generators

## Source and scope

D. Liang and Q. Meng, *Viscosity Solutions of Stochastic Hamilton--Jacobi--
Bellman Equations with Jumps*, arXiv:2605.20593v1, 20 May 2026. The supplied
31-page preprint is used at physical pp. 4--5 and 29.

This note isolates the elementary Lyapunov calculation in Lemma 5.13. It does
not adopt the preprint's later weak-comparison or uniqueness route.

## Callable conditional lemma

Let `p >= 2` and `phi(x) = 1 + |x|^p`. Consider a controlled jump generator
with linear-growth drift, bounded diffusion, and compensated jump displacement
`g` satisfying

`|g(t,e,x,u)| <= rho(e) (1 + |x| + |u|)`.

For a compact control set, or more generally after replacing the control bound
by an explicit uniform bound, suppose

`integral_E (rho(e)^2 + rho(e)^p) nu(de) < infinity`.

Taylor's integral remainder and the derivative bounds for `phi` give

`sup_u L^u phi(x) <= C_phi phi(x)`.

The constant depends on the linear-growth and diffusion constants, `p`, the
control bound, and the displayed rho-moment. The calculation supplies a weight
for a separately established nonlocal HJB comparison or envelope argument.

## Boundary

The source assumes a finite-intensity Poisson measure and the stronger
integrability `integral_E exp(rho(e)) nu(de) < infinity`. The displayed lemma
only needs the stated polynomial moments, but it still requires the generator's
compensation convention and enough integrability for the Taylor remainder.
It does not repair the source's invalid conversion of L2 approximation to an
L-infinity essential-supremum estimate, and therefore does not establish the
source uniqueness theorem.
