# Wave 4 PA3: annular screening and single-bit planar transfer references

## Exponential decay in two-dimensional classical O(n) models

Source SHA-256 `9c94c692eda095e40eac070fba05a3e5340b023e9afb4ce873cefa4d5a361c66`, physical pp. 4--12, Lemma 2.1, Proposition 2.2, Lemma 3.2, and Proposition 3.1.  For a finite pinned S2 spin graph and edge forms, the response form
\[
R(h,k)=-D^2W(hc,kc)
\]
is gradient-invariant and satisfies `R(h,\bar h)\le\beta\|h\|_2^2`.  A finite family `f_i` obeys the fourth-order rotation inequality
\[
R(Q,\bar Q)\le(6\beta^2+4\beta^{3/2}+\beta)\|T\|_{HS}^2+
\beta\sum_{i,j}\min\{\|f_i\|_\infty^2\|df_j\|_2^2,\|f_j\|_\infty^2\|df_i\|_2^2\}.
\]
The multiscale annular Fourier family has `\lambda_N\gtrsim\log N`, cost `O(1+\log N)`, and yields the uniform twist estimate `\min_tZ(t)/\max_tZ(t)\ge1-C_\beta/\log N`.  This feeds pinning, annular crossing suppression, and a coarse-path union bound.

**Scope.** Scoped reference. It requires the finite S2 ferromagnetic graph, stated pinned boundary gauge, nonnegative bounded strengths, and the source's component-conditioning step before extension to O(n).  It is not an iid percolation theorem.

## A Pivotal Amplitude for Voronoi Percolation from Cardy's Formula

Source SHA-256 `50c54704fe210d89ed392432d8b3e61c9d950c6a1d6dd171169362a41ce5d305`, physical pp. 5, 8, and 35, Proposition 2.2, the four-wall transfer identity, and Corollary 6.7.  Screened arm probes retain an arm test after the last failed screen and pay a summable geometric-scale error.  The reference accepts fixed-scale joint crossing/SLE6 convergence and mesh-first four-/six-arm exponents.  Across an annulus, the signed black-versus-white cap difference is transmitted exactly when all four interfaces traverse; otherwise it vanishes.  On zero-mass messages, successful ratio-L block transfer gives
\[
\|M(u\wedge v)\|_\pi\le C(s/r)^{-2\lambda-\nu'}\|u\|_r\|v\|_r.
\]

**Scope.** Scoped reference. It requires the stated Cardy/SLE6 and arm inputs, good deterministic mesh sequence, prescribed screen buffers, successful intermediate seams, and zero-mass message norms.  No contraction through a failed cut is asserted.

## From critical crossings to quenched near-critical universality in Voronoi percolation

Source SHA-256 `164f1043f61eb5e74b7aabbc0a21d9c58783af253dc37b6a76288b7844d1a922`, physical pp. 8 and 47--51, Proposition 2.4 and Lemmas 6.1, 6.3--6.5.  Efron--Stein resampling is paired with arm screens.  At fixed annular scales, guarded alternating arms have conditional probability at least `cA_e(l,L)`.  A four-run necklace transports exactly one black/white connection bit; with an inside/outside exchange, any crossing whose quad contains the trial disk depends on its interior only through that bit, while disjoint quads are unchanged.  This is the source's signed relative-replacement interface.

**Scope.** Scoped reference. It requires typical local geometry, guarded landing patches, finite buffered trial annuli, the specified insertion histories, and the source's quenched arm and RSW inputs.  It neither proves those inputs nor licenses an arbitrary interior exchange.

## 固定来源

- 物理页 4, 5, 6, 7, 8, 9, 10, 11, 12。Lemma 2.1; Proposition 2.2; Lemma 3.2; Proposition 3.1 SHA-256 `9c94c692eda095e40eac070fba05a3e5340b023e9afb4ce873cefa4d5a361c66`。[Exponential decay in two-dimensional classical O(n) models](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Exponential-decay-in-two-dimensional-classical-On-models-September-23-2026/paper.pdf)
- 物理页 5, 8, 35。Proposition 2.2; four-wall transfer identity; Corollary 6.7 SHA-256 `50c54704fe210d89ed392432d8b3e61c9d950c6a1d6dd171169362a41ce5d305`。[A Pivotal Amplitude for Voronoi Percolation from Cardy's Formula](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/A-Pivotal-Amplitude-for-Voronoi-Percolation-from-Cardys-Formula-October-5-2026/voronoi-pivotal-amplitude.pdf)
- 物理页 8, 47, 48, 49, 50, 51。Proposition 2.4; Lemmas 6.1, 6.3--6.5 SHA-256 `164f1043f61eb5e74b7aabbc0a21d9c58783af253dc37b6a76288b7844d1a922`。[From critical crossings to quenched near-critical universality in Voronoi percolation](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/From-critical-crossings-to-quenched-near-critical-universality-in-Voronoi-percolation-October-5-2026/critical-crossings-quenched-near-critical-universality-voronoi-percolation.pdf)
