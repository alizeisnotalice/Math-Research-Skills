# Strict E-function logarithm admission gate

Source: Stéphane Fischler and Tanguy Rivoal, *Transcendence of values of logarithms of E-functions*, **Mathematische Annalen** 394 (2026), Article 12, DOI `10.1007/s00208-026-03374-z`. Local published PDF SHA-256 `86669c0103d2a589c9a45970734a9ebac47c737382c015fa026b546960c0301d`; physical PDF pp. 1, 3--4.

**Scoped reference.** Let `f in Q[[z]]` be a strict E-function and let nonzero rational `xi` satisfy `f(xi)>0` and `ln(f(xi)) notin Q`. Theorem 2 states that there are effective `c,d>0` such that, for every `(a,b) in Z x N_{>0}`,
\[
 \left|\ln(f(\xi))-\frac ab\right|\geq \exp(-c b^d).
\]
The source reduces this to lower bounds for `f(xi)-exp(a/b)` and invokes a quantitative linear-independence measure only after one has specified a strict E-function system `Y'=AY`, its common denominator `T`, a regular rational evaluation point, and height/coefficient controls.

For an Euler--Mascheroni candidate, this is an admission gate, not a route to a conclusion: separately prove that the proposed number is exactly `ln(f(xi))`, that `f` is strict with rational coefficients, that `xi` is non-singular and rational, that `f(xi)>0`, and that irrationality is independently available before applying Theorem 2. It does not apply merely from a recurrence, an E-operator label, or an extended-E expression containing logarithms.
