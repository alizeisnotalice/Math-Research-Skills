# Common-truncation oscillation packing

Source: *Riesz transforms and uniform rectifiability in higher codimension*, family 081, SHA-256 `8445a9b1c8e5a4c3bc3f2b5a95fbcfab782f3b81db567bf2ea74f5b5325d5688`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Riesz-transforms-and-uniform-rectifiability-in-higher-codimension-September-24-2026/paper.pdf), physical pp. 10--12, Lemma 2.1 and Proposition 2.2.

For a finite selected dyadic family, choose compact mean-zero Lipschitz tests and witness directions. First establish the weighted Bessel bound from support overlap, scale counting, cancellation, and AD-regular cell masses. Then fix one outer ball around the top cube and choose one positive hard truncation only after selection; use that same truncation for every fine selected cube. The kernel-tail comparison reduces the witnesses to pairings with the restricted operator, so Bessel plus the assumed \(L^2\) hard-truncation bound gives the packing sum.

Input must explicitly include the finite family, one outer ball, common truncation, test supports, Lipschitz/cancellation constants, AD bounds, and the hard-truncation \(L^2\) bound. Output is a Carleson-mass inequality for that family.

Boundary: cellwise or scale-dependent truncations are not interchangeable with the common-truncation argument. This reference does not prove uniform rectifiability or the global Riesz-transform theorem.
