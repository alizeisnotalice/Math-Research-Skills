# Exact SDP for piecewise SOS-convex moment optimization

## Source and scope

X. Huang, S. Li, and S. M. Robinson, *Piecewise SOS-Convex Moment
Optimization and Applications via Exact Semi-Definite Programs*, EURO Journal
on Computational Optimization 12 (2024), article 100094,
DOI 10.1016/j.ejco.2024.100094. The checked e-print is arXiv:2402.07064v6.
Physical pp. 5--10 are used.

The result concerns a probability-measure moment problem whose objective has
the source form `min_k max_l g_{k,l}`, with SOS-convex polynomial pieces on a
compact projected spectrahedron. It is a conditional exact equality, not a
generic numerical SDP recovery claim.

## Callable conditional result

First certify all of the following:

- the support has the source's projected-spectrahedron form and is compact;
- its LMI has a strict feasible lift;
- each objective piece and moment function is SOS-convex;
- the source's interior moment condition holds and the primal has a
  minimizer.

Theorem 2.4 converts nonnegativity of every fixed-`k` max-SOS-convex branch
into PSD matrices, simplex weights, and an SOS Gram identity. Theorem 3.4
then combines that representation with conic strong duality to prove
`min(P) = max(D)`, where `D` is the explicitly displayed SDP.

## Boundary

The later measure-recovery theorem has additional conditions beyond Theorem
3.4. In particular, a floating-point Gram matrix is only a candidate: retain
exact SOS coefficient identities, PSD certificates, the support Slater
witness, and every recovery-specific sign and duality condition before
claiming a recovered optimal measure.
