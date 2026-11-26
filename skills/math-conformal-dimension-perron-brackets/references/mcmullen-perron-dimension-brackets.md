# Perron-root brackets for conformal-dimension calculations

## Verified source scope

Curtis T. McMullen, *Hausdorff Dimension and Conformal Dynamics III: Computation of Dimension*, American Journal of Mathematics 120(4) (1998), 691--721, DOI `10.1353/ajm.1998.0031`. The inspected revised author manuscript has SHA-256 `4d171e6886871c1ba706f4af205e744c2b024f6cfc20ea66ab4dedc45d651991`.

Physical PDF pp. 7--10 define a finite expanding Markov partition, the inverse-derivative transition matrix, and prove the Perron-root enclosure. The proof uses an invariant density of dimension `delta`, a finite Markov graph, and derivative extrema on every directed block. It does not construct those data for an arbitrary map.

## Certified finite interface

For each directed block `i -> j`, provide strictly positive certified bounds

\[
 S_{ij}\leq |f_i'(x)|^{-1}\leq U_{ij}\quad(x\in P_i\cap f_i^{-1}(P_j)),
\]

and put zero in both matrices on absent edges. If the partition is expanding and supports an invariant density of dimension `delta`, the source proves

\[
 \rho(S^\delta)\leq 1\leq\rho(U^\delta).
\]

The positive roots of `rho(S^s)=1` and `rho(U^s)=1` therefore give rigorous lower and upper bounds for `delta` in the order determined by entrywise monotonicity. Bounds obtained from sample derivatives alone are not certified.

Under a `C^2` expanding partition, refinements shrink at an exponential rate and the source proves convergence of the bracket. The printed high-precision numerical tables are explicitly labelled empirical unless derivative extrema are bounded rigorously.

## Required caller evidence

Supply the finite Markov partition and transition graph; an expansion metric and constant; interval proofs for every derivative bound; and a verified Perron-root/root enclosure. Without all four, this is only a numerical estimate, not a dimension certificate.

## Exact finite Perron-direction helper

`scripts/perron_ratio_bounds.py` applies the elementary Collatz--Wielandt
inequality to a finite nonnegative rational matrix `A` and a strictly positive
rational vector `v`:

\[
 \min_i\frac{(Av)_i}{v_i}\leq\rho(A)\leq
 \max_i\frac{(Av)_i}{v_i}.
\]

Thus a lower ratio bound strictly above one certifies `rho(A)>1`, and an
upper ratio bound strictly below one certifies `rho(A)<1`, without floating
point eigenvalues. Only after the caller has supplied the preceding expanding
Markov and entrywise-powered-weight prerequisites may these strict signs be
combined with Perron-root monotonicity to compare a tested exponent with the
unknown dimension. The helper intentionally does not name or compute such a
dimension.
