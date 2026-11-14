# Negative pattern: a.s.-finite is not enough for optional stopping

For simple symmetric random walk from zero, T=inf{n:S_n=1} is a.s. finite and S_T=1, so E[S_T]=1 while E[S_0]=0. Every bounded stop T∧N still has E[S_{T∧N}]=0: negative values on paths that have not yet hit +1 cancel the stopped value. That cancellation disappears in the a.s. limit because the stopped family is not uniformly integrable.

Exact enumeration in evidence/W02/examples/exact_enumeration.py verified the finite-horizon expectation and survival contribution for N=1,…,10. It does not prove recurrence or the general optional-stopping theorem. State a valid optional-stopping condition or prove the needed UI; never infer expectation preservation from T<∞ a.s. alone.


Do not copy a scalar-component Riesz constant into the vector ℓ² norm: S024's scalar sharp estimate gives a dimension-dependent componentwise bound and a lower benchmark, not the sharp dimension-free C207 constant. Likewise, do not apply the S031 half-space martingale-problem theorem to a conditioned unbounded-path model without checking its inward-drift, coefficient-Hölder, ellipticity and growth assumptions and separately proving tightness under the conditional law.


For A007, f.d.d. convergence or a renewal law of large numbers alone is insufficient for Aldous Proposition 1.2/2.2: the first route is for martingales with fixed-time UI and a continuous limit; the second requires a uniform two-sided stopping-time condition. Neither theorem supplies renewal-age tightness or a polling waiting-time limit.
