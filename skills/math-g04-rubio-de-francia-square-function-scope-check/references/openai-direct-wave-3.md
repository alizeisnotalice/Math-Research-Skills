# Buffered refined decoupling with a common time slab

Source: *Endpoint pointwise convergence for the Schrodinger equation in higher dimensions*, family 080, SHA-256 `4f859efa28f227ff69181aaf307e445839b3455fc2df49da5062e01ed5e3ff34`, [official PDF](https://raw.githubusercontent.com/openai/math/3344da59991ed94f9ba711217b29c1d760badfa6/preprints/Endpoint-pointwise-convergence-for-the-Schrodinger-equation-in-higher-dimensions-September-24-2026/paper.pdf), physical pp. 8--13, Lemma 2.5 and Proposition 2.6.

1. Input \(R\ge2\), a fixed padded time slab of length \(O(R)\), labelled tubes with globally separated intercepts, bounded-overlap cap colors, and functions with the displayed parabolic Fourier support and exterior-tail bound.
2. Require a transverse support-to-count margin \(a+1/2\le b\), count only the uncut strips \(bT\), and let every unit \(R^{1/2}\)-cube in the interior meet at most \(M\) counted tubes.
3. Apply weighted positive-definite \(\ell^2\) decoupling after coarse-cap grouping and parabolic rescaling; carry the common slab, collar, lattice class, and count through every scale. Output the source's refined \(L^p\) estimate with factor \(R^\varepsilon M^{1/2-1/p}\), then atomize only under the same collar convention.

Boundary: this reference is not ordinary Rubio de Francia for arbitrary intervals. Clipping strips before overlap counting, dropping the common slab, or weakening the half-unit collar invalidates the supplied interface.
