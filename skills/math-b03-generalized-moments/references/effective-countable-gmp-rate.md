# Effective countable GMP relaxation rate

## Source and scope

L. Gamertsfelder and B. Mourrain, *The Effective Countable Generalized
Moment Problem*, arXiv:2501.09385v4, dated 1 September 2025. The supplied
27-page preprint is used at physical pp. 8--10.

This is a conditional rate result for the source's countable generalized
moment problem and its Moment--SOS hierarchy. It is not a finite-dimensional
GMP routine and does not turn a numerical SDP solution into a rate or an
optimizer certificate.

## Callable conditional result

Use this result only after the caller has certified all of the following in
the notation of the source:

- Assumptions 1.3, 1.9 and 2.1, including a positive direction `w`, a dual
  optimizer `v*`, and the applicable effective Positivstellensatz constants;
- the countable constraint map, cone, support descriptions and degree
  truncations; and
- Proposition 1.8 strong duality for the target GMP.

For `v_epsilon = v* - epsilon w`, the source proves strict positivity of
`q = f - h.v_epsilon` using
`q_min >= epsilon min_i (h_i.w) > 0`. Applying its effective
Positivstellensatz at the displayed degree threshold makes `v_epsilon`
feasible for the truncated dual. Theorem 2.4 then gives
`0 <= d* - d*_ell <= kappa ell^(-theta)`, and Corollary 2.5 transfers the
same upper bound to the primal value gap.

## Boundary

The theorem does not itself verify the three assumptions, dual attainment,
strong duality, or Positivstellensatz constants. The source's later full
optimizer-convergence statement has the additional unique-minimizer gate;
without uniqueness, value convergence or truncated feasible-set control must
not be restated as convergence of arbitrary selected optimizers.
