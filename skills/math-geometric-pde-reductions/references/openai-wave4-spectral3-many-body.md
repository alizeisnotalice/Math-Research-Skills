# Scoped OpenAI many-body interfaces (wave4 spectral-3)

The three source routes below are conditional on their named Hamiltonians,
scalings, and imported estimates.  They are not generic Bose-gas or Coulomb
atom results.

## Priced Coulomb sectors and conditional Thomas--Fermi fields

*Generalized ionization energies for full Coulomb atoms* ([pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Generalized-ionization-energies-for-full-Coulomb-atoms-September-24-2026/paper.pdf), SHA-256 `1450c11be0743629e3d65fc8318c005fee278d61019f5021d2383b697ac787e8`, physical pp. 5--10, 14, 16, 19, 24--33) uses the full Coulomb Hamiltonian with two spin states, `P(lambda)=min_n(E_n+lambda n)`, and the scaling `lambda=s^{-4}`, `s->0`, `Zs^3->infinity`.

The reusable bookkeeping interface is: Lemma 2.1 restricts strictly bound minimizing sectors and supplies the localization multiplier identity; Lemma 2.2 applies its local-field comparison only to an unshifted delta-state and cuts satisfying its displayed support, scale, and gradient budgets.  Lemma 2.5 obtains an exterior occupation bound by shell localization and biasing with the shell weight, not by an unconditioned density bound.  Given the nested observation sigma-fields and kernels (3.1)--(3.3), the source builds the local variational density through (3.17), then its conditional barrier invariant in Proposition 4.1.  The stated limiting charge/profile identification is a further subsequential construction, so retain all priced-sector, scale, conditioning, and exceptional-mass conditions.

## Hard-sphere depletion and momentum distribution

*Quantum Depletion and Momentum Distribution in the Dilute Hard-Sphere Bose Gas* ([pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Quantum-Depletion-and-Momentum-Distribution-in-the-Dilute-Hard-Sphere-Bose-Gas-October-5-2026/Quantum-Depletion-in-the-Dilute-Hard-Sphere-Bose-Gas.pdf), SHA-256 `9e8a9907a3ac08117a26db2543c06ee2d1a232319ad4d12ae579f4fd46396133`, physical pp. 3--6, 8, 10--11, 33, 43, 51, 76) fixes its hard-sphere scaling and ordered limits before using the ground-state multiplier calculation and companion count/energy estimates.  The usable method is a source-specific order of operations: establish the finite-volume lower/upper energy accounting, invoke the stated stationary killed-path law, control deletion and folded-path errors, and only then pass to the limiting momentum statement.  Each passage depends on the hard-sphere boundary/domain convention and the cited companion inputs; neither a generic repulsive potential nor a changed order of thermodynamic/dilute limits qualifies.

## Fixed bounded repulsive potentials

*Quantum Depletion for Fixed Bounded Repulsive Potentials* ([pinned PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Quantum-Depletion-for-Fixed-Bounded-Repulsive-Potentials-October-5-2026/fixed-repulsion-quantum-depletion.pdf), SHA-256 `808cf0e274a8852cd16dd3048da2cdbb62feeacaca6c2d332140ea6a95d6e0a9`, physical pp. 1--3, 8--10, 13, 17--19) assumes the paper's nonnegative bounded radial potential, scattering normalization, and ordered limiting regime.  Proposition 3.1 is the central source interface: it combines imported Lee--Huang--Yang/local-box inputs with a positive-remainder box estimate.  The continuation uses the constrained box estimate to transfer the required moments and occupations.  Thus report the potential class, box size/particle-number constraint, and which imported energy estimate is actually available; do not transfer its depletion formula to unbounded, sign-changing, nonradial, or differently scaled interactions.
