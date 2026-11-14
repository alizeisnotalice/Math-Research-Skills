# Positive example: state an invariance transfer with its inputs

**Request:** “Can I replace the Boolean cube by Gaussians to estimate a degree-(d) PTF's noise stability?”

**Good workflow:**

1. Write the PTF as (f(x)=\mathrm{sgn}(Q(x))) on the uniform cube and state (\mathbb E[Q^2]), degree (d), and the normalization used for \(\mathrm{Inf}_i(Q)\).
2. Check \(\max_i\mathrm{Inf}_i(Q)\le\tau\), moment matching, and the ensemble hypercontractivity required by the chosen MOO theorem.
3. Smooth the sign threshold (or truncate/smooth (Q)) and account for the removed high-degree tail.
4. Bound the probability that the Gaussian polynomial lies near zero; only then transfer the smooth expectation back to sign/noise stability.
5. State the error dependence on (d,\tau,\epsilon), and the small-ball step. If those parameters are unavailable, report a qualitative transfer or a gap, not an explicit bound.

This is an invariance argument. If the input is instead an arbitrary k-wise independent Gaussian vector, state that joint-law condition and use a bounded-independence theorem such as Kane's; invariance does not itself impose or characterize k-wise independence.
